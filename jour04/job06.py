class Vehicle:

    def __init__(self, brand: str, model: str, year: int, price: float):
        self.__brand = brand
        self.__model = model
        if ( isinstance(year, int) and year > 0 ):
            self.__year = year
        else:
            raise Exception("Vehicle.__init__(): Year should be int > 0.")
        if ( isinstance(price, float) and price > 0 ):
            self.__price = price
        else:
            raise Exception("Vehicle.__init__(): Price should be float > 0.")

    def vehicleInfos(self):
        print("===========================")
        print(f"Marque = {self.__brand}")
        print(f"Modèle = {self.__model}")
        print(f"Année = {self.__year}")
        print(f"Prix = {self.__price}€")

    def start_engine(self):
        print(f"Attention, je roule")

class Car(Vehicle):

    def __init__(self, brand: str, model: str, year: int, price: float):
        super().__init__(brand, model, year, price)
        self.__doors = 4

    def vehicleInfos(self):
        super().vehicleInfos()
        print(f"Nombre de portes = {self.__doors}")

    def start_engine(self):
        super().start_engine()
        print("knch knch brrrrrm brbrbr...")

class Motorcycle(Vehicle):

    def __init__(self, brand: str, model: str, year: int, price: float, wheels: int=2):
        super().__init__(brand, model, year, price)
        self.__wheels = wheels

    def vehicleInfos(self):
        super().vehicleInfos()
        print(f"Nombre de roues = {self.__wheels}")

    def start_engine(self):
        super().start_engine()
        print("clinc grouUUUuuuuuu...")  

car = Car("Mercedes", "Classe A", 2020, 18500.0)
car.vehicleInfos()
car.start_engine()

motorcyle = Motorcycle("Yamaha", "1200 Vmax", 1987, 4500.0)
motorcyle.vehicleInfos()
motorcyle.start_engine()