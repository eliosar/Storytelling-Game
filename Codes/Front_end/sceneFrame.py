from Back_end import manager
from flask import render_template

def start(scene_name: str):
    background_64 = manager.get_image_as_base64(manager.get_background_image_in_scene(scene_name))
    choices_as_str = []
    choices_next_scene_url = []
    texts_as_str = []
    speekers = []
    icons = []
    other_urls = []

    choices = manager.get_choices_from_scene(scene_name)
    texts = manager.get_texts_from_scene(scene_name)
    
    for choice in choices:
        choices_as_str.append(choice["choicename"])
        choices_next_scene_url.append(manager.join_paths(('/scene', choice["scenename"])))

    for text in texts:
        texts_as_str.append(text["text"])
        image = manager.get_speeker_image(text["speekername"])
        speekers.append(manager.get_image_as_base64(image))
    
    home_icon = manager.get_image_as_base64(manager.get_icon_image('home.jpeg'))
    icons.append(home_icon)

    other_urls.append('/')
    
    data = (scene_name, background_64, choices_as_str, choices_next_scene_url, texts_as_str, speekers, icons, other_urls)
    return render_template('sceneFrame.html', context=data)