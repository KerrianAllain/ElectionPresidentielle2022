from FonctionsAuxiliaires import *
from requests import get



#  _____                                      _   _             _____            _____
# |  __ \                                    | | (_)           |  __ \          |  __ \
# | |__) |___  ___ _   _ _ __   ___ _ __ __ _| |_ _  ___  _ __ | |  | | ___  ___| |  | | ___  _ __  _ __   ___  ___  ___
# |  _  // _ \/ __| | | | '_ \ / _ \ '__/ _` | __| |/ _ \| '_ \| |  | |/ _ \/ __| |  | |/ _ \| '_ \| '_ \ / _ \/ _ \/ __|
# | | \ \  __/ (__| |_| | |_) |  __/ | | (_| | |_| | (_) | | | | |__| |  __/\__ \ |__| | (_) | | | | | | |  __/  __/\__ \
# |_|  \_\___|\___|\__,_| .__/ \___|_|  \__,_|\__|_|\___/|_| |_|_____/ \___||___/_____/ \___/|_| |_|_| |_|\___|\___||___/
#                       | |
#                       |_|

class RecuperationDesDonnees:
	def __init__(self):
		"""
		Initialise une instance de la classe RecuperationDesDonnees.
		Le constructeur de la classe initialise une instance de la classe RecuperationDesDonnees avec une base de données vide.

		Arguments:
			- Aucun argument explicite n'est requis.

		Retour:
			- Aucune valeur de retour explicite n'est générée par cette méthode.

		La méthode crée un attribut `database` dans l'instance de la classe, qui est une structure
		de données vide utilisée pour stocker les données récupérées.

		Notes:
			- Cette classe peut être utilisée comme point central pour la récupération et le stockage de données.
			- La base de données est initialement vide, et les données peuvent être ajoutées ultérieurement.
		"""
		self.database = {}


	#                                               _____
	#                                              |  __ \
	#  _ __ ___  ___ _   _ _ __   ___ _ __ ___ _ __| |  | | ___  _ __  _ __   ___  ___  ___
	# | '__/ _ \/ __| | | | '_ \ / _ \ '__/ _ \ '__| |  | |/ _ \| '_ \| '_ \ / _ \/ _ \/ __|
	# | | |  __/ (__| |_| | |_) |  __/ | |  __/ |  | |__| | (_) | | | | | | |  __/  __/\__ \
	# |_|  \___|\___|\__,_| .__/ \___|_|  \___|_|  |_____/ \___/|_| |_|_| |_|\___|\___||___/
	#                     | |
	#                     |_|

	def recupererDonnees(self, url: str) -> dict:
		"""
		Récupère des données depuis une URL et les organise dans un dictionnaire.
		Cette méthode utilise une requête HTTP pour récupérer des données à partir de l'URL spécifiée.
		Les données sont organisées dans un dictionnaire où les clés sont les en-têtes et les valeurs sont des listes de données.

		Arguments:
			- `url` (str): L'URL à partir de laquelle récupérer les données.

		Retour:
			- dict: Un dictionnaire organisé avec les en-têtes comme clés et les données correspondantes comme valeurs.
					Si la requête échoue, la fonction renvoie None.

		- La méthode utilise la bibliothèque `requests` pour effectuer une requête HTTP à l'URL spécifiée.
		- Si la requête réussit (status code 200), les données sont extraites et organisées dans un dictionnaire.
		- Chaque en-tête devient une clé dans le dictionnaire, et les valeurs associées sont stockées dans des listes.
		- Si la requête échoue, un message d'erreur est affiché, et la fonction renvoie None.

		Notes:
			- S'asurer que le module `requests` est installé (`pip install requests`).
			- Cette méthode est destinée à récupérer des données tabulaires avec des en-têtes.
		"""
		dictionnaire = {}
		requete = get(url)

		if requete.status_code == 200:
			lines = requete.text.split('\n')
			lines = [line for line in lines if line.strip()]

			en_tetes = lines[0].split(';')
			donnee = [line.split(';') for line in lines[1:]]

			for en_tete in en_tetes:
				dictionnaire[en_tete] = []

			for lignes in donnee:
				for en_tete, value in zip(en_tetes, lignes):
					dictionnaire[en_tete].append(value)
			return dictionnaire
		else:
			print("La requête a échoué avec le code :", requete.status_code)
			return None


	#                              _               _____
	#                             (_)             |  __ \
	#   ___  _ __ __ _  __ _ _ __  _ ___  ___ _ __| |  | | ___  _ __  _ __   ___  ___  ___
	#  / _ \| '__/ _` |/ _` | '_ \| / __|/ _ \ '__| |  | |/ _ \| '_ \| '_ \ / _ \/ _ \/ __|
	# | (_) | | | (_| | (_| | | | | \__ \  __/ |  | |__| | (_) | | | | | | |  __/  __/\__ \
	#  \___/|_|  \__, |\__,_|_| |_|_|___/\___|_|  |_____/ \___/|_| |_|_| |_|\___|\___||___/
	#             __/ |
	#            |___/

	def organiserDonnees(self, dictionnaire: dict) -> dict:
		"""
		Organise les données issues d'un dictionnaire des résultats d'une élection présidentielle.
		Cette fonction effectue plusieurs tâches pour nettoyer, restructurer et calculer les rapports
		des données électorales par département.

		Arguments :
			- `dictionnaire` (dict): Un dictionnaire contenant les données brutes de résultats d'élection.

		Retourne :
			- dict: Un dictionnaire contenant les données organisées par département.

		La fonction réalise les opérations suivantes :
			- Supprime les clés indésirables du dictionnaire telles que les informations de
				circonscription, de vote, de candidats individuels, etc.
			- Renomme certaines clés pour une meilleure lisibilité et uniformité dans le dictionnaire.
			- Agrège les données par département en calculant la somme des chiffres clés tels
				que les inscrits, abstentions, votants, blancs, nuls, exprimés, etc.
			- Calcule les rapports (en pourcentage) pour les chiffres clés tels que les abstentions,
				votants, blancs, nuls, exprimés par rapport aux inscrits pour chaque département.

		Les clés supprimées du dictionnaire comprennent les informations spécifiques à un bureau de vote,
		des données personnelles des candidats, etc. Les clés restantes comprennent les informations générales
		et agrégées par département, telles que les chiffres bruts et les rapports calculés.

		Les données relatives à chaque département sont accessibles dans le dictionnaire retourné, avec les codes
		de département comme clés et les informations agrégées comme valeurs associées à ces clés.
		"""

		clesARetirer = [
			'Code de la circonscription', 'Libellé de la circonscription', 'Code de la commune', 'Libellé de la commune',
			'Code du b.vote', '% Abs/Ins', '% Vot/Ins', '% Blancs/Ins', '% Blancs/Vot', '% Nuls/Ins', '% Nuls/Vot',
			'% Exp/Ins', '% Exp/Vot', 'N°Panneau', 'Sexe', 'Nom', 'Prénom', 'Voix', '% Voix/Ins', '% Voix/Exp\r'
		]

		for cle in clesARetirer:
			if cle in dictionnaire:
				del dictionnaire[cle]

		clesARenommer = {
			'Code du département': 'Code_Departement',
			'Libellé du département': 'Libelle_Departement',
			'Exprimés': 'Exprimes',
		}

		for ancienneCle, nouvelleCle in clesARenommer.items():
			if ancienneCle in dictionnaire:
				dictionnaire[nouvelleCle] = dictionnaire.pop(ancienneCle)

		donneesDepartement = {}
		for departement in range(len(dictionnaire['Code_Departement'])):
			codeDepartement = dictionnaire['Code_Departement'][departement]
			if codeDepartement not in donneesDepartement:
				donneesDepartement[codeDepartement] = {
					'Libelle_Departement': dictionnaire['Libelle_Departement'][departement],
					'Inscrits': 0,
					'Abstentions': 0,
					'Votants': 0,
					'Blancs': 0,
					'Nuls': 0,
					'Exprimes': 0
				}

			donneesDepartement[codeDepartement]['Inscrits'] += int(dictionnaire['Inscrits'][departement])
			donneesDepartement[codeDepartement]['Abstentions'] += int(dictionnaire['Abstentions'][departement])
			donneesDepartement[codeDepartement]['Votants'] += int(dictionnaire['Votants'][departement])
			donneesDepartement[codeDepartement]['Blancs'] += int(dictionnaire['Blancs'][departement])
			donneesDepartement[codeDepartement]['Nuls'] += int(dictionnaire['Nuls'][departement])
			donneesDepartement[codeDepartement]['Exprimes'] += int(dictionnaire['Exprimes'][departement])

		for codeDepartement, donneeDepartement in donneesDepartement.items():
			for cle in ['Abstentions', 'Votants', 'Blancs', 'Nuls', 'Exprimes']:
				donneeDepartement[f"Rapport_{cle}/Ins"] = round(donneeDepartement[cle] / donneeDepartement['Inscrits'] * 100, 2)
		return donneesDepartement


	#        _     _             _      _____
	#       | |   | |           (_)    |  __ \
	#   ___ | |__ | |_ ___ _ __  _ _ __| |  | | ___  _ __  _ __   ___  ___  ___
	#  / _ \| '_ \| __/ _ \ '_ \| | '__| |  | |/ _ \| '_ \| '_ \ / _ \/ _ \/ __|
	# | (_) | |_) | ||  __/ | | | | |  | |__| | (_) | | | | | | |  __/  __/\__ \
	#  \___/|_.__/ \__\___|_| |_|_|_|  |_____/ \___/|_| |_|_| |_|\___|\___||___/

	def obtenirDonnees(self, url: str) -> dict:
		"""
		Obtient et organise les données à partir d'une URL spécifiée.
		Cette méthode combine les étapes de récupération et d'organisation des données.
		Elle utilise les méthodes `recupererDonnees` et `organiserDonnees` pour récupérer et
		organiser les données à partir de l'URL spécifiée.

		Arguments:
			- `url` (str): L'URL à partir de laquelle récupérer les données.

		Retour:
			- dict: Un dictionnaire contenant les données organisées par département.

		- La méthode utilise la méthode `recupererDonnees` pour obtenir les données brutes depuis l'URL.
		- Ensuite, elle utilise la méthode `organiserDonnees` pour nettoyer, restructurer et calculer
			les rapports des données électorales par département.

		Notes:
			- S'assurer que les méthodes `recupererDonnees` et `organiserDonnees` fonctionnent correctement.
		"""
		return self.organiserDonnees(self.recupererDonnees(url))



