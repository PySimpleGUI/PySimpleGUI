import PySimpleGUIQt as sg
import webbrowser
import subprocess

# Destinations
VIEW_ISSUES_URL = r'https://github.com/MikeTheWatchGuy/PySimpleGUI/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc'
PULL_REQUEST_URL = r'https://github.com/MikeTheWatchGuy/PySimpleGUI/compare/master...Dev-latest'
DISCORD = r"C:\Users\mike\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk"

def system_tray():

    menu_def = ['UNUSED',
                ['Discord', 'Chrome', 'Open Issues', 'Pull Request', 'Exit']]
    # tray = sg.SystemTray(menu=menu_def, filename='myicon.ico', tooltip='My System Tray Launcher')
    tray = sg.SystemTray(menu=menu_def, data_base64=logo, tooltip='My System Tray Launcher')

    # The Event Loop runs every 5000ms
    poll_frequncy = 5000

    tray.ShowMessage('Starup', 'System tray launcher has started')

    while True:
        menu_item = tray.Read(timeout=poll_frequncy)

        if menu_item == 'Exit':
            break
        if menu_item == sg.EVENT_SYSTEM_TRAY_ICON_ACTIVATED:
            # TODO Insert code to get number of emails... this is a demo only...
            tray.ShowMessage('You clicked me', 'You have 18 new emails')
        elif  menu_item.startswith('Chrome'):       # The launches do work however
            webbrowser.open_new('http://')
        elif  menu_item.startswith('Open'):
            webbrowser.open_new_tab(VIEW_ISSUES_URL)
        elif  menu_item.startswith('Pull'):
            webbrowser.open_new_tab(PULL_REQUEST_URL)
        elif menu_item == 'Discord':
            sp = subprocess.Popen([DISCORD, ''], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

logo = b'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'

system_tray()