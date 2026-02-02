class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1

    def nommer(self, nouveau_prenom):
        self.prenom = nouveau_prenom

animal_1 = Animal()

print(f"L'âge de l'animal est {animal_1.age} ans.")
animal_1.vieillir()
print(f"L'âge de l'animal est {animal_1.age} ans.")
animal_1.vieillir()
print(f"L'âge de l'animal est {animal_1.age} ans.")
animal_1.nommer("Luna")
print(f"L'animal se nomme {animal_1.prenom}")