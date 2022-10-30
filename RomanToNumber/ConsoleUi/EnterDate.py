

def NumeralToRoman():
    #Hard Coded cannot be changed
    dict_roman = {1:'I',4:'IV',5:'V',10:'X',40: 'XL',50:'L',100:'C',500:'D',1000:'M'}  
    stored_values_thousandths = {
      1: 0, # ones spot
      2: 0, # tens spot
      3: 0, # hundres spot
      4: 0, # thousandths spot
      5: 0
    }
    #--------------------------------------------------------------------------------
    loop_input = ''
    loop = False
    while loop == False:
        lst = []
        lst_convert = []
        num_dif = 0
        date_input = input("Enter Date -> ")
        if date_input.isdigit():
            for enum, value in enumerate(str(date_input)[::-1], 1):
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
            lst = list(reversed(lst))        
            for num in range (len(lst)):
            
                if lst[num] == 1000:
                    lst_convert.append(dict_roman[lst[num]])                
                elif lst[num] >= 1000:               
                    num_dif = lst[num]               
                    while num_dif != 0:
                        lst_convert.append(dict_roman[1000])
                        num_dif -= 1000                
                elif lst[num] < 1000 and lst[num] >= 900:
                    num_dif = 1000 - lst[num]
                    lst_convert.append(dict_roman[num_dif] + dict_roman[1000])
                      
                elif lst[num] < 1000 and lst[num] >= 500:                 
                     lst_convert.append(dict_roman[500])                 
                     num_dif = lst[num] - 500                 
                     while num_dif != 0:
                        lst_convert.append(dict_roman[100])
                        num_dif -= 100                 
                elif lst[num] == 100:
                    lst_convert.append(dict_roman[lst[num]])
                
                elif lst[num] < 100 and lst[num] >= 90:
                    num_dif = 100 - lst[num]
                    lst_convert.append(dict_roman[num_dif] + dict_roman[100])
                
                elif lst[num] < 100 and lst[num] >= 50:             
                     lst_convert.append(dict_roman[50])
                 
                     num_dif = lst[num] - 50
                 
                     while num_dif != 0:
                        lst_convert.append(dict_roman[10])
                        num_dif -= 10                 
               
                #50's--------------------------------------------------------
                elif lst[num] == 50:             
                    lst_convert.append(dict_roman[lst[num]])
                
                elif lst[num] < 100 and lst[num] >= 90:
                    num_dif = 100 - lst[num]
                    lst_convert.append(dict_roman[num_dif] + dict_roman[100])
               

                elif lst[num] == 40:
                    lst_convert.append(dict_roman[40])
                
                #10's------------------------------------------------------
                elif lst[num] == 10:
                    lst_convert.append(dict_roman[lst[num]])
                
                elif lst[num] < 10 and lst[num] >= 9:
                    num_dif = 10 - lst[num]
                    lst_convert.append(dict_roman[num_dif] + dict_roman[10])
               

                elif lst[num] < 10 and lst[num] >= 5:
                 
                     lst_convert.append(dict_roman[5])
                 
                     num_dif = lst[num] - 5
                 
                     while num_dif != 0:
                        lst_convert.append(dict_roman[1])
                        num_dif -= 1                 
                
                elif lst[num] == 4:
                    lst_convert.append(dict_roman[4])
                
                elif lst[num] < 4 and lst[num] > 0:
                     #lst_convert.append(dict_roman[1])
                     num_dif = lst[num]             
                     while num_dif != 0:
                        lst_convert.append(dict_roman[1])
                        num_dif -= 1          
                 
            final = ''.join(lst_convert)

            print(f'\nRoman Numeral Date: {final}\n')
            loop_input = input('Would you like to enter another? y/n')
            if loop_input.upper() == 'Y':
                loop = False
            elif loop_input.upper() == 'N':
                loop = True
            else:
                print('Invalid input!')
        else:
            print('Invalid input!')
