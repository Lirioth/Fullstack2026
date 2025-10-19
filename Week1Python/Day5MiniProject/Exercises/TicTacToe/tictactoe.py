"""Module: tictactoe
Purpose: Day 5 mini-project delivering a two-player CLI tic-tac-toe game.
Author: Kevin Cusnir 'Lirioth'
Created: 2025-10-18
Last Updated: 2025-10-19

Features:
    - 3x3 board rendering with headers
    - Input validation and replay loop
    - Win and tie detection helpers
"""

from __future__ import annotations

# Tic Tac Toe (short & simple)
# Two players take turns on a 3x3 grid. First to 3 in a row wins.
# 🚀 Run: python3 tictactoe.py

def new_board() -> list[list[str]]:
    """Return a fresh 3×3 board filled with spaces."""
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def display_board(board: list[list[str]]) -> None:
    """Print the board in a friendly 3×3 grid with row/column headers."""
    print("  1 2 3")
    for i, row in enumerate(board, 1):
        print(i, "|".join(row))
        if i < 3:
            print("  -----")

def parse_move(user_input: str) -> tuple[int, int]:
    """Return zero-based row/col from raw user input or raise ValueError."""
    parts = user_input.split()
    if len(parts) != 2:
        raise ValueError("Please enter two numbers like: 2 3")
    try:
        row, col = map(int, parts)
    except ValueError as exc:
        raise ValueError("Please enter two numbers like: 2 3") from exc
    return row - 1, col - 1


def validate_move(board: list[list[str]], user_input: str) -> tuple[int, int]:
    """Validate a move string against the current board and return coordinates."""
    row, col = parse_move(user_input)
    if row not in (0, 1, 2) or col not in (0, 1, 2):
        raise ValueError("Invalid move. Try again.")
    if board[row][col] != " ":
        # ⚠️ Prevent players from overwriting an occupied square.
        raise ValueError("Invalid move. Try again.")
    return row, col


def player_input(board: list[list[str]], player: str) -> tuple[int, int]:
    """Ask user for 'row col' (1..3 1..3) until a valid empty cell is chosen."""
    while True:
        try:
            s = input(f"Player {player}, enter row and col (1-3 1-3) 🙂: ").strip()
            return validate_move(board, s)
        except ValueError as err:
            print(err)
        except IndexError:
            print("Invalid move. Try again.")

def check_win(board: list[list[str]], player: str) -> bool:
    """Return True if ``player`` has 3 in a row anywhere."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:  # rows
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:  # cols
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:  # main diag
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:  # anti diag
        return True
    return False

def is_tie(board: list[list[str]]) -> bool:
    """Return True if no spaces left (board is full)."""
    return all(cell != " " for row in board for cell in row)

def play() -> None:
    """Main game loop: alternate turns until win or tie."""
    board = new_board()
    player = "X"  # X starts
    while True:
        display_board(board)
        r, c = player_input(board, player)
        board[r][c] = player

        if check_win(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break
        if is_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        player = "O" if player == "X" else "X"


def main():
    """Main entry point with replay option."""
    print("🎮 Welcome to Tic Tac Toe! 🎮\n")
    
    while True:
        play()
        
        # ✅ IMPROVED: Added replay functionality
        replay = input("\n🔄 Play again? (y/n): ").strip().lower()
        if replay != 'y' and replay != 'yes':
            print("\n👋 Thanks for playing! Goodbye! 🎉")
            break
        print("\n" + "="*40 + "\n")


if __name__ == "__main__":
    main()
