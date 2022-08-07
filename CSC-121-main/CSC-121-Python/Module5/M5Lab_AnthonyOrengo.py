 
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 18:38:37 2021

@author: Anthony
"""

# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 12:02:17 2021

@author: orengoa0459
"""

# This program allows the user to input student grade information and
#displays it in dataframe frame.
# 06/24/2021
# CSC121 M5Lab – DataFrame
# Anthony Orengo


#Pseudocode
#1. Declare two functions called main and get student grades.
#2. Create a user menu in the main function, that has two options(1.Student Grades 2.Exit)
#3. In the get student grades function, declare a list for student grades.
#4. Get number of test types.
#5. Get user to input the name of each test (Math,Science,English, etc.).
#6. Get user to input the number of students.
#7. Get user to enter in the first students name, followed by the grade for each test.
#Repeat until all students are entered.
#8. Convert dictionary data to dataframe by using pandas. 
#9. Update index names to the tests name
#10. Display completed dataframe to the user.


import numpy as np
import pandas as pd
from io import StringIO

#Declare dictionary and test name list
grades_dict = {}
test_name_list = [] 


def get_student_grades(grades_dict):
    #Reset dictionary and list to allow user to enter more
    grades_dict.clear()
    test_name_list.clear()
    x = False
    y = False
    #Decleare and initialize student grades list
    student_grade_list = np.array
    
    while x == False:
        #Get number of test from user
        test_num = input("Enter number of test types(Math,Science,English, etc... --> ")
        #Determine if input is digit
        if(test_num.isalpha()):
            print("Invalid choice! You must enter a number.")        
        else:
           
            test_num = int(test_num) 
    
            #Get Dataframe index names
            for x in range(test_num):
                test_name = input(f"Enter test name {x + 1} --> ")
                test_name_list.append(test_name)      
            while y == False:
                #Get total number of students  
                total_students = input("Enter number of students --> ")  
                #Determine if input is digit
                if total_students.isalpha():
                    print("Invalid choice! You must enter a number.")
                else:
            
                    total_students = int(total_students) 
                    #Get student information 
                    for x in range(total_students):               
                        student_name = input(f"Enter student {x + 1} name --> ")  
                        #Create empty list for student name
                        grades_dict[student_name] = []
                        #Enter student grades for each test
                        for i in range(test_num):
                            student_grade = input(f"Enter students {test_name_list[i]} grade --> ")
                            #Add grades to list
                            grades_dict[student_name].append(student_grade) 
                    x = True
                    y = True
    #Convert dictionary to dataframe using pandas
    gradesDF = pd.DataFrame(grades_dict)
    #Establish index names     
    gradesDF.index = [test_name_list]
    #Display dataframe to user
    print(gradesDF)

def main():
    #Declare and initialize sentinel
    loop = False
    
    while loop == False:
        #Display main menu
        print("MENU\n"
              "1. Enter Student Grades\n"
              "2. Exit\n"
              )
        menu_choice = input("Make a selection --> ")
        if menu_choice == '1':
            #Get student grades
            get_student_grades(grades_dict)
        elif menu_choice == '2':
            #End program
            loop = True
        else:
            print("Invalid selection! Try again!")
#Call main function
main()































