import PySimpleGUI as sg

layout = [[sg.Text('Filename', )],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]

button, (number,) = sg.FlexForm('Get filename example').LayoutAndRead(layout)



import PySimpleGUI as sg

button, (filename,) = sg.FlexForm('Get filename example').LayoutAndRead(
    [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()]])