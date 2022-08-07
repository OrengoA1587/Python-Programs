import os
# Description: This program determines the highest and second highest number out of
# 10 numbers inputted by the user.
# Date: 05/29/2021
# Program: CSC121 M1HW
# Programmer: Anthony Orengo
# Exercise 3.16



# Pseudocode
# 1. Create standard messages Class with two defined static methods that will
# display a "main menu" and "invalid option". Place " @staticmethod " above defined method.
# 2. Define a function called "main()" and declare variables,objects from standard messages class,
# and sentinels that will be used to navigate the main menu. The main menu will contain
#two options, the game option and exit option.
# 3. Define a function called highest number.
# 4. Declare and intialize variables for the highest and second highest number.
# 5. Declare and initialize total numbers variable. The variable will be user to set the number of
# iterations for the loop. The variable will be set a string that will be parsed to an int and incremented by 1.
# The variable is incremented by one for loop purposes.
# 6. Create a "for" loop called "numbers" and set range to number of iterations set by user (1,totalNumbers).
# 7. Get numbers from user and parse the string to an int.
# 8. Create nested loops to determine and set the highest and second highest numbers.
# 9. Display the highest and second highest number to the user once all numbers are inputted.
 


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
    totalNumbers = ""
    count = "1"
   
#Declare loop
    #Get total numbers to input from user
    totalNumbers = input("How many number do you want to enter --> ")
    #Parse input to integer
    totalNumbers = int(totalNumbers)
    #Add 1 to totalNumbers for loop purposes
    totalNumbers += 1
    #Loop iteration is set to users inputted number
    for numbers in range(1,totalNumbers):
        #Get number from user
        num = input("Enter number " + count + " :  ")
        #Parse string to integer
        num = int(num)
        count = int(count)
        count += 1
        count = str(count)
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
def main():
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

#Call main function

main()



