import PySimpleGUI as sg

"""
    Demo - User Setting API to automatically save and load Input Elements

    This Demo Program shows an easy way to add saving and loading of Input elements.  
    
    The variable keys_to_save is used to determine which elements will be saved to the user settings file.
    
    The function make_key returns a dictionary that's used as keyword parameters that are passed to the Input elements. Using this technique allows the Input elements in the layout to benefit from the docstrings provided by PySimpleGUI.  Another approach could be to use a function that returns an Input element, but that limits the flexibility for configuring Input elements.

    Copyright 2023 PySimpleGUI
"""

keys_to_save = ('-IN1-', '-IN2-', '-IN3-', '-IN4-')

def make_key(key):
    """
    Returns a dictionary that is used to pass parameters to an Input element.
    Another approach could be to return an Input element. The downside to that approach is
    the lack of parameters and associated docstrings when creating the layout.

    :param key:
    :return: Dict
    """
    return {'default_text':sg.user_settings_get_entry(key, ''), 'key':key}


def main():
    layout = [  [sg.Text('Automatically Load and Save Of Inputs', font='_ 15')],
                [sg.Text('Input 1'), sg.Input(**make_key('-IN1-'))],
                [sg.Text('Input 2'), sg.Input(**make_key('-IN2-'), background_color='green')],
                [sg.Text('Input 3'), sg.Input(**make_key('-IN3-'), text_color='blue')],
                [sg.Text('Input 4'), sg.Input(**make_key('-IN4-'), size=5)],
                [sg.Button('Exit (and save)', key='-EXIT SAVE-'), sg.Button('Exit without save')]  ]

    window = sg.Window('Save / Load Inputs Using User Settings API', layout)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit without save':
            sg.popup_quick_message('Exiting without save', text_color='white', background_color='red', font='_ 20')

            break
        elif event == '-EXIT SAVE-':
            sg.popup_quick_message('Saving settings & Exiting', text_color='white', background_color='red', font='_ 20')
            for key in keys_to_save:
                sg.user_settings_set_entry(key, values[key])
            break

    window.close()

if __name__ == '__main__':
    main()
