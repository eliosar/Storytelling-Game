# check if at least one scene is available/ready before anything alse
import manager, addScene

manager.create_folder_sceleton()

if manager.is_at_least_one_scene_available():
    pass
else:
    print('no scene folder has been found')
    addScene.addScene()