# Projet ETL (Extract, Transform, Load) pour la collecte de données sur le PIB des pays

Ce projet vise à extraire, transformer et charger les données sur le PIB (Produit Intérieur Brut) des pays à partir d'une source en ligne, puis à les stocker dans une base de données SQLite et un fichier JSON.

## Objectif
L'objectif principal de ce projet est de collecter les données sur le PIB des pays à partir de la page Wikipedia "List of countries by GDP (nominal)", de les nettoyer et de les stocker de manière structurée dans une base de données relationnelle et un fichier JSON.

### Dépendances :
   Ce projet nécessite les dépendances suivantes :

    pandas
    requests
    BeautifulSoup (bs4)
    sqlite3

### Structure du projet

    - etl_project.py: Le script principal du projet qui contient les fonctions pour extraire, transformer et charger les données.
    - etl_project_log.txt: Le fichier de journalisation où les étapes du processus ETL sont enregistrées.
    World_Economies.db: La base de données SQLite où les données sont stockées.
    - Countries_by_GDP.json: Le fichier JSON où les données sont également sauvegardées.

### Utilisation:
    - Assurez-vous d'avoir les dépendances requises installées sur votre environnement Python.
    - Exécutez le script etl_project.py.
    - Les étapes du processus ETL seront enregistrées dans le fichier de journalisation etl_project_log.txt.
    - Les données nettoyées seront stockées dans la base de données SQLite - World_Economies.db et dans le fichier JSON Countries_by_GDP.json.



## Contributions
Les contributions sont les bienvenues ! N'hésitez pas à soumettre des problèmes ou à ouvrir des demandes d'extraction pour suggérer des améliorations.
