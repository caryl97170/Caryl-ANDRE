"""Contrôle trimestriel de cohérence télétravail / restauration — données fictives.

1. Consolide les fichiers mensuels du trimestre (télétravail et cantine).
2. Rapatrie le matricule sur le fichier cantine, qui ne contient que le nom
   et le prénom (équivalent de la RECHERCHEX faite dans Excel).
3. Rapproche les deux sources par matricule et par date.
4. Une anomalie = un passage à la cantine un jour déclaré en télétravail.
"""
import glob
import pandas as pd

def consolider(motif, colonne_date):
    fichiers = sorted(glob.glob(motif))
    return pd.concat(
        [pd.read_csv(f, sep=";", parse_dates=[colonne_date]).assign(Fichier_source=f) for f in fichiers],
        ignore_index=True,
    )

# 1. Consolidation des trois mois du trimestre
tele = consolider("teletravail_*.csv", "Date_teletravail").drop_duplicates(["Matricule", "Date_teletravail"])
cant = consolider("cantine_*.csv", "Date_passage")

# 2. Rapatriement du matricule à partir du nom et du prénom
referentiel = tele[["Matricule", "Nom", "Prenom"]].drop_duplicates()
nb = referentiel.groupby(["Nom", "Prenom"]).size().rename("Nb_correspondances").reset_index()
cant = cant.merge(nb, on=["Nom", "Prenom"], how="left").fillna({"Nb_correspondances": 0})
uniques = referentiel.merge(nb[nb.Nb_correspondances == 1][["Nom", "Prenom"]], on=["Nom", "Prenom"])
cant = cant.merge(uniques, on=["Nom", "Prenom"], how="left")
cant["Statut_correspondance"] = cant["Nb_correspondances"].map(
    lambda n: "Trouvé" if n == 1 else ("Introuvable" if n == 0 else "Homonyme à vérifier")
)
print(cant["Statut_correspondance"].value_counts().to_string(), "\n")

# 3. Rapprochement sur le matricule et la date (passages identifiés uniquement)
identifies = cant.dropna(subset=["Matricule"]).drop_duplicates(["Matricule", "Date_passage"])
anomalies = tele.merge(
    identifies[["Matricule", "Date_passage", "Heure_entree", "Heure_sortie"]],
    left_on=["Matricule", "Date_teletravail"],
    right_on=["Matricule", "Date_passage"],
    how="inner",
)

# 4. Synthèse par collaborateur, base des éventuelles reprises sur salaire
synthese = (
    anomalies.groupby(["Matricule", "Nom", "Prenom", "Service"])
    .agg(jours_en_anomalie=("Date_teletravail", "count"))
    .reset_index()
    .sort_values("jours_en_anomalie", ascending=False)
)
a_verifier = cant[cant["Statut_correspondance"] != "Trouvé"]

print(f"Jours de télétravail déclarés : {len(tele)}")
print(f"Passages à la cantine         : {len(cant)}")
print(f"Jours en anomalie             : {len(anomalies)}")
print(f"Collaborateurs en anomalie    : {len(synthese)}")
print(f"Passages à vérifier à la main : {len(a_verifier)}")
synthese.to_csv("collaborateurs_en_anomalie.csv", sep=";", index=False)
a_verifier.to_csv("passages_a_verifier.csv", sep=";", index=False)
