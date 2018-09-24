import PySimpleGUI as sg

layout = [[sg.T('Calendar Test')],
          [sg.In('', size=(20,1), key='input')],
          [sg.CalendarButton('Choose Date', target='input', key='date')],
          [sg.Ok(key=1)]]

window = sg.Window('Calendar', grab_anywhere=False).Layout(layout)
b,v = window.Read()
sg.Popup(v['input'])
