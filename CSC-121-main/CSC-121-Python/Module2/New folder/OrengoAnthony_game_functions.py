 # The rockPaperScissors function receives numbers representing the
# computer and player's choices.
# It returns 0 if there is a tie, 1 if the computer won, 2 if the 
# player won, or 3 if the player made an invalid choice.
# Global constants
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3
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
