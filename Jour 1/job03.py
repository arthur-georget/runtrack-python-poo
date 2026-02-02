class Operation:
    def __init__(self):
        self.nombre1 = 12
        self.nombre2 = 3

    def addition(self):
        self.resultat = self.nombre1 + self.nombre2
        print(self.resultat)

operation_1 = Operation()
operation_1.addition()