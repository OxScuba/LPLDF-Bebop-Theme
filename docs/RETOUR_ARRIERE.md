# Retour arrière

## Désactiver immédiatement le thème sur une page

Dans le CMS concerné, retirer uniquement :

```html
<style>
@import url("https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css?v=5.0.0");
</style>
```

Le contenu reste présent, mais reprend l’apparence native de be-BOP.

## Restaurer une page CMS

Avant chaque remplacement, conserver l’ancien contenu dans un fichier local.
Pour revenir en arrière :

1. ouvrir la page CMS ;
2. conserver **Use advanced HTML edition** si la sauvegarde contient du HTML ;
3. remplacer le contenu par la sauvegarde ;
4. enregistrer.

## Restaurer une ancienne feuille CSS

Depuis le dépôt local, recopier une sauvegarde de `versions/` vers
`custom.css`, puis publier le commit. GitHub Pages propage normalement la
modification en quelques minutes.

## Désactiver un bloc produit

Vider la zone **Add CMS code and widgets after product page core** du produit
concerné. La description, le prix, la galerie et le panier natifs restent
intacts.

Ce retour arrière ne demande aucune intervention SSH, aucun redémarrage et
aucune modification du be-BOP partagé.
