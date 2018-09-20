import pandas as pd
import PySimpleGUI as sg

def table_example():
    sg.SetOptions(auto_size_buttons=True)
    filename = sg.PopupGetFile('filename to open', no_window=True, file_types=(("CSV Files", "*.csv"),))
    # --- populate table with file contents --- #
    if filename == '':
        exit(69)
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
            exit(69)
    # sg.SetOptions(element_padding=(0, 0))

    col_layout = [[sg.Table(values=data, headings=header_list, display_row_numbers=True,
                            auto_size_columns=False, size=(None, len(data)))]]

    canvas_size = (13*10*len(header_list), 600)      # estimate canvas size - 13 pixels per char * 10 per column * num columns
    layout = [[sg.Column(col_layout, size=canvas_size, scrollable=True)]]

    form = sg.FlexForm('Table', grab_anywhere=False)
    b, v = form.LayoutAndRead(layout)

    exit(69)

table_example()
