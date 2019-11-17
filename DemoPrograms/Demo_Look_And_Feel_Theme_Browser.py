import PySimpleGUI as sg

"""
    Allows you to "browse" through the look and feel settings.  Click on one and you'll see a 
    Popup window using the color scheme you chose.  It's a simply little program that demonstrates
    how snappy a GUI can feel if you enable an element's events rather than waiting on a button click.
    In this program, as soon as a listbox entry is clicked, the read returns.
"""

sg.change_look_and_feel('GreenTan')
color_list = sg.list_of_look_and_feel_values()
color_list.sort()
layout = [[sg.Text('Look and Feel Browser')],
          [sg.Text('Click a look and feel color to see demo window')],
          [sg.Listbox(values=color_list,
                      size=(20, 12), key='-LIST-', enable_events=True)],
          [sg.Button('Exit')]]

window = sg.Window('Look and Feel Browser', layout)

while True:  # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    sg.change_look_and_feel(values['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

window.close()
