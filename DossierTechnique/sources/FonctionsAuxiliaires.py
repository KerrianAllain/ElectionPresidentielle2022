from RecuperationDesDonnees import *



#         __  __ _      _
#        / _|/ _(_)    | |
#   __ _| |_| |_ _  ___| |__   __ _  __ _  ___
#  / _` |  _|  _| |/ __| '_ \ / _` |/ _` |/ _ \
# | (_| | | | | | | (__| | | | (_| | (_| |  __/
#  \__,_|_| |_| |_|\___|_| |_|\__,_|\__, |\___|
#                                    __/ |
#                                   |___/

def affichage(valeur: int) -> str:
	"""
	Affiche une valeur entière avec des espaces de séparation tous les trois chiffres.

	Arguments :
		valeur (int): La valeur entière à afficher.

	Retourne :
		str: La valeur entière formatée avec des espaces de séparation.

	Étapes :
		1. Convertit la valeur en chaîne de caractères et inverse l'ordre des caractères.
		2. Insère un espace tous les trois chiffres.
		3. Retourne la chaîne inversée avec les espaces.
	"""
	valeur = str(valeur)[::-1]
	espaces, chaine = 3, ""

	if len(valeur) <= 3:
		return valeur[::-1]
	else:
		for chiffre in range(len(valeur)):
			if chiffre == espaces:
				chaine += " "
				espaces += 3
			chaine += valeur[chiffre]
		return chaine[::-1]


#            _     _       _____                        _                            _
#           (_)   | |     |  __ \                      | |                          | |
#   _____  ___ ___| |_ ___| |  | | ___ _ __   __ _ _ __| |_ ___ _ __ ___   ___ _ __ | |_
#  / _ \ \/ / / __| __/ _ \ |  | |/ _ \ '_ \ / _` | '__| __/ _ \ '_ ` _ \ / _ \ '_ \| __|
# |  __/>  <| \__ \ ||  __/ |__| |  __/ |_) | (_| | |  | ||  __/ | | | | |  __/ | | | |_
#  \___/_/\_\_|___/\__\___|_____/ \___| .__/ \__,_|_|   \__\___|_| |_| |_|\___|_| |_|\__|
#                                     | |
#                                     |_|

def existeDepartement(database: dict, code_ou_nom: str) -> bool:
	"""
	Vérifie si un département existe dans la base de données.

	Arguments :
		database (dict): Le dictionnaire contenant les données organisées par département.
		code_ou_nom (str): Le code ou le nom du département à vérifier.

	Retourne :
		bool: True si le département existe dans la base de données, False sinon.

	Notes d'utilisation :
		- Si la chaîne contient des chiffres, elle est considérée comme le code du département.
		- Si la chaîne contient des lettres, elle est considérée comme le nom du département.
	"""
	if code_ou_nom.isdigit():
		return code_ou_nom in database
	else:
		for data in database.values():
			if data['Libelle_Departement'].lower() == code_ou_nom.lower():
				return True
		return False


#  _ _     _       _____                        _                            _
# | (_)   | |     |  __ \                      | |                          | |
# | |_ ___| |_ ___| |  | | ___ _ __   __ _ _ __| |_ ___ _ __ ___   ___ _ __ | |_ ___
# | | / __| __/ _ \ |  | |/ _ \ '_ \ / _` | '__| __/ _ \ '_ ` _ \ / _ \ '_ \| __/ __|
# | | \__ \ ||  __/ |__| |  __/ |_) | (_| | |  | ||  __/ | | | | |  __/ | | | |_\__ \
# |_|_|___/\__\___|_____/ \___| .__/ \__,_|_|   \__\___|_| |_| |_|\___|_| |_|\__|___/
#                             | |
#                             |_|

def listeDepartements(database: dict) -> list:
	"""
	Récupère une liste de dictionnaires contenant les données des départements.

	Arguments :
		database (dict): Le dictionnaire contenant les données organisées par département.

	Retourne :
		list: Une liste de dictionnaires contenant les données des départements.
	"""
	liste_departements = []

	for departement in range(len(database)):
		departement_str = str(departement).zfill(2)

		try:
			dictionnaire = recupererDonneesDepartement(database, departement_str)
			if len(dictionnaire) > 0:
				liste_departements.append(dictionnaire)
		except:
			pass
	return liste_departements


