-- Contrôle trimestriel de cohérence télétravail / restauration — données fictives
-- Tables consolidées sur le trimestre (fichiers mensuels d'avril, mai et juin réunis) :
--   declarations_teletravail(Matricule, Service, Date_teletravail)
--   passages_cantine(Matricule, Date_passage, Heure_entree, Heure_sortie)

-- Détail : jours déclarés en télétravail avec un passage à la cantine le même jour
SELECT t.Matricule,
       t.Service,
       t.Date_teletravail,
       MIN(c.Heure_entree) AS Heure_entree
FROM declarations_teletravail AS t
JOIN passages_cantine AS c
  ON c.Matricule = t.Matricule
 AND c.Date_passage = t.Date_teletravail
GROUP BY t.Matricule, t.Service, t.Date_teletravail
ORDER BY t.Matricule, t.Date_teletravail;

-- Synthèse : collaborateurs en anomalie et nombre de jours concernés
SELECT t.Matricule,
       t.Service,
       COUNT(DISTINCT t.Date_teletravail) AS Jours_en_anomalie
FROM declarations_teletravail AS t
JOIN passages_cantine AS c
  ON c.Matricule = t.Matricule
 AND c.Date_passage = t.Date_teletravail
GROUP BY t.Matricule, t.Service
ORDER BY Jours_en_anomalie DESC;
