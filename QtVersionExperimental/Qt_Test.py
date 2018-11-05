import PySimpleGUI_Qt as sg
layout = [
        [sg.Text('Hello PySimpleGUI!'),sg.Text(' '*5), sg.Text('On the same row'), ],
        [sg.Text('Input something here'), sg.Input('default text')],
        [sg.Combo(['Combo 1', 'Combo 2', 'Combo 3'])],
        [sg.Listbox(['Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'], size=(30,10)),
        sg.Slider((1,100))],
        [sg.Slider((1,10), orientation='h')],
        [sg.Checkbox('Checkbox 1')],
        [sg.Checkbox('Checkbox 2')],
        [sg.Checkbox('Checkbox 3')],
        [sg.Radio('Radio1', group_id=1),sg.Radio('Radio2', group_id=1)],
        [sg.Spin((5,8))],
        [sg.Button('My Button')],
          ]
window = sg.Window('My first QT Window').Layout(layout)
while True:
    event, values = window.Read()
    print(event, values)

