#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
 
"""
Created on Tue Jun  1 12:07:19 2021

@author: orengoa0459
"""

import random
import sys
import os

class MathProblemFunctions():

    # Displays correct response////////////////////////////////////////////////
    staticmethod(0)
    def correct_answer_response(response):
        
        #Response strings 
        response = ""
        responseOne = "Very Good!"
        responseTwo = "Nice Work!"
        responseThree = "Keep up the good work!"
        
        
        #Create random object
        responseNum = random.randrange(1,4)
        if responseNum == 1:
            response = responseOne
            print(response)
        elif responseNum == 2:
            response = responseTwo
            print(response)
        elif responseNum == 3:
            response = responseThree
            print(response)
    # Displays incorrect response//////////////////////////////////////////////
    staticmethod(0)
    def incorrect_answer_response(response):
        
        #Response strings 
        response = ""
        responseOne = "You can do it!"
        responseTwo = "It's Ok, try again!"
        responseThree = "Keep trying! I know you can get the answer!"
        
        
        #Create random object
        responseNum = random.randrange(1,4)
        if responseNum == 1:
            response = responseOne
            print(response)
        elif responseNum == 2:
            response = responseTwo
            print(response)
        elif responseNum == 3:
            response = responseThree
            print(response)        
        # multiplication_problem_level_1/////////////////////////////////////
    def invalidNumberInput():
            print("Invalid Input! You must enter a number!")

    def multiplication_beginner_level_1():

        #Declare and initialize variable
        score = 0       
        loop = 0

        while loop < 10:
            # Declare and initialize loop variables
            response = ""
            count = 0
            retry_loop = False
            num_one = random.randrange(1,5)
            num_two = random.randrange(1,5)
            answer = num_one * num_two
            answer = str(answer)

            #Get input from user----------------------------------
            print("\nHow much is", num_one, "times {}?" .format(num_two))
            choice = input("Enter Answer: ")

            #Determine if user "choice" equals answer
            if choice == answer:
                #Increment players score
                score += 1
                #Displays positive correct message
                MathProblemFunctions.correct_answer_response(response)
            #If response is not correct, user will prompted to answer again
            elif choice != answer:
                # Displays positive incorrect message
                MathProblemFunctions.incorrect_answer_response(response)
                #Increment number of tries
                count += 1
                #Intiate loop loop until user answers correctly or exceeds number of tries
                while retry_loop == False:
                    #Get input from user
                    print("\nHow much is", num_one, "times {}?" .format(num_two))
                    choice = input("Enter Answer: ")
                    if choice == answer:
                        # Displays positive correct message
                        MathProblemFunctions.correct_answer_response(response)
                        # Increment players score
                        score += 1
                        #Exits loop to next question
                        retry_loop = True
                    elif choice != answer and choice.isalpha() and count < 3:
                        print(MathProblemFunctions.invalidNumberInput())
                        # Increment number of tries
                        count += 1
                    elif choice != answer and count < 2:
                        MathProblemFunctions.incorrect_answer_response(response)
                        # Increment number of tries
                        count += 1
                    elif count >= 2:
                        #Displays failed message to user
                        print("Sorry but you failed to answer correctly!\n" +
                              "The correct answer is: ", answer, "\n")
                        retry_loop = True
                    else:
                        #Displays incorrect reponse
                        print("Incorrect Response! ")
            else:
                # Displays incorrect reponse
                print("Incorrect Response! ")  
            #Increments loop until 10 iterations are complete
            loop += 1

        #Displays players score
        print("\n\nYou scored ",score, "out of 10")
        if score == 10:
            print("Great Job! You scored a perfect score...")
        elif score >=8 and score < 10:
            print("Good Job! You almost scored perfectly...")
        elif score > 5 and score <= 7:
            print("Good Job! You multiplication skills are average...")
        elif score > 3 and score < 5:
            print("Ok job! You need some work...")
        elif score < 3:
            print("Keep studying and you will get better!\n\n")

     #End multiplication_problem_level_1/////////////////////////////////////
     # multiplication_problem_level_2/////////////////////////////////////
    def multiplication_beginner_level_2():
        # Declare and initialize variable
        score = 0
        loop = 0

        while loop < 10:
            # Declare and initialize loop variables
            response = ""
            count = 0
            retry_loop = False
            num_one = random.randrange(1, 6)
            num_two = random.randrange(1, 6)
            answer = num_one * num_two
            answer = str(answer)

            # Get input from user----------------------------------
            print("\nHow much is", num_one, "times {}?" .format(num_two))
            choice = input("Enter Answer: ")

            # Determine if user "choice" equals answer
            if choice == answer:
                # Increment players score
                score += 1
                # Displays positive correct message
                MathProblemFunctions.correct_answer_response(response)
            # If response is not correct, user will prompted to answer again
            elif choice != answer:
                # Displays positive incorrect message
                MathProblemFunctions.incorrect_answer_response(response)
                # Increment number of tries
                count += 1
                # Intiate loop loop until user answers correctly or exceeds number of tries
                while retry_loop == False:
                    # Get input from user
                    print("\nHow much is", num_one, "times {}?" .format(num_two))
                    choice = input("Enter Answer: ")
                    if choice == answer:
                        # Displays positive correct message
                        MathProblemFunctions.correct_answer_response(response)
                        # Increment players score
                        score += 1
                        # Exits loop to next question
                        retry_loop = True
                    elif choice != answer and choice.isalpha() and count < 3:
                        print(MathProblemFunctions.invalidNumberInput())
                        # Increment number of tries
                        count += 1
                    elif choice != answer and count < 2:
                        MathProblemFunctions.incorrect_answer_response(response)
                        # Increment number of tries
                        count += 1
                    elif count >= 2:
                        # Displays failed message to user
                        print("Sorry but you failed to answer correctly!\n" +
                              "The correct answer is: ", answer, "\n")
                        retry_loop = True
                    else:
                        # Displays incorrect reponse
                        print("Incorrect Response! ")
            else:
                # Displays incorrect reponse
                print("Incorrect Response! ")
                # Increments loop until 10 iterations are complete
            loop += 1

        # Displays players score
        print("\n\nYou scored ", score, "out of 10")
        if score == 10:
            print("Great Job! You scored a perfect score...")
        elif score >= 8 and score < 10:
            print("Good Job! You almost scored perfectly...")
        elif score > 5 and score <= 7:
            print("Good Job! You multiplication skills are average...")
        elif score > 3 and score < 5:
            print("Ok job! You need some work...")
        elif score < 3:
            print("Keep studying and you will get better!\n\n")

     #End multiplication_problem_level_2/////////////////////////////////////
      # multiplication_problem_level_3/////////////////////////////////////
    def multiplication_beginner_level_3():
        # Declare and initialize variable
        score = 0
        loop = 0

        while loop < 10:
            # Declare and initialize loop variables
            response = ""
            count = 0
            retry_loop = False
            num_one = random.randrange(1, 7)
            num_two = random.randrange(1, 7)
            answer = num_one * num_two
            answer = str(answer)

            # Get input from user----------------------------------
            print("\nHow much is", num_one, "times {}?" .format(num_two))
            choice = input("Enter Answer: ")

            # Determine if user "choice" equals answer
            if choice == answer:
                # Increment players score
                score += 1
                # Displays positive correct message
                MathProblemFunctions.correct_answer_response(response)
            # If response is not correct, user will prompted to answer again
            elif choice != answer:
                # Displays positive incorrect message
                MathProblemFunctions.incorrect_answer_response(response)
                # Increment number of tries
                count += 1
                # Intiate loop loop until user answers correctly or exceeds number of tries
                while retry_loop == False:
                    # Get input from user
                    print("\nHow much is", num_one, "times {}?" .format(num_two))
                    choice = input("Enter Answer: ")
                    if choice == answer:
                        # Displays positive correct message
                        MathProblemFunctions.correct_answer_response(response)
                        # Increment players score
                        score += 1
                        # Exits loop to next question
                        retry_loop = True
                    elif choice != answer and choice.isalpha() and count < 3:
                        print(MathProblemFunctions.invalidNumberInput())
                        # Increment number of tries
                        count += 1
                    elif choice != answer and count < 2:
                        MathProblemFunctions.incorrect_answer_response(response)
                        # Increment number of tries
                        count += 1
                    elif count >= 2:
                        # Displays failed message to user
                        print("Sorry but you failed to answer correctly!\n" +
                              "The correct answer is: ", answer, "\n")
                        retry_loop = True
                    else:
                        # Displays incorrect reponse
                        print("Incorrect Response! ")
            else:
                # Displays incorrect reponse
                print("Incorrect Response! ")
                # Increments loop until 10 iterations are complete
            loop += 1

        # Displays players score
        print("\n\nYou scored ", score, "out of 10")
        if score == 10:
            print("Great Job! You scored a perfect score...")
        elif score >= 8 and score < 10:
            print("Good Job! You almost scored perfectly...")
        elif score > 5 and score <= 7:
            print("Good Job! You multiplication skills are average...")
        elif score > 3 and score < 5:
            print("Ok job! You need some work...")
        elif score < 3:
            print("Keep studying and you will get better!\n\n")

     #End multiplication_problem_level_3///////////////////////////////////////////////

