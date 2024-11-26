#as an aggie...

from playsound import playsound
#pip install playsound==1.2.2
#if 'playsound' is already installed consider uninstalling it first as bugs have been known to arise
#this is **REQUIRED** for the program


def give_rules():
    """Informational function that provides rules.

    :param: none
    :return: none
    """

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
    """Informational function that provides credits.

    :param: none
    :return: none
    """

    print("--------------------------------")
    print(">>> CREDITS <<<<")
    print("Connect 4 was developed for ENGR 102's Team Lab 13 by Team 3 consisting of:\n*Andrew Feng\n*Jacob "
          "Jones\n*Mason Kielinski\n*Daniel Wisa\n\nLast updated 4:19 AM CST on November 26th, 2024.")
    input("\nPress anything to continue... ")


def open_menu():
    """Opens the main menu which provides multiple different options for the current player.

    :param: none
    :return: a string that differs based on user input, which can cause the game to end, quit, or continue
    """

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


def create_board():
    """Create an empty board (unneeded, but it makes the main code look neater)

    :param: none
    :return: empty 6x7 board (2D list) of periods
    """

    return [[".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", "."]]


def print_board(board):
    """Prints the formatted and visually enhanced board with a heading and little legs.

    :param board: 2D list of the current in-game board
    :return: none
    """
    print(" _1__2__3__4__5__6__7_")
    for i in range(len(board)):
        print("|", end="")
        for j in range(len(board[i])):
            print("", board[i][j], end=" ")
        print("|")
    print("-----------------------\n//                   \\\\")


def update_board(board, col, icon):
    """Updates the current in-game board after a new turn; plays a small SFX as well.

    :param board: 2D list of current in-game board
    :param col: column to place new icon
    :param icon: current player's icon
    :return: updated 2D list of new in-game board
    """
    col = int(col) - 1
    row = 0
    while row < len(board):
        if board[row][col] != '.':
            break
        else:
            row += 1
    board[row - 1][col] = icon
    playsound("connect4_sound.mp3")
    return board


def valid_input(board, col):
    """Checks input for validity.

    :param board: 2D list of current in-game board
    :param col: Column player is attempting to add to
    :return: True if input is valid and False if not
    """
    try:
        col = int(col)
    except ValueError:
        return False
    else:
        if 0 < col < 8:
            return board[0][col - 1] == "."
        return False


def check_for_win(board):
    """Checks board for a win.

    :param board: 2D list of current in-game board
    :return: True if Connect 4 (horizontal, vertical, diagonal) is reached and False if not
    """
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


def check_for_tie(board):
    """Comes after check_for_win(board) that checks if all places have been filled.

    :param board: 2D list of current in-game board
    :return: True if board is full and False if not
    """

    return not "." in board[0]


