import PySimpleGUI as sg
# import PySimpleGUIWx as sg
# import PySimpleGUIQt as sg
import time

"""
    Design pattern - System Tray and GUI Window
    
    This design pattern will show you how to run a system tray icon and a GUI window
    simultaneously.  BOTH the system tray and the window will be active at the same time.
    
    The "close window" action is similar to what most windows programs do that have a tray icon.
    When you close the window with an "X", it closes the GUI window and shows a message in the
    tray that the window has been "Minimized".
    
    To make things "easier", a new window is created each time rather than trying to hide and unhide.
    On some systems, the hide method doesn't work very well (Raspberry Pi for example).
    
    You can "Minimize" to the tray in 3 ways in this program:
        1. Click the "X" on the window
        2. Click the button "Minimize to tray"
        3. Right click tray icon and choose "Hide"
        
    To exit the entire program, you will need to do this from the System tray by choosing "Exit"
    
    Copyright 2020 PySimpleGUI.org
"""

icon = sg.DEFAULT_BASE64_ICON

sg.theme('Dark Red')
delay_time = 15 * 60

def time_as_int():
    return int(round(time.time()))

def make_a_window():

    layout = [  [sg.Text(f'{delay_time // 60 % 60:2}:{delay_time % 60:02}', key='-OUT-', size=(20, 2), justification='c', font='Any 24')],
                [sg.Button('Start', size=(10,1))],[sg.Button('Minimize\nTo Tray', size=(10,2))]  ]

    return sg.Window('Window Title', layout, element_justification='c', icon=icon)

def main():

    menu_def = ['UNUSED', ['Show','Hide','Exit']]

    tray = sg.SystemTray(menu=menu_def, data_base64=icon)
    window = make_a_window()
    start, current, paused = time_as_int(), 0, True

    while True:
        event = tray.read(timeout=100)
        if event == 'Exit':
            break
        elif event in('Show', sg.EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED) and not window:
            print('Showing a new window')
            window, paused = make_a_window(), True
        elif event == 'Hide' and window:
            window.close()
            window = None

        if window:
            event, values = window.read(timeout=1000)
            if event in (sg.WIN_CLOSED, 'Minimize\nTo Tray'):
                print('Minimizing to tray')
                tray.show_message('Minimizing', 'Minimizing to Tray')
                window.close()
                window = None
                continue
            elif event == 'Start':
                start, paused = time_as_int(), False
            if not paused:
                remaining = delay_time - (time_as_int() - start)
                if remaining < 0:
                    tray.show_message('Look away', 'It is time to look away for 20 seconds')
                    start = time_as_int()
                else:
                    window['-OUT-'].update(f'{remaining//60%60:2}:{remaining%60:02}')
    tray.close()
    if window:
        window.close()


main()