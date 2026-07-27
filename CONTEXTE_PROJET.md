# Contexte — Refonte be-BOP LPLDF

## Projet

Boutique officielle de la saga jeunesse illustrée **Les Petites Leçons de
Frédéric**.

- Boutique : https://xn--lespetitesleonsdefrdric-89b1db.fr/
- Atelier et canon : https://github.com/OxScuba/Atelier-LPLDF
- Thème : https://github.com/OxScuba/LPLDF-Bebop-Theme

## Objectif

Transformer le rendu générique de be-BOP en boutique éditoriale immersive :

- bleu encre, crème papier, or chandelle et vert sauge ;
- village et personnages au centre de l’expérience ;
- hiérarchie visuelle claire et parcours d’achat raccourci ;
- vraies grilles de produits, cartes, extraits et mini-jeux ;
- fiches produit à double niveau de lecture ;
- animations discrètes et accessibilité mobile ;
- Pack Découverte mis en avant.

## Contrainte technique résolue

Version be-BOP :

`885a5ddec4e7f47cec0d52bd0ef9132706350e87`

La source `src/app.html` se trouve dans un dossier partagé par deux instances
be-BOP. Elle ne doit pas être modifiée.

GitHub Pages sert la feuille :

https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css

Chaque CMS charge cette feuille depuis le mode **Use advanced HTML edition**.
Le test public `test-css-lpldf` a confirmé que cette méthode fonctionne. En
mode TinyMCE normal, be-BOP supprime la balise `<style>`.

## Données commerciales retenues

- tomes papier T00 à T10 : 10 € chacun ;
- Pack Découverte T00–T04 : 40 € ;
- Pack Liberté et responsabilité T05–T09 : 45 € ;
- Collection T00–T10 : 90 € ;
- albums carrés d’environ 15 × 15 cm ;
- 38 pages ;
- lecture dès 7 ans.

## Images disponibles

- panoramas du village avec et sans personnages ;
- quatuor et portraits de Fred, Lina, Tom et Milo ;
- scène et mini-jeux T00 ;
- scène, trois doubles pages et mini-jeux T01 à T04 ;
- trois doubles pages T05 ;
- couvertures des produits ;
- QR Lightning.

Les images manquantes de T06 à T10 ne doivent pas être promises dans les pages
avant leur création.

## Règle de reprise

Avant toute modification, lire :

1. `README.md`
2. `CONTEXTE_PROJET.md`
3. `CHANGELOG.md`
4. `docs/INSTALLATION_PAS_A_PAS.md`
5. le CMS ou la fiche produit concernée

Ne jamais publier de secret, accès SSH, donnée client ou fichier `.env`.
