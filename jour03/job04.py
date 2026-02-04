from random import randrange, choice
class Player:
    
    def __init__(self, name, number, position):
        self.__name = name
        self.__number = number
        self.__position = position
        self.__nb_of_scored_goal = 0
        self.__nb_of_assist = 0
        self.__nb_of_yellow_card = 0
        self.__nb_of_red_card = 0
        self.display_stats()

    def score_a_goal(self):
        self.__nb_of_scored_goal += 1

    def decisive_pass_made(self):
        self.__nb_of_assist += 1

    def receive_yellow_card(self):
        self.__nb_of_yellow_card += 1

    def receive_red_card(self):
        self.__nb_of_red_card += 1

    def display_stats(self):
        print("===============================================")
        print( f"Nom: {self.__name}")
        print( f"Numéro: {self.__number}")
        print( f"Position: {self.__position}")
        print( f"Buts marqués: {self.__nb_of_scored_goal}")
        print( f"Passes décivives: {self.__nb_of_assist}")
        print( f"Cartons jaunes: {self.__nb_of_yellow_card}")
        print( f"Cartons rouges: {self.__nb_of_red_card}")

class Team:

    def __init__(self, players):
        self.__players = players

    def add_player(self, player):
        self._players.append(player)
    
    def display_players_stats(self):
        for player in self.__players:
            player.display_stats()

    def update_player_stat(self, player, type):
        match type:
            case "goal":
                player.score_a_goal()
            case "assist":
                player.decisive_pass_made()
            case "yellow":
                player.receive_yellow_card()
            case "red":
                player.receive_red_card()
            case " ":
                pass
            case _:
                print("update_player_stats(): Unknown action type")

player1 = Player("Maurice Guichard",1,"Gardien")
player2 = Player("Fernand Canelle",2,"Défenseur")
player3 = Player("Jacques Davy",3,"Milieu de terrain")
player4 = Player("Joseph Verlet",4,"Attaquant")
player5 = Player("Georges Bilot",5,"Ailier droit")
player6 = Player("Charles Bilot",6,"Avant centre")
player7 = Player("Louis Menier",7,"Arrière droit")
player8 = Player("Marius Royet",8,"Défenseur")
player9 = Player("Georges Garnier",9,"Milieu de terrain")
player10 = Player("Gaston Cyprès",10,"Défenseur")
player11 = Player("Augustin Filez",11,"Attaquant")
    
equipe_de_france_1904 = Team([player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11])

equipe_de_france_1904.display_players_stats()

print("################################################")
print("MATCH CONTRE LA BELGIQUE")
print("################################################")
### Match ###
for time in range(90):
    action = choice([" ", "goal", "yellow", "red"])
    if randrange(10) >= 9:
        if action == "goal":
            equipe_de_france_1904.update_player_stat(choice([player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]),"assist")
        equipe_de_france_1904.update_player_stat(choice([player1,player2,player3,player4,player5,player6,player7,player8,player9,player10,player11]),action)

equipe_de_france_1904.display_players_stats()