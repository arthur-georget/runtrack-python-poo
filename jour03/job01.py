class City:
    def __init__(self, name, nb_of_residents):
        self.__name = name
        self.__nb_of_residents = nb_of_residents

    def get_name(self):
        return self.__name
    
    def get_nb_of_residents(self):
        return self.__nb_of_residents
    
    def set_nb_of_residents(self, nb_of_residents):
        self.__nb_of_residents = nb_of_residents

class People:
    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.__city = city
        self.__add_resident()

    def __add_resident(self):
        self.__city.set_nb_of_residents(self.__city.get_nb_of_residents()+1)

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age

city1 = City("Paris", 10000000)
city2 = City("Marseille", 861635)

print(f"Population de la ville de {city1.get_name()}: {city1.get_nb_of_residents()} habitants")
print(f"Population de la ville de {city2.get_name()}: {city2.get_nb_of_residents()} habitants")

people1 = People("John", 45, city1)
people2 = People("Myrtille", 4, city1)
people3 = People("Chloé", 18, city2)

print(f"Mise à jour de la population de la ville de {city1.get_name()}: {city1.get_nb_of_residents()} habitants")
print(f"Mise à jour de la population de la ville de {city2.get_name()}: {city2.get_nb_of_residents()} habitants")