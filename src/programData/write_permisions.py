import os
import src.programData.thisdir
homedir =  os.path.expanduser(r"~")
thisdir = src.programData.thisdir.thisdir()
def check_for_write_permissions(dir):
        i=2 # change this to 1 to debug flatpak
        if 'FLATPAK_ID' in os.environ or i==1:
            import subprocess

            command = f'cat /.flatpak-info' # this is for actual flatpak
            #command = 'flatpak info --show-permissions io.github.tntwise.REAL-Video-Enhancer' 
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = result.stdout.split('\n')
            output_2=[]
            for i in output:
                if len(i) > 0 and i != '\n':
                    output_2.append(i)
            directories_with_permissions=[]
            for i in output_2:
                if 'filesystems=' in i:
                    i=i.split(';')
                    s=[]
                    for e in  i:
                        if len(e) > 0 and i != '\n':
                            s.append(e)
                    for j in s:
                        j=j.replace('filesystems=','')
                        if j == 'xdg-download':
                            j=f'{homedir}/Downloads'
                        j=j.replace('xdg-',f'{homedir}/')
                        j=j.replace('~',f'{homedir}')
                        directories_with_permissions.append(j)
            for i in directories_with_permissions:
                
                if dir[-1] !='/':
                    dir+='/'
                print(f'Checking dir: {i.lower()} is in or equal to Selected Dir: {dir.lower()}')
                    
                
                if i.lower() in dir.lower() or 'io.github.tntwise.real-video-enhancer' in dir.lower() and ':ro' not in i:
                    return True
                else:
                    if '/run/user/1000/doc/' in dir:
                        dir=dir.replace('/run/user/1000/doc/','')
                        dir=dir.split('/')
                        permissions_dir=''
                        for index in range(len(dir)):
                            if index != 0:
                                permissions_dir+=f'{dir[index]}/'
                        if homedir not in permissions_dir:
                            dir=f'{homedir}/{permissions_dir}'
                        else:
                            dir=f'/{permissions_dir}'
                        
                        
                    print(f'Checking dir: {i.lower()} is in or equal to Selected Dir: {dir.lower()}')
                    if i.lower() in dir.lower() or 'io.github.tntwise.real-video-enhancer' in dir.lower() and ':ro' not in i:
                        return True
            
            return False
        else:
                if os.access(dir, os.R_OK) and os.access(dir, os.W_OK):
                    print('has access')
                    return True
                return False