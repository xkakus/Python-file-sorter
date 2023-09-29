import os, shutil

def rename_if_exists(destination, filename):
    base, ext = os.path.splitext(filename)
    i = 1
    while True:
        new_filename = f"{base} ({i}){ext}"
        new_path = os.path.join(destination, new_filename)
        if not os.path.exists(new_path):
            return new_path
        i += 1

path = input('What is the target folder: ')
if path == '':
    path = 'C:/Users/yuxua/Desktop/test'

files = os.listdir(path)

while not os.path.isdir(os.path.join(path, 'images')) or not os.path.isdir(os.path.join(path, 'documents')) or not os.path.isdir(os.path.join(path, 'medias')) or not os.path.isdir(os.path.join(path, 'random')):
    if not os.path.isdir(os.path.join(path, 'images')):
        print("Made Img")
        os.makedirs(os.path.join(path, 'images'))
    elif not os.path.isdir(os.path.join(path, 'documents')):
        print("Made Doc")
        os.makedirs(os.path.join(path, 'documents'))
    elif not os.path.isdir(os.path.join(path, 'medias')):
        print("Made Med")
        os.makedirs(os.path.join(path, 'medias'))
    else:
        print("made Ran")
        os.makedirs(os.path.join(path, 'random'))

for file in files:
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):  # Check if it's a file
        fileName, ext = os.path.splitext(file)
        ext = ext[1:]

        if ext in ["gif", "jpg", "png", "jpeg", "bmp", "tif", "tiff"]:
            destination = os.path.join(path, 'images')
        elif ext in ['doc', 'docx', 'xls', 'xlsx', 'pdf', 'txt', 'ai', 'svg', 'eps', 'idml', 'indd']:
            destination = os.path.join(path, 'documents')
        elif ext in ['prproj', 'mp4', 'mov', 'avi', 'aep', 'aepx', 'sesx', 'wav', 'mp3', 'flac']:
            destination = os.path.join(path, 'medias')
        else:
            destination = os.path.join(path, 'random', ext)

        if not os.path.exists(destination):
            os.makedirs(destination)

        new_path = os.path.join(destination, file)

        if os.path.exists(new_path):
            new_path = rename_if_exists(destination, file)

        shutil.move(file_path, new_path)
    else:
        print(f"Skipping directory: {file_path}")