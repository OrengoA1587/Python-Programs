#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 12:06:30 2021

@author: orengoa0459
"""
# Description: This program is designed to help elementary school students(grades 2+), learn
# multiplication. The program consist of 3 difficulty levels (beginner,intermediate,expert)
# and 3 sub levels (level 1,2,3). When the user selects their difficulty level they
# will be prompted to select a sub category level. Each multiplication game consists
# of 10 problems. Users will be given a designated number of retries per difficulty
# level. Once the user completes the 10 problems, the score will be displayed.

# Date: Start 06/03/2021 End: 06/08/2021
# CSC121 M2HW – Computer Assisted
# Anthony Orengo

import  DifficultyLevel as dif_Level
import  StandardMessages as messages 
import os
import sys
 
def main():
    menuLoop = 0
    while menuLoop == 0:
        #Display main menu to user
        messages.StandardMessages.main_menu()
        #Get input from user
        choice = input("Choose from the menu --> ")
        if choice == "1":
            #Select difficulty level
            dif_Level.difficultyLevel()
        elif choice == "2":
            messages.StandardMessages.display_instructions()
        elif choice == "q":
            #Exits program
            menuLoop += 1
        else:
            #Display invalid choice to user
            print(messages.StandardMessages.invalidMessages())
            
if __name__ == "__main__":
    main()



