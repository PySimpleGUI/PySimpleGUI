import PySimpleGUI as sg
import subprocess

import ctypes
import os
import win32process

# hwnd = ctypes.windll.kernel32.GetConsoleWindow()
# if hwnd != 0:
#     ctypes.windll.user32.ShowWindow(hwnd, 0)
#     ctypes.windll.kernel32.CloseHandle(hwnd)
#     _, pid = win32process.GetWindowThreadProcessId(hwnd)
#     os.system('taskkill /PID ' + str(pid) + ' /f')


# Test this command in a dos window if you are having trouble.
HOW_DO_I_COMMAND =  'python -m howdoi.howdoi'

# if you want an icon on your taskbar for this gui, then change this line of code to point to the ICO file
DEFAULT_ICON = 'E:\\TheRealMyDocs\\Icons\\QuestionMark.ico'

def HowDoI():
    '''
    Make and show a window (PySimpleGUI form) that takes user input and sends to the HowDoI web oracle
    Excellent example of 2 GUI concepts
        1. Output Element that will show text in a scrolled window
        2. Non-Window-Closing Buttons - These buttons will cause the form to return with the form's values, but doesn't close the form
    :return: never returns
    '''
    # -------  Make a new FlexForm  ------- #
    sg.ChangeLookAndFeel('GreenTan')            # give our form a spiffy set of colors

    layout =  [
                [sg.Text('Ask and your answer will appear here....', size=(40, 1))],
                [sg.Output(size=(127, 30), font=('Helvetica 10'))],
                [ sg.Spin(values=(1, 2, 3, 4), initial_value=1, size=(2, 1), key='Num Answers', font='Helvetica 15'),
                  sg.Text('Num Answers',font='Helvetica 15'), sg.Checkbox('Display Full Text', key='full text', font='Helvetica 15'),
                sg.T('Command History', font='Helvetica 15'), sg.T('', size=(40,3), text_color=sg.BLUES[0], key='history')],
                [sg.Multiline(size=(85, 5), enter_submits=True, key='query', do_not_clear=False),
                sg.ReadFormButton('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
                sg.SimpleButton('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]
              ]

    form = sg.FlexForm('How Do I ??', default_element_size=(30, 2), icon=DEFAULT_ICON, font=('Helvetica',' 13'), default_button_element_size=(8,2), return_keyboard_events=True, no_titlebar=True)
    form.Layout(layout)
    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    command_history = []
    history_offset = 0
    while True:
        (button, value) = form.Read()
        if button is 'SEND':
            query = value['query'].rstrip()
            print(query)
            QueryHowDoI(query, value['Num Answers'], value['full text'])  # send the string to HowDoI
            command_history.append(query)
            history_offset = len(command_history)-1
            form.FindElement('query').Update('')                       # manually clear input because keyboard events blocks clear
            form.FindElement('history').Update('\n'.join(command_history[-3:]))
        elif button is None or button is 'EXIT':            # if exit button or closed using X
            break
        elif 'Up' in button and len(command_history):                                # scroll back in history
            command = command_history[history_offset]
            history_offset -= 1 * (history_offset > 0)      # decrement is not zero
            form.FindElement('query').Update(command)
        elif 'Down' in button and len(command_history):                              # scroll forward in history
            history_offset += 1 * (history_offset < len(command_history)-1) # increment up to end of list
            command = command_history[history_offset]
            form.FindElement('query').Update(command)
        elif 'Escape' in button:                            # clear currently line
            form.FindElement('query').Update('')

    exit(69)

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

