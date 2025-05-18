import base64
from Back_end import handleFiles

STORY_ROOT_FOLDER = 'Story'
DUMP_ROOT_FOLDER = 'Dump'
DUMMIES_ROOT_FOLDER = 'Dummies'

ICONS_FOLDER = 'Icons'
SPEEKERS_FOLDER = 'Speekers'
SCENES_ROOT_FOLDER = 'Scenes'



def join_strings(inp: tuple):
    res = ''
    for txt in inp:
        res = res + txt

    return res

def join_paths(inp: tuple):
    res = []

    for i in range(len(inp)):
        res.append(inp[i])
        if i != len(inp) - 1:
            res.append('/')

    return join_strings(res)

def create_folder_sceleton():
    handleFiles.create_folder(join_paths((STORY_ROOT_FOLDER, SCENES_ROOT_FOLDER)))
    handleFiles.create_folder(join_paths((STORY_ROOT_FOLDER, SPEEKERS_FOLDER)))
    handleFiles.create_folder(join_paths((STORY_ROOT_FOLDER, ICONS_FOLDER)))

    handleFiles.create_folder(DUMP_ROOT_FOLDER)
    handleFiles.create_folder(DUMMIES_ROOT_FOLDER)

def is_at_least_one_scene_available():
    path = join_paths((STORY_ROOT_FOLDER, SCENES_ROOT_FOLDER))
    itemsInOrdner = handleFiles.getItems(path)

    if len(itemsInOrdner) > 0:        
        return handleFiles.is_folder(handleFiles.getItems(path)[0]) == True
    
    return False

def is_dump_file_right():
    root = DUMP_ROOT_FOLDER
    items = handleFiles.getItems(root)

    if len(items) == 0:
        print('Found nothing in the dump-folder')
    else:
        if handleFiles.is_folder(items[0]):
            root = items[0] # now the scene-folder
            items = handleFiles.getItems(root)

            is_folder_empty = False
            usable_items = []
            item_count = 0
            subtract_count_because_of_wanted_folder = 0
            
            if len(items) == 0:
                is_folder_empty = True
                print('Found nothing in the Scene-folder')
            else:
                item_count += len(items)

                for item in items:
                    name = handleFiles.get_name_from_path(item)
                    print('------------------ Going through "' + name + '" ------------------')

                    if name == 'background.jpeg':
                        usable_items.append(name)

                    if name == 'Choices':
                        subtract_count_because_of_wanted_folder += 1
                        temp_items = handleFiles.getItems(item)
                        
                        if len(temp_items) == 0:
                            is_folder_empty = True
                            print('Found nothing in the Texts-folder')
                        else:
                            item_count += len(temp_items)

                            for temp_item in temp_items:
                                name = handleFiles.get_name_from_path(temp_item)

                                print('------------------ Going through "' + name + '" ------------------')
                                if name.count('choice') > 0 and name.count('.json') > 0:
                                    handle_dict_for_keys_and_str(['choicename', 'scenename'], usable_items, name, temp_item)
                    
                    if name == 'status.json':
                        handle_dict_for_keys_and_str(['status'], usable_items, name, item)
                    
                    if name == 'Texts':
                        subtract_count_because_of_wanted_folder += 1
                        temp_items = handleFiles.getItems(item)
                        
                        if len(temp_items) == 0:
                            is_folder_empty = True
                            print('Found nothing in the Texts-folder')
                        else:
                            item_count += len(temp_items)

                            for temp_item in temp_items:
                                name = handleFiles.get_name_from_path(temp_item)

                                print('------------------ Going through "' + name + '" ------------------')

                                if name.count('text') > 0  and name.count('.json') > 0:
                                    handle_dict_for_keys_and_str(['text', 'speekername'], usable_items, name, temp_item)
                
                print('\nUsable items were: ' + str(usable_items))
                if len(usable_items) < (item_count - subtract_count_because_of_wanted_folder): # have to substract every wanted folder (e.g. "Texts"-folder) inside the scenes folder
                    print('Not every element in the Scene-folder had been usable')
            
            if len(usable_items) == (item_count - subtract_count_because_of_wanted_folder) and is_folder_empty == False:
                return True
        else:
            print('Found no folder as first item in the dump-folder')
    print('')

    return False

def handle_dict_for_keys_and_str(keys: str, usable_items: list, name: str, item_path: str):
    (data, is_usable) = handleFiles.get_file_data_as_dict(item_path)

    if is_usable:
        for key in keys:
            if key not in data or type(data[key]) != str:
                print('Found no topic "' + key + '"')
                is_usable = False
        
    if is_usable == True:
        usable_items.append(name)

def is_dump_scenename_unique():
    dump_items = handleFiles.getItems(DUMP_ROOT_FOLDER)
    dump_scenename = handleFiles.get_name_from_path(dump_items[0])

    items = handleFiles.getItems(join_paths((STORY_ROOT_FOLDER, SCENES_ROOT_FOLDER)))
    for item in items:
        name = handleFiles.get_name_from_path(item)
        if name == dump_scenename:
            print('scenename is not unique')
            return False
    
    return True


def add_new_scene_from_dump_file():
    root = DUMP_ROOT_FOLDER
    items = handleFiles.getItems(root)
    from_path = items[0]

    to_path = join_paths((STORY_ROOT_FOLDER, SCENES_ROOT_FOLDER, handleFiles.get_name_from_path(from_path)))

    handleFiles.move_file(from_path, to_path)

def get_path_to_file_in_scene(scene_name: str, file_name: str):
    return join_paths((STORY_ROOT_FOLDER, SCENES_ROOT_FOLDER, scene_name, file_name))

def get_background_from_scene_as_base64(scene_name: str):
    bitstring = handleFiles.get_data_from_file(get_path_to_file_in_scene(scene_name, 'background.jpeg'))

    # Encode the bytes to a base64 string
    base64_string = base64.b64encode(bitstring).decode("utf-8")

    # Create the data URI
    data_uri = f"data:image/jpeg;base64,{base64_string}"

    return data_uri

def get_texts_from_scene(scene_name: str):
    res = []
    path = get_path_to_file_in_scene(scene_name, 'Texts')
    for item in handleFiles.getItems(path):
        res.append(handleFiles.get_file_data_as_dict(item))
    return res

def get_choices_from_scene(scene_name: str):
    res = []
    path = get_path_to_file_in_scene(scene_name, 'Choices')
    for item in handleFiles.getItems(path):
        res.append(handleFiles.get_file_data_as_dict(item))
    return res

def get_status_from_scene(scene_name: str):
    return handleFiles.get_file_data_as_dict(get_path_to_file_in_scene(scene_name, 'status.json'))