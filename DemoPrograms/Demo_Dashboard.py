import PySimpleGUI as sg

"""
    Dashboard using blocks of information.

    Copyright 2020 PySimpleGUI.org
"""


theme_dict = {'BACKGROUND': '#2B475D',
                'TEXT': '#FFFFFF',
                'INPUT': '#F2EFE8',
                'TEXT_INPUT': '#000000',
                'SCROLL': '#F2EFE8',
                'BUTTON': ('#000000', '#C2D4D8'),
                'PROGRESS': ('#FFFFFF', '#C7D5E0'),
                'BORDER': 1,'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0}

# sg.theme_add_new('Dashboard', theme_dict)     # if using 4.20.0.1+
sg.LOOK_AND_FEEL_TABLE['Dashboard'] = theme_dict
sg.theme('Dashboard')

BORDER_COLOR = '#C7D5E0'
DARK_HEADER_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))

top_banner = [[sg.Text('Dashboard'+ ' '*64, font='Any 20', background_color=DARK_HEADER_COLOR),
               sg.Text('Tuesday 9 June 2020', font='Any 20', background_color=DARK_HEADER_COLOR)]]

top  = [[sg.Text('The Weather Will Go Here', size=(50,1), justification='c', pad=BPAD_TOP, font='Any 20')],
            [sg.T(f'{i*25}-{i*34}') for i in range(7)],]

block_3 = [[sg.Text('Block 3', font='Any 20')],
            [sg.Input(), sg.Text('Some Text')],
            [sg.Button('Go'), sg.Button('Exit')]  ]


block_2 = [[sg.Text('Block 2', font='Any 20')],
            [sg.T('This is some random text')],
            [sg.Image(data=sg.DEFAULT_BASE64_ICON)]  ]

block_4 = [[sg.Text('Block 4', font='Any 20')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')]]


layout = [[sg.Column(top_banner, size=(960, 60), pad=(0,0), background_color=DARK_HEADER_COLOR)],
          [sg.Column(top, size=(920, 90), pad=BPAD_TOP)],
          [sg.Column([[sg.Column(block_2, size=(450,150), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_3, size=(450,150),  pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT, background_color=BORDER_COLOR),
           sg.Column(block_4, size=(450, 320), pad=BPAD_RIGHT)]]

window = sg.Window('Dashboard PySimpleGUI-Style', layout, margins=(0,0), background_color=BORDER_COLOR, no_titlebar=True, grab_anywhere=True)

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
window.close()
