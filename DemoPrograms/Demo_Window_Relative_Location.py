import PySimpleGUI as sg

"""
    Demo - Relative Location
    
    How to create a window at a location relative to where it would normally be placed.
    
    Normally, by default, windows are centered on the screen. 
    Other ways initial window position is determined:
    1. You can also specify the location when creating it by using the location parameter
    2. You can use set_options to set the location all windows will be created
    
    This demo shows how to use the paramter to Window called relative_location.
    
    As the name suggests, it is a position relative to where it would normally be created.
    
    Both positive and negative values are valid.  
        relative_location=(0, -150) will create the window UP 150 pixels from where it would normally be created

    Copyright 2021 PySimpleGUI
"""


def second_window():
    layout = [[sg.Text('Window 2\nrelative_location=(0,-150)')],
              [sg.Button('Exit')]]

    window = sg.Window('Window 2', layout, relative_location=(0,-150), finalize=True)
    return window


def main():
    sg.set_options(font='_ 18', keep_on_top=True)
    layout = [  [sg.Text('Window 1\nrelative_location=(0,150)')],
                [sg.Button('Popup'), sg.Button('Exit')]  ]

    window = sg.Window('Window 1', layout, relative_location=(0,150), finalize=True)

    window2 = second_window()

    while True:             # Event Loop
        window, event, values = sg.read_all_windows()
        if window == None:      # If all windows were closed
            break
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
        if event == 'Popup':
            sg.popup('Popups will go to the center of course!')

    sg.popup_no_buttons('All windows closed... Bye!', background_color='red', text_color='white', auto_close_duration=3, auto_close=True, no_titlebar=True)

if __name__ == '__main__':
    main()