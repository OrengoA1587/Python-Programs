# Description: This program ask the user to input the total amount of numbers they would
# like to add to the list. The user will be prompted to enter their numbers.
# Upon completion, the program will display all the numbers in the list, the minimum
# and maximum number, total of all numbers, and the average number in the list.

# Date 06/08/2021
# CSC-121 M3Lab – Lists
# Anthony Orengo

#Pseudocode
#1. Define main function and declare and initialize variables, sentinel, and list.
#2. Define function to get numbers from user.
#3. Define function to display main menu to user.
#4. In the main function, create a loop for the main menu. Get input from the user and
# and parse the string to an int. You will use the list and number as arguments in the
# get number function. 
#5. In the get number function, add a loop to get 10 numbers from the user. Each number
#will be inserted into the list until 10 numbers have been added.
#6. After the user inputs all numbers into the list, the numbers in the list will be
#displayed to the user. 
#7. The min/max number, total of numbers, and average number will also be displayed to
# the user.


#Function to get numbers and add them to a list
def get_numbers(total_num, number_list):
     i = 1
     while i <= total_num:
            #Get numbers from user
            num = input(f"Enter number choice {i} --> ")            
            #Determine if the user entered a digit or letter
            if num.isalpha():
                print("Invalid input! You must enter a number!")
            
            else:
                #num = int(num)
                num = float(num)
                #Add users number to list
                number_list.insert(i,num)
                i += 1

     return number_list
#Function to display main menu to user       
def main_menu():
    print("Main Menu\n" +
        "1. Enter Numbers\n" +
        "2. Exit")

def main():
    #Declare and initialize sentinel    
    menu_loop = 0
    #Declare list
    number_list = []
    total_num = ""
    while menu_loop == 0:
        #Displays main menu to user
        main_menu()
        #Get input from user
        choice = input("Make a selection --> ")
        if choice == "1":
            #Get total numbers from user
            total_num = input("How many numbers do you want to add to the list? --> ")
            #Determine if the user entered a digit or letter
            if total_num.isalpha():
                    print("You must enter a number")
            else:
                    #Parse string to int
                    total_num = int(total_num)
                    #Call get_numbers function
                    get_numbers(total_num, number_list)
                    #Display all numbers in list
                    print("\nNumber List\n******************")
                    for element in number_list:
                            x = 1
                            print(f"{element}")
                    #Display the smallest number in the list to the user
                    print(f"Smallest Number: {min(number_list)}")
                    #Display the largest number in the list to the user
                    print(f"Largest Number: {max(number_list)}")
                    #Display the total sum of all numbers in the list to the user
                    print(f"Total: {sum(number_list)}")
                    #Display the average number in the list to the user
                    print(f"Average Number: {sum(number_list)/len(number_list)}\n")
        
        elif choice == "2":
            #Ends the program
            menu_loop += 1
        else:
           print("Invalid option! Try again!")     
        number_list.clear()
#Call  main function
main()
