#!/usr/bin/env python
import PySimpleGUI as sg


layout = [[sg.Text('Calendar Test')],
          [sg.Input('', size=(20, 1), key='input')],
          [sg.CalendarButton('Choose Date', target='input', key='date')],
          [sg.Ok(key=1)]]

window = sg.Window('Calendar', layout, grab_anywhere=False)
event, values = window.read()
sg.popup(values['input'])
windowclose()
