import random

board = ["_", "_", "_",
         "_", "_", "_",
         "_", "_", "_"]

current_player = "X"
winner = None
game_running = True


def print_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("------")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("------")
    print(board[6] + "|" + board[7] + "|" + board[8])


def player_input(board):
    user_input = int(input("Enter a number 1-9: "))
    if user_input >= 1 and user_input <= 9 and board[user_input - 1] == "_":
        board[user_input - 1] = current_player

    else:
        print("This spot has been occupied")


def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "_":
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] and board[3] != "_":
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6] != "_":
        winner = board[6]
        return True


def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "_":
        winner = board[0]
        return True

    elif board[1] == board[4] == board[7] and board[1] != "_":
        winner = board[1]
        return True

    elif board[2] == board[5] == board[8] and board[2] != "_":
        winner = board[2]
        return True


def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "_":
        winner = board[0]
        return True

    elif board[2] == board[4] == board[6] and board[2] != "_":
        winner = board[2]
        return True


def check_tie(board):
    global game_running
    if "_" not in board:
        print_board(board)
        print("It is a tie")
        game_running = False


def check_win():
    global game_running
    if check_horizontal(board) or check_row(board) or check_diag(board):
        print_board(board)
        print(f"The winner is {winner}")
        game_running = False


def switch():
    global current_player
    if current_player == "X":
        current_player = "O"

    else:
        current_player = "X"


def opponent(board):
    if current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "_":
            board[position] = "O"
            switch()


while game_running:
    print_board(board)
    player_input(board)
    check_win()
    check_tie(board)
    switch()
    opponent(board)
    check_tie(board)


