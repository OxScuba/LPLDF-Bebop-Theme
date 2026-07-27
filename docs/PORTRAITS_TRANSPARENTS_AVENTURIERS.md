# Portraits transparents pour la Home

## Objectif technique

Créer quatre images carrées PNG de 1600 × 1600 px :

- un seul personnage en pied ;
- fond réellement transparent ;
- marge de sécurité d’environ 8 % autour de la silhouette ;
- ombre très légère uniquement sous les chaussures ;
- aucun texte, décor, cadre, logo, objet flottant ou autre personnage ;
- même direction de lumière et même niveau de finition pour les quatre images.

Les références officielles du dépôt `Atelier-LPLDF` doivent être jointes à la
génération. La cohérence du visage, de l’âge et des vêtements prévaut sur toute
interprétation nouvelle.

## Fred

Nom : `lpldf-fred-transparent.png`

Prompt :

> Crée un personnage en pied détouré sur fond entièrement transparent,
> fidèle à l’image de référence officielle de Fred dans Les Petites Leçons de
> Frédéric. Fred est un jeune homme de 21 ans, grand et mince, aux cheveux
> châtain roux ondulés avec une mèche souple, au visage ouvert et attentif. Il
> porte son long manteau bleu, un gilet jaune moutarde, une chemise blanche,
> une cravate sombre, un pantalon brun et des chaussures foncées. Il tient son
> carnet brun-rouge entrouvert contre lui et lève légèrement un sourcil, comme
> s’il venait de remarquer une conséquence oubliée. Illustration jeunesse
> premium, chaleureuse, élégante et cohérente avec les albums. Silhouette
> complète, mains et chaussures visibles, centrée, sans décor, sans texte,
> sans cadre, sans accessoire flottant, fond alpha réellement transparent.

## Lina

Nom : `lpldf-lina-transparent.png`

Prompt :

> Crée un personnage en pied détouré sur fond entièrement transparent,
> fidèle à l’image de référence officielle de Lina dans Les Petites Leçons de
> Frédéric. Lina a 8 ans, de très longs cheveux roux-cuivrés abondants et
> bouclés, de grands yeux verts et une expression attentive. Elle porte sa
> longue robe verte à manches courtes, avec col clair et petits points dorés ou
> pâles, ainsi que des chaussures brunes. Elle penche légèrement la tête et
> tourne son regard vers une personne hors champ, comme si elle remarquait
> quelqu’un que le groupe avait oublié. Illustration jeunesse premium,
> chaleureuse et cohérente avec les albums. Respecter son âge d’enfant.
> Silhouette complète, mains et chaussures visibles, centrée, sans décor, sans
> texte, sans cadre, fond alpha réellement transparent.

## Tom

Nom : `lpldf-tom-transparent.png`

Prompt :

> Crée un personnage en pied détouré sur fond entièrement transparent,
> fidèle à l’image de référence officielle de Tom dans Les Petites Leçons de
> Frédéric. Tom a 9 ans, des cheveux châtain clair très ébouriffés, de grands
> yeux verts et une expression enthousiaste. Il porte une chemise ou tunique
> crème à col lacé, les manches retroussées, un pantalon brun et des bottes
> brunes, sans bretelles visibles. Sa posture traduit l’élan : un pied
> légèrement en avant et une main ouverte comme s’il disait « J’ai une idée ! »,
> sans agressivité. Illustration jeunesse premium, chaleureuse et cohérente
> avec les albums. Silhouette complète, mains et chaussures visibles, centrée,
> sans décor, sans texte, sans cadre, fond alpha réellement transparent.

## Milo

Nom : `lpldf-milo-transparent.png`

Prompt :

> Crée un personnage en pied détouré sur fond entièrement transparent,
> fidèle à l’image de référence officielle de Milo dans Les Petites Leçons de
> Frédéric. Milo a 7 ans et doit clairement paraître le plus jeune du groupe.
> Reprendre exactement son visage, ses cheveux, ses yeux et ses vêtements
> depuis la référence officielle jointe. Il tient un petit caillou ou un objet
> de preuve dans sa paume et l’observe avec une expression calme et précise,
> comme s’il venait de remarquer un détail absent. Illustration jeunesse
> premium, chaleureuse et cohérente avec les albums. Silhouette complète,
> mains et chaussures visibles, centrée, sans décor, sans texte, sans cadre,
> fond alpha réellement transparent.

## Contrôle avant import

- vérifier la transparence dans un logiciel affichant un damier ;
- vérifier que les quatre personnages ont une échelle cohérente ;
- vérifier que Milo paraît plus jeune que Lina, elle-même plus jeune que Tom ;
- vérifier que Fred apparaît comme un jeune adulte et non comme un professeur ;
- compresser les PNG sans réduire la définition ;
- importer dans be-BOP puis conserver les quatre slugs exacts retournés.