#        _     _             _      _____                                   _____                        _                            _
#       | |   | |           (_)    |  __ \                                 |  __ \                      | |                          | |
#   ___ | |__ | |_ ___ _ __  _ _ __| |  | | ___  _ __  _ __   ___  ___  ___| |  | | ___ _ __   __ _ _ __| |_ ___ _ __ ___   ___ _ __ | |_
#  / _ \| '_ \| __/ _ \ '_ \| | '__| |  | |/ _ \| '_ \| '_ \ / _ \/ _ \/ __| |  | |/ _ \ '_ \ / _` | '__| __/ _ \ '_ ` _ \ / _ \ '_ \| __|
# | (_) | |_) | ||  __/ | | | | |  | |__| | (_) | | | | | | |  __/  __/\__ \ |__| |  __/ |_) | (_| | |  | ||  __/ | | | | |  __/ | | | |_
#  \___/|_.__/ \__\___|_| |_|_|_|  |_____/ \___/|_| |_|_| |_|\___|\___||___/_____/ \___| .__/ \__,_|_|   \__\___|_| |_| |_|\___|_| |_|\__|
#                                                                                      | |
#                                                                                      |_|

def obtenirDonneesDepartement(database: dict, code_departement: str) -> dict:
	"""
	Renvoie les données d'un département spécifique à partir du dictionnaire de la base de données.

	Arguments :
		database (dict): Le dictionnaire contenant les données organisées par département.
		code_departement (str): Le code du département dont on veut récupérer les données.

	Retourne :
		dict: Un dictionnaire contenant les données du département correspondant au code spécifié.
	"""
	return database.get(code_departement, {})


#                _                   _          _____                        _                            _
#               | |                 | |        |  __ \                      | |                          | |
#  _ __ ___  ___| |__   ___ _ __ ___| |__   ___| |  | | ___ _ __   __ _ _ __| |_ ___ _ __ ___   ___ _ __ | |_
# | '__/ _ \/ __| '_ \ / _ \ '__/ __| '_ \ / _ \ |  | |/ _ \ '_ \ / _` | '__| __/ _ \ '_ ` _ \ / _ \ '_ \| __|
# | | |  __/ (__| | | |  __/ | | (__| | | |  __/ |__| |  __/ |_) | (_| | |  | ||  __/ | | | | |  __/ | | | |_
# |_|  \___|\___|_| |_|\___|_|  \___|_| |_|\___|_____/ \___| .__/ \__,_|_|   \__\___|_| |_| |_|\___|_| |_|\__|
#                                                          | |
#                                                          |_|

def rechercheDepartement(database: dict) -> None:
	"""
	Permet à l'utilisateur de rechercher un département en saisissant un code ou un libellé partiel.

	La fonction utilise la base de données fournie pour suggérer des options de recherche.
	Une fois l'utilisateur a fait un choix final, la fonction vérifie si le département existe dans la base de données.

	Arguments :
		database (dict): Le dictionnaire contenant les données organisées par département.

	Retourne :
		None: La fonction ne retourne rien, elle imprime les résultats directement.

	Notes :
		- La fonction utilise une boucle infinie pour permettre à l'utilisateur de réessayer jusqu'à ce qu'un choix valide soit effectué.
		- Les suggestions sont basées sur la correspondance du libellé du département ou du code partiel entré par l'utilisateur.
		- L'utilisateur peut choisir parmi les suggestions fournies, et la fonction confirme si le département choisi existe dans la base de données.
	"""
	while True:
		entree_utilisateur = input("Entrez un code de département ou un libellé partiel de département : ")
		suggestions = suggestionRecherche(database, entree_utilisateur)

		if suggestions:
			print("Suggestions de recherche :")
			for suggestion in suggestions:
				print(suggestion)

			choix_final = input("Entrez votre choix final : ")
			if existeDepartement(database, choix_final):
				print(f"Le département '{choix_final}' existe dans la base de données.")
				break
			else:
				print("Veuillez entrer un code ou un libellé valide de département.")
		else:
			print("Aucune suggestion trouvée. Veuillez entrer une autre recherche.")


