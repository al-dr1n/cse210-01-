"""
Overview: Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three x's or three o's drawn in the spaces of a grid of nine squares.
Rules: Tic-Tac-Toe is played according to the following rules.
    1. The game is played on a grid that is three squares by three squares.
    2. Player one uses x's. Player two uses o's.
    3. Players take turns putting their marks in empty squares.
    4. The first player to get three of their marks in a row (vertically, horizontally, or diagonally) is the winner.
    5. If all nine squares are full and neither player has three in a row, the game ends in a draw.

"""



# global variables
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"] 
in_game = True
winner = None
current_player = "x"


def main():
    # show playing board
    print()
    display_board()

    while in_game:
        # show who is playing
        turns(current_player)
        # check if game ended
        game_end()
        # assign who is next to play
        other_player()
        # show playing board
        display_board()
    # show who wins the game
    if winner == "x" or winner == "o":
        print()
        print(winner.upper() + " wins!""\n""Good game. Thanks for playing!")
        print()
    elif winner == None:
        print()
        print("It is a draw.")
        print()

# show playing board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

    return board

# show who is playing
def turns(player):
    print()
    print(player + "'s turn to play")
    user = input("select number from 1 to 9: ")
    print()

    valid = False
    while not valid:
        # check if the input is valid
        while user not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            user = input("select number from 1 to 9: ")
            print()
        
        user = int(user) - 1
        # check if input is available
        if board[user] == "-":
            valid = True
        else:
            print("Not allowed, try again!")

    board[user] = player
    
    return turns

# check if the game ended
def game_end():
    game_win()
    game_tie()
    return

# check who wins
def game_win():
    global winner
    
    row_winner = win_row()
    column_winner = win_column()
    diagonal_winner = win_diagonal()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return

# check rows
def win_row():
    global in_game

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        in_game = False
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    
    return

# check columns
def win_column():
    global in_game

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        in_game = False
    
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

    return

# check diagonals
def win_diagonal():
    global in_game

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        in_game = False
    
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return

# check if no winner
def game_tie():
    global in_game

    if "-" not in board:
        in_game = False

    return

# assign who is next to play
def other_player():
    global current_player

    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"

    return


if __name__ == "__main__":
    main()



