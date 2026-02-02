class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def sePresenter(self):
        print(f"Je suis {self.prenom} {self.nom}")

personne_1 = Personne("Doe", "John")
personne_2 = Personne("Dupond", "Jean")

personne_1.sePresenter()
personne_2.sePresenter()