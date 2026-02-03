class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = True

    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombre_de_pages(self):
        return self.__nombre_de_pages
    
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int):
            if nombre_de_pages > 0:
                self.__nombre_de_pages = nombre_de_pages
            else:
                print("Le nombre de page doit être supérieur à 0.")
        else:
            print("Le nombre de page doit être un entier supérieur à 0.")

    def vérification(self):
        if self.__disponible:
            return True
        else:
            return False

    def emprunter(self):
        if self.__disponible:
            self.__disponible = False
            print(f"Merci d'avoir emprunté {self.__titre}: veuillez le rendre d'ici une semaine.")
        else:
            print(f"Désolé mais {self.__titre} a déjà été emprunté.")

    def rendre(self):
        if not self.__disponible:
            self.__disponible = True
            print(f"Merci d'avoir rendu {self.__titre}.")
        else:
            print(f"Vous ne pouvez pas rendre {self.__titre} puisqu'il est déjà en stock.")

livre1 = Livre("Blade Runner", "Philipp K Dick", 345)
livre2 = Livre("Fondation", "Isaac Asimov", 432)

livre1.rendre()
livre2.emprunter()
livre2.emprunter()
livre2.rendre()