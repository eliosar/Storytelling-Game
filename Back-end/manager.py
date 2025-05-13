import handleFiles

STORY_ROOT_FOLDER = 'Story/'
DUM_ROOT_FOLDER = 'Dump/'

ICONS_FOLDER = 'Icons/'
SPEEKERS_FOLDER = 'Speekers/'
SCENES_ROOT_FOLDER = 'Scenes/'



def join_strings(inp: tuple):
    res = ''
    for txt in inp:
        res = res + txt

    return res

def create_folder_sceleton():
    handleFiles.create_folder(join_strings((STORY_ROOT_FOLDER, SCENES_ROOT_FOLDER)))
    handleFiles.create_folder(join_strings((STORY_ROOT_FOLDER, SPEEKERS_FOLDER)))
    handleFiles.create_folder(join_strings((STORY_ROOT_FOLDER, ICONS_FOLDER)))

def is_at_least_one_scene_available():
    path = join_strings((STORY_ROOT_FOLDER, SCENES_ROOT_FOLDER))
    itemsInOrdner = handleFiles.getItems(path)

    if len(itemsInOrdner) > 0:        
        path = join_strings((path, handleFiles.getItems(path)[0]))
        return handleFiles.is_folder(path) == True
    
    return False

def is_dump_file_right():
    pass

def add_new_scene_from_dump_file():
    pass