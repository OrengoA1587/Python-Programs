#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Description: This program use a dictionary to quiz the user on country
# capitals. The quiz consists of 10 questions and upon completion, will display
# the total correct and incorrect responses.
# 06/22/2021
# CTI-110 M4HW – Country Capitals
# Anthony Orengo

import M4HW_Country_Capitals as Capitals
import random

#Pseudocode:
#1. Hardcode two identical dictionaries with different names .
#2. Define main function.
#3. Create a main menu with two options controlled by a sentinel
#4. Define country capitals game function with a variable called score.
#5. Create a for loop with a range of 10(10 Questions).
#6. Create method to get random key (country) from the dictionary and declare a variable to
#to get the countries value(capital).
#7. Convert the values letters to all lowercase using .lower().
#8. Prompt user to input the correct answer. Use if/elif to determine if the users answer is
# correct. If the user answers correctly, use the pop method to remove the country from the dictionary
# and add 1 point to the users score. If the user answers incorrectly, the country will remain in
# the dictionary.
#9. At the end of the game display the users total correct and incorrect answers.
#10. Return to the main menu and call a method to reload the dictionary items so the
# user has the option to play again. 



def country_capitals_game(COUNTRY_CAPITALS):
    score = 0
    incorrect_score = 0
    print("\nThe quiz consist of 10 questions. Begin when you are ready.\n"
          f"You may also exit the game at anytime by inputting \"q\" as an answer.\n\n")
          
    for count in range(10):

        random_country = random.choice(list(COUNTRY_CAPITALS)) #Get random country from dictionary
        get_value = COUNTRY_CAPITALS.get(random_country) #Get the value related to the country
        get_value = str(get_value.lower()) #Convert string to all lowercase
        answer = input(f"{count + 1}. What is the capital of {random_country}? ")#Get input from user

        if answer.lower() == str(get_value):
            print("Correct!")
            score += 1 # Add 1 point to users score
            COUNTRY_CAPITALS.pop(random_country,get_value) # Remove country from the dictionary to prevent repeats
        elif answer.lower() == "washington dc" and str(get_value) == "washington d.c.": # US Capital variation
            print("Correct!")
            COUNTRY_CAPITALS.pop(random_country, get_value) # Remove country from the dictionary to prevent repeats
        elif answer.lower() == "q":
            quit()#Exit game
        else:
            print("Incorrect!") # Display incorrect to the user
            incorrect_score += 1
    print(f"\nScore\n"
          f"--------------------\n"
          f"Total Correct: {score}\n"# Display final score to the user
          f"Total Incorrect: {incorrect_score}\n"
          f"--------------------\n")
def main():
    menu_loop = False #Declare and initialize sentinel
    while menu_loop == False:
        # Display main menu to user
        print("MENU\n"+
              "1. Country Capitals\n"+
              "2. Exit")
        choice = input("Make a selection from the menu --> ")#Get input from the user
        if choice == "1":
            country_capitals_game(Capitals.COUNTRY_CAPITALS) #start country capitals game
            Capitals.reload_country_capitals(Capitals.COUNTRY_CAPITALS) #Reload country capitals into dictionary
        elif choice == "2":
            menu_loop = True #Exit program
        else:
            #Display invalid option to the user
            print("Invalid Option! Try again!")

main();                     
