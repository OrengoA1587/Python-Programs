# TODO 1: Implement the `create_container` function here.
from site import enablerlcompleter
from typing import Container


def create_container(container_type):

    if container_type == 'list':
        container_type = []
    elif container_type == 'dict':
        container_type = {}
    elif container_type == 'set':
        container_type = set()
    elif container_type == 'tuple':
        container_type = ()
    return container_type


# TODO 2: Implement the `access_item` function here.
def access_item(num,container_type):
   
    if type(container_type) == list:
        return container_type[num]         
    elif container_type == dict:
        return container_type
    elif container_type == 'set':
        container_type = set()
    elif container_type == 'tuple':
        container_type = ()
     

 
# TODO 3: Implement the `add_item` function here.
def add_item(num,container_type):
    print(num[0])
    print(num[1]) 
    if type(container_type) == list:
        container_type.append(num)
        return container_type        
    elif type(container_type) == dict:
        container_type.update({num[0]:str(num[1])})  
        return container_type
    elif type(container_type) == set: 
        container_type.add(num)
        return container_type
          
    #elif container_type == 'tuple':
         
# TODO 4: Implement the `remove_item` function here.


# TODO 5: Implement the `update_item` function here.


# TODO 6: Implement the `convert_container` function here.

def main():
    container = create_container('dict')
     
    container = add_item((9,'e'),container)
    print(container)
main()
#container = {1,2,3,4}
    #add_item(9,container) 
     
    #element = access_item(2,container)
    #print(element)
