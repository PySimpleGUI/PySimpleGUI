import PySimpleGUIWx as sg

"""
    System Tray Icon
    Your very own peronsal status monitor in your system tray
    Super easy to use.
    1. Find an icon file or use this default
    2. Create your menu defintion
    3. Add if statements to take action based on your input

"""

ICON_FILE = r'C:\Icons\logo32x32.ico'

menu_def = ['UNUSED', ['My', 'Simple', '---', 'Menu', 'Exit']]

tray = sg.SystemTray(menu=menu_def, filename=ICON_FILE)

tray.ShowMessage('Starting', 'Now Starting the application')

while True:
    event = tray.Read()
    if event == 'Exit':
        break
    elif event == 'Menu':       # add your checks here
        pass
    tray.ShowMessage('Event', '{}'.format(event))