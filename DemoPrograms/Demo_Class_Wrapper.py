import PySimpleGUI as sg

"""
    Demo - Class wrapper
    
    Using a class to encapsulate PySimpleGUI Window creation & event loop

    Copyright 2022 PySimpleGUI
"""

class SampleGUI():

    def __init__(self):
        self.layout = [ [sg.Text('My layout')],
                        [sg.Input(key='-IN-')],
                        [sg.Button('Go'), sg.Button('Exit')] ]

        self.window = sg.Window('My new window', self.layout)

    def run(self):
        while True:             # Event Loop
            self.event, self.values = self.window.read()
            if self.event in (sg.WIN_CLOSED, 'Exit'):
                break

            if self.event == 'Go':
                self.button_go()

        self.window.close()

    def button_go(self):
        sg.popup('Go button clicked', 'Input value:', self.values['-IN-'])

# Create the class
my_gui = SampleGUI()
# run the event loop
my_gui.run()
