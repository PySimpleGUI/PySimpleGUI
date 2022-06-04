import PySimpleGUI as sg

"""
    Demo - User Settings as a Database

    The PySimpleGUI User Settings APIs are implemnted to look like a dictionary to the
    user and utilize JSON files to store the data.  As a result, one "key" is used to 
    store and retrieve each "setting".  This capability cab be used to implement a
    simple database.
    
    In this demo the User Settings file is used to store a user ID and data associated
    with that ID.  Each User ID has a dictionary stored in the User Settings file. This
    dictionary is built from the values dictionary of the window.  There is a map varaible
    called data_map that translates between the two dictionaries.
    
    Copyright 2022 PySimpleGUI
"""

def get_id_data(user_setting, id):
    return user_setting[id]

def main():
    # Maps between keys used in the User Settings an the Window itself
    data_map = {'-name-': '-NAME-', '-password-': '-PASSWORD-', '-dept-': '-DEPT-', '-security-': '-SECURITY-'}
    user_data = sg.UserSettings('my_user_data.json')
    INPUT_SIZE=30
    layout = [  [sg.Text('User ID Management')],
                [sg.Push(), sg.Text('User ID:'), sg.Input(key='-ID-', size=INPUT_SIZE)],
                [sg.Push(), sg.Text('Name:'), sg.Input(key='-NAME-', size=INPUT_SIZE,)],
                [sg.Push(), sg.Text('Password:'), sg.Input(key='-PASSWORD-', size=INPUT_SIZE, password_char='*')],
                [sg.Push(), sg.Text('Department:'), sg.Input(key='-DEPT-', size=INPUT_SIZE,)],
                [ sg.Text('Security Level:'), sg.Combo(('Low', 'Medium', 'High'), size=(INPUT_SIZE-2,3), readonly=True, default_value='Low', key='-SECURITY-')],

                [sg.Button('Add/Update'), sg.Button('Load'), sg.Button('Display'), sg.Button('Exit')]  ]

    window = sg.Window('User Settings as Database', layout)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Add/Update':
            # Make a dictionary of data for the ID being added/updated based on the window's values
            user = values['-ID-']
            data = {}
            for setting_key, values_key in data_map.items():
                data[setting_key] = values[values_key]
            user_data[user] = data
            sg.popup(f'Added or updated user: {values["-ID-"]}')
        elif event == 'Load':
            user = values['-ID-']
            data = user_data[user]
            for setting_key, values_key in data_map.items():
                value = data[setting_key] if data is not None else ''
                window[values_key].update(value)
        elif event == 'Display':
            user = values['-ID-']
            data = user_data[user]
            output = f'Detailed User Information for ID: {user}\n'
            for setting_key, values_key in data_map.items():
                value = data[setting_key] if data is not None else ''
                output += f'{setting_key} = {value}\n'
            sg.popup_scrolled(output, title='Detailed User Data')
if __name__ == '__main__':
    main()
