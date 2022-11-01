#!/usr/bin/env python
import PySimpleGUI as sg
import csv


def TableSimulation():
    """
    Display data in a table format
    """

    sg.popup_quick_message('Hang on for a moment, this will take a bit to create....', auto_close=True, non_blocking=True, font='Default 18')

    sg.set_options(element_padding=(0, 0))

    menu_def = [['File', ['Open', 'Save', 'Exit']],
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['Help', 'About...'], ]

    MAX_ROWS = 20
    MAX_COL = 10

    columm_layout =  [[sg.Text(str(i), size=(4, 1), justification='right')] + [sg.InputText(size=(10, 1), pad=(1,1),border_width=0, justification='right', key=(i, j)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]


    layout = [[sg.Menu(menu_def)],
              [sg.Text('Table Using Combos and Input Elements', font='Any 18')],
              [sg.Text('Type in a row, column and value. The form will update the values in realtime as you type'),
               sg.Input(key='inputrow', justification='right', size=(8, 1), pad=(1, 1)),
               sg.Input(key='inputcol', size=(8, 1), pad=(1, 1), justification='right'),
               sg.Input(key='value', size=(8, 1), pad=(1, 1), justification='right')],
              [sg.Col(columm_layout, size=(800, 600), scrollable=True)]]

    window = sg.Window('Table', layout,  return_keyboard_events=True, resizable=True)

    while True:
        event, values = window.read()
        # --- Process buttons --- #
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'About...':
            sg.popup('Demo of table capabilities')
        elif event == 'Open':
            filename = sg.popup_get_file(
                'filename to open', no_window=True, file_types=(("CSV Files", "*.csv"),))
            # --- populate table with file contents --- #
            if filename is not None:
                with open(filename, "r") as infile:
                    reader = csv.reader(infile)
                    try:
                        # read everything else into a list of rows
                        data = list(reader)
                    except:
                        sg.popup_error('Error reading file')
                        continue
                # clear the table
                [window[(i, j)].update('') for j in range(MAX_COL)
                 for i in range(MAX_ROWS)]

                for i, row in enumerate(data):
                    for j, item in enumerate(row):
                        location = (i, j)
                        try:            # try the best we can at reading and filling the table
                            target_element = window[location]
                            new_value = item
                            if target_element is not None and new_value != '':
                                target_element.update(new_value)
                        except:
                            pass

        # if a valid table location entered, change that location's value
        try:
            location = (int(values['inputrow']), int(values['inputcol']))
            target_element = window[location]
            new_value = values['value']
            if target_element is not None and new_value != '':
                target_element.update(new_value)
        except:
            pass

    window.close()


TableSimulation()
