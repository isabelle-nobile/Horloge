class MenuView:
    """La classe qui affiche le menu principal"""

    def __init__(self):
        """Afficher les possibilités du menu principal à l'utilisateur"""

        print("\n\n ---- Clock ----")
        print("\n\n---- Menu principal ----\n")
        print("\nMerci d'entrer un des mots suivant: ")
        print(
            "afficher:             ",
            "Afficher l'heure actuelle",
        )
        print(
            "alarme:             ",
            "Crée une alarme",
        )
        print(
            "mode             ",
            "Choisir le mode d'affichages d'heure ",
        )
        print(
            "quitter:             ",
            "Quitter le programme\n",
        )
        self.command = None

    def launch_command_menu(self):
        """Lance la commande du menu choisi par l'utilisateur"""

        input_option = input("Veuillez rentrer votre option : ")

        if input_option == "afficher":
            self.command = "afficher"
        elif input_option == "alarme":
            self.command = "alarme"
        elif input_option == "mode":
            self.command = "mode" 
        elif input_option == "quitter":
            print("\nMerci d'avoir utilisé ce programme\n")
            self.command = "quitter"
        else:
            print(
                "\nMerci de rentrer la bonne commande comme indiqué",
                "dans les propositions ci-dessous\n",
            )
            self.launch_command_menu()

        return self.command