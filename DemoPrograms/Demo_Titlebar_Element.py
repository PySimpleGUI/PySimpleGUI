import PySimpleGUI as sg

"""
    The Custom Titlebar Demo
    3 ways of getting a custom titlebar:
    1. set_options - will create a titlebar that every window will have based on theme
    2. Titlebar element - Adds custom titlebar to your window
    3. use_custom_titlebar parameter - Add to your Window object
    
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.

"""

# sg.set_options(use_custom_titlebar=True)
# sg.set_options(titlebar_background_color='red', titlebar_text_color='white', titlebar_font='courier 12', )



def main():
    layout = [
        # [sg.Titlebar('My Custom Titlebar', background_color='light blue', text_color='red', k='-T-')],
        [sg.Text('My Window')],
        [sg.Input(k='-IN1-')],
        [sg.Input(k='-IN2-')],
        [sg.Input(k='-IN3-')],
        [sg.Button('Clear'), sg.Button('Popup'), sg.Button('Exit')]]

    # Use the same title so that when the window minimizes, the title will be the same as the custom titlebar title
    # window = sg.Window('My Custom Titlebar', layout)
    window = sg.Window('My Custom Titlebar', layout, use_custom_titlebar=True)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Clear':
            [window[k]('') for k in ('-IN1-', '-IN2-', '-IN3-')]
        elif event == 'Popup':
            sg.popup('This is a popup')

    window.close()


main()
