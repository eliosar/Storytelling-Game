from Back_end import manager
from flask import render_template
from Front_end import frontManager

def start(scene_name: str):
    text_index = int(frontManager.get_cookie(frontManager.COOKIE_TEXT_INDEX_KEY, '0'))
    current_scene_cookie: str = frontManager.get_cookie(frontManager.COOKIE_CURRENT_SCENE_NAME_KEY, '')
    all_seen_scenes: list = frontManager.get_cookie(frontManager.COOKIE_ALL_SEEN_SCENES_KEY, [])

    if current_scene_cookie != scene_name:
        text_index = 0
    
    if all_seen_scenes.count(scene_name) == 0:
        all_seen_scenes.append(scene_name)

    background_64 = manager.get_image_as_base64(manager.get_background_image_in_scene(scene_name))
    choices_as_str = []
    choices_next_scene_url = []
    texts_as_str = []
    speekers = []
    icons = []
    other_urls = []
    is_last_text = False

    choices = manager.get_choices_from_scene(scene_name)
    texts = manager.get_texts_from_scene(scene_name)
    
    if text_index == len(texts) - 1:
        for choice in choices:
            choices_as_str.append(choice["choicename"])
            choices_next_scene_url.append(manager.join_paths(('/scene', choice["scenename"])))
        
        is_last_text = True

    for text in texts:
        texts_as_str.append(text["text"])
        image = manager.get_speeker_image(text["speekername"])
        speekers.append(manager.get_image_as_base64(image))
    
    home_icon = manager.get_image_as_base64(manager.get_icon_image('home.jpeg'))
    next_text_icon = manager.get_image_as_base64(manager.get_icon_image('rightArrow.jpeg'))
    icons.append(home_icon)
    icons.append(next_text_icon)

    next_text_path = manager.join_paths(('/scene', scene_name, str(text_index + 1)))
    other_urls.append('/')
    other_urls.append(next_text_path)
    
    data = (scene_name, background_64, choices_as_str, choices_next_scene_url, texts_as_str, speekers, icons, other_urls, text_index, is_last_text)
    
    resp = frontManager.create_response(render_template('sceneFrame.html', context=data))
    frontManager.set_cookie(frontManager.COOKIE_CURRENT_SCENE_NAME_KEY, scene_name, resp)
    frontManager.set_cookie(frontManager.COOKIE_TEXT_INDEX_KEY, str(text_index), resp)
    frontManager.set_cookie(frontManager.COOKIE_ALL_SEEN_SCENES_KEY, all_seen_scenes, resp)
    
    return resp