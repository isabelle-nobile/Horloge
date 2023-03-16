from time import localtime, strftime, sleep, time

class Horloge:
    def __init__(self):
        self.mode_24h = True
        self.pause = False
        self.heure = localtime()
        self.heure_alarme = None
        
    def afficher_heure(self, heure, alarme):
        """Affiche l'heure actuelle"""
        heures, minutes, secondes = heure
        if self.mode_24h:
            format_heure = '%H:%M:%S'
        else:
            format_heure = '%I:%M:%S %p'
        print(strftime(format_heure, localtime()), end='\r')
        if (heures, minutes, secondes) == heure:
            print("L'heure de l'alarme est atteinte!")
            alarme[0] = False
        elif alarme[0]:
            if (heures, minutes, secondes) == alarme[1]:
                print("L'alarme est déclenchée!")
                alarme[0] = False
        
    def regler_heure(self, heures: int, minutes: int, secondes: int):
        """Permet de régler l'heure"""
        self.heure = localtime()
        self.heure = (heures, minutes, secondes)
        self.afficher_heure(self.heure, self.heure_alarme)

    def changer_format_heure(self):
        """Change le format de l'heure entre AM/PM et 24 heures"""
        self.mode_24h = not self.mode_24h
    
    def demander_format_affichage(self):
        """Demande à l'utilisateur de choisir le format d'affichage de l'heure"""
        choix = input("Choisissez le format d'affichage de l'heure : \n 1 - pour 24h \n 2 - pour AM/PM \n")
        if choix == "1":
            self.mode_24h = True
        elif choix == "2":
            self.mode_24h = False
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
            self.demander_format_affichage()
        
    def demarrer(self):
        """Démarre l'horloge"""
        while True:
            heures, minutes, secondes = localtime().tm_hour, localtime().tm_min, localtime().tm_sec
            self.afficher_heure((heures, minutes, secondes), self.heure_alarme)
            choix = input("Appuyez sur 'p' pour mettre en pause ou 'q' pour quitter ou 'c' pour changer le format d'affichage : ")
            if choix == "p":
                self.mettre_en_pause()
            elif choix == "q":
                print("Au revoir !")
                break
            elif choix == "c":
                self.demander_format_affichage()
            sleep(1)


    def regler_alarme(self, heure):
        """Permet de régler l'alarme"""
        self.heure_alarme = [True, heure]
        
    def mettre_en_pause(self):
        """Met en pause l'horloge"""
        self.pause = True
        
    def reprendre(self):
        """Reprend l'horloge"""
        self.pause = False
