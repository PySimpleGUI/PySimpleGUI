import PySimpleGUI_Qt as sg

layout = [
            [sg.Text('This is the new Dial Element!')],
            [sg.Dial(range=(1,100), key='_DIAL_')],
            [sg.Button('Show'), sg.Button('Exit')]
         ]

window = sg.Window('Window Title').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break

window.Close()
