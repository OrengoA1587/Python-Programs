# Kilometers to miles converter
# 6/12/2019
# CTI-110 P5T1_KilometerConverter 
# Anthony Orengo


# Get input from user
# Calculate user input by multiplying input by variable "miles"
# Display results
# Return to main and wait for user input


#miles = kilometers * 0.6214
def main():
    kilometers = float(input("Enter a distance in kilometers  "))
    miles = kilometers * .6214

    print("Your distance is  ", miles, "miles")
    return main()

main()
