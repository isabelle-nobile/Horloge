# import time

# # Initialisation de l'heure
# heure = (16, 30, 0)

# # Initialisation de l'alarme
# alarme = (16, 30, 10)

# def demander_format_affichage():
#     """Demande le format d'affichage de l'heure"""
#     print("\nMerci de choisir un format d'affichage")
#     print("1 - pour 24h")
#     print("2 - pour AM/PM")

#     choix = input("Votre choix: ")

#     if choix == "1":
#         format_affichage = "%H:%M:%S"
#     elif choix == "2":
#         format_affichage = "%I:%M:%S %p"
#     else:
#         print("Choix invalide")
#         demander_format_affichage()

#     return format_affichage

# # Boucle principale
# while True:
#     # Demander le format d'affichage de l'heure
#     format_affichage = demander_format_affichage()

#     # Affichage de l'heure avec le format choisi
#     heure_affichage = time.strftime(format_affichage, heure)
#     print(heure_affichage)

#     # Vérification de l'alarme
#     if heure == alarme:
#         print("Alarme !")
#         break

#     # Mise à jour de l'heure
#     heure = (heure[0], heure[1], heure[2]+1)
#     if heure[2] >= 60:
#         heure = (heure[0], heure[1]+1, 0)
#     if heure[1] >= 60:
#         heure = (heure[0]+1, 0, 0)
#     if heure[0] >= 24:
#         heure = (0, 0, 0)

#     # Attente d'une seconde
#     time.sleep(1)


import time

# Initialisation de l'heure
heure = (16, 30, 0)

# Initialisation de l'alarme
alarme = (16, 30, 10)

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
        demander_format_affichage()

    return format_affichage

# Boucle principale
while True:
    # Demander le format d'affichage de l'heure
    format_affichage = demander_format_affichage()

    # Affichage de l'heure avec le format choisi
    heure_affichage = time.strftime(format_affichage, heure)
    print(heure_affichage)

    # Vérification de l'alarme
    if heure == alarme:
        print("Alarme !")
        break

    # Mise à jour de l'heure
    heure = (heure[0], heure[1], heure[2]+1)
    if heure[2] >= 60:
        heure = (heure[0], heure[1]+1, 0)
    if heure[1] >= 60:
        heure = (heure[0]+1, 0, 0)
    if heure[0] >= 24:
        heure = (0, 0, 0)

    # Attente d'une seconde
    time.sleep(1)