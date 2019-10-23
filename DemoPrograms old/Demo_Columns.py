#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

sg.ChangeLookAndFeel('BlueMono')

# Column layout
col = [[sg.Text('col Row 1', text_color='white', background_color='blue')],
       [sg.Text('col Row 2', text_color='white', background_color='blue'), sg.Input('col input 1')],
       [sg.Text('col Row 3', text_color='white', background_color='blue'), sg.Input('col input 2')]]
# Window layout
layout = [[sg.Listbox(values=('Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'),
                      select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(20, 3)),
           sg.Column(col, background_color='blue')],
          [sg.Input('Last input')],
          [sg.OK()]]

# Display the window and get values
event, values = sg.Window('Compact 1-line form with column').Layout(layout).Read()

sg.Popup(event, values, line_width=200)

