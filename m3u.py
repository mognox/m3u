#! python3
import os
while True:
    while True:
        print('Enter the name of the directory containing the game files, or enter "cd" ' + 
        'to use the current directory:')
        path = input()
        if path == 'cd':
            path = os.getcwd()
        if os.path.exists(path):
            break
        else:
            print('Please enter a directory that exists.')
            continue
    while True:
        print('Enter the name of the game you would like to create an .m3u file for.\n' +
        'To narrow down the search, include information such as the region ex. "(USA)".')
        gameName = input()
        if os.path.isfile(os.path.join(path, gameName) + '.m3u'):
            while True:
                print('An existing .m3u file matching the game name was found. Delete this file? y/n')
                delete = input().strip()
                if delete == 'n':
                    break
                if delete == 'y':
                    os.remove(os.path.join(path, gameName) + '.m3u')
                    break
                else:
                    print('Please enter either "y" or "n".')
                    continue
        for file in os.listdir(path):
            if gameName in file:
                if file.endswith('.cue') or file.endswith('.chd'):
                    print('Found applicable file: %s' % (file))
                    m3u = open(os.path.join(path, gameName) + '.m3u', 'a')
                    m3u.write(file + '\n')
                    m3u.close()
        try:
            m3u = open(os.path.join(path, gameName) + '.m3u', 'r')
        except FileNotFoundError:
            print('No files matching the name provided were found.')
            continue
        m3uContent = m3u.read()
        print('The following is the content of the .m3u file:\n' + m3uContent + 'Is this acceptable? '
        + 'Enter any key except "n" to save this file.')
        m3u.close()
        end = input().strip()
        if end == 'n':
            print('Quit the program or search again? Enter "s" to search or any other key to quit.')
            redo = input().strip()
            if redo == 's':
                continue
            else:
                quit()
        else:
            print('Would you like to create another .m3u file? If so, enter "y". To quit, enter any other key.')
            repeat = input().strip()
            if repeat == 'y':
                print('Would you like to change directories? If so, enter "y". If not, enter any other key.')
                changeDir = input().strip()
                if changeDir == 'y':
                    break
            else:
                print('The .m3u file can be found at: %s' % os.path.join(path, gameName) + '.m3u.\n' +
                'The filename is ' + gameName + '.m3u. Is this acceptable? Enter any key except "n" to quit.')
                rename = input().strip()
                if rename == 'n':   
                    while True:
                        try:
                            print('Enter what you would like the file to be called. Do not enter the file extension.')
                            newName = input()
                            os.rename(os.path.join(path, gameName) + '.m3u', os.path.join(path, newName + '.m3u'))
                            break
                        except:
                            print('Please enter a usable name.')
                            continue
                quit()