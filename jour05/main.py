from src.menu import *

def main():

    parts_theseus_ship = [Part("Mât","Bois"),Part("Voile","Lin"),Part("Ancre","Métal"),Part("Barre","Bois"),Part("Pont","Bois"),Part("Safran","Bois"),Part("Poupe","Bois"),Part("Proue","Bois")]
    theseus_ship = Ship("Bâteau de Thésée",parts_theseus_ship)

    try:
        menu = Menu(theseus_ship)
        running = True
        arguments = None,None
        
        while running:
            menu.display_menu()
            arguments = menu.ask_user_input()
            menu.call_actions(arguments)
            if menu.get_state() == -1:
                print("Merci d'avoir utilisé le menu de maintenance.")
                break

    except KeyboardInterrupt:
        print("Merci d'avoir utilisé le menu de maintenance.")

if __name__ == "__main__":
    main()