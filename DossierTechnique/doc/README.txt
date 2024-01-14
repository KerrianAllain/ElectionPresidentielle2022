# Projet d'Analyse des Résultats de l'Élection Présidentielle 2022

Ce projet vise à analyser et visualiser les résultats de l'élection présidentielle d'avril 2022 en France.
Il inclut des fonctionnalités pour récupérer, organiser et représenter graphiquement les données électorales par département.


## Installation
1. Cloner le dépôt :
	```bash
	git clone https://github.com/KerrianAllain/ElectionPresidentielle2022.git
	cd ElectionPresidentielle2022
	```

2. Installez les dépendances :
	```bash
	pip install -r requirements.txt
	```


## Utilisation
1. Naviguer vers le répertoire sources à l'aide de la commande :
	```bash
	cd sources
	```

2. Exécuter le script principal pour récupérer les données et ouvrir l'Interface Homme Machine :
	```bash
	python IHM.py
	```

3. Le script ouvrira une fenêtre Tkinter et générera des graphiques à barres et circulaires
pour les résultats nationaux ainsi que pour des départements spécifiques.


## Structure du Projet
- **IHM.py**: Le script général pour l'utilisation du projet.
- **Graphiques.py**: Le script pour générer les graphiques.
- **FonctionsAuxiliaires.py**: Contient des fonctions auxiliaires pour la récupération des données et la génération des graphiques.
- **RecuperationDesDonnees.py**: Gère la récupération des données depuis une URL et leur organisation.


## Configuration
Système d'exploitation:
    -> Le projet est compatible avec les systèmes d'exploitation Linux et Windows.

Environnement Python:
    -> S'assurer d'avoir Python 3.X installé sur la machine.

Dépendances:
    -> Les dépendances nécessaires au fonctionnement du projet sont répertoriées dans le fichier requirements.txt.
        -> Il est possible de les installer en utilisant la commande : `pip install -r requirements.txt`


## Auteurs
- ALLAIN Kerrian
- GEORGES—HAMON Evan
- ALLAIN Ethann