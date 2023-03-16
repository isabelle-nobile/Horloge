from time import localtime, strftime, sleep, time

import os 
from time import struct_time, mktime

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
        
    def regler_heure(self, heures: int, minutes: int, secondes: int):
        """Permet de régler l'heure"""
        self.heure = localtime()
        self.heure = struct_time((self.heure.tm_year, self.heure.tm_mon, self.heure.tm_mday, heures, minutes, secondes, self.heure.tm_wday, self.heure.tm_yday, self.heure.tm_isdst))
        self.afficher_heure()

    def changer_format_heure(self):
        """Change le format de l'heure entre AM/PM et 24 heures"""
        self.mode_24h = not self.mode_24h
        if self.mode_24h:
            self.format_affichage = '%H:%M:%S'
        else:
            self.format_affichage = '%I:%M:%S %p'
        self.afficher_heure()
    
    def demander_format_affichage(self):
        """Demande à l'utilisateur de choisir le format d'affichage de l'heure"""
        choix = input("Choisissez le format d'affichage de l'heure : \n 1 - pour 24h \n 2 - pour AM/PM \n")
        if choix == "1":
            self.mode_24h = True
            self.format_affichage = '%H:%M:%S'
        elif choix == "2":
            self.mode_24h = False
            self.format_affichage = '%I:%M:%S %p'
        else:
            print("Choix invalide. Veuillez entrer 1 ou 2.")
            self.demander_format_affichage()
        
    def demarrer(self):
        """Démarre l'horloge"""
        while True:
            if self.pause:
                sleep(1)
                continue
            self.heure = localtime()
            self.afficher_heure()
            choix = input("Appuyez sur 'p' pour mettre en pause ou 'q' pour quitter : ")
            if choix == "p":
                self.mettre_en_pause()
            elif choix == "q":
                print("Au revoir !")
                break
            sleep(1)



            
    def mettre_en_pause(self):
        """Met en pause l'horloge"""
        self.pause = True

        
    def reprendre(self):
        """Reprend l'horloge"""
        self.pause = False
