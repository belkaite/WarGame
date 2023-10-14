# WarGame

A classic War card game implemented using Python with Object-Oriented Programming paradigm.

## Rules of the Game

1. **Setup**: A deck of cards is shuffled and divided evenly between two players. No jokers are included.
2. **Card Battle**: Each player reveals the top card of their deck.
3. **Determine Winner**: The player with the higher card wins the round and collects both cards, placing them at the bottom of their deck.
4. **Tie**: In case of a tie, both cards are discarded, and no player collects them.
5. **End Condition**: The game ends when a player runs out of cards.
6. **Players**: The game is designed for exactly two players.

## Game Flow

### 1. Initialization
- **Player Setup**: Get the names of the two players.
- **Deck Setup**: Initialize and shuffle a deck, distributing it evenly among the players.
- **Start Message**: Introduce players and indicate the start of the game.

### 2. Game Rounds
- **Card Draw**: Players reveal their top card, which is displayed by the program.
- **Determine Round Winner**: Compare the cards and determine the round's winner or if there's a tie:
  - **Win**: Indicate the round’s winner, transfer cards to the winner’s deck, and show the updated card count for both players.
  - **Tie**: Declare a tie, discard the cards, and display the updated card count for both players.

### 3. Conclusion
- **Natural End**: If a player runs out of cards, announce the other player as the winner and show the final card count.
- **Forced End**: On `Ctrl + D`, conclude the game, declare the player with the most cards as the winner, and show the final card count.