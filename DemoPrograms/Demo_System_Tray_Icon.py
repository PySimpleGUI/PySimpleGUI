import PySimpleGUI as sg
# import PySimpleGUIWx as sg
# import PySimpleGUIQt as sg

"""
    System Tray Icon
    Your very own peronsal status monitor in your system tray
    Super easy to use.
    1. Find an icon file or use this default
    2. Create your menu defintion
    3. Add if statements to take action based on your input

    Note from the imports that this code works on all PySimpleGUI ports (except Web).
    For the tkinter port, however, the icon isn't located in the system tray. Instead it's located just above
    the system tray in the form of what looks like an "icon" on your desktop.  It's actually a very small window.
    
    In June 2021 a new package was added to the PySimpleGUI family - psgtray
    With this package, you can get a real system tray icon while using tkinter rather than a desktop-icon that this
        demo is demonstrating.  The Demo Program - Demo_psgtray_Tray_Icon_Tkinter - shows how to integrate it with PySimpleGUI 
    
    Copyright 2022 PySimpleGUI
"""




menu_def = ['UNUSED', ['My', '&Simple::my key', 'Has Sub', ['1','2'], '---', 'Menu', 'E&xit']]

tray = sg.SystemTray(menu=menu_def, data_base64=sg.DEFAULT_BASE64_ICON)

while True:
    event = tray.read()
    print(event)
    if event == 'Exit':
        break
    elif event == 'Menu':
        tray.show_message('Title', 'Hey, you clicked Menu!')
tray.close()