import os, shutil, sys, argparse

path = input("What is the file path? \n")
if path == '':
    print('default: C:/Users/yuxua/Desktop/random')
    path = 'C:/Users/yuxua/Desktop/random'

files = os.listdir(path)

for file in files:
    filename,extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path+'/'+extension):
        if os.path.exists(path+'/'+'photo'+'/'):
            match extension:
                case "png" | "jpg" | "jpeg" :
                    shutil.move(path+'/'+file, path+'/'+'photo'+'/'+file)
                case _ :
                    shutil.move(path+'/'+file, path+'/'+extension+'/'+file)
        else:
            os.makedirs(path+'/'+'photo'+'/')
    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+file, path+'/'+extension+'/'+file)

