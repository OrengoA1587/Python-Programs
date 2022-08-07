# Total calories burned 
# 06/11/2019
# CTI-110 P4HW1 - Calories Burned
# Anthony Orengo
#

#Get specific number of calories burned per min from user
#Multiply users calories per min by 20, 35, 45
#Display total calories burned for 20, 35, 45

def main():
    
    # Prompt user to input calories burned per min
    calories = int(input("Enter your bodies calories burned per min  "))  

    # Loop displaying results for total calories burned (20, 35, 45)   
    for calories_burned in (20, 35, 45):
        print("Calories burned", calories_burned * calories)

    
    return main()
main()
