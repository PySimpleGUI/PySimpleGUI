#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import csv

def table_example():
    filename = sg.PopupGetFile('filename to open', no_window=True, file_types=(("CSV Files","*.csv"),))
    # --- populate table with file contents --- #
    if filename == '':
        sys.exit(69)
    data = []
    header_list = []
    button = sg.PopupYesNo('Does this file have column names already?')
    if filename is not None:
        with open(filename, "r") as infile:
            reader = csv.reader(infile)
            if button == 'Yes':
                header_list = next(reader)
            try:
                data = list(reader)  # read everything else into a list of rows
                if button == 'No':
                    header_list = ['column' + str(x) for x in range(len(data[0]))]
            except:
                sg.PopupError('Error reading file')
                sys.exit(69)
    sg.SetOptions(element_padding=(0, 0))

    layout = [[sg.Table(values=data,
                            headings=header_list,
                            max_col_width=25,
                            auto_size_columns=True,
                            justification='right',
                            alternating_row_color='lightblue',
                            num_rows=min(len(data), 20))]]


    window = sg.Window('Table', grab_anywhere=False).Layout(layout)
    event, values = window.Read()

    sys.exit(69)

table_example()
