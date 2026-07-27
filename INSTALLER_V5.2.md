# Installer la refonte V5.2

Cette version corrige et améliore les éléments constatés sur la page publique :

1. les images demandées en `2048` renvoyaient une erreur 404 ;
2. le mode plein écran supprimait le menu, le panier et le pied de page ;
3. la Home était trop longue avec les onze produits ;
4. la présentation des personnages ne reflétait pas assez leur canon.

La nouvelle page `cms/Home.html` ne contient plus ces widgets. Les cartes sont
en HTML continu et renvoient vers les vraies pages produits.

## 1. Publier le CSS

Remplacer le fichier `custom.css` du dépôt GitHub
`OxScuba/LPLDF-Bebop-Theme` par celui de cette archive, puis valider et pousser
la modification sur la branche `main`.

Attendre une à deux minutes, puis ouvrir :

https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css

Rechercher dans la page :

`V5.2 — sélecteur des quatre aventuriers`

Si cette phrase apparaît, la nouvelle feuille est publiée.

## 2. Remplacer la page Home dans be-BOP

1. Ouvrir l’administration be-BOP.
2. Ouvrir la page CMS dont le slug est `home`.
3. Cocher **Use advanced HTML edition**.
4. Cliquer dans le grand champ **Raw HTML** et remplacer tout son contenu par
   celui de `cms/Home.html`.
5. Décocher **Full screen**. Le menu, le panier et le pied de page natifs
   réapparaîtront, tandis que le CSS conservera les sections sur toute la largeur.
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
- quatre couvertures choisies comme portes d’entrée ;
- sélecteur interactif Fred, Lina, Tom et Milo ;
- trois avis disposés en cartes.

## 4. Installer la page Univers

Appliquer la même procédure à `cms/Univers.html` :

- édition HTML avancée ;
- collage dans **Raw HTML** ;
- **Full screen** décoché ;
- enregistrement puis contrôle public.

## 5. Futurs portraits transparents

Le sélecteur fonctionne immédiatement avec les quatre images déjà importées.
Lorsque les portraits détourés seront prêts, les importer sous les noms :

- `lpldf-fred-transparent.png`
- `lpldf-lina-transparent.png`
- `lpldf-tom-transparent.png`
- `lpldf-milo-transparent.png`

Noter les quatre slugs retournés par be-BOP. Il suffira ensuite de remplacer les
quatre URL correspondantes dans `cms/Home.html`. Aucun changement de structure
ou de CSS ne sera nécessaire.
