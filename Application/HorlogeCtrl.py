from time import localtime, strftime, sleep

class Horloge:
    def __init__(self):
        self.mode_24h = True
        self.pause = False
        self.heure = localtime()
        self.heure_alarme = None
        self.format_affichage = '%H:%M:%S'
        
    def afficher_heure(self):
        """Affiche l'heure actuelle"""
        print(strftime(self.format_affichage, self.heure), end='\r')
        
    def regler_heure(self, heures, minutes, secondes):
        """Permet de régler l'heure"""
        self.heure = localtime()
        self.heure = self.heure._replace(hour=heures, minute=minutes, second=secondes)
        self.afficher_heure()
        
    def regler_alarme(self, heures, minutes, secondes):
        """Régler l'heure de l'alarme"""
        self.heure_alarme = (heures, minutes, secondes)
        
    def activer_alarme(self):
        """Vérifie l'heure actuelle pour l'alarme"""
        while True:
            if self.pause:
                continue
            heure_actuelle = localtime()
            if self.heure_alarme is not None and heure_actuelle[3:6] == self.heure_alarme:
                self.pause = True
                print("L'heure de l'alarme est atteinte!")
                break
            self.afficher_heure()
            sleep(1)
        
    def changer_format_heure(self):
        """Change le format de l'heure entre AM/PM et 24 heures"""
        self.mode_24h = not self.mode_24h
        if self.mode_24h:
            self.format_affichage = '%H:%M:%S'
        else:
            self.format_affichage = '%I:%M:%S %p'
        self.afficher_heure()

    def demander_format_affichage(self):
        """Demande à l'utilisateur de choisir le format d'affichage de l'heure"""
        choix = input("Choisissez le format d'affichage de l'heure : \n 1 - pour 24h \n 2 - pour AM/PM \n")
        if choix == "1":
            self.mode_24h = True
            self.format_affichage = '%H:%M:%S'
        elif choix == "2":
            self.mode_24h = False
            self.format_affichage = '%I:%M:%S %p'
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
            self.demander_format_affichage()

        
    def mettre_en_pause(self):
        """Met en pause l'horloge"""
        self.pause = True
        
    def reprendre(self):
        """Reprend l'horloge après une pause"""
        self.pause = False
        self.afficher_heure()
        
    def demarrer(self):
        """Démarre l'horloge"""
        self.afficher_heure()
        while True:
            if self.pause:
                continue
            self.heure = localtime()
            self.afficher_heure()
            sleep(1)
