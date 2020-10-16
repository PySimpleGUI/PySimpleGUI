import PySimpleGUI as sg

"""
    Demo - Basic window design pattern
    * Creates window in a separate function for easy "restart"
    * Saves theme as a user variable
    * Puts main code into a main function so that multiprocessing works if you later convert to use
    
    Copyright 2020 PySimpleGUI.org
"""


# ------------------- Create the window -------------------
def make_window():
    # Set theme based on previously saved
    sg.theme(sg.user_settings_get_entry('theme', None))

    # -----  Layout & Window Create  -----
    layout = [[sg.T('This is your layout')],
               [sg.OK(), sg.Button('Theme', key='-THEME-'), sg.Button('Exit')]]

    return sg.Window('Pattern for theme saving', layout)


# ------------------- Main Program and Event Loop -------------------

def main():
    window = make_window()

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        if event == '-THEME-':      # Theme button clicked, so get new theme and restart window
            ev, vals = sg.Window('Choose Theme', [[sg.Combo(sg.theme_list(), k='-THEME LIST-'), sg.OK(), sg.Cancel()]]).read(close=True)
            if ev == 'OK':
                window.close()
                sg.user_settings_set_entry('theme', vals['-THEME LIST-'])
                window = make_window()

    window.close()


if __name__ == '__main__':
    main()

