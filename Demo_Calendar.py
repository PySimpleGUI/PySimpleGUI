import PySimpleGUI as sg

layout = [[sg.T('Calendar Test')],
          [sg.CalendarButton('Choose Date', key='date')],
          [sg.Ok(key=1)]]

form = sg.FlexForm('Calendar')
b,v = form.LayoutAndRead(layout)
sg.Popup(v['date'])
