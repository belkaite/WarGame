# 🃏 WarGame 🃏

A classic War card game implemented using Python and following the Object-Oriented Programming paradigm.

## 📜 Rules of the Game

1. **Setup**: 🎴 A deck of cards is shuffled and divided evenly between two players. No jokers included.
2. **Card Battle**: 🤺 Each player reveals the top card of their deck.
3. **Determine Winner**: 🏆 The player with the higher card wins the round and adds both cards to their deck.
4. **Tie**: ➖ In case of a tie, both cards are discarded, and no player collects them.
5. **End Condition**: 🏁 The game ends when a player runs out of cards.
6. **Players**: 🧑‍🤝‍🧑 The game is designed for exactly two players.

## 🔄 Game Flow

### 1. Initialization
- **Player Setup**: 👥 Obtain the names of the two players.
- **Deck Setup**: 🃏 Initialize and shuffle a deck, distributing it evenly among the players.
- **Start Message**: 🚦 Introduce players and announce the start of the game.

### 2. Game Rounds
- **Card Draw**: 🗳️ Players reveal their top card, which is displayed by the program.
- **Determine Round Winner**: 🥇 Compare cards and determine the round's winner or declare a tie:
  - **Win**: The round’s winner takes both cards, adding them to their deck. Display the updated card count for both players.
  - **Tie**: Discard both cards and display the updated card count for both players.

### 3. Conclusion
- **Natural End**: 🏅 If a player runs out of cards, announce the other player as the winner and display the final card count.
- **Forced End**: ⛔ On `Ctrl + D`, conclude the game, declare the player with the most cards as the winner, and display the final card count.





