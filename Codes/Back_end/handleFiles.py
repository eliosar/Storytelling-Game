import os
from pathlib import Path
from Back_end import manager
import json
import shutil


def create_folder(root: str):
    # if not already there, create new folder(s)
    Path(root).mkdir(parents=True, exist_ok=True)
    return root

def does_exist(path: str):
    return os.path.exists(path)

def get_name_from_path(path: str):
    return os.path.basename(path)

def getItems(root: str):
    res = []

    for name in os.listdir(root):
        res.append(manager.join_paths((root, name)))

    return res

def is_folder(item):
    return os.path.isdir(item)

def get_file_data_as_dict(path: str):
    try:
        return (json.loads(get_data_from_file(path)), True)
    except:
        print('Wrong json syntax')
        return (None, False)
    
def move_file(from_path: str, to_path: str):
    shutil.move(from_path, to_path)

def get_data_from_file(file_path:str):
    file_name = get_name_from_path(file_path)
    data = []
    
    with open(file_path, 'rb') as file:
        data = file.read()

    print(file_name + ' loaded')

    return data