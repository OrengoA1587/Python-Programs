# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 17:13:47 2021

@author: Anthony
"""

# This program allows the user to create an array and manipulate the elements 
#within the array by use of numpy.  
# 06/26/2021
# CSC121 M5HW – Array Manipulations
# Anthony Orengo

#Pseudocode
#1. Define main function and create an options menu consisting of 5 options 
# with exit being the 5th option and the rest for array manipulation.
#2. Define functions display array create array, square value, add four, 
# and multiply by six.
#3. In the create array function, use a for loop to get integer values from the 
# user. Determine if input is a int by using the isalpha().
# Append the array and add the value. Continue the loop for range of 9.
#4. Display the values within the array by using the numpy function. Declare a
# new array and reshape the array to 3 x3 (3,3). Use a for loop to display the 
# the elements of the new array. Format the print display to remove the brackets.
#5. In the square value function, determine if an array has been create. If an 
#array has not been created, return the user to the main menu. If an array has 
#been created, use the numpy function to broadcast and reshape the array. You
# will need to declare a new array to do this. Display the new array using the 
# display array function.
#6.In the add four function, determine if the array has values. Declare a 
# new array using numpy and add 4 to the array (new_array += 4). Reshape the
# array to 3x3 and display to user using the display function.
#7. In the multiply by six function, determine if the array has values. Declare a 
# new array using numpy and multiply 6 to the array (new_array *= 6). Reshape the
# array to 3x3 and display to user using the display function.
#8. The user may exit the program or create a new array. Ensure to clear the 
# array before the user inputs values.

#Import pandas and numpy
import numpy as np
import pandas as pd

#Declare and initialize global array
arr = []


def display_array(arr):
    #Displays the array and formats to remove brackets
     for i in arr:
        for elem in i:
            print("{}".format(elem).rjust(3), end=" ")
        print(end="\n")
        

def create_array(arr):
    #Clear the array to allow the user to enter a new array
    arr.clear()
    count = 1
    x = 0
    while x < 9:
        num = (input(f"Enter integer {count}: "))
        # Determine if input is a digit
        if num.isalpha() or num == "":
            print("Invalid input! You must enter a number.")
        else:
            num = int(num)
            arr.append(num)
            x += 1
            count += 1
        
    #Declare new array using the numpy function and reshape the array to 3x3    
    new_arr = np.array(arr).reshape(3,3)  
    #Display the array to user
    display_array(new_arr)   
def square_value(arr):
    #Determine if array has values
    if len(arr) < 1:
        print("\nYou need to create an array (option 1 main menu).\n")
    else:
        #Declare new array using the numpy function
        new_array = np.array([arr])
        #Declare new array using the numpy function, multiply,and reshape the array to 3x3  
        new_array2 = np.multiply(new_array,arr).reshape(3,3)        
        #Display the array to user
        display_array(new_array2) 
    
def add_four(arr):
     #Determine if array has values
    if len(arr) < 1:
        print("\nYou need to create an array (option 1 main menu).\n")
    else:
        #Declare new array using the numpy function
        new_array = np.array([arr])
        #Add four to each value in the array
        new_array += 4
        #Declare new array using the numpy function and reshape the array to 3x3  
        new_array2 = np.array(new_array).reshape(3,3)       
        #Display the array to user
        display_array(new_array2) 
    
def multiply_by_six(arr):
     #Determine if array has values 
    if len(arr) < 1:
        print("\nYou need to create an array (option 1 main menu).\n")
    else:
        #Declare new array using the numpy function
        new_array = np.array([arr])
        #Multiply 6 by each value in the array
        new_array *= 6       
        #Declare new array using the numpy function and reshape the array to 3x3  
        new_array2 = np.array(new_array).reshape(3,3)       
        #Display the array to user
        display_array(new_array2) 
def main():
    
    #Declare and initialize sentinel
    loop = False
    
    while loop == False:
        #Display main menu
        print("MENU\n"
              "1. Create a 3-by-3 Array\n"
              "2. Display square Values for elements in array\n"
              "3. Add 4 to every element and display result\n"
              "4. Multiply elements by 6 and display result\n"
              "5. Exit\n"
              )
        #Get input from user for menu selection
        menu_choice = input("Make a selection --> ")
        if menu_choice == '1':
            #Create array function
            create_array(arr)            
        elif menu_choice == '2':
            #Square array function
            square_value(arr)  
        elif menu_choice == '3':
            #Add 4 function
            add_four(arr)  
        elif menu_choice == '4':
            #Multiply by 6 function
            multiply_by_six(arr)  
        elif menu_choice == '5':
            #End program
            loop = True
        else:
            print("Invalid selection! Try again!")
#Call main function
main()
