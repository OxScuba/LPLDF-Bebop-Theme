# Maintenance du dépôt

## Avant une modification

```bash
git pull --ff-only
git status
python3 tests/validate_package.py
```

## Après une modification

```bash
python3 tests/validate_package.py
git diff --check
git status
git diff --stat
```

## Publication

```bash
git add -A
git diff --cached --stat
git commit -m "Décrit précisément la modification"
git push
git status
```

## Ajouter une image

1. préparer un nom descriptif et stable ;
2. importer l’image dans be-BOP ;
3. relever son slug exact ;
4. l’ajouter à `donnees/REGISTRE_IMAGES_BEBOP.csv` ;
5. utiliser le slug dans le CMS ;
6. contrôler le rendu public.

## Ajouter ou modifier un produit

Mettre à jour ensemble :

- la fiche de `produits/papier/` ou `produits/packs/` ;
- le bloc de `produits/cms-apres-produit/` s’il existe ;
- `donnees/ISBN_et_donnees_produits.csv` ;
- `donnees/PLAN_DES_TAGS.csv` ;
- les pages CMS qui présentent directement ce produit.

## Retour arrière

Git conserve l’historique du projet. Avant de restaurer une ancienne version :

```bash
git log --oneline --decorate -n 15
git show --stat IDENTIFIANT_DU_COMMIT
```

Créer de préférence un nouveau commit de correction plutôt que réécrire l’historique public.

## Informations publiques

Avant chaque publication, vérifier que le diff ne contient ni secret, ni accès, ni donnée personnelle, ni détail d’infrastructure sans utilité documentaire.
