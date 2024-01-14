from RecuperationDesDonnees import *
from FonctionsAuxiliaires import *
from customtkinter import *
from Graphiques import *



#  _____       _ _   _       _ _           _   _                   _        _ _ _____ _    _ __  __
# |_   _|     (_) | (_)     | (_)         | | (_)                 | |      | ( )_   _| |  | |  \/  |
#   | |  _ __  _| |_ _  __ _| |_ ___  __ _| |_ _  ___  _ __     __| | ___  | |/  | | | |__| | \  / |
#   | | | '_ \| | __| |/ _` | | / __|/ _` | __| |/ _ \| '_ \   / _` |/ _ \ | |   | | |  __  | |\/| |
#  _| |_| | | | | |_| | (_| | | \__ \ (_| | |_| | (_) | | | | | (_| |  __/ | |  _| |_| |  | | |  | |
# |_____|_| |_|_|\__|_|\__,_|_|_|___/\__,_|\__|_|\___/|_| |_|  \__,_|\___| |_| |_____|_|  |_|_|  |_|

database = recuperationDesDonnees()

appearance_value = "light"
set_default_color_theme("blue")
set_appearance_mode(appearance_value)

root = CTk()
# Obtenir les dimensions de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Définir la taille de la fenêtre en fonction des dimensions de l'écran
root.geometry("%dx%d" % (screen_width, screen_height))

# Désactiver la possibilité de redimensionner la fenêtre
root.resizable(width = False, height = False)

# Ajouter un titre et un icône à la fenêtre
root.title("Election présidentielle de 2022")
root.iconbitmap("France.ico")


									  
											  
#   __ _ _ __  _ __   __ _ _ __ ___ _ __   ___ ___
#  / _` | '_ \| '_ \ / _` | '__/ _ \ '_ \ / __/ _ \
# | (_| | |_) | |_) | (_| | | |  __/ | | | (_|  __/
#  \__,_| .__/| .__/ \__,_|_|  \___|_| |_|\___\___|
#       | |   | |
#       |_|   |_|

def apparence():
    """
    Cette fonction alterne entre les modes d'apparence "clair" et "sombre" en modifiant la variable
	globale `appearance_value` et en appelant la fonction `set_appearance_mode()`.

    Arguments:
    	- Aucun argument explicite n'est requis, mais la variable globale `appearance_value` est utilisée.

    Retour:
    	- Aucune valeur de retour explicite n'est générée par cette fonction.

    La fonction utilise un bloc `if-else` pour changer la valeur de `appearance_value` entre "clair"
	et "sombre" et appelle ensuite `set_appearance_mode()` avec cette nouvelle valeur.

    Notes:
    	- Cette fonction utilise une variable globale `appearance_value`, s'assurer qu'elle est correctement initialisée.
    	- La fonction `set_appearance_mode()` est utilisée pour appliquer le changement d'apparence.
    """
    global appearance_value
    appearance_value = "dark" if appearance_value == "light" else "light"
    set_appearance_mode(appearance_value)


#                             _                     ______ _                           _
#                            (_)                   |  ____| |                         | |
#  ___ _   _ _ __  _ __  _ __ _ _ __ ___   ___ _ __| |__  | | ___ _ __ ___   ___ _ __ | |_ ___
# / __| | | | '_ \| '_ \| '__| | '_ ` _ \ / _ \ '__|  __| | |/ _ \ '_ ` _ \ / _ \ '_ \| __/ __|
# \__ \ |_| | |_) | |_) | |  | | | | | | |  __/ |  | |____| |  __/ | | | | |  __/ | | | |_\__ \
# |___/\__,_| .__/| .__/|_|  |_|_| |_| |_|\___|_|  |______|_|\___|_| |_| |_|\___|_| |_|\__|___/
#           | |   | |
#           |_|   |_|

def supprimerElements():
    """
    Cette fonction parcourt tous les widgets enfants de la fenêtre principale (`root`) et les supprime
    en utilisant la méthode `destroy()`.

    Arguments:
    	- Aucun argument explicite n'est requis.

    Retour:
    	- Aucune valeur de retour explicite n'est générée par cette fonction.

    La fonction utilise une boucle `for` pour parcourir tous les widgets enfants de la fenêtre principale.
    Pour chaque widget, la méthode `destroy()` est appelée, entraînant la suppression du widget.

    Notes:
	    - S'assurer que la variable `root` est correctement définie avant d'appeler cette fonction.
	    - Cette fonction ne renvoie aucune valeur.
    """
    for widget in root.winfo_children():
        widget.destroy()


#  _    _                      _____
# | |  | |                    |  __ \
# | |__| | ___  _ __ ___   ___| |__) |_ _  __ _  ___
# |  __  |/ _ \| '_ ` _ \ / _ \  ___/ _` |/ _` |/ _ \
# | |  | | (_) | | | | | |  __/ |  | (_| | (_| |  __/
# |_|  |_|\___/|_| |_| |_|\___|_|   \__,_|\__, |\___|
#                                          __/ |
#                                         |___/

