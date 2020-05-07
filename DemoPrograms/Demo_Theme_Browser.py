import PySimpleGUI as sg

"""
    Allows you to "browse" through the theme settings.  Click on one and you'll see a 
    Popup window using the color scheme you chose.  It's a simply little program that demonstrates
    how snappy a GUI can feel if you enable an element's events rather than waiting on a button click.
    In this program, as soon as a listbox entry is clicked, the read returns.
"""

sg.theme('Dark Green 5')

layout = [[sg.Text('Look and Feel Browser')],
          [sg.Text('Click a look and feel color to see demo window')],
          [sg.Listbox(values=sg.theme_list(),
                      size=(20, 20), key='-LIST-', enable_events=True)],
          [sg.Button('Exit')]]

window = sg.Window('Look and Feel Browser', layout)

while True:  # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    sg.theme(values['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]), default_text=values['-LIST-'][0])

window.close()
