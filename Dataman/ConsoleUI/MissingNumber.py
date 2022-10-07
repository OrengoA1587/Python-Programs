
import random
import DatamanLibrary as DL


def MissingNumberGameSelection():

   menuLoop = False

   while menuLoop == False:
        #Display functional menu to user
        DL.MissingNumberMenu()
        choice = input("Select from the Menu --> ")
        if choice == "1":
            MissingNumberGame(1,10)#Random number 1-10
        elif choice == "2":
            MissingNumberGame(20,40)#Random number 20-40               
        elif choice == "3":
            MissingNumberGame(40,80)#Random number 40-80  
        elif choice == "4":
            MissingNumberGame(80,120)#Random number 80-120
        elif choice == "5":
            menuLoop = True
        else:
            print("Invalid Selction!")

def MissingNumberGame(x,y):
    operatorList = ['+','-','*']

    randomOperator = random.randint(0,len(operatorList)-1)
    operator = operatorList[randomOperator]
    num1 = random.randint(x,y)
    num2 = random.randint(x,y)
    if num2 > num1:
       num3 = num1
       num1 = num2
       num2 = num3
        
     
    if operator == '+':
        
        total = num1 + num2
        problemList = ["0",str(num1),str(num2),str(total)]
        
        subscriptRand = random.randint(1,3)
         
        if subscriptRand == 1:    
            print(f"? + {problemList[2]} = {problemList[3]}")
            userInput = input("Guess the Missing Number --> ")
            if userInput == problemList[1]:
                print("Great Job!")
            elif userInput != problemList[1]:
                print("Wrong Answer!")
        elif subscriptRand == 2:
            print(f"{problemList[1]} + ? = {problemList[3]}")
            userInput = input("Guess the Missing Number --> ")
            if userInput == problemList[2]:
                print("Great Job!")
            elif userInput != problemList[2]:
                print("Wrong Answer!")
        elif subscriptRand == 3:
            print(f"{problemList[1]} + {problemList[2]} = ?")
            userInput = input("Guess the Missing Number --> ")
            if userInput == problemList[3]:
                print("Great Job!")
            elif userInput != problemList[3]:
                print("Wrong Answer!")

    elif operator == '-':
        total = num1 - num2        
        problemList = ["0",str(num1),str(num2),str(total)]       
        subscriptRand = random.randint(1,3)        
        if subscriptRand == 1:
            print(f"? - {problemList[2]} = {problemList[3]}")
            userInput = input("Guess the Missing Number --> ")
            if userInput == problemList[1]:
                print("Great Job!")
            elif userInput != problemList[1]:
                print("Wrong Answer!")
        elif subscriptRand == 2:
            print(f"{problemList[1]} - ? = {problemList[3]}")
            userInput = input("Guess the Missing Number --> ")
            if userInput == problemList[2]:
                print("Great Job!")
            elif userInput != problemList[2]:
                print("Wrong Answer!")
        elif subscriptRand == 3:
            print(f"{problemList[1]} - {problemList[2]} = ?")
            userInput = input("Guess the Missing Number --> ")
            if userInput == problemList[3]:
                print("Great Job!")
            elif userInput != problemList[3]:
                print("Wrong Answer!")
    elif operator == '*':
        total = num1 * num2
        problemList = ["0",str(num1),str(num2),str(total)]       
        
        subscriptRand = random.randint(1,3)
       
        if subscriptRand == 1:
            print(f"? * {problemList[2]} = {problemList[3]}")
            userInput = input("Guess the Missing Number --> ")
            if userInput == problemList[1]:
                print("Great Job!")
            elif userInput != problemList[1]:
                print("Wrong Answer!")
        elif subscriptRand == 2:
            print(f"{problemList[1]} * ? = {problemList[3]}")
            userInput = input("Guess the Missing Number --> ")
            if userInput == problemList[2]:
                print("Great Job!")
            elif userInput != problemList[2]:
                print("Wrong Answer!")
        elif subscriptRand == 3:
            print(f"{problemList[1]} * {problemList[2]} = ?")
            userInput = input("Guess the Missing Number --> ")
            if userInput == problemList[3]:
                print("Great Job!")
            elif userInput != problemList[3]:
                print("Wrong Answer!")


    #TODO: DIVISION
    #elif operator == '/':
    #    total = num1 + num2
    #    problemList = [0,num1,num2,total]
        
    #    subscriptRand = random.randint(0,3)
    #    if subscriptRand == 1:
    #        print(f"? / {problemList[2]} = {problemList[3]}")
    #        userInput = input("Guess the Missing Number --> ")
    #        if userInput == problemList[1]:
    #            print("Great Job!")
    #        elif userInput != problemList[1]:
    #            print("Wrong Answer!")
    #    elif subscriptRand == 2:
    #        print(f"{problemList[1]} / ? = {problemList[3]}")
    #        userInput = input("Guess the Missing Number --> ")
    #        if userInput == problemList[2]:
    #            print("Great Job!")
    #        elif userInput != problemList[2]:
    #            print("Wrong Answer!")
    #    elif subscriptRand == 3:
    #        print(f"{problemList[1]} / {problemList[2]} ? = ?")
    #        userInput = input("Guess the Missing Number --> ")
    #        if userInput == problemList[3]:
    #            print("Great Job!")
    #        elif userInput != problemList[3]:
    #            print("Wrong Answer!")