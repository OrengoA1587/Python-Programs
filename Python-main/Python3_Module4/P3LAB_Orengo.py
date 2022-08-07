# Enter number grade to determine letter grade
# Anthony Orengo
# 06/10/2019

# Prompt user to input number
# Determine letter grade for users input
# Display users letter grade
def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 50
    

    #Prompt user to input number grade
    score = int(input('Enter grade: '))

    # Determine which letter grade the users number is
    # Display users letter grade
    if score >= A_score:
        print('Your grade is: A')
    else:
        if score >= B_score:
            print('Your grade is: B')
        else:
            if score >= C_score:
                print('Your grade is a: C')
            else:
                if score >= D_score:
                    print('Your grade is a: D')
                else:
                    if score >= F_score:
                       print('Your grade is: F') 



# program start
main()
