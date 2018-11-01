#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import pandas as pd


def table_example():
    sg.SetOptions(auto_size_buttons=True)
    filename = sg.PopupGetFile('filename to open', no_window=True, file_types=(("CSV Files", "*.csv"),))
    # --- populate table with file contents --- #
    if filename == '':
        sys.exit(69)
    data = []
    header_list = []
    button = sg.PopupYesNo('Does this file have column names already?')
    if filename is not None:
        try:
            df = pd.read_csv(filename, sep=',', engine='python', header=None)  # Header=None means you directly pass the columns names to the dataframe
            data = df.values.tolist()               # read everything else into a list of rows
            if button == 'Yes':                     # Press if you named your columns in the csv
                header_list = df.iloc[0].tolist()   # Uses the first row (which should be column names) as columns names
                data = df[1:].values.tolist()       # Drops the first row in the table (otherwise the header names and the first row will be the same)
            elif button == 'No':                    # Press if you didn't name the columns in the csv
                header_list = ['column' + str(x) for x in range(len(data[0]))]  # Creates columns names for each column ('column0', 'column1', etc)
        except:
            sg.PopupError('Error reading file')
            sys.exit(69)

    layout = [[sg.Table(values=data, headings=header_list, display_row_numbers=True,
                            auto_size_columns=False, num_rows=min(25,len(data)))]]

    window = sg.Window('Table', grab_anywhere=False)
    event, values = window.Layout(layout).Read()

    sys.exit(69)

table_example()
