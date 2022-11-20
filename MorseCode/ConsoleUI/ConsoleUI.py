




from asyncio.windows_events import NULL
from types import NoneType


morse_dict = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",
              ".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",
              ".--":"W","-..-":"X","-.--":"Y","--..":"Z","-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6",
              "--...":"7","---..":"8","----.":"9",}



#test_string = ".- -. - .... --- -. -.--"
test_string = input("Enter Morse Code: ")
morse_list = test_string.split()
x = []
decode = ""
for morse in morse_list:
    x.append(morse_dict.get(morse))
print(len(x))

for i in x:
    if i == None:
        print("Invalid input")
    else:

        print(f'Decoded: {decode.join(x)}')
