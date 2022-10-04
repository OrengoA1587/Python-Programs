


import Continue as con
import re # Regex import to customize string input
 

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
    
   loop = False
   while loop == False:       
       if CheckCharArrayForSpecificCharacters(letter) == False: #Determine is list contain correct characters at the given subscript
            return "invalid"
       else:
           #store subscripts 0 and 2 in variables num1 and num2 for later user
           num1 = int(letter[0]) 
           num2 = int(letter[2])
    
           total = num1 + num2 #Perform calculation to determine correct answer

           if letter[1] == '+':
                total = num1 + num2 #Calculate correct answer
                if total == int(letter[4]): # Check answer
                    return True
                else:
                    return False
           elif letter[1] == '-':
                total = num1 - num2 #Calculate correct answer
                if total == int(letter[4]): # Check answer
                    return True
                else:
                    return False
           elif letter[1] == 'X' or letter[1] == 'x' or letter[1] == '*':
                total = num1 * num2 #Calculate correct answer
                if total == int(letter[4]): # Check answer
                    return True
                else:
                    return False
           elif letter[1] == '/':
                total = num1 / num2 #Calculate correct answer
                if total == int(letter[4]): # Check answer
                    return True
                else:
                    return False
           else:
               return "invalid"
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
        
        
