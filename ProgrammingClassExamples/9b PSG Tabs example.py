import PySimpleGUI as sg

tab1_layout =  [[sg.Text('This is inside tab 1')]]

tab2_layout = [[sg.Text('This is inside tab 2')]]

layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout),
                         sg.Tab('Tab 2', tab2_layout)]])],
          [sg.ReadButton('Read')]]

window = sg.Window('Main Window').Layout(layout)

while True:
    b, v = window.Read()
    if b is not None:
        print(b,v)
    else:
        break
