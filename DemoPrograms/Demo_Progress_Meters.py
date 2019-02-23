#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
from time import sleep
from sys import exit as exit


"""
    Demonstration of simple and multiple OneLineProgressMeter's
    
    Shows how 2 progress meters can be running at the same time.
    Note -- If the user wants to cancel a meter, it's important to use the "Cancel" button, not the X
    If the software determined that a meter should be cancelled early, 
        calling OneLineProgresMeterCancel(key) will cancel the meter with the matching key
"""

# sg.ChangeLookAndFeel('Dark')


"""
    The simple case is that you want to add a single meter to your code.  The one-line solution
"""

def DemoOneLineProgressMeter():
    # Display a progress meter. Allow user to break out of loop using cancel button
    for i in range(1000):
        if not sg.OneLineProgressMeter('My 1-line progress meter', i+1, 1000, 'meter key' ):
            break


    layout = [
                [sg.T('One-Line Progress Meter Demo', font=('Any 18'))],
                [sg.T('Outer Loop Count', size=(15,1), justification='r'), sg.In(default_text='100', size=(5,1), key='CountOuter', do_not_clear=True),
                 sg.T('Delay'), sg.In(default_text='10', key='TimeOuter', size=(5,1), do_not_clear=True), sg.T('ms')],
                [sg.T('Inner Loop Count', size=(15,1), justification='r'), sg.In(default_text='100', size=(5,1), key='CountInner', do_not_clear=True) ,
                 sg.T('Delay'), sg.In(default_text='10', key='TimeInner', size=(5,1), do_not_clear=True), sg.T('ms')],
                [sg.Button('Show', pad=((0,0), 3), bind_return_key=True), sg.T('me the meters!')]
              ]

    window = sg.Window('One-Line Progress Meter Demo').Layout(layout)

    while True:
        event, values = window.Read()
        if event is None:
            break
        if event == 'Show':
            max_outer = int(values['CountOuter'])
            max_inner = int(values['CountInner'])
            delay_inner = int(values['TimeInner'])
            delay_outer = int(values['TimeOuter'])
            for i in range(max_outer):
                if not sg.OneLineProgressMeter('Outer Loop', i+1, max_outer, 'outer'):
                    break
                sleep(delay_outer/1000)
                for j in range(max_inner):
                    if not sg.OneLineProgressMeter('Inner Loop', j+1, max_inner, 'inner'):
                        break
                    sleep(delay_inner/1000)

'''
    Make your own progress meter!  
    Embed the meter right into your window
'''

def CustomMeter():
    # layout the form
    layout = [[sg.Text('A custom progress meter')],
              [sg.ProgressBar(1000, orientation='h', size=(20,20), key='progress')],
              [sg.Cancel()]]

    # create the form`
    window = sg.Window('Custom Progress Meter').Layout(layout)
    progress_bar = window.FindElement('progress')
    # loop that would normally do something useful
    for i in range(1000):
        # check to see if the cancel button was clicked and exit loop if clicked
        event, values = window.Read(timeout=0)
        if event == 'Cancel' or event == None:
            break
        # update bar with loop value +1 so that bar eventually reaches the maximum
        progress_bar.UpdateBar(i+1)
    # done with loop... need to destroy the window as it's still open
    window.Close()

CustomMeter()
DemoOneLineProgressMeter()