# CTI-110 
# P3HW2 - MealTipTax 
# Anthony Orengo
# 06/10/2019
#


# Prompt user to enter meal cost
# Calculate tip cost by multiplying meal cost by gratuity percentages (15, 18, 20)
# Display tip cost for percentages 15, 18, 20
# Calcultate total meal cost by adding meal cost tip cost
# Display total meal cost with different tip percentages (15, 18 , 20)

# Beginning of main program
def main():
    # Variables representing various percentages
    fifteen_percent = .15
    eighteen_percent = .18
    twenty_percent = .20

    # Prompt user to input cost of meal
    meal_cost = int(input(" Enter your meal cost  "))

    # Display menu representing user options for 15%, 18%, 20%
    print("Meal tip options")
    print("15")
    print("18")
    print("20")

    # Prompt user to input tip percentage
    meal_tip = float(input("Choose your gratuity  "))

    # Meal tax formula 7% sales tax multiplied by meal cost.
    meal_tax = meal_cost * .07 + meal_cost

    # Statement representing calculation for tip, tax, and meal cost.
    # Display total cost of meal to include sales tax and tip.
    # Invalid "Error", if other than the tip percentages displayed.
    if meal_tip == 15:
        print("Your total meal cost is", "$",meal_tax * fifteen_percent + meal_tax)
    else:
        if meal_tip == 18:
            print("Your total meal cost is", "$",meal_tax * eighteen_percent + meal_tax)
        else:
            if meal_tip == 20:
                print("Your total meal cost is", "$",meal_tax * twenty_percent + meal_tax)
            else:
                print("Error! Invalid tip percentage")
    # Return to main statement (restart program)
    return main()

# Main program starts
main()
