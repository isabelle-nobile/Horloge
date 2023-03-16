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

# instancier la classe Horloge
mon_horloge = Horloge()

# appeler la méthode afficher_heure()
mon_horloge.afficher_heure()
