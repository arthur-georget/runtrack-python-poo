class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

rectangle1 = Rectangle(10,5)
print(f"longueur: {rectangle1.get_longueur()}")
print(f"largeur: {rectangle1.get_largeur()}")

rectangle1.set_longueur(20)
rectangle1.set_largeur(8)

print(f"longueur: {rectangle1.get_longueur()}")
print(f"largeur: {rectangle1.get_largeur()}")