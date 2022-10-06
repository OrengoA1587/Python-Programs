 

def make_field(content,length):

  content = str(content)
  end_adjust = 1  
  if len(content) <= length - 2:      

      append_num = (length - len(content))#
      append_num -= end_adjust
      pre_adjust = append_num + len(content)
      
      string_revised = content.rjust(pre_adjust)
      string_revised = string_revised.ljust((append_num + 1) + len(content))
      
      return (f'|{string_revised}|')

  else: #len(content) > length - 2:     
      x = length - 2 
      string = content[:x] 

      append_num = len(content) - (length -2)
      append_num -= end_adjust    

      string_revised = string.ljust(x + end_adjust )#Append end of string            
      append_num += end_adjust
      string_revised = string_revised.rjust(x + append_num) #Prepend beginning of string         
       
      return (f'|{string_revised}|')

def main():
  print(make_field(1000,7))
  print(make_field("year",8))
  print(make_field("world",5))

main()












#prepend = append_num + x  



#string_revised = string_revised.ljust((append_num - 1) + len(content))#Append end of string  