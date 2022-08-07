
# This program allows the user to create a dictionary that they can
# search, add to, update, and display contents within the dictionary.
# Date 06/17/2021
# CSC121 M4Lab – Dictionary Manipulations
# Anthony Orengo

#Pseudocode
#1. Declare initialize GLOBAL dictinary
#2. Define functions main(), create_dictionary(),search_dictionary(),add_to_dictionary(),update_dictionary(),
#display_dictionary()
#3. Create a functional menu that consist of 6 options, 5 that consist of the above functions and 1 that is an
# exit option.
#4. Declare and initialize the main menu sentinel
#5. In the create dictionary function, get the user to enter the amount of countries they would like to enter.
# The user will then be prompt to enter the country name(key) and the TLD (value). You will use the dictionary update
# to input the data in to the dictionary.
#6. In the search dictionary function, prompt user to enter the country name(key). You will need an if statement to
# to determine if the country exist. If the country exist, display data to user.
#7. In the add to dictionary function, prompt user to input a country name and its TLD. Use the update() dictionary method
# to update dictionary with inputted values.
#8. In the update dictionary function, prompt user to enter the country name(key). You will use the search dictionary
# method (.get()) to determine if the country exist. If it exist, you will prompt the user to input the update TLD.
# You will use the update() dictionary method to update the dictionary.
#9. In the display dictionary function, display the entire dictionary in tabular format.
#10. The menu will continue until the user exits.
#

#GLOBAL
DICTIONARY = {}

def create_dictionary():
    #Get number of countries to input from user
    country_num = input("How many countries would you like to add? ")
    #Determine if user enters a letter
    if country_num.isalpha():
        print("Input error! Must be a digit!")
    else:
        #Add key-value pairs
        country_num = int(country_num)
        for num in range(1, country_num+1):
            name = input(f"Enter country name {num}: ")
            country_tld = input(f"Enter TLD for {name}: ")
            #Update dictionary with key-value pairs
            DICTIONARY.update({name: country_tld})

def search_dictionary():
    #Get country name from user
    name = input("Enter key name: ")
    #Search dictionary
    DICTIONARY.get(name)
    #Display results to user if country exist
    if name in DICTIONARY:
        print(f"Country Exist!\n")
        print(f'{"Country":<20}{"Country TLD":}')
        print("---------------------------------")
        print(f'{name:<20}{DICTIONARY.get(name)} ')
    #Display if country does not exist
    else:
        print("Country does not exist!")

def add_to_dictionary():
    for num in range(1):
        #Prompt user to enter country name
        name = input(f"Enter country name: ")
        #Prompt user to enter country TLD
        country_tld = input(f"Enter TLD for {name}: ")
        # Update dictionary with key-value pairs
        DICTIONARY.update({name: country_tld})

def update_dictionary():
    #Prompt user to enter key name
    name = input("Enter key name: ")
    #Search dictionary for key name
    DICTIONARY.get(name)
    if name in DICTIONARY:
        #Prompt user to enter new TLD
        country_tld = input("Enter countries new TLD --> ")
        #Update dictionary
        DICTIONARY.update({name: country_tld})
    else:
        print("Country does not exist!")


def display_dictionary():
    #Diplays all items in the dictionary
    print(f'{"Country":<20}{"Country TLD":}')
    print("---------------------------------")
    for k, v in DICTIONARY.items():
        print(f'{k:<20}{v}')

def main():
    menu_loop = False
    while menu_loop == False:
        #Display menu to user
        print("MENU\n"+
              "-------------------\n"+
              "1) Create dictionary\n"+
              "2) Search for TLD\n" +
              "3) Add to dictionary\n" +
              "4) Update dictionary\n" +
              "5) Display dictionary content\n" +
              "6) Exit\n")
        #Get input from user
        choice = input("Make a selection --> ")
        if choice == '1':
            create_dictionary()
        elif choice == '2':
            search_dictionary()
        elif choice == '3':
             add_to_dictionary()
        elif choice == '4':
            update_dictionary()
        elif choice == '5':
            display_dictionary()
        elif choice == '6':
            menu_loop = True
        else:
            print("Invalid Option")

# Call main function
main()