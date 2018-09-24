import PySimpleGUI as sg

"""
    Demo of how to combine elements into your own custom element
"""

sg.SetOptions(element_padding=(0,0))
# sg.ChangeLookAndFeel('Dark')
# --- Define our "Big-Button-Spinner" compound element. Has 2 buttons and an input field --- #
NewSpinner =  [sg.ReadButton('-', size=(2,1), font='Any 12'),
               sg.In('0', size=(2,1), font='Any 14', justification='r', key='spin'),
               sg.ReadButton('+', size=(2,1), font='Any 12')]
# --- Define Window --- #
layout = [
          [sg.Text('Spinner simulation')],
            NewSpinner,
            [sg.T('')],
          [sg.Ok()]
         ]

window = sg.Window('Spinner simulation').Layout(layout)

# --- Event Loop --- #
counter = 0
while True:
    button, value = window.Read()

    if button == 'Ok' or button is None:    # be nice to your user, always have an exit from your form
        break

    # --- do spinner stuff --- #
    counter += 1 if button =='+' else -1 if button == '-' else 0
    window.FindElement('spin').Update(counter)
