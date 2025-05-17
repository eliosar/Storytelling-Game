import handleFiles

def save_file(data: list, file_path:str):
    print('there is nothing here currently')
    # file_name = handleFiles.get_name_from_path(file_path)

    # print('saving to: ' + file_name)
    # with open(file_path, 'wb') as file:
    #     pickle.dump(data, file)

    # print(file_name + ' saved')


def load_file(file_path:str):
    file_name = handleFiles.get_name_from_path(file_path)
    data = []
    
    with open(file_path, 'rb') as file:
        data = file.read()

    print(file_name + ' loaded')

    return data