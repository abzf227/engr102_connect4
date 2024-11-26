#as an aggie...

def create_board():  # create a board (technically unneeded, but it makes the code look neater)
    return [[".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."]]


def print_board(board):  # define how to print the board
    print(" _1__2__3__4__5__6__7_")
    for i in range(len(board)):
        print("|", end="")
        for j in range(len(board[i])):
            print("", board[i][j], end=" ")
        print("|")
    print("-----------------------\n//                   \\\\")


def update_board(board, col, icon):
    col = int(col) - 1
    row = 0
    while row < len(board):
        if (board[row][col] != '.'):
            break
        else:
            row += 1
    board[row - 1][col] = icon
    return board


def valid_input(board, col):
    try:
        col = int(col)
    except ValueError:
        return False
    else:
        if 0 < col < 8:
            return board[0][col - 1] == "."
        return False


def check_for_win(board):
    rows = len(board)
    cols = len(board[0])

    #helper function
    def check_line(a, b, c, d):
        return a == b == c == d and a != "."

    #horizontal
    for r in range(rows):
        for c in range(cols - 3):
            if check_line(board[r][c], board[r][c + 1], board[r][c + 2], board[r][c + 3]):
                return True

    #vertical
    for r in range(rows - 3):
        for c in range(cols):
            if check_line(board[r][c], board[r + 1][c], board[r + 2][c], board[r + 3][c]):
                return True

    #diagonals
    for r in range(rows - 3):
        for c in range(cols - 3):
            if check_line(board[r][c], board[r + 1][c + 1], board[r + 2][c + 2], board[r + 3][c + 3]):
                return True

    for r in range(3, rows):
        for c in range(cols - 3):
            if check_line(board[r][c], board[r - 1][c + 1], board[r - 2][c + 2], board[r - 3][c + 3]):
                return True

    return False  # no winner yet


#main:
print(" _____                     _      ___\n|     |___ ___ ___ ___ ___| |_   | | |\n|   --| . |   |   | -_|  _|  _|  |_  |\n|_____|___|_|_|_|_|___|___|_|      |_|\nBy Andrew Feng, Jacob Jones, Mason Kielinski, Daniel Wisa\nASCII Art credit to patorjk.com\n")
input("Enter anything to start... ")


icon_1 = "\u25CF"
icon_2 = "\u25CE"
p1_wins = 0
p2_wins = 0
game_running = True
while game_running:
    board = create_board()

    game_end = False
    current_turn = 1
    current_player = None
    while not game_end:
        if current_turn % 2 != 0:
            current_player = icon_1
        else:
            current_player = icon_2
        print(f"Player 1: {icon_1}    ||    Player 2: {icon_2} \nCurrent turn: {current_turn}\n")
        print_board(board)
        print(f"It's Player {(current_turn + 1) % 2 + 1}'s {current_player} turn...")
        col = input("Please enter a column from 1-7: ")
        while not valid_input(board, col):
            col = input("Invalid input! Please try again: ")
        board = update_board(board, col, current_player)
        if check_for_win(board):
            print_board(board)
            print(f"Player {(current_turn + 1) % 2 + 1} {current_player} has won on turn {current_turn}!")
            if current_turn % 2 == 1:
                p1_wins += 1
            else:
                p2_wins += 1
            print(f"Current Record: {icon_1} {p1_wins} - {p2_wins} {icon_2}")
            game_end = True
            print("--------------------------------")
        else:
            print("--------------------------------")
            current_turn += 1
    rematch = input("Rematch? (y/n): ")
    while rematch.lower() != "y" and rematch.lower() != "n":
        rematch = input("Invalid input! Rematch or no? (y/n): ")
    if rematch == "n":
        print(f"Final Record: {icon_1} {p1_wins} - {p2_wins} {icon_2}\nThanks for playing!!")
        game_running = False
