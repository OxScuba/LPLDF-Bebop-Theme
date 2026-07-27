# Architecture des contenus

## Sources principales

| Élément | Emplacement | Rôle |
|---|---|---|
| thème actif | `custom.css` | identité visuelle et composants |
| pages éditoriales | `cms/` | contenus HTML avancés |
| fiches papier | `produits/papier/` | textes prêts pour les produits |
| offres groupées | `produits/packs/` | contenus des packs |
| blocs enrichis | `produits/cms-apres-produit/` | sections visuelles sous les produits |
| images | `donnees/REGISTRE_IMAGES_BEBOP.csv` | noms et slugs be-BOP |
| produits | `donnees/ISBN_et_donnees_produits.csv` | ISBN et informations structurées |
| navigation commerciale | `donnees/PLAN_DES_TAGS.csv` | tags et regroupements |
| référencement | `donnees/SEO_pages.csv` | titres et descriptions SEO |

## Règles de cohérence

- Un contenu utilisé par la boutique possède une source unique dans le dépôt.
- Le `custom.css` de la racine est la seule feuille de style publiée.
- Les images sont référencées dans le registre avant d’être ajoutées durablement.
- Les slugs de produits sont écrits en minuscules et séparés par des tirets.
- Les tags, slugs produit et slugs image restent trois catégories distinctes.
- Les fichiers de `juridique/` sont des modèles, pas des textes réputés validés.
- Les prévisualisations générées ne sont pas versionnées.

## Mise à jour d’une page

1. Modifier le fichier dans `cms/`.
2. Mettre à jour le registre ou les données associées si nécessaire.
3. Lancer la validation.
4. Examiner le diff Git.
5. Publier le dépôt.
6. Copier le CMS dans be-BOP.
7. Vérifier le résultat public.
