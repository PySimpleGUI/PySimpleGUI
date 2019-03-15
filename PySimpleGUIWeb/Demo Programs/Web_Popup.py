import PySimpleGUIWeb as sg

"""
  ____                         
 |  _ \ ___  _ __  _   _ _ __  
 | |_) / _ \| '_ \| | | | '_ \ 
 |  __/ (_) | |_) | |_| | |_) |
 |_|   \___/| .__/ \__,_| .__/ 
            |_|         |_|  

A Popup demonstration. A "Popup" window is shown over the main
window.  Clicking OK will close the Popup and you return to main again.
"""

print('Starting up...')

layout = [
    [sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_')],
    [sg.Input(do_not_clear=True, key='_IN_')],
    [sg.Button('Show'), sg.Button('Exit'), sg.Button('Blank')]
]

window = sg.Window('Window Title').Layout(layout)

while True:  # Event Loop
    print('in event loop')
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break
    if event == 'Show':
        sg.Popup('A popup!', ' You typed ', values['_IN_'])

window.Close()