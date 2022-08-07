 # This program will convert Pounds to Kilograms.
 # 06/15/2019
 # CTI-110 P2HW1 - Pounds to Kilograms Converter
 # Anthony Orengo

# 1.) Create function by defining main.
# 2.) Declare variables.
#       pounds = float 0.0
#       kilogram = float 0.0

#Prompt user to input number of pounds.
# Set number of pounds to variable "pounds".
# Set kilogram formula to variable "kilogram"(pounds / 2.2046).
# Calculate pounds to kilograms by dividing variable "pounds" by variable "kilogram".
# Display results by printing number of kilograms.
# Create "return" statement and input "main()".
# Initiate program by defining "main" function.

#Define function "main".
def main():
    #Prompt user to input number of pounds.    
    pounds = float(input("Enter number of pounds:"))

    #Calculate pounds to kilograms by multiplying variable "pounds" by variable "kilogram".
    kilogram = pounds / 2.2046

    #Display results by printing number of kilograms.
    #Note:
    #"str" added for character "$" placement. Note: will change data variables to string format.
    #remove "str" and replace "+" with  "," to return string to data.
    print("Your number is " + str(kilogram) + str('kg')) 

    #Restart program by returning to main().
    return main()

# Main program begins.
main()
 
