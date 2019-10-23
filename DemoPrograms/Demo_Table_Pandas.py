#!/usr/bin/env python
import PySimpleGUI as sg
import pandas as pd

# Yet another example of showing CSV data in Table

def table_example():

    sg.set_options(auto_size_buttons=True)
    filename = sg.popup_get_file(
        'filename to open', no_window=True, file_types=(("CSV Files", "*.csv"),))
    # --- populate table with file contents --- #
    if filename == '':
        return

    data = []
    header_list = []
    button = sg.popup_yes_no('Does this file have column names already?')

    if filename is not None:
        try:
            # Header=None means you directly pass the columns names to the dataframe
            df = pd.read_csv(filename, sep=',', engine='python', header=None)
            data = df.values.tolist()               # read everything else into a list of rows
            if button == 'Yes':                     # Press if you named your columns in the csv
                # Uses the first row (which should be column names) as columns names
                header_list = df.iloc[0].tolist()
                # Drops the first row in the table (otherwise the header names and the first row will be the same)
                data = df[1:].values.tolist()
            elif button == 'No':                    # Press if you didn't name the columns in the csv
                # Creates columns names for each column ('column0', 'column1', etc)
                header_list = ['column' + str(x) for x in range(len(data[0]))]
        except:
            sg.popup_error('Error reading file')
            return

    layout = [
        [sg.Table(values=data,
                  headings=header_list,
                  display_row_numbers=True,
                  auto_size_columns=False,
                  num_rows=min(25, len(data)))]
    ]

    window = sg.Window('Table', layout, grab_anywhere=False)
    event, values = window.read()
    window.close()


table_example()
