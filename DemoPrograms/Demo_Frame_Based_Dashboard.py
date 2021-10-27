import PySimpleGUI as sg

"""
    Demo - Resizable Dashboard using Frames

    This Demo Program looks similar to the one based on the Column Element.
    This version has a big difference in how it was implemented and the fact that it can be resized.

    It's a good example of how PySimpleGUI evolves, continuously.  When the original Column-based demo
        was written, none of these techniques such as expansion, were easily programmed.

    Dashboard using blocks of information.

    Copyright 2021 PySimpleGUI.org
"""


theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 0,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

sg.theme_add_new('Dashboard', theme_dict)
sg.theme('Dashboard')

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 0))
BPAD_LEFT_INSIDE = (0, (10, 0))
BPAD_RIGHT = ((10,20), (10, 0))

top_banner = [
               [sg.Text('Dashboard', font='Any 20', background_color=DARK_HEADER_COLOR, enable_events=True, grab=False), sg.Push(background_color=DARK_HEADER_COLOR),
               sg.Text('Wednesday 27 Oct 2021', font='Any 20', background_color=DARK_HEADER_COLOR)],
               ]

top  = [[sg.Push(), sg.Text('Weather Could Go Here', font='Any 20'), sg.Push()],
            [sg.T('This Frame has a relief while the others do not')],
            [sg.T('This window is resizable (see that sizegrip in the bottom right?)')]]

block_3 = [[sg.Text('Block 3', font='Any 20')],
            [sg.Input(), sg.Text('Some Text')],
            [sg.T('This frame has element_justification="c"')],
            [sg.Button('Go'), sg.Button('Exit')]  ]


block_2 = [[sg.Text('Block 2', font='Any 20')],
            [sg.T('This is some random text')],
            [sg.Image(data=sg.DEFAULT_BASE64_ICON, enable_events=True)]  ]

block_4 = [[sg.Text('Block 4', font='Any 20')],
            [sg.T('You can move the window by grabbing this block (and the top banner)')],
            [sg.T('This block is a Column Element')],
            [sg.T('The others are all frames')],
            [sg.T('The Frame Element, with a border_width=0\n    and no title is just like a Column')],
            [sg.T('Frames that have a fixed size \n    handle element_justification better than Columns')]]


layout = [
          [sg.Frame('', top_banner,   pad=(0,0), background_color=DARK_HEADER_COLOR,  expand_x=True, border_width=0, grab=True)],
          [sg.Frame('', top, size=(920, 100), pad=BPAD_TOP,  expand_x=True,  relief=sg.RELIEF_GROOVE, border_width=3)],
          [sg.Frame('', [[sg.Frame('', block_2, size=(450,150), pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True, expand_y=True, )],
                        [sg.Frame('', block_3, size=(450,150),  pad=BPAD_LEFT_INSIDE, border_width=0, expand_x=True, expand_y=True, element_justification='c')]],
                    pad=BPAD_LEFT, background_color=BORDER_COLOR, border_width=0, expand_x=True, expand_y=True),
           sg.Column(block_4, size=(450, 320), pad=BPAD_RIGHT,  expand_x=True, expand_y=True, grab=True),],[sg.Sizegrip(background_color=BORDER_COLOR)]]

window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=True, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_LOC_EXIT)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == 'Edit Me':
        sg.execute_editor(__file__)
    elif event == 'Version':
        sg.popup_scrolled(sg.get_versions(), keep_on_top=True)
    elif event == 'File Location':
        sg.popup_scrolled('This Python file is:', __file__)
window.close()
