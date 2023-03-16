import time

def afficher_heure(heure, alarme):
    while True:
        heure_actuelle = time.localtime()
        heures, minutes, secondes = heure_actuelle.tm_hour, heure_actuelle.tm_min, heure_actuelle.tm_sec
        print(f"{heures:02d}:{minutes:02d}:{secondes:02d}", end="\r")
        time.sleep(1)
        if (heures, minutes, secondes) == heure:
            print("L'heure de l'alarme est atteinte!")
            alarme[0] = False
            break
        elif alarme[0]:
            if (heures, minutes, secondes) == alarme[1]:
                print("L'alarme est déclenchée!")
                alarme[0] = False
                break
        else:
            print("L'alarme a été arrêtée.")
            break

def regler_alarme(heure):
    return [True, heure]

heure = (15, 15, 15)
alarme = regler_alarme((11, 15, 20))
print("L'heure de l'alarme est réglée sur :", alarme[1][0], ":", alarme[1][1], ":", alarme[1][2])


