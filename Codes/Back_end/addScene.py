import manager

def addScene():
    finished = False
    
    while finished == False:
        decision = ''
        
        print('Please put the new Scene into the "Dump"-folder')
        print('You can look up the rules for creating your Scene-Folder in the README-File')

        while decision != 'n' and decision != 'y':
            decision = input('Are you finished?(y/n): ')
        
        if decision == 'y':
            print('We see, if everything is as it should be\n')
            finished = manager.is_dump_file_right()

            if finished == True:
                finished = manager.is_dump_scenename_unique()
                if finished == True:
                    print('The folder follows the rules')
                    decision = input('Do you want to move it to the scenes-folder? (y/n)')
                    manager.add_new_scene_from_dump_file()
            
            if finished == False:
                print('Please try to go over the problems and correct them')
        else:
            finished = True