class Personnage:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1

    def droite(self):
        self.x += 1

    def bas(self):
        self.y += 1

    def haut(self):
        self.y -= 1

    def position(self):
        return self.x, self.y
    
p1 = Personnage(5,25)
print(f"Position du personnage: {p1.position()}")
p1.gauche()
print(f"Position du personnage: {p1.position()}")
p1.droite()
print(f"Position du personnage: {p1.position()}")
p1.bas()
print(f"Position du personnage: {p1.position()}")
p1.haut()
print(f"Position du personnage: {p1.position()}")