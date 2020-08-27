import PySimpleGUI as sg
import subprocess

"""
    Demo PyCharm Launch - Edit this file button
    
    Quick demo to show you how to add a button to your code that when pressed will open the file
    in PyCharm for editing.
    
    Note that this is a Windows version.  You'll need a slightly different path for Linux.

    Copyright 2020 PySimpleGUI.org
"""

# Change this variable to match the location of your PyCharm folder. It should already have the batch file.
PYCHARM = r"C:\Program Files\JetBrains\PyCharm Community Edition 2019.1.1\bin\pycharm.bat"

layout = [  [sg.Text('Edit Window Using PyCharm')],
            [sg.Button('PyCharm Me'), sg.Button('Exit')]  ]

window = sg.Window('PyCharm Launch Demo', layout)

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'PyCharm Me':
        subprocess.Popen([PYCHARM, __file__], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

window.close()
