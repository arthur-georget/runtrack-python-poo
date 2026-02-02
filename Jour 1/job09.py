class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        prixTTC = self.prixHT * self.TVA + self.prixHT
        return prixTTC
    
    def afficherPrixHT(self):
        return self.prixHT
    
    def afficherTVA(self):
        return self.TVA
    
    def afficher(self):
        return f"nom: {self.nom}", f"prix HT: {self.prixHT}", f"TVA: {self.TVA}", f"prix TTC: {self.CalculerPrixTTC()}"
    
    def renommer(self, nouveau_nom):
        self.nom = nouveau_nom

    def changer_prix(self, nouveau_prix):
        self.prixHT = nouveau_prix
    
produit1 = Produit("Lait", 1.80, 0.055)
produit2 = Produit("Ordinateur", 400, 0.2)
produit3 = Produit("Carotte", 0.5, 0.1)

print(f"Le prix TTC du {produit1.nom} est {produit1.CalculerPrixTTC()} avec une TVA de {produit1.TVA}")
print(f"Le prix TTC du {produit2.nom} est {produit2.CalculerPrixTTC()} avec une TVA de {produit2.TVA}")
print(f"Le prix TTC du {produit3.nom} est {produit3.CalculerPrixTTC()} avec une TVA de {produit3.TVA}")

print(f"Les informations de {produit1.nom} sont {produit1.afficher()}")

produit1.renommer("Lait Bio")
produit1.changer_prix(2.10)

produit2.renommer("Ordinateur éthique et réparable")
produit2.changer_prix(650)

produit3.renommer("Carotte Bio")
produit3.changer_prix(0.7)

print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())