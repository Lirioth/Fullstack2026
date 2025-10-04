# Tic Tac Toe (short & simple)
# Two players take turns on a 3x3 grid. First to 3 in a row wins.
# 🚀 Run: python3 tictactoe.py

def new_board():
    """Return a fresh 3x3 board filled with spaces."""
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def display_board(b):
    """Print the board in a friendly 3x3 grid with row/col headers."""
    print("  1 2 3")
    for i, row in enumerate(b, 1):
        print(i, "|".join(row))
        if i < 3:
            print("  -----")

def player_input(b, player):
    """Ask user for 'row col' (1..3 1..3) until a valid empty cell is chosen."""
    while True:
        try:
            s = input(f"Player {player}, enter row and col (1-3 1-3): ").strip()
            r_str, c_str = s.split()
            r, c = int(r_str) - 1, int(c_str) - 1
            if r in (0,1,2) and c in (0,1,2) and b[r][c] == " ":
                return r, c
            print("Invalid move. Try again.")
        except Exception:
            print("Please enter two numbers like: 2 3")

def check_win(b, p):
    """Return True if player p has 3 in a row anywhere."""
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] == p:  # rows
            return True
        if b[0][i] == b[1][i] == b[2][i] == p:  # cols
            return True
    if b[0][0] == b[1][1] == b[2][2] == p:      # main diag
        return True
    if b[0][2] == b[1][1] == b[2][0] == p:      # anti diag
        return True
    return False

def is_tie(b):
    """Return True if no spaces left (board is full)."""
    return all(cell != " " for row in b for cell in row)

def play():
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

if __name__ == "__main__":
    play()
