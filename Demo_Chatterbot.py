import PySimpleGUI as g
from chatterbot import ChatBot
import chatterbot.utils

'''
Demo_Chatterbot.py
A GUI wrapped arouind the Chatterbot package.
The GUI is used to show progress bars during the training process and 
to collect user input that is sent to the chatbot.  The reply is displayed in the GUI window
'''

# Create the 'Trainer GUI'
MAX_PROG_BARS = 20
bars = []
texts = []
training_layout = [[g.T('TRAINING PROGRESS', size=(20,1), font=('Helvetica', 17))]]
for i in range(MAX_PROG_BARS):
    bars.append(g.ProgressBar(100, size=(30, 5)))
    texts.append(g.T(' '*20))
    training_layout += [[texts[i], bars[i]]]

training_form = g.FlexForm('Training')
training_form.Layout(training_layout)
current_bar = 0

# callback function for training runs
def print_progress_bar(description, iteration_counter, total_items, progress_bar_length=20):
    global current_bar
    global bars
    global texts
    global training_form
    # update the form and the bars
    training_form.ReadNonBlocking()
    bars[current_bar].UpdateBar(iteration_counter, max=total_items)
    texts[current_bar].Update(description)
    if iteration_counter == total_items:
        current_bar += 1

# redefine the chatbot text based progress bar with a graphical one
chatterbot.utils.print_progress_bar = print_progress_bar

chatbot = ChatBot('Ron Obvious', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

################# GUI #################
with g.FlexForm('Chat Window', auto_size_text=True, default_element_size=(30, 2)) as form:
    layout = [[g.Output(size=(80, 20))],
              [g.Multiline(size=(70, 5), enter_submits=True),
               g.ReadFormButton('SEND', bind_return_key=True), g.SimpleButton('EXIT')]]

    form.Layout(layout)
    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
    while True:
        button, (value,) = form.Read()
        if button != 'SEND':
            break
        print(value.rstrip())
        # send the user input to chatbot to get a response
        response = chatbot.get_response(value.rstrip())
        print(response)