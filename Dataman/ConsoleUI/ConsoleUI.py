
 
#specCharacters = ['1','2','3','4','5','6','7','8','9','0','+','-','x','X','*','/','=']
    #result = []
    #for i in letter:

    #    if i in specCharacters:
    #        result.append("True")
    #    else:
    #        result.append("False")

def MainMenu():

    print("Dataman\n"+
          "1. Answer Checker\n"+
          "2. TODO\n"+
          "3. TODO\n"+
          "4. TODO\n"+
          "8. Exit\n")

def CheckCharArrayForSpecificCharacters(letter):   
    #num1 = letter[0]
    #num2 = letter[2]
    #num3 = letter[4]

    if str(letter[0]).isdigit and str(letter[2]).isdigit and str(letter[4]).isdigit and letter[3] == '=' and letter[1] == '+' or letter[1] == '-' or letter[1] == '/' or letter[1].lower() == 'x':
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
    contLoop = False
    while checkLoop == False:
        problem = input("Enter a Problem --> ")
        problem.split()
        letter = [x for x in problem]
         
         
        if  CheckAnswerChecker(letter) == False:
            print("Incorrect Answer!")
        elif CheckAnswerChecker(letter) == 'invalid':      
            print("Invalid input!")
        else:
            print("Great Job!")
            while contLoop == False:
                cont = input("Continue Y/N -->")
                if cont.lower() == "y":
                    print("")
                elif cont.lower() == "n":
                    contLoop = True
                    checkLoop = True
                else:
                    print("Invalid Input!")
        
        
   
def TODO():
    print("Pending")
def Main():
    menuLoop = False

    while menuLoop == False:

        MainMenu()
        choice = int(input("Select from the Menu --> "))

        if choice == 1:
            AnswerChecker()
        elif choice == 2:
            TODO()
        elif choice == 3:
            TODO()
        elif choice == 4:
            TODO()
        elif choice == 8:
            menuLoop = True
     
Main()
exit()