class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages

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

livre1 = Livre("Blade Runner", "Philipp K Dick", 345)
livre2 = Livre("Fondation", "Isaac Asimov", 432)

print(f"{livre1.get_titre()} a été écrit par {livre1.get_auteur()} et a {livre1.get_nombre_de_pages()} pages.")
print(f"{livre2.get_titre()} a été écrit par {livre2.get_auteur()} et a {livre2.get_nombre_de_pages()} pages.")

livre1.set_titre("Le livre de Hain")
livre1.set_auteur("Ursula Le Guin")
livre1.set_nombre_de_pages("toto")
livre1.set_nombre_de_pages(-3)
livre1.set_nombre_de_pages(0.4)
livre1.set_nombre_de_pages(1345)

print(f"{livre1.get_titre()} a été écrit par {livre1.get_auteur()} et a {livre1.get_nombre_de_pages()} pages.")