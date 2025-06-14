from Back_end import manager
from flask import render_template
from Front_end import frontManager

mainFrame_file = "Codes/Front_end/templates/mainFrame.html"

def reset_htmlFile(pathFile: str):
    file = open(pathFile, "w")
    file.write("<!DOCTYPE html><html><head><title>Storytelling Game</title><style>body, html {height: 100%;margin: 0;justify-content: center;align-items: center;background-color: #f0f0f0;font-family: sans-serif;} .form-container {text-align: center;}input {margin: 3px;font-size: larger;width: 200px; height: 50px}</style></head>")
    # ^ this creates styling for the mainFrame html

def get_Beginning_Scene_Name():
    all_scene_names = manager.get_all_scene_names()
    for scene_name in all_scene_names:
        dic_status = manager.get_status_from_scene(scene_name)[0]
        if dic_status["status"] == "Beginning":
            return scene_name
    return "No beginning scene found"

def check_if_end_scene_exist():
    all_scene_names = manager.get_all_scene_names()
    for scene_name in all_scene_names:
        dic_status = manager.get_status_from_scene(scene_name)[0]
        if dic_status["status"] == "End":
            return True
    return False

def write_Scene_in_MainFrame(scene_name: str, is_disable_scene: bool):
    file = open(mainFrame_file, "a")
    scene_background = manager.get_image_as_base64(manager.get_background_image_in_scene(scene_name))
    file.write("<div class='form-container'>")
    file.write(f"<form action='/scene/{scene_name}' method='get'>")
    file.write(f"<input type='submit' value='{scene_name}' {'disabled' if is_disable_scene else ''} style=background-image:url({scene_background}) />")
    file.write("</form>")
    file.write("</div>")
    file.close()


def get_scene_names_from_scene_choices(scene_name: str):
    scene_names_from_choices = []
    choices = manager.get_choices_from_scene(scene_name)
    for choice in choices:
        scene_names_from_choices.append(choice["scenename"])
    return scene_names_from_choices

def generate_all_layers_in_tree(scene_names: list):
    all_seen_scenes: list = frontManager.get_cookie(frontManager.COOKIE_ALL_SEEN_SCENES_KEY, [])
    file = open(mainFrame_file, "a")
    
    for scene in scene_names:
        is_disable_scene = all_seen_scenes.count(scene) == 0
        if manager.get_status_from_scene(scene)[0]["status"] == 'Beginning':
            is_disable_scene = False
        write_Scene_in_MainFrame(scene, is_disable_scene)

    choices_of_next_layer = []
    for scene in scene_names:
        if manager.get_status_from_scene(scene)[0]["status"] != "End":
            choices_of_next_layer.extend(get_scene_names_from_scene_choices(scene))
    if choices_of_next_layer != []:
        generate_all_layers_in_tree(choices_of_next_layer)
    file.close()
    
    
def start():
    
    if check_if_end_scene_exist() == False:
        return "Error: No End-Scene in Scenes"

    reset_htmlFile(mainFrame_file)

    beginning_scene_name = get_Beginning_Scene_Name()
    

    file = open(mainFrame_file, "a")
    file.write("<body>")
    file.write("<div class='form-container'>")
    file.close()
    generate_all_layers_in_tree([beginning_scene_name])
    file = open(mainFrame_file, "a")
    file.write("</div>")
    file.write("</body>")
    file.write("</html>")
    file.close()
    
    return render_template('mainFrame.html', context=[])