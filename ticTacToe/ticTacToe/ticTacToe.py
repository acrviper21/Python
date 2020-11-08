# By: Erik Sistos
# Date: 11/08/2020
# Description: This program creates a simple game of tic tac toe

#create board for game
board = [" " for i in range(9)]

# Create function to print the rows of the board
def print_board():
    row1 = "|{}|{}|{}|".format(board[0], board[1], board[2])
    row2 = "|{}|{}|{}|".format(board[3], board[4], board[5])
    row3 = "|{}|{}|{}|".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# Create funtion to handle player's move
def player_move(icon):
    if icon == "X":
        number = 1
    elif icon == "O":
        number = 2

    print(f"Your turn player {number}")
    choice = int(input("Enter your move (1-9): ").strip())

    # If player tries to place on a spot taken it has them try again for a different spot
    while board[choice - 1] == "X" or board[choice-1] == "O":
        print()
        print("That space is taken!")
        print(f"Your turn player {number}")
        choice = int(input("Enter your move (1-9): ").strip())

    # If player picks an empty spot it places their icon in it
    else:
        board[choice - 1] == " "
        board[choice - 1] = icon
        
# Create function to determine winner
def is_victory(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or \
        (board[3] == icon and board[4] == icon and board[5] == icon) or \
        (board[6] == icon and board[7] == icon and board[8] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[0] == icon and board[3] == icon and board[6] == icon) or \
        (board[1] == icon and board[4] == icon and board[7] == icon) or \
        (board[2] == icon and board[5] == icon and board[8] == icon) or \
        (board[0] == icon and board[4] == icon and board[8] == icon) or \
        (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
      
# Create function to determine if their the two players tied
def is_draw():
    if " " not in board:
        return True
    else:
        return False

# Run game
while True:
    print_board()
    player_move("X")
    print_board()
    if is_victory("X"):
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("Its a draw!")
        break
    player_move("O")
    if is_victory("O"):
        print_board()
        print("O Wins! Congratulation!")
        break
    elif is_draw():
        print("Its a draw!")
        break
    

    
