import PySimpleGUI as sg

'''
    IP Address entry window with digit validation and auto advance
    If not a digit or ., the ignored
    . will advance the focus to the next entry
    On the last input, once it's complete the focus moves to the OK button
    Pressing spacebar with focus on OK generates an -OK- event
'''

# create a short-cut element so don't have to type this in over and over


def MyInput(key): return sg.I('', size=(3, 1), key=key, pad=(0, 2))


layout = [[sg.T('Your typed chars appear here:'), sg.T('', key='-OUTPUT-')],
          [MyInput(0), sg.T('.'), MyInput(1), sg.T('.'),
           MyInput(2), sg.T('.'), MyInput(3)],
          [sg.B('Ok', key='-OK-', bind_return_key=True), sg.B('Exit')]]

window = sg.Window('Window Title', layout, return_keyboard_events=True)

while True:             # Event Loop
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elem = window.find_element_with_focus()

    if elem is not None:
        key = elem.Key
        # get value of input field that has focus
        value = values[key]
        if event == '.' and key != '-OK-':                    # if a ., then advance to next field
            elem.update(value[:-1])
            value = value[:-1]
            next_elem = window[key+1]
            next_elem.set_focus()

        elif event not in '0123456789':
            elem.update(value[:-1])

        elif len(value) > 2 and key < 3:     # if 2 digits typed in, move on to next input
            next_elem = window[key+1]
            next_elem.set_focus()

        elif len(value) > 2 and key == 3:
            window['-OK-'].set_focus()
            print('You entered IP Address {}.{}.{}.{}'.format(*values.values()))

window.close()
