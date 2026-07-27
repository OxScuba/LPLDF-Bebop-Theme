# Publication dans le dépôt GitHub

## Fichiers à copier à la racine

- `custom.css`
- `README.md`
- `CHANGELOG.md`
- `.nojekyll`
- dossiers `cms/`, `produits/`, `donnees/`, `docs/`, `juridique/`,
  `versions/` et `tests/`

## Commandes

Depuis le dossier local du dépôt :

```bash
cd "$HOME/Documents/LPLDF-Bebop-Theme"
git pull --ff-only origin main
```

Copier ensuite les fichiers de la V5 dans ce dossier depuis VS Code ou le
gestionnaire de fichiers, puis :

```bash
git status
git add .
git commit -m "Installation du thème LPLDF V5"
git push origin main
```

## Règle de sécurité

Le dépôt est public. Ne jamais y ajouter :

- mot de passe ;
- accès SSH ;
- fichier `.env` ;
- clé API ;
- sauvegarde de base de données ;
- coordonnées ou commandes de clients.
