def MainMenu():
    #Display main menu to user
    print("Dataman\n"+
          "1. Answer Checker\n"+
          "2. Number Guesser\n"+
          "3. Force Out\n"+
          "4. Missing Number\n"+
          "5. Memory Bank\n"+
          "6. Exit\n")
def GuessNumberMenu():
    #Display guess number menu to user
    print("Number Guesser\n"+
          "1. 1-10\n"+
          "2. 1-20\n"+
          "3. 1-50\n"+
          "4. 1-100\n"+
          "5. Exit\n")

def ForceOutMenu():
    #Display force out menu to user
    print("Force Out\n"+
          "1. Start Number 10-20\n"+
          "2. Start Number 20-40\n"+
          "3. Start Number 40-80\n"+
          "4. Start number 80-120\n"+
          "5. Exit\n")

def MissingNumberMenu():
    #Display missing number menu to user
    print("Missing Number\n"+
          "1. Start Number 10-20\n"+
          "2. Start Number 20-40\n"+
          "3. Start Number 40-80\n"+
          "4. Start number 80-120\n"+
          "5. Exit\n")

def MemoryBankMenu():
    #Display memory bank menu to user
    print("Memory Bank\n"+
          "1. Play Game\n"+
          "2. Add to Bank\n"+
          "3. Clear Bank\n"+          
          "4. Exit\n")

def DisplayMemoryBankInputError():
    print("\n*******ERROR******\n\n1. Invalid Problem!\n2. Problem must be written in format 1+1=2 \n3. Answer must be correct \n\n******************\n")