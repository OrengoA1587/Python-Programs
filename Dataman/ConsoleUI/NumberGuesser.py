
import random
import DatamanLibrary as DL
 


def GuessNumber():  
     
    menuLoop = False

    while menuLoop == False:
        #Display functional menu to user
        DL.GuessNumberMenu()
        choice = input("Select from the Menu --> ")
        if choice == "1":
            GuessTheNumber(1,10)#Random number 1-10           
        elif choice == "2":
            GuessTheNumber(1,20)#Random number 1-20  
             
        elif choice == "3":
            GuessTheNumber(1,50)#Random number 1-30  
        elif choice == "4":
            GuessTheNumber(1,100)#Random number 1-100
        elif choice == "5":
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
        userInput = input("Guess a number between " + str(num1) + " and " + str(num2) + " --> ")
        if userInput == correctNum:
            print("\nGreat Job!\n")
            loop = True
        elif increment > 1:
            print("You ran out of chances! The random number was: ", correctNum, "\n")
            loop = True
        elif userInput != correctNum:
            if int(userInput) > int(correctNum):
                print("To High! Try a lower number.\n")
            elif int(userInput) < int(correctNum):
                print("To Low! Try a higher number.\n")
            #print("Try Again!")
            increment += 1
         
        
        else:
            print("Invalid Input!")

            
