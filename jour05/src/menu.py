from src.ship import *

class Menu:

    def __init__(self, ship: Ship):
        if isinstance(ship, Ship):
            self.__ship = ship
        else:
            raise Exception("Menu.__init__(): ship should be an instance of Ship class.")
        self.__state = 0
        self.__history = []

    def display_menu(self):
        match self.__state:
            case 0:
                print("##################################################################")
                print(f"Menu principal de maintenance du {self.__ship.get_name()}")
                print("1 - Remplacer les pièces")
                print("2 - Modifier des matériaux")
                print("3 - Afficher l'état du bateau")
                print("4 - Afficher l'historique des modifications du bateau")
                print("5 - Quitter")
            case 1:
                print("==================================================================")
                print(f"Menu de remplacement de pièces du {self.__ship.get_name()}")
            case 2:
                print("==================================================================")
                print(f"Menu de modification de matériaux du {self.__ship.get_name()}")
            case _:
                pass

    def ask_user_input(self) -> tuple[str,str]:
        match self.__state:
            case 0:
                user_input = 0
                while not (0 < user_input < 6):
                    try:
                        user_input = int(input("Que voulez-vous faire? (1-5) "))
                    except:
                        print("Veuillez renseigner un chiffre entre 1 et 5.")
                self.__state = user_input
                return self.ask_user_input()
            case 1:
                part_found = False
                while not part_found:
                    part_to_replace = input("Quelle pièce voulez-vous remplacer? ")
                    part_found,index = self.__ship.is_part_found(part_to_replace)
                    if part_found:
                        new_part_material = input("En quelle matière est cette nouvelle pièce? ")
                        return part_to_replace,new_part_material
            case 2:
                part_found = False
                while not part_found:
                    part_to_replace = input("Quelle pièce voulez-vous modifier? ")
                    part_found,index = self.__ship.is_part_found(part_to_replace)
                    if part_found:
                        new_part_material = input("En quelle matière est cette nouvelle pièce? ")
                        return part_to_replace,new_part_material
            case _:
                pass

    def call_actions(self, arguments: tuple[str,str]):
        match self.__state:
            case 1:
                part_to_replace,new_part_material = arguments
                self.__ship.replace_part(part_to_replace, Part(part_to_replace, new_part_material))
                print(f"La pièce {part_to_replace} a été remplacée par une pièce {part_to_replace} en {new_part_material}.")
                self.__history.append(f"La pièce {part_to_replace} a été remplacée par une pièce {part_to_replace} en {new_part_material}.")
                self.__state = 0
            case 2:
                part_to_replace,new_part_material = arguments
                self.__ship.change_part(part_to_replace, new_part_material)
                print(f"La pièce {part_to_replace} a été modifiée, elle est maintenant en {new_part_material}.")
                self.__history.append(f"La pièce {part_to_replace} a été modifiée, elle est maintenant en {new_part_material}.")
                self.__state = 0
            case 3:
                self.__ship.display_state()
                self.__state = 0
            case 4:
                self.__display_history()
                self.__state = 0
            case 5:
                self.__state = -1
            case _:
                pass

    def __display_history(self):
        for i in range(len(self.__history)):
            print(f"{i}: {self.__history[i]}")

    def get_state(self):
        return self.__state