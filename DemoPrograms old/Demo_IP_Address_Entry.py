import PySimpleGUI as sg

'''
    IP Address entry window with digit validation and auto advance
    If not a digit or ., the ignored
    . will advance the focus to the next entry
    On the last input, once it's complete the focus moves to the OK button
    Pressing spacebar with focus on OK generates an _OK_ event
'''

# create a short-cut element so don't have to type this in over and over
InIp = lambda key: sg.Input(do_not_clear=True, size=(3, 1), key=key, pad=(0, 2))

layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_')],
            [InIp(0), sg.T('.'), InIp(1), sg.T('.'), InIp(2), sg.T('.'), InIp(3)],
            [sg.Button('Ok', key='_OK_', bind_return_key=True), sg.Button('Exit')]]

window = sg.Window('Window Title', return_keyboard_events=True).Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    print(event)
    if event is None or event == 'Exit':
        break
    elem = window.FindElementWithFocus()
    if elem is not None:
        key = elem.Key
        value = values[key]                 # get value of input field that has focus
        if event == '.' and key!= '_OK_':                    # if a ., then advance to next field
            elem.Update(value[:-1])
            value = value[:-1]
            next_elem = window.Element(key+1)
            next_elem.SetFocus()
        elif event not in '0123456789':
            elem.Update(value[:-1])
        elif len(value) > 2 and key < 3:     # if 2 digits typed in, move on to next input
            next_elem = window.Element(key+1)
            next_elem.SetFocus()
        elif len(value)> 2 and key == 3:
            window.Element('_OK_').SetFocus()
            print('You entered IP Address {}.{}.{}.{}'.format(*values.values()))

window.Close()
