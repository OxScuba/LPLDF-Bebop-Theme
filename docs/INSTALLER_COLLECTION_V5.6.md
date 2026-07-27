# Installer la Collection marchande native

Cette mise à jour concerne :

- le thème `custom.css` ;
- la page CMS `la-collection` ;
- la description et le CMS du Pack Découverte ;
- la description et le CMS du Pack Liberté et responsabilité ;
- le registre des images.

## 1. Publier le dépôt

Depuis le dossier local du dépôt :

```bash
python3 tests/validate_package.py
git add .
git commit -m "Catalogue natif be-BOP de la Collection v5.6"
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

Ne pas supprimer ni transformer les lignes de ce type :

```text
[Product=t01-les-marchands-de-chandelles?display=img-4]
```

Elles ne sont pas du texte visible : be-BOP les remplace par ses véritables
composants produit. Chaque carte reçoit ainsi automatiquement :

- l’image principale configurée dans la fiche produit ;
- le prix en sats calculé par be-BOP ;
- le prix en euros ;
- le bouton natif `Ajouter au panier` ;
- un lien vers la fiche produit.

Le CSS masque uniquement la variante mobile simplifiée de be-BOP, qui ne possède
pas de bouton panier, et adapte la variante `img-4` aux petits écrans.

## 5. Conditions côté produits

Pour que chaque carte soit complète, vérifier dans chaque fiche produit :

1. qu’une image principale est définie ;
2. que le produit est visible dans l’e-shop ;
3. que l’ajout au panier est autorisé ;
4. que son prix final en euros est correct ;
5. que le stock ou la disponibilité autorise la commande.

Pour le second pack, l’image principale attendue dans be-BOP est :

```text
pack-liberte-et-responsabilite-t05-a-t09-0-goJlQO
```

## 6. Contrôle

Sur ordinateur et téléphone, vérifier :

- les deux packs apparaissent dans deux cartes de même style ;
- chaque pack affiche sa propre image ;
- le Pack Découverte mène vers `/product/pack-decouverte-t00-t04` ;
- le Pack Liberté et responsabilité mène vers `/product/pack-saison-2-t05-t09` ;
- le prix en sats et le prix en euros sont visibles sur chaque carte ;
- `Ajouter au panier` ajoute réellement le produit sans ouvrir sa fiche ;
- `Découvrir le tome` ou `Découvrir le pack` ouvre la fiche correspondante ;
- les miniatures ont un style uniforme pour les saisons et les tomes seuls ;
- le Tome 00 est indiqué comme offert uniquement dans le Pack Découverte ;
- les cinq albums de chaque pack sont présents dans son CMS ;
- aucun ancien texte long ne se répète au-dessus du CMS.
