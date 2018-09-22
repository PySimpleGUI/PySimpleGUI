import PySimpleGUI as sg

layout = [[sg.T('Calendar Test')],
          [sg.In('', size=(20,1), key='input')],
          [sg.CalendarButton('Choose Date', target='input', key='date')],
          [sg.Ok(key=1)]]

form = sg.FlexForm('Calendar', grab_anywhere=False)
b,v = form.LayoutAndRead(layout)
sg.Popup(v['input'])
