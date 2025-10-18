# 🎮 Hangman Game# 🎮 Mini-Project #2 — Hangman (Python) ✨



A fully playable terminal-based Hangman game implementing conditionals, loops, functions, and modular programming concepts.Learn and practice **Conditionals, Loops, Functions, and Modules** by building a fully playable **Hangman** game in the terminal.  

English-only code & comments ✅ — Emoji-rich README ✅ — Simple to run ✅

## 📊 Quick Stats

## 📂 Structure

| Metric | Value |```

|--------|-------|hangman_project/

| **Difficulty** | ⭐⭐⭐ Intermediate |├─ src/

| **Python Version** | 3.8+ |│  ├─ game.py    # Core game logic (HangmanGame class)

| **Topics** | Game Logic, Classes, Modular Design |│  ├─ words.py   # Word list + random chooser

| **Files** | 4 Python files (1 main + 3 modules) |│  └─ art.py     # ASCII gallows for 0..6 mistakes

| **Concepts** | State Machines, Input Validation, ASCII Art |└─ main.py       # CLI runner (play again loop)

```

## 🎯 Learning Objectives  

## 🚀 Run

By completing this project, you will:```bash

python3 main.py

- ✅ **Build a complete game loop** with play-again functionality```

- ✅ **Design state machines** tracking game progress and user inputYou’ll see the ASCII gallows and a masked word (letters as `*`). Type a **single letter** and press Enter to guess.  

- ✅ **Implement modular architecture** separating concerns (game logic, data, UI)- Correct? Letters appear in all matching positions.  

- ✅ **Practice OOP principles** with the `HangmanGame` class- Wrong? A new body part is added (6 total).  

- ✅ **Master input validation** accepting only single letters- No repeated guesses allowed.  

- ✅ **Work with ASCII art** for visual feedback- Spaces and punctuation in phrases are shown as-is.  



## 📂 Project Structure## 🧠 Rules Recap

- The computer picks a random word/phrase and shows `*` for each letter (spaces remain visible).

```- You guess letters until you **solve** it or the gallows completes (6 mistakes).

Hangman/- Repeating a guessed letter is not allowed and doesn’t cost a life.

├── main.py              # CLI runner with play-again loop

└── src/## 🛠️ Notes

    ├── game.py          # Core game logic (HangmanGame class)- Clean, well-commented code for readability.

    ├── words.py         # Word list + random selection- Separated into modules to emphasize **modularity**.

    └── art.py           # ASCII gallows art (0-6 mistakes)- Works with Python 3.8+ and no external dependencies.

```

## 🎯 Example Words

## 🚀 How to RunIncludes the starter list (e.g., `correction`, `python`, `credit card`, `south`, etc.). You can add more in `src/words.py`.



```bash## 💡 Tips

# Navigate to the Hangman directory- Keep guesses to **one letter**.  

cd Exercises/Hangman- If you want to add a “guess the full word” feature, it’s easy—look for the input loop in `main.py`.



# Run the gameHave fun & happy hacking! ✨🐍

python main.py
```

## 🎮 Game Rules

1. **Objective**: Guess the hidden word/phrase before the gallows completes
2. **Gameplay**:
   - Computer picks a random word/phrase
   - Letters are shown as `*`, spaces/punctuation remain visible
   - Guess one letter at a time
   - Correct guesses reveal all matching positions
   - Wrong guesses add a body part to the gallows (max 6 mistakes)
3. **Win Condition**: Reveal all letters before 6 wrong guesses
4. **Lose Condition**: Complete the gallows (6 wrong guesses)

## 💡 Key Features

### Modular Design
- **`game.py`**: Contains `HangmanGame` class managing game state
  - Tracks guessed letters, wrong attempts, masked display
  - Only letters are maskable; spaces/punctuation show as-is
- **`words.py`**: Word source with `random_word()` function
  - Starter list: `correction`, `python`, `credit card`, `south`, etc.
  - Easy to expand with more words/phrases
- **`art.py`**: ASCII art for visual feedback
  - 7 gallows stages (0-6 wrong guesses)
  - Defines `MAX_WRONG = 6` constant

### Intelligent Masking
```python
# Example: "credit card"
# Display: "****** ****"
# After guessing 'c': "c***c* c***"
# After guessing 'r': "cr***c car*"
```

### Input Validation
- Accepts only single alphabetic characters
- Rejects repeated guesses (doesn't count as wrong)
- Case-insensitive (converts all to lowercase)

## 🧩 Example Words

The starter word list includes:
- `correction`, `childish`, `beach`, `python`
- `assertive`, `interference`, `complete`
- `share`, `credit card`, `rush`, `south`

**Add more in `src/words.py`** to expand the game!

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Import errors** | Ensure you run from the `Hangman/` directory or use `python -m` |
| **ASCII art not displaying** | Use a terminal with proper Unicode support |
| **"No guesses left" immediately** | Check `MAX_WRONG` in `art.py` is set to 6 |
| **Repeated guess allowed** | Verify `guessed` set is tracking correctly in `game.py` |

## 🎓 Concepts Demonstrated

1. **Object-Oriented Programming**
   - `HangmanGame` class encapsulating state and behavior
   - Methods: `guess()`, `display()`, `is_won()`, `is_lost()`

2. **Modular Programming**
   - Separation of concerns (game logic, data, UI)
   - Clean imports between modules

3. **State Management**
   - Tracking guessed letters with `Set[str]`
   - Wrong attempt counter
   - Win/loss conditions

4. **String Manipulation**
   - Character masking with `*`
   - Case normalization
   - Letter detection with `isalpha()`

## 📝 Code Quality Notes

- ✅ **Full type hints** on all functions and methods
- ✅ **Comprehensive docstrings** explaining behavior
- ✅ **Clean separation of concerns** across modules
- ✅ **No external dependencies** - pure Python 3.8+
- ✅ **Emoji-rich output** for engaging user experience

## 🎯 Extension Ideas

Want to enhance the game? Try:

1. **Difficulty levels**: Easy/Medium/Hard word lists
2. **Score tracking**: Keep track of wins/losses across sessions
3. **Hint system**: Reveal random letter for cost of 1 wrong guess
4. **Full word guessing**: Allow typing entire word as final guess
5. **Multiplayer**: Player 1 enters word, Player 2 guesses
6. **Save/Load**: Persist game state to continue later

## 👤 Author

**Kevin Cusnir 'Lirioth'**  
Repository: [Fullstack2026](https://github.com/Lirioth/Fullstack2026)  
Week 1 Day 5 - Mini Project

---

*Have fun and happy hacking!* ✨🐍
