import PySimpleGUI as sg

"""
    Demo - Changing your window's theme at runtime
    * Create your window using a "window create function"
    * When your window's theme changes, close the window, call the "window create function"
    
    Copyright 2021 PySimpleGUI
"""


# ------------------- Create the window -------------------
def make_window(theme=None):
    if theme:
        sg.theme(theme)
    # -----  Layout & Window Create  -----
    layout = [[sg.T('This is your layout')],
              [sg.Button('Ok'), sg.Button('Change Theme'), sg.Button('Exit')]]

    return sg.Window('Pattern for changing theme', layout)


# ------------------- Main Program and Event Loop -------------------
def main():
    window = make_window()

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        if event == 'Change Theme':      # Theme button clicked, so get new theme and restart window
            event, values = sg.Window('Choose Theme', [[sg.Combo(sg.theme_list(), readonly=True, k='-THEME LIST-'), sg.OK(), sg.Cancel()]]).read(close=True)
            print(event, values)
            if event == 'OK':
                window.close()
                window = make_window(values['-THEME LIST-'])

    window.close()


if __name__ == '__main__':
    main()