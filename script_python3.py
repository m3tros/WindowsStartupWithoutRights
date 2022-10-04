import os
import sys

def main(filename=None):
    print('Metros Software (script type: Windows Startup Without Permission). (version 1.0 2022).')
    if filename == None:
        print(f'Current path: {os.getcwd()}')
        filename = input('Enter the full path to the program to run it: ')
    else:
        if os.path.isfile(filename) == True:
            print(f'File name: {filename}')
        else:
            print(f'[ERROR]: Could not find the file: {filename}')
            sys.exit()
    os.system(f'cmd /min /C "set __COMPAT_LAYE 	R=RunAsInVoker && start {filename}')

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
    except IndexError:
        filename = None
    main(filename)
