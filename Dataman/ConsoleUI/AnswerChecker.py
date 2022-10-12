


import Continue as con
import re # Regex import to customize string input
import operator as op

def CheckCharArrayForSpecificCharacters(letter):    
        #Determine if letter array has exactly 5 subscripts
        #Determine if character list has digits and characters "+,-,*,/" at the correct subscript
        #Return false if input is invalid

        if not letter or len(letter) < 5 or len(letter) > 5:             
            return False
        elif str(letter[0]).isdigit and str(letter[2]).isdigit and str(letter[4]).isdigit and letter[3] == '=' and letter[1] == '+' or letter[1] == '-' or letter[1] == '/' or letter[1].lower() == 'x':
            return True
        else:
            return False
 
def CheckAnswerChecker(letter):
   auth_operators={
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv}  
   loop = False
   while loop == False:       
       if CheckCharArrayForSpecificCharacters(letter) == False: #Determine is list contain correct characters at the given subscript
            return "invalid"
       else:
           #store subscripts 0 and 2 in variables num1 and num2 for later user
           num1 = int(letter[0]) 
           num2 = int(letter[2])
           #Determine is num2 is greater than num1; used to avoid negative numbers
           if num2 > num1 and letter[1] != "/":
                num3 = num1
                num1 = num2
                num2 = num3     

           total = auth_operators[letter[1]](num1,num2) #Calculate answer 
           if total == int(letter[4]): # Check answer
               return True #Return true for correct
           else:
               return False #Return false for incorrect
          
def AnswerChecker():
    
    checkLoop = False  
     
    while checkLoop == False:
        contLoop = False
        problem = input("Enter a Problem --> ") #Get problem from user in format "1+1=2"
        problem = ''.join(problem.split()) #Split problem to eliminate white space and string together
        letter = list(filter(None, re.split(r'(\d+)',problem)))#Split  list at the digit and operator and filter out delimeters(",") from list       
         
        if  CheckAnswerChecker(letter) == False: #Send problem to checkanswerchecker function to determine correct answer
            print("Incorrect Answer!")
            if con.ContinueGame(contLoop,checkLoop) == False:#Get input from user to continue or end the game
                checkLoop = True
                contLoop = True
        elif CheckAnswerChecker(letter) == 'invalid':#Display invalid to user if input is incorrect      
            print("Invalid input!")
            if con.ContinueGame(contLoop,checkLoop) == False:#Get input from user to continue or end the game
                checkLoop = True
                contLoop = True
        else:
            print("Great Job!")
            if con.ContinueGame(contLoop,checkLoop) == False:#Get input from user to continue or end the game
                checkLoop = True
                contLoop = True
        
        
