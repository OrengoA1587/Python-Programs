#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 18:23:30 2021

@author: orengoa0459
"""
import  MathProblems as problems
import  StandardMessages as messages
import os
import sys

def difficultyLevel():
    levelSelection = 0
    menuLoop = 0

    while (menuLoop == 0):
        #Display difficult level menu to user
        messages.StandardMessages.difficulty_level_menu()
        #Get input from user
        choice = input("Choose from the menu --> ")

        #Beginners--------------------
        if choice == "1":
            while levelSelection == 0:
                # Display difficult level sub-menu to user
                messages.StandardMessages.beginner_menu()
                # Get input from user
                choice_level = input()
                if choice_level == "1":
                    problems.MathProblemFunctions.multiplication_beginner_level_1() #Beginner Level one game
                elif choice_level == "2":
                    problems.MathProblemFunctions.multiplication_beginner_level_2() #Beginner Level two game
                elif choice_level == "3":
                    problems.MathProblemFunctions.multiplication_beginner_level_3() #Beginner Level three game
                elif choice_level == "q":
                    levelSelection += 1
                else:
                    messages.StandardMessages.invalidMessages()
            break
        #Intermediate--------------------
        elif choice == "2":
            while levelSelection == 0:
                # Display difficult level sub-menu to user
                messages.StandardMessages.intermediate_menu()
                # Get input from user
                choice_level = input()
                if choice_level == "1":
                    problems.MathProblemFunctions.multiplication_intermediate_level_1() #Intermediate Level one game
                elif choice_level == "2":
                    problems.MathProblemFunctions.multiplication_intermediate_level_2() #Intermediate Level two game
                elif choice_level == "3":
                    problems.MathProblemFunctions.multiplication_intermediate_level_3() #Intermediate Level three game
                elif choice_level == "q":
                    levelSelection += 1
                else:
                    messages.StandardMessages.invalidMessages()
                
            break
        #Expert--------------------
        elif choice == "3":
            while levelSelection == 0:
                # Display difficult level sub-menu to user
                messages.StandardMessages.Expert_menu()
                # Get input from user
                choice_level = input()
                if choice_level == "1":
                    problems.MathProblemFunctions.multiplication_expert_level_1() #Expert Level one game
                elif choice_level == "2":
                    problems.MathProblemFunctions.multiplication_expert_level_2() #Expert Level two game
                elif choice_level == "3":
                    problems.MathProblemFunctions.multiplication_expert_level_3() #Expert Level three game
                elif choice_level == "q":
                    levelSelection += 1
                else:
                    messages.StandardMessages.invalidMessages()
            break
            # Exits program
        elif choice == "q":
                menuLoop += 1
        else:
            messages.StandardMessages.invalidMessages()
