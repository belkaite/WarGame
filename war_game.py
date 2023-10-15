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

# Initialization
player1_name, player2_name = get_player_names()
player1 = Player(name=player1_name)
player2 = Player(name=player2_name)
deck = Deck()
deck.shuffle()
# Deal cards to players
player1.hand, player2.hand = deck.split()
# Welcome Message
print(f"Welcome {player1.name} and {player2.name}. Let’s start the game!")

