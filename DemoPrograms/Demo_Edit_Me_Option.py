import PySimpleGUI as sg

"""
    Demo "Edit Me" (and Version)
    
    More and more of these Demos are getting an "Edit me" option added.
    
    It's a big time saver to be able to right click and choose "Edit me" to edit a program you're developing.
    It's maybe an even bigger time saver if you've not worked on it for some time and have forgotten where
        the source code is located on your computer.  
        
    You can add this capability to your program by adding a right click menu to your window and calling the
    editor that you set up in the global PySimpleGUI options.
    
    A constant MENU_RIGHT_CLICK_EDITME_VER_EXIT, when set at the right click menu shows a "Version" and "Edit Me" meny item.
    
    You will need to have first set up your editor by using the menu in sg.main()
    
    Copyright 2021, 2022, 2023 PySimpleGUI.org
"""


layout = [[sg.Text('Edit this program by right clicking and choosing "Edit me"')],
          [sg.Button('Exit')]]

window = sg.Window('Edit Me Right Click Menu Demo', layout, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT)

while True:  # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Edit Me':
            sg.execute_editor(__file__)
    elif event == 'Version':
            sg.popup_scrolled(__file__, sg.get_versions(), location=window.current_location(), keep_on_top=True, non_blocking=True)

window.close()