#                                               _____                                   _____                        _                            _
#                                              |  __ \                                 |  __ \                      | |                          | |
#  _ __ ___  ___ _   _ _ __   ___ _ __ ___ _ __| |  | | ___  _ __  _ __   ___  ___  ___| |  | | ___ _ __   __ _ _ __| |_ ___ _ __ ___   ___ _ __ | |_
# | '__/ _ \/ __| | | | '_ \ / _ \ '__/ _ \ '__| |  | |/ _ \| '_ \| '_ \ / _ \/ _ \/ __| |  | |/ _ \ '_ \ / _` | '__| __/ _ \ '_ ` _ \ / _ \ '_ \| __|
# | | |  __/ (__| |_| | |_) |  __/ | |  __/ |  | |__| | (_) | | | | | | |  __/  __/\__ \ |__| |  __/ |_) | (_| | |  | ||  __/ | | | | |  __/ | | | |_
# |_|  \___|\___|\__,_| .__/ \___|_|  \___|_|  |_____/ \___/|_| |_|_| |_|\___|\___||___/_____/ \___| .__/ \__,_|_|   \__\___|_| |_| |_|\___|_| |_|\__|
#                     | |                                                                          | |
#                     |_|                                                                          |_|

def recupererDonneesDepartement(database: dict, code_ou_nom: str) -> dict:
	"""
	Récupère les données d'un département à partir de la base de données.

	Arguments :
		database (dict): Le dictionnaire contenant les données organisées par département.
		code_ou_nom (str): Le code ou le nom du département dont on veut récupérer les données.

	Retourne :
		dict: Un dictionnaire contenant les données du département correspondant à la chaîne spécifiée.
	"""
	if code_ou_nom.isdigit():
		return obtenirDonneesDepartement(database, code_ou_nom)
	else:
		for code, data in database.items():
			if data['Libelle_Departement'].lower() == code_ou_nom.lower():
				return obtenirDonneesDepartement(database, code)
	return {}


#                                  _   _             _____           _                   _
#                                 | | (_)           |  __ \         | |                 | |
#  ___ _   _  __ _  __ _  ___  ___| |_ _  ___  _ __ | |__) |___  ___| |__   ___ _ __ ___| |__   ___
# / __| | | |/ _` |/ _` |/ _ \/ __| __| |/ _ \| '_ \|  _  // _ \/ __| '_ \ / _ \ '__/ __| '_ \ / _ \
# \__ \ |_| | (_| | (_| |  __/\__ \ |_| | (_) | | | | | \ \  __/ (__| | | |  __/ | | (__| | | |  __/
# |___/\__,_|\__, |\__, |\___||___/\__|_|\___/|_| |_|_|  \_\___|\___|_| |_|\___|_|  \___|_| |_|\___|
#             __/ | __/ |
#            |___/ |___/

def suggestionRecherche(database: dict, entree_utilisateur: str) -> list:
	"""
	Fournit des suggestions de recherche pour un code ou libellé de département.

	Arguments :
		database (dict): Le dictionnaire contenant les données organisées par département.
		entree_utilisateur (str): L'entrée de l'utilisateur (code ou libellé partiel).

	Retourne :
		list: Une liste contenant jusqu'à 10 codes ou libellés correspondant à l'entrée.
	"""
	suggestions = []
	count = 0

	for data in database.values():
		if data['Libelle_Departement'].lower().startswith(entree_utilisateur.lower()):
			suggestions.append(data['Libelle_Departement'])
			count += 1
			if count >= 10:
				break

	if count < 10:
		for code in database.keys():
			if code.startswith(entree_utilisateur):
				if code not in suggestions:
					suggestions.append(code)
					count += 1
			if count >= 10:
				break
	return suggestions



if __name__ == '__main__':
	database = recuperationDesDonnees()