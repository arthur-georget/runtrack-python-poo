if __name__ == "__main__":
    from part import *
else:
    from src.part import *

class Ship:

    def __init__(self, name: str, parts: list = []):
        if isinstance(name, str):
            self.__name = name
            if isinstance(parts, list):
                self.__parts = parts
            else:
                raise Exception("Ship.__init__(): parts should be a list.")
        else:
            raise Exception("Ship.__init__(): name should be a str.")
        
    def get_name(self) -> str:
        return self.__name
    
    def get_parts(self) -> list:
        return self.__parts

    def display_state(self):
        print("====================")
        for part in self.__parts:
            print(part)

    def is_part_found(self, part_name: str) -> tuple[bool,int]:
        if isinstance(part_name, str):
                for index in range(len(self.__parts)):
                    if part_name == self.__parts[index].get_name():
                        return True,index
                print(f"C'est quoi une {part_name}?")
                return False,-1
        else:
            raise Exception("Ship.is_part_found(): part_name should be a str.")

    def replace_part(self, part_name: str, new_part: Part):
        if isinstance(part_name, str):
            if isinstance(new_part, Part):
                part_found,index = self.is_part_found(part_name)
                if part_found:
                    self.__parts[index] = new_part  
            else:
                raise Exception("Ship.replace_part(): part should be an instance of the class Part.")
        else:
            raise Exception("Ship.replace_part(): part_name should be a str.")

    def change_part(self, part_name: str, new_material: str):
        if isinstance(part_name, str):
            if isinstance(new_material, str):
                part_found,index = self.is_part_found(part_name)
                if part_found:
                    self.__parts[index].change_material(new_material)
            else:
                raise Exception("Ship.replace_part(): new_material should be a str.")
        else:
            raise Exception("Ship.replace_part(): part_name should be a str.")
        
class RacingShip(Ship):

    def __init__(self, name: str, max_speed: int, parts: list = []):
        Ship.__init__(self, name, parts)
        if isinstance(max_speed, int):
            self.__max_speed = max_speed
        else:
            raise Exception("RacingShip.__init__(): max_speed should be an int.")


    def display_speed(self):
        print(f"La vitesse du {self.get_name()} est de {self.__max_speed} noeuds.")

if __name__ == "__main__":

    parts_charlie_dalin_ship = [Part("Mât","Carbone"),Part("Voile","Polyester"),Part("Ancre","Acier"),Part("Barre","Carbone"),Part("Pont","Fibre de verre"),Part("Safran","Fibre de verre"),Part("Poupe","Fibre de verre")]
    racing_ship = RacingShip("Macif Santé Prévoyance", 20, parts_charlie_dalin_ship)
    racing_ship.display_speed()
    racing_ship.display_state()
    racing_ship.change_part("Poupe","Pierre")
    racing_ship.display_state()
    print("L'adresse mémoire de la Poupe n'a pas changé.")
    racing_ship.replace_part("Poupe",Part("Poupe","Carbone"))
    racing_ship.display_state()
    print("L'adresse mémoire de la Poupe a changé.")