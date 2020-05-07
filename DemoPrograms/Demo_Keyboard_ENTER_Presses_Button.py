import PySimpleGUI as sg
"""
    tkinter and Qt do not "activate" buttons by pressing the ENTER key with the button highlighted / in focus
    This demo will enable the application to click on a button if the button has focus (is highlighted) and the
    user presses the ENTER key.
    NOTE that the SPACE BAR works correctly out of the box with both tkinter and Qt.  If a button has focus and 
    you press the space bar, then tkinter and Qt will both consider that a button click.  But not so with the ENTER
    key.
    
    The solution is for your program to read the keyboard presses and act upon those directly.  It's trivial logic
    in the end:
    1. Get a key press
    2. See if the key is the ENTER key
    3. Find the Element that currently has focus
    4. Click the Button if the Element with focus is a button 

"""

QT_ENTER_KEY1 = 'special 16777220'
QT_ENTER_KEY2 = 'special 16777221'

layout = [[sg.Text('Test of Enter Key use')],
          [sg.Input(key='-IN-')],
          [sg.Button('Button 1', key='-1-')],
          [sg.Button('Button 2', key='-2-')],
          [sg.Button('Button 3', key='-3-')], ]

window = sg.Window('My new window', layout,
                   return_keyboard_events=True)
while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event in ('\r', QT_ENTER_KEY1, QT_ENTER_KEY2):         # Check for ENTER key
        # go find element with Focus
        elem = window.find_element_with_focus()
        if elem is not None and elem.Type == sg.ELEM_TYPE_BUTTON:       # if it's a button element, click it
            elem.Click()
        # check for buttons that have been clicked
    elif event == '-1-':
        print('Button 1 clicked')
    elif event == '-2-':
        print('Button 2 clicked')
    elif event == '-3-':
        print('Button 3 clicked')

window.close()