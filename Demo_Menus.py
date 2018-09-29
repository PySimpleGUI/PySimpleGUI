#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI_mod as sg
else:
    import PySimpleGUI27 as sg
"""
    Demonstration of MENUS!
    How do menus work?  Like buttons is how.
    Check out the variable menu_def for a hint on how to 
    define menus
"""
def SecondForm():

    layout = [[sg.Text('The second form is small \nHere to show that opening a window using a window works')],
              [sg.OK()]]

    window = sg.Window('Second Form').Layout(layout)
    b, v = window.Read()


def TestMenus():
    import PySimpleGUI as sg

    sg.ChangeLookAndFeel('LightGreen')
    sg.SetOptions(element_padding=(0, 0))

    # ------ Menu Definition ------ #
    menu_def = [['&File', ['&Open', '&Save', '---', 'Properties', 'E&xit' ]],
                ['&Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                [''
                 '&Help', '&About...'],]

    # ------ GUI Defintion ------ #
    layout = [
            [sg.Menu(menu_def, tearoff=False)],
              [sg.Output(size=(60,20))],
            [sg.In('Test', key='input', do_not_clear=True)]
              ]

    window = sg.Window("Windows-like program", default_element_size=(12, 1), auto_size_text=False, auto_size_buttons=False,
                       default_button_element_size=(12, 1)).Layout(layout)

    # ------ Loop & Process button menu choices ------ #
    while True:
        button, values = window.Read()
        if button is None or button == 'Exit':
            return
        print('Button = ', button)
        # ------ Process menu choices ------ #
        if button == 'About...':
            window.Hide()
            sg.Popup('About this program','Version 1.0', 'PySimpleGUI rocks...', grab_anywhere=True)
            window.UnHide()
        elif button == 'Open':
            filename = sg.PopupGetFile('file to open', no_window=True)
            print(filename)
        elif button == 'Properties':
            SecondForm()



TestMenus()