# Installer la page d’accueil V5.1

Cette version corrige deux problèmes constatés sur la page publique :

1. l’import du CSS avait été supprimé par be-BOP ;
2. les widgets `[Product]`, `[TagProducts]` et `[Slider]` découpaient la structure HTML.

La nouvelle page `cms/Home.html` ne contient plus ces widgets. Les cartes sont
en HTML continu et renvoient vers les vraies pages produits.

## 1. Publier le CSS

Remplacer le fichier `custom.css` du dépôt GitHub
`OxScuba/LPLDF-Bebop-Theme` par celui de cette archive, puis valider et pousser
la modification sur la branche `main`.

Attendre une à deux minutes, puis ouvrir :

https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css

Rechercher dans la page :

`V5.1 — composants 100 % HTML`

Si cette phrase apparaît, la nouvelle feuille est publiée.

## 2. Remplacer la page Home dans be-BOP

1. Ouvrir l’administration be-BOP.
2. Ouvrir la page CMS dont le slug est `home`.
3. Cocher **Use advanced HTML edition**.
4. Remplacer tout le contenu par celui de `cms/Home.html`.
5. Conserver **Full screen** activé.
6. Enregistrer.
7. Rouvrir immédiatement la page dans l’administration et vérifier que
   **Use advanced HTML edition** est toujours coché.

L’import doit être exactement :

```html
<style>
@import url("https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css");
</style>
```

## 3. Vérifier sans être trompé par le cache

Ouvrir la boutique dans une fenêtre de navigation privée, puis actualiser une
fois la page.

Les signes qui confirment le bon chargement sont :

- grand bandeau illustré dès le haut de page ;
- titre blanc dans le bandeau ;
- Pack Découverte présenté dans une carte inclinée ;
- grille homogène de onze couvertures ;
- trois avis disposés en cartes.

## 4. Réglages du thème natif

Ils pourront ensuite harmoniser l’en-tête, les boutons, les fiches produits et
le pied de page. Ils ne sont pas nécessaires pour que la composition de la
page Home V5.1 fonctionne.
