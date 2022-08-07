

import random

number = random.randint(1, 100)
    
guess = 0    
count = 0


while guess == 0:
    count +=1
    user_num = int(input("Guess the random number:  "))
    if user_num > number: 
             print("Too high, try again")
          
    elif user_num < number:
            print("Too low, try again")
                  
    elif user_num == number:
            print("Congratulations! You guessed right")
            print("Number of Attempts: ", count)



