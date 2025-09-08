def new_board():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def display_board(b):
    print("  1 2 3")
    for i, row in enumerate(b, 1):
        print(i, "|".join(row))
        if i < 3:
            print("  -----")

def player_input(b, player):
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
    for i in range(3):
        if b[i][0] == b[i][1] == b[i][2] == p:
            return True
        if b[0][i] == b[1][i] == b[2][i] == p:
            return True
    if b[0][0] == b[1][1] == b[2][2] == p:
        return True
    if b[0][2] == b[1][1] == b[2][0] == p:
        return True
    return False

def is_tie(b):
    for row in b:
        if " " in row:
            return False
    return True

def play():
    board = new_board()
    player = "X"
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
