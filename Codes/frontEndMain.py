from Front_end import mainFrame, sceneFrame, frontManager
from flask import Flask, redirect

app = Flask(__name__, template_folder='Front_end/templates/')

@app.route('/', methods=['get'])
def main_view():
    return mainFrame.start()

@app.route('/scene/<scene_name>', methods=['get'])
def scene_view(scene_name: str):
    return sceneFrame.start(scene_name)

@app.route('/scene/<scene_name>/<text_index>', methods=['get'])
def change_text(scene_name: str, text_index: str):
    resp = frontManager.make_response(redirect(f'/scene/{scene_name}'))

    frontManager.set_cookie(frontManager.COOKIE_TEXT_INDEX_KEY, text_index, resp)
    frontManager.set_cookie(frontManager.COOKIE_CURRENT_SCENE_NAME_KEY, scene_name, resp)

    return resp
    

def start():
    app.run(debug=True)

if __name__ == '__main__':
    start()