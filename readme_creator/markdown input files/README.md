
<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Logo%20with%20text%20for%20GitHub%20Top.png" alt="Python GUIs for Humans">
  <h2 align="center">Windows Shortcut Creation</h2>
</p>

Create Windows Shortcuts to your python programs and any other file easily using this application created using PySimpleGUI.


![image](https://user-images.githubusercontent.com/46163555/137822565-f461a4b8-0cee-47bc-964b-f171abb53147.png)



## Installation

### Old-school Straight Pip

pip install psgshortcut

### pip via `python -m pip` the python recommended way

#### If `python` is your command

python -m pip install psgshortcut

#### If `python3` is your command

python3 -m pip install psgshortcut

## Usage

Open a command window and type:   

psgshortcut   


## Create a Shortcut To This Program


Use this program to make a shortcut to itself so that you can then put on your desktop or pin to your taskbar or ???


To do this, follow these steps:

1. Open a command window (I promise, it's the last time you'll need to for this program)
2. Type - `where psgshortcut`
3. Copy the line that `where psgshortcut` gave you into the first input of the shortcut maker program
4. Run psgshortcut by typing `psgshortcut` in your command window
5. Right click and choose "File Location"
6. Copy the file location results, but change the extension from .py to .ico and paste into the Icon file input of the shortcut maker
7. Click "Create Shortcut"

This will create a shortcut in the same folder as the target file.  You can safely move this shortcut file to any place you want (like to your desktop).  Double-click the shortcut and your program should launch.

## Make Shortcuts To Anything

You can not only make shortcuts to Python programs, but you can make shortcuts to EXE and other files.  The GUI is self-explanatory.  Fill in the inputs, click the Make Shortcut button and you'll find the shortcut in the same folder as the target program.

## License

Licensed under an LGPL3 License

## This PyPI Was Designed and Written By

This program originated from the PySimpleGUI Demo Programs.  You'll find it here: 
[Demo_Make_Windows_Shortcut](https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Make_Windows_Shortcut.pyw)

Mike from PySimpleGUI.org 

## Contributing

Like the PySimpleGUI project, this project is currently licensed under an open-source license, the project itself is structured like a proprietary product. Pull Requests are not accepted.

## Copyright

Copyright 2021 PySimpleGUI
