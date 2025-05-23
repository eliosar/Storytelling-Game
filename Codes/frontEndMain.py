from Front_end import mainFrame, sceneFrame
from flask import Flask

app = Flask(__name__, template_folder='Front_end/templates/')

@app.route('/', methods=['get'])
def main_view():
    return mainFrame.start()

@app.route('/scene/<scene_name>', methods=['get'])
def scene_view(scene_name: str):
    print(scene_name)
    return sceneFrame.start(scene_name)

def start():
    app.run(debug=True)

if __name__ == '__main__':
    start()