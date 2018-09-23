import PySimpleGUI as sg

sg.ChangeLookAndFeel('LightGreen')
sg.SetOptions(element_padding=(0, 0))

# ------ Menu Definition ------ #
menu_def = [['File', ['Open', 'Save', 'Exit' ]],
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['Help', 'About...'], ]

# ------ GUI Defintion ------ #
layout = [
    [sg.Menu(menu_def)],
    [sg.Output(size=(60, 20))]
]

form = sg.FlexForm("Windows-like program", default_element_size=(12, 1), auto_size_text=False, auto_size_buttons=False,
                   default_button_element_size=(12, 1)).Layout(layout)

# ------ Loop & Process button menu choices ------ #
while True:
    button, values = form.Read()
    if button == None or button == 'Exit':
        break
    print('Button = ', button)
    # ------ Process menu choices ------ #
    if button == 'About...':
        sg.Popup('About this program', 'Version 1.0', 'PySimpleGUI rocks...')
    elif button == 'Open':
        filename = sg.PopupGetFile('file to open', no_window=True)
        print(filename)