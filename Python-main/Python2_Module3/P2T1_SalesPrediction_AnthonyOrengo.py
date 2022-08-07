
# This program calculates projected annual profits.
# 6/15/2019
# CTI-110 P2T1-Sales Prediction
# Anthony Orengo

# 1.) Create function by defining main.
# 2.) Declare variables.
#       projected_sales = float 0.0
#       percent = float .23
# 3.) Prompt user to input projected amount of total sales.      
# 4.) Calculate projected annual profits by using:
#         total = percent * projected_sales  
# 5.) Display results.
# 6.) Return statement main()
        

# Define "main()" as a function for Sales Prediction.
def main():
    # Prompt user to input projected annual sales.
    projected_sales = float(input("Enter your projected amount of total sales: "))

    # Variable represents the typical annual profit percentage.
    percent = .23
    
    # Calculate annual profits by variable "projected sales" and variable "percent".
    total = percent * projected_sales

    # Print results of percent multiplied by projected total sales.
    #
    # "str" added for character "$" placement. Note: will change data variables to string format.
    # remove "str" and replace "+" with  "," to return string to data.
    print('Your projected annual profit is: $' + str(total))

    # Return statement
    return main()

# Start of program    
main()