class HomePage:
	def __init__(self):
		"""
		Initialise la page d'accueil avec une barre de recherche, des boutons de suggestions, un bouton de recherche,
		un bouton pour actualiser la page, et un bouton pour afficher les chiffres graphiques à l'échelle nationale.
		Les boutons servent à afficher les 10 premiers résultats commençant par ce que l'utilisateur a entré.
		"""

		# Initialisation des variables de la page d'accueil
		self.entreeUtilisateur = ""
		self.indice_entree = 0
		self.taille_entree = 0
		self.listeSug = []
		self.numBouton = 0

		# Placement de tous les boutons et l'entrée sur la fenêtre
		# L'entrée est définit avec un placeholder_text qui permet d'avoir un texte de base dans l'entrée pour que l'utilisateur sache ce qu'il doit faire
		self.my_entry = CTkEntry(root, placeholder_text="Entrez le nom ou le code du département", width=650, height=50, font=("Arial", 18), corner_radius=50)
		self.my_entry.grid(row=0, column=0, sticky=W, pady=25, padx=25)
		self.my_entry.bind("<Key>", self.intercepte)

		self.button_Rechercher = CTkButton(root, text="Rechercher", command=self.entree, height=50, font=("Arial", 18))
		self.button_Rechercher.grid(row=0, column=1, sticky=W, padx=0)

		self.button_Actualiser = CTkButton(root, text="Actualiser", command=self.actualiser, height=50, font=("Arial", 18))
		self.button_Actualiser.grid(row=0, column=2, sticky=W, padx=25)

		self.button_National = CTkButton(root, text="National", command=self.national, height=50, font=("Arial", 18))
		self.button_National.grid(row=1, column=1, sticky=W, padx=0)

		self.button_Theme = CTkButton(root, text="Thème", command=self.appearanceSelf)
		self.button_Theme.grid(row=10, column=2, sticky=W, padx=0)

		# Les boutons de suggestions sont définits sans nom
		self.button1 = CTkButton(root, text="", width=650, height=50, font=("Arial", 18), corner_radius=50, anchor="w", command=self.boutonsValeur1)
		self.button1.grid(row=1, column=0, sticky=W, padx=25)

		self.button2 = CTkButton(root, text="", width=650, height=50, font=("Arial", 18), corner_radius=50, anchor="w", command=self.boutonsValeur2)
		self.button2.grid(row=2, column=0, sticky=W, padx=25)

		self.button3 = CTkButton(root, text="", width=650, height=50, font=("Arial", 18), corner_radius=50, anchor="w", command=self.boutonsValeur3)
		self.button3.grid(row=3, column=0, sticky=W, padx=25)

		self.button4 = CTkButton(root, text="", width=650, height=50, font=("Arial", 18), corner_radius=50, anchor="w", command=self.boutonsValeur4)
		self.button4.grid(row=4, column=0, sticky=W, padx=25)

		self.button5 = CTkButton(root, text="", width=650, height=50, font=("Arial", 18), corner_radius=50, anchor="w", command=self.boutonsValeur5)
		self.button5.grid(row=5, column=0, sticky=W, padx=25)

		self.button6 = CTkButton(root, text="", width=650, height=50, font=("Arial", 18), corner_radius=50, anchor="w", command=self.boutonsValeur6)
		self.button6.grid(row=6, column=0, sticky=W, padx=25)

		self.button7 = CTkButton(root, text="", width=650, height=50, font=("Arial", 18), corner_radius=50, anchor="w", command=self.boutonsValeur7)
		self.button7.grid(row=7, column=0, sticky=W, padx=25)

		self.button8 = CTkButton(root, text="", width=650, height=50, font=("Arial", 18), corner_radius=50, anchor="w", command=self.boutonsValeur8)
		self.button8.grid(row=8, column=0, sticky=W, padx=25)

		self.button9 = CTkButton(root, text="", width=650, height=50, font=("Arial", 18), corner_radius=50, anchor="w", command=self.boutonsValeur9)
		self.button9.grid(row=9, column=0, sticky=W, padx=25)

		self.button10 = CTkButton(root, text="", width=650, height=50, font=("Arial", 18), corner_radius=50, anchor="w", command=self.boutonsValeur10)
		self.button10.grid(row=10, column=0, sticky=W, padx=25)

		# On règle la couleur de la fenêtre et des boutons
		self.appearanceSelf("initialisation des couleurs de boutons")


	#                                                         _____      _  __
	#                                                        / ____|    | |/ _|
	#   __ _ _ __  _ __   ___  __ _ _ __ __ _ _ __   ___ ___| (___   ___| | |_
	#  / _` | '_ \| '_ \ / _ \/ _` | '__/ _` | '_ \ / __/ _ \\___ \ / _ \ |  _|
	# | (_| | |_) | |_) |  __/ (_| | | | (_| | | | | (_|  __/____) |  __/ | |
	#  \__,_| .__/| .__/ \___|\__,_|_|  \__,_|_| |_|\___\___|_____/ \___|_|_|
	#       | |   | |
	#       |_|   |_|

	def appearanceSelf(self, valeur="boutton"):
		"""
		Change le thème de la page.
		Appelée lors de l'instanciation de l'objet PageAccueil et par le bouton Thème.
		Appelle la fonction self.remplirBouttons() pour que les boutons s'adaptent à ce changement de thème.
		
		Arguments :
			valeur (str): Valeur par défaut "boutton", détermine si la fonction a été appelée par le bouton Thème.

		Notes:
			La couleur des boutons est également ajustée en fonction du thème choisi.
		"""
		if valeur == "boutton":
			apparence()
		if appearance_value == "light":
			self.button_Theme.configure(fg_color="gray80", hover_color="gray68", text_color="gray2")
		else:
			self.button_Theme.configure(fg_color="gray10", hover_color="gray5", text_color="gray98")
		self.remplirBoutons()


	#             _               _ _
	#            | |             | (_)
	#   __ _  ___| |_ _   _  __ _| |_ ___  ___ _ __
	#  / _` |/ __| __| | | |/ _` | | / __|/ _ \ '__|
	# | (_| | (__| |_| |_| | (_| | | \__ \  __/ |
	#  \__,_|\___|\__|\__,_|\__,_|_|_|___/\___|_|

	def actualiser(self):
		"""
		Réinitialise la page d'accueil.
		Appelée par le bouton Actualiser.
		"""
		self.__init__()


	#             _
	#            | |
	#   ___ _ __ | |_ _ __ ___  ___
	#  / _ \ '_ \| __| '__/ _ \/ _ \
	# |  __/ | | | |_| | |  __/  __/
	#  \___|_| |_|\__|_|  \___|\___|

	def entree(self):
		"""
		Vérifie si l'utilisateur a rentré un département existant en France.
		Appelée par le bouton Rechercher ou si l'utilisateur appuie sur la touche Entrée dans l'entrée de recherche.

		Notes:
			Si l'entrée est vide, avertit l'utilisateur. Si le département n'existe pas, affiche un message d'avertissement.
			Si le département existe, supprime tout sur la fenêtre et affiche la page de recherche avec le département en paramètre.
		"""
		if self.entreeUtilisateur == "":
			self.listeSug = []
			self.remplirBoutons()
			self.button1.configure(text="Vous n'avez pas rempli le champ de saisie")
			if appearance_value == "light":
				self.button1.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button1.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")
		else:
			if not existeDepartement(database, self.entreeUtilisateur):
				self.listeSug = []
				self.remplirBoutons()
				self.button1.configure(text="Ce département n'existe pas en France")
			else:
				supprimerElements()
				PageRecherche = GraphPage(self.entreeUtilisateur)


	#              _   _                   _
	#             | | (_)                 | |
	#  _ __   __ _| |_ _  ___  _ __   __ _| |
	# | '_ \ / _` | __| |/ _ \| '_ \ / _` | |
	# | | | | (_| | |_| | (_) | | | | (_| | |
	# |_| |_|\__,_|\__|_|\___/|_| |_|\__,_|_|

	def national(self):
		"""Affiche la page de recherche avec l'échelle nationale.

		Notes:
			Supprime tous les éléments sur la fenêtre et appelle la classe GraphPage avec "national" en paramètre.
		"""
		supprimerElements()
		PageRecherche = GraphPage("national")


	#  _                 _   _               __      __   _                __
	# | |               | | | |              \ \    / /  | |              /_ |
	# | |__   ___  _   _| |_| |_ ___  _ __  __\ \  / /_ _| | ___ _   _ _ __| |
	# | '_ \ / _ \| | | | __| __/ _ \| '_ \/ __\ \/ / _` | |/ _ \ | | | '__| |
	# | |_) | (_) | |_| | |_| || (_) | | | \__ \\  / (_| | |  __/ |_| | |  | |
	# |_.__/ \___/ \__,_|\__|\__\___/|_| |_|___/ \/ \__,_|_|\___|\__,_|_|  |_|

	def boutonsValeur1(self):
		"""Récupère la valeur du bouton1 et l'assigne à l'entrée utilisateur.

		Notes:
			Si le bouton affiche un message d'erreur, rien ne change.
		"""
		bout = self.button1.cget("text")
		if bout != "" and bout != "Ce département n'existe pas en France" and bout != "Vous n'avez pas rempli le champs de saisie":
			self.my_entry.delete(0, END)
			self.my_entry.insert(0, bout)
			self.entreeUtilisateur = bout
			self.taille_entree = len(self.entreeUtilisateur)
			self.indice_entree = self.taille_entree
			self.numBouton = 1


	#  _                 _   _               __      __   _               ___
	# | |               | | | |              \ \    / /  | |             |__ \
	# | |__   ___  _   _| |_| |_ ___  _ __  __\ \  / /_ _| | ___ _   _ _ __ ) |
	# | '_ \ / _ \| | | | __| __/ _ \| '_ \/ __\ \/ / _` | |/ _ \ | | | '__/ /
	# | |_) | (_) | |_| | |_| || (_) | | | \__ \\  / (_| | |  __/ |_| | | / /_
	# |_.__/ \___/ \__,_|\__|\__\___/|_| |_|___/ \/ \__,_|_|\___|\__,_|_||____|

	def boutonsValeur2(self):
		"""Récupère la valeur du bouton2 et l'assigne à l'entrée utilisateur."""
		bout = self.button2.cget("text")
		if bout != "":
			self.my_entry.delete(0, END)
			self.my_entry.insert(0, bout)
			self.entreeUtilisateur = bout
			self.taille_entree = len(self.entreeUtilisateur)
			self.indice_entree = self.taille_entree
			self.numBouton = 2


	#  _                 _   _               __      __   _                ____
	# | |               | | | |              \ \    / /  | |              |___ \
	# | |__   ___  _   _| |_| |_ ___  _ __  __\ \  / /_ _| | ___ _   _ _ __ __) |
	# | '_ \ / _ \| | | | __| __/ _ \| '_ \/ __\ \/ / _` | |/ _ \ | | | '__|__ <
	# | |_) | (_) | |_| | |_| || (_) | | | \__ \\  / (_| | |  __/ |_| | |  ___) |
	# |_.__/ \___/ \__,_|\__|\__\___/|_| |_|___/ \/ \__,_|_|\___|\__,_|_| |____/

	def boutonsValeur3(self):
		"""Récupère la valeur du bouton3 et l'assigne à l'entrée utilisateur."""
		bout = self.button3.cget("text")
		if bout != "":
			self.my_entry.delete(0, END)
			self.my_entry.insert(0, bout)
			self.entreeUtilisateur = bout
			self.taille_entree = len(self.entreeUtilisateur)
			self.indice_entree = self.taille_entree
			self.numBouton = 3


	#  _                 _   _               __      __   _                 _  _
	# | |               | | | |              \ \    / /  | |               | || |
	# | |__   ___  _   _| |_| |_ ___  _ __  __\ \  / /_ _| | ___ _   _ _ __| || |_
	# | '_ \ / _ \| | | | __| __/ _ \| '_ \/ __\ \/ / _` | |/ _ \ | | | '__|__   _|
	# | |_) | (_) | |_| | |_| || (_) | | | \__ \\  / (_| | |  __/ |_| | |     | |
	# |_.__/ \___/ \__,_|\__|\__\___/|_| |_|___/ \/ \__,_|_|\___|\__,_|_|     |_|

	def boutonsValeur4(self):
		"""Récupère la valeur du bouton4 et l'assigne à l'entrée utilisateur."""
		bout = self.button4.cget("text")
		if bout != "":
			self.my_entry.delete(0, END)
			self.my_entry.insert(0, bout)
			self.entreeUtilisateur = bout
			self.taille_entree = len(self.entreeUtilisateur)
			self.indice_entree = self.taille_entree
			self.numBouton = 4


	#  _                 _   _               __      __   _                 _____
	# | |               | | | |              \ \    / /  | |               | ____|
	# | |__   ___  _   _| |_| |_ ___  _ __  __\ \  / /_ _| | ___ _   _ _ __| |__
	# | '_ \ / _ \| | | | __| __/ _ \| '_ \/ __\ \/ / _` | |/ _ \ | | | '__|___ \
	# | |_) | (_) | |_| | |_| || (_) | | | \__ \\  / (_| | |  __/ |_| | |   ___) |
	# |_.__/ \___/ \__,_|\__|\__\___/|_| |_|___/ \/ \__,_|_|\___|\__,_|_|  |____/

	def boutonsValeur5(self):
		"""Récupère la valeur du bouton5 et l'assigne à l'entrée utilisateur."""
		bout = self.button5.cget("text")
		if bout != "":
			self.my_entry.delete(0, END)
			self.my_entry.insert(0, bout)
			self.entreeUtilisateur = bout
			self.taille_entree = len(self.entreeUtilisateur)
			self.indice_entree = self.taille_entree
			self.numBouton = 5


	#  _                 _   _               __      __   _                   __
	# | |               | | | |              \ \    / /  | |                 / /
	# | |__   ___  _   _| |_| |_ ___  _ __  __\ \  / /_ _| | ___ _   _ _ __ / /_
	# | '_ \ / _ \| | | | __| __/ _ \| '_ \/ __\ \/ / _` | |/ _ \ | | | '__| '_ \
	# | |_) | (_) | |_| | |_| || (_) | | | \__ \\  / (_| | |  __/ |_| | |  | (_) |
	# |_.__/ \___/ \__,_|\__|\__\___/|_| |_|___/ \/ \__,_|_|\___|\__,_|_|   \___/

	def boutonsValeur6(self):
		"""Récupère la valeur du bouton6 et l'assigne à l'entrée utilisateur."""
		bout = self.button6.cget("text")
		if bout != "":
			self.my_entry.delete(0, END)
			self.my_entry.insert(0, bout)
			self.entreeUtilisateur = bout
			self.taille_entree = len(self.entreeUtilisateur)
			self.indice_entree = self.taille_entree
			self.numBouton = 6


	#  _                 _   _               __      __   _              ______
	# | |               | | | |              \ \    / /  | |            |____  |
	# | |__   ___  _   _| |_| |_ ___  _ __  __\ \  / /_ _| | ___ _   _ _ __ / /
	# | '_ \ / _ \| | | | __| __/ _ \| '_ \/ __\ \/ / _` | |/ _ \ | | | '__/ /
	# | |_) | (_) | |_| | |_| || (_) | | | \__ \\  / (_| | |  __/ |_| | | / /
	# |_.__/ \___/ \__,_|\__|\__\___/|_| |_|___/ \/ \__,_|_|\___|\__,_|_|/_/

	def boutonsValeur7(self):
		"""Récupère la valeur du bouton7 et l'assigne à l'entrée utilisateur."""
		bout = self.button7.cget("text")
		if bout != "":
			self.my_entry.delete(0, END)
			self.my_entry.insert(0, bout)
			self.entreeUtilisateur = bout
			self.taille_entree = len(self.entreeUtilisateur)
			self.indice_entree = self.taille_entree
			self.numBouton = 7


	#  _                 _   _               __      __   _                 ___
	# | |               | | | |              \ \    / /  | |               / _ \
	# | |__   ___  _   _| |_| |_ ___  _ __  __\ \  / /_ _| | ___ _   _ _ _| (_) |
	# | '_ \ / _ \| | | | __| __/ _ \| '_ \/ __\ \/ / _` | |/ _ \ | | | '__> _ <
	# | |_) | (_) | |_| | |_| || (_) | | | \__ \\  / (_| | |  __/ |_| | | | (_) |
	# |_.__/ \___/ \__,_|\__|\__\___/|_| |_|___/ \/ \__,_|_|\___|\__,_|_|  \___/

	def boutonsValeur8(self):
		"""Récupère la valeur du bouton8 et l'assigne à l'entrée utilisateur."""
		bout = self.button8.cget("text")
		if bout != "":
			self.my_entry.delete(0, END)
			self.my_entry.insert(0, bout)
			self.entreeUtilisateur = bout
			self.taille_entree = len(self.entreeUtilisateur)
			self.indice_entree = self.taille_entree
			self.numBouton = 8


	#  _                 _   _               __      __   _                 ___
	# | |               | | | |              \ \    / /  | |               / _ \
	# | |__   ___  _   _| |_| |_ ___  _ __  __\ \  / /_ _| | ___ _   _ _ _| (_) |
	# | '_ \ / _ \| | | | __| __/ _ \| '_ \/ __\ \/ / _` | |/ _ \ | | | '__\__, |
	# | |_) | (_) | |_| | |_| || (_) | | | \__ \\  / (_| | |  __/ |_| | |    / /
	# |_.__/ \___/ \__,_|\__|\__\___/|_| |_|___/ \/ \__,_|_|\___|\__,_|_|   /_/

	def boutonsValeur9(self):
		"""Récupère la valeur du bouton9 et l'assigne à l'entrée utilisateur."""
		bout = self.button9.cget("text")
		if bout != "":
			self.my_entry.delete(0, END)
			self.my_entry.insert(0, bout)
			self.entreeUtilisateur = bout
			self.taille_entree = len(self.entreeUtilisateur)
			self.indice_entree = self.taille_entree
			self.numBouton = 9


	#  _                 _   _               __      __   _                __  ___
	# | |               | | | |              \ \    / /  | |              /_ |/ _ \
	# | |__   ___  _   _| |_| |_ ___  _ __  __\ \  / /_ _| | ___ _   _ _ __| | | | |
	# | '_ \ / _ \| | | | __| __/ _ \| '_ \/ __\ \/ / _` | |/ _ \ | | | '__| | | | |
	# | |_) | (_) | |_| | |_| || (_) | | | \__ \\  / (_| | |  __/ |_| | |  | | |_| |
	# |_.__/ \___/ \__,_|\__|\__\___/|_| |_|___/ \/ \__,_|_|\___|\__,_|_|  |_|\___/

	def boutonsValeur10(self):
		"""Récupère la valeur du bouton10 et l'assigne à l'entrée utilisateur."""
		bout = self.button10.cget("text")
		if bout != "":
			self.my_entry.delete(0, END)
			self.my_entry.insert(0, bout)
			self.entreeUtilisateur = bout
			self.taille_entree = len(self.entreeUtilisateur)
			self.indice_entree = self.taille_entree
			self.numBouton = 10


	#  _                 _              _    _ ____
	# | |               | |            | |  | |  _ \
	# | |__   ___  _   _| |_ ___  _ __ | |__| | |_) |
	# | '_ \ / _ \| | | | __/ _ \| '_ \|  __  |  _ <
	# | |_) | (_) | |_| | || (_) | | | | |  | | |_) |
	# |_.__/ \___/ \__,_|\__\___/|_| |_|_|  |_|____/

	def boutonHB(self):
		"""Appelle la fonction correspondante self.boutonsValeur en fonction de self.numBouton.

		Notes:
			Cette fonction est appelée lorsque la flèche du bas ou celle du haut est pressée.
			Elle insère dans l'entrée la valeur du bouton.
		"""
		if 1 <= self.numBouton <= 10:
			getattr(self, f"boutonsValeur{self.numBouton}")()


	#             _                  __      __   _
	#            | |                 \ \    / /  | |
	#   ___ _ __ | | _____   _____ _ _\ \  / /_ _| | ___ _   _ _ __
	#  / _ \ '_ \| |/ _ \ \ / / _ \ '__\ \/ / _` | |/ _ \ | | | '__|
	# |  __/ | | | |  __/\ V /  __/ |   \  / (_| | |  __/ |_| | |
	#  \___|_| |_|_|\___| \_/ \___|_|    \/ \__,_|_|\___|\__,_|_|

	def enleverValeur(self):
		"""Gère les éventuelles suppressions de caractères dans self.entreeUtilisateur en tenant compte de l'emplacement du curseur avec la touche supprimer.

		Returns:
			str: Chaîne mise à jour après suppression de caractères.
		"""
		entree = ""
		for i in range(self.taille_entree):
			if i != self.indice_entree - 1:
				entree = entree + self.entreeUtilisateur[i]
		self.entreeUtilisateur = entree
		return self.entreeUtilisateur


	#  _
	# (_)
	#  _ _ __  ___  ___ _ __ ___ _ __
	# | | '_ \/ __|/ _ \ '__/ _ \ '__|
	# | | | | \__ \  __/ | |  __/ |
	# |_|_| |_|___/\___|_|  \___|_|

	def inserer(self, button):
		"""Gère les insertions de caractères dans self.entreeUtilisateur en tenant compte de l'emplacement du curseur.

		Arguments :
			button (str): Caractère à insérer.

		Returns:
			str: Chaîne mise à jour après l'insertion de caractères.
		"""
		if self.indice_entree == self.taille_entree:
			self.entreeUtilisateur = self.entreeUtilisateur + button
		elif self.indice_entree == 0:
			self.entreeUtilisateur = button + self.entreeUtilisateur
		else:
			entree = ""
			for i in range(self.taille_entree):
				if i == self.indice_entree:
					entree = entree + button
				entree = entree + self.entreeUtilisateur[i]
			self.entreeUtilisateur = entree
		return self.entreeUtilisateur


	#  _       _                          _
	# (_)     | |                        | |
	#  _ _ __ | |_ ___ _ __ ___ ___ _ __ | |_ ___
	# | | '_ \| __/ _ \ '__/ __/ _ \ '_ \| __/ _ \
	# | | | | | ||  __/ | | (_|  __/ |_) | ||  __/
	# |_|_| |_|\__\___|_|  \___\___| .__/ \__\___|
	#                              | |
	#                              |_|

	def intercepte(self, button):
		"""Appelée en cas d'appui sur une touche, cette fonction vérifie si ce qui a été entré dans la barre de recherche a changé.
		Si oui, réinitialise les suggestions présentes dans les boutons.
		Lorsque quelque chose est affiché dans un bouton, ce bouton devient plus foncé, et s'il est vide, il prend la même couleur que le fond de l'écran en gérant le mode clair ou sombre.

		Arguments :
			button (Event): L'événement de la touche pressée.
		"""
		# Vérifie si la touche pressée est la touche de suppression
		if button.keycode == 8:
			if self.indice_entree != 0:
				self.enleverValeur()
				if self.taille_entree > 0:
					self.taille_entree -= 1
					self.indice_entree -= 1
		
		# Vérifie si la touche pressée est la touche de suppression Suppr
		elif button.keycode == 46:
			if self.indice_entree < self.taille_entree:
				self.indice_entree += 1
				self.enleverValeur()
				self.taille_entree -= 1
				self.indice_entree -= 1

		# Vérifie si la touche pressée est la flèche de gauche
		elif button.keycode == 37:
			if self.indice_entree > 0:
				self.indice_entree -= 1

		# Vérifie si la touche pressée est la flèche de droite
		elif button.keycode == 39:
			if self.indice_entree < self.taille_entree:
				self.indice_entree += 1

		# Vérifie si la touche pressée est la flèche de haut
		elif button.keycode == 38:
			if self.numBouton > 1:
				self.numBouton -= 1
				return self.boutonHB()
			else:
				self.numBouton = len(self.listeSug)
				return self.boutonHB()

		# Vérifie si la touche pressée est la flèche de bas
		elif button.keycode == 40:
			if self.numBouton < len(self.listeSug):
				self.numBouton += 1
				return self.boutonHB()
			else:
				self.numBouton = 1
				return self.boutonHB()

		# Vérifie si la touche pressée est la touche entrée
		elif button.keycode == 13:
			return self.entree()

		# Vérifie si la touche pressée est une lettre, un chiffre ou un caractère autre
		if 65 <= button.keycode <= 90 or 48 <= button.keycode <= 57 or 96 <= button.keycode <= 111 or 185 <= button.keycode <= 226:
			self.inserer(button.char)
			self.indice_entree += 1
			self.taille_entree += 1

		if self.entreeUtilisateur != "":    
			self.listeSug = suggestionRecherche(database, self.entreeUtilisateur)
		else:
			self.listeSug = []
		self.numBouton = 0
		self.remplirBoutons()


	#                           _ _      ____              _
	#                          | (_)    |  _ \            | |
	#  _ __ ___ _ __ ___  _ __ | |_ _ __| |_) | ___  _   _| |_ ___  _ __  ___
	# | '__/ _ \ '_ ` _ \| '_ \| | | '__|  _ < / _ \| | | | __/ _ \| '_ \/ __|
	# | | |  __/ | | | | | |_) | | | |  | |_) | (_) | |_| | || (_) | | | \__ \
	# |_|  \___|_| |_| |_| .__/|_|_|_|  |____/ \___/ \__,_|\__\___/|_| |_|___/
	#                    | |
	#                    |_|

	def remplirBoutons(self):
		"""Remplit les boutons en fonction de la liste des suggestions et du thème choisi."""
		# Si aucun résultat n'est trouvé pour ce que l'utilisateur a entré, cela doit être indiqué
		if len(self.listeSug) == 0 and self.entreeUtilisateur != "":
			self.button1.configure(text="Ce département n'existe pas en France")
			if appearance_value == "light":
				self.button1.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button1.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")
		else:
			self.button1.configure(text="")
			if appearance_value == "light":
				self.button1.configure(fg_color="gray92", hover_color="gray92")
			else:
				self.button1.configure(fg_color="gray14", hover_color="gray14")

		if len(self.listeSug) >= 1:
			self.button1.configure(text=self.listeSug[0])
			if appearance_value == "light":
				self.button1.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button1.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")

		if len(self.listeSug) >= 2:
			self.button2.configure(text=self.listeSug[1])
			if appearance_value == "light":
				self.button2.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button2.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")
		else:
			self.button2.configure(text="")
			if appearance_value == "light":
				self.button2.configure(fg_color="gray92", hover_color="gray92")
			else:
				self.button2.configure(fg_color="gray14", hover_color="gray14")

		if len(self.listeSug) >= 3:
			self.button3.configure(text=self.listeSug[2])
			if appearance_value == "light":
				self.button3.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button3.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")
		else:
			self.button3.configure(text="")
			if appearance_value == "light":
				self.button3.configure(fg_color="gray92", hover_color="gray92")
			else:
				self.button3.configure(fg_color="gray14", hover_color="gray14")

		if len(self.listeSug) >= 4:
			self.button4.configure(text=self.listeSug[3])
			if appearance_value == "light":
				self.button4.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button4.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")
		else:
			self.button4.configure(text="")
			if appearance_value == "light":
				self.button4.configure(fg_color="gray92", hover_color="gray92")
			else:
				self.button4.configure(fg_color="gray14", hover_color="gray14")

		if len(self.listeSug) >= 5:
			self.button5.configure(text=self.listeSug[4])
			if appearance_value == "light":
				self.button5.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button5.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")
		else:
			self.button5.configure(text="")
			if appearance_value == "light":
				self.button5.configure(fg_color="gray92", hover_color="gray92")
			else:
				self.button5.configure(fg_color="gray14", hover_color="gray14")

		if len(self.listeSug) >= 6:
			self.button6.configure(text=self.listeSug[5])
			if appearance_value == "light":
				self.button6.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button6.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")
		else:
			self.button6.configure(text="")
			if appearance_value == "light":
				self.button6.configure(fg_color="gray92", hover_color="gray92")
			else:
				self.button6.configure(fg_color="gray14", hover_color="gray14")

		if len(self.listeSug) >= 7:
			self.button7.configure(text=self.listeSug[6])
			if appearance_value == "light":
				self.button7.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button7.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")
		else:
			self.button7.configure(text="")
			if appearance_value == "light":
				self.button7.configure(fg_color="gray92", hover_color="gray92")
			else:
				self.button7.configure(fg_color="gray14", hover_color="gray14")

		if len(self.listeSug) >= 8:
			self.button8.configure(text=self.listeSug[7])
			if appearance_value == "light":
				self.button8.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button8.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")
		else:
			self.button8.configure(text="")
			if appearance_value == "light":
				self.button8.configure(fg_color="gray92", hover_color="gray92")
			else:
				self.button8.configure(fg_color="gray14", hover_color="gray14")

		if len(self.listeSug) >= 9:
			self.button9.configure(text=self.listeSug[8])
			if appearance_value == "light":
				self.button9.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button9.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")
		else:
			self.button9.configure(text="")
			if appearance_value == "light":
				self.button9.configure(fg_color="gray92", hover_color="gray92")
			else:
				self.button9.configure(fg_color="gray14", hover_color="gray14")

		if len(self.listeSug) >= 10:
			self.button10.configure(text=self.listeSug[9])
			if appearance_value == "light":
				self.button10.configure(fg_color="gray87", hover_color="gray75", text_color="gray2")
			else:
				self.button10.configure(fg_color="gray9", hover_color="gray5", text_color="gray98")
		else:
			self.button10.configure(text="")
			if appearance_value == "light":
				self.button10.configure(fg_color="gray92", hover_color="gray92")
			else:
				self.button10.configure(fg_color="gray14", hover_color="gray14")



