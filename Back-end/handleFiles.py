import os
from pathlib import Path
import manager, saveAndLoad
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
        res.append(manager.join_strings(root, name))

    return res

def is_folder(item):
    return os.path.isdir(item)

def get_file_data_as_dict(path: str):
    try:
        return (json.loads(saveAndLoad.load_file(path)), True)
    except:
        print('wrong json syntax')
        return (None, False)
    
def move_file(from_path: str, to_path: str):
    shutil.copyfile(from_path, to_path)