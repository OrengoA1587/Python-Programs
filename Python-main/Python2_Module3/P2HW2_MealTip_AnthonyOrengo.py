
 # This program calculates tip cost and total meal cost. 
 # 6/12/2019
 # CTI-110 P2HW2 - Meal Tip Calculator
 # Anthony Orengo

# Define main function main(). 
# Prompt user to enter meal cost.
# Set meal cost to variable "meal_cost".
# Set tip percentages to 3 separate variables "fifteen_percent, eighteen_percent, and twenty_percent".
# Set tip cost to 3 separate variables tip_15, tip_18, and tip_20.
# Calculate tip cost by multiplying variable "meal cost" by variables "fifteen_percent, eighteen_percent, and twenty_percent".
# Set total meal cost to 3 separate variables "total_15, total_18, and total_20".
# Calcultate total meal cost by adding tip percentage variables by total meal cost variable.
# Display tip cost without meal cost.
# Display total meal cost with tip included.
# Return to main with return statement "return main()".


# Define main function main(). 
def main():
    # Set meal cost variable.
    # Prompt user to input cost of meal.
    meal_cost = float(input(" Enter your meal cost:  "))

    # Set tip percentages to 3 separate variables.
    fifteen_percent = .15
    eighteen_percent = .18
    twenty_percent = .20
    
    # Calculate tip cost by multiplying percentage variables by meal cost variable.
    tip_15 = fifteen_percent * meal_cost
    tip_18 = eighteen_percent * meal_cost
    tip_20 =  twenty_percent * meal_cost
    
    # Calcultate total meal cost by adding tip cost variables by meal cost variable.
    total_15 = tip_15 + meal_cost
    total_18 = tip_18 + meal_cost
    total_20 = tip_20 + meal_cost

    # Display total cost of tip for for each percentage.
    print("                             ")
    print(" Total tip cost:")
    print("_____________________________")
    # "str" added for character "$" placement. Note: will change data variables to string format.
    # remove "str" and replace "+" with  "," to return string to data.
    print("15%: $" + str(tip_15)) 
    print("18%: $" + str(tip_18)) 
    print("20%: $" + str(tip_20))
    # Display total cost of meal with tip included.
    print("                             ")
    print(" Total meal cost with tip:")
    print("_____________________________")    
    print("15%: $" + str(total_15)) 
    print("18%: $" + str(total_18)) 
    print("20%: $" + str(total_20))
    print("                             ")

    # Restart main.
    return main()

# Main program
main()
