from time import localtime, strftime, sleep

class Horloge:
    def __init__(self):
        self.mode_24h = True
        self.pause = False
        self.heure = localtime()
        self.heure_alarme = None
        
    def afficher_heure(self):
        """Affiche l'heure actuelle"""
        if self.mode_24h:
            format_heure = '%H:%M:%S'
        else:
            format_heure = '%I:%M:%S %p'
        print(strftime(format_heure, self.heure), end='\r')
        
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
        choix = input("Voulez-vous afficher l'heure en mode 24h ? (Oui/Non) ")
        if choix.lower() == "oui":
            self.mode_24h = True
        else:
            self.mode_24h = False
        self.afficher_heure()

        
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
