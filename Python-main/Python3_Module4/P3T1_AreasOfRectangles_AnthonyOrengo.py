# Calculate area of two rectangles and determine whether they
# are greater than or equal to each other.

# 6/9/2019
# CTI-110 P3T1-Areas of Rectangles
# Anthony Orengo

# Get user to enter length and width for rectangle on and two
# Calculate area of rectangle one and two by multiplying length and width
# Determine which rectangle is larger or if both are equal
# Display which rectangle is larger or if both are equal

# Prompt user to input length and width for each rectangle
def main():
    rectangleOneLength = float(input(" What is rectangle 1's length  "))
    rectangleOneWidth = float(input(" What is rectangle 1's width  "))

                                 
    rectangleTwoLength = float(input(" What is rectangle 2's length  "))
    rectangleTwoWidth = float(input(" What is rectangle 2's width  "))
    # Calculate area of rectangle one by multiplying length and width
    rectangleOneArea = rectangleOneLength * rectangleOneWidth

    # Calculate area of rectangle two by multiplying length and width
    rectangleTwoArea = rectangleTwoLength * rectangleTwoWidth

    # Display results of rectangle one and two
    print( " The area of rectangle one is  ", rectangleOneArea)
    print( " The area of rectangle two is  ", rectangleTwoArea)

    # If statement comparing which rectangle is larger or if both are equal
    # Display results of larger rectangle or if both are equal
    if rectangleOneArea > rectangleTwoArea:
    
        print("rectangle one is larger")
    else:    
      
         if rectangleTwoArea > rectangleOneArea:
            print("rectangle two is larger")
         else:
               if rectangleOneArea == rectangleTwoArea:
                    print("Both rectangles have equal area")
    # Return to main statement
    return main()
# Start of main
main()

                
