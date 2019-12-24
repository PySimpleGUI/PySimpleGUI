#!/usr/bin/env python
import PySimpleGUI as sg
import subprocess

'''
    Famouns howdoi command in PSG
'''


# Test this command in a dos window if you are having trouble.
HOW_DO_I_COMMAND = 'python -m howdoi.howdoi'


def HowDoI():
    '''
    Make and show a window (PySimpleGUI form) that takes user input and sends to the HowDoI web oracle
    Excellent example of 2 GUI concepts
        1. Output Element that will show text in a scrolled window
        2. Non-Window-Closing Buttons - These buttons will cause the form to return with the form's values, but doesn't close the form
    :return: never returns
    '''
    # -------  Make a new Window  ------- #
    # give our form a spiffy set of colors
    sg.theme('GreenTan')

    layout = [
        [sg.Text('Ask and your answer will appear here....', size=(40, 1))],
        [sg.Output(size=(120, 30), font=('Helvetica 10'))],
        [sg.Spin(values=(1, 2, 3, 4), initial_value=1, size=(2, 1), key='Num Answers', font='Helvetica 15'),
         sg.Text('Num Answers', font='Helvetica 15'), sg.CBox(
             'Display Full Text', key='full text', font='Helvetica 15'),
         sg.Text('Command History', font='Helvetica 15'), sg.Text('', size=(40, 3), text_color=sg.BLUES[0], key='history')],
        [sg.MLine(size=(85, 5), enter_submits=True, key='query', do_not_clear=False),
         sg.Button('SEND', button_color=(
             sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
         sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]
    ]

    window = sg.Window('How Do I ??', layout, default_element_size=(30, 2),
                       font=('Helvetica', ' 13'),
                       default_button_element_size=(8, 2),
                       return_keyboard_events=True, no_titlebar=True,
                       grab_anywhere=True)
    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    command_history = []
    history_offset = 0
    while True:
        event, values = window.read()
        if event == 'SEND':
            query = values['query'].rstrip()
            # print(query)
            # send the string to HowDoI
            QueryHowDoI(query, values['Num Answers'], values['full text'])
            command_history.append(query)
            history_offset = len(command_history)-1
            # manually clear input because keyboard events blocks clear
            window['query'].update('')
            window['history'].update('\n'.join(command_history[-3:]))
        elif event == None or event == 'EXIT':            # if exit button or closed using X
            break
        # scroll back in history
        elif 'Up' in event and len(command_history):
            command = command_history[history_offset]
            # decrement is not zero
            history_offset -= 1 * (history_offset > 0)
            window['query'].update(command)
        # scroll forward in history
        elif 'Down' in event and len(command_history):
            # increment up to end of list
            history_offset += 1 * (history_offset < len(command_history)-1)
            command = command_history[history_offset]
            window['query'].update(command)
        elif 'Escape' in event:                            # clear currently line
            window['query'].update('')
    window.close()


def QueryHowDoI(Query, num_answers, full_text):
    '''
    Kicks off a subprocess to send the 'Query' to HowDoI
    Prints the result, which in this program will route to a gooeyGUI window
    :param Query: text english question to ask the HowDoI web engine
    :return: nothing
    '''
    full_text_option = ' -a' if full_text else ''
    t = subprocess.Popen(HOW_DO_I_COMMAND + ' \"' + Query + '\" -n ' +
                         str(num_answers)+full_text_option, stdout=subprocess.PIPE)
    (output, err) = t.communicate()
    print('{:^88}'.format(Query.rstrip()))
    print('_'*60)
    print(output.decode("utf-8"))
    exit_code = t.wait()


if __name__ == '__main__':
    HowDoI()