#                                           _   _             _____            _____
#                                          | | (_)           |  __ \          |  __ \
#  _ __ ___  ___ _   _ _ __   ___ _ __ __ _| |_ _  ___  _ __ | |  | | ___  ___| |  | | ___  _ __  _ __   ___  ___  ___
# | '__/ _ \/ __| | | | '_ \ / _ \ '__/ _` | __| |/ _ \| '_ \| |  | |/ _ \/ __| |  | |/ _ \| '_ \| '_ \ / _ \/ _ \/ __|
# | | |  __/ (__| |_| | |_) |  __/ | | (_| | |_| | (_) | | | | |__| |  __/\__ \ |__| | (_) | | | | | | |  __/  __/\__ \
# |_|  \___|\___|\__,_| .__/ \___|_|  \__,_|\__|_|\___/|_| |_|_____/ \___||___/_____/ \___/|_| |_|_| |_|\___|\___||___/
#                     | |
#                     |_|

def recuperationDesDonnees() -> dict:
	"""
	Récupère et organise les données de l'élection présidentielle depuis une URL spécifiée.
	Cette fonction utilise la classe `RecuperationDesDonnees` pour obtenir et organiser les données
	depuis une URL donnée. Elle renvoie un dictionnaire contenant les données organisées par département.

	Retour:
		- dict: Un dictionnaire contenant les données organisées par département.

	- La fonction utilise la classe `RecuperationDesDonnees` pour créer une instance et appelle
		la méthode `obtenirDonnees` avec l'URL spécifiée.
	- Si la récupération des données échoue, un message d'erreur est affiché, et la fonction renvoie None.
	- Sinon, elle renvoie le dictionnaire contenant les données organisées par département.

	Notes:
		- S'assurer que la classe `RecuperationDesDonnees` et la méthode `obtenirDonnees` fonctionnent correctement.
		- L'URL spécifiée est celle de l'élection présidentielle d'avril 2022 en France.
	"""
	database = RecuperationDesDonnees().obtenirDonnees("https://static.data.gouv.fr/resources/election-presidentielle-des-10-et-24-avril-2022-resultats-definitifs-du-1er-tour/20220414-152542/resultats-par-niveau-burvot-t1-france-entiere.txt")

	if not database:
		print("Erreur lors de la récupération des données.")
	return database



if __name__ == '__main__':
	database = recuperationDesDonnees()