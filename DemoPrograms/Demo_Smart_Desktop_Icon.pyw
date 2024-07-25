"""

Creates what appears to be an icon on your desktop, but is in reality a PySimpleGUI program.

Copyright 2024 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""



import PySimpleGUI as sg

def main():
    icon=sg.EMOJI_BASE64_COOL

    #------- GUI definition & setup --------#

    sg.theme('black')


    layout = [[sg.Image(source=icon, key='-IMAGE-', p=0, enable_events=True)]]

    window = sg.Window('Desktop Icon Demo', layout, element_justification='center', finalize=True, resizable=True, no_titlebar=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, margins=(0,0), grab_anywhere=True, auto_save_location=True)

    window['-IMAGE-'].bind('<Double-Button-1>', '+DOUBLE_CLICK+')

    #------------ The Event Loop ------------#
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        # Add your double-click action here... such as launching another program
        if event == '-IMAGE-+DOUBLE_CLICK+':
            sg.popup_quick_message('Double Clicked', location=window.current_location(), font='_ 20', background_color='red', text_color='white')
            # Example of launch explorer when the icon is double-clicked.  Add change to your own program.
            sg.execute_command_subprocess('explorer', wait=False)
        elif event == 'Version':
            sg.popup_scrolled(sg.get_versions(), f'This Program: {__file__}' ,keep_on_top=True, non_blocking=True, location=window.current_location())
        elif event == 'Edit Me':
            sg.execute_editor(__file__)

    window.close()

if __name__ == '__main__':

    main()