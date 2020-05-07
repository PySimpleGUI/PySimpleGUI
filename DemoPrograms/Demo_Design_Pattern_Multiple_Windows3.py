import PySimpleGUI as sg

'''
    Example of wizard-like PySimpleGUI windows
'''

layout = [[sg.Text('Window 1'), ],
          [sg.Input()],
          [sg.Text('',size=(20,1),  key='-OUTPUT-')],
          [sg.Button('Next >'), sg.Button('Exit')]]

window = sg.Window('Window 1', layout)

window3_active = window2_active = False
while True:
    if not window2_active:
        event1, values1 = window.read()
        if event1 is None or event1 == 'Exit':
            break
        window['-OUTPUT-'].update(values1[0])

    if not window2_active and event1 == 'Next >':
        window2_active = True
        window.hide()
        layout2 = [[sg.Text('Window 2')],
                   [sg.Button('< Prev'), sg.Button('Next >')]]

        window2 = sg.Window('Window 2', layout2)

    if window2_active:
        event2 = window2.read()[0]
        if event2 in (sg.WIN_CLOSED, 'Exit', '< Prev'):
            window2_active = False
            window2.close()
            window.un_hide()
        elif event2 == 'Next >':
            window3_active = True
            window2_active = False
            window2.hide()
            layout3 = [[sg.Text('Window 3')],
                       [sg.Button('< Prev'), sg.Button('Exit')]]
            window3 = sg.Window('Window 3', layout3)

    if window3_active:
        ev3, vals3 = window3.read()
        if ev3 == '< Prev':
            window3.close()
            window3_active = False
            window2_active = True
            window2.un_hide()
        elif ev3 in (sg.WIN_CLOSED, 'Exit'):
            break

window.close()
