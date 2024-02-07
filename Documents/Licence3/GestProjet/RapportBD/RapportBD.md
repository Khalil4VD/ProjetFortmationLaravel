---
title: "EXPLORATION APPROFONDIE DES PERFORMANCES STATISTIQUES DES JOUEURS DE FOOTBALL PROFESSIONNEL : VERS UNE NOUVELLE VISION DU TALENT"
author:
  
- MAKHLOUFI Khalil,
- CHIRANE Rania,
- MARTIN Samuel,
- GONZALEZ Emmanuel,
- VITOFFODJI Adjimon.


date: "24/11/2023"
output:
  pdf_document:
    fig_caption: yes
    keep_md: yes
    keep_tex: yes
    md_extensions: +raw_attribute
    number_sections: yes
    toc: yes
    toc_depth: 1
toc-title: "Table des matières"

---




**Introduction **

\bigskip

 Au cœur de l'ébullition du monde du football, ce rapport de base de données représente une étape cruciale dans la réalisation d'un projet novateur. Notre objectif principal est de démystifier les performances des footballeurs professionnels sur plusieurs saisons, redéfinissant ainsi les critères d'excellence et offrant une perspective inédite aux passionnés de ce sport.

Cette base de données est conçue pour être bien plus qu'un simple entrepôt d'informations. Elle aspire à devenir un espace d'exploration pour les néophytes, une mine de talents pour les recruteurs et une source d'engagement pour les spectateurs. En unissant ces aspects, elle devient une passerelle permettant une expérience enrichissante et accessible à tous.

La centralité de cette base de données réside dans sa capacité à mettre en lumière les performances individuelles des joueurs. Elle ouvre ainsi de nouvelles perspectives pour le recrutement, érigeant une toile dynamique où chaque statistique compte.

Dans ce rapport, nous plongerons dans la manière dont cette base de données révolutionnaire est conçue, organisée et maintenue pour répondre aux besoins croissants des utilisateurs. Nous détaillerons également comment elle redéfinit la manière dont le talent est perçu et compris dans le monde du football, offrant une perspective unique grâce à l'analyse précise des données.

Cette introduction pose les bases de notre exploration, où les chiffres prennent vie et où chaque aspect de la performance des joueurs est mis en avant. Nous allons examiner en détail comment cette base de données éclaire d'une lumière nouvelle le paysage du football professionnel, offrant une vision détaillée et informée des compétences et des réussites des acteurs de ce sport captivant.

\bigskip

\centering

**De quelle manière les données des performance des footballeurs sur des saisons multiples peuvent-elles être exploitées pour améliorer le processus de recrutement, offrir une information pertinente aux spectateurs et ériger des comparaisons significatives entre joueurs au sein du football professionnel? 
**

\bigskip

\section{Objectif, préparation, outils}

