
#Imported Dataman Modules
import random 
import DatamanLibrary as DL
def ForceOutGameSelection():

    menuLoop = False

    while menuLoop == False:
        #Display functional menu to user
        DL.ForceOutMenu()
        choice = input("Select from the Menu --> ")
        if choice == "1":
            ForceOutGame(10,20)#Random number 10-20
        elif choice == "2":
            ForceOutGame(20,40)#Random number 20-40               
        elif choice == "3":
            ForceOutGame(40,80)#Random number 40-80  
        elif choice == "4":
            ForceOutGame(80,120)#Random number 80-120
        elif choice == "5":
            menuLoop = True
        else:
            print("Invalid Selction!")
def ForceOutGame(num1,num2):
    startNum = random.randint(num1,num2)
    gameNum = startNum
     
    print("Start Number:  ",startNum)
    while gameNum > 0:         
        userInput = input("Enter Number to Subtract --> ")
        if userInput.isdigit():
            if int(userInput) <= 9:
                if gameNum < int(userInput):
                    print("Your number is higher than the current number.\nCurrent Number: ",gameNum)
                else:
                    x = int(userInput)
                    gameNum -= x
                    if gameNum > 0:
                        print("Keep Going!\nCurrent Number: ",gameNum)          
                
            else:
                print("Invalid Entry! Select a number 1-9\nCurrent Number: ",gameNum)    
                
        else:
            print("Invalid Entry!\nCurrent Number: ",gameNum) 
             

    print("Great Job!\n")
