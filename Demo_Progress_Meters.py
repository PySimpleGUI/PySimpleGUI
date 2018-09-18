from time import sleep
import PySimpleGUI as sg

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

import PySimpleGUI as sg

# Display a progress meter in work loop. User is not allowed to break out of the loop
for i in range(10000):
    if i % 5 == 0: sg.OneLineProgressMeter('My 1-line progress meter', i+1, 10000, 'single')

# Display a progress meter. Allow user to break out of loop using cancel button
for i in range(10000):
    if not sg.OneLineProgressMeter('My 1-line progress meter', i+1, 10000, 'single'):
        break




layout = [
            [sg.T('One-Line Progress Meter Demo', font=('Any 18'))],
            [sg.T('Outer Loop Count', size=(15,1), justification='r'), sg.In(default_text='100', size=(5,1), key='CountOuter', do_not_clear=True),
             sg.T('Delay'), sg.In(default_text='10', key='TimeOuter', size=(5,1), do_not_clear=True), sg.T('ms')],
            [sg.T('Inner Loop Count', size=(15,1), justification='r'), sg.In(default_text='100', size=(5,1), key='CountInner', do_not_clear=True) ,
             sg.T('Delay'), sg.In(default_text='10', key='TimeInner', size=(5,1), do_not_clear=True), sg.T('ms')],
            [sg.SimpleButton('Show', pad=((0,0), 3), bind_return_key=True), sg.T('me the meters!')]
          ]

form = sg.FlexForm('One-Line Progress Meter Demo')
form.Layout(layout)

while True:
    button, values = form.Read()
    if button is None:
        break
    if button == 'Show':
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

exit(69)
