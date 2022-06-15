import PySimpleGUI as sg

"""
    Demo - User Setting API to save and load a window's contents

    The PySimpleGUI "User Settings API" is a simple interface to JSON and Config Files.
    If you're thinking of storying information in a JSON file, consider using the PySimpleGUI
        User Settings API calls.  They make JSON files act like dictionaries.  There's no need
        to load nor save as that's done for you.

    There are 2 interfaces to the User Settings API.
        1. Function calls - sg.user_settings
        2. UserSettings Object - Uses a simple class interface

    Note that using the Object/class interface does not require you to write a class.  If you're using
    PySimpleGUI, you are already using many different objects.  The Elements & Window are objects.

    In this demo, a UserSetting object is used to save the values from Input elements into a JSON file.
    You can also re-loda the values from the JSON into your window.

    Copyright 2022 PySimpleGUI
"""

# Create a UserSettings object. The JSON file will be saved in the same folder as this .py file
window_contents = sg.UserSettings(path='.', filename='mysettings.json')

def main():
    layout = [  [sg.Text('My Window')],
                [sg.Input(key='-IN1-')],
                [sg.Input(key='-IN2-')],
                [sg.Input(key='-IN3-')],
                [sg.Input(key='-IN4-')],
                [sg.Input(key='-IN5-')],
                [sg.Button('Save'), sg.Button('Load'), sg.Button('Exit')]  ]

    window = sg.Window('Save / Load Inputs Using User Settings API', layout)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        # To SAVE the values, loop through all elements in the values dictionary and save their values
        if event == 'Save':
            for key in values:
                window_contents[key] = values[key]
        # To LOAD values from a settings file into a window, loop through values dictionary and update each element
        if event == 'Load':
            for key in values:
                saved_value = window_contents[key]
                window[key].update(saved_value)

    window.close()

if __name__ == '__main__':
    main()
