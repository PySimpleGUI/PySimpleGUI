#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

from chatterbot import ChatBot
import chatterbot.utils


'''
Demo_Chatterbot.py
A GUI wrapped arouind the Chatterbot package.
The GUI is used to show progress bars during the training process and 
to collect user input that is sent to the chatbot.  The reply is displayed in the GUI window
'''

# Create the 'Trainer GUI'
# The Trainer GUI consists of a lot of progress bars stacked on top of each other
sg.ChangeLookAndFeel('GreenTan')
# sg.DebugWin()
MAX_PROG_BARS = 20              # number of training sessions
bars = []
texts = []
training_layout = [[sg.T('TRAINING PROGRESS', size=(20, 1), font=('Helvetica', 17))], ]
for i in range(MAX_PROG_BARS):
    bars.append(sg.ProgressBar(100, size=(30, 4)))
    texts.append(sg.T(' ' * 20, size=(20, 1), justification='right'))
    training_layout += [[texts[i], bars[i]],]       # add a single row

training_window = sg.Window('Training').Layout(training_layout)
current_bar = 0

# callback function for training runs
def print_progress_bar(description, iteration_counter, total_items, progress_bar_length=20):
    global current_bar
    global bars
    global texts
    global training_window
    # update the window and the bars
    button, values = training_window.Read(timeout=0)
    if button is None:       # if user closed the window on us, exit
        sys.exit(69)
    if bars[current_bar].UpdateBar(iteration_counter, max=total_items) is False:
        sys.exit(69)
    texts[current_bar].Update(description)      # show the training dataset name
    if iteration_counter == total_items:
        current_bar += 1

# redefine the chatbot text based progress bar with a graphical one
chatterbot.utils.print_progress_bar = print_progress_bar

chatbot = ChatBot('Ron Obvious', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

################# GUI #################

layout = [[sg.Output(size=(80, 20))],
          [sg.Multiline(size=(70, 5), enter_submits=True),
           sg.Button('SEND', bind_return_key=True), sg.Button('EXIT')]]

window = sg.Window('Chat Window', auto_size_text=True, default_element_size=(30, 2)).Layout(layout)

# ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
while True:
    event, (value,) = window.Read()
    if event is not 'SEND':
        break
    string = value.rstrip()
    print('     '+string)
    # send the user input to chatbot to get a response
    response = chatbot.get_response(value.rstrip())
    print(response)