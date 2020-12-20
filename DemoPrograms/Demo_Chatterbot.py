#!/usr/bin/env python
import PySimpleGUI as sg
import chatterbot.utils


'''
Demo_Chatterbot.py

Note - this code was written using version 0.8.7 of Chatterbot... to install:

python -m pip install chatterbot==0.8.7

It still runs fine with the old version. 

A GUI wrapped arouind the Chatterbot package.
The GUI is used to show progress bars during the training process and
to collect user input that is sent to the chatbot.  The reply is displayed in the GUI window
'''

# Create the 'Trainer GUI'
# The Trainer GUI consists of a lot of progress bars stacked on top of each other
sg.theme('GreenTan')
# sg.DebugWin()
MAX_PROG_BARS = 20              # number of training sessions
bars = []
texts = []
training_layout = [[sg.Text('TRAINING PROGRESS', size=(20, 1), font=('Helvetica', 17))]]
for i in range(MAX_PROG_BARS):
    bars.append(sg.ProgressBar(100, size=(30, 4)))
    texts.append(sg.Text(' ' * 20, size=(20, 1), justification='right'))
    training_layout += [[texts[i], bars[i]], ]       # add a single row

training_window = sg.Window('Training', training_layout)
current_bar = 0

# callback function for training runs


def print_progress_bar(description, iteration_counter, total_items, progress_bar_length=20):
    global current_bar
    global bars
    global texts
    global training_window
    # update the window and the bars
    button, values = training_window.read(timeout=0)
    if button is None:       # if user closed the window on us, exit
        return
    if bars[current_bar].UpdateBar(iteration_counter, max=total_items) is False:
        return
    # show the training dataset name
    texts[current_bar].update(description)
    if iteration_counter == total_items:
        current_bar += 1


# redefine the chatbot text based progress bar with a graphical one
chatterbot.utils.print_progress_bar = print_progress_bar


from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train based on the english corpus
trainer.train("chatterbot.corpus.english")

# Train based on english greetings corpus
trainer.train("chatterbot.corpus.english.greetings")

# Train based on the english conversations corpus
trainer.train("chatterbot.corpus.english.conversations")
chatbot = ChatBot('Ron Obvious', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

# Train based on the english corpus
# chatbot.train("chatterbot.corpus.english")

################# GUI #################

layout = [[sg.Multiline(size=(80, 20), reroute_stdout=True, echo_stdout_stderr=True)],
          [sg.MLine(size=(70, 5), key='-MLINE IN-', enter_submits=True, do_not_clear=False),
           sg.Button('SEND', bind_return_key=True), sg.Button('EXIT')]]

window = sg.Window('Chat Window', layout,
            default_element_size=(30, 2))

# ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
while True:
    event, values = window.read()
    if event != 'SEND':
        break
    string = values['-MLINE IN-'].rstrip()
    print('  ' + string)
    # send the user input to chatbot to get a response
    response = chatbot.get_response(values['-MLINE IN-'].rstrip())
    print(response)
