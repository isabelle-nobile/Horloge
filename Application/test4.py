import time

class Alarme:
    def __init__(self):
        self.active = True
        self.heure = None

    def declencher(self):
        print("L'alarme est déclenchée!")
        self.active = False

    def heure_atteinte(self):
        print("L'heure de l'alarme est atteinte!")
        self.active = False

    def regler_heure(self, heure):
        self.heure = heure
        self.active = True


class Horloge:
    def __init__(self, heure, alarme):
        self.heure = heure
        self.alarme = alarme

    def afficher_compte_a_rebours(self):
        heures, minutes, secondes = self.heure

        while heures >= 0:
            print(f"{heures:02d}:{minutes:02d}:{secondes:02d}", end="\r")
            time.sleep(1)

            if heures == 0 and minutes == 0 and secondes == 0:
                print("Le temps est écoulé!")
                break

            secondes -= 1
            if secondes < 0:
                minutes -= 1
                secondes = 59
            if minutes < 0:
                heures -= 1
                minutes = 59

        if self.alarme.active:
            print("L'alarme n'a pas été déclenchée.")
        else:
            print("L'alarme a été arrêtée.")

        self.alarme.active = True

heure = (16, 30, 20)
alarme = Alarme()
alarme.regler_heure((16, 30, 0))
horloge = Horloge(heure, alarme)
horloge.afficher_compte_a_rebours()

