


import Continue as con
import re # Regex import to customize string input
 

def CheckCharArrayForSpecificCharacters(letter):   
        #num1 = letter[0]
        #num2 = letter[2]
        #num3 = letter[4]
        if not letter:
             
            return False
        elif str(letter[0]).isdigit and str(letter[2]).isdigit and str(letter[4]).isdigit and letter[3] == '=' and letter[1] == '+' or letter[1] == '-' or letter[1] == '/' or letter[1].lower() == 'x':
            return True
        else:
            return False
 
def CheckAnswerChecker(letter):
    
   loop = False
   while loop == False:       
       if CheckCharArrayForSpecificCharacters(letter) == False: 
            return "invalid"
       else:
           num1 = int(letter[0]) 
           num2 = int(letter[2])
    
           total = num1 + num2  

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
        problem = input("Enter a Problem --> ")
        problem = ''.join(problem.split())
        letter = list(filter(None, re.split(r'(\d+)',problem)))            
         
        if  CheckAnswerChecker(letter) == False:
            print("Incorrect Answer!")
            if con.ContinueGame(contLoop,checkLoop) == False:
                checkLoop = True
                contLoop = True
        elif CheckAnswerChecker(letter) == 'invalid':      
            print("Invalid input!")
            if con.ContinueGame(contLoop,checkLoop) == False:
                checkLoop = True
                contLoop = True
        else:
            print("Great Job!")
            if con.ContinueGame(contLoop,checkLoop) == False:
                checkLoop = True
                contLoop = True
        
        
