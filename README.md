# LPLDF be-BOP — Refonte visuelle V5.3

Thème et contenus prêts à intégrer pour la boutique **Les Petites Leçons de
Frédéric**, sur be-BOP
`885a5ddec4e7f47cec0d52bd0ef9132706350e87`.

## Architecture retenue

La source be-BOP est partagée entre deux boutiques. Aucun fichier serveur n’est
modifié. Le thème est chargé depuis chaque page CMS grâce au mode
**Use advanced HTML edition** :

```html
<style>
@import url("https://oxscuba.github.io/LPLDF-Bebop-Theme/custom.css");
</style>
```

Cette balise est déjà incluse dans tous les fichiers de `cms/` et dans les
blocs de `produits/cms-apres-produit/`.

## Contenu du dépôt

- `custom.css` : design system V5.3 publié avec GitHub Pages ;
- `cms/` : 14 pages complètes en HTML avancé ;
- `produits/papier/` : descriptions en texte simple, prix, tags et ISBN ;
- `produits/cms-apres-produit/` : 11 blocs éditoriaux à placer après le cœur
  des fiches papier ;
- `produits/packs/` : descriptions et prix proposés pour les packs ;
- `donnees/` : tags, SEO et données bibliographiques ;
- `docs/` : installation, réglages, contrôles et retour arrière ;
- `juridique/` : brouillons à compléter avant publication ;
- `versions/` : sauvegardes des versions antérieures.

## Déploiement

1. Publier `custom.css`.
2. Configurer le thème natif et la langue française.
3. Convertir une page CMS de test en HTML avancé.
4. Installer `cms/Home.html` dans **Raw HTML**, avec **Full screen** désactivé.
5. Installer `cms/Univers.html`, puis les autres pages une à une.
6. Ajouter les blocs de `produits/cms-apres-produit/` dans la zone
   **Add CMS code and widgets after product page core**.
7. Contrôler ordinateur et mobile après chaque étape.

La procédure complète se trouve dans
`docs/INSTALLATION_PAS_A_PAS.md`.

## Sécurité

Le dépôt est public. Il ne doit contenir aucun mot de passe, accès SSH, secret,
fichier `.env` ou donnée client.
