"""
    Module to sync folders to HardDrive

    1. Select Folders to sync
    2. remember folders for next time
    3. verify if files exist
    4. notify user


"""

import os

def ask_for_folders():
    """ ask for folders """

    print('which folders do you want to sync')
    folders_to_copy = []
    check_if_done = True

    while check_if_done == True :
        folder = input('Type Folder')
        folders_to_copy.append(folder)
        ansy = input('do you want to add more ?')
        if ansy == 'n' or ansy == 'no':
            check_if_done = False
    with open('./backup_setting.txt') as fhand:
        fhand.writelines(folders_to_copy)
    return folders_to_copy

if os.path.isfile('./backup_setting.txt'):
    response_list = ['y','n','yes','no','nah','yea']
    answer = ""

    while answer != 'y' and answer != 'n':
        answer = input('Do you want to back up the same folders as last time ?') \
    ### WRONG INPUT
    if answer == 'y':
        with open ('./backup_setting.txt') as fhand:
                last_backup = fhand.readlines()
                print(last_backup[-1])
    elif answer == 'n':
        backup_folder_list = ask_for_folders()
        print(backup_folder_list)

else:
    print("You don't have any past backups we'll do a new one")
    backup_folder_list = ask_for_folders()
    print(backup_folder_list)
