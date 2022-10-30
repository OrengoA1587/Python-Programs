# TODO 1: Implement the `create_container` function here.
from ast import Num
from site import enablerlcompleter
from typing import Container


def create_container(container_type):
    if container_type == 'list':
        container_type = []
        return container_type
    elif container_type == 'dict':
        container_type = {}
    elif container_type == 'set':
        container_type = set()
    elif container_type == 'tuple':
        container_type = ()
    return container_type

 #TODO 2: Implement the `access_item` function here.
def access_item(num,container_type):     
    if type(container_type) == list:        
        if num in range (len(container_type)):
            return container_type[num]        
        else:
            return False                          
    elif type(container_type) == dict:         
        if num in container_type.keys():
            print(container_type)
            return container_type[num]        
        else:
            return False
    elif type(container_type) == set:        
        if num in range (len(list(container_type))):
            return True        
        else:
            return False
    elif type(container_type) == tuple:
        if num in range (len(container_type)):
            return container_type[num]        
        else:
            return False     
# TODO 3: Implement the `add_item` function here.
def add_item(num,container_type):     
    if type(container_type) == list:         
        container_type.append(num)        
        return container_type        
    elif type(container_type) == dict:
        container_type.update({num[0]:str(num[1])})  
        return container_type
    elif type(container_type) == set: 
        container_type.add(num)
        return container_type          
    elif type(container_type) == tuple:
         x = list(container_type)#Convert tuple to list to add elements
         x.append(num)
         container_type = tuple(x)#Convert back to tuple                
         return container_type
# TODO 4: Implement the `remove_item` function here.
def remove_item(num,container_type):
    if type(container_type) == list: 
        c = container_type.count(num)
        for i in range (c):
            container_type.remove(num)   
        return container_type        
    elif type(container_type) == dict:
        del container_type[num] 
        return container_type
    elif type(container_type) == set: 
        x = list(container_type)#Convert tuple to list to remove elements
        c = x.count(num)
        for i in range (c):
            x.remove(num)   
        container_type = set(x)#Convert back to tuple
        return container_type 
          
    elif type(container_type) == tuple:
        x = list(container_type)#Convert tuple to list to remove elements
        c = x.count(num)
        for i in range (c):
            x.remove(num)   
        container_type = tuple(x)#Convert back to tuple
        return container_type 

# TODO 5: Implement the `update_item` function here.
def update_item(num1,num2,container_type,value):
    #print(container_type)
    if type(container_type) == list:   
        if value == False:
            for i in range(len(container_type)):            
                if container_type[i] == num1:                   
                   container_type[i] = num2                    
                return container_type              
        else:
            for i in range(len(container_type)):            
                if container_type[i] == num1:                
                    container_type[i] = num2                
            return container_type        
    #elif type(container_type) == dict:
    #    if type(num2) == tuple:  
    #        print("wow")
    #        container_type[num1] = container_type.pop([(num2)])
    #    else:
    #       container_type[num1] = num2
    #    return container_type

    elif type(container_type) == set: 
        x = list(container_type)#Convert tuple to list to remove elements
        #c = x.count(num1)
        for i in range (len(x)):
            if x[i] == num1:
                x[i] = num2
        container_type = set(x)#Convert back to tuple
        return container_type 
          
    elif type(container_type) == tuple:
        x = list(container_type)#Convert tuple to list to remove elements         
        for i in range (len(x)):
            if x[i] == num1:
                x[i] = num2   
        container_type = tuple(x)#Convert back to tuple
        return container_type 

# TODO 6: Implement the `convert_container` function here.
def convert_container(container,container_type):     
    if container_type == 'list':
        container = list(container)
        return container
    elif container_type == 'dict':
        container = dict.fromkeys(container)
        return container
    elif container_type == 'set':
        container = set(container)
        return container
    elif container_type == 'tuple':
        container = tuple(container)
        return container
    return container_type

def main():
    #Set container type
    container1 = create_container('list')
    container2 = create_container('dict')
    container3 = create_container('set')
    container4 = create_container('tuple')
   
    #------------------------------------------------
    #Add to container 
    container1 = add_item(1,container1)#Add list
    container1 = add_item(2,container1)#Add list
    container1 = add_item(3,container1)#Add list
    container1 = add_item(4,container1)#Add list
    container1 = add_item(1,container1)#Add list
    container2 = add_item((1,'e'),container2)#Add to dictionary
    container2 = add_item((2,'f'),container2)#Add to dictionary
    container2 = add_item((3,'g'),container2)#Add to dictionary
    container2 = add_item((4,'h'),container2)#Add to dictionary
    container3 = add_item(1,container3)#Add to set
    container3 = add_item(2,container3)#Add to set
    container3 = add_item(3,container3)#Add to set
    container3 = add_item(4,container3)#Add to set
    container3 = add_item(4,container3)#Add to set
    container3 = add_item(5,container3)#Add to set
    container4 = add_item(1,container4)#Add to tuple
    container4 = add_item(2,container4)#Add to tuple
    container4 = add_item(3,container4)#Add to tuple
    container4 = add_item(1,container4)#Add to tuple
    #print(container1)
    #print(container2)
    #print(container3)
    #print(container4)
    #------------------------------------------------
    ###Access container
    #access1 = access_item(0,container1)
    #access2 = access_item(9,container2)
    #access3 = access_item(0,container3)
    #access4 = access_item(0,container4)
    #print(access1)
    #print(access2)
    #print(access3)
    #print(access4)
    ##--------------------------------------------------
    ##Remove Item from container
    #remove1 = remove_item(1,container1)
    #remove2 = remove_item(2,container2)
    #remove3 = remove_item(4,container3)
    #remove4 = remove_item(1,container4)
    #print(remove1)
    #print(remove2)
    #print(remove3)
    #print(remove4)
    ##--------------------------------------------------
    ##Update Container
    #container1 = update_item(1,9,container1,True)
    #print(container1)
    #container1 = update_item(1,9,container1,False)
    #print(container1)
    container2 = update_item(1,'z',container2,False)
    print(container2)
    container2 = update_item(1,(9,'e'),container2,False)
    print(container2)
    #container3 = update_item(5,19,container3,False)
    #print(container3)
    #container4 = update_item(1,(9,11),container4,False)
    #print(container4)
    #---------------------------------------------------
    #Convert Container
    #container1 = convert_container(container1,'dict')
    #container2 = convert_container(container2,'list')
    #container3 = convert_container(container3,'tuple')
    #container4 = convert_container(container4,'set')
    #print(type(container1))
    #print(type(container2))
    #print(type(container3))
    #print(type(container4))
    #print(container1)
    #print(container2)
    #print(container3)
    #print(container4)
if __name__ == '__main__':
    main()
 