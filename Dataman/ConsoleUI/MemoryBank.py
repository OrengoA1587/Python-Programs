#Imported Dataman Modules
import DatamanLibrary as DL
import re
import operator as op
import MemoryBankProblemVerification as MBPV

def MemoryBankMenuSelection():

   menuLoop = False#Declare and initialize game memu sentinel

   while menuLoop == False:#Continues loop until boolean equals true
        #Display functional menu to user
        DL.MemoryBankMenu()
        choice = input("Select from the Menu --> ")#Get input from user
        if choice == "1":
            PlayMemoryBank()#Execute function (Play memory bank game)
        elif choice == "2":
            AddToBank()#Execute function (Add to gamebank file)          
        elif choice == "3":
            ClearBank()#Execute function (Clear gamebank file)           
        elif choice == "4":
            menuLoop = True
        else:
            print("Invalid Selction!")

#PLAY MEMORY BANK GAME FUNCTION----------------------------------------------------------------------------------------------
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
    score = 0

    #Count number of lines in GameBank file to ensure math problems exist
    with open("GameBank.txt", mode="r") as gameFile:              
         for count, line in enumerate(gameFile):    
                
             pass    
        
    if count + 1 > 0:  
        with open("GameBank.txt", mode="r") as gameFile:
            #gameDoc = gameFile.readline()
             
            count +=1
            while count != 0:                    
                    problem = gameFile.readline()#Read each line in text document                   
                    problem = ''.join(problem.split())#Join string at locations that are white space
                    letter = list(filter(None, re.split(r'(\d+)',problem)))#Split  list at the digit and operator and filter out delimeters(",") from list

                    print(letter)#THIS IS FOR DEBUGGING PURPOSES ONLY. WILL BE REMOVED WHEN ALL BUGS ARE FIXED.
                    #Declare and initialize variables with appropriate subscipt
                    num1 = int(letter[0])
                    num2 = int(letter[2])
                    operator = (letter[1])

                    #totalFromDoc = int(letter[4])
                    total = auth_operators[operator](num1,num2)#Calculate total
                    print(total)#THIS IS FOR DEBUGGING PURPOSES ONLY. WILL BE REMOVED WHEN ALL BUGS ARE FIXED.
                    answer = input(f"{num1} {operator} {num2} = ?  ")#Get input from user

                    if answer == str(total):#Verify answer is correct or incorrect
                        print("Great Job!")
                        score += 1
                    else:
                        print("Sorry! Incorrect Answer.")
                    count -= 1  

            print(f"\n*****GAMEOVER*****\n\nPLAYER SCORE: {score}\n\n******************\n")#Display players score when game is finished
            gameFile.close()
    else:
        print("Memory Bank Empty...")#Display if file is empty
        gameFile.close()#Close file

#ADD TO GAMEBANK FILE FUNCTION----------------------------------------------------------------------------------------------
def AddToBank():
    count = 0
    #Get admin authentication by verifying password from txt doc
    #Get admin to enter problems and use the split/join and regex function to create proper format
    #Write to txt doc

    #Get user to input admin password and verify that the inputted password matches the stored admin password in doc.
    password = input("Enter Admin Password --> ")
    with open("DatamanPass.txt",mode = "r") as readDoc:
        #adminPass = readDoc.readline()
        password2 = readDoc.readline()
    readDoc.close()
    
    #Allow user to write to document if password matches admin password
    if password == password2:            
       with open("GameBank.txt", mode="r") as gameFile:              
            for count, line in enumerate(gameFile):    
                
                pass
       #Determines if lines are equal to zero. If lines are equal to zero a new document or current document is refreshed/cleared
       #Condition statement to determine if there is space available to add math problems to document
       if count + 1 == 0:
            problem = input("Enter Problem --> ")#Get user to enter problem to store in document
            problem = ''.join(problem.split()) #Split problem to eliminate white space and string together
             
            if MBPV.VerifyMemoryBankProblem(problem) == True:#Verifies that inputted problem is indeed a correct problem (ex. 1+1=2)
                with open("GameBank.txt", mode = "w") as gameFile:
                     gameFile.write(problem)#Writes problem to document
                     print("Problem Added Successfully")
                     gameFile.close()
            else:
                DL.DisplayMemoryBankInputError()
       #If lines are greater than 1 and less than 10. Allow user to enter/add a new problem
       elif count +1 < 10 and count +1 > 0:
            problem = input("Enter Problem --> ")
            problem = ''.join(problem.split()) #Split problem to eliminate white space and string together
            if MBPV.VerifyMemoryBankProblem(problem) == True:#Verifies that inputted problem is indeed a correct problem (ex. 1+1=2)
                with open("GameBank.txt", mode = "a") as gameFile:
                     gameFile.write(f"\n{problem}")#Writes problem to document
                     print("Problem Added Successfully")
                     gameFile.close()
            else:
                DL.DisplayMemoryBankInputError()#Displays error to user
                gameFile.close()
       elif count == 10:#If count is equal to 10 display memory bank full to user
            print("Memory Bank Full! Clear bank!")   
            gameFile.close()        
    else:
        print("Invalid Password!")

 #CLEAR GAMEBANK FILE FUNCTION----------------------------------------------------------------------------------------------       
def ClearBank():
    #Clear txt doc
    password = input("Enter Admin Password --> ")
    with open("DatamanPass.txt",mode = "r") as readDoc:
        #adminPass = readDoc.readline()
        password2 = readDoc.readline()
    readDoc.close()
    if password == password2: 
            with open("GameBank.txt", mode = "w") as f:#Opens gamebank document and overwrites and clears the document
                 pass
            print("Memory Bank Cleared....")