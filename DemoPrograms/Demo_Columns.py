#!/usr/bin/env python
import PySimpleGUI as sg

'''
    Usage of Column Element
    
    How to embed a layout in a layout
    
    Copyright 2022-2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.
    
    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.
    
    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
'''

sg.theme('BlueMono')

# Column layout
col = [[sg.Text('col Row 1', text_color='white', background_color='blue')],
       [sg.Text('col Row 2', text_color='white', background_color='blue', pad=(0,(25,0))),sg.T('Another item'), sg.T('another'), sg.Input('col input 1')],
       [sg.Text('col Row 3', text_color='white', background_color='blue'), sg.Input('col input 2')]]
# Window layout
layout = [[sg.Listbox(values=('Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'),
                      select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(20, 3)),
           sg.Column(col, background_color='blue')],
          [sg.Input('Last input')],
          [sg.OK()]]

# Display the window and get values
window = sg.Window('Column Element', layout, margins=(0,0), element_padding=(0,0))
event, values = window.read()

sg.popup(event, values, line_width=200)

window.close()
