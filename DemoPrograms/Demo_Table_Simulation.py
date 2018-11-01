#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import csv


def TableSimulation():
    """
    Display data in a table format
    """
    sg.SetOptions(element_padding=(0,0))

    menu_def = [['File', ['Open', 'Save', 'Exit']],
                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                ['Help', 'About...'],]

    columm_layout = [[]]

    MAX_ROWS = 20
    MAX_COL = 10
    for i in range(MAX_ROWS):
        inputs = [sg.T('{}'.format(i), size=(4,1), justification='right')] + [sg.In(size=(10, 1), pad=(1, 1), justification='right', key=(i,j), do_not_clear=True) for j in range(MAX_COL)]
        columm_layout.append(inputs)

    layout = [ [sg.Menu(menu_def)],
               [sg.T('Table Using Combos and Input Elements', font='Any 18')],
               [sg.T('Type in a row, column and value. The form will update the values in realtime as you type'),
               sg.In(key='inputrow', justification='right', size=(8,1), pad=(1,1), do_not_clear=True),
               sg.In(key='inputcol', size=(8,1), pad=(1,1), justification='right', do_not_clear=True),
               sg.In(key='value', size=(8,1), pad=(1,1), justification='right', do_not_clear=True)],
               [sg.Column(columm_layout, size=(800,600), scrollable=True)] ]

    window = sg.Window('Table', return_keyboard_events=True).Layout(layout)

    while True:
        event, values = window.Read()
        # --- Process buttons --- #
        if event is None or event == 'Exit':
            break
        elif event == 'About...':
            sg.Popup('Demo of table capabilities')
        elif event == 'Open':
            filename = sg.PopupGetFile('filename to open', no_window=True, file_types=(("CSV Files","*.csv"),))
            # --- populate table with file contents --- #
            if filename is not None:
                with open(filename, "r") as infile:
                    reader = csv.reader(infile)
                    try:
                        data = list(reader)  # read everything else into a list of rows
                    except:
                        sg.PopupError('Error reading file')
                        continue
                # clear the table
                [window.FindElement((i,j)).Update('') for j in range(MAX_COL) for i in range(MAX_ROWS)]

                for i, row in enumerate(data):
                    for j, item in enumerate(row):
                        location = (i,j)
                        try:            # try the best we can at reading and filling the table
                            target_element = window.FindElement(location)
                            new_value = item
                            if target_element is not None and new_value != '':
                                target_element.Update(new_value)
                        except:
                            pass

        # if a valid table location entered, change that location's value
        try:
            location = (int(values['inputrow']), int(values['inputcol']))
            target_element = window.FindElement(location)
            new_value = values['value']
            if target_element is not None and new_value != '':
                target_element.Update(new_value)
        except:
            pass

TableSimulation()