import time

class Horloge:
    def __init__(self, heure_defaut=(16, 30, 0), alarme_defaut=(16, 30, 10)):
        self.heure = heure_defaut
        self.alarme = alarme_defaut
        self.format_affichage = "%H:%M:%S"
        
    def afficher_heure(self):
        """Affiche l'heure en fonction du format d'affichage choisi"""
        
        if self.format_affichage == "%H:%M:%S":
            heure_affichage = '{:02d}:{:02d}:{:02d}'.format(*self.heure)
        elif self.format_affichage == "%I:%M:%S %p":
            heure_affichage = time.strftime("%I:%M:%S %p", time.strptime('{:02d}:{:02d}:{:02d}'.format(*self.heure), "%H:%M:%S"))
        else:
            heure_affichage = "Format d'affichage invalide"

        print(heure_affichage)
    
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

    def mettre_a_jour_heure(self):
        """Met à jour l'heure"""
        self.heure = (self.heure[0], self.heure[1], self.heure[2]+1)
        if self.heure[2] >= 60:
            self.heure = (self.heure[0], self.heure[1]+1, 0)
        if self.heure[1] >= 60:
            self.heure = (self.heure[0]+1, 0, 0)
        if self.heure[0] >= 24:
            self.heure = (0, 0, 0)

    def demander_heure(self):
        """Demande à l'utilisateur de rentrer une nouvelle heure"""
        
        heure = input("Entrez l'heure (HH:MM:SS) : ")
        try:
            heure = tuple(map(int, heure.split(":")))
            assert len(heure) == 3
            assert all(0 <= h < 60 for h in heure)
            self.heure = heure
        except (ValueError, AssertionError):
            print("Heure invalide.")
            self.demander_heure()

    def demander_alarme(self):
        """Demande à l'utilisateur de rentrer une nouvelle alarme"""
        
        alarme = input("Entrez l'alarme (HH:MM:SS) : ")
        try:
            alarme = tuple(map(int, alarme.split(":")))
            assert len(alarme) == 3
            assert all(0 <= h < 60 for h in alarme)
            self.alarme = alarme
        except (ValueError, AssertionError):
            print("Heure invalide.")
            self.demander_alarme()

    def question_heure(self):
        """Demande à l'utilisateur s'il souhaite choisir son heure ou une heure prédéfinis"""

        print("\nVoulez-vous changer l'heure ou garder celle prédéfinie (16:30:00)?")
        print("1 - Rentrer mon heure")
        print("2 - Choisir l'heure prédéfinie")
        choix_heure = input("Votre choix: ")

        if choix_heure == "1":
            response_h = self.demander_heure()
        elif choix_heure == "2":
            response_h = (16, 30, 00)
        else:
            print("Choix invalide")
            response_h = self.question_heure()
        return response_h
    
    def question_alarme(self):
        """Demande à l'utilisateur s'il souhaite choisir son alarme ou une alarme prédéfinis"""
        
        print("\nVoulez-vous chnager l'alarme ou garder celle prédéfinis (16:30:10)?")
        print("1 - Rentrer mon alarme")
        print("2 - Choisir l'alarme prédéfinis")
        choix_heure = input("Votre choix: ")

        if choix_heure == "1":
            response_a = self.demander_alarme()
        elif choix_heure == "2":
            response_a = (16, 30, 10)
        else:
            print("Choix invalide")
            response_a = self.question_alarme()
        return response_a
    
    def main(self):
        """Lance le programme"""
        heure = self.question_heure()

        # Initialisation de l'alarme
        alarme = self.question_alarme()

        # Demander le format d'affichage de l'heure
        format_affichage = self.demander_format_affichage()

        # Boucle principale
        while True:
            # Affichage de l'heure avec le format choisi
            self.afficher_heure()

            # Vérification de l'alarme
            if self.heure == self.alarme:
                print("Dring Dring !!!")
                print("L'Alarme vient de se délancher!")
                break
                
            # Mise à jour de l'heure
            heure = self.mettre_a_jour_heure()

            # Attente d'une seconde
            time.sleep(1)

horloge = Horloge()
horloge.main()