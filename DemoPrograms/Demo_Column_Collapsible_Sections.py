import PySimpleGUI as sg

"""
    Demo - "Collapsible" sections of windows

    This demo shows one techinique for creating a collapsible section (Column) within your window.

    To open/close a section, click on the arrow or name of the section.
    Section 2 can also be controlled using the checkbox at the top of the window just to
    show that there are multiple way to trigger events such as these.
    
    Feel free to modify to use the fonts and sizes of your choosing.  It's 1 line of code to make the section.
    It could have been done directly in the layout.

    Copyright 2021 PySimpleGUI.org
"""


def Collapsible(layout, key, title='', arrows=(sg.SYMBOL_DOWN, sg.SYMBOL_UP), collapsed=False):
    """
    User Defined Element
    A "collapsable section" element. Like a container element that can be collapsed and brought back
    :param layout:Tuple[List[sg.Element]]: The layout for the section
    :param key:Any: Key used to make this section visible / invisible
    :param title:str: Title to show next to arrow
    :param arrows:Tuple[str, str]: The strings to use to show the section is (Open, Closed).
    :param collapsed:bool: If True, then the section begins in a collapsed state
    :return:sg.Column: Column including the arrows, title and the layout that is pinned
    """
    return sg.Column([[sg.T((arrows[1] if collapsed else arrows[0]), enable_events=True, k=key+'-BUTTON-'),
                       sg.T(title, enable_events=True, key=key+'-TITLE-')],
                      [sg.pin(sg.Column(layout, key=key, visible=not collapsed, metadata=arrows))]], pad=(0,0))


SEC1_KEY = '-SECTION1-'
SEC2_KEY = '-SECTION2-'

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
            [sg.Checkbox('Blank checkbox'), sg.Checkbox('Hide Section 2', enable_events=True, key='-OPEN SEC2-CHECKBOX-')],
            #### Section 1 part ####
            [Collapsible(section1, SEC1_KEY,  'Section 1', collapsed=True)],
            #### Section 2 part ####
            [Collapsible(section2, SEC2_KEY, 'Section 2', arrows=( sg.SYMBOL_TITLEBAR_MINIMIZE, sg.SYMBOL_TITLEBAR_MAXIMIZE))],
            [sg.Button('Button1'),sg.Button('Button2'), sg.Button('Exit')]]

window = sg.Window('Visible / Invisible Element Demo', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event.startswith(SEC1_KEY):
        window[SEC1_KEY].update(visible=not window[SEC1_KEY].visible)
        window[SEC1_KEY+'-BUTTON-'].update(window[SEC1_KEY].metadata[0] if window[SEC1_KEY].visible else window[SEC1_KEY].metadata[1])

    if event.startswith(SEC2_KEY) or event == '-OPEN SEC2-CHECKBOX-':
        window[SEC2_KEY].update(visible=not window[SEC2_KEY].visible)
        window[SEC2_KEY+'-BUTTON-'].update(window[SEC2_KEY].metadata[0] if window[SEC2_KEY].visible else window[SEC2_KEY].metadata[1])
        window['-OPEN SEC2-CHECKBOX-'].update(not window[SEC2_KEY].visible)

window.close()
