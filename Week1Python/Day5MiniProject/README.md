# 📅 Day 5 - Mini Project Week

**Author:** Kevin Cusnir "Lirioth"  
**Course:** Fullstack Bootcamp 2026  
**Last Updated:** October 18, 2025

🎉 Congratulations! You've reached the capstone of Week 1. Time to showcase your Python mastery with complete, production-ready applications that integrate everything you've learned!

## Overview

Day 5 bundles the entire first week into portfolio-ready mini projects. Tic-Tac-Toe and Hangman demonstrate how to structure multi-module apps with validation, user feedback, and replay loops while the challenge sets push your algorithmic thinking.

## Features

- Two flagship games (Tic-Tac-Toe, Hangman) with modular architecture, validation, and replay support
- Challenge collections that reinforce problem solving, pattern recognition, and data processing
- Detailed project walkthroughs, architecture diagrams, and future enhancements checklists

## Quick Start

```bash
cd Day5MiniProject/Exercises/TicTacToe
python tictactoe.py
```

Launch Hangman and the challenge sets by navigating to their directories and running the provided entry scripts.

## 📊 Quick Stats

| Metric | Value |
|--------|-------|
| **⏰ Duration** | 8-12 hours |
| **🎯 Difficulty** | 🟡 Intermediate to 🔴 Advanced |
| **📝 Projects** | 2 Major (Tic-Tac-Toe, Hangman) + 4 Challenge Sets |
| **✅ Prerequisites** | Days 1-4 completion required |
| **🐍 Python Version** | 3.8+ |
| **📚 Key Topics** | Integration, Architecture, Game Logic, Algorithms |

