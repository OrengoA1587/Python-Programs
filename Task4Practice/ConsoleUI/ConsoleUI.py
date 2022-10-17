import os


def get_path_depth(path):
    path = os.path.normpath(path)
   
    return len(path.split(os.sep)) -1
def generate_dir_report(path):
     
    for root,dirs,files in sorted((os.walk(path))): 
        filepath = root
        #print(get_path_depth(filepath))
        print(path)
        for file_name in sorted(files):            
             
            print(f'{file_name}')
         
# TODO: Place your code here
if __name__ == '__main__':
     pass
     generate_dir_report('data/dir-top')

 