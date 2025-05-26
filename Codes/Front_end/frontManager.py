from flask import request, make_response, Response

COOKIE_TEXT_INDEX_KEY = 'text_index'
COOKIE_CURRENT_SCENE_NAME_KEY = 'current_scene_name'

# https://www.geeksforgeeks.org/flask-cookies/

def set_cookie(key: str, value: str, resp: Response):
    resp.set_cookie(key=key, value=str(value), max_age=None, expires=None)

def get_cookie(key: str, default: str):
    '''
    :param key: the key to the cookie
    :param default: the value you get, when no cookie with this key is found
    '''
    return request.cookies.get(key, default)

def create_response(thing):
    return make_response(thing)