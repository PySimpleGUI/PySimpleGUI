import PySimpleGUI as sg

tab1_layout =  [[sg.T('This is inside tab 1')]]

tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.In(key='in')]]

layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, tooltip='tip'), sg.Tab('Tab 2', tab2_layout)]], tooltip='TIP2')],
          [sg.RButton('Read')]]

window = sg.Window('My window with tabs', default_element_size=(12,1)).Layout(layout)

while True:
    b, v = window.Read()
    print(b,v)
    if b is None:           # always,  always give a way out!
        break