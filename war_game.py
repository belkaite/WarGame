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
        self.cards = [
            Card(rank, suit)
            for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]
            for rank in [
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                "10",
                "Jack",
                "Queen",
                "King",
                "Ace",
            ]
        ]

    def shuffle(self):
        random.shuffle(self.cards)

    def split(self):
        return self.cards[:26], self.cards[26:]


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self):
        return self.hand.pop(0)


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
        self.player1.hand, self.player2.hand = self.deck.split()

    def message(self):
        pass

    def compare_cards(self, card1, card2):
        """
        Compares two cards. Returns:
        - 0 if it's a tie.
        - 1 if card1 is greater.
        - 2 if card2 is greater.
        """
        rank_order = [
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "Jack",
            "Queen",
            "King",
            "Ace",
        ]

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
        Executes the main game loop until one of the players runs out of cards or the game is interrupted.
        """
        war_pile = []

        print(
            f"Welcome {self.player1.name} and {self.player2.name}. Let’s start the game? Yes/No"
        )
        welcome_msg = input().lower().strip()

        if welcome_msg == "yes":
            try:
                while len(self.player1.hand) > 0 and len(self.player2.hand) > 0:
                    player1_card = self.player1.draw()
                    player2_card = self.player2.draw()

                    print(f"{self.player1.name} reveals: {player1_card}")
                    print(f"{self.player2.name} reveals: {player2_card}")

                    result = self.compare_cards(player1_card, player2_card)

                    print("Press 'Enter' to see the result...")
                    input()

                    if result == 0:
                        print("It's a tie!")
                        war_pile.extend([player1_card, player2_card])
                        if len(self.player1.hand) == 0 or len(self.player2.hand) == 0:
                            break
                    elif result == 1:
                        self.player1.hand.extend([player1_card, player2_card])
                        if war_pile:
                            self.player1.hand.extend(war_pile)
                            war_pile.clear()
                        print(
                            f"{self.player1.name} wins the round and collects the cards. The player has {len(self.player1.hand)} now, while {self.player2.name} has {len(self.player2.hand)}"
                        )
                    else:
                        self.player2.hand.extend([player1_card, player2_card])
                        if war_pile:
                            self.player2.hand.extend(war_pile)
                            war_pile.clear()
                        print(
                            f"{self.player2.name} wins the round and collects the cards. The player has {len(self.player2.hand)} now, while {self.player1.name} has {len(self.player1.hand)}"
                        )

                    print("-" * 50)
                    print("Next round is about to start...")
                    input(
                        "Press 'Enter' to play the next round or 'Ctrl + D' to conclude the game..."
                    )

            except EOFError:
                pass

        if len(self.player1.hand) == 0:
            print(
                f"{self.player2.name} wins the game with {len(self.player2.hand)} cards!"
            )
        elif len(self.player2.hand) == 0:
            print(
                f"{self.player1.name} wins the game with {len(self.player1.hand)} cards!"
            )
        else:
            if len(self.player1.hand) > len(self.player2.hand):
                print(
                    f"The game was interrupted. {self.player1.name} has the most cards with {len(self.player1.hand)} and is the winner!"
                )
            elif len(self.player1.hand) < len(self.player2.hand):
                print(
                    f"The game was interrupted. {self.player2.name} has the most cards with {len(self.player2.hand)} and is the winner!"
                )
            else:
                print("The game was interrupted. It's a tie!")


if __name__ == "__main__":
    player1_name = input("Enter the name of player 1: ")
    player2_name = input("Enter the name of player 2: ")
    war_game = Game(player1_name, player2_name)
    war_game.start()
    war_game.message()
    war_game.game_loop()
