# CTI-110 
# P3HW1 - Color Mixer 
# Anthony Orengo
# 06/11/2019



# Display color options menu
# Set colors red, yellow, blue to variables
# Prompt user to input two colors
# set color options one and two to variables.
# Determine secondary color based on users color options.
# Set "invalid selection" if user fails to choose one of the color options listed. 
# Display secondary color if user correctly choose two 


def colorMain():    
       print("Color options")
       print("1. red:")
       print("2. yellow:")
       print("3. blue:")


       # Color variables
       red = 1
       yellow = 2
       blue = 3
       # Prompt user to input two colors
       color_one = int(input(" Enter your first primary color:  "))
       color_two = int(input(" Enter your second primary color:  "))


       # If statement representing argument between two colors
       if color_one == 1 and color_two == 3 or color_two == 1 and color_one == 3:
              print("Your color is: Purple")

       else:
           if color_one == 1 and color_two == 2 or color_two == 1 and color_one == 2:
               print("Your color is: Orange")
           else:
                if color_one == 2 and color_two == 3 or color_two == 2 and color_one == 3:
                     print("Your color is: Green")
                else:
                       if color_one == 1 and color_two == 1 or color_two == 1 and color_one == 1:
                              print("The color mixer program determines secondary colors, but you decided to choose the exact same colors.")
                              print("The program will entertain your choices.")
                              print("your color is: Red")
                       else:
                              if color_one == 2 and color_two == 2 or color_two == 2 and color_one == 2:
                                     print("The color mixer program determines secondary colors, but you decided to choose the exact same colors.")
                                     print("The program will entertain your choices.")
                                     print("your color is: Yellow")
                              else:
                                     if color_one == 3 and color_two == 3 or color_two == 3 and color_one == 3:
                                            print("The color mixer program determines secondary colors, but you decided to choose the exact same colors.")
                                            print("The program will entertain your choices.")
                                            print("your color is: Blue")
                                     else:
                                            print("Invalid selection")
       # return to colorMain after selection
       return colorMain()
#Main program
colorMain()



