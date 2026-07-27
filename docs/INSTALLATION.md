# Installation et fonctionnement

## Principe

Chaque page CMS commence par :

```html
<style>
@import url("https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css");
</style>
```

Le navigateur télécharge le fichier `custom.css` publié par GitHub Pages et applique ses règles au contenu de la page.

## Publication du CSS

GitHub Pages doit être configuré sur :

- branche : `main` ;
- dossier : `/ (root)`.

Le fichier servi publiquement est le `custom.css` situé à la racine du dépôt. Les copies placées dans un autre dossier ne sont pas utilisées par cette URL.

Après un `git push`, vérifier :

```text
https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css
```

## Intégration d’un CMS

1. Ouvrir la page dans l’administration be-BOP.
2. Activer l’édition HTML avancée.
3. Remplacer entièrement le HTML brut par le fichier correspondant de `cms/`.
4. Enregistrer.
5. Vérifier la page publique sur ordinateur et mobile.
6. Tester également dans une fenêtre privée afin d’écarter un ancien cache.

## Ordre conseillé pour une mise à jour

1. modifier et valider les fichiers localement ;
2. publier `custom.css` sur GitHub ;
3. attendre que l’URL publique contienne les changements ;
4. mettre à jour les CMS concernés ;
5. effectuer la validation visuelle.

## Cache

GitHub Pages et le navigateur peuvent conserver temporairement une ancienne version du CSS. En cas de doute :

- ouvrir l’URL publique du CSS ;
- rechercher une règle récemment ajoutée ;
- recharger la boutique sans cache ;
- tester en navigation privée.

Les règles indispensables aux interactions sensibles peuvent également être répétées dans le CMS concerné afin de conserver un affichage sûr pendant l’actualisation du cache.
