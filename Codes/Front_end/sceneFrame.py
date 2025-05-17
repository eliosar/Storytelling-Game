from Back_end import manager

def start(scene_name: str):
    data = manager.get_data_from_scene(scene_name)
    return data