# Description: This program uses a for loop to display the same elements in the table using less
# lines of code.
# Date: 05/25/2021
# Program: CSC121 M1Lab– Debugging
# Programmer: Anthony Orengo
# Exercise 3.7



# Pseudocode 
# 1. Declare variable "i" and initialize to "0".
# 2. Declare for loop and set range to "6".
# 3. Add print line and replace 0-5 with variable "i" Ex. change "print(0, '\t', 0 ** 2, '\t', 0 ** 3)" to  "print(i, '\t', i ** 2, '\t', i ** 3)".
# 4. Increment loop using "i+=1".
# 5. Run program and view output to verify if both methos are the same.
#----------------------------------------------------------------------------------------------------------------------------------------------------//

# Declare and initialize loop variable
i = 0; 

# Display table title
print('number\t square\t cube')
# For loop to display table elements
for i in range(6):
    print(i, '\t', i ** 2, '\t', i ** 3)
    i+=1

input('\n\nPress ENTER to exit')  








##########################################################################
# (C) Copyright 2019 by Deitel & Associates, Inc. and                    #
# Pearson Education, Inc. All Rights Reserved.                           #
#                                                                        #
# DISCLAIMER: The authors and publisher of this book have used their     #
# best efforts in preparing the book. These efforts include the          #
# development, research, and testing of the theories and programs        #
# to determine their effectiveness. The authors and publisher make       #
# no warranty of any kind, expressed or implied, with regard to these    #
# programs or to the documentation contained in these books. The authors #
# and publisher shall not be liable in any event for incidental or       #
# consequential damages in connection with, or arising out of, the       #
# furnishing, performance, or use of these programs.                     #
##########################################################################
