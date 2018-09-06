
def TightLayout():
    """
    Turn off padding in order to get a really tight looking layout.
    """
    import PySimpleGUI as sg

    sg.ChangeLookAndFeel('Dark')
    sg.SetOptions(element_padding=(0, 0))
    layout = [[sg.T('User:', pad=((3, 0), 0)), sg.OptionMenu(values=('User 1', 'User 2'), size=(20, 1)),
               sg.T('0', size=(8, 1))],
              [sg.T('Customer:', pad=((3, 0), 0)), sg.OptionMenu(values=('Customer 1', 'Customer 2'), size=(20, 1)),
               sg.T('1', size=(8, 1))],
              [sg.T('Notes:', pad=((3, 0), 0)), sg.In(size=(44, 1), background_color='white', text_color='black')],
              [sg.ReadFormButton('Start', button_color=('white', 'black')),
               sg.ReadFormButton('Stop', button_color=('white', 'black')),
               sg.ReadFormButton('Reset', button_color=('white', '#9B0023')),
               sg.ReadFormButton('Submit', button_color=('white', 'springgreen4')),
               sg.SimpleButton('Exit', button_color=('white', '#00406B')),
               ]
              ]

    form = sg.FlexForm("Time Tracker", default_element_size=(12, 1), text_justification='r', auto_size_text=False,
                       auto_size_buttons=False, no_titlebar=True,
                       default_button_element_size=(12, 1))
    form.Layout(layout)
    while True:
        button, values = form.Read()
        if button is None or button == 'Exit':
            return


TightLayout()