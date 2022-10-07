import re
import DatamanLibrary as DL
import AnswerChecker as AC
import NumberGuesser as NG
import ForceOut as FO
import MissingNumber as MN

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
            
        elif choice == "3":
            FO.ForceOutGameSelection()
        elif choice == "4":
            MN.MissingNumberGameSelection()
        elif choice == "8":
            menuLoop = True
        else:
            print("Invalid Selction!")
     
Main()
exit()