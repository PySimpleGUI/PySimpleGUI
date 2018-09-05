import PySimpleGUI as sg

layout = [[sg.T('Calendar Test')],
          [sg.In('', size=(20,1))],
          [sg.CalendarButton('Choose Date', target=(1,0), key='date')],
          [sg.Ok(key=1)]]

form = sg.FlexForm('Calendar', no_titlebar=True)
b,v = form.LayoutAndRead(layout)
sg.Popup(v['date'])
