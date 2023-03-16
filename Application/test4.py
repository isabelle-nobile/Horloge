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

class Horloge:
    def __init__(self, heure, alarme):
        self.heure = heure
        self.alarme = alarme

    def afficher_heure(self):
        while True:
            heure_actuelle = time.localtime()
            heures, minutes, secondes = heure_actuelle.tm_hour, heure_actuelle.tm_min, heure_actuelle.tm_sec
            print(f"{self.heure[0]:02d}:{self.heure[1]:02d}:{self.heure[2]:02d}", end="\r")
            time.sleep(1)
            if (heures, minutes, secondes) == self.heure:
                self.alarme.heure_atteinte()
                break
            elif self.alarme.active and (heures, minutes, secondes) == self.alarme.heure:
                self.alarme.declencher()
                break
            elif not self.alarme.active:
                print("L'alarme a été arrêtée.")
                break


alarme = Alarme()
alarme.heure = (15, 15, 0)
horloge = Horloge((15, 15, 15), alarme)
print("L'heure de l'alarme est réglée sur :", alarme.heure[0], ":", alarme.heure[1], ":", alarme.heure[2])
horloge.afficher_heure()
