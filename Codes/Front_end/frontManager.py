from flask import request, make_response, Response
import json

COOKIE_TEXT_INDEX_KEY = 'text_index'
COOKIE_CURRENT_SCENE_NAME_KEY = 'current_scene_name'
COOKIE_ALL_SEEN_SCENES_KEY = 'all_seen_scenes'

# https://www.geeksforgeeks.org/flask-cookies/

def set_cookie(key: str, value, resp: Response):
    resp.set_cookie(key=key, value=json.dumps(value), max_age=None, expires=None)

def get_cookie(key: str, default: any):
    '''
    :param key: the key to the cookie
    :param default: the value you get, when no cookie with this key is found
    '''
    json_cookie = request.cookies.get(key, json.dumps(default))
    return json.loads(json_cookie)

def create_response(thing):
    return make_response(thing)