import PySimpleGUI as sg

"""
    Demo "Edit Me"
    
    More and more of these Demos are getting an "Edit me" option added.
    
    It's a big time saver to be able to right click and choose "Edit me" to edit a program you're developing.
    It's maybe an even bigger time saver if you've not worked on it for some time and have forgotten where
        the source code is located on your computer.  
        
    You can add this capability to your program by adding a right click menu to your window and calling the
    editor that you set up in the global PySimpleGUI options.
    
    You need to do 2 things to make this work:
    1. Add a right click menu - requires you to add 1 parameter to your Window creation
    2. Add 1 if statement to your event loop.

    You will need to have first set up your editor by using the menu in sg.main()
    
    Copyright 2021 PySimpleGUI.org
"""


layout = [[sg.Text('Edit this program by right clicking and choosing "Edit me"')],
          [sg.Button('Exit')]]

window = sg.Window('Edit Me Right Click Menu Demo', layout, right_click_menu=[[''], ['Edit Me', 'Exit',]])

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Edit Me':
        sg.execute_editor(__file__)

window.close()
