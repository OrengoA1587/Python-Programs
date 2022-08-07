# Carpayment formula
#
#         r * P
#   C = __________
#       1-(1+r)^-N
#     


# Declare variables
rate = 0.0
priciple = 0.0
interest = 0.0
months = -0.0
years = 0.0

# Prompt user to input loan amount, interest rate, and total years of laon.
def carpaymentCalculator():
    priciple = float(input("How much is your vehicle loan:  "))
    interest = float(input("What is your vehicle loan interest rate:  "))
    years = float(input("How many years will you be financing your vehicle:  "))

    # Total rate formula
    total_rate = (interest / 100) / 12

    # Total months formula.
    total_months = -12 * years

    # 
    top = total_rate * priciple
    #
    bottom = 1 - (1 + total_rate) ** total_months

    # Calculate total monthly payment by dividing the top against the bottom
    monthlyPayment = top / bottom

    print("Your total monthly priciple is", monthlyPayment)

carpaymentCalculator()
