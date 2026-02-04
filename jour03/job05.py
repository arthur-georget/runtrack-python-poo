from random import randrange, choice
from time import sleep

class Character:
    
    def __init__(self, name, life):
        self.__name = name
        self.__life = life

    def punch(self, opponent):
        print(f"{self.__name} a mis un coup de poing à {opponent.get_name()}")
        opponent.get_hurt(5)
        
    def kick(self, opponent):
        print(f"{self.__name} a mis un coup de pied à {opponent.get_name()}")
        opponent.get_hurt(10)
        
    def get_name(self):
        return self.__name
    
    def get_life(self):
        return self.__life

    def get_hurt(self, pain):
        self.__life -= pain
        print(f"{self.__name}: {choice(["ouch!","ughh..","argh!"])}")
    

class Game:
    
    def __init__(self):
        self.difficulty = 1
        self.__winner = 0
        self.__running = True

    def __choose_difficulty(self):
        difficulty = 0
        while not 0 < difficulty < 5:
            try:
                difficulty = int(input("Veuillez choisir un niveau de difficulté entre 1 et 4: "))
            except:
                print("Veuillez sélectionner un niveau de difficulté entier entre 1 et 4.")
        self.difficulty = difficulty

    def __check_victory(self, p1_life, p2_life):
        if (p1_life <= 0) and (p2_life <= 0):
            self.__running = False
            self.__winner = 0
        elif (p1_life <= 0):
            self.__running = False
            self.__winner = 2
        elif (p2_life <= 0):
            self.__running = False
            self.__winner = 1
        else:
            self.__running = True
            self.__winner = 0

    def start_game(self):
        self.__choose_difficulty()
        player = Character("Joe", 100//self.difficulty)
        opponent = Character("Amy", 25*self.difficulty)
        
        self.__running = True

        while self.__running:
            if choice([True,False]):
                if randrange(20) > 7:
                    choice([player.punch(opponent),player.kick(opponent)])
                else:
                    print(f"{opponent.get_name()} a paré le coup de {player.get_name()}.")
            else:
                if randrange(20) > 7:
                    choice([opponent.punch(player),opponent.kick(player)])
                else:
                    print(f"{player.get_name()} a paré le coup de {opponent.get_name()}.")
            
            print(f"Vie {player.get_name()} --> {player.get_life()}")
            print(f"Vie {opponent.get_name()} --> {opponent.get_life()}")

            p1_life = player.get_life()
            p2_life = opponent.get_life()

            self.__check_victory(p1_life, p2_life)

            sleep(choice([0.7,0.8,1,1,2]))  

        if self.__winner == 1:
            print(f"{player.get_name()} a gagné!")
        elif self.__winner == 2:
            print(f"{opponent.get_name()} a gagné!")
        else:
            print("Egalité!!")

game1 = Game()
game1.start_game()
