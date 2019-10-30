#!/usr/bin/env python
import PySimpleGUIWeb as sg
import subprocess
import howdoi

# Test this command in a dos window if you are having trouble.
HOW_DO_I_COMMAND =  'python -m howdoi.howdoi'

def HowDoI():
    '''
    Make and show a window (PySimpleGUI form) that takes user input and sends to the HowDoI web oracle
    Excellent example of 2 GUI concepts
        1. Output Element that will show text in a scrolled window
        2. Non-Window-Closing Buttons - These buttons will cause the form to return with the form's values, but doesn't close the form
    :return: never returns
    '''
    # -------  Make a new Window  ------- #
    sg.change_look_and_feel('GreenTan')            # give our form a spiffy set of colors

    layout =  [
                [sg.Text('Ask and your answer will appear here....', size=(40, 1))],
                [sg.MLineOutput(size_px=(980, 400),key='_OUTPUT_' )],
                # [ sg.Spin(values=(1, 2, 3, 4), initial_value=1, size=(2, 1), key='Num Answers', font='Helvetica 15'),
                [ sg.CBox('Display Full Text', key='full text', font='Helvetica 15'),
                sg.Text('Command History', font='Helvetica 15'), sg.Text('', size=(40,3), text_color=sg.BLUES[0], key='history')],
                [sg.MLine(size=(85, 5), enter_submits=True, key='query', do_not_clear=False),
                sg.ReadButton('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
                sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]
              ]

    window = sg.Window('How Do I?', layout, default_element_size=(30,1),
            font=('Helvetica',' 17'), default_button_element_size=(8,2),
            return_keyboard_events=False)
    
    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    command_history = []
    history_offset = 0
    while True:

        event, values = window.Read()
        # print(event, values)
        if type(event) is int:
            event = str(event)
        if event == 'SEND':
            query = values['query'].rstrip()
            window['_OUTPUT_'].update(query, append=True)
            print(query)
            QueryHowDoI(query, 1, values['full text'], window)  # send the string to HowDoI
            command_history.append(query)
            history_offset = len(command_history)-1

            # manually clear input because keyboard events blocks clear
            window['query'].update('')
            window['history'].update('\n'.join(command_history[-3:]))

        # if exit button or closed using X
        elif event == None or event == 'EXIT':
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

        # clear currently line
        elif 'Escape' in event:
            window['query'].update('')

    window.close()

def QueryHowDoI(Query, num_answers, full_text, window:sg.Window):
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
    window['_OUTPUT_'].update('{:^88}'.format(Query.rstrip()), append=True)
    window['_OUTPUT_'].update('_'*60, append=True)
    window['_OUTPUT_'].update(output.decode("utf-8"), append=True)
    exit_code = t.wait()

if __name__ == '__main__':
    HowDoI()

