from Back_end import manager
from flask import render_template

def start(scene_name: str):
    background_path = manager.get_background_path_from_scene_for_template(scene_name)
    data = (background_path,)
    return render_template('sceneFrame.html', context=data)