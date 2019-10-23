#!/usr/bin/env python
import PySimpleGUI as sg

'''
    Usage of Column Element
'''

sg.change_look_and_feel('BlueMono')

css = {'text_color': 'white', 'background_color': 'blue'}
# Column layout
col = [[sg.Text('col Row 1', **css)],
       [sg.Text('col Row 2', **css), sg.Input('col input 1')],
       [sg.Text('col Row 3', **css), sg.Input('col input 2')]]
# Window layout
layout = [[sg.Listbox(values=('Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'),
                      select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(20, 3)),
           sg.Col(col, background_color='blue')],
          [sg.Input('Last input')],
          [sg.OK()]]

# Display the window and get values
window = sg.Window('Compact 1-line form with column', layout)
event, values = window.read()

sg.popup(event, values, line_width=200)

window.close()