## 📑 Table of Contents
- [📦 Overview](#overview)
- [✨ Features](#features)
- [⚡ Quick Start](#quick-start)
- [🎯 Learning Objectives](#-learning-objectives)
- [📚 Week 1 Integration](#-week-1-integration)
- [📁 Directory Structure](#-directory-structure)
- [🚀 Projects Portfolio Overview](#-projects-portfolio-overview)
- [🏗️ Project Architecture Lessons](#️-project-architecture-lessons)
- [📊 Assessment Checklist](#-assessment-checklist)
- [🔧 Troubleshooting](#-troubleshooting)
- [🔗 Next Steps](#-next-steps)
- [📄 License](#-license)

## 🎯 Learning Objectives

By the end of this day, you will confidently:
- 🔗 Integrate all Week 1 concepts (variables, loops, dictionaries, functions) into cohesive applications
- 🏗️ Plan, structure, and architect multi-component programs
- 🧩 Apply systematic problem-solving strategies to complex challenges
- ✨ Write clean, organized, professional-grade documented code
- 🐛 Debug and test your own programs with systematic approaches
- 🎤 Present and articulate your code solutions clearly
- 🎮 Build interactive games with user-friendly interfaces
- 📈 Implement advanced algorithms and data processing pipelines

## 📚 Week 1 Integration

### 🧠 Skills You'll Apply
This day combines everything from Week 1:
- **Day 1**: Variables, conditionals, input/output, basic operations
- **Day 2**: Lists, loops, data formatting, iteration patterns  
- **Day 3**: Dictionaries, data structures, key-value manipulation
- **Day 4**: Functions, code organization, parameter handling

### 💡 Project-Based Learning
- Real-world problem solving
- Code architecture and design
- Testing and validation
- Documentation and presentation

## 📁 Directory Structure

```
Day5MiniProject/
├── 📄 README.md                        # This overview file
├── 🧠 Exercises/                       # Practice exercises and mini projects
│   ├── 💡 Challenges1/                 # Challenge set one solutions
│   │   └── 📄 challengessolutions.py   # Run to review solution implementations
│   ├── 💡 Challenges2/                 # Challenge set two implementations
│   │   └── 📄 main.py                  # Run to explore advanced practice problems
│   ├── 🎯 Hangman/                     # Hangman word game
│   │   └── 📄 main.py                  # Run to play the Hangman game
│   └── 🎮 TicTacToe/                   # Tic-Tac-Toe project files
│       └── 📄 tictactoe.py             # Complete game code
└── 💪 DailyChallenge/                  # Additional challenges
    ├── 🚀 AdvancedAlgorithm/           # Extended algorithm challenge set
    │   └── 📄 main.py                  # Entry point for advanced algorithms
    └── 🧩 Challenges/                  # Daily coding challenge collection
        └── 📄 challenges.py            # Core challenge scripts
```

## 🚀 Projects Portfolio Overview

### 🎮 **Flagship Project: Tic-Tac-Toe Game**
**Complete 3x3 grid strategy game demonstrating Week 1 mastery:**

```bash
cd Exercises/TicTacToe
python tictactoe.py
```

**🎯 Features & Implementation:**
- 🎲 **Game Board**: 3x3 grid using nested lists `[[" ", " ", " "], [...], [...]]`
- 🎨 **Visual Display**: Formatted board with row/column headers and separators
- 👥 **Two-Player System**: Alternating turns between Player X and Player O
- ✅ **Input Validation**: 
  - Parse "row col" format (e.g., "2 3")
  - Validate coordinates are in range (1-3)
  - Check cell is empty before placing mark
  - Friendly error messages with retry prompts
- 🏆 **Win Detection**: Check rows, columns, and diagonals after each move
- 🤝 **Draw Detection**: Recognize when board is full with no winner
- ⚙️ **Modular Functions**:
  - `new_board()`: Create fresh game board
  - `display_board(b)`: Render board to console
  - `parse_move(input)`: Convert input to coordinates
  - `validate_move(board, input)`: Check move validity
  - `player_input(b, player)`: Handle player input with validation
  - `check_win(b)`: Detect winning conditions
  - `play()`: Main game loop orchestration

### 🎪 **Hangman Word Guessing Game**
**Interactive word game with ASCII art visualization:**

```bash
cd Exercises/Hangman
python main.py
```

**🎯 Current Features:**
- 📚 Random word selection from word list
- 🎨 ASCII art hangman visualization (progressive gallows display)
- ✏️ Letter tracking (guessed letters, remaining attempts)
- 🔤 Input validation for single letter guesses
- 🏆 Win/lose condition detection
- 🎮 Replay functionality

**🚧 Future Enhancements (TODO):**
- 📊 Score tracking system across multiple games
- 🎚️ Multiple difficulty levels (word length selection)
- 🗂️ Word categories (animals, countries, technology, etc.)

**🗂️ Modular Structure:**
- `game.py`: Core game logic and state management
- `words.py`: Word lists and category management
- `art.py`: ASCII art display functions
- `main.py`: Game orchestration and user interface

### 💡 **Challenge Sets - Algorithm Practice**

#### **🥉 Challenges Set 1: Foundational Algorithms**
```bash
cd Exercises/Challenges1
python challengessolutions.py
```
**Focus**: Core algorithm patterns and problem-solving strategies
- String manipulation techniques
- List processing patterns
- Basic algorithm implementation
- Solution analysis and optimization

#### **🥈 Challenges Set 2: Advanced Patterns**
```bash
cd Exercises/Challenges2
python main.py
```
**📂 Structured Implementation:**
- `main.py`: Challenge orchestration
- `src/patterns.py`: Pattern recognition algorithms
- `src/ex2analysis.py`: Data analysis functions

**Topics**: 
- Complex data transformations
- Pattern matching algorithms
- Statistical analysis
- Multi-step problem solving

### 💪 **Daily Challenges - Skill Integration**

#### **🧩 Core Challenges Collection**
```bash
cd DailyChallenge/Challenges
python challenges.py
```
**Categories:**
- 🔤 String manipulation puzzles
- 📊 Data processing and transformation tasks  
- 🧮 Mathematical problem solving
- 🎯 Logic puzzles and algorithm challenges

#### **🚀 Advanced Algorithm Challenge**
```bash
cd DailyChallenge/AdvancedAlgorithm
python main.py
```

**📂 Advanced Structure:**
- `main.py`: Entry point and orchestration
- `src/pairs.py`: Pair analysis algorithms
- `src/demodata.py`: Test data generation

**Advanced Topics:**
- Pair analysis and matching algorithms
- Complex data structure manipulation
- Performance optimization techniques
- Edge case handling strategies

---

## 🎬 Project Demos & Visual Examples

### 🎮 Tic-Tac-Toe Gameplay Visualization

**Initial Board:**
```
  1 2 3
1  | | 
  -----
2  | | 
  -----
3  | | 

Player X's turn...
```

**Mid-Game:**
```
  1 2 3
1 X|O|X
  -----
2 O|X| 
  -----
3  |O| 

Player X's turn...
```

**Victory!**
```
  1 2 3
1 X|O|X
  -----
2 O|X|O
  -----
3  | |X

🏆 Player X wins! (Diagonal: 1→5→9)
```

### 🎪 Hangman Game Progress

**Round 1 (6 lives):**
```
  +---+
      |
      |
      |
      |
 ========

Word: _ _ _ _ _ _
Lives: 6
Guessed: []
Guess a letter: e
```

**Round 3 (4 lives):**
```
  +---+
  |   |
  O   |
      |
      |
 ========

Word: P _ _ _ _ N
Lives: 4
Guessed: ['E', 'A', 'O']
Guess a letter: t
```

**Victory!**
```
  +---+
  |   |
  O   |
 /|\  |
 / \  |
 ========

Word: P Y T H O N
🎉 Congratulations! You won!
Lives remaining: 2
```

---

## 🏗️ Project Architecture Lessons

### 📐 Tic-Tac-Toe Structure (MVC Pattern)

```
📦 tictactoe.py
│
├─ 🧠 GAME LOGIC (Model)
│  ├─ new_board() → [[" "]*3, [" "]*3, [" "]*3]
│  │     Creates empty 3x3 board
│  │
│  ├─ check_win(board, player) → bool
│  │     Checks rows, columns, diagonals
│  │
│  └─ is_tie(board) → bool
│        Checks if board is full
│
├─ 🖥️ DISPLAY (View)
│  └─ display_board(board) → None
│        Renders board to console with formatting
│
└─ 🎮 USER INTERACTION (Controller)
   ├─ player_input(board, player) → (row, col)
   │     Gets and validates move from user
   │
   ├─ parse_move(input) → (row, col)
   │     Converts "2 3" to (1, 2)
   │
   ├─ validate_move(board, input) → (row, col)
   │     Checks if move is legal
   │
   └─ play() → None
         Main game loop orchestration

Benefits of this structure:
✅ Separation of concerns
✅ Easy to test individual components
✅ Clear responsibility boundaries
✅ Simple to add features (AI, replay, etc.)
```

### 🎪 Hangman Modular Design

```
📦 hangman/
│
├─ 📁 src/
│  │
│  ├─ 📄 game.py (Business Logic)
│  │  └─ HangmanGame class
│  │     ├─ __init__(word)
│  │     ├─ guess_letter(letter) → bool
│  │     ├─ is_won() → bool
│  │     ├─ is_lost() → bool
│  │     └─ get_display_word() → str
│  │
│  ├─ 📄 words.py (Data Layer)
│  │  ├─ WORD_LIST = [...]
│  │  └─ get_random_word() → str
│  │
│  └─ 📄 art.py (Presentation Layer)
│     └─ HANGMAN_STAGES = [...]
│         Returns ASCII art for each stage
│
└─ 📄 main.py (Entry Point)
   └─ Main game loop
      ├─ Create game instance
      ├─ Display current state
      ├─ Get user input
      ├─ Update game state
      └─ Check win/loss conditions

Architecture Benefits:
✅ Each file has single responsibility
✅ Easy to add new word categories
✅ Simple to change ASCII art
✅ Game logic independent of display
✅ Can reuse components in other projects
```

---

## 🎓 Key Takeaways & Skills Integration

### What You've Learned This Week

| Week 1 Concept | Where You Used It | Why It Matters |
|----------------|-------------------|----------------|
| **Variables** | Board state, player names, scores | Storing and tracking data |
| **Conditionals** | Win checking, input validation | Decision making logic |
| **Loops** | Game loops, input retry | Repetitive tasks & iteration |
| **Lists** | Board grid, word letters, guesses | Dynamic data collections |
| **Dictionaries** | *Not used yet - see challenges!* | Key-value data management |
| **Functions** | Every game action | Code organization & reuse |
| **Strings** | Word display, user messages | Text manipulation |
| **Input/Output** | User interaction, game display | User experience |
| **Error Handling** | Invalid moves, bad input | Robust applications |

### 🎯 Professional Coding Patterns You've Applied

1. **Input Validation Loop**
   ```python
   while True:
       try:
           # Get and validate input
           break  # Exit on success
       except ValueError:
           # Show error and retry
   ```

2. **Game State Management**
   ```python
   board = new_board()  # Initialize
   while not game_over:
       display_board(board)  # Show state
       move = get_input()    # Get action
       update_board(move)    # Update state
       check_conditions()    # Evaluate
   ```

3. **Separation of Concerns**
   - Data (board, words)
   - Logic (win checking, validation)
   - Display (rendering, formatting)
   - Control (game loop, flow)

---

## 📊 Project Assessment Rubric

Use this rubric to evaluate your project quality and identify areas for improvement:

### 🎮 Tic-Tac-Toe Evaluation (100 Points Total)

| Criterion | Points | Requirements | Self-Check |
|-----------|--------|--------------|------------|
| **🎯 Functionality** | 40 | ✅ Game plays correctly start to finish<br>✅ Win detection works (rows, cols, diagonals)<br>✅ Tie detection works<br>✅ Turn alternation is correct | ⬜ |
| **🛡️ Input Validation** | 20 | ✅ Handles out-of-bounds input (0, 4, 99)<br>✅ Prevents overwriting occupied cells<br>✅ Accepts valid formats (1 1, 2 3, etc)<br>✅ Clear error messages displayed | ⬜ |
| **🏗️ Code Quality** | 20 | ✅ Functions are modular and well-named<br>✅ Code has helpful comments<br>✅ No redundant/duplicate code<br>✅ Variables have clear names | ⬜ |
| **👤 User Experience** | 10 | ✅ Clear instructions for players<br>✅ Board displays cleanly after each move<br>✅ Friendly error messages<br>✅ Winner announcement is clear | ⬜ |
| **🐛 Error Handling** | 10 | ✅ No crashes on invalid input<br>✅ Handles string input gracefully<br>✅ Edge cases covered (full board, first move) | ⬜ |

### 📈 Scoring Guide:

- **90-100 Points**: 🏆 **Excellent** - Production ready! Could ship to users
- **80-89 Points**: ⭐ **Great** - Solid work, minor improvements possible
- **70-79 Points**: 👍 **Good** - Core functionality works, needs refinement
- **60-69 Points**: 🔧 **Acceptable** - Basic features work, significant improvements needed
- **< 60 Points**: 📚 **Needs Work** - Review Week 1 fundamentals

---

## 🚀 Extension Challenges

Ready to level up? Try these enhancements to make your projects even better!

### 🥈 Silver Level: Enhance Existing Projects

#### Tic-Tac-Toe Enhancements
1. **Score Tracking System** ⭐⭐
   - Track wins for X and O across multiple games
   - Display statistics after each game
   - Save high scores to a file
   
2. **Larger Board** ⭐⭐
   - Make board size configurable (4x4, 5x5)
   - Adjust win condition (4 in a row for 4x4, etc.)
   
3. **Better UI** ⭐
   - Clear screen between moves
   - Add colors using ANSI codes
   - Show move history
   
4. **Replay System** ⭐
   - Ask "Play again?" at end
   - Reset board without restarting program

#### Hangman Enhancements
1. **Word Categories** ⭐⭐
   - Animals, Countries, Technology, Food
   - Let player choose category
   - Different difficulty per category
   
2. **Hint System** ⭐⭐
   - Player can request 1 hint per game
   - Reveal random letter or word definition
   
3. **Score System** ⭐
   - Points based on letters remaining
   - Bonus for quick wins
   - Track personal best
   
4. **Multiplayer** ⭐⭐⭐
   - Player 1 enters word
   - Player 2 guesses
   - Hide input while typing word

### 🥇 Gold Level: Build New Projects

#### 1. **Blackjack Card Game** ⭐⭐⭐
```python
# Features to implement:
- Card deck with shuffle
- Player vs Dealer
- Hit/Stand decisions
- Ace handling (1 or 11)
- Bust detection
- Winning conditions
```

#### 2. **Password Generator** ⭐
```python
# Features to implement:
- Customizable length
- Include/exclude: uppercase, lowercase, numbers, symbols
- Check password strength
- Generate multiple passwords
```

#### 3. **Todo List Application** ⭐⭐
```python
# Features to implement:
- Add/remove/complete tasks
- List all tasks
- Filter by status (pending/complete)
- Save to file (persistence)
- Priority levels
```

#### 4. **Quiz Game** ⭐⭐
```python
# Features to implement:
- Multiple choice questions
- Score tracking
- Timer for each question
- Difficulty levels
- Results summary
```

### 🏆 Platinum Level: Advanced Projects

#### 1. **Connect Four** ⭐⭐⭐⭐
```python
# Challenges:
- Vertical board (gravity mechanics)
- Check diagonal wins in any direction
- AI opponent with strategy
- Animated piece dropping
```

#### 2. **Text-Based RPG** ⭐⭐⭐⭐⭐
```python
# Systems to implement:
- Character stats (HP, attack, defense)
- Inventory system
- Combat system
- Room navigation
- Item/weapon management
- Save/load game state
```

#### 3. **Caesar Cipher Tool** ⭐⭐⭐
```python
# Features:
- Encrypt/decrypt messages
- Variable shift amount
- Brute force decoder
- Handle special characters
- File encryption
```

#### 4. **Contact Book Manager** ⭐⭐⭐
```python
# CRUD Operations:
- Create: Add new contacts
- Read: Search and display contacts
- Update: Modify existing contacts
- Delete: Remove contacts
- Save to JSON file
- Import/export contacts
```

### 💡 Learning Path Suggestion

```
Start Here → Enhance Tic-Tac-Toe (Score tracking)
    ↓
    Add Hangman categories
    ↓
    Build Password Generator (easiest new project)
    ↓
    Build Todo List (file I/O practice)
    ↓
    Build Quiz Game (data structures)
    ↓
    Build Blackjack (complex logic)
    ↓
    Build Connect Four (advanced algorithms)
    ↓
Master Level → Build Text-Based RPG
```

---

## 🧪 Testing Your Projects

Systematic testing ensures your code works in all scenarios:

### **Test Plan for Tic-Tac-Toe**

#### ✅ **Test 1: Basic Win - Row**
```
Moves: X(1,1), O(2,1), X(1,2), O(2,2), X(1,3)
Expected: "Player X wins!" (top row complete)
Status: ⬜ Pass / ⬜ Fail
```

#### ✅ **Test 2: Basic Win - Column**
```
Moves: X(1,1), O(1,2), X(2,1), O(2,2), X(3,1)
Expected: "Player X wins!" (left column complete)
Status: ⬜ Pass / ⬜ Fail
```

#### ✅ **Test 3: Basic Win - Diagonal**
```
Moves: X(1,1), O(1,2), X(2,2), O(1,3), X(3,3)
Expected: "Player X wins!" (diagonal complete)
Status: ⬜ Pass / ⬜ Fail
```

#### ✅ **Test 4: Tie Game**
```
Fill entire board with no winner
Expected: "It's a tie!"
Status: ⬜ Pass / ⬜ Fail
```

#### ⚠️ **Test 5: Invalid Input - Out of Bounds**
```
Input: "5 5"
Expected: Error message + prompt again
Status: ⬜ Pass / ⬜ Fail
```

#### ⚠️ **Test 6: Invalid Input - Non-numeric**
```
Input: "abc def"
Expected: Error message + prompt again
Status: ⬜ Pass / ⬜ Fail
```

#### ⚠️ **Test 7: Invalid Input - Occupied Cell**
```
X marks (2,2), then O tries (2,2)
Expected: "Cell occupied" + prompt again
Status: ⬜ Pass / ⬜ Fail
```

#### ⚠️ **Test 8: Invalid Input - Wrong Format**
```
Input: "1" (only one number)
Expected: Error message + prompt again
Status: ⬜ Pass / ⬜ Fail
```

### **Testing Checklist:**

- [ ] All win conditions tested (3 rows, 3 cols, 2 diagonals)
- [ ] Tie game works correctly
- [ ] All invalid inputs handled gracefully
- [ ] No crashes during entire game
- [ ] Board displays correctly after each move
- [ ] Turn alternation works properly
- [ ] Game ends at appropriate time

---

## 🎯 Code Review Checklist

Before considering your project complete, review:

### **Architecture**
- [ ] Functions have single, clear responsibilities
- [ ] No duplicate code (DRY principle)
- [ ] Related logic is grouped together
- [ ] Constants are defined (not magic numbers)

### **Readability**
- [ ] Variable names are descriptive (`player_move` not `pm`)
- [ ] Functions are documented with docstrings
- [ ] Complex logic has explanatory comments
- [ ] Code follows consistent formatting

### **Functionality**
- [ ] All features work as specified
- [ ] Edge cases are handled
- [ ] No known bugs remain
- [ ] Input validation is thorough

### **User Experience**
- [ ] Instructions are clear and helpful
- [ ] Error messages guide the user
- [ ] Output is well-formatted
- [ ] Game flow feels natural

---

## 📊 Comprehensive Assessment & Portfolio

### 🎮 **Tic-Tac-Toe Project Evaluation**

Your flagship project demonstrates Python mastery across four key dimensions:

#### 🏗️ **Code Structure & Organization** (25%)
- [ ] ✅ Functions are well-defined with single, clear purposes
- [ ] 📦 Code is organized into logical modules/sections
- [ ] 🎯 Appropriate data structures chosen (lists for board, etc.)
- [ ] ♻️ DRY principle applied - no unnecessary repetition
- [ ] 🔧 Helper functions properly abstract complexity
- [ ] 📊 Clear separation of concerns (display, logic, validation)

#### ⚙️ **Functionality & Correctness** (25%)
- [ ] 🚀 Game runs without crashes or errors
- [ ] ✅ All game rules implemented correctly
- [ ] 🎯 Input validation catches all invalid moves
- [ ] 🏆 Win conditions detect all 8 possible winning patterns
- [ ] 🤝 Draw conditions recognized when board fills
- [ ] 🔄 Game loop handles turn alternation properly
- [ ] 📍 Coordinate system works accurately (1-3 range)

#### 🎨 **User Experience Design** (25%)
- [ ] 📖 Clear, welcoming instructions at game start
- [ ] 🎨 Board display is clean and easy to read
- [ ] 💬 Prompts are intuitive with examples
- [ ] ⚠️ Error messages are helpful and specific
- [ ] 🎯 Game flow feels natural and engaging
- [ ] 😊 Friendly messages with emojis enhance experience
- [ ] 🔄 Retry logic gracefully handles errors

#### 📖 **Documentation & Code Quality** (25%)
- [ ] 💬 Code includes helpful inline comments
- [ ] 📝 Functions have clear, informative docstrings
- [ ] 📄 README explains project and how to run
- [ ] 🎨 Code follows PEP 8 style guidelines
- [ ] 📏 Consistent naming conventions throughout
- [ ] 🔍 Variable names are descriptive and clear
- [ ] ✨ Code is readable and maintainable

### 🎪 **Hangman Project Evaluation**
- [ ] 🎮 Complete game loop with win/lose detection
- [ ] 🎨 ASCII art displays correctly
- [ ] 📚 Word selection system functional
- [ ] ✏️ Letter tracking accurate
- [ ] 🔧 Modular structure with separate files
- [ ] 📊 Score tracking and replay functionality

### 💪 **Challenge Sets Completion**
- [ ] 🥉 Complete Challenges Set 1 exercises
- [ ] 🥈 Complete Challenges Set 2 advanced problems
- [ ] 💪 Attempt daily challenge problems
- [ ] 🚀 Solve advanced algorithm challenges
- [ ] 📝 Document problem-solving approaches
- [ ] 🧠 Explain algorithmic thinking process

### 🏆 **Overall Week 1 Mastery**
- [ ] ✅ All Day 1-4 exercises completed
- [ ] 🎮 Tic-Tac-Toe fully functional
- [ ] 🎪 Hangman or alternative project completed
- [ ] 💡 Multiple challenges solved
- [ ] 🧠 Can explain code decisions and trade-offs
- [ ] 📚 Ready to advance to Week 2 (OOP)

## 🔧 Development Process

### 1. 📋 Planning Phase
- **Understand requirements**: Read project specifications carefully
- **Break down the problem**: Identify major components and functions needed
- **Design data structures**: Plan how to represent game state
- **Sketch the flow**: Outline the main game loop and user interactions

### 2. 🏗️ Implementation Phase
- **Start small**: Build basic functionality first
- **Test frequently**: Run your code after each major addition
- **Refactor regularly**: Improve code organization as you go
- **Document as you code**: Add comments and docstrings

### 3. 🧪 Testing Phase
- **Test edge cases**: Try invalid inputs and unusual scenarios
- **Verify game rules**: Ensure all winning conditions work
- **Get feedback**: Have someone else try your game
- **Polish the experience**: Improve user interface and messages

## 🛠️ Technical Requirements

### 🐍 Python Features to Demonstrate
- **Variables & Data Types**: Effective use of strings, integers, booleans
- **Control Flow**: Conditional statements and loops
- **Data Structures**: Lists for board state, dictionaries for player data
- **Functions**: Modular code with clear function responsibilities
- **Input/Output**: User interaction and display formatting

### 📋 Code Quality Standards
- **Naming**: Use descriptive variable and function names
- **Structure**: Organize code into logical functions
- **Comments**: Explain complex logic and function purposes
- **Error Handling**: Validate user input and handle edge cases

## 🔧 Troubleshooting Guide

### Common Project Issues
| Problem | Solution |
|---------|----------|
| Logic errors in game rules | Step through code manually with test cases |
| Input validation failing | Test with various input types and edge cases |
| Code becoming too complex | Break large functions into smaller ones |
| Hard to track game state | Use clear variable names and add debug prints |

### 💡 Success Strategies
- **🐌 Start simple**: Get basic version working first
- **🔍 Debug systematically**: Use print statements to track values
- **📚 Reference previous days**: Apply patterns from earlier exercises  
- **🤝 Ask for help**: Don't hesitate to seek guidance when stuck

---

## 📊 Assessment Checklist

Verify your Week 1 mastery before moving forward:

### 🥉 Essential (Required)
- [ ] Complete Tic-Tac-Toe game with working win detection
- [ ] Implement input validation in all projects
- [ ] Use functions to organize code logically
- [ ] Apply loops for game flow and repetition
- [ ] Successfully integrate concepts from Days 1-4

### 🥈 Intermediate (Recommended)
- [ ] Complete Hangman game with ASCII art
- [ ] Solve at least 3 challenges from Challenges1 or Challenges2
- [ ] Implement replay functionality in games
- [ ] Add error handling for edge cases
- [ ] Write clear docstrings for all functions
- [ ] Organize code into logical modules

### 🥇 Advanced (Optional)
- [ ] Complete Advanced Algorithm challenges
- [ ] Optimize code for performance
- [ ] Add advanced features (scoring, difficulty levels)
- [ ] Implement AI opponent for Tic-Tac-Toe
- [ ] Create comprehensive test cases
- [ ] Build additional projects beyond requirements

### 💪 Week 1 Mastery (Bonus)
- [ ] Complete ALL exercises from Days 1-5 (XP + Gold + Ninja)
- [ ] Solve all Daily Challenges
- [ ] Build a custom project combining all concepts
- [ ] Refactor code with advanced Python patterns
- [ ] Create a portfolio presentation of your work

---

## 🎓 Portfolio Presentation

### 📝 What to Include
- **Project demo**: Show your game in action
- **Code walkthrough**: Explain key functions and design decisions
- **Challenges faced**: Discuss problems you solved
- **Lessons learned**: Reflect on your development process

### 🌟 Showcase Your Growth
- Compare your Day 5 code to Day 1 exercises
- Highlight sophisticated techniques you've learned
- Demonstrate problem-solving and debugging skills
- Show pride in your accomplishments!

## 🔗 Next Steps

After completing Week 1:
- **📊 Reflect**: What concepts feel solid? What needs more practice?
- **🚀 Prepare**: Get ready for Week 2 (Object-Oriented Programming)
- **💼 Portfolio**: Add your projects to a personal coding portfolio
- **🔄 Practice**: Continue coding to reinforce your skills

## 📚 Additional Resources

- [🎮 Game Development with Python](https://realpython.com/pygame-a-primer/)
- [📋 Project Planning Guide](https://realpython.com/python-project-structure/)
- [🧪 Testing Your Code](https://realpython.com/python-testing/)

---

## � License

This day’s exercises and notes are distributed under the repository’s [MIT License](../../LICENSE).

---

## �🐛 Common Errors & Solutions

### Error 1: Infinite game loops
**What it means**: Game never ends due to incorrect loop condition

**Example**:
```python
❌ while True:
       # Game logic
       if someone_won():
           print("Winner!")
           # Forgot to break!

✅ game_over = False
   while not game_over:
       # Game logic
       if someone_won() or board_full():
           game_over = True  # Exit loop
```

### Error 2: Not validating user input in games
**What it means**: Assuming user always enters valid data

**Example**:
```python
❌ row, col = input("Enter row col: ").split()
   row = int(row)  # ValueError if user enters text!

✅ try:
       row, col = input("Enter row col: ").split()
       row, col = int(row), int(col)
       if not (1 <= row <= 3 and 1 <= col <= 3):
           print("Must be 1-3!")
   except ValueError:
       print("Enter two numbers separated by space!")
```

### Error 3: Modifying game state incorrectly
**What it means**: Not checking if move is valid before applying

**Example**:
```python
❌ def make_move(board, row, col, player):
       board[row][col] = player  # Overwrites existing moves!

✅ def make_move(board, row, col, player):
       if board[row][col] == " ":  # Check if empty
           board[row][col] = player
           return True
       print("Cell already taken!")
       return False
```

### Error 4: Not handling edge cases in win detection
**What it means**: Missing diagonal checks or off-by-one errors

**Example**:
```python
❌ # Missing diagonal check
   def check_winner(board):
       # Only checks rows and columns
       for i in range(3):
           if all(board[i]):  # Incomplete logic
               return True

✅ def check_winner(board, player):
       # Check rows
       for row in board:
           if all(cell == player for cell in row):
               return True
       # Check columns
       for col in range(3):
           if all(board[row][col] == player for row in range(3)):
               return True
       # Check diagonals
       if all(board[i][i] == player for i in range(3)):
           return True
       if all(board[i][2-i] == player for i in range(3)):
           return True
       return False
```

### Error 5: File handling errors in Hangman
**What it means**: Not handling missing or empty word files

**Example**:
```python
❌ def load_words():
       with open("words.txt") as f:
           return f.read().split()  # FileNotFoundError if missing!

✅ def load_words():
       try:
           with open("words.txt") as f:
               words = [w.strip() for w in f if w.strip()]
               if not words:
                   print("Word file is empty!")
                   return ["python", "developer"]  # Fallback
               return words
       except FileNotFoundError:
           print("words.txt not found, using defaults")
           return ["python", "developer", "function"]
```

### Error 6: Not resetting game state between rounds
**What it means**: Previous game data carries over to new game

**Example**:
```python
❌ guessed_letters = []  # Global variable
   
   def play_game():
       # Uses same guessed_letters from last game!
       
✅ def play_game():
       guessed_letters = []  # Fresh state each game
       # Rest of game logic
       
✅ # Or reset explicitly
   def reset_game():
       global guessed_letters
       guessed_letters = []
```

### Error 7: String comparison case sensitivity
**What it means**: Not handling uppercase/lowercase input consistently

**Example**:
```python
❌ word = "PYTHON"
   guess = input("Guess a letter: ")  # User types "p"
   if guess in word:  # False! "p" != "P"

✅ word = "PYTHON"
   guess = input("Guess a letter: ").upper()
   if guess in word:  # Now works!

✅ # Or normalize everything
   word = "python".lower()
   guess = input("Guess: ").lower()
```

### Error 8: Not tracking game statistics properly
**What it means**: Counters or scores not updating correctly

**Example**:
```python
❌ def update_score(score):
       score += 10  # Only modifies local copy!
       
   player_score = 0
   update_score(player_score)
   # player_score still 0!

✅ def update_score(score):
       return score + 10
   
   player_score = update_score(player_score)

✅ # Or use mutable object
   stats = {"score": 0, "wins": 0}
   def update_score(stats):
       stats["score"] += 10  # Modifies original dict
```

---

## 👤 Author

**Kevin Cusnir 'Lirioth'**  
Repository: [Fullstack2026](https://github.com/Lirioth/Fullstack2026)  
Week 1 Day 5 - Mini Project

---

**⏱️ Estimated Time**: 6-8 hours  
**🎯 Difficulty**: Intermediate to Advanced  
**📋 Prerequisites**: Days 1-4 completion  

Time to build something amazing! You've got all the tools you need. 🚀