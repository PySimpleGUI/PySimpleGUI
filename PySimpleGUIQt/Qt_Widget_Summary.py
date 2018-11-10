import PySimpleGUIQt as sg

sg.ChangeLookAndFeel('LightGreen')

layout = [
            [sg.Text('Widgets Currently Supported By PySimpleGUIQt')],
            [sg.Text('Text', size=(200,35)), sg.Text('Text In Any Color/Font', font=('Courier', 15), text_color='red')],
            [sg.Text('Single Line Input', size=(200,35)), sg.Input(size=(200,25))],
            [sg.Text('Multi Line\nInput/Output', size=(200,60)), sg.Multiline(size=(200,75))],
            [sg.Text('ListBox', size=(200,35)),sg.Listbox(['Listbox 1','Listbox 2','Listbox 3'], size=(200,85)) ],
            [sg.Text('ComboBox / Dropdown', size=(200,25)),sg.Combo(['Combo item 1',], size=(200,35)) ],
            [sg.Text('Spinner', size=(200,35)),sg.Spin([1,2,3], size=(40,30)) ],
            [sg.Text('Checkbox', size=(200,35)), sg.Checkbox('Checkbox', change_submits=True) ],
            [sg.Text('RadioButton', size=(200,35)), sg.Radio('Radio Button', 1) ],
            [sg.Text('Slider', size=(200,35)), sg.Slider(orientation='h') ],
            [sg.Text('Button', size=(200,35)), sg.Button('Button') ],
            [sg.Text('Table', size=(200,35)), sg.Table([[0,1,3,4]])],
            [sg.Text('Frame', size=(200,35)), sg.Frame('Frame',[[sg.T('')],[sg.T('')]])],
            [sg.Text('Stdout Output', size=(200,35)), sg.Output(size=(200,75)) ],
            [sg.Text('Dial', size=(200,35)),sg.Dial(size=(150,75)), sg.Stretch() ],
            [sg.Button('Blank'), sg.Button('Exit')]
         ]

window = sg.Window('Window Title',
                   font=('Helvetica', 13)).Layout(layout)

while True:             # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break

window.Close()
