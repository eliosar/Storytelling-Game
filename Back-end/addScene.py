import manager

def addScene():
    decision = ''
    finished = False

    print('Please put the new Scene into the "Dump"-folder')
    print('You can look up the rules for creating your Scene-Folder in the README-File')
    
    while finished == False:
        while decision != 'n' and decision != 'y':
            decision = input('Are you finished? (y/n)')
        
        if decision == 'y':
            print('We see, if everything is as it should be')
            finished = manager.is_dump_file_right()

            if finished == True:
                manager.add_new_scene_from_dump_file()
            else:
                print('please try to go over the problems and correct them')