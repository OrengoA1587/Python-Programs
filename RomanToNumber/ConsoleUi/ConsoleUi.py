


dict_roman = {'I':1,'IV':4,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

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

if __name__ == '__main__':     
    lst = []
    str_roman = 'MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMCMXCV'
    for letter in str_roman:
        lst.append(letter)
    #print(lst)
    print(f'Date: {Roman_Numeral(lst)}') #Display converted date to user
 

    
         

     