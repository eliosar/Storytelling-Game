from Back_end import manager
from flask import render_template

def get_Beginning_Scene_Name():
    all_scene_names = manager.get_all_scene_names()
    for scene_name in all_scene_names:
        dic_status = manager.get_status_from_scene(scene_name)[0]
        if dic_status.get("status")== "Beginning":
            return scene_name
    return "No beginning scene found"
    


def start():
    beginning_scene_name = get_Beginning_Scene_Name()
    beginning_background = manager.get_image_as_base64(manager.get_background_image_in_scene(beginning_scene_name))
    return render_template('mainFrame.html', context=[beginning_scene_name, beginning_background])