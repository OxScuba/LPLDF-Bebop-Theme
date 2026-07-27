# Remplacer le dépôt local par la version nettoyée

Les commandes suivantes supposent :

- archive téléchargée dans `~/Téléchargements` ;
- dépôt Git existant dans `~/Documents/LPLDF-Bebop-Theme`.

## 1. Extraire l’archive

```bash
cd "$HOME/Téléchargements"
unzip LPLDF-Bebop-Theme-PROPRE.zip
```

## 2. Synchroniser le contenu

```bash
rsync -av --delete \
  --exclude=".git/" \
  "$HOME/Téléchargements/LPLDF-Bebop-Theme-PROPRE/" \
  "$HOME/Documents/LPLDF-Bebop-Theme/"
```

`--delete` retire du dépôt local les anciens fichiers absents de la version propre. L’exclusion `.git/` conserve l’historique et la connexion au dépôt GitHub.

## 3. Contrôler avant publication

```bash
cd "$HOME/Documents/LPLDF-Bebop-Theme"
python3 tests/validate_package.py
git status
git diff --stat
```

## 4. Publier

```bash
git add -A
git diff --cached --stat
git commit -m "Nettoyage et restructuration du dépôt public"
git push
git status
```

Les suppressions affichées par Git sont normales : elles correspondent aux anciennes copies, archives et instructions ponctuelles retirées du dépôt.
