import os


def get_path_depth(path):
    path = os.path.normpath(path)
     
    return len(path.split(os.sep))
def generate_dir_report(path,report_file_path,show_files,num_files,file_size,hl):
    with open(report_file_path,mode='w') as wf:
        main_path_depth = get_path_depth(path)
        for root, dirs, files in os.walk(path):
            dir_indent =  get_path_depth(root) - main_path_depth - 1            
            file_indent = dir_indent + 1             
            level = file_indent 
             
            if num_files == True:
                num_f = f'({len(files)} files)'  
            else:
                num_f = ''
            if level == 0:                                  
                 print('+', os.path.basename(root), num_f)
                 wf.writelines('+ ' + os.path.basename(root) + num_f + '\n')
                 #print('+', os.path.basename(root), num_f, file = wf)
            elif level == 1:                  
                 print('|-+',os.path.basename(root),num_f)
                 #print('|-+',os.path.basename(root),num_f, file = wf)
                 wf.writelines('|-+' + os.path.basename(root) + num_f + '\n')
            elif level == 2:                 
                 print('  |-+',os.path.basename(root),num_f)
                 #print('  |-+',os.path.basename(root),num_f, file = wf)
                 wf.writelines('  |-+' + os.path.basename(root) + num_f + '\n')
          
            if show_files == True:             
                for f in files:  
                    if file_size == True:
                        file_name = os.path.join(root, f)
                        size = os.path.getsize(file_name)           
                        size = f'({size} bytes)' 
                    else:
                        size = ''
                    if f.endswith(f'.{hl}'):
                        if level == 0:
                            #print(('|-- ', f),size, '<--', file = wf)
                            print(('|-- ' + f),size, '<--')
                            wf.writelines(('|-- ' + f)+size+ '<--' + '\n')
                        elif level == 1:
                            #print(('  |-- ', f),size, '<--', file = wf)
                            print(('  |-- ' + f),size, '<--') 
                            wf.writelines(('  |-- '+ f)+size+ '<--' + '\n')
                        elif level == 2:
                            #print(('    |-- ', f),size, '<--', file = wf)
                            print(('    |-- ' + f),size, '<--')
                            wf.writelines(('    |-- ' + f)+size+ '<--' + '\n')
                    else:
                        if level == 0:
                            #print(('|-- ', f),size, file = wf)
                            print(('|-- '+ f),size)
                            wf.writelines(('|-- '+ f)+size + '\n')
                        elif level == 1:
                            #print(('  |-- ', f),size, file = wf)
                            print(('  |-- '+ f),size) 
                            wf.writelines(('  |-- '+ f)+size + '\n')
                        elif level == 2:
                            #print(('    |-- ', f),size, file = wf)
                            print(('    |-- '+ f),size)
                            wf.writelines(('    |-- '+ f)+size + '\n')
        
    wf.close()     
# TODO: Place your code here
if __name__ == '__main__':
     pass
     generate_dir_report('data/dir-top','dir-report.txt', show_files=True,num_files=True,file_size=True,hl='txt')

             
                 
                 