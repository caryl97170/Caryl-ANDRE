"""Contrôle de cohérence télétravail / restauration — données fictives.

Rapproche les déclarations de télétravail et les passages à la cantine
par collaborateur et par date. Une anomalie = un passage à la cantine
un jour déclaré en télétravail.
"""
import pandas as pd

tele = pd.read_csv("declarations_teletravail.csv", sep=";", parse_dates=["Date_teletravail"])
cant = pd.read_csv("passages_cantine.csv", sep=";", parse_dates=["Date_passage"])

# 1. Préparation : clé commune (matricule + date), doublons retirés
tele = tele.drop_duplicates(["Matricule", "Date_teletravail"])
cant = cant.drop_duplicates(["Matricule", "Date_passage"])

# 2. Rapprochement : jointure sur le matricule et la date
anomalies = tele.merge(
    cant,
    left_on=["Matricule", "Date_teletravail"],
    right_on=["Matricule", "Date_passage"],
    how="inner",
)

# 3. Synthèse par collaborateur
synthese = (
    anomalies.groupby(["Matricule", "Service"])
    .agg(jours_en_anomalie=("Date_teletravail", "count"),
         premiere_date=("Date_teletravail", "min"),
         derniere_date=("Date_teletravail", "max"))
    .reset_index()
    .sort_values("jours_en_anomalie", ascending=False)
)

print(f"Jours de télétravail déclarés : {len(tele)}")
print(f"Jours en anomalie             : {len(anomalies)}")
print(f"Collaborateurs en anomalie    : {synthese['Matricule'].nunique()}")
synthese.to_csv("collaborateurs_en_anomalie.csv", sep=";", index=False)
