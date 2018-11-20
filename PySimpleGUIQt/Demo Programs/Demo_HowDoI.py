#!/usr/bin/env python
import sys
import PySimpleGUIQt as sg
import subprocess


# Test this command in a dos window if you are having trouble.
HOW_DO_I_COMMAND =  'python -m howdoi.howdoi'

# if you want an icon on your taskbar for this gui, then change this line of code to point to the ICO file
DEFAULT_ICON = 'question.ico'

def HowDoI():
    '''
    Make and show a window (PySimpleGUI form) that takes user input and sends to the HowDoI web oracle
    Excellent example of 2 GUI concepts
        1. Output Element that will show text in a scrolled window
        2. Non-Window-Closing Buttons - These buttons will cause the form to return with the form's values, but doesn't close the form
    :return: never returns
    '''
    # -------  Make a new Window  ------- #
    sg.ChangeLookAndFeel('GreenTan')            # give our form a spiffy set of colors

    layout =  [
                [sg.Text('Ask and your answer will appear here....')],
                [sg.Output(size=(900, 500), font=('Courier', 10))],
                [ sg.Spin(values=(1, 4), initial_value=1, size=(50, 25), key='Num Answers', font=('Helvetica', 15)),
                  sg.Text('Num Answers',font=('Helvetica', 15), size=(170,22)), sg.Checkbox('Display Full Text', key='full text', font=('Helvetica', 15), size=(200,22)),
                sg.T('Command History', font=('Helvetica', 15)), sg.T('', size=(100,25), text_color=sg.BLUES[0], key='history'), sg.Stretch()],
                [sg.Multiline(size=(600, 100), enter_submits=True, focus=True, key='query', do_not_clear=False), sg.Stretch(),
                sg.ReadButton('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
                sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0])), sg.Stretch()]
              ]

    window = sg.Window('How Do I ??',
                       default_element_size=(100, 25),
                       # element_padding=(10,10),
                       icon=DEFAULT_ICON,
                       font=('Helvetica',14),
                       default_button_element_size=(70,50),
                       return_keyboard_events=True,
                       no_titlebar=False,
                       grab_anywhere=True,)

    window.Layout(layout)
    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    command_history = []
    history_offset = 0
    while True:
        event, values = window.Read()
        if event == 'SEND' or event == 'query':
            # window.FindElement('+OUTPUT+').Update('test of output')                       # manually clear input because keyboard events blocks clear

            query = values['query'].rstrip()
            # print(query)
            QueryHowDoI(query, values['Num Answers'], values['full text'])  # send the string to HowDoI
            command_history.append(query)
            history_offset = len(command_history)-1
            window.FindElement('query').Update('')                       # manually clear input because keyboard events blocks clear
            window.FindElement('history').Update('\n'.join(command_history[-3:]))
        elif event == None or event == 'EXIT':            # if exit button or closed using X
            break
        elif 'Up' in event and len(command_history):                                # scroll back in history
            command = command_history[history_offset]
            history_offset -= 1 * (history_offset > 0)      # decrement is not zero
            window.FindElement('query').Update(command)
        elif 'Down' in event and len(command_history):                              # scroll forward in history
            history_offset += 1 * (history_offset < len(command_history)-1) # increment up to end of list
            command = command_history[history_offset]
            window.FindElement('query').Update(command)
        elif 'Escape' in event:                            # clear currently line
            window.FindElement('query').Update('')


def QueryHowDoI(Query, num_answers, full_text):
    '''
    Kicks off a subprocess to send the 'Query' to HowDoI
    Prints the result, which in this program will route to a gooeyGUI window
    :param Query: text english question to ask the HowDoI web engine
    :return: nothing
    '''
    howdoi_command = HOW_DO_I_COMMAND
    full_text_option = ' -a' if full_text else ''
    t = subprocess.Popen(howdoi_command + ' \"'+ Query + '\" -n ' + str(num_answers)+full_text_option, stdout=subprocess.PIPE)
    (output, err) = t.communicate()
    print('{:^88}'.format(Query.rstrip()))
    print('_'*60)
    print(output.decode("utf-8") )
    exit_code = t.wait()

if __name__ == '__main__':
    HowDoI()

