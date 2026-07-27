# Installer les guides interactifs — version 5.7

## 1. Publier les fichiers GitHub Pages

Remplacer le dépôt local par le contenu de l’archive, valider, puis pousser :

```bash
cd ~/Documents/LPLDF-Bebop-Theme
python3 tests/validate_package.py
git add -A
git commit -m "Ajout des guides interactifs de l’Univers v5.7"
git push
```

Attendre ensuite que cette adresse affiche le nouveau CSS :

`https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css`

## 2. Remplacer la page Univers dans be-BOP

Dans **Merch → CMS**, ouvrir la page **Univers** :

1. conserver le titre et le slug actuels ;
2. activer **Use advanced HTML edition** ;
3. cocher **Display raw HTML** si l’option apparaît ;
4. remplacer tout le champ **Raw HTML** par le contenu de `cms/Univers.html` ;
5. enregistrer.

Les quinze nouveaux portraits ont déjà leurs slugs définitifs dans le fichier.
Aucun nouvel envoi d’image n’est nécessaire.

## 3. Contrôler le résultat

- cliquer successivement sur Bastiat / Fred, Thomas d’Aquin, Locke et Scuba
  Wizard ;
- vérifier que chaque fiche remplace l’écran par une visionneuse et qu’aucun
  grand portrait ne reste dans le flux normal de la page ;
- fermer avec la croix, puis avec un clic hors de la fiche ;
- répéter le test sur téléphone ;
- contrôler que le texte de chaque fiche peut défiler jusqu’à la question finale.

## 4. En cas d’ancien style en cache

Faire un rechargement forcé de la page (`Ctrl` + `Maj` + `R`) ou ouvrir la page
dans une fenêtre privée. Le lien CSS ne doit pas recevoir de suffixe de version :

```html
@import url("https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css");
```
