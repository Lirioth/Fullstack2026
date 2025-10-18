# ⭕ Tic-Tac-Toe Game

A classic 2-player Tic-Tac-Toe game in the terminal with intelligent win detection and tie handling.

## 📊 Quick Stats

| Metric | Value |
|--------|-------|
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Python Version** | 3.8+ |
| **Topics** | 2D Lists, Game Logic, Win Detection |
| **Files** | 1 Python file |
| **Concepts** | Board State, Pattern Matching, Input Validation |

## 🎯 Learning Objectives

By completing this project, you will:

- ✅ **Work with 2D data structures** representing game boards
- ✅ **Implement win detection algorithms** checking rows, columns, diagonals
- ✅ **Build turn-based game logic** alternating between players
- ✅ **Practice input validation** ensuring valid moves
- ✅ **Handle edge cases** detecting ties and full boards
- ✅ **Create user-friendly interfaces** with clear board display

## 📂 Project Structure

```
TicTacToe/
└── tictactoe.py         # Complete game implementation
```

## 🚀 How to Run

```bash
# Navigate to the TicTacToe directory
cd Exercises/TicTacToe

# Run the game
python tictactoe.py
```

## 🎮 Game Rules

1. **Setup**: 3x3 grid with row and column coordinates (1-3)
   ```
     1 2 3
   1  | | 
     -----
   2  | | 
     -----
   3  | | 
   ```

2. **Gameplay**:
   - Player X starts first
   - Players alternate turns
   - **Enter "row col" format** (e.g., "2 3" for row 2, column 3)
   - First player to get 3 in a row wins
   - Game ends in tie if board fills with no winner

3. **Win Conditions**:
   - Horizontal: Three marks in same row
   - Vertical: Three marks in same column
   - Diagonal: Three marks from corner to corner

## 💡 Key Features

### Board Display
```
Current board:
 X |   | O
-----------
   | X |  
-----------
 O |   | X
```

### Win Detection
- **Rows**: Checks all 3 horizontal lines
- **Columns**: Checks all 3 vertical lines
- **Diagonals**: Checks both diagonal lines (top-left to bottom-right, top-right to bottom-left)

### Input Validation
- Rejects numbers outside 1-3 range for rows and columns
- Prevents overwriting occupied squares
- Handles invalid input gracefully
- Clear error messages guide users to correct format

### Tie Detection
- Monitors board fullness
- Declares tie when no moves remain and no winner

### Replay Functionality ✨
- **Play again option** after each game completes
- Fresh board automatically created for new game
- Graceful exit with goodbye message
- Seamless game flow without restarting program

## 🧩 Example Game

```
🎮 Welcome to Tic Tac Toe! 🎮

  1 2 3
1  | | 
  -----
2  | | 
  -----
3  | | 
Player X, enter row and col (1-3 1-3) 🙂: 2 2

  1 2 3
1  | | 
  -----
2  |X| 
  -----
3  | | 
Player O, enter row and col (1-3 1-3) 🙂: 1 1

  1 2 3
1 O| | 
  -----
2  |X| 
  -----
3  | | 
Player X, enter row and col (1-3 1-3) 🙂: 1 3

  1 2 3
1 O| |X
  -----
2  |X| 
  -----
3  | | 
Player O, enter row and col (1-3 1-3) 🙂: 3 1

  1 2 3
1 O| |X
  -----
2  |X| 
  -----
3 O| | 
Player X, enter row and col (1-3 1-3) 🙂: 3 3

  1 2 3
1 O| |X
  -----
2  |X| 
  -----
3 O| |X
Player X wins!

🔄 Play again? (y/n): n

👋 Thanks for playing! Goodbye! 🎉
```

Player O, choose a position (1-9): 1
 O |   |  
-----------
   | X |  
-----------
   |   |  

Player X, choose a position (1-9): 3
 O |   | X
-----------
   | X |  
-----------
   |   |  

Player O, choose a position (1-9): 7
 O |   | X
-----------
   | X |  
-----------
 O |   |  

Player X wins! 🎉
```

## 🔧 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Board not displaying** | Check terminal width, ensure at least 15 characters wide |
| **Invalid move accepted** | Verify `is_valid_move()` function checks both range and occupation |
| **Winner not detected** | Review `check_winner()` logic for all 8 winning combinations |
| **Game continues after win** | Ensure main loop breaks when `check_winner()` returns True |

## 🎓 Concepts Demonstrated

1. **2D Data Structures**
   - Board represented as list of lists `[[],[],[]]`
   - Index mapping: position → row/col coordinates
   - State tracking for each cell

2. **Algorithm Design**
   - Win detection with row/column/diagonal checks
   - Move validation logic
   - Tie detection algorithm

3. **Game State Management**
   - Current player tracking
   - Move history implicit in board state
   - Win/tie/ongoing states

4. **User Interface**
   - Clear board visualization
   - Informative prompts
   - Victory/tie announcements

## 📝 Code Quality Notes

- ✅ **Clean function separation** (display, validation, win checking)
- ✅ **Type hints** for better code clarity
- ✅ **Descriptive variable names** (`current_player`, `board`)
- ✅ **No external dependencies** - pure Python 3.8+
- ✅ **Comprehensive comments** explaining game logic

## 🎯 Extension Ideas

Want to enhance the game? Try:

1. **AI Opponent**: Implement computer player with minimax algorithm
2. **Difficulty Levels**: Easy (random), Medium (blocking), Hard (optimal)
3. **Scoreboard**: Track wins/losses/ties across multiple games
4. **Undo Move**: Allow players to take back last move
5. **Board Sizes**: Support 4x4 or 5x5 boards
6. **Themes**: Customize X/O symbols (emojis, colors)

## 👤 Author

**Kevin Cusnir 'Lirioth'**  
Repository: [Fullstack2026](https://github.com/Lirioth/Fullstack2026)  
Week 1 Day 5 - Mini Project

---

*Enjoy the classic game!* ⭕❌
