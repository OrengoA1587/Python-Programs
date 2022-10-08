
import DatamanLibrary as DL
import re
import operator as op
import MemoryBankProblemVerification as MBPV
def MemoryBankMenuSelection():

   menuLoop = False

   while menuLoop == False:
        #Display functional menu to user
        DL.MemoryBankMenu()
        choice = input("Select from the Menu --> ")
        if choice == "1":
            PlayMemoryBank()
        elif choice == "2":
            AddToBank()          
        elif choice == "3":
            ClearBank()           
        elif choice == "4":
            menuLoop = True
        else:
            print("Invalid Selction!")

def PlayMemoryBank():
    #Read from text doc bank and display to user
    #Store what was read from the doc in list
    #perform calculations to determine answer and store in variable
    #Get input from the user to verify input to the answer
    #Display to user if the answer is correct or not
    auth_operators={
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv}
    count =0

    with open("GameBank.txt", mode="r") as gameFile:              
         for count, line in enumerate(gameFile):    
                
             pass
     
        
    if count + 1 > 0:  
        with open("GameBank.txt", mode="r") as gameFile:
            #gameDoc = gameFile.readline()
             
            count +=1
            while count != 0:
                    #print("Line {}: {}".format(count, line.strip()))
                    #print(gameFile.readline())
                    problem = gameFile.readline()
                    #line = gameFile.readline()
                    problem = ''.join(problem.split())
                    letter = list(filter(None, re.split(r'(\d+)',problem)))#Split  list at the digit and operator and filter out delimeters(",") from list
                    print(letter)
                    num1 = int(letter[0])
                    num2 = int(letter[2])
                    operator = (letter[1])
                    totalFromDoc = int(letter[4])
                    total = auth_operators[operator](num1,num2)
                    print(total)
                    answer = input(f"{num1} {operator} {num2} = ?  ")

                    if answer == str(total):
                        print("Great Job!")
                    else:
                        print("Sorry! Incorrect Answer.")

                    count -= 1
                 
                 

    else:
        print("Memory Bank Empty...")
#if count == 0:
#            print("Game Over.....")
#        else:
#            print()

     
def AddToBank():
    count = 0
    #Get admin authentication by verifying password from txt doc
    #Get admin to enter problems and use the split/join and regex function to create proper format
    #Write to txt doc
    password = input("Enter Admin Password --> ")
    with open("DatamanPass.txt",mode = "r") as readDoc:
        #adminPass = readDoc.readline()
        password2 = readDoc.readline()
    readDoc.close()
    if password == password2:            
       with open("GameBank.txt", mode="r") as fp:              
            for count, line in enumerate(fp):    
                
                pass
       #print(count + 1)
       if count + 1 == 0:
            problem = input("Enter Problem --> ")
            problem = ''.join(problem.split()) #Split problem to eliminate white space and string together
             
            if MBPV.VerifyMemoryBankProblem(problem) == True:
                with open("GameBank.txt", mode = "w") as f:
                     f.write(problem)
                     print("Problem Added Successfully")
                     f.close()
            else:
                DL.DisplayMemoryBankInputError()
       elif count +1 < 10 and count +1 > 0:
            problem = input("Enter Problem --> ")
            problem = ''.join(problem.split()) #Split problem to eliminate white space and string together
            if MBPV.VerifyMemoryBankProblem(problem) == True:
                with open("GameBank.txt", mode = "a") as f:
                     f.write(f"\n{problem}")
                     print("Problem Added Successfully")
                     f.close()
            else:
                DL.DisplayMemoryBankInputError()
       elif count == 10:
            print("Memory Bank Full! Clear bank!")   
                    
    else:
        print("Invalid Password!")
    
def ClearBank():
    #Clear txt doc
    password = input("Enter Admin Password --> ")
    with open("DatamanPass.txt",mode = "r") as readDoc:
        #adminPass = readDoc.readline()
        password2 = readDoc.readline()
    readDoc.close()
    if password == password2: 
            with open("GameBank.txt", mode = "w") as f:
                 pass
            print("Memory Bank Cleared....")