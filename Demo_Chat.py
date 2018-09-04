import PySimpleGUI as sg

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
    # -------  Make a new FlexForm  ------- #
    sg.ChangeLookAndFeel('GreenTan')            # give our form a spiffy set of colors

    form = sg.FlexForm('Chat window with history', default_element_size=(30, 2), font=('Helvetica',' 13'), default_button_element_size=(8,2), return_keyboard_events=True)

    multiline_elem = sg.Multiline(size=(85, 5), enter_submits=True, key='query', do_not_clear=False)
    history_elem = sg.T('', size=(20,3))
    layout =  [
                [sg.Text('Your output will go here', size=(40, 1))],
                [sg.Output(size=(127, 30), font=('Helvetica 10'))],
                [sg.T('Command History'), history_elem],
                [multiline_elem,
                sg.ReadFormButton('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
                sg.SimpleButton('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]
              ]
    form.Layout(layout)

    # ---===--- Loop taking in user input and using it  --- #
    command_history = []
    history_offset = 0
    while True:
        (button, value) = form.Read()
        if button is 'SEND':
            query = value['query'].rstrip()
            # EXECUTE YOUR COMMAND HERE
            print('The command you entered was {}'.format(query))
            command_history.append(query)
            history_offset = len(command_history)-1
            multiline_elem.Update('')                       # manually clear input because keyboard events blocks clear
            history_elem.Update('\n'.join(command_history[-3:]))
        elif button is None or button is 'EXIT':            # quit if exit button or X
            break
        elif 'Up' in button and len(command_history):
            command = command_history[history_offset]
            history_offset -= 1 * (history_offset > 0)      # decrement is not zero
            multiline_elem.Update(command)
        elif 'Down' in button and len(command_history):
            history_offset += 1 * (history_offset < len(command_history)-1) # increment up to end of list
            command = command_history[history_offset]
            multiline_elem.Update(command)
        elif 'Escape' in button:
            multiline_elem.Update('')

    exit(69)


ChatBotWithHistory()
