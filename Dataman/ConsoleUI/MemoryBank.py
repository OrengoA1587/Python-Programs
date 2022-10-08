


def MemoryBankMenuSelection():

   menuLoop = False

   while menuLoop == False:
        #Display functional menu to user
        DL.MissingNumberMenu()
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

    print("TODO")
def AddToBank():

    print("TODO")


def ClearBank():

    print("TODO")