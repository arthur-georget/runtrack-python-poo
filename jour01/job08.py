from math import pi

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        print(f"rayon: {self.rayon}")
        print(f"circonference: {self.circonference()}")
        print(f"aire: {self.aire()}")
        print(f"diametre: {self.diametre()}")

    def circonference(self):
        circonference = 2*pi*self.rayon
        return circonference
    
    def aire(self):
        aire = pi*self.rayon**2
        return aire
    
    def diametre(self):
        diametre = self.rayon*2
        return diametre
    
c1 = Cercle(4)
c1.afficherInfos()

c2 = Cercle(7)
c2.afficherInfos()