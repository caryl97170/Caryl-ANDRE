-- Contrôle trimestriel de cohérence télétravail / restauration — données fictives
-- Tables consolidées sur le trimestre (fichiers mensuels d'avril, mai et juin réunis) :
--   declarations_teletravail(Matricule, Nom, Prenom, Service, Date_teletravail)
--   passages_cantine(Nom, Prenom, Date_passage, Heure_entree, Heure_sortie)
-- Le fichier cantine ne contient pas le matricule : on le rapatrie depuis le nom et le prénom.

-- 1. Référentiel des collaborateurs et détection des homonymes
WITH referentiel AS (
    SELECT DISTINCT Matricule, Nom, Prenom FROM declarations_teletravail
),
noms AS (
    SELECT Nom, Prenom, COUNT(*) AS Nb_correspondances, MIN(Matricule) AS Matricule
    FROM referentiel
    GROUP BY Nom, Prenom
),
-- 2. Passages cantine identifiés (correspondance unique uniquement)
cantine_identifiee AS (
    SELECT DISTINCT n.Matricule, c.Date_passage
    FROM passages_cantine AS c
    JOIN noms AS n ON n.Nom = c.Nom AND n.Prenom = c.Prenom
    WHERE n.Nb_correspondances = 1
)
-- 3. Synthèse : collaborateurs en anomalie et nombre de jours concernés
SELECT t.Matricule, t.Nom, t.Prenom, t.Service,
       COUNT(DISTINCT t.Date_teletravail) AS Jours_en_anomalie
FROM declarations_teletravail AS t
JOIN cantine_identifiee AS ci
  ON ci.Matricule = t.Matricule
 AND ci.Date_passage = t.Date_teletravail
GROUP BY t.Matricule, t.Nom, t.Prenom, t.Service
ORDER BY Jours_en_anomalie DESC;

-- 4. Passages à vérifier manuellement : homonymes et noms introuvables
SELECT c.Nom, c.Prenom, c.Date_passage,
       CASE WHEN n.Nb_correspondances IS NULL THEN 'Introuvable'
            ELSE 'Homonyme à vérifier' END AS Statut_correspondance
FROM passages_cantine AS c
LEFT JOIN (SELECT Nom, Prenom, COUNT(DISTINCT Matricule) AS Nb_correspondances
           FROM declarations_teletravail GROUP BY Nom, Prenom) AS n
  ON n.Nom = c.Nom AND n.Prenom = c.Prenom
WHERE n.Nb_correspondances IS NULL OR n.Nb_correspondances > 1
ORDER BY c.Date_passage;
