import os, shutil

def rename_if_exists(destination, extension, filename): # gets the target destination, then the filename (file.txt)
    base, ext = os.path.splitext(filename)   # next, the file is split into two parts by the dot
    i = 1                                    # this creates and assings a variable
    while True:                              # conditional test
        new_filename = f"{base} ({i}){ext}"  # a template string, it will use the splitted file, base the front, i, the incriment, and ext, the file extension
        new_path = os.path.join(destination, extension, new_filename) # this creates a new variable, this will create the file path (User/user/Desktop/folder/new_filename (1).txt)
        if not os.path.exists(new_path):     # this tests if the name is already taken, if not, return the new path, then incriment again to prevent duplicate of duplicate file name
            return new_path
        i += 1

path = input('What is the target folder: ')  # this prompts for the target folder path, and assigns a value
if path == '':
    path = 'C:/Users/yuxua/Desktop/test'

files = os.listdir(path)                     # this will list the files within the target directory

# for each file in the directory
for file in files:
    # this creates the complete file path for each file in the directory
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):  # Check if it's a file
        # this splits the file into two part, the name of the file, and the extension
        fileName, ext = os.path.splitext(file)
        # this gets rid of the period
        ext = ext[1:]

        # this compares the extension, if matched, then assign the variable destination to the target path
        match ext:
            case ["gif", "jpg", "png", "jpeg", "bmp", "tif", "tiff"]:
                destination = os.path.join(path, 'images')
            case ['doc', 'docx', 'xls', 'xlsx', 'pdf', 'txt', 'ai', 'svg', 'eps', 'idml', 'indd', 'pptx', 'ppt', 'xopp']:
                destination = os.path.join(path, 'documents')
            case ['prproj', 'mp4', 'mov', 'avi', 'aep', 'aepx', 'sesx', 'wav', 'mp3', 'flac']:
                destination = os.path.join(path, 'medias')
            case _:
                destination = os.path.join(path, 'random', ext)
                
        # if the directory doesnt exists, then make it
        if not os.path.exists(destination):
            os.makedirs(destination)

        # assign the new file path
        if not os.path.exists(os.path.join(destination, ext)):
            os.makedirs(os.path.join(destination, ext))

        new_path = os.path.join(destination, ext, file)

        # tests for repeated name in the targeted path, if it does, call the function rename_if_exists() and rename the file
        if os.path.exists(new_path):
            new_path = rename_if_exists(destination, ext, file)

        # moves the file to the target directory
        shutil.move(file_path, new_path)
    else:
        # ignored directory
        print(f"Skipping directory: {file_path}")