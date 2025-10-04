# 🎮 Mini-Project #2 — Hangman (Python) ✨

Learn and practice **Conditionals, Loops, Functions, and Modules** by building a fully playable **Hangman** game in the terminal.  
English-only code & comments ✅ — Emoji-rich README ✅ — Simple to run ✅

## 📂 Structure
```
hangman_project/
├─ src/
│  ├─ game.py    # Core game logic (HangmanGame class)
│  ├─ words.py   # Word list + random chooser
│  └─ art.py     # ASCII gallows for 0..6 mistakes
└─ main.py       # CLI runner (play again loop)
```
  
## 🚀 Run
```bash
python3 main.py
```
You’ll see the ASCII gallows and a masked word (letters as `*`). Type a **single letter** and press Enter to guess.  
- Correct? Letters appear in all matching positions.  
- Wrong? A new body part is added (6 total).  
- No repeated guesses allowed.  
- Spaces and punctuation in phrases are shown as-is.  

## 🧠 Rules Recap
- The computer picks a random word/phrase and shows `*` for each letter (spaces remain visible).
- You guess letters until you **solve** it or the gallows completes (6 mistakes).
- Repeating a guessed letter is not allowed and doesn’t cost a life.

## 🛠️ Notes
- Clean, well-commented code for readability.
- Separated into modules to emphasize **modularity**.
- Works with Python 3.8+ and no external dependencies.

## 🎯 Example Words
Includes the starter list (e.g., `correction`, `python`, `credit card`, `south`, etc.). You can add more in `src/words.py`.

## 💡 Tips
- Keep guesses to **one letter**.  
- If you want to add a “guess the full word” feature, it’s easy—look for the input loop in `main.py`.

Have fun & happy hacking! ✨🐍
