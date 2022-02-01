import PySimpleGUI as sg
"""
    Demo showing how to remove the titlebar and replace with your own
    Unlike previous demos that lacked a titlebar, this one provides a way for you
    to "minimize" your window that does not have a titlebar.  This is done by faking
    the window using a hidden window that is minimized.
   
    The DarkGrey8 is already a theme in PySimpleGUI.  It's here to show you how to add your own and have it them
    be used by your Custom Titlebar. 
   
    Copyright 2020, 2022 PySimpleGUI.org
"""


# If not running 4.28.0.4+ that has the DarkGrey8 theme, then uncomment to get it added.
DarkGrey8 = {'BACKGROUND': '#19232D',
              'TEXT': '#ffffff',
              'INPUT': '#32414B',
              'TEXT_INPUT': '#ffffff',
              'SCROLL': '#505F69',
              'BUTTON': ('#ffffff', '#32414B'),
              'PROGRESS': ('#505F69', '#32414B'),
              'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
              }

sg.theme_add_new('DarkGrey8', DarkGrey8)

sg.theme('DarkGrey8')



def main():
    # sg.theme('light green 3')
    # sg.theme('dark red')

    title = 'Customized Titlebar Window'

    layout = [  [sg.Titlebar(title, sg.CUSTOM_TITLEBAR_ICON)],
                [sg.T('This is normal window text.  The above is a  "Custom Titlebar"')],
                [sg.T('They can be made by adding a Titlebar element to your layout')],
                [sg.T('Input something:')],
                [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
                [sg.Button('Go')]]

    window = sg.Window(title, layout, resizable=True, no_titlebar=True, keep_on_top=True, margins=(0,0), finalize=True)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Go':
            window['-OUT-'].update(values['-IN-'])
    window.close()


if __name__ == '__main__':
    main()
