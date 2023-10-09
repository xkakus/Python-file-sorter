#!/usr/bin/env python
import os, shutil, re, json

def rename_if_exists(destination, extension, filename, subject=None):
    base, ext = os.path.splitext(filename)
    i = 1
    while True:
        new_filename = f"{base} ({i}){ext}"
        if subject == None:
            new_path = os.path.join(destination, extension, new_filename)
        else:
            new_path = os.path.join(destination, subject, extension, new_filename)

        if not os.path.exists(new_path):
            return new_path
        i += 1

def get_info(fileName):
    # subjects = ['acct', 'econ', 'mis', 'stat', 'macro']
    subjects = {
        "acct":["accounting"],
        "econ":["micro", "macro"],
        "mis":["management information system", "information system"],
        "stat":["statistic", "Quantitative Methods"]
        }
    for subject in subjects:
        if re.search(subject, fileName, re.IGNORECASE):
            return subject
    for subject, aliases in subjects.items():
        for alias in aliases:
            if re.search(alias, fileName, re.IGNORECASE):
                return subject
    return None

path = input('What is the target folder: ')
home_dir = os.path.expanduser("~")
if path == '':
    path = os.path.join(home_dir, 'Desktop', 'sort')
    if not os.path.exists(path):
        os.makedirs(path)
        print(f'made {path}')


files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        fileName, ext = os.path.splitext(file)
        ext = ext[1:]

        extension_map = {
            "images": ["gif", "jpg", "png", "jpeg", "bmp", "tif", "tiff"],
            "documents": ['doc', 'docx', 'xls', 'xlsx', 'pdf', 'txt', 'ai', 'svg', 'eps', 'idml', 'indd', 'pptx', 'ppt', 'xopp'],
            "medias": ['prproj', 'mp4', 'mov', 'avi', 'aep', 'aepx', 'sesx', 'wav', 'mp3', 'flac'],
            "code": ['py', 'html', 'css', 'js', 'json', 'ipynb']
        }

        for folder, aliases in extension_map.items():
            for alias in aliases:
                if ext == alias:
                    destination = os.path.join(path, folder)
                    print(destination)
                
        if not os.path.exists(destination):
            os.makedirs(destination)

        subject = get_info(fileName)
        if subject == None:
            if not os.path.exists(os.path.join(destination, ext)):
                os.makedirs(os.path.join(destination, ext))
            new_path = os.path.join(destination, ext, file)
            if os.path.exists(new_path):
                new_path = rename_if_exists(destination, ext, file)
        else:
            if not os.path.exists(os.path.join(destination, subject, ext)):
                os.makedirs(os.path.join(destination, subject, ext))
            new_path = os.path.join(destination, subject, ext, file)
            if os.path.exists(new_path):
                new_path = rename_if_exists(destination, ext, file, subject)

        shutil.move(file_path, new_path)
    else:
        print(f"Skipping directory: {file_path}")
