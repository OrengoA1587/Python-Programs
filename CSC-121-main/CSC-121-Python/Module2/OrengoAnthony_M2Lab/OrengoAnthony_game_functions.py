import random

# This program is a version of the "Rock", "Paper", "Scissors" game, using the python
#console. The user will have the option to play a 1, 2, or 3 round game. The winner will
#be display to the user upon completion of the game. 
# Date 05/31/2021
# CSC121- M2Lab Code Modularizing
# Anthony Orengo


 
#Pseudocode
#1. Import Random class.
#2. Declare and initialize global constants/function variables to track score, round number, and result.
#3. Define functions mainMenu, displayInvalidMessage, gameOne, two, and three,rockPaperScissors, and choiceStrings
#4. The mainMenu function will contain a layout of the main menu using the print function. 
#5. The displayInvalidOption function will return the string .
#6. Define functions rockPaperScissors, and choiceStrings. ChoiceString will require a parameter to be passed (computers choice/players choice)
#The choice number will determine what option was chose(Ex: if player chooses 1 and 1 represents rock, "rock" will be returned from choiceString function)
#The rockPaperScissors function will determine the result of who won the round. This function will consist of two parameters (computer, player) and will
#Determine if the cpu or player won or if they tied. Nested loops will be required to accomplish this by eliminating possiblities.
#7: Depending on the game, the round will continue until either player reaches the desired score. The "score tracker" variables will need to be
#incremented along with the "roundNum" variable
#8: The winner/loser will be displayed to the user upon completion of the round(s).




 
# Global constants
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3
 

#Display Menu Options---------------------------------------------------- 
def mainMenu():
        print(
        "***********************\n"+
        "Rock, Paper, Scissors  \n"+
        "***********************\n"+
        "1. 1 Round\n" +
        "2. 2 Rounds\n"+
        "3. 3 Rounds\n"+
        "4. Exit\n"+ 
        "***********************")
#END Display Menu Options-------------------------------------------------
#Display Invalid Option---------------------------------------------------- 
def displayMessageInvalid():
  return "Invalid option! Try Again!"
#END Invalid Menu Option-------------------------------------------------
#gameOne------------------------------------------------------------------         
def gameOne():
    result = TIE
    while result==TIE:
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
                print ('Computer chose:', choiceString(computer))
                print ('You chose:', choiceString(player))
                #Determine the winner of the round
                result = rockPaperScissors(computer, player)
        
                if result == TIE:
                    print('\nYou made the same choice as ' \
                  'the computer. Starting over')

                if (result == COMPUTER_WINS):
                    print ('\nThe computer wins the game')
                elif result == PLAYER_WINS:
                    print ('\nYou win the game')
                else:
                    print ('\nYou made an invalid choice. No winner')
        else:
                print("Invalid Option!Try Again!")
#End gameOne------------------------------------------------------------------  
#gameTwo------------------------------------------------------------------         
def gameTwo():
    #Declare and initialize variables to tracke score,round number, and result
    cpuScore = 0
    playerScore = 0
    result = TIE
    roundNum = 1

    #While loop is used to run as many rounds as needed until either opponent wins.
    while cpuScore < 2 and playerScore < 2:
        # Get computer number
        computer = random.randint(1, 3)
        print("Round: ", roundNum)
        # Get player number
        player = input('Enter:\n'
                           '1 for rock\n' \
                           '2 for paper\n'
                           '3 for scissors -->  ')
         #Determine if input is a digit
        if player.isdigit():
                player = int(player)
                print ('Computer chose:', choiceString(computer))
                print ('You chose:', choiceString(player))
        
                result = rockPaperScissors(computer, player)
        
                if result == TIE:
                    print('\nYou made the same choice as ' \
                          'the computer. Starting over')
            
                if (result == COMPUTER_WINS):
                    print ('\nThe computer wins round: ' , roundNum)
                    cpuScore += 1            
                    roundNum +=1
                elif result == PLAYER_WINS:
                    print ('\nYou won round: ' , roundNum)
                    playerScore += 1
                    roundNum +=1
                else:
                    print ('\nYou made an invalid choice. No winner')
                # Determine final winner
                if playerScore >= 2 or cpuScore >= 2:
                        if playerScore > cpuScore:
                                print("You won the game! Great Job!")
                        else:                        
                                print("You Lost! The computer wins!") 
        else:
                print("Invalid Option!Try Again!")
    
#End gameTwo------------------------------------------------------------------
#gameThree------------------------------------------------------------------         
def gameThree():
    #Declare and initialize variables to tracke score,round number, and result
    cpuScore = 0
    playerScore = 0
    result = TIE
    roundNum = 1

    #While loop is used to run as many rounds as needed until either opponent wins.
    while cpuScore < 3 and playerScore < 3:
        # Get computer number
        computer = random.randint(1, 3)

        # Get player number
        player = input('Enter:\n'
                           '1 for rock\n' \
                           '2 for paper\n'
                           '3 for scissors -->  ')
        if player.isdigit():
                player = int(player)
                print ('Computer chose:', choiceString(computer))
                print ('You chose:', choiceString(player))
        
                result = rockPaperScissors(computer, player)
        
                if result == TIE:
                    print('\nYou made the same choice as ' \
                                  'the computer. Starting over')
            
                if (result == COMPUTER_WINS):
                    print ('\nThe computer wins round: ' , roundNum)
                    cpuScore += 1            
                    roundNum +=1
                elif result == PLAYER_WINS:
                    print ('\nYou won round: ' , roundNum)
                    playerScore += 1
                    roundNum +=1
                else:
                    print ('\nYou made an invalid choice. No winner')
                # Determine final winner
                if playerScore >= 3 or cpuScore >= 3:
                        if playerScore > cpuScore:
                                print("You won the game! Great Job!")
                        else:                        
                                print("You Lost! The computer wins!") 
        else:
                print("Invalid Option!Try Again!")
#End gameThree------------------------------------------------------------------    
def rockPaperScissors(computer, player):
    
    if(computer == player):
        return TIE
    
    if computer == ROCK: 
        if player == PAPER: 
            return PLAYER_WINS
        elif player == SCISSORS: 
            return COMPUTER_WINS
        else:
            return INVALID
    elif computer == PAPER: 
        if player == ROCK: 
            return COMPUTER_WINS
        elif player == SCISSORS: 
            return PLAYER_WINS
        else:
            return INVALID
    else: #computer chose scissors
        if player == ROCK: 
            return PLAYER_WINS
        elif player == PAPER: 
            return COMPUTER_WINS
        else:
            return INVALID
            
# The choiceString function displays a choice in string format
def choiceString(choice):
    if choice == ROCK:
        return 'rock'
    elif choice == PAPER:
        return 'paper'
    elif choice == SCISSORS:
        return 'scissors'
    else:
        return 'something went wrong'

if __name__ == "__main__":
    main()
