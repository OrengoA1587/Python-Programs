 

def make_field(content,length):

  content = str(content)
  end_adjust = 1  
  if len(content) <= length - 2:      

      append_num = (length - len(content))# 
      append_num -= end_adjust
      pre_adjust = append_num + len(content)
      
      string_revised = content.rjust(pre_adjust) #Append string from the left
      string_revised = string_revised.ljust((append_num + 1) + len(content)) # Prepend beginning of string from the right
      
      return (f'|{string_revised}|') #return result to user

  else: #len(content) > length - 2:     
      x = length - 2 
      string = content[:x] #Reduce string down to length - 2. Ex. If length = 5 then x = 5 - 2. x = 3

      append_num = len(content) - (length -2) #ex. append_num = content length (5) - (length(5) - 2) = 2
      append_num -= end_adjust #Take away 1 to account for the left adjustment
      string_revised = string.ljust(x + end_adjust )#Append string from the left by x + end_adjust
      append_num += end_adjust #Add 1 to account for the right adjustment
      string_revised = string_revised.rjust(x + append_num) #Prepend beginning of string by x + append_num (ex. 3+2)         
       
      return (f'|{string_revised}|') #return result to user

if __name__ == '__main__':
  print(make_field(1000,7))
  print(make_field("year",8))
  print(make_field("world",5))
  input()

#main()

