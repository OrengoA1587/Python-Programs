
import re
import operator as op
import AnswerChecker as AC
def VerifyMemoryBankProblem(problem):
    auth_operators={
    "+": op.add,
    "-": op.sub,
    "*": op.mul,
    "/": op.truediv}
    
    subscriptDivide = list(filter(None, re.split(r'(\d+)',problem)))#Split  list at the digit and operator and filter out delimeters(",") from list
    total=0
    if AC.CheckCharArrayForSpecificCharacters(subscriptDivide) == True:
        num1 = int(subscriptDivide[0])
        num2 = int(subscriptDivide[2])
        operator = subscriptDivide[1]
        usersInputTotal = int(subscriptDivide[4])

        total = auth_operators[operator](num1,num2)
         
        if total == usersInputTotal:
            return True
        else:
            return False
    else:       
        return False

    #total = auth_operators[operator](num1,num2)
    #print(total)
    #print(usersInputTotal)
    #print(operator)
    #print(num1,num2,total)


    