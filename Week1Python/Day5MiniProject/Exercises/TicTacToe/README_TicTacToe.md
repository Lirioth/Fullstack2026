# 🎮 Mini-Project — Tic Tac Toe (CLI)

A tiny 2‑player Tic Tac Toe you can run in the terminal. Simple, readable, and fully commented in English.

## 🚀 How to run
```bash
python3 tictactoe.py
```

## 🎯 How to play
- The board is 3×3. Player **❌ X** starts, then **⭕ O**.
- On your turn, type **row** and **col** (numbers 1..3). Example: `2 3`
- A move is valid only if it's inside the grid and the cell is empty.
- First player with 3 in a row (row, column, or diagonal) **🏆 wins**.
- If the board fills up with no winner, it's a **🤝 tie**.

## 📁 Files
- `tictactoe.py` — complete game implementation.
- **⚙️ Functions:**
  - `new_board()` — create an empty board.
  - `display_board(board)` — print the board.
  - `player_input(board, player)` — read/validate a move.
  - `check_win(board, player)` — detect a win.
  - `is_tie(board)` — detect a tie.
  - `play()` — main game loop.

## Example session
```
  1 2 3
1  | | 
  -----
2  | | 
  -----
3  | | 
Player X, enter row and col (1-3 1-3): 2 2
  1 2 3
1  | | 
  -----
2  |X| 
  -----
3  | | 
Player O, enter row and col (1-3 1-3): 1 1
...
Player X wins!
```

## Notes
- The code favors clarity over micro-optimizations.
- To add features (e.g., replay prompt or AI), extend `play()` or add new helpers.
