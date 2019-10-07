#!/usr/bin/env python
import PySimpleGUI as sg
"""
    Demonstration of MENUS!
    How do menus work?  Like buttons is how.
    Check out the variable menu_def for a hint on how to 
    define menus
"""
def second_window():

    layout = [[sg.Text('The second form is small \nHere to show that opening a window using a window works')],
              [sg.OK()]]

    window = sg.Window('Second Form', layout)
    event, values = window.read()
    window.close()

def test_menus():


    sg.change_look_and_feel('LightGreen')
    sg.set_options(element_padding=(0, 0))

    # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open', '&Save', '&Properties', 'E&xit' ]],
                ['&Edit', ['&Paste', ['Special', 'Normal',], 'Undo'],],
                ['&Toolbar', ['---', 'Command &1', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['&Help', '&About...'],]

    # ------ GUI Defintion ------ #
    layout = [
              [sg.Menu(menu_def, tearoff=False, pad=(20,1))],
              [sg.Output(size=(60,20))],
              ]

    window = sg.Window("Windows-like program",
                       layout,
                       default_element_size=(12, 1),
                       auto_size_text=False,
                       auto_size_buttons=False,
                       default_button_element_size=(12, 1))

    # ------ Loop & Process button menu choices ------ #
    while True:
        event, values = window.read()
        if event is None or event == 'Exit':
            return
        print('Event = ', event)
        # ------ Process menu choices ------ #
        if event == 'About...':
            window.disappear()
            sg.popup('About this program','Version 1.0', 'PySimpleGUI rocks...', grab_anywhere=True)
            window.reappear()
        elif event == 'Open':
            filename = sg.popup_get_file('file to open', no_window=True)
            print(filename)
        elif event == 'Properties':
            second_window()

test_menus()