#   _____                 _     _____
#  / ____|               | |   |  __ \
# | |  __ _ __ __ _ _ __ | |__ | |__) |_ _  __ _  ___
# | | |_ | '__/ _` | '_ \| '_ \|  ___/ _` |/ _` |/ _ \
# | |__| | | | (_| | |_) | | | | |  | (_| | (_| |  __/
#  \_____|_|  \__,_| .__/|_| |_|_|   \__,_|\__, |\___|
#                  | |                      __/ |
#                  |_|                     |___/

class GraphPage:
	def __init__(self, user_answer):
		"""On actualiser une page d'affichage de graphique. Elle est appelé par la class HomePage avec l'entrée de l'utilisateur.
		Sur cette page une place un label avec le nom/libellé du département que l'on a rentrer, même si on a rentrer son code.
		Puis il y un boutons pour afficher le graphique en secteur et un en barres. Un bouton pour retourner à la page d'accueil.
		Et enfin un boutton pour changer le thème de la page."""
		# Initialisation des variables de la page d'accueil
		self.departement = str(user_answer)
		if self.departement == "national":
			self.departement = "National"
		else:
			self.donneesDep = recupererDonneesDepartement(database, self.departement)
			self.departement = self.donneesDep['Libelle_Departement']

		# Placement de tous les boutons et l'entrée sur la fenêtre
		# L'entrée est définit avec un placeholder_text qui permet d'avoir un texte de base dans l'entrée pour que l'utilisateur sache ce qu'il doit faire
		self.label = CTkLabel(root, text = self.departement, font=("Arial", 25))
		self.label.grid(row=0, column=2, sticky=N, pady=50)

		self.button_Accueil = CTkButton(root, text="Accueil", command=self.acceuil, height=50, font=("Arial", 18))
		self.button_Accueil.grid(row=1, column=3, sticky=N, padx=100, pady=50)

		self.button_Theme = CTkButton(root, text="Thème", command=self.apparenceSelf)
		self.button_Theme.grid(row=4, column=3, sticky=N, padx=100, pady=285)

		self.button_Graph_Secteurs = CTkButton(root, text="Graphique en secteurs", command=self.secteurs, height=50, font=("Arial", 18))
		self.button_Graph_Secteurs.grid(row=1, column=1, sticky=N, padx=100, pady=50)

		self.button_Graph_Barres = CTkButton(root, text="Graphique en barres", command=self.barres, height=50, font=("Arial", 18))
		self.button_Graph_Barres.grid(row=1, column=2, sticky=N, padx=60, pady=50)

		# On règle la couleur de la fenêtre et du thème
		self.apparenceSelf("initialisation de la du bouton")


	#                           _ _
	#                          (_) |
	#   __ _  ___ ___ ___ _   _ _| |
	#  / _` |/ __/ __/ _ \ | | | | |
	# | (_| | (_| (_|  __/ |_| | | |
	#  \__,_|\___\___\___|\__,_|_|_|

	def acceuil(self):
		"""Renvoie à la page d'accueil en supprimant tous les éléments actuels de la fenêtre.

		Paramètres:
		Aucun.

		Renvoie:
		Aucun retour, mais redirige vers la page d'accueil.
		"""
		supprimerElements()
		PageAcceuil = HomePage()

	#                                                   _____      _  __
	#                                                  / ____|    | |/ _|
	#   __ _ _ __  _ __   __ _ _ __ ___ _ __   ___ ___| (___   ___| | |_
	#  / _` | '_ \| '_ \ / _` | '__/ _ \ '_ \ / __/ _ \\___ \ / _ \ |  _|
	# | (_| | |_) | |_) | (_| | | |  __/ | | | (_|  __/____) |  __/ | |
	#  \__,_| .__/| .__/ \__,_|_|  \___|_| |_|\___\___|_____/ \___|_|_|
	#       | |   | |
	#       |_|   |_|

	def apparenceSelf(self, valeur="boutton"):
		"""Change le thème de la page en fonction de la valeur fournie.

		Paramètres:
		- valeur (str): La valeur détermine le thème. Par défaut, "boutton" indique le changement en fonction du bouton Thème.

		Renvoie:
		Aucun retour, mais ajuste l'apparence de la page en fonction du thème.
		"""
		if valeur == "boutton":
			apparence()
		if appearance_value == "light":
			self.button_Theme.configure(fg_color="gray80", hover_color="gray68", text_color="gray2")
		else:
			self.button_Theme.configure(fg_color="gray10", hover_color="gray5", text_color="gray98")


	#                _
	#               | |
	#  ___  ___  ___| |_ ___ _   _ _ __ ___
	# / __|/ _ \/ __| __/ _ \ | | | '__/ __|
	# \__ \  __/ (__| ||  __/ |_| | |  \__ \
	# |___/\___|\___|\__\___|\__,_|_|  |___/

	def secteurs(self):
		"""Affiche un graphique en secteurs en fonction de l'échelle choisie (nationale ou départementale).

		Paramètres:
		Aucun.

		Renvoie:
		Aucun retour, mais affiche le graphique en secteurs dans une fenêtre matplotlib.
		"""
		if self.departement == "National":
			graphiqueCirculaire(listeDepartements(database))
		else:
			graphiqueCirculaire(self.donneesDep)


	#  _
	# | |
	# | |__   __ _ _ __ _ __ ___  ___
	# | '_ \ / _` | '__| '__/ _ \/ __|
	# | |_) | (_| | |  | | |  __/\__ \
	# |_.__/ \__,_|_|  |_|  \___||___/

	def barres(self):
		"""Affiche un graphique en barres en fonction de l'échelle choisie (nationale ou départementale).

		Paramètres:
		Aucun.

		Renvoie:
		Aucun retour, mais affiche le graphique en barres dans une fenêtre matplotlib.
		"""
		if self.departement == "National":
			graphiqueBarre(listeDepartements(database))
		else:
			graphiqueBarre(self.donneesDep)


PageAccueil=HomePage()


root.mainloop()