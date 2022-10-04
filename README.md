
<p align="center"><img src="https://user-images.githubusercontent.com/107058068/193857918-6fed00c0-2144-47d3-83a3-26c2837ebc81.png" alt="WindowsStartupWithoutRights" width="100px" height="100px"></p>
<h1 align="center">Windows Startup Without Permission</h1>

# Description
Windows Startup Without Permission script — this script is written in <a href="https://en.wikipedia.org/wiki/Batch_file">batch</a> and allows you to run programs for Windows without administrator rights.

# Script (batch)
```batch
@echo off
chcp 1251>nul
color 0f
echo Metros Software (script type: Windows Startup Without Permission). (version 1.0 2022).
echo.
echo Current path: %cd%
set /p mswswp_filename=Enter the full path to the program to run it: 
cmd /min /C "set __COMPAT_LAYE 	R=RunAsInVoker && start %mswswp_filename%
```

> To run, you just need to run the batch file and enter the name of the windows executable file.

# Script (python3)
```python3
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
```

> Addition in Python version 3 in addition, it is possible to use a startup parameter that takes the name of the executable file.
