# Installer les fiches des packs et la nouvelle Collection

Cette mise à jour concerne uniquement :

- le thème `custom.css` ;
- la page CMS `la-collection` ;
- la description et le CMS du Pack Découverte ;
- la description et le CMS du Pack Liberté et responsabilité.

## 1. Publier le dépôt

Depuis le dossier local du dépôt :

```bash
python3 tests/validate_package.py
git add .
git commit -m "Ajout des CMS des packs et refonte de la Collection v5.5"
git push
```

Attendre la mise à jour de GitHub Pages avant de modifier les CMS dans be-BOP.

## 2. Pack Découverte Bastiat

Produit :

```text
Pack Découverte Bastiat — T00 à T04
```

Slug :

```text
pack-decouverte-t00-t04
```

Prix :

```text
40 €
```

Dans **Basic Settings > Description**, copier uniquement le texte compris entre
`DÉBUT` et `FIN` dans :

```text
produits/packs/pack-decouverte-t00-t04.txt
```

Dans **Advanced Features > CMS Content > Content after product details** :

1. cocher `Edit as raw HTML` ;
2. remplacer le contenu par l’intégralité de :

```text
produits/cms-apres-pack/pack-decouverte-t00-t04.html
```

## 3. Pack Liberté et responsabilité

Produit :

```text
Pack Liberté et responsabilité — T05 à T09
```

Slug :

```text
pack-saison-2-t05-t09
```

Prix :

```text
45 €
```

Dans **Basic Settings > Description**, copier uniquement le texte compris entre
`DÉBUT` et `FIN` dans :

```text
produits/packs/pack-saison-2-t05-t09.txt
```

Dans **Advanced Features > CMS Content > Content after product details** :

1. cocher `Edit as raw HTML` ;
2. remplacer le contenu par l’intégralité de :

```text
produits/cms-apres-pack/pack-saison-2-t05-t09.html
```

## 4. Page La Collection

Ouvrir la page CMS dont le slug est :

```text
la-collection
```

Activer l’édition HTML avancée puis remplacer le contenu complet par :

```text
cms/La_Collection.html
```

## 5. Contrôle

Sur ordinateur et téléphone, vérifier :

- les deux packs apparaissent dans la section « Deux parcours complets » ;
- le Pack Découverte mène vers `/product/pack-decouverte-t00-t04` ;
- le Pack Liberté et responsabilité mène vers `/product/pack-saison-2-t05-t09` ;
- les prix affichés sont respectivement `40 €` et `45 €` ;
- les valeurs barrées sont `50 €` ;
- le Tome 00 est indiqué comme offert uniquement dans le Pack Découverte ;
- les cinq albums de chaque pack sont présents dans son CMS ;
- aucun ancien texte long ne se répète au-dessus du CMS.
