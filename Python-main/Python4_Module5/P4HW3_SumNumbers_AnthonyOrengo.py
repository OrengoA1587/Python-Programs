# Determine number of bugs collected for five days
# 06/10/2019
# CTI-110 P4T2 - Bug Collector
# Anthony Orengo
def main():
      
      hours = int(input("Enter hours  "))
      speed = int(input("What is the speed of your vehicle  "))
      distance = speed * hours
      total = 0.0
      print("Hour           Distance Traveled")
      print("--------------------------------")
      for counter in range(hours):
            print(counter,"                  ", speed,)

      total = total + distance
      print("The total miles driven are", total)
      return main()

main()

    

    
    


    

    

