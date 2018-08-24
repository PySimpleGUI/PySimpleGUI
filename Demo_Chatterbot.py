import PySimpleGUI as gui
from chatterbot import ChatBot
import chatterbot.utils

'''
Demo_Chatterbot.py
A GUI wrapped arouind the Chatterbot package.
The GUI is used to show progress bars during the training process and 
to collect user input that is sent to the chatbot.  The reply is displayed in the GUI window
'''

# redefine the chatbot text based progress bar with a graphical one
def print_progress_bar(description, iteration_counter, total_items, progress_bar_length=20):
    gui.EasyProgressMeter(description, iteration_counter, total_items)

chatterbot.utils.print_progress_bar = print_progress_bar

chatbot = ChatBot('Ron Obvious', trainer='chatterbot.trainers.ChatterBotCorpusTrainer')

# Train based on the english corpus
chatbot.train("chatterbot.corpus.english")

################# GUI #################
with gui.FlexForm('Chat Window', auto_size_text=True, default_element_size=(30, 2)) as form:
    layout = [ [gui.Output(size=(80, 20))],
               [gui.Multiline(size=(70, 5), enter_submits=True),
               gui.ReadFormButton('SEND', bind_return_key=True), gui.SimpleButton('EXIT')]]

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