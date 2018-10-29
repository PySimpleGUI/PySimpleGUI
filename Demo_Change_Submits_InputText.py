#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

"""
    Demonstrates the new change_submits parameter for inputtext elements
    It ONLY submits when a button changes the field, not normal user input
    Be careful on persistent forms to not clear the input
"""
layout = [[ sg.Text('Test of reading input field') ],
          [sg.T('This input is normal'), sg.In()],
          [sg.T('This input change submits'), sg.In(change_submits=True)],
          [sg.T('This multiline input change submits'), sg.Multiline(change_submits=True, do_not_clear=True)],
          [sg.T('This input is normal'), sg.In(), sg.FileBrowse()],
          [sg.T('File Browse submits'), sg.In(change_submits=True,
                                             do_not_clear=True,
                                             key='_in1_'), sg.FileBrowse()],
          [sg.T('Color Chooser submits'), sg.In(change_submits=True,
                                             do_not_clear=True,
                                             key='_in2_'), sg.ColorChooserButton('Color...', target=(sg.ThisRow, -1))],
          [sg.T('Folder Browse submits'), sg.In(change_submits=True,
                                             do_not_clear=True,
                                             key='_in3_'), sg.FolderBrowse()],
          [sg.T('Calendar Chooser submits'), sg.In(change_submits=True,
                                             do_not_clear=True,
                                             key='_in4_'), sg.CalendarButton('Date...', target=(sg.ThisRow, -1))],
          [sg.T('Disabled input submits'), sg.In(change_submits=True,
                                             do_not_clear=True,
                                             disabled=True,
                                             key='_in5'), sg.FileBrowse()],
          [sg.T('This input clears after submit'),sg.In(change_submits=True,
                                                        key='_in6_'), sg.FileBrowse()],
          [ sg.Button('Read')]]

window = sg.Window('Demonstration of InputText with change_submits',
                   auto_size_text=False,
                   default_element_size=(22,1),
                   text_justification='right',
                   ).Layout(layout)

while True:     # Event Loop
    event, values = window.Read()
    print(event, values)
    if event is None:
        break
