import OrengoAnthony_game_functions as gameFunctions
import random
import os
 
 

# main function
def main():
    
    result = gameFunctions.TIE

    while result==gameFunctions.TIE:
        # Get computer number
        computer = random.randint(1, 3)

        # Get player number
        player = int(input('Enter:\n'
                           '1 for rock\n' \
                           '2 for paper\n'
                           '3 for scissors -->  '))

        print ('Computer chose:', gameFunctions.choiceString(computer))
        print ('You chose:', gameFunctions.choiceString(player))
        
        result = gameFunctions.rockPaperScissors(computer, player)
        
        if result == gameFunctions.TIE:
            print('\nYou made the same choice as ' \
                  'the computer. Starting over')

    if (result == gameFunctions.COMPUTER_WINS):
        print ('\nThe computer wins the game')
    elif result == gameFunctions.PLAYER_WINS:
        print ('\nYou win the game')
    else:
        print ('\nYou made an invalid choice. No winner')
    
 
# Call the main function.
clear = lambda: os.system('cls')    
if __name__ == "__main__":
    main()
    clear()