#Beginning of Intermediate math problems. Players will be given less tries to get the answer correctly
     # multiplication_problem_intermediate_level_1/////////////////////////////////////
    def multiplication_intermediate_level_1():
        # Declare and initialize variable
        score = 0
        loop = 0

        while loop < 10:
            # Declare and initialize loop variables
            response = ""
            count = 0
            retry_loop = False
            num_one = random.randrange(1, 10)
            num_two = random.randrange(1, 10)
            answer = num_one * num_two
            answer = str(answer)

            # Get input from user----------------------------------
            print("\nHow much is", num_one, "times {}?" .format(num_two))
            choice = input("Enter Answer: ")

            # Determine if user "choice" equals answer
            if choice == answer:
                # Increment players score
                score += 1
                # Displays positive correct message
                MathProblemFunctions.correct_answer_response(response)
            # If response is not correct, user will prompted to answer again
            elif choice != answer:
                # Displays positive incorrect message
                MathProblemFunctions.incorrect_answer_response(response)
                # Increment number of tries
                count += 1
                # Intiate loop loop until user answers correctly or exceeds number of tries
                while retry_loop == False:
                    # Get input from user
                    print("\nHow much is", num_one, "times {}?" .format(num_two))
                    choice = input("Enter Answer: ")
                    if choice == answer:
                        # Displays positive correct message
                        MathProblemFunctions.correct_answer_response(response)
                        # Increment players score
                        score += 1
                        # Exits loop to next question
                        retry_loop = True
                    elif choice != answer and choice.isalpha() and count < 1:
                        print(MathProblemFunctions.invalidNumberInput())
                        # Increment number of tries
                        count += 1
                    elif choice != answer and count < 1:
                        MathProblemFunctions.incorrect_answer_response(response)
                        # Increment number of tries
                        count += 1
                    elif count >= 1:
                        # Displays failed message to user
                        print("Sorry but you failed to answer correctly!\n" +
                              "The correct answer is: ", answer, "\n")
                        retry_loop = True
                    else:
                        # Displays incorrect reponse
                        print("Incorrect Response! ")
            else:
                # Displays incorrect reponse
                print("Incorrect Response! ")
                # Increments loop until 10 iterations are complete
            loop += 1

        # Displays players score
        print("\n\nYou scored ", score, "out of 10")
        if score == 10:
            print("Great Job! You scored a perfect score...")
        elif score >= 8 and score < 10:
            print("Good Job! You almost scored perfectly...")
        elif score > 5 and score <= 7:
            print("Good Job! You multiplication skills are average...")
        elif score > 3 and score < 5:
            print("Ok job! You need some work...")
        elif score < 3:
            print("Keep studying and you will get better!\n\n")

     #End multiplication_problem_level_intermediate/////////////////////////////////////
        # multiplication_problem_intermediate_level_1/////////////////////////////////////
    def multiplication_intermediate_level_2():        
            # Declare and initialize variable
            score = 0
            loop = 0

            while loop < 10:
                # Declare and initialize loop variables
                response = ""
                count = 0
                retry_loop = False
                num_one = random.randrange(1, 15)
                num_two = random.randrange(1, 15)
                answer = num_one * num_two
                answer = str(answer)

                # Get input from user----------------------------------
                print("\nHow much is", num_one, "times {}?" .format(num_two))
                choice = input("Enter Answer: ")

                # Determine if user "choice" equals answer
                if choice == answer:
                    # Increment players score
                    score += 1
                    # Displays positive correct message
                    MathProblemFunctions.correct_answer_response(response)
                # If response is not correct, user will prompted to answer again
                elif choice != answer:
                    # Displays positive incorrect message
                    MathProblemFunctions.incorrect_answer_response(response)
                    # Increment number of tries
                    count += 1
                    # Intiate loop loop until user answers correctly or exceeds number of tries
                    while retry_loop == False:
                        # Get input from user
                        print("\nHow much is", num_one, "times {}?" .format(num_two))
                        choice = input("Enter Answer: ")
                        if choice == answer:
                            # Displays positive correct message
                            MathProblemFunctions.correct_answer_response(response)
                            # Increment players score
                            score += 1
                            # Exits loop to next question
                            retry_loop = True
                        elif choice != answer and choice.isalpha() and count < 1:
                            print(MathProblemFunctions.invalidNumberInput())
                            # Increment number of tries
                            count += 1
                        elif choice != answer and count < 1:
                            MathProblemFunctions.incorrect_answer_response(response)
                            # Increment number of tries
                            count += 1
                        elif count >= 1:
                            # Displays failed message to user
                            print("Sorry but you failed to answer correctly!\n" +
                                  "The correct answer is: ", answer, "\n")
                            retry_loop = True
                        else:
                            # Displays incorrect reponse
                            print("Incorrect Response! ")
                else:
                    # Displays incorrect reponse
                    print("Incorrect Response! ")
                    # Increments loop until 10 iterations are complete
                loop += 1

            # Displays players score
            print("\n\nYou scored ", score, "out of 10")
            if score == 10:
                print("Great Job! You scored a perfect score...")
            elif score >= 8 and score < 10:
                print("Good Job! You almost scored perfectly...")
            elif score > 5 and score <= 7:
                print("Good Job! You multiplication skills are average...")
            elif score > 3 and score < 5:
                print("Ok job! You need some work...")
            elif score < 3:
                print("Keep studying and you will get better!\n\n")

        # End multiplication_problem_level_intermediate_level_2/////////////////////////////////////
    # multiplication_problem_intermediate_level_3/////////////////////////////////////
    def multiplication_intermediate_level_3():
            # Declare and initialize variable
            score = 0
            loop = 0

            while loop < 10:
                # Declare and initialize loop variables
                response = ""
                count = 0
                retry_loop = False
                num_one = random.randrange(1, 20)
                num_two = random.randrange(1, 20)
                answer = num_one * num_two
                answer = str(answer)

                # Get input from user----------------------------------
                print("\nHow much is", num_one, "times {}?" .format(num_two))
                choice = input("Enter Answer: ")

                # Determine if user "choice" equals answer
                if choice == answer:
                    # Increment players score
                    score += 1
                    # Displays positive correct message
                    MathProblemFunctions.correct_answer_response(response)
                # If response is not correct, user will prompted to answer again
                elif choice != answer:
                    # Displays positive incorrect message
                    MathProblemFunctions.incorrect_answer_response(response)
                    # Increment number of tries
                    count += 1
                    # Intiate loop loop until user answers correctly or exceeds number of tries
                    while retry_loop == False:
                        # Get input from user
                        print("\nHow much is", num_one, "times {}?" .format(num_two))
                        choice = input("Enter Answer: ")
                        if choice == answer:
                            # Displays positive correct message
                            MathProblemFunctions.correct_answer_response(response)
                            # Increment players score
                            score += 1
                            # Exits loop to next question
                            retry_loop = True
                        elif choice != answer and choice.isalpha() and count < 0:
                            print(MathProblemFunctions.invalidNumberInput())
                            # Increment number of tries
                            count += 1
                        elif choice != answer and count < 0:
                            MathProblemFunctions.incorrect_answer_response(response)
                            # Increment number of tries
                            count += 1
                        elif count >= 0:
                            # Displays failed message to user
                            print("Sorry but you failed to answer correctly!\n" +
                                  "The correct answer is: ", answer, "\n")
                            retry_loop = True
                        else:
                            # Displays incorrect reponse
                            print("Incorrect Response! ")
                else:
                    # Displays incorrect reponse
                    print("Incorrect Response! ")
                    # Increments loop until 10 iterations are complete
                loop += 1

            # Displays players score
            print("\n\nYou scored ", score, "out of 10")
            if score == 10:
                print("Great Job! You scored a perfect score...")
            elif score >= 8 and score < 10:
                print("Good Job! You almost scored perfectly...")
            elif score > 5 and score <= 7:
                print("Good Job! You multiplication skills are average...")
            elif score > 3 and score < 5:
                print("Ok job! You need some work...")
            elif score < 3:
                print("Keep studying and you will get better!\n\n")
    # End multiplication_problem_level_intermediate_level)3/////////////////////////////////////
    # Beginning of expert math problems. Players will be given less tries to get the answer correctly
    # multiplication_problem_expert_level11/////////////////////////////////////
    def multiplication_expert_level_1():
        # Declare and initialize variable
            score = 0
            loop = 0

            while loop < 10:
                # Declare and initialize loop variables
                response = ""
                count = 0
                retry_loop = False
                num_one = random.randrange(1, 50)
                num_two = random.randrange(1, 50)
                answer = num_one * num_two
                answer = str(answer)

                # Get input from user----------------------------------
                print("\nHow much is", num_one, "times {}?" .format(num_two))
                choice = input("Enter Answer: ")

                # Determine if user "choice" equals answer
                if choice == answer:
                    # Increment players score
                    score += 1
                    # Displays positive correct message
                    MathProblemFunctions.correct_answer_response(response)
                # If response is not correct, user will prompted to answer again
                elif choice != answer:
                    # Displays positive incorrect message
                    print("Incorrect answer! I am sure you will get the next one!")                 
                else:
                    # Displays incorrect reponse
                    print("Incorrect Response! ")
                    # Increments loop until 10 iterations are complete
                loop += 1

            # Displays players score
            print("\n\nYou scored ", score, "out of 10")
            if score == 10:
                print("Great Job! You scored a perfect score...")
            elif score >= 8 and score < 10:
                print("Good Job! You almost scored perfectly...")
            elif score > 5 and score <= 7:
                print("Good Job! You multiplication skills are average...")
            elif score > 3 and score < 5:
                print("Ok job! You need some work...")
            elif score < 3:
                print("Keep studying and you will get better!\n\n")

    # End multiplication_problem_level_intermediate_level1/////////////////////////////////////
    # multiplication_problem_expert_level2/////////////////////////////////////
    def multiplication_expert_level_2():
            # Declare and initialize variable
            score = 0
            loop = 0

            while loop < 10:
                # Declare and initialize loop variables
                response = ""
                count = 0
                retry_loop = False
                num_one = random.randrange(1, 100)
                num_two = random.randrange(1, 100)
                answer = num_one * num_two
                answer = str(answer)

                # Get input from user----------------------------------
                print("\nHow much is", num_one, "times {}?" .format(num_two))
                choice = input("Enter Answer: ")

                # Determine if user "choice" equals answer
                if choice == answer:
                    # Increment players score
                    score += 1
                    # Displays positive correct message
                    MathProblemFunctions.correct_answer_response(response)
                # If response is not correct, user will prompted to answer again
                elif choice != answer:
                    # Displays positive incorrect message
                    print("Incorrect answer! I am sure you will get the next one!")                   
                     
                else:
                    # Displays incorrect reponse
                    print("Incorrect Response! ")
                    # Increments loop until 10 iterations are complete
                loop += 1

            # Displays players score
            print("\n\nYou scored ", score, "out of 10")
            if score == 10:
                print("Great Job! You scored a perfect score...")
            elif score >= 8 and score < 10:
                print("Good Job! You almost scored perfectly...")
            elif score > 5 and score <= 7:
                print("Good Job! You multiplication skills are average...")
            elif score > 3 and score < 5:
                print("Ok job! You need some work...")
            elif score < 3:
                print("Keep studying and you will get better!\n\n")

    # End multiplication_problem_expert_level2/////////////////////////////////////
    # multiplication_problem_expert_level 3/////////////////////////////////////
    def multiplication_expert_level_3():
            # Declare and initialize variable
            score = 0
            loop = 0

            while loop < 10:
                # Declare and initialize loop variables
                response = ""
                count = 0
                retry_loop = False
                num_one = random.randrange(1, 1000)
                num_two = random.randrange(1, 1000)
                answer = num_one * num_two
                answer = str(answer)

                # Get input from user----------------------------------
                print("\nHow much is", num_one, "times {}?" .format(num_two))
                choice = input("Enter Answer: ")

                # Determine if user "choice" equals answer
                if choice == answer:
                    # Increment players score
                    score += 1
                    # Displays positive correct message
                    MathProblemFunctions.correct_answer_response(response)
                # If response is not correct, user will prompted to answer again
                elif choice != answer:
                    # Displays positive incorrect message
                    print("Incorrect answer! I am sure you will get the next one!")
                    
                else:
                    # Displays incorrect reponse
                    print("Incorrect Response! ")
                    # Increments loop until 10 iterations are complete
                loop += 1

            # Displays players score
            print("\n\nYou scored", score, "out of 10")
            if score == 10:
                print("Great Job! You scored a perfect score...")
            elif score >= 8 and score < 10:
                print("Good Job! You almost scored perfectly...")
            elif score > 5 and score <= 7:
                print("Good Job! You multiplication skills are average...")
            elif score > 3 and score < 5:
                print("Ok job! You need some work...")
            elif score < 3:
                print("Keep studying and you will get better!\n\n")

    # End multiplication_problem_expert_level 3/////////////////////////////////////
