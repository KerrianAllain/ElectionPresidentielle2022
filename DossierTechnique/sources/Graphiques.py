from RecuperationDesDonnees import *
from FonctionsAuxiliaires import *
import matplotlib.pyplot as plt



#                        _     _                  ____
#                       | |   (_)                |  _ \
#   __ _ _ __ __ _ _ __ | |__  _  __ _ _   _  ___| |_) | __ _ _ __ _ __ ___
#  / _` | '__/ _` | '_ \| '_ \| |/ _` | | | |/ _ \  _ < / _` | '__| '__/ _ \
# | (_| | | | (_| | |_) | | | | | (_| | |_| |  __/ |_) | (_| | |  | | |  __/
#  \__, |_|  \__,_| .__/|_| |_|_|\__, |\__,_|\___|____/ \__,_|_|  |_|  \___|
#   __/ |         | |               | |
#  |___/          |_|               |_|

def graphiqueBarre(database: dict) -> None:
	"""
	Affiche un diagramme à barres représentant la répartition des votes au niveau national
	ou pour un département spécifique.

	Paramètres :
		- database (dict): Un dictionnaire représentant les données nationales ou une liste de
			dictionnaires représentant les données de plusieurs départements.

	Retour :
		- None

	Étapes :
		1. Vérifie le type de database (national ou départemental).
		2. Calcule la somme des votes pour chaque catégorie.
		3. Affiche un diagramme à barres avec les résultats.
	"""
	colors = ['gold', 'mediumpurple', 'lightskyblue', 'gray', 'salmon']
	labels = ['Abstentions', 'Blancs', 'Exprimes', 'Nuls', 'Votants']
	nom_graphique = "National"
	sizes = [0] * 5

	if isinstance(database, dict):
		nom_graphique = f"du département : {database['Libelle_Departement']}"
		database = [database]

	for departement in range(len(database)):
		for indice in range(len(sizes)):
			valeur = database[departement][labels[indice]]
			sizes[indice] += valeur

	labels = [f'Abstentions\n{affichage(sizes[0])}', f'Blancs\n{affichage(sizes[1])}', f'Exprimés\n{affichage(sizes[2])}', f'Nuls\n{affichage(sizes[3])}', f'Votants\n{affichage(sizes[4])}']

	plt.figure("Graphique à bâtons")
	plt.title(f"Diagramme {nom_graphique}")
	plt.bar(labels, sizes, color = colors)
	plt.show()


#                        _     _                   _____ _                _       _
#                       | |   (_)                 / ____(_)              | |     (_)
#   __ _ _ __ __ _ _ __ | |__  _  __ _ _   _  ___| |     _ _ __ ___ _   _| | __ _ _ _ __ ___
#  / _` | '__/ _` | '_ \| '_ \| |/ _` | | | |/ _ \ |    | | '__/ __| | | | |/ _` | | '__/ _ \
# | (_| | | | (_| | |_) | | | | | (_| | |_| |  __/ |____| | | | (__| |_| | | (_| | | | |  __/
#  \__, |_|  \__,_| .__/|_| |_|_|\__, |\__,_|\___|\_____|_|_|  \___|\__,_|_|\__,_|_|_|  \___|
#   __/ |         | |               | |
#  |___/          |_|               |_|

def graphiqueCirculaire(database: dict) -> None:
	"""
	Affiche un diagramme circulaire représentant la répartition des votes au niveau national
	ou pour un département spécifique.

	Paramètres :
		- database (dict): Un dictionnaire représentant les données nationales ou départementales.
			Si c'est un dictionnaire unique, il est considéré comme les données nationales.
			Si c'est une liste de dictionnaires, chaque dictionnaire représente les données d'un département.

	Retour :
		- None

	Étapes :
		1. Vérifie le type de database (national ou départemental).
		2. Calcule le pourcentage des votes par rapport aux inscrits.
		3. Ajuste les tailles des parts pour assurer une somme de 100%.
		4. Affiche un diagramme circulaire avec les résultats.
	
	Notes :
		- Les données nationales sont généralement un dictionnaire unique avec des clés telles que 'Inscrits', 'Votants', 'Nuls', etc.
		- Les données départementales sont une liste de dictionnaires, chaque dictionnaire représentant les données d'un département.
		- La fonction utilise la bibliothèque Matplotlib pour générer le diagramme circulaire.
	"""
	colors = ['salmon', 'gray', 'lightskyblue', 'mediumpurple', 'gold']
	labels = ['Votants', 'Nuls', 'Exprimes', 'Blancs', 'Abstentions']
	nom_graphique = "National"
	explode = (0, 0, 0, 0, 0)

	if isinstance(database, dict):
		nom_graphique = f"du département : {database['Libelle_Departement']}"
		database = [database]

	inscrits = sum(departement['Inscrits'] for departement in database)
	sizes = [round(database[0][label] / inscrits * 100, 2) for label in labels]
	sizes = [round(ratio / sum(sizes), 3) * 100 for ratio in sizes]

	plt.figure("Diagramme circulaire")
	plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 90)
	plt.title(f"Diagramme {nom_graphique}")
	plt.axis('equal')
	plt.show()



if __name__ == '__main__':
	database = recuperationDesDonnees()					# Obtention de la base de données
	liste_departements = listeDepartements(database)	# Obtention de la liste des départements

	graphiqueBarre(liste_departements)								# Appel du graphiqueBarre avec les données nationales
	graphiqueBarre(recupererDonneesDepartement(database, 'Ain'))	# Appel du graphiqueBarre avec les données de l'Ain
	graphiqueBarre(recupererDonneesDepartement(database, '01'))		# Appel du graphiqueBarre avec les données de 01

	graphiqueCirculaire(liste_departements)								# Appel du graphiqueCirculaire avec les données nationales
	graphiqueCirculaire(recupererDonneesDepartement(database, 'Ain'))	# Appel du graphiqueCirculaire avec les données de l'Ain
	graphiqueCirculaire(recupererDonneesDepartement(database, '01'))	# Appel du graphiqueCirculaire avec les données de 01