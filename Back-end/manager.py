import handleFiles

STORY_ROOT_FOLDER = 'Story/'
DUMP_ROOT_FOLDER = 'Dump/'

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

    handleFiles.create_folder(join_strings((DUMP_ROOT_FOLDER)))

def is_at_least_one_scene_available():
    path = join_strings((STORY_ROOT_FOLDER, SCENES_ROOT_FOLDER))
    itemsInOrdner = handleFiles.getItems(path)

    if len(itemsInOrdner) > 0:        
        path = join_strings((path, handleFiles.getItems(path)[0]))
        return handleFiles.is_folder(path) == True
    
    return False

def is_dump_file_right():
    root = DUMP_ROOT_FOLDER
    items = handleFiles.getItems(root)

    if len(items) > 0:
        if handleFiles.is_folder(items[0]):
            root = join_strings(root, items[0]) # now the scene-folder
            items = handleFiles.getItems(root)
            
            usable_items = []

            for item in items:
                name = handleFiles.get_name_from_path(item)
                print('------------------ going through "' + name + '" ------------------')

                if name == 'background.png':
                    usable_items.append(name)

                if name.count('choice') > 0 and name.count('.json') > 0:
                    (data, is_usable) = handleFiles.get_file_data_as_dict(item)
                    if is_usable:
                        if type(data['choicename']) != str:
                            print('found no topic "choicename"')
                            is_usable = False
                        if type(data['scenename']) != str:
                            print('found no topic "scenename"')
                            is_usable = False
                        
                        if is_usable == True:
                            usable_items.append(name)
                
                if name == 'status.json':
                    (data, is_usable) = handleFiles.get_file_data_as_dict(item)
                    if is_usable == True:
                        if type(data['status']) != str:
                            print('found no topic "status"')
                            is_usable = False
                        
                        if is_usable == True:
                            usable_items.append(name)
                
                if name == 'Texts':
                    temp_items = handleFiles.getItems(item)
                    
                    for temp_item in temp_items:
                        (data, is_usable) = handleFiles.get_file_data_as_dict(temp_item)

                        if is_usable:
                            if type(data['text']) != str:
                                print('found no topic "text"')
                                is_usable = False
                            if type(data['speekername']) != str:
                                print('found no topic "speekername"')
                                is_usable = False
                            
                            if is_usable == True:
                                usable_items.append(name)

            
            if len(usable_items) != len(items):
                print('not all available items in the scene-folder were usable')
                print('usable items were: ' + usable_items)
    return False

def is_dump_scenename_unique():
    dump_items = handleFiles.getItems(DUMP_ROOT_FOLDER)
    dump_scenename = handleFiles.get_name_from_path(dump_items[0])

    items = handleFiles.getItems(join_strings((STORY_ROOT_FOLDER, SCENES_ROOT_FOLDER)))
    for item in items:
        name = handleFiles.get_name_from_path(item)
        if name == dump_scenename:
            return False
    
    return True


def add_new_scene_from_dump_file():
    root = DUMP_ROOT_FOLDER
    items = handleFiles.getItems(root)
    from_path = join_strings(root, items[0])

    to_path = join_strings((STORY_ROOT_FOLDER, SCENES_ROOT_FOLDER, handleFiles.get_name_from_path(from_path)))

    handleFiles.move_file(from_path, to_path)