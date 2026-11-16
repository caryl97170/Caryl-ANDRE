"""Contrôle trimestriel de cohérence télétravail / restauration — données fictives.

1. Consolide les fichiers mensuels du trimestre (télétravail et cantine).
2. Rapproche les deux sources par collaborateur et par date.
3. Une anomalie = un passage à la cantine un jour déclaré en télétravail.
"""
import glob
import pandas as pd

# 1. Consolidation des trois mois du trimestre
tele = pd.concat(
    [pd.read_csv(f, sep=";", parse_dates=["Date_teletravail"]).assign(Fichier_source=f)
     for f in sorted(glob.glob("teletravail_*.csv"))],
    ignore_index=True,
)
cant = pd.concat(
    [pd.read_csv(f, sep=";", parse_dates=["Date_passage"]).assign(Fichier_source=f)
     for f in sorted(glob.glob("cantine_*.csv"))],
    ignore_index=True,
)

# 2. Préparation : une ligne par collaborateur et par jour
tele = tele.drop_duplicates(["Matricule", "Date_teletravail"])
cant = cant.drop_duplicates(["Matricule", "Date_passage"])

# 3. Rapprochement : jointure sur le matricule et la date
anomalies = tele.merge(
    cant[["Matricule", "Date_passage", "Heure_entree", "Heure_sortie"]],
    left_on=["Matricule", "Date_teletravail"],
    right_on=["Matricule", "Date_passage"],
    how="inner",
)

# 4. Synthèse par collaborateur, base des éventuelles reprises sur salaire
synthese = (
    anomalies.groupby(["Matricule", "Service"])
    .agg(jours_en_anomalie=("Date_teletravail", "count"))
    .reset_index()
    .sort_values("jours_en_anomalie", ascending=False)
)

print(f"Jours de télétravail déclarés sur le trimestre : {len(tele)}")
print(f"Passages à la cantine sur le trimestre         : {len(cant)}")
print(f"Jours en anomalie                              : {len(anomalies)}")
print(f"Collaborateurs en anomalie                     : {len(synthese)}")
synthese.to_csv("collaborateurs_en_anomalie.csv", sep=";", index=False)
