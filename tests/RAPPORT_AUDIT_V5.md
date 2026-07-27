# Rapport d’audit V5

## État public observé le 27 juillet 2026

- page d’accueil riche mais affichée comme un document linéaire ;
- grands espaces blancs autour des images ;
- onze produits empilés dans une colonne ;
- liens d’action peu visibles ;
- sélecteur de langue positionné sur `en` ;
- boutons `Buy now` et `Add to cart` ;
- mention `VAT excluded` ;
- fiches produit natives fonctionnelles avec galeries complètes ;
- prix papier affiché à 10 € ;
- Pack Découverte affiché à 40 €.

## Cause du premier échec CSS

En édition TinyMCE normale, be-BOP a retiré la balise `<style>`. Le HTML public
du CMS de test ne contenait plus que le `<div>`.

Après activation de **Use advanced HTML edition**, le badge de connexion a été
affiché. La feuille GitHub Pages peut donc être chargée sans modifier
`src/app.html`.

## Réponse de la V5

- import CSS intégré dans chaque CMS ;
- thème natif documenté pour les pages sans import ;
- héros immersif et sections pleine largeur ;
- grilles responsive pour les produits ;
- boutons, cartes, extraits et avis hiérarchisés ;
- header et footer harmonisés ;
- onze blocs éditoriaux sous les fiches produit ;
- ISBN présents dans chaque fiche ;
- retour arrière possible depuis l’administration.

## Dépendances restantes dans be-BOP

- sélectionner le français comme langue réellement utilisée ;
- configurer le thème natif ;
- créer et affecter les tags ;
- vérifier les sliders d’avis ;
- installer les CMS en mode avancé ;
- ajouter les blocs après produit ;
- compléter les mentions légales, CGV et confidentialité.
