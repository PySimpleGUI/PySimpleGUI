import PySimpleGUI as sg

"""
    Demo - Class wrapper
    
    Using a class to encapsulate PySimpleGUI Window creation & event loop
    
    This is NOT a recommended design pattern.  It mimics the object oriented design that many OO-based
    GUI frameworks use, but there is no advantage to structuring you code in his manner.  It adds
    confusion, not clarity.  
    
    The class version is 18 lines of code.  The plain version is 13 lines of code.  
    
    Two things about the class wrapper jump out as adding confusion:
    1. Unneccessary fragmentation of the event loop - the button click code is pulled out of the loop entirely
    2. "self" clutters the code without adding value
    

    Copyright 2022, 2023 PySimpleGUI
"""

'''
    MM'""""'YMM dP                            
    M' .mmm. `M 88                            
    M  MMMMMooM 88 .d8888b. .d8888b. .d8888b. 
    M  MMMMMMMM 88 88'  `88 Y8ooooo. Y8ooooo. 
    M. `MMM' .M 88 88.  .88       88       88 
    MM.     .dM dP `88888P8 `88888P' `88888P' 
    MMMMMMMMMMM                               
                                              
    M""MMMMM""M                            oo                   
    M  MMMMM  M                                                 
    M  MMMMP  M .d8888b. 88d888b. .d8888b. dP .d8888b. 88d888b. 
    M  MMMM' .M 88ooood8 88'  `88 Y8ooooo. 88 88'  `88 88'  `88 
    M  MMP' .MM 88.  ... 88             88 88 88.  .88 88    88 
    M     .dMMM `88888P' dP       `88888P' dP `88888P' dP    dP 
    MMMMMMMMMMM
'''
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


'''
    M"""""""`YM                                       dP 
    M  mmmm.  M                                       88 
    M  MMMMM  M .d8888b. 88d888b. 88d8b.d8b. .d8888b. 88 
    M  MMMMM  M 88'  `88 88'  `88 88'`88'`88 88'  `88 88 
    M  MMMMM  M 88.  .88 88       88  88  88 88.  .88 88 
    M  MMMMM  M `88888P' dP       dP  dP  dP `88888P8 dP 
    MMMMMMMMMMM                                          
                                                         
    M""MMMMM""M                            oo                   
    M  MMMMM  M                                                 
    M  MMMMP  M .d8888b. 88d888b. .d8888b. dP .d8888b. 88d888b. 
    M  MMMM' .M 88ooood8 88'  `88 Y8ooooo. 88 88'  `88 88'  `88 
    M  MMP' .MM 88.  ... 88             88 88 88.  .88 88    88 
    M     .dMMM `88888P' dP       `88888P' dP `88888P' dP    dP 
    MMMMMMMMMMM
'''

def gui_function():
    layout = [ [sg.Text('My layout')],
             [sg.Input(key='-IN-')],
             [sg.Button('Go'), sg.Button('Exit')] ]

    window = sg.Window('My new window', layout)

    while True:             # Event Loop
        event, values = window.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break

        if event == 'Go':
            sg.popup('Go button clicked', 'Input value:', values['-IN-'])

    window.close()

gui_function()
