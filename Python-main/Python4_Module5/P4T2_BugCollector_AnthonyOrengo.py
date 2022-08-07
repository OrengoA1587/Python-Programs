# Determine number of bugs collected for five days
# 06/10/2019
# CTI-110 P4T2 - Bug Collector
# Anthony Orengo

def main():
    # Set sccumulator
    total = 0

    # Prompt user to input number of bugs collected
    for day in range(1, 6):
        print("Enter number of bugs collected on day", day)
        #User inputs number of bugs collected
        bugs = int(input())
        #Calculate total number of bugs collected
        total += bugs

    #Display the total number of bugs collected for five days
    print("You collected a total of", total, "bugs")

    
main()
exit(1)


    

    