\subsection{Objectif de l'étude}

Le rôle de la base de données dans notre projet est fondamental pour atteindre notre objectif principal : concevoir une plateforme novatrice axée sur l'analyse approfondie des performances des joueurs de football. Cette base de données constitue le socle de notre plateforme, offrant aux utilisateurs la possibilité de comparer minutieusement ces performances à l'aide de statistiques détaillées.

En établissant des fonctionnalités telles que l'intégration de nouveaux joueurs, la gestion des favoris et l'invitation d'autres passionnés, notre but est de créer une communauté active et engagée. Cette plateforme vise à rassembler les passionnés de football, leur permettant d'explorer, d'évaluer et de discuter des performances de leurs joueurs préférés dans un environnement interactif et collaboratif. La base de données joue ainsi un rôle central en fournissant les données pertinentes et actualisées qui alimentent cette expérience immersive pour les utilisateurs.

\subsection{Pré-traitement}

Dans le processus de prétraitement des données, plusieurs lignes ont été supprimées afin de rationaliser notre ensemble de données. Les données des championnats situés au Brésil, au Portugal, aux Pays-Bas et aux États-Unis ont été exclues de notre analyse.

En ce qui concerne les modifications apportées aux données, le nom du championnat français a été uniformisé pour tous les joueurs, étant désigné désormais sous l'appellation "Ligue 1" pour ceux ayant évolué en France.

De plus, certaines colonnes ont été supprimées de l'ensemble de données, notamment les données contenues dans les colonnes Avg, Avg match. Ces suppressions ont été effectuées car ces données ne contribuaient pas significativement à notre analyse.

En parallèle, une nouvelle colonne a été introduite : le ratio de buts par match. Cette mesure vise à évaluer l'impact d'un joueur sur le terrain. Plus le ratio se rapproche de 1, plus le joueur a marqué fréquemment, tandis qu'une valeur proche de 0 indique une performance moindre en termes de buts marqués par match. De plus, les attributs âge et nationalité ont été aussi ajoutés pour offrir une possibilité supplémentaire aux utilisateurs de proposer des graphes.

Il convient de noter également qu'une sélection a été opérée, éliminant les joueurs ayant disputé moins de 20 matchs. Cette décision a été prise pour garantir la pertinence des ratios calculés, évitant ainsi les distorsions pouvant survenir lorsque le nombre de matchs est insuffisant pour évaluer de manière significative les performances d'un joueur.

Enfin, pour consolider notre base de données, nous avons introduit des identifiants uniques pour chaque entité principale. Ces identifiants garantissent une structure robuste en facilitant les requêtes spécifiques et les relations entre les différentes entités. Ils renforcent la cohérence des données et simplifient la gestion des interactions au sein de la base de données. Ces identifiants uniques servent de pierre angulaire pour des requêtes précises et une navigation fluide, assurant ainsi une expérience utilisateur optimale dans la suite du projet.

\subsection{Logiciels, outils}

Dans la réalisation de ce projet, nous avons utilisé le logiciel Excel (2016) pour constituer nos différentes tables. Ensuite, nous avons importé ces tables au format CSV dans le logiciel SQL PhpMyAdmin à l'aide de la version gratuite du logiciel WAMP pour certains, afin de relier à travers les clés primaires et étrangères, les différentes tables.

Pour la réalisation du MCD, nous nous sommes aidés de Mocodo.fr et pour représenter chaque type des données, nous avons créé un MCD sur Phpmyadmin.

Pour la rédaction de ce rapport, nous avons utilisé la version 28-1-2 du logiciel Rstudio sous Mac à l'aide de R Markdown pour générer directement notre document en format PDF.



\section{Structure et éléments clés des données}

\subsection{Modèle conceptuel de données (MCD)}

\subsubsection{Description Générale}
Cette première partie présente une vue d'ensemble du MCD, expliquant les concepts fondamentaux, les entités principales et les relations clés au sein de la base de données.
\bigskip

\begin{figure}[ht]
    \centering
    \includegraphics[width=\textwidth]{/Users/khalil4vd/Documents/Licence3/GestProjet/RapportBD/MOD.png}
    \caption{Description générale du MCD (mocodo.fr)}
    \label{fig:mcd1}
\end{figure}

\subsubsection{Éléments Clés}
La seconde partie se concentre sur les éléments spécifiques du MCD, détaillant les entités, leurs attributs et les associations entre elles. Cette section met en lumière la façon dont le MCD représente précisément la structure des données pour répondre aux besoins du projet.
\bigskip

\begin{figure}[ht]
    \centering
    \includegraphics[width=\textwidth]{/Users/khalil4vd/Documents/Licence3/GestProjet/RapportBD/MOD2.png}
    \caption{Éléments clés du MCD (phpmyadmin)}
    \label{fig:mcd2}
\end{figure}

\subsection{Éléments clés du modèle conceptuel des données}

Cette section se concentre sur les éléments spécifiques du MCD et détaille les entités, leurs attributs et les associations entre elles. Elle met en lumière la façon dont le MCD représente précisément la structure des données pour répondre aux besoins du projet.

\begin{verbatim}
Statistiques (id_stat, matchs_joué, nb_but, ratio_b/m)
Joueurs (id_joueur, nom, âge, nationalité)
Club (id_club, nom)
Championnat (id_ligue, pays)
Réaliser (id_stat, id_joueur, date)
Jouer (id_club, id_joueur, date)
Appartenir (id_club, id_ligue)
\end{verbatim}
