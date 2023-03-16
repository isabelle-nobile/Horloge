# import time

# # Initialisation de l'heure
# heure = 0

# # Boucle principale
# while True:
#     # Demander le format d'affichage de l'heure
#     print("\nMerci de choisir un format d'affichage")
#     print("1 - pour 24h")
#     print("2 - pour AM/PM")

#     choix = input("Votre choix: ")

#     if choix == "1":
#         # Mode 24h
#         for i in range(24):
#             heure_affichage = '{:02d}:00:00'.format(heure)
#             print(heure_affichage)
#             heure = (heure + 1) % 24
#             time.sleep(1)
#     elif choix == "2":
#         # Mode AM/PM
#         for i in range(24):
#             heure_affichage = time.strftime("%I:%M:%S %p", time.strptime('{:02d}:00:00'.format(heure), "%H:%M:%S"))
#             print(heure_affichage)
#             heure = (heure + 1) % 24
#             time.sleep(1)
#     else:
#         print("Choix invalide")

import time

def demander_format_affichage():
    """Demande le format d'affichage de l'heure"""
    print("\nMerci de choisir un format d'affichage")
    print("1 - pour 24h")
    print("2 - pour AM/PM")

    choix = input("Votre choix: ")

    if choix == "1":
        # Mode 24h
        for i in range(24):
            heure_affichage = '{:02d}:00:00'.format(heure)
            print(heure_affichage)
            heure = (heure + 1) % 24
            time.sleep(1)
            
        format_affichage = "%H:%M:%S"

    elif choix == "2":
        # Mode AM/PM
        for i in range(24):
            heure_affichage = time.strftime("%I:%M:%S %p", time.strptime('{:02d}:00:00'.format(heure), "%H:%M:%S"))
            print(heure_affichage)
            heure = (heure + 1) % 24
            time.sleep(1)
        
        format_affichage = "%I:%M:%S %p"
        
    else:
        print("Choix invalide")
        format_affichage = demander_format_affichage()

    return format_affichage

# Initialisation de l'heure
heure = 0

# Boucle principale
while True:
    # Demander le format d'affichage de l'heure
    format_affichage = demander_format_affichage()

    # Affichage de l'heure avec le format choisi
    heure_affichage = time.strftime(format_affichage, time.strptime('{:02d}:00:00'.format(heure), "%H:%M:%S"))
    print(heure_affichage)

    # Mise à jour de l'heure
    heure = (heure + 1) % 24

    # Attente d'une seconde
    time.sleep(1)
