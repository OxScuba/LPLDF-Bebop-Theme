<h1 align="center">Boutique des Petites Leçons de Frédéric</h1>

<p align="center">
  <strong>Des histoires pour apprendre à penser librement.</strong><br>
  Thème visuel, pages éditoriales et données de publication de la boutique be-BOP consacrée à la saga jeunesse <em>Les Petites Leçons de Frédéric</em>.
</p>

<p align="center">
  <img alt="be-BOP" src="https://img.shields.io/badge/boutique-be--BOP-183247?style=flat-square">
  <img alt="CMS HTML" src="https://img.shields.io/badge/CMS-HTML_D5A33B?style=flat-square">
  <img alt="CSS" src="https://img.shields.io/badge/thème-CSS-2E7D5B?style=flat-square">
  <img alt="Albums" src="https://img.shields.io/badge/collection-T00–T10-5B2738?style=flat-square">
</p>

<p align="center">
  <a href="https://xn--lespetitesleonsdefrdric-89b1db.fr/">Voir la boutique</a> ·
  <a href="#-architecture">Architecture</a> ·
  <a href="#-mise-à-jour">Mise à jour</a> ·
  <a href="docs/INSTALLATION.md">Installation</a>
</p>

> Un village, quatre aventuriers et des idées qui deviennent visibles à travers leurs conséquences.

## 📚 Le projet

**Les Petites Leçons de Frédéric** est une saga d’albums illustrés destinée principalement aux enfants de 7 à 10 ans, avec une seconde lecture pour les parents et les éducateurs.

Fred, alter ego fictionnel de Frédéric Bastiat, accompagne Lina, Tom et Milo dans des aventures consacrées à la liberté, la responsabilité, la propriété, l’économie, la monnaie et Bitcoin.

Ce dépôt constitue la source de travail de la boutique :

- thème visuel commun publié avec GitHub Pages ;
- pages CMS prêtes à intégrer dans be-BOP ;
- textes et blocs éditoriaux des fiches produit ;
- données des produits, ISBN, tags et SEO ;
- registre central des images et de leurs slugs be-BOP ;
- outils de validation et de génération.

Le dépôt éditorial complet de la saga reste séparé : celui-ci concerne uniquement sa présentation et sa commercialisation sur la boutique.

## 🎨 Identité visuelle

Le thème reprend l’univers des albums :

| Élément | Usage |
|---|---|
| Bleu encre `#183247` | navigation, sections fortes et boutons secondaires |
| Crème `#FFF8E8` | fonds éditoriaux et respiration |
| Or `#D8A83E` | appels à l’action et détails |
| Sauge `#DFE8DC` | sections pédagogiques |
| Georgia | grands titres narratifs |
| Outfit | interface et textes courants |

Le CSS principal est disponible à l’adresse :

```text
https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css
```

## 🗂️ Architecture

```text
LPLDF-Bebop-Theme/
├── cms/                    pages éditoriales de la boutique
├── produits/
│   ├── papier/             descriptions des albums papier
│   ├── packs/              descriptions des offres groupées
│   └── cms-apres-produit/  blocs visuels sous les fiches produit
├── donnees/                ISBN, slugs, tags, SEO et contrôles
├── docs/                   installation et maintenance
├── juridique/              modèles publics à compléter avant usage
├── tests/                  validation statique du dépôt
├── tools/                  scripts de génération et de prévisualisation
├── custom.css              thème réellement servi par GitHub Pages
└── .nojekyll               publication directe des fichiers statiques
```

## 🧩 Pages CMS

Les fichiers de `cms/` correspondent aux pages éditoriales de la boutique :

- Home ;
- La Collection ;
- Quel tome choisir ;
- Univers ;
- Parents & Éducateurs ;
- Ebooks ;
- Avis des lecteurs ;
- À propos ;
- FAQ ;
- Contact ;
- Livraison et retours ;
- Soutenir la collection ;
- Bitcoin ;
- Preuves d’ancrage Timechain.

Chaque CMS importe `custom.css`, puis place son contenu dans un conteneur `.lpldf-page`.

## 🖼️ Images

Le fichier [`donnees/REGISTRE_IMAGES_BEBOP.csv`](donnees/REGISTRE_IMAGES_BEBOP.csv) est la source centrale des images utilisées par le site. Il associe :

- nom de fichier ;
- slug attribué par be-BOP ;
- usage ;
- tome concerné ;
- statut.

Toute nouvelle image doit être ajoutée au registre avant son utilisation durable dans un CMS.

## 🔄 Mise à jour

Après modification :

```bash
python3 tests/validate_package.py
git status
git diff --stat
git add -A
git diff --cached --stat
git commit -m "Décrit précisément la modification"
git push
git status
```

Le fichier réellement publié par GitHub Pages est toujours le `custom.css` situé **à la racine** du dépôt.

Pour le détail, consulter :

- [installation et fonctionnement](docs/INSTALLATION.md) ;
- [remplacement du dépôt local](docs/REMPLACER_DEPOT_LOCAL.md) ;
- [maintenance du dépôt](docs/MAINTENANCE.md) ;
- [architecture des contenus](docs/ARCHITECTURE.md) ;
- [configuration du thème natif](docs/THEME_NATIF_BEBOP.md) ;
- [plan des CMS](docs/PLAN_CMS.md).

## ✅ Validation

Le script de validation contrôle notamment :

- les 14 pages CMS ;
- la structure HTML minimale ;
- les images et textes alternatifs ;
- les liens obligatoires ;
- l’absence de placeholders ;
- les 11 fiches papier et leurs ISBN ;
- les 11 blocs éditoriaux après produit ;
- l’équilibre syntaxique du CSS.

```bash
python3 tests/validate_package.py
```

## 🔐 Hygiène du dépôt public

Ce dépôt ne doit contenir que des ressources publiables :

- aucun identifiant ni secret ;
- aucun accès d’administration ;
- aucune information personnelle ou donnée client ;
- aucun détail d’infrastructure inutile au fonctionnement du thème.

Les fichiers du dossier `juridique/` sont des modèles et doivent être complétés et vérifiés avant publication.

---

<p align="center">
  <strong>Observer. Comprendre. Choisir.</strong>
</p>