#main:
log_text = open("log.txt", 'w')
print(" _____                     _      ___\n|     |___ ___ ___ ___ ___| |_   | | |\n|   --| . |   |   | -_|  _|  _|  "
      "|_  |\n|_____|___|_|_|_|_|___|___|_|      |_|\n>>>> Connect 4 <<<<\nBy Team 3 - Andrew Feng, Jacob Jones, "
      "Mason Kielinski,"
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
current_game = 1
game_running = True
early_end = False
while game_running:
    log_text.write(f"====GAME {current_game}====\n")
    board = create_board()
    game_end = False
    current_turn = 1
    while not game_end:
        print(f"Player 1: {icons[1]}    ||    Player 2: {icons[2]} \nCurrent game: {current_game}\nCurrent turn: {current_turn}\n")
        print_board(board)
        print(f"It's Player {(current_turn + 1) % 2 + 1}'s {icons[(current_turn + 1) % 2 + 1]} turn...")
        col = input("Please enter a column from 1-7 (or press 0 for more options): ")

        while not valid_input(board, col):
            if int(col) == 0:
                menu_action = open_menu()  # Store the result of open_menu()
                if menu_action == "surrender":
                    print_board(board)
                    log_text.write(
                        f"Player {(current_turn+1) % 2 + 1} has surrendered to Player {current_turn % 2 + 1} on turn {current_turn}!\n")
                    log_text.flush()
                    print(
                        f"Player {(current_turn+1) % 2 + 1} {icons[(current_turn+1) % 2 + 1]} has surrendered to Player {current_turn % 2 + 1} {icons[current_turn % 2 + 1]} has won on turn {current_turn}!")
                    if current_turn % 2 == 1:
                        p1_wins += 1
                    else:
                        p2_wins += 1
                    print(f"Current Record: {icons[1]} {p1_wins} - {p2_wins} {icons[2]}")
                    log_text.write(f"Current Record: Player 1 ({p1_wins}) - ({p2_wins}) Player 2\n")
                    log_text.flush()
                    game_end = True
                    print("--------------------------------")
                    break
                elif menu_action == "end session":
                    print(f"Game ended!\nFinal Record: {icons[1]} {p1_wins} - {p2_wins} {icons[2]}\nThanks for playing!!")
                    print("--------------------------------")
                    game_running = False
                    early_end = True
                    log_text.write(f"Player {(current_turn+1) % 2 + 1} ended the session.\nFinal Record: Player 1 ({p1_wins}) - ({p2_wins}) Player 2\n====END LOG====")
                    log_text.close()
                    break
                elif menu_action == "close menu":
                    print_board(board)
                    col = input("Please enter a column from 1-7 (or press 0 for more options): ")
                    continue  # Exit the menu and continue to prompt for input
            col = input("Invalid input! Please try again: ")

        if game_end or not game_running:
            break

        board = update_board(board, col, icons[(current_turn + 1) % 2 + 1])
        log_text.write(f'Player {(current_turn + 1) % 2 + 1} placed chip in column {col}\n')
        log_text.flush()
        if check_for_win(board):
            print_board(board)
            print(
                f"Connect 4! Player {(current_turn + 1) % 2 + 1} {icons[(current_turn + 1) % 2 + 1]} has won on turn {current_turn}!")
            log_text.write(f"Connect 4! Player {(current_turn + 1) % 2 + 1} has won on turn {current_turn}!\n")
            log_text.flush()
            if current_turn % 2 == 1:
                p1_wins += 1
            else:
                p2_wins += 1
            print(f"Current Record: {icons[1]} {p1_wins} - {p2_wins} {icons[2]}")
            log_text.write(f"Current Record: Player 1 ({p1_wins}) - ({p2_wins}) Player 2\n")
            log_text.flush()
            game_end = True
            print("--------------------------------")
        elif check_for_tie(board):
            print_board(board)
            print("It's a tie! Board is full with no win for either player.")
            log_text.write("Players have tied! Board is full with no win for either player.")
            p1_wins += 0.5
            p2_wins += 0.5
            print(f"Current Record: {icons[1]} {p1_wins} - {p2_wins} {icons[2]}")
            log_text.write(f"Current Record: Player 1 {p1_wins} - Player 2 {p2_wins}\n")
            log_text.flush()
            game_end = True
            print("--------------------------------")
        else:
            print("--------------------------------")
            current_turn += 1

    if not early_end:
        rematch = input("Rematch? (y/n): ")
        while rematch.lower() != "y" and rematch.lower() != "n":
            rematch = input("Invalid input! Rematch or no? (y/n): ")
        if rematch == "n":
            print("--------------------------------")
            log_text.write(f"====GAME HAS ENDED====\nFinal Record: Player 1 ({p1_wins}) - ({p2_wins}) Player 2\n====END LOG====")
            print(f"Game Over!\nFinal Record: {icons[1]} {p1_wins} - {p2_wins} {icons[2]}\nThanks for playing!!")
            print("--------------------------------")
            game_running = False
            log_text.close()
        else:
            current_game += 1

