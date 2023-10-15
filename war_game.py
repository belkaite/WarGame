import random

def get_player_names():
    """
    Get names of the two players.
    """
    player1 = input("Enter the name of player 1: ")
    player2 = input("Enter the name of player 2: ")
    return player1, player2

class Card:
    """
    Represent a playing card.
        rank: "2", "3", "4", ..., "King", "Ace".
        suit: "Hearts", "Diamonds", "Clubs", "Spades".
    """

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    

class Deck: 
    """
    Represent a deck of 52 playing cards (does not include the Jokers).
    Shullfte the deck. 
    Splits the deck for each player.
    """
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in ["Hearts", "Diamonds", "Clubs", "Spades"] 
                                      for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]]

    def shuffle(self):
        random.shuffle(self.cards)

    def split(self):
        return self.cards[:26], self.cards[26:]

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def __str__(self):
        pass
        # Create a string of cards using their __str__ method and join them with commas
        #cards_string = ', '.join(str(card) for card in self.hand)
        #return f"{self.name} has {len(self.hand)} cards: {cards_string}"

    def draw(self):
         return self.hand.pop(0)


# Welcome Message
# print(f"Welcome {player1.name} and {player2.name}. Let’s start the game!")
# Directly print out each player's hand
# print(len(player1.hand))

class Game:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(name=player1_name)
        self.player2 = Player(name=player2_name)
        self.deck = Deck()
        self.deck.shuffle()
    
    def start(self):
        self.player1.hand, self.player2.hand = self.deck.split()

    def message(self):
        print(f"Welcome {self.player1.name} and {self.player2.name}. Let’s start the game!")

    #Make sure players can show their top card when it's their turn.
    def game_loop(self):

        try:
            while self.player1.hand != 0 or self.player2.hand != 0:
                cards_shown = []
                card_from_player1 = self.player1.draw
                cards_shown.append(card_from_player1)
                print(f"{player1.name} has placed {card_from_player1}")

                card_from_player2 = self.player2.draw
                cards_shown.append(card_from_player2)
                print(f"{player2.name} has placed {card_from_player2}")

                #if #rankas is pirmo playerio == #rankas is antro playerio:
                    #War logic

                
        except:
            pass


    


