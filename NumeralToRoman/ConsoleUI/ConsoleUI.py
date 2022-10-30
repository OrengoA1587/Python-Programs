

from audioop import reverse
from datetime import date
from math import log10

 # MCMXCIV

dict_roman = {1:'I',4:'IV',5:'V',10:'X',40: 'XL',50:'L',100:'C',500:'D',1000:'M'}

def NumeralToRoman():


    return date


if __name__ == '__main__':
    #str = 'MCMXCIV'
    #date = 1994
    my_integer_input = 2014
    lst = []
    lst_convert = []
    num_dif = 0
    stored_values_thousandths = {
      1: 0, # ones spot
      2: 0, # tens spot
      3: 0, # hundres spot
      4: 0, # thousandths spot
      5: 0
    }


    for enum, value in enumerate(str(my_integer_input)[::-1], 1):
      stored_values_thousandths[enum] = int(value)       
      if enum == 1:
          lst.append(int(value) * 1)
      if enum == 2:
          lst.append(int(value) * 10)
      if enum == 3:
          lst.append(int(value) * 100)
      if enum == 4:
          lst.append(int(value) * 1000)
      if enum == 5:
          lst.append(int(value) * 10000)
    # MCMXCIV     
    lst = list(reversed(lst))
    print(lst)
    #MDCCXCIV
    for num in range (len(lst)):
        print(num)
        if lst[num] == 1000:
            lst_convert.append(dict_roman[lst[num]])
            print(lst_convert)
        elif lst[num] >= 1000:               
            num_dif = lst[num]
            print(num_dif)
            while num_dif != 0:
                lst_convert.append(dict_roman[1000])
                num_dif -= 1000
            print(lst_convert)
        elif lst[num] < 1000 and lst[num] >= 900:
            num_dif = 1000 - lst[num]
            lst_convert.append(dict_roman[num_dif] + dict_roman[1000])
            print(lst_convert)        
        elif lst[num] < 1000 and lst[num] >= 500:
             print('here')
             lst_convert.append(dict_roman[500])
             print(lst_convert)
             num_dif = lst[num] - 500
             print(num_dif)
             while num_dif != 0:
                lst_convert.append(dict_roman[100])
                num_dif -= 100                 
             print(lst_convert)
        elif lst[num] == 100:
            lst_convert.append(dict_roman[lst[num]])
            print(lst_convert)
        elif lst[num] < 100 and lst[num] >= 90:
            num_dif = 100 - lst[num]
            lst_convert.append(dict_roman[num_dif] + dict_roman[100])
            print(lst_convert)
        elif lst[num] < 100 and lst[num] >= 50:
             print('here')
             lst_convert.append(dict_roman[50])
             print(lst_convert)
             num_dif = lst[num] - 50
             print(num_dif)
             while num_dif != 0:
                lst_convert.append(dict_roman[10])
                num_dif -= 10                 
             print(lst_convert)
        #50's--------------------------------------------------------
        elif lst[num] == 50:             
            lst_convert.append(dict_roman[lst[num]])
            print(lst_convert)
        elif lst[num] < 100 and lst[num] >= 90:
            num_dif = 100 - lst[num]
            lst_convert.append(dict_roman[num_dif] + dict_roman[100])
            print(lst_convert)

        elif lst[num] == 40:
            lst_convert.append(dict_roman[40])
            print(lst_convert)
        #10's------------------------------------------------------
        elif lst[num] == 10:
            lst_convert.append(dict_roman[lst[num]])
            print(lst_convert)
        elif lst[num] < 10 and lst[num] >= 9:
            num_dif = 10 - lst[num]
            lst_convert.append(dict_roman[num_dif] + dict_roman[10])
            print(lst_convert)

        elif lst[num] < 10 and lst[num] >= 5:
             print('here')
             lst_convert.append(dict_roman[5])
             print(lst_convert)
             num_dif = lst[num] - 5
             print(num_dif)
             while num_dif != 0:
                lst_convert.append(dict_roman[1])
                num_dif -= 1                 
             print(lst_convert)
        elif lst[num] == 4:
            lst_convert.append(dict_roman[4])
            print(lst_convert)
        elif lst[num] < 4 and lst[num] > 0:
             #lst_convert.append(dict_roman[1])
             num_dif = lst[num]             
             while num_dif != 0:
                lst_convert.append(dict_roman[1])
                num_dif -= 1           
             print(lst_convert)
    final = ''.join(lst_convert)

    print(f'Roman Numeral Date: {final}')