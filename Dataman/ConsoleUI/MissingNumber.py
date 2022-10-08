
import random
import DatamanLibrary as DL
import operator as op

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
    allowed_operators={
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv}

    #Declare and initialize operator list
    operatorList = ['+','-','*']

    #Get random operator from operator list and store specific subscript in operator variable
    randomOperator = random.randint(0,len(operatorList)-1)
    operator = operatorList[randomOperator]

    #Get random integers for num1 and num2
    num1 = random.randint(x,y) 
    num2 = random.randint(x,y)

    #Determine is num2 is greater than num1; used to avoid negative numbers
    if num2 > num1:
       num3 = num1
       num1 = num2
       num2 = num3       
    
    #Calculate total 
    total = allowed_operators[operator](num1,num2)
    problemList = [str(num1),str(num2),str(total)]
        #Get random subscript number to determine which subscript number will be removed from the displayed problem
    subscriptRand = random.randint(0,2)
         
    if subscriptRand == 0: #Number at subscript "0" is removed from the math problem.   
            print(f"? {operator} {problemList[1]} = {problemList[2]}") #Display math problem to user with missing number
            userInput = input("Guess the Missing Number --> ") #Get user input to guess the missing number
            if userInput == problemList[0]:
                print("Great Job!")
            elif userInput != problemList[0]:
                print("Wrong Answer!")
    elif subscriptRand == 1:#Number at subscript "1" is removed from the math problem.
            print(f"{problemList[0]} {operator} ? = {problemList[2]}") #Display math problem to user with missing number
            userInput = input("Guess the Missing Number --> ") #Get user input to guess the missing number
            if userInput == problemList[1]:
                print("Great Job!")
            elif userInput != problemList[1]:
                print("Wrong Answer!")
    elif subscriptRand == 2:#Number at subscript "2" is removed from the math problem.
            print(f"{problemList[0]} {operator} {problemList[1]} = ?") #Display math problem to user with missing number
            userInput = input("Guess the Missing Number --> ") #Get user input to guess the missing number
            if userInput == problemList[2]:
                print("Great Job!")
            elif userInput != problemList[2]:
                print("Wrong Answer!")     






    #CODE REDUCTION_________________________________________________________________________________________________________________________________
    #elif operator == '-':
    #    #SUBTRACTION
    #    total = num1 - num2        
    #    problemList = [str(num1),str(num2),str(total)]       
    #    subscriptRand = random.randint(0,2)        
    #    if subscriptRand == 0: #Number at subscript "0" is removed from the math problem.  
    #        print(f"? - {problemList[1]} = {problemList[2]}") #Display math problem to user with missing number
    #        userInput = input("Guess the Missing Number --> ") #Get user input to guess the missing number
    #        if userInput == problemList[0]:
    #            print("Great Job!")
    #        elif userInput != problemList[0]:
    #            print("Wrong Answer!")
    #    elif subscriptRand == 1: #Number at subscript "1" is removed from the math problem. 
    #        print(f"{problemList[0]} - ? = {problemList[2]}") #Display math problem to user with missing number
    #        userInput = input("Guess the Missing Number --> ") #Get user input to guess the missing number
    #        if userInput == problemList[1]:
    #            print("Great Job!")
    #        elif userInput != problemList[1]:
    #            print("Wrong Answer!")
    #    elif subscriptRand == 2: #Number at subscript "2" is removed from the math problem. 
    #        print(f"{problemList[0]} - {problemList[1]} = ?") #Display math problem to user with missing number
    #        userInput = input("Guess the Missing Number --> ") #Get user input to guess the missing number
    #        if userInput == problemList[2]:
    #            print("Great Job!")
    #        elif userInput != problemList[2]:
    #            print("Wrong Answer!")
    #elif operator == '*':
    #    #MULTIPLICATION
    #    total = num1 * num2
    #    problemList = [str(num1),str(num2),str(total)]       
        
    #    subscriptRand = random.randint(0,2)
       
    #    if subscriptRand == 0: #Number at subscript "0" is removed from the math problem.  
    #        print(f"? * {problemList[1]} = {problemList[2]}")
    #        userInput = input("Guess the Missing Number --> ")
    #        if userInput == problemList[0]:
    #            print("Great Job!")
    #        elif userInput != problemList[0]:
    #            print("Wrong Answer!")
    #    elif subscriptRand == 1: #Number at subscript "1" is removed from the math problem. 
    #        print(f"{problemList[0]} * ? = {problemList[2]}")
    #        userInput = input("Guess the Missing Number --> ")
    #        if userInput == problemList[1]:
    #            print("Great Job!")
    #        elif userInput != problemList[1]:
    #            print("Wrong Answer!")
    #    elif subscriptRand == 2: #Number at subscript "2" is removed from the math problem. 
    #        print(f"{problemList[0]} * {problemList[1]} = ?")
    #        userInput = input("Guess the Missing Number --> ")
    #        if userInput == problemList[2]:
    #            print("Great Job!")
    #        elif userInput != problemList[2]:
    #            print("Wrong Answer!")


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
    #            print("Wrong Answer!")__________________________________________________________________________________________________________________________________________________________________________