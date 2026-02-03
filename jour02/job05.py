from time import sleep
class Voiture:
    def __init__(self, marque, annee, kilometrage):
        self.__marque = marque
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 10

    def get_marque(self):
        return self.__marque
    
    def set_marque(self, marque):
        self.__marque = marque

    def get_annee(self):
        return self.__annee
    
    def set_annee(self, annee):
        self.__annee = annee

    def get_kilometrage(self):
        return self.__kilometrage
    
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def demarrer(self):
        if not self.__en_marche:
            if self.__verifier_plein() > 5:
                self.__en_marche = True
                print(f"Knch knch knch broooooom...")
                sleep(1)
                print(f"La voiture {self.get_marque()} a bien démarré.")
            else:
                print(f"Knch knch knch")
                sleep(1)
                print(f"La voiture {self.get_marque()} ne démarre pas... Il n'y a surement plus assez d'essence dans le réservoir.")
        else:
            print(f"La voiture {self.get_marque()} est déjà démarrée.")

    def arreter(self):
        if self.__en_marche:
            self.__en_marche = False
            print("Brrmbbb...")
            sleep(1)
            print(f"La voiture {self.get_marque()} s'est arrêtée.")
        else:
            print(f"La voiture {self.__marque} est déjà arrêtée.")

    def __verifier_plein(self):
        return self.__reservoir

    def consomme_essence(self):
        self.__reservoir -= 1
        print(f"bbrm brRrrmm brm brm brm...")
        sleep(1)
        if self.__reservoir <= 0:
            print(f"La jauge à essence de la {self.__marque} affiche 0.")
            self.arreter()

voiture1 = Voiture("Citroën", 1993, 354212)
print(f"La voiture {voiture1.get_marque()} de {voiture1.get_annee()} a {voiture1.get_kilometrage()} kilomètres au compteur.")

voiture1.demarrer()
while voiture1.get_en_marche():
    voiture1.consomme_essence()

voiture1.demarrer()