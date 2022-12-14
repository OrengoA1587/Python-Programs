
import RomanLibrary as RL
import RomanToNumeral as RTN
import EnterDate as ED
dict_roman = {'I':1,'IV':4,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'MTV': 4000, 'IVT':5000, 'XT':10000}

def Roman_Numeral(lst):

    lst_convert = [] # used to store converted roman numerals to numbers
    date = 0 # date counter 
    for letter in lst:
        lst_convert.append(dict_roman[letter])# Convert roman to numeral using dictionary
    lst_convert.append(0) #Add to end of list to prevent index out of range     
    #print(lst_convert)#Display list for debugging purposes

    for num in range (len(lst_convert) - 1):         
        if lst_convert[num] == 0:            
            return date
        elif lst_convert[num] >= lst_convert[num + 1]:
            date += lst_convert[num]           
        elif lst_convert[num] < lst_convert[num +1]:
            date += lst_convert[num + 1] - lst_convert[num]            
            lst_convert.remove(lst_convert[num + 1])
    return date 


def main():
    menu_loop = False

    while menu_loop == False: 

        choice = input(RL.MainMenu())
         
        if choice == '1':
            RTN.EnterRoman()
        elif choice == '2':
            ED.NumeralToRoman()
        elif choice == '3':
            menu_loop = True
        else:
            print("Invalid Selection!")


if __name__ == '__main__':     
      
    main()

    
         

     