#Import python support file


import random
import OrengoAnthony_game_functions as gameFunctions

# This program is a version of the "Rock", "Paper", "Scissors" game, using the python
#console. The user will have the option to play a 1, 2, or 3 round game. The winner will
#be display to the user upon completion of the game. 
# Date 05/31/2021
# CSC121- M2Lab Code Modularizing
# Anthony Orengo
 
#Pseudocode
#1. Import game functions file "OrengoAnthony_game_functions".
#2. Define main function and create an active menu for the user.
#3. Declare and initialize input and loop sentinel.
#4. Create a while loop to control main menu flow.
#5: Add 4 options to the menu (1 round, 2 round, 3 round,Exit)
#6: Add the game function to the appropriate menu choice(Ex: gameFunctions.gameOne() will go with menu choice 1)
#7: ****Refer to OrengoAnthony_game_functions for additional information.
#8: End the program/loop by changing loop variable to true.  

# main function

def main():
    choice = ""
    menu_Loop = False
    game_loop = False
    result = gameFunctions.TIE
    while menu_Loop == False:
         game_loop = False
    #Display Menu Options---------------------------------------------------- 
         print(
        "Rock, Paper, Scissors  \n"+
        "--------------------------------\n"+
        "1. Game\n" +
        "2. Exit\n"+ 
        "***********************")
         # Get input from user
         choice = input("\nChoose from the Menu --> ")
         if choice == "1":
            while game_loop == False:
            # Get computer number
                computer = random.randint(1, 3)

            # Get player number
                player = input('Enter:\n'
                           '1 for rock\n' \
                           '2 for paper\n'
                           '3 for scissors -->  ')
                #Determine if input is a digit
                if player.isdigit():              
                    player = int(player)
                    #Diplay choices to user
                    print ('Computer chose:', gameFunctions.choiceString(computer))
                    print ('You chose:', gameFunctions.choiceString(player))
                    #Determine the winner of the round
                    result = gameFunctions.rockPaperScissors(computer, player)
        
                    if result == gameFunctions.TIE:
                        print('\nYou made the same choice as ' \
                      'the computer. Starting over')

                    elif (result == gameFunctions.COMPUTER_WINS):
                        print ('\nThe computer wins the game')
                        print("Do you wish to play again? ")
                        choice = input("1. Yes\n"+
                                       "2. No\n"+
                                       "--> ")
                        if choice == '1':
                             game_loop = False
                        elif choice == '2':
                             game_loop = True
                        else:
                            print("Invalid Option!")
                            game_loop = True
                    elif result == gameFunctions.PLAYER_WINS:
                        print ('\nYou win the game')
                        print("Do you wish to play again? ")
                        choice = input("1. Yes\n" +
                                       "2. No\n"+
                                       "--> ")
                        if choice == '1':
                            game_loop = False
                        elif choice == '2':
                            game_loop = True
                        else:
                            print("Invalid Option!")
                            game_loop = True
                else:
                     print ('\nYou made an invalid choice. No winner')
         
         elif choice == "2":
         #Exits program
             menu_Loop = True
         else:
             print("Invalid option! Try Again!")
 
# Call the main function.

    
if __name__ == "__main__":
    
    main()





    


