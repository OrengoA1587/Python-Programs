import os


def get_path_depth(path):
    path = os.path.normpath(path)
     
    return len(path.split(os.sep))
def generate_dir_report(path,out_file,show_files,num_files,file_size,hl):
    with open(out_file,mode='w') as wf:
        main_path_depth = get_path_depth(path)
        for root, dirs, files in os.walk(path):
            dir_indent =  get_path_depth(root) - main_path_depth - 1            
            file_indent = dir_indent + 1             
            level = file_indent         
            if num_files == True:
                num_f = f'({len(files)} files)'        
            if level == 0:
                 indent = '' * 2 * (level)
                 print('+{}{}'.format(indent, os.path.basename(root)), num_f, file = wf)                   

            elif level == 1:
                 indent = '' * 2 * (level)
                 print('|-+ {}{}'.format(indent, os.path.basename(root)),num_f, file = wf)
            elif level == 2:
                 indent = '' * 3 * (level)
                 print('  |-+ {}{}'.format(indent, os.path.basename(root)),num_f, file = wf)
             
            file_indent = ' ' * 2 * (level)
            if show_files == True:             
                for f in files:  
                    if file_size == True:
                        file_name = os.path.join(root, f)
                        size = os.path.getsize(file_name)           
                        size = f'({size} bytes)' 
                    else:
                        size = ''
                    if f.endswith(f'.{hl}'):
                        print('{}{}'.format(file_indent + '|-- ', f),size, '<--', file = wf)
                    else:
                        print('{}{}'.format(file_indent + '|-- ', f),size, file = wf)
        
    wf.close()     
# TODO: Place your code here
if __name__ == '__main__':
     pass
     generate_dir_report('data/dir-top','dir-report.txt', show_files=True,num_files=True,file_size=True,hl='txt')

 