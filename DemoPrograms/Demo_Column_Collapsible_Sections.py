import PySimpleGUI as sg

"""
    Demo - "Collapsible" sections of windows

    This demo shows one techinique for creating a collapsible section (Column) within your window.

    It uses the "pin" function so you'll need version 4.28.0+

    A number of "shortcut aliases" are used in the layouts to compact things a bit.
    In case you've not encountered these shortcuts, the meaning are:
    B = Button, T = Text, I = Input = InputText, k = key
    Also, both methods for specifying Button colors were used (tuple / single string)
    Section #2 uses them the most to show you what it's like to use more compact names.

    To open/close a section, click on the arrow or name of the section.
    Section 2 can also be controlled using the checkbox at the top of the window just to
    show that there are multiple way to trigger events such as these.

    Copyright 2020 PySimpleGUI.org
"""


SYMBOL_UP =    '▲'
SYMBOL_DOWN =  '▼'


def collapse(layout, key):
    """
    Helper function that creates a Column that can be later made hidden, thus appearing "collapsed"
    :param layout: The layout for the section
    :param key: Key used to make this seciton visible / invisible
    :return: A pinned column that can be placed directly into your layout
    :rtype: sg.pin
    """
    return sg.pin(sg.Column(layout, key=key))


section1 = [[sg.Input('Input sec 1', key='-IN1-')],
            [sg.Input(key='-IN11-')],
            [sg.Button('Button section 1',  button_color='yellow on green'),
             sg.Button('Button2 section 1', button_color='yellow on green'),
             sg.Button('Button3 section 1', button_color='yellow on green')]]

section2 = [[sg.I('Input sec 2', k='-IN2-')],
            [sg.I(k='-IN21-')],
            [sg.B('Button section 2',  button_color=('yellow', 'purple')),
             sg.B('Button2 section 2', button_color=('yellow', 'purple')),
             sg.B('Button3 section 2', button_color=('yellow', 'purple'))]]


layout =   [[sg.Text('Window with 2 collapsible sections')],
            [sg.Checkbox('Blank checkbox'), sg.Checkbox('Hide Section 2', enable_events=True, key='-OPEN SEC2-CHECKBOX')],
            #### Section 1 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='yellow'), sg.T('Section 1', enable_events=True, text_color='yellow', k='-OPEN SEC1-TEXT')],
            [collapse(section1, '-SEC1-')],
            #### Section 2 part ####
            [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC2-', text_color='purple'),
             sg.T('Section 2', enable_events=True, text_color='purple', k='-OPEN SEC2-TEXT')],
            [collapse(section2, '-SEC2-')],
            #### Buttons at bottom ####
            [sg.Button('Button1'),sg.Button('Button2'), sg.Button('Exit')]]

window = sg.Window('Visible / Invisible Element Demo', layout)

opened1, opened2 = True, True

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event.startswith('-OPEN SEC1-'):
        opened1 = not opened1
        window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
        window['-SEC1-'].update(visible=opened1)

    if event.startswith('-OPEN SEC2-'):
        opened2 = not opened2
        window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
        window['-OPEN SEC2-CHECKBOX'].update(not opened2)
        window['-SEC2-'].update(visible=opened2)

window.close()
