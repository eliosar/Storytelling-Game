from Front_end import mainFrame, sceneFrame
from flask import Flask

app = Flask(__name__, template_folder='Front_end/templates/')

@app.route('/')
def main_view():
    return mainFrame.start()

@app.route('/scene/<sceneName>')
def scene_view(sceneName: str):
    return sceneFrame.start(sceneName)

def start():
    app.run(debug=True)

if __name__ == '__main__':
    start()