import random

number = random.randint(1, 3)


rock = "rock"
paper = "paper"
scissors = "scissors"

cRock = 1
cPaper = 2
cScissors = 3

def main():
    user_num = str(input("rock, paper, or scissors   "))
    
    
    if number == 1 and user_num == "scissors":
        print("Rock")
        print("Player 1 you lose")
        print("Player 2 you win")
    else:
        if number == 3 and user_num == "rock":
            print("Scissors")
            print("Player 1 you win")
            print("Player 2 you lose")

        else:
            if number == 1 and user_num == "paper":
                print("Rock")
                print("Player 1 you win")
                print("Player 2 you lose")
            else:
                if number == 2 and user_num == "rock":
                    print("Paper")
                    print("player 1 you lose")
                    print("Player 2 you win")

                else:

                    if number == 2 and user_num =="scissors":
                        print("Paper")
                        print("player 1 you win")
                        print("Player 2 you lose")
                    else:
                        if number == 3 and user_num == "paper":
                            print("Scissors")
                            print("player 1 you lose")
                            print("Player 2 you win")
                        else:
                            if number == 1 and user_num == "rock":
                                print("Rock")
                                print("Draw!, Rematch")
                                return main()
                            else:
                                 if number == 2 and user_num == "paper":
                                     print("Paper")
                                     print("Draw!, Rematch")
                                     return main()
                                 else:
                                     if number == 3 and user_num == "scissors":
                                         print("Scissors")
                                         print("Draw!, Rematch")
                                         return main()
main()



    
    
    
