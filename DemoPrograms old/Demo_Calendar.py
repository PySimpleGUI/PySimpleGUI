#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

layout = [[sg.T('Calendar Test')],
          [sg.In('', size=(20,1), key='input')],
          [sg.CalendarButton('Choose Date', target='input', key='date')],
          [sg.Ok(key=1)]]

window = sg.Window('Calendar', grab_anywhere=False).Layout(layout)
event,values = window.Read()
sg.Popup(values['input'])
