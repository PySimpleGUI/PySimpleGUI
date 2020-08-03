import PySimpleGUI as sg

"""
    Demonstrates that using a Column Element to make groups of Elements appear and disappear
    will cause the layout of the elements in the column to remain as they were.  If each individual element
    were made invisible and then visible, then tkinter puts EACH ELEMENT on a separate row when it is made
    visible again.  This means a row of 6 elements will become a column of 6 elements if you make each of them
    visible one at a time.

"""

layout = [[sg.Col([[sg.Text('My Window')], [sg.Input(key='-IN-'), sg.Button('My button', key='-OUT-')]], key='-COL-'), sg.Canvas(size=(0,0), pad=(0,0))],
          [sg.Button('Invisible'), sg.Button('Visible'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Invisible':
        window['-COL-'].update(visible=False)
    elif event == 'Visible':
        window['-COL-'].update(visible=True)

window.close()
