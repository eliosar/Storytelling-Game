from Back_end import manager
from flask import render_template

def start(scene_name: str):
    background_path = manager.get_background_from_scene_as_base64(scene_name)
    
    data = (background_path,)
    return render_template('sceneFrame.html', context=data)