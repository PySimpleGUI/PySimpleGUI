import PySimpleGUI as sg

layout = [[sg.Text('Window 1'), ],
          [sg.Input(do_not_clear=True)],
          [sg.Text('', key='_OUTPUT_')],
          [sg.Button('Next >'), sg.Button('Exit')]]

win1 = sg.Window('Window 1').Layout(layout)

win3_active = win2_active = False
while True:
    if not win2_active:
        ev1, vals1 = win1.Read()
        if ev1 is None or ev1 == 'Exit':
            break
        win1.FindElement('_OUTPUT_').Update(vals1[0])

    if not win2_active and ev1 == 'Next >':
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Window 2')],
                   [sg.Button('< Prev'), sg.Button('Next >')]]

        win2 = sg.Window('Window 2').Layout(layout2)

    if win2_active:
        ev2, vals2 = win2.Read()
        if ev2 in (None, 'Exit', '< Prev'):
            win2_active = False
            win2.Close()
            win1.UnHide()
        elif ev2 == 'Next >':
            win3_active = True
            win2_active = False
            win2.Hide()
            layout3 = [[sg.Text('Window 3')],
                       [sg.Button('< Prev'), sg.Button('Exit')]]
            win3 = sg.Window('Window 3').Layout(layout3)

    if win3_active:
        ev3, vals3 = win3.Read()
        if ev3 == '< Prev':
            win3.Close()
            win3_active = False
            win2_active = True
            win2.UnHide()
        elif ev3 in (None, 'Exit'):
            break
