# Installer le comparateur de tomes — v5.8

Cette version transforme les dix carrés T01 à T10 de la page « Quel tome
choisir » en fiches consultables sans quitter la page.

## 1. Publier le dépôt

Depuis le dépôt local :

```bash
python3 tests/validate_package.py
git add -A
git commit -m "Ajout du comparateur interactif des tomes v5.8"
git push
```

Attendre ensuite la publication de `custom.css` par GitHub Pages.

## 2. Remplacer le CMS dans be-BOP

Dans l’administration be-BOP, ouvrir la page correspondant au slug
`quel-tome-choisir`.

Activer l’édition HTML avancée, puis remplacer tout le HTML brut par le contenu
du fichier :

```text
cms/Quel_tome_choisir.html
```

Enregistrer la page.

## 3. Vérifier le résultat

Effectuer un rechargement forcé de la page publique, puis contrôler :

- chaque carré T01 à T10 ouvre la bonne fiche ;
- la couverture et les textes correspondent au tome ;
- « Découvrir le Tome » ouvre la bonne fiche produit ;
- les liens précédent et suivant parcourent les dix tomes ;
- la croix et le clic sur l’arrière-plan ferment la fiche ;
- après fermeture, la section de choix reste visible ;
- aucun contenu ne déborde sur téléphone.

Le Tome 00 reste présenté séparément comme porte d’entrée de la saga.
