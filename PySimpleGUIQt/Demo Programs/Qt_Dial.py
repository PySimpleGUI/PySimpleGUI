import PySimpleGUIQt as sg

layout = [
            [sg.Text('This is the new Dial Element!')],
            [sg.T(' ', size=(70,10)), sg.T('0', key='+DIAL_VALUE+', font=('Helvetica', 15))],
            [sg.Dial(range=(1,100), key='_DIAL_', change_submits=True)],
            [sg.Slider((1,100), orientation='h', key='_SLIDER_', change_submits=True),
             sg.T(' 1', key='+SLIDER_VALUE+', font=('Helvetica', 15))],
            [sg.T('1' + 30*' ' + '100')],
            [sg.Button('Show'), sg.Button('Exit')]
         ]

window = sg.Window('Window Title').Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    window.FindElement('+DIAL_VALUE+').Update(values['_DIAL_'])
    window.FindElement('+SLIDER_VALUE+').Update(values['_SLIDER_'])

window.Close()
