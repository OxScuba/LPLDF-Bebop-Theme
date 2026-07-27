# Installation V5.3 pas à pas

## 0. Ce qui est déjà validé

Le CMS `test-css-lpldf` a affiché le badge de connexion lorsque l’option
**Use advanced HTML edition** était activée. GitHub Pages et `@import`
fonctionnent donc avec cette instance.

Ne jamais modifier `src/app.html` : le fichier source est partagé entre deux
boutiques.

## 1. Publier le CSS V5.3

Remplacer le fichier racine `custom.css` du dépôt par celui de cette version,
puis attendre la mise à jour de GitHub Pages.

Contrôler directement :

https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css

Le fichier doit commencer par `DESIGN SYSTEM V5` et contenir
`V5.3 — visionneuse grand format CSS`. Il ne doit plus contenir le badge
`CSS LPLDF connecté`.

## 2. Configurer le thème natif

Dans **Admin > Merch > Themes**, appliquer les valeurs de
`THEME_NATIF_BEBOP.md`. Ce thème reste actif sur le panier, le paiement et les
pages qui ne chargent pas encore `custom.css`.

Dans **Admin > Merch > Layout** :

- langue et interface françaises ;
- masquer le sélecteur de thème ;
- conserver les menus indiqués dans `PLAN_CMS.md` ;
- vérifier logo, favicon, titre et description du site.

## 3. Installer la page d’accueil

1. Sauvegarder le contenu actuel de la page d’accueil.
2. Ouvrir sa configuration CMS.
3. Décocher **Full screen** pour conserver le menu, le panier et le pied de
   page natifs. Le CSS V5.3 maintient malgré tout les sections en pleine largeur.
4. Cocher **Use advanced HTML edition**.
5. Coller l’intégralité de `../cms/Home.html` dans **Raw HTML**.
6. Enregistrer.
7. Recharger la boutique avec `Ctrl + Shift + R`.
8. Contrôler l’ordinateur et le téléphone.

Le passage en édition avancée peut effacer le contenu TinyMCE existant. Ne
cocher cette option qu’après avoir copié le fichier complet à installer.

## 4. Installer les CMS prioritaires

Procéder page par page :

1. `Univers.html`
2. `La_Collection.html`
3. `Quel_tome_choisir.html`
4. `Parents_Educateurs.html`
5. `Avis_des_lecteurs.html`

Pour chaque page :

- sauvegarder l’ancien contenu ;
- décocher **Full screen** ;
- cocher **Use advanced HTML edition** ;
- coller le fichier entier, y compris la balise `<style>` ;
- vérifier les images, widgets, liens et affichage mobile.

## 5. Créer et affecter les tags

Suivre `../donnees/CONFIGURATION_TAGS_ET_WIDGETS.txt`, puis contrôler que
`[TagProducts=livre-papier]` affiche les onze tomes dans une grille.

Tags structurants :

- `livre-papier`, `ebook`, `pack`, `hors-serie` ;
- `saison-1`, `saison-2`, `saison-3`, `collection-complete` ;
- `t00` à `t10`.

## 6. Enrichir les fiches produit

Les descriptions principales restent en texte simple.

Pour chaque tome papier :

1. ouvrir le produit dans l’administration ;
2. repérer **Add CMS code and widgets after product page core** ;
3. coller le fichier HTML correspondant dans
   `../produits/cms-apres-produit/` ;
4. ne pas cocher **Hide on mobile** ;
5. enregistrer et vérifier le rendu.

Commencer par T01. Si son bloc charge correctement le thème et apparaît sous
la description, appliquer la même opération aux dix autres tomes.

Ordre recommandé des galeries :

- T00 : couverture, scène de présentation, mini-jeux ;
- T01 à T04 : couverture, scène, trois doubles pages, mini-jeux ;
- T05 : couverture, trois doubles pages ;
- T06 à T10 : couverture, puis nouveaux visuels lorsqu’ils seront prêts.

## 7. Installer les pages secondaires

1. `FAQ.html`
2. `Livraison_et_Retours.html`
3. `Contact.html`
4. `A_Propos.html`
5. `Ebooks.html`
6. `Bitcoin.html`
7. `Preuves_ancrage_Timechain.html`
8. `Soutenir_la_collection.html`

## 8. Terminer le juridique et le contrôle qualité

Les fichiers de `juridique/` contiennent des champs à compléter. Ne pas les
publier sans vérification.

Terminer avec :

- panier ;
- paiement euros et Bitcoin ;
- frais de livraison ;
- mobile ;
- liens ;
- ISBN ;
- SEO ;
- absence de texte anglais visible.
