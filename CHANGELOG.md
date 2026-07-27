# Journal des évolutions

Ce fichier conserve uniquement les changements durables du thème et des contenus de la boutique.

## 5.8

- transformation des dix carrés de choix T01 à T10 en ouvertures de fiches ;
- ajout de la couverture, du récit, des notions et de la phrase pivot de chaque tome ;
- ajout d’un bouton explicite vers la fiche produit, sans quitter la page avant ce choix ;
- navigation circulaire entre le tome précédent et le tome suivant ;
- fermeture vers la section « Ce que votre enfant aimerait comprendre » ;
- adaptation des fiches au téléphone et aux petits écrans ;
- validation automatique des dix fiches, couvertures, boutons et navigations.

## 5.7.2

- audit de toutes les pages CMS, blocs produit, blocs pack et aperçus HTML ;
- confirmation que les visionneuses produit JavaScript préservent déjà le défilement ;
- régénération de l’aperçu Home avec le nouveau retour de section ;
- remplacement des contrôles ponctuels par une règle générique applicable à
  toutes les futures fenêtres CSS ;
- refus automatique d’une fermeture visant un marqueur placé après son contenu ;
- refus automatique d’une fenêtre privée de croix ou d’arrière-plan fermant.

## 5.7.1

- déplacement des ancres de fermeture au début de leur section d’origine ;
- retour à « Entrez réellement dans l’album » après fermeture d’une image ;
- retour à « Les grandes idées entrent dans l’histoire » après fermeture d’un guide ;
- même protection appliquée aux fiches des quatre aventuriers dans Univers ;
- ajout d’une marge d’ancrage pour ne pas masquer le titre sous la navigation.

## 5.7

- transformation des seize noms de guides en bulles interactives ;
- création de seize fiches illustrées : parcours, œuvres, concepts et rôle dans la saga ;
- correspondance canonique des guides avec les Tomes 00 à 42 ;
- ajout des quinze nouveaux portraits transparents au registre des images ;
- ajout d’une fiche dédiée à Scuba Wizard comme auteur, illustrateur et passeur ;
- affichage des fiches dans une visionneuse fermée par défaut, adaptée au mobile ;
- ajout de validations empêchant la perte d’une bulle, d’une fiche ou d’un portrait.

## 5.6.1

- correction des sélecteurs selon la structure DOM réellement générée par be-BOP ;
- restauration des grilles de deux, quatre ou cinq produits selon la section ;
- restauration des bandes pleine largeur crème, blanches et vert sauge ;
- conservation des composants marchands natifs : image, sats, euros et panier ;
- maintien d’une carte par ligne sur téléphone et de deux cartes sur tablette.

## 5.6

- remplacement des cartes éditoriales de la Collection par treize widgets produit natifs be-BOP ;
- uniformisation des deux packs, des saisons et des tomes seuls dans un même langage visuel ;
- affichage des deux visuels de packs, dont le Pack Liberté et responsabilité ;
- affichage dynamique du prix en sats et du prix en euros ;
- ajout au panier possible directement depuis la page Collection ;
- conservation d’un accès explicite à chaque fiche produit ;
- adaptation de la variante native `img-4` aux écrans mobiles.

## 5.5

- création de deux CMS enrichis pour les Packs Découverte et Saison 2 ;
- raccourcissement des descriptions natives afin d’éviter les répétitions ;
- présentation commerciale équilibrée des deux packs sur la page Collection ;
- ajout visible du Pack Liberté et responsabilité à 45 € au lieu de 50 € ;
- suppression du second rappel redondant du Pack Saison 2 sous les tomes.

## 5.4.7

- suppression des largeurs minimales héritées de la mise en page produit pour ordinateur ;
- adaptation mobile complète du titre, de la galerie, des miniatures et du panneau d’achat ;
- suppression du découpage horizontal des boutons et de la description native ;
- sécurisation de la largeur des blocs CMS produit sans modifier le header ni le footer.

## 5.4.6

- restauration du comportement natif des miniatures produit : elles changent l’image affichée sans ouvrir la visionneuse ;
- ouverture plein écran réservée au clic sur la grande image affichée ;
- ajout d’une visionneuse accessible et fermable par bouton, clic sur le fond ou touche Échap ;
- correction renforcée de la largeur mobile au niveau global de la page be-BOP.

## 5.4.5

- suppression du débordement horizontal créé par le bloc CMS produit ;
- rétablissement de la largeur normale de l’en-tête, du contenu et du pied de page sur mobile ;
- élargissement maîtrisé du conteneur CMS à l’intérieur de la fiche native ;
- transformation de la sélection d’image native be-BOP en visionneuse plein écran ;
- ajout d’un bouton de fermeture propre à chaque fiche T00 à T10 ;
- aucune duplication des images dans le flux de la page.

## 5.4.4

- réécriture des onze fiches papier T00 à T10 à partir du corpus publié de l’Atelier LPLDF ;
- descriptions natives raccourcies pour éviter leur répétition avec les blocs CMS ;
- ajout d’une description courte propre à chaque tome ;
- correction canonique de la présentation du Tome 08 ;
- correction globale du format physique : 21 × 21 cm, 38 pages couverture comprise ;
- correction cohérente des trois fiches de packs ;
- ajout de contrôles empêchant le retour de dimensions physiques erronées.

## 5.4.3

- suppression du collage de couvertures du Pack Saison 2, que be-BOP pouvait extraire de son conteneur ;
- nouveau bandeau Saison 2 entièrement éditorial, sans image parasite ;
- nouveau bloc de prix « Album papier » pour les Tomes 00 et 10 ;
- amélioration de l’espacement entre le prix et le bouton sur ordinateur et mobile.

## 5.4.2

- remplacement des shortcodes produit de la page Collection par des cartes HTML stables ;
- suppression des conteneurs blancs et du second rendu natif des produits ;
- ajout d’une navigation interne entre les saisons ;
- création d’un bandeau visuel pour le Pack Saison 2 ;
- amélioration de la grille sur ordinateur, tablette et mobile.

## 5.4.1

- ajout du retour vers le visuel de l’équipe dans le sélecteur des aventuriers ;
- restauration du lien vers la page Univers ;
- cadrage intégral des portraits transparents ;
- amélioration de l’affichage mobile.

## 5.4

- sécurisation des visionneuses d’images dans les CMS Home et Univers ;
- simplification du sélecteur des aventuriers sur l’accueil ;
- protection contre l’affichage des grandes images dans le flux de la page.

## 5.3

- ajout des visionneuses d’images en grand format sans JavaScript ;
- enrichissement des fiches des personnages dans la page Univers ;
- création du registre central des images be-BOP.

## 5.2

- refonte éditoriale de l’accueil et de l’Univers ;
- amélioration de la navigation commerciale ;
- ajout des portraits et contenus issus du canon de la saga.

## 5.1

- adaptation des composants au HTML avancé de be-BOP ;
- remplacement des interactions fragiles par des composants HTML et CSS.

## 5.0

- création du système visuel LPLDF ;
- mise en place du CSS externe publié avec GitHub Pages ;
- première harmonisation des CMS, fiches produit, tags et données SEO.
