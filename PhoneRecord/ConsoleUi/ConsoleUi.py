

from datetime import datetime

def filter_phone_calls(area_code,start_hour,end_hour,input_path,output_path):

    with open(input_path, mode="r") as readFile:
        with open(output_path, mode='w')as writeFile:
            phoneList = readFile.readlines()
            
            for x in phoneList:             
                 x = str(x)
                 x = x.split(' ')
                 date_x = str(x[0])                 
                 date_x = date_x.replace('-','/') + ' ' + str(x[1])             
                 date_time = datetime.strptime(date_x,'%Y/%m/%d %H:%M:%S:')                 
                 y = str(x[2])       
                 if int(y[3:6]) == area_code and date_time.hour in range(start_hour,end_hour):
                     
                     writeFile.writelines(f'{date_time}: {y}')
                     print(f'{date_time}: {y}')  
          

if __name__ == '__main__':
    pass # use this block for validation
    filter_phone_calls(area_code=412,start_hour=0,end_hour = 1,input_path = 'data/phone_calls.txt',output_path='data/phone_calls_filtered.txt')

