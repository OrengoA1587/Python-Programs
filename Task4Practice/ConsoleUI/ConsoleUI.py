import os


def get_path_depth(path):
    path = os.path.normpath(path)
     
    return len(path.split(os.sep))
def generate_dir_report(path,out_file,show_files,num_files,file_size,h1):
    with open(out_file,mode='w') as wf:
        for root, dirs, files in os.walk(path):
            #size = files
        
            level = root.replace(path, '').count(os.sep)
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
             
            subindent = ' ' * 2 * (level)
            if show_files == True:             
                for f in files:  
                    if file_size == True:
                        file_name = os.path.join(root, f)
                        size = os.path.getsize(file_name)           
                        size = f'({size} bytes)' 
                    else:
                        size = ''
                    if f.endswith(f'.{h1}'):
                        print('{}{}'.format(subindent + '|-- ', f),size, '<--', file = wf)
                    else:
                        print('{}{}'.format(subindent + '|-- ', f),size, file = wf)
    wf.close()     
# TODO: Place your code here
if __name__ == '__main__':
     pass
     generate_dir_report('data/dir-top','dir-report.txt', show_files=True,num_files=True,file_size=True,h1='txt')

 