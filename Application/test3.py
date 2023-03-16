import time
import datetime

class Horloge:
    """La classe qui gère l'horloge"""

    def __init__(self):
        """Initialisation des attributs"""

        self.heure = None
        self.alarme = None
        self.format_affichage = None

    def demarrer(self):
        """Lance l'horloge pour afficher l'heure personnalisée"""

        self.demander_format_affichage()

        # Remplacer cette ligne par votre_tuple = (heure, minute, seconde)
        votre_tuple = (14, 56, 0)
        self.heure = time.struct_time((0, 0, 0, votre_tuple[0], votre_tuple[1], votre_tuple[2], -1, -1, -1))
        self.afficher_heure(votre_tuple)
        
        while True:
            self.afficher_heure(votre_tuple)
            time.sleep(1)

    def demander_format_affichage(self):
        """Demande le format d'affichage de l'heure"""

        print("\nMerci de choisir un format d'affichage")
        print("1 - pour 24h")
        print("2 - pour AM/PM")

        choix = input("Votre choix: ")

        if choix == "1":
            self.format_affichage = "%H:%M:%S"
        elif choix == "2":
            self.format_affichage = "%I:%M:%S %p"
        else:
            print("Choix invalide")
            self.demander_format_affichage()

    def afficher_heure(self, heure):
        """Affiche l'heure dans le format requis"""

        # Créer un objet datetime à partir du tuple heure
        heure_dt = datetime.datetime(1900, 1, 1, heure[0], heure[1], heure[2])

        # Utiliser strftime pour afficher l'heure au format souhaité
        heure_formattee = heure_dt.strftime(self.format_affichage)
        print(heure_formattee)

    def regler_alarme(self):
        """Règle l'alarme"""

        heures = input("Heure de l'alarme: ")
        minutes = input("Minutes de l'alarme: ")
        secondes = input("Secondes de l'alarme: ")

        self.alarme = (int(heures), int(minutes), int(secondes))

        print("Alarme réglée à %02d:%02d:%02d" % self.alarme)
