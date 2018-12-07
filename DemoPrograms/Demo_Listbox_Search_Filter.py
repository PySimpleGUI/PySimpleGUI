import PySimpleGUI as sg

names = ['Roberta', 'Kylie', 'Jenny', 'Helen',
        'Andrea', 'Meredith','Deborah','Pauline',
        'Belinda', 'Wendy']

layout = [  [sg.Text('Listbox with search')],
            [sg.Input(do_not_clear=True, size=(20,1),enable_events=True, key='_INPUT_')],
            [sg.Listbox(names, size=(20,4), enable_events=True, key='_LIST_')],
            [sg.Button('Chrome'), sg.Button('Exit')]]

window = sg.Window('Listbox with Search').Layout(layout)
# Event Loop
while True:
    event, values = window.Read()
    if event is None or event == 'Exit':                # always check for closed window
        break
    if values['_INPUT_'] != '':                         # if a keystroke entered in search field
        search = values['_INPUT_']
        new_values = [x for x in names if search in x]  # do the filtering
        window.Element('_LIST_').Update(new_values)     # display in the listbox
    else:
        window.Element('_LIST_').Update(names)          # display original unfiltered list
    if event == '_LIST_' and len(values['_LIST_']):     # if a list item is chosen
        sg.Popup('Selected ', values['_LIST_'])

window.Close()
