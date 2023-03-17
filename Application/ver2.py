import time

def afficher_heure(heure, format_affichage):
    """Affiche l'heure en fonction du format d'affichage choisi"""
    if format_affichage == "%H:%M:%S":
        heure_affichage = '{:02d}:{:02d}:{:02d}'.format(*heure)
    elif format_affichage == "%I:%M:%S %p":
        heure_affichage = time.strftime("%I:%M:%S %p", time.strptime('{:02d}:{:02d}:{:02d}'.format(*heure), "%H:%M:%S"))
    else:
        heure_affichage = "Format d'affichage invalide"

    print(heure_affichage)

def demander_format_affichage():
    """Demande le format d'affichage de l'heure"""
    print("\nMerci de choisir un format d'affichage")
    print("1 - pour 24h")
    print("2 - pour AM/PM")

    choix = input("Votre choix: ")

    if choix == "1":
        format_affichage = "%H:%M:%S"
    elif choix == "2":
        format_affichage = "%I:%M:%S %p"
    else:
        print("Choix invalide")
        format_affichage = demander_format_affichage()

    return format_affichage

def mettre_a_jour_heure(heure):
    """Met à jour l'heure"""
    heure = (heure[0], heure[1], heure[2]+1)
    if heure[2] >= 60:
        heure = (heure[0], heure[1]+1, 0)
    if heure[1] >= 60:
        heure = (heure[0]+1, 0, 0)
    if heure[0] >= 24:
        heure = (0, 0, 0)
    return heure

def demander_heure():
    """Demande à l'utilisateur de rentrer une nouvelle heure"""
    
    heure = input("Entrez l'heure (HH:MM:SS) : ")
    try:
        heure = tuple(map(int, heure.split(":")))
        assert len(heure) == 3
        assert all(0 <= h < 60 for h in heure)
        return heure
    except (ValueError, AssertionError):
        print("Heure invalide.")
        return demander_heure()

def demander_alarme():
    """Demande à l'utilisateur de rentrer une nouvelle alarme"""
    
    alarme = input("Entrez l'alarme (HH:MM:SS) : ")
    try:
        alarme = tuple(map(int, alarme.split(":")))
        assert len(alarme) == 3
        assert all(0 <= h < 60 for h in alarme)
        return alarme
    except (ValueError, AssertionError):
        print("Heure invalide.")
        return demander_alarme()
    
def question_heure():
    print("\nVoulez-vous chnager l'heure ou garder celle prédéfinis (16:30:00)?")
    print("1 - Rentrer mon heure")
    print("2 - Choisir l'heure prédéfinis")
    choix_heure = input("Votre choix: ")

    if choix_heure == "1":
        response_h = demander_heure()
    elif choix_heure == "2":
        response_h = (16, 30, 00)
    else:
        print("Choix invalide")
        response_h = question_heure()
    return response_h

def question_alarme():
    print("\nVoulez-vous chnager l'alarme ou garder celle prédéfinis (16:30:10)?")
    print("1 - Rentrer mon alarme")
    print("2 - Choisir l'alarme prédéfinis")
    choix_heure = input("Votre choix: ")

    if choix_heure == "1":
        response_a = demander_alarme()
    elif choix_heure == "2":
        response_a = (16, 30, 10)
    else:
        print("Choix invalide")
        response_a = question_alarme()
    return response_a


def main():

    heure = question_heure()

    # Initialisation de l'alarme
    alarme = question_alarme()

    # Demander le format d'affichage de l'heure
    format_affichage = demander_format_affichage()

    # Boucle principale
    while True:
        # Affichage de l'heure avec le format choisi
        afficher_heure(heure, format_affichage)

        # Vérification de l'alarme
        if heure == alarme:
            print("Dring Dring !!!")
            print("L'Alarme vient de se délancher!")
            break
            

        # Mise à jour de l'heure
        heure = mettre_a_jour_heure(heure)

        # Attente d'une seconde
        time.sleep(1)

main()