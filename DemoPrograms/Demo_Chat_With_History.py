#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

'''
A chatbot with history
Scroll up and down through prior commands using the arrow keys
Special keyboard keys:
    Up arrow - scroll up in commands
    Down arrow - scroll down in commands
    Escape - clear current command
    Control C - exit form
'''

def ChatBotWithHistory():
    # -------  Make a new Window  ------- #
    sg.ChangeLookAndFeel('GreenTan')            # give our form a spiffy set of colors

    layout =  [[sg.Text('Your output will go here', size=(40, 1))],
                [sg.Output(size=(127, 30), font=('Helvetica 10'))],
                [sg.T('Command History'), sg.T('', size=(20,3), key='history')],
                [sg.Multiline(size=(85, 5), enter_submits=True, key='query', do_not_clear=False),
                sg.ReadButton('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
                sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

    window = sg.Window('Chat window with history', default_element_size=(30, 2), font=('Helvetica',' 13'), default_button_element_size=(8,2), return_keyboard_events=True).Layout(layout)

    # ---===--- Loop taking in user input and using it  --- #
    command_history = []
    history_offset = 0
    while True:
        (event, value) = window.Read()
        if event is 'SEND':
            query = value['query'].rstrip()
            # EXECUTE YOUR COMMAND HERE
            print('The command you entered was {}'.format(query))
            command_history.append(query)
            history_offset = len(command_history)-1
            window.FindElement('query').Update('')                       # manually clear input because keyboard events blocks clear
            window.FindElement('history').Update('\n'.join(command_history[-3:]))
        elif event is None or event is 'EXIT':            # quit if exit event or X
            break
        elif 'Up' in event and len(command_history):
            command = command_history[history_offset]
            history_offset -= 1 * (history_offset > 0)      # decrement is not zero
            window.FindElement('query').Update(command)
        elif 'Down' in event and len(command_history):
            history_offset += 1 * (history_offset < len(command_history)-1) # increment up to end of list
            command = command_history[history_offset]
            window.FindElement('query').Update(command)
        elif 'Escape' in event:
            window.FindElement('query').Update('')

    sys.exit(69)


ChatBotWithHistory()
