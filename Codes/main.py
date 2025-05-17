from Back_end import manager
import addScene

manager.create_folder_sceleton()

if manager.is_at_least_one_scene_available():
    decision = input('Do you want to add a new Scene?(y/n): ')
    if decision == 'y':
        addScene.addScene()
else:
    print('No scene folder has been found')
    addScene.addScene()