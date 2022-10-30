


import RomanLibrary as RL

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


menu_loop = False
def EnterRoman():
    loop_input = ''
    loop = False
    while loop == False:
        lst = []
        str_roman = input("Enter Roman Numeral: ")
        str_roman = str_roman.upper()
        invalid_roman = False
        for letter in str_roman:
            if letter in dict_roman:
                lst.append(letter)
            else:                
                invalid_roman = True
        if invalid_roman == False:
            print(f'Date: {Roman_Numeral(lst)}') #Display converted date to user
            loop_input = input('Would you like to enter another? y/n')
            if loop_input.upper() == 'Y':
                loop = False
            elif loop_input.upper() == 'N':
                loop = True
            else:
                print('Invalid input!')
        else:
            print("Invalid Characters!")