
import random
import DatamanLibrary as DL
 


def GuessNumber():  
     
    menuLoop = False

    while menuLoop == False:

        DL.GuessNumberMenu()
        choice = input("Select from the Menu --> ")
        if choice == "1":
            GuessTheNumber(1,10)            
        elif choice == "2":
            GuessTheNumber(1,20)
             
        elif choice == "3":
            GuessTheNumber(1,50)
        elif choice == "4":
            GuessTheNumber(1,100)
        elif choice == "8":
            menuLoop = True
        else:
            print("Invalid Selction!")
     


def GuessTheNumber(num1,num2):
    increment = 0
    loop = False
    randNum = random.randint(num1,num2)
    correctNum = str(randNum)
    print(correctNum)
    while loop == False:
        userInput = input("Guess the number between 1 and 10 --> ")
        if increment > 1:
            print("You ran out of chances! The random number was: ", correctNum)
            loop = True
        elif userInput != correctNum:
            print("Try Again!")
            increment += 1
         
        elif userInput == correctNum:
            print("Great Job!")
            loop = True
         

            
