import PySimpleGUI as sg

"""
    Demonstrates that using a Column Element to make groups of Elements appear and disappear
    will cause the layout of the elements in the column to remain as they were.  If each individual element
    were made invisible and then visible, then tkinter puts EACH ELEMENT on a separate row when it is made
    visible again.  This means a row of 6 elements will become a column of 6 elements if you make each of them
    visible one at a time.

"""

layout = [[sg.Column([[sg.Text('My Window')],[sg.Input(key='_IN_'), sg.B('My button', key='_OUT_')]], key='_COL_')],
            [sg.Button('Invisible'), sg.B('Visible'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Invisible':
        window.Elem('_COL_').Update(visible=False)
    elif event == 'Visible':
        window.Elem('_COL_').Update(visible=True)

window.Close()
