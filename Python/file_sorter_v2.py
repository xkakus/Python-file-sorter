#!/usr/bin/env python
import os, shutil, re

def rename_if_exists(destination, extension, filename):
    base, ext = os.path.splitext(filename)
    i = 1
    while True:
        new_filename = f"{base} ({i}){ext}"
        new_path = os.path.join(destination, extension, new_filename)
        if not os.path.exists(new_path):
            return new_path
        i += 1

def get_info(fileName):
    fileName = fileName.split(r'_')
    fileName[1] = fileName[1].lower()
    if fileName[1] in ['acct', 'econ', 'mis', 'stat']:
        return fileName[1]
    else:
        return None

path = input('What is the target folder: ')
if path == '':
    path = '/home/xkaku/Desktop/test'

files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        fileName, ext = os.path.splitext(file)
        ext = ext[1:]

        if ext in ["gif", "jpg", "png", "jpeg", "bmp", "tif", "tiff"]:
            destination = os.path.join(path, 'images')
        elif ext in ['doc', 'docx', 'xls', 'xlsx', 'pdf', 'txt', 'ai', 'svg', 'eps', 'idml', 'indd', 'pptx', 'ppt', 'xopp']:
            destination = os.path.join(path, 'documents')
        elif ext in ['prproj', 'mp4', 'mov', 'avi', 'aep', 'aepx', 'sesx', 'wav', 'mp3', 'flac']:
            destination = os.path.join(path, 'medias')
        elif ext in ['py', 'html', 'css', 'js', 'json']:
            destination = os.path.join(path, 'code')
        else:
            destination = os.path.join(path, 'random', ext)
                
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
                new_path = rename_if_exists(destination, subject, ext, file)

        shutil.move(file_path, new_path)
    else:
        print(f"Skipping directory: {file_path}")
