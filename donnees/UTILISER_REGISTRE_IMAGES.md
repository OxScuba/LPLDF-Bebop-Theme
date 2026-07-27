# Utiliser le registre des images be-BOP

Le fichier `REGISTRE_IMAGES_BEBOP.csv` constitue la source centrale pour les
noms, usages et slugs d’images employés dans les CMS.

À chaque nouvel import :

1. nommer le fichier avant l’envoi selon le modèle existant ;
2. importer l’image dans **Admin > Merch > Pictures** ;
3. copier exactement le slug retourné par be-BOP ;
4. ajouter une ligne au registre ;
5. indiquer l’usage prévu et le statut ;
6. remplacer l’URL concernée dans le CMS ;
7. vérifier l’image au format `1024`.

## Statuts conseillés

- `actif` : utilisé dans le site ;
- `disponible` : importé mais pas encore utilisé ;
- `a_remplacer` : provisoire ;
- `archive` : conservé pour historique ;
- `a_creer` : prévu mais non produit.

## URL type

```html
/picture/raw/SLUG_BEBOP/format/1024?v=1
```

Ne pas utiliser le format `2048` sur cette instance : les tests publics ont
montré que be-BOP renvoie une erreur 404 pour ce format.
