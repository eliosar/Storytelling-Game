# check if at least one scene is available/ready before anything alse
import manager, addScene

if manager.is_at_least_one_scene_available():
    pass
else:
    print('no scene folder has been found')
    manager.create_folder_sceleton()
    addScene.addScene()