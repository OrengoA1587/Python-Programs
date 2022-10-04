import re
import DatamanLibrary as DL
import AnswerChecker as AC
import NumberGuesser as NG
 
   
def TODO():
    print("Pending")
def Main():
    menuLoop = False

    while menuLoop == False:

        DL.MainMenu()
        choice = input("Select from the Menu --> ")

        if choice == "1":
            AC.AnswerChecker()#Start Answer Checker Game
        elif choice == "2":
            NG.GuessNumber()#Start Number Guessser Game
            TODO()
        elif choice == "3":
            TODO()
        elif choice == "4":
            TODO()
        elif choice == "8":
            menuLoop = True
        else:
            print("Invalid Selction!")
     
Main()
exit()