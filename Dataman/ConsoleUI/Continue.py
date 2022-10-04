def ContinueGame(contLoop,checkLoop):
    while contLoop == False:
        cont = input("Continue Y/N -->")
        if cont.lower() == "y":
              contLoop = True
              print("")
        elif cont.lower() == "n":
              return False
        else:
              print("Invalid Input!")