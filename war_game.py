import random


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
    """
    Continuously play rounds until one player has all the cards.
    """

    def __init__(self, player1_name, player2_name):
        self.player1 = Player(name=player1_name)
        self.player2 = Player(name=player2_name)
        self.deck = Deck()
        self.deck.shuffle()
    

    def start(self):
        self.player1 = input("Enter the name of player 1: ")
        self.player2 = input("Enter the name of player 2: ")
        self.player1.hand, self.player2.hand = self.deck.split()

    def message(self):
        print(f"Welcome {self.player1.name} and {self.player2.name}. Let’s start the game!")

    #Make sure players can show their top card when it's their turn.

    def compare_cards(self, card1, card2):
        """
        Compares two cards. Returns:
        - 0 if it's a tie.
        - 1 if card1 is greater.
        - 2 if card2 is greater.
        """
        rank_order = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

        # Find the indices (positions) of the cards in the rank_order list
        card1_rank = rank_order.index(card1.rank)
        card2_rank = rank_order.index(card2.rank)

        if card1_rank > card2_rank:
            return 1
        elif card1_rank < card2_rank:
            return 2
        else:
            return 0

    def game_loop(self):
        """
        Executes the main game loop until one of the players runs out of cards.
        """
        # Ensuring that the game loop continues as long as both players have cards to play. 
        while len(self.player1.hand) > 0 and len(self.player2.hand) > 0:
            player1_card = self.player1.draw()
            player2_card = self.player2.draw()

            print(f"{self.player1.name} reveals: {player1_card}")
            print(f"{self.player2.name} reveals: {player2_card}")

            result = self.compare_cards(player1_card, player2_card)

            if result == 0:
                # Tie - both cards are discarded
                print("It's a tie! Both cards are discarded.")

            elif result == 1:
                # Player 1 wins the round
                self.player1.hand.extend([player1_card, player2_card])
                print(f"{self.player1.name} wins the round and collects the cards.")

            else:
                # Player 2 wins the round
                self.player2.hand.extend([player1_card, player2_card])
                print(f"{self.player2.name} wins the round and collects the cards.")

    
if __name__ == "__main__":
    war_game = Game()
    war_game.start()

