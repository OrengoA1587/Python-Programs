import os
# Description: This program uses a for loop to display the same elements in the table using less
# lines of code.
# Date: 05/29/2021
# Program: CSC121 M1Lab– Debugging
# Programmer: Anthony Orengo
# Exercise 3.16



# Pseudocode 
# 1. Declare variable "i" and initialize to "0".
# 2. Declare for loop and set range to "6".
# 3. Add print line and replace 0-5 with variable "i" Ex. change "print(0, '\t', 0 ** 2, '\t', 0 ** 3)" to  "print(i, '\t', i ** 2, '\t', i ** 3)".
# 4. Increment loop using "i+=1".
# 5. Run program and view output to verify if both methods are the same.


#StandardMessages Class------------------------------------------------
class StandardMessages:
    #Display Invalid Option
    @staticmethod
    def display_invalid_option():
        print("Invalid Option! Please Try  Again....")

    #Display Menu Options
    @staticmethod
    def main_menu():
        print(
        "***********************\n"+
        "1. Highest Number Game\n" +
        "2. Exit\n\n\n"+         
        "***********************")
#END StandardMessages Class---------------------------------------------
#Highest and second highest function-----------------------------------
def highest_num():
    highestNum = 0
    secondHighestNum = 0
    numStr = ""
   
#Declare loop
    #Loop is set to 10 iterations
    for numbers in range(1,11):
        #Get number from user
        num = input("Enter a number:  ")
        #Parse string to integer
        num = int(num)
   
        if num > highestNum and secondHighestNum >= 0:
            secondHighestNum = highestNum   
            highestNum = num     
        elif num < highestNum:
            if num > secondHighestNum:
                secondHighestNum = num
            elif num < secondHighestNum or num == secondHighestNum:
                secondHighestNum = secondHighestNum + 0
            
        elif num == highestNum:
                highestNum = highestNum + 0  
        else: 
            print("Invalid")
    
    print("Highest Number", highestNum)
    print("Second Highest Number" , secondHighestNum)
   
#END Highest and second highest function----------------------------------

#Declare and initiate variables and objects
choice = ""
menuLoop = 1
MessageInvalid = StandardMessages()
DisplayMenu = StandardMessages()
while menuLoop == 1:
    DisplayMenu.main_menu()
    # Get input from user
    choice = input("\nChoose from the Menu --> ")
    if choice == "1":
        #Start Highest Number game 
        highest_num()
       
    elif choice == "2":
        #Exits program
        print("Goodbye")
        menuLoop = 0
        exit()
    else:
        MessageInvalid.display_invalid_option()

# END Display main menu to user------------------------------------------------




