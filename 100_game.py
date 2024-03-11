#File: CS112_A1_T2_1_20230216.py
#Purpose: This is a two players game that takes inputs from each player by order and adds the sum till it reaches 100 or more and the player who reaches 100 wins and if it reached more than 100 it is a draw and then the user chooses to close the program or play again
#Author: Abdelrahman Mohamed Abdelgawad Mohamed
#ID: 20230216


sum=0
#                                      BEGINING OF THE PROGRAM
#menu
print("Welcome to the 100 game!!")
while True :    #while loop to make sure the user enters a valid choice
    print("Please select a choice: ")
    print("A) Start the game")
    print("B) Close the program")
    decision = input()
    if decision.upper() == 'A':
        while True :
            #First player's choice
            while True:           #while loop to make sure the user enters a valid number
                choice1=input("First player's turn: choose a number from 1 to 10:")
                if choice1.isdigit() == True and int(choice1) <= 10 and int(choice1) >= 1 and int(choice1) < 101 - sum :
                    break
                #if statement to check if the number is valid and an integer
                elif choice1.isdigit() == True and int(choice1) >= 101-sum : print("Please enter a smaller number")
                else:print("Invalid input! Please enter an integer from 1 to 10")
            sum += int(choice1)
            print("The sum is:",sum)
            if sum == 100:
                print("First player won!")
                break
            #Second player's choice
            while True:           #while loop to make sure the user enters a valid number
                choice2=input("Second player's turn: choose a number from 1 to 10:")
                if choice2.isdigit() == True and int(choice2) <= 10 and int(choice2) >= 1 and int(choice2) < 101 - sum:
                    break
                elif choice2.isdigit() == True and int(choice2) >= 101-sum : print("Please enter a smaller number")
                else:print("Invalid input!")
            sum += int(choice2)
            print("The sum is:",sum)
            if sum == 100:
                print("Second player won!")
                break   
    elif decision.upper() == 'B':   #a message to say that the user chose to close the program
        print("Closing program....")
        break
    else :    #a message if the user entered a wrong input
        print("invalid choice!")
#                                         END OF THE PROGRAM