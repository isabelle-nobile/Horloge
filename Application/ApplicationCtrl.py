import sys
from os import system, name
import View.MenuView as MenuView
from Application.HorlogeCtrl import Horloge

class ApplicationCtrl:
    """La classe qui gère le menu principale"""

    def start(self):
        """Lance l'application pour demander une action sur le menu principal"""
        self.command = MenuView.MenuView()
        self.horloge = Horloge()
        self.menu_starting = self.command.launch_command_menu()


        if self.menu_starting == "afficher":
            print("")
            self.horloge.demarrer()
        elif self.menu_starting == "alarme":
            print("")
            self.horloge.regler_alarme()
        elif self.menu_starting == "mode":
            print("")
            self.horloge.changer_format_heure()
        elif self.menu_starting == "supprimer":
            self.clear_terminal()
            self.start()

    def clear_terminal(self):
        """Supprimer le terminal"""
        # Pour windows
        if name == 'nt':
            _ = system('cls')
    
        # Pour mac et linux
        else:
            _ = system('clear')