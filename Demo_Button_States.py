import PySimpleGUI as sg
"""
Demonstrates using a "tight" layout with a Dark theme.
Shows how button states can be controlled by a user application.  The program manages the disabled/enabled
states for buttons and changes the text color to show greyed-out (disabled) buttons
"""

sg.ChangeLookAndFeel('Dark')
sg.SetOptions(element_padding=(0,0))

layout = [[sg.T('User:', pad=((3,0),0)), sg.OptionMenu(values = ('User 1', 'User 2'), size=(20,1)), sg.T('0', size=(8,1))],
          [sg.T('Customer:', pad=((3,0),0)), sg.OptionMenu(values=('Customer 1', 'Customer 2'), size=(20,1)), sg.T('1', size=(8,1))],
          [sg.T('Notes:', pad=((3,0),0)), sg.In(size=(44,1), background_color='white', text_color='black')],
          [sg.ReadFormButton('Start', button_color=('white', 'black'), key='start'),
           sg.ReadFormButton('Stop', button_color=('gray34', 'black'), key='stop'),
           sg.ReadFormButton('Reset', button_color=('gray', 'firebrick3'), key='reset'),
           sg.ReadFormButton('Submit', button_color=('gray34', 'springgreen4'), key='submit')]
          ]

form = sg.FlexForm("Time Tracker", default_element_size=(12,1), text_justification='r', auto_size_text=False, auto_size_buttons=False,
                   default_button_element_size=(12,1))
form.Layout(layout)
recording = have_data = False
while True:
    button, values = form.Read()
    if button is None:
        exit(69)
    if button is 'Start':
        form.FindElement('start').Update(button_color=('gray34','black'))
        form.FindElement('stop').Update(button_color=('white', 'black'))
        form.FindElement('reset').Update(button_color=('white', 'firebrick3'))
        recording = True
    elif button is 'Stop' and recording:
        form.FindElement('stop').Update(button_color=('gray34','black'))
        form.FindElement('start').Update(button_color=('white', 'black'))
        form.FindElement('submit').Update(button_color=('white', 'springgreen4'))
        recording = False
        have_data = True
    elif button is 'Reset':
        form.FindElement('stop').Update(button_color=('gray34','black'))
        form.FindElement('start').Update(button_color=('white', 'black'))
        form.FindElement('submit').Update(button_color=('gray34', 'springgreen4'))
        form.FindElement('reset').Update(button_color=('gray34', 'firebrick3'))
        recording = False
        have_data = False
    elif button is 'Submit' and have_data:
        form.FindElement('stop').Update(button_color=('gray34','black'))
        form.FindElement('start').Update(button_color=('white', 'black'))
        form.FindElement('submit').Update(button_color=('gray34', 'springgreen4'))
        form.FindElement('reset').Update(button_color=('gray34', 'firebrick3'))
        recording = False

