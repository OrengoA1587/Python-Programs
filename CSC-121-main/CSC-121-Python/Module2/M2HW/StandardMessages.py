# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 11:09:20 2021

@author: Anthony
"""

class StandardMessages():
    # Displays main menu//////////////////////////////////////////////////////
    staticmethod(0)
    def main_menu():
        
        print("\nMain Menu\n" +
              "*********************\n" +
              "1. Multiplication Game\n" +
              "2. Instructions\n" +
              "q. Exit")
        
    # Displaysdifficulty level menu///////////////////////////////////////////
    staticmethod(0)
    def difficulty_level_menu():
        
        print("\nSelect Difficulty Level\n" +
              "*********************\n" +
              "1. Beginner     (Grade 2-3)\n" +
              "2. Intermediate (Grade 4-5)\n"+
              "3. Expert       (Grade 5+)\n"+
              "q. Return to Main Menu")
        # Displays main menu//////////////////////////////////////////////////////
        staticmethod(0)

    def beginner_menu():
        print("\nBeginner\n" +
            "*********************\n" +
              "1. Level 1 (Digits 1-5)\n" +
              "2. Level 2 (Digits 1-6)\n" +
              "3. Level 3 (Digits 1-7)\n" +
              "q. Exit")

    def intermediate_menu():
        print("\nIntermediate\n" +
              "*********************\n" +
              "1. Level 1 (Digits 1-10)\n" +
              "2. Level 2 (Digits 1-15)\n" +
              "3. Level 3 (Digits 1-20)\n" +
              "q. Exit")

    def Expert_menu():
        print("\nExpert\n" +
              "*********************\n" +
              "1. Level 1 (Digits 1-50)\n" +
              "2. Level 2 (Digits 1-100)\n" +
              "3. Level 3 (Digits 1-1000)\n" +
              "q. Exit")

    # Displays invalid message////////////////////////////////////////////////    
    staticmethod(0)
    def invalidMessages():
        
        print("Invalid Option! Try Again!")

    def invalidNumberInput():
        print("Invalid Input! You must enter a number!")


    #Displays instructions to user

    def display_instructions():
        print("Game Instructions\n"+
              "***************************************************************\n"+
              "1. Start the game by selecting ""Multiplication Game"".\n" +
              "2. Select difficulty level base on grade level or preference\n"+
              "3. Select the sub level category for the difficulty level\n" +
              "4. The user will be given 10 random multiplication problems to\n"+
              "   answer. Depending on the difficulty, the user will have a limited\n"+
              "   number of chances to answer the problem correctly.\n"+
              "5. At the end of the game the users score will be displayed.\n"+
              "6. The user will be redirected to the sub level category where \n"+
              "   they can choose the next level.")


















              
