#File: CS112_A1_T6_20230216
#Purpose: This is a tic tac toe game with numbers where the player who makes the addition of a line's elements equal 15 wins and if all places were taken and no one has won yet it will be a draw
#Author: Abdelrahman Mohamed Abdelgawad Mohamed
#ID: 20230216
#version:1.0
#Date: 3/1/2024



# Define player 1 and player 2 numbers
plyr1 = [1, 3, 5, 7, 9]
plyr2 = [2, 4, 6, 8]

# Function to print the tic-tac-toe board
def printBoard(board):
    print(f"[{board[0]},{board[1]},{board[2]}]\n[{board[3]},{board[4]},{board[5]}]\n[{board[6]},{board[7]},{board[8]}]")

# Function to take number input from players
def nmbrInput(turn):
    # If it's player 1's turn, prompt for an odd number, else prompt for an even number
    if turn == 1:
        while True:
            choice = input("Enter an odd number from 1 to 9: ")
            if choice.isdigit() == True and int(choice) in plyr1:
                return choice
            else:
                print("Invalid input")
    else:
        while True:
            choice = input("Enter an even number from 2 to 8: ")
            if choice.isdigit() == True and int(choice) in plyr2:
                return choice
            else:
                print("Invalid input")

# Function to place the chosen number on the board
def takeChoice(board, nmbr):
    # Prompt the player to choose a position on the board to place their number
    while True:
        choice = input("where do you want to place the number?\n1)top left    | 2)top middle    | 3)top right\n4)middle left | 5)middle        | 6)middle right\n7)bottom left | 8)bottom middle | 9)bottom right\n")
        # Check if the choice is valid and the position is empty, then place the number
        if choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and board[int(choice) - 1] == 0:
            board[int(choice) - 1] = nmbr
            break
        elif choice in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and board[int(choice) - 1] != 0:
            print("This place is already taken!")
        else:
            print("Invalid input")
    return board

# Function to check if there is a winner or a draw
def checkWin(board, player):
    # Check if any row, column, or diagonal sums up to 15, indicating a win
    if (int(board[0]) + int(board[1]) + int(board[2]) == 15 or int(board[3]) + int(board[4]) + int(board[5]) == 15 or
        int(board[6]) + int(board[7]) + int(board[8]) == 15 or int(board[0]) + int(board[3]) + int(board[6]) == 15 or
        int(board[1]) + int(board[4]) + int(board[7]) == 15 or int(board[2]) + int(board[5]) + int(board[8]) == 15 or
        int(board[0]) + int(board[4]) + int(board[8]) == 15 or int(board[2]) + int(board[4]) + int(board[6]) == 15):
        # If there's a win, print the winning player
        print(f"{player} player won!")
        return 1
    # Check if the board is full, indicating a draw
    if all(board):
        print("Draw!")
        return 1

# Main program
print("***Welcome to tic-tac-toe game***")

while True:
    # Initialize the board
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print()
    print("What do you want to do dear user?") #menu
    print("1) Start the game")
    print("2) Close the program")
    # Prompt the user for their decision
    decision = input("Please choose from above: ")
    if decision == '1':
        print()
        # Display the initial empty board
        printBoard(board)
        # Start the game loop
        while True:
            print()
            # Player 1's turn
            print("***First player's turn***")
            # Get the number input from player 1
            nmbr = nmbrInput(1)
            # Take the choice of position from player 1 and update the board
            board = takeChoice(board, nmbr)
            # Print the updated board
            printBoard(board)
            # Check if player 1 has won or if it's a draw
            if checkWin(board, "First"):
                break
            print()
            print("***Second player's turn***")
            # Get the number input from player 2
            nmbr = nmbrInput(2)
            # Take the choice of position from player 2 and update the board
            board = takeChoice(board, nmbr)
            # Print the updated board
            printBoard(board)
            # Check if player 2 has won or if it's a draw
            if checkWin(board, "Second"):
                break
    elif decision == '2': #a message to say that the user chose to close the program
        print("Closing program....")
        break
    else: #a message if the user entered a wrong input
        print("invalid choice!")
#                                         END OF THE PROGRAM