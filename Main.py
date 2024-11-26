#as an aggie...

from playsound import playsound


def give_rules():
    print("--------------------------------")
    print(">>>> RULES <<<<")
    print("\nAlright, it's simple: each turn, a player makes one move: select a column and your \"chip\" "
          "will\nfall to the bottom of that column.\n\nIn order to win, you need to connect four of your OWN "
          "pieces together (whether it be in a line\nor a diagonal) while simultaneously making sure your "
          "opponent doesn't get there first!\n\nThat's basically the entire gist of it. If you ever need help, "
          "simply enter \"0\" when it's your turn.")
    input("\nOnce you're ready, press anything to continue... ")
    print("Good luck!")


def give_credits():
    print("--------------------------------")
    print(">>> CREDITS <<<<")
    print("Connect 4 was developed for ENGR 102's Team Lab 13 by Team 3 consisting of:\n*Andrew Feng\n*Jacob "
          "Jones\n*Mason Kielinski\n*Daniel Wisa\n\nLast updated 4:19 AM CST on November 26th, 2024.")
    input("\nPress anything to continue... ")


def open_menu():
    allowed_inputs = ["h", "r", "c", "x", "z"]
    yes_no_allow = ["y", "n"]
    while True:
        print("--------------------------------")
        print(
            ">>>> MAIN MENU <<<<\n\n*Rules [H]\n*Surrender [R]\n*Credits [C]\n*End Game Session [X]\n*Close Game Menu "
            "[Z]\n")
        next_input = input("What would you like to do? ").lower()
        while next_input not in allowed_inputs:
            next_input = input("Invalid input! What would you like to do? ").lower()
        if next_input == "h":
            give_rules()
            continue
        elif next_input == "r":
            next_input = input("Are you sure? Doing so will automatically forfeit this game (y/n): ")
            while next_input not in yes_no_allow:
                next_input = input("Invalid input! Would you like to surrender this game? (y/n): ")
            if next_input == "y":
                print("--------------------------------")
                return "surrender"
            else:
                continue
        elif next_input == "c":
            give_credits()
            continue
        elif next_input == "x":
            next_input = input(
                "Are you sure? Doing so will automatically end this game session for BOTH players (y/n): ")
            while next_input not in yes_no_allow:
                next_input = input("Invalid input! Would you like to end this game session? (y/n): ")
            if next_input == "y":
                print("--------------------------------")
                return "end session"
        else:
            print("--------------------------------")
            return "close menu"


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
        if board[row][col] != '.':
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
print(" _____                     _      ___\n|     |___ ___ ___ ___ ___| |_   | | |\n|   --| . |   |   | -_|  _|  _|  "
      "|_  |\n|_____|___|_|_|_|_|___|___|_|      |_|\n>>>> Connect 4 <<<<\nBy Team 3 - Andrew Feng, Jacob Jones, Mason Kielinski, "
      "Daniel Wisa\n(Title ASCII Art credit to patorjk.com)\n")
input("Enter anything to start... ")

print("--------------------------------")
ip = input("Welcome to Connect 4! Do you need to learn the rules? (y/n) ")
while ip.lower() != "y" and ip.lower() != "n":
    ip = input("Invalid input! Do you need to learn the rules? (y/n) ")
if ip.lower() == "y":
    give_rules()
else:
    print("Good luck!")
print("--------------------------------")

icons = {
    1: "\u25CF",
    2: "\u25CE"
}

p1_wins = 0
p2_wins = 0
game_running = True
while game_running:
    board = create_board()
    game_end = False
    current_turn = 1
    while not game_end:
        print(f"Player 1: {icons[1]}    ||    Player 2: {icons[2]} \nCurrent turn: {current_turn}\n")
        print_board(board)
        if current_turn > 1:
            playsound("connect4_sound.mp3")
        print(f"It's Player {(current_turn + 1) % 2 + 1}'s {icons[(current_turn + 1) % 2 + 1]} turn...")
        col = input("Please enter a column from 1-7 (or press 0 for more options): ")

        while not valid_input(board, col):
            if int(col) == 0:
                menu_action = open_menu()  # Store the result of open_menu()
                if menu_action == "surrender":
                    print_board(board)
                    print(
                        f"Player {current_turn % 2 + 1} {icons[current_turn % 2 + 1]} has surrendered to Player {(current_turn + 1) % 2 + 1} {icons[(current_turn + 1) % 2 + 1]} has won on turn {current_turn}!")
                    if current_turn % 2 == 1:
                        p1_wins += 1
                    else:
                        p2_wins += 1
                    print(f"Current Record: {icons[1]} {p1_wins} - {p2_wins} {icons[2]}")
                    game_end = True
                    print("--------------------------------")
                    break
                elif menu_action == "end session":
                    print(f"Final Record: {icons[1]} {p1_wins} - {p2_wins} {icons[2]}\nThanks for playing!!")
                    game_running = False
                    break
                elif menu_action == "close menu":
                    print_board(board)
                    col = input("Please enter a column from 1-7 (or press 0 for more options): ")
                    continue  # Exit the menu and continue to prompt for input
            col = input("Invalid input! Please try again: ")

        if game_end or not game_running:
            break

        board = update_board(board, col, icons[(current_turn + 1) % 2 + 1])
        if check_for_win(board):
            print_board(board)
            print(
                f"Connect 4! Player {(current_turn + 1) % 2 + 1} {icons[(current_turn + 1) % 2 + 1]} has won on turn {current_turn}!")
            if current_turn % 2 == 1:
                p1_wins += 1
            else:
                p2_wins += 1
            print(f"Current Record: {icons[1]} {p1_wins} - {p2_wins} {icons[2]}")
            game_end = True
            print("--------------------------------")
        else:
            print("--------------------------------")
            current_turn += 1

    rematch = input("Rematch? (y/n): ")
    while rematch.lower() != "y" and rematch.lower() != "n":
        rematch = input("Invalid input! Rematch or no? (y/n): ")
    if rematch == "n":
        print(f"Final Record: {icons[1]} {p1_wins} - {p2_wins} {icons[2]}\nThanks for playing!!")
        game_running = False
