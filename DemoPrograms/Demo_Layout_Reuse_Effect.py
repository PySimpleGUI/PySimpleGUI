import PySimpleGUI as sg

"""
    Demo - Layout "Reuse" (but NOT reusing the layout)
    As cautioned in the PySimpleGUI documentation, layouts cannot be "reused".
    
    That said, there is a very simple design pattern that you'll find in many many
    Demo Programs.  Any program that is capable of changing the theme uses this
    same kind of pattern.
    
    Goal - write the layout code once and then use it multiple times
        The layout is reused 
    
    Solution - create the layout and window in a function and return it

    Copyright 2021 PySimpleGUI
"""


def make_window():
    """
    Defines the layout and creates the window.

    This will allow you to "reuse" the layout.
    Of course, the layout isn't reused, it is creating a new copy of the layout
    every time the function is called.

    :return: newly created window
    :rtype: sg.Window
    """

    # ------------------- Layout Definition -------------------
    layout = [[sg.Text('This is your layout')],
              [sg.Input(key='-IN-')],
              [sg.Text('You typed:'), sg.Text(size=(20,1), key='-OUT-')],
              [sg.Button('Go'), sg.Button('Dark Gray 13 Theme'), sg.Button('Exit')]]

    # ------------------- Window Creation -------------------
    return sg.Window('Window Title', layout)

def main():
    """
    Your main program that contains your event loop
    Rather than creating the layout and Window in this function, you will
    instead call the make_window function to make the layout and Window
    """

    window = make_window()      # create the window

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Go':
            # change the "output" element to be the value of "input" element
            window['-OUT-'].update(values['-IN-'])
        elif event.startswith('Dark'):
            sg.theme('Dark Gray 13')
            window.close()              # close the window
            window = make_window()      # make a new window with the "same layout"

    window.close()


if __name__ == '__main__':
    main()