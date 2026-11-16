# Portfolio — Caryl André · Version livrable

**Site Web statique, en français, responsive, prêt à être hébergé.** Aucune base de données, aucun compte technique et aucune dépendance npm nécessaires.

## Contenu livré

- `index.html` : accueil, projets filtrables (Data / Mécanique / Musique & son), parcours, présentation, contact.
- `profil.html` : parcours professionnel complet, expériences AXA et BNP Paribas, formation, compétences, lien CV.
- `projets/` : 5 études de projet (AZMUT BI, YZOCEL Stage, Golf IV TDI, Bakerz Beatz, Sonorisation).
- `media/` : 7 visuels initiaux + 8 captures authentiques d’AZMUT BI et de YZOCEL Stage, recadrées en PNG sans perte.
- `assets/` : styles, interactions JS, favicon, **CV PDF fourni dans la conversation**.

## Tester localement

Ouvrir `index.html` dans un navigateur. Pour tester dans un serveur local (recommandé) :

```bash
python -m http.server 8000
```

Puis ouvrir `http://localhost:8000`.

## Publier sur GitHub Pages

1. Sur GitHub, créer un dépôt public `portfolio` (ou autre nom).
2. À la racine du dépôt, envoyer **le contenu décompressé du ZIP**, et non le ZIP lui-même.
3. Dans le dépôt : Settings > Pages > Build and deployment > Deploy from a branch > `main` > `/(root)` > Save.
4. Une adresse sera ensuite affichée dans Pages, généralement `https://<identifiant>.github.io/portfolio/` pour un dépôt de projet.
5. Mettre **cette adresse réelle** dans CVDesignR et, idéalement, ajouter le lien dans la bio GitHub.

> GitHub Pages ne publie pas automatiquement les modifications conservées uniquement en local : il faut envoyer les fichiers modifiés dans le dépôt.

## Ajouter d'autres photos plus tard

Chaque page possède son dossier dans `media/` :

- AZMUT BI : `media/azmut-bi/` ; page `projets/azmut-bi.html`
- YZOCEL Stage : `media/yzocel-stage/` ; page `projets/yzocel-stage.html`
- Golf IV : `media/golf-iv/` ; page `projets/golf-iv-tdi.html`
- Bakerz Beatz : `media/musique/` ; page `projets/bakerz-beatz.html`
- Sonorisation : `media/sonorisation/` ; page `projets/sonorisation.html`

Pour ajouter une photo, idéalement l'optimiser en `.webp`, la copier dans le bon dossier et ajouter ce bloc dans `<div class="media-grid">` de la fiche projet correspondante :

```html
<figure class="gallery-item">
  <a class="gallery-open" data-lightbox="true" href="../media/sonorisation/nouvelle-photo.webp" aria-label="Agrandir la photo">
    <img src="../media/sonorisation/nouvelle-photo.webp" loading="lazy" decoding="async" alt="Description du contenu réel de la photo">
  </a>
  <figcaption>Description de la réalisation</figcaption>
</figure>
```

La galerie permettra automatiquement l'agrandissement de l'image, sans autre programmation.

### Ajouter un morceau de musique (création originale uniquement)

Placer le fichier dans `media/musique/` et ajouter dans `projets/bakerz-beatz.html` :

```html
<div class="media-tile">
  <h4>Titre de la composition</h4>
  <audio controls preload="none">
    <source src="../media/musique/ma-composition.mp3" type="audio/mpeg">
    Votre navigateur ne prend pas en charge l'audio HTML5.
  </audio>
</div>
```

Ne publier que des fichiers audio que tu es autorisé à diffuser (échantillons ou samples correctement licenciés).

## À vérifier avant de diffuser aux recruteurs

- **CV** : le document sous `assets/cv-caryl-andre-version-fournie.pdf` est le dernier PDF disponible dans la conversation, **pas une version finale corrigée**. Le remplacer par ton CV définitif et garder le même nom de fichier.
- **LinkedIn / GitHub** : aucune URL personnelle réelle n'a été inventée. Ajouter ton profil une fois l'adresse confirmée.
- **AZMUT BI** et **YZOCEL Stage** sont présentés à leur stade de développement/conception, sans inventer de fonctionnalités livrées ni d'utilisateurs.
- Ajouter les photos supplémentaires et captures d'écran qui montrent les travaux réellement réalisés.
- Les photos de mécanique peuvent montrer un lieu privé ; vérifier ce que tu acceptes de rendre public. Le site utilise des images réexportées en WebP sans métadonnées de géolocalisation intégrées.
- Vérifier le libellé officiel du MBA et du Master ainsi que l'usage exact des compétences listées.

## Personnalisation

Le site est en HTML/CSS/JavaScript pur. Couleurs et tailles sont personnalisables dans `assets/styles.css` (variables `:root`).

Aucune plateforme n'héberge encore ce site : le ZIP est une version **prête à déployer**, pas une URL publique existante.

## V4 — Ajout des captures du 16 novembre 2026

Les 8 captures de l’utilisateur ont été **recadrées directement depuis les images sources** : retrait des barres de navigateur, des fenêtres ChatGPT et des éléments de bord, sans recréation du texte ou des chiffres. Les captures ne démontrent pas à elles seules le fonctionnement complet de toutes les fonctionnalités.

## V5 — Captures fidèles (16 novembre 2026)

Cette version remplace les huit fichiers de captures d’écran par des **recadrages en PNG sans perte effectués directement sur les huit captures sources 1920 × 1080**. Aucune IA de génération d’images n’a été utilisée : pixels de l’interface, textes, proportions et couleurs sont strictement identiques à la zone correspondante des originaux. Les seules zones retirées sont les barres d’application/navigateur, les bordures externes et, pour certaines captures de YZOCEL Stage, des marges vides autour de l’écran.

Le fichier `manifest_captures_v5.json` consigne pour chaque capture la source, le rectangle de recadrage et son empreinte SHA-256. Certaines captures ont été prises avec un défilement partiel : les éléments déjà hors champ n’ont pas été reconstitués.


## V6 — Relecture éditoriale avant publication

- Texte de chantier retiré des pages Bakerz Beatz, sonorisation et Golf IV ; aucune photo, démonstration ou fonctionnalité inventée.
- Les 8 captures V5 originales (PNG) sont conservées **octet pour octet**.
- Un index des fichiers et un contrôle de navigation sont disponibles dans `CONTROLES_AVANT_PUBLICATION.md`.
- **À faire avant mise en ligne publique** : remplacer le CV provisoire par sa version définitive ; contrôler l'adresse e-mail visible dans certaines captures ; valider le dépôt GitHub et le nom d’utilisateur sous lesquels publier.
