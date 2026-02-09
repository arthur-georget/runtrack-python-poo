from random import shuffle
from time import sleep

class Card:

    def __init__(self, color: str, rank: int):

        if isinstance(color, str):
            self.__color = color
        else:
            raise Exception("Card.__init__(): color should be a str.")
        
        if isinstance(rank, int):
            self.__rank = rank
            self.__value = rank
        else:
            raise Exception("Card.__init__(): rank should be an int.")

    def get_color(self) -> str:
        return self.__color
    
    def get_rank(self) -> int:
        return self.__rank

    def get_value(self) -> int:
        return self.__value
    
    def set_value(self, value: int):
        if isinstance(value, int):
            self.__value = value
        else:
            raise Exception("Card.set_value(): value should be an int.")
    
    def set_blackjack_value(self):
        if self.__rank >= 11:
            self.__value = 10

    def ask_ace_value(self):
        self.__value = 0
        while self.__value not in (1,11):
            self.__value = input("Quelle valeur voulez-vous assigner à votre As? (1 ou 10)")
        sleep(1)

    def get_card_name(self):
        if self.__rank == 1:
            rank_name = "As"
        elif 2 <= self.__rank <= 10:
            rank_name = str(self.__rank)
        else:
            match self.__rank:
                case 11:
                    rank_name = "Valet"
                case 12:
                    rank_name = "Dame"
                case 13:
                    rank_name = "Roi"
        return (f"{rank_name} de {self.__color}")

class Dealer:

    def __init__(self):
        self.__hand = []
        self.__hand_value = 0
        self.__is_winning = True

    def get_hand(self):
        return self.__hand
    
    def set_hand(self, hand: list):
        self.__hand = hand

    def get_hand_value(self):
        return self.__hand_value
    
    def set_hand_value(self):
        self.__hand_value = 0
        for card in self.__hand:
            self.__hand_value += card.get_value()

    def get_is_winning(self):
        return self.__is_winning
    
    def set_is_winning(self, is_winning: bool):
        if isinstance(is_winning, bool):
            self.__is_winning = is_winning
        else:
            raise Exception("Dealer.set_is_winning(): is_winning should be a bool.")
        
    def get_card(self, card: Card):
        if isinstance(card, Card):
            self.__hand.append(card)
        else:
            raise Exception("Dealer.get_card(): card should be a Card object.")

    def throw_hand(self):
        self.__hand = []
        self.__hand_value = 0

class Player(Dealer):

    def __init__(self, name: str):
        Dealer.__init__(self)
        if isinstance(name, str):
            self.__name = name
        else:
            raise Exception("Player.__init__(): name should be a str.")
        self.__score = 0

    def get_name(self):
        return self.__name
    
    def get_score(self):
        return self.__score
    
    def set_score(self, score: int):
        if ( isinstance(score, int) and score > 0 ):
            self.__score = score
        else:
            raise Exception("Player.set_score(): Score should be an int > 0.")

class Game:

    def __init__(self):
        self.__pack = []
        self.__players_amount = None
        self.__players = [Player]
        self.__dealer = Dealer()
        self.playing = True
        
    def display_cards(self):
        for card in self.__pack:
            card.display_card()

    def build_pack(self):
        self.__pack = []
        colors = ["Trèfle","Carreau","Coeur","Pique"]
        for color in colors:
            for i in range(1,14):
                card = Card(color,i)
                card.set_blackjack_value()
                self.__pack.append(card)
        print("Le croupier sort un nouveau paquet de carte...")
        sleep(2)
    
    def shuffle_pack(self):
        shuffle(self.__pack)
        print("Le croupier mélange les cartes.")
        print("tchff tchff tchff...")
        sleep(2)
    
    def build_players(self):
        self.__players = []
        for i in range(1,self.__players_amount+1):
            name = None
            while not (isinstance(name, str)):
                name = input(f"Joueur {i}, comment vous appelez-vous? ")
            self.__players.append(Player(name))
    
    def start_game(self):
        for player in self.__players:
            for _ in range(2):
                player.get_card(self.__pack[-1])
                print(f"{player.get_name()}: Vous avez reçu une carte {self.__pack[-1].get_card_name()}.")
                self.__pack.pop()
                sleep(1)
            player.set_hand_value()
            print(f"{player.get_name()}, votre main vaut {player.get_hand_value()} points.")
            sleep(1)
        
    def ask_how_many_players(self):
        self.__players_amount = 0
        while not ( 1 <= self.__players_amount <= 7 ):
            self.__players_amount = int(input("Combien de personnes veulent jouer? (1-7) "))

    def ask_players_choices(self):
        for player in self.__players:
            choice = ""
            while choice not in ("N","n","Non","non","NON"):
                choice = input(f"{player.get_name()}, voulez-vous une carte supplémentaire? (O/N) ")
                if choice in ("O","o","Oui","oui","OUI") :
                    player.get_card(self.__pack[-1])
                    print(f"{player.get_name()}, vous avez une carte {self.__pack[-1].get_card_name()}.")
                    sleep(1)
                    if self.__pack[-1].get_rank() == 1:
                        self.__pack[-1].ask_ace_value()
                    self.__pack.pop()
                    player.set_hand_value()
                    print(f"{player.get_name()}, votre main vaut {player.get_hand_value()} points.")
                    sleep(1)
                    if player.get_hand_value() > 21:
                        player.set_is_winning(False)
                        print(f"Dommage {player.get_name()}: vous avez perdu!")
                        break

    def dealer_turn(self):
        dealer_hand_value = 0
        while dealer_hand_value <= 17:
            self.__dealer.get_card(self.__pack[-1])
            print(f"Le croupier a pioché une carte {self.__pack[-1].get_card_name()}.")
            sleep(1)
            if self.__pack[-1].get_rank() == 1:
                if self.__dealer.get_hand_value() <= 10:
                    self.__pack[-1].set_value(11)
                    print("Le croupier a choisi une valeur d'As à 11.")
                else:
                    print("Le croupier a choisi une valeur d'As à 1.")
                sleep(1)
            self.__pack.pop()
            self.__dealer.set_hand_value()
            dealer_hand_value = self.__dealer.get_hand_value()
            
    def reward_winners(self):
        for player in self.__players:
            if player.get_is_winning():
                if self.__dealer.get_hand_value() < player.get_hand_value() or self.__dealer.get_hand_value() > 21:
                    player.set_score(player.get_score() + 1)
                    print(f"Bravo {player.get_name()}! Vous avez battu le croupier avec {player.get_hand_value()} contre {self.__dealer.get_hand_value()} points.")
                else:
                    print(f"{player.get_name()}, vous avez perdu.")
                sleep(1)

    def reset_game(self):
        for player in self.__players:
            player.throw_hand()
        self.__dealer.throw_hand()
        self.build_pack()
        self.shuffle_pack()

    def ask_to_play_again(self):
        choice = ""
        while choice not in ("N","n","Non","non","NON","O","o","Oui","oui","OUI"):
            choice = input(f"Voulez-vous jouer encore? (O/N) ")
            if choice in ("N","n","Non","non","NON") :
                self.playing = False
def main():
    try:
        game = Game()
        game.ask_how_many_players()
        game.build_players()
        while game.playing:
            game.reset_game()
            game.start_game()
            game.ask_players_choices()
            game.dealer_turn()
            game.reward_winners()
            game.ask_to_play_again()
        print("\nMerci d'avoir joué au BlackJack.")

    except KeyboardInterrupt:
        print("\nMerci d'avoir joué au BlackJack.")

if __name__ == "__main__":
    main()