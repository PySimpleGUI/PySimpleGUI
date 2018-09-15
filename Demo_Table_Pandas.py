import pandas as pd
import PySimpleGUI as sg

"""

    Display a CSV file using Table Element and Pandas
    Thank you to     for writing this demo

"""


def table_example():
    filename = sg.PopupGetFile('filename to open', no_window=True, file_types=(("CSV Files", "*.csv"),))
    # --- populate table with file contents --- #
    data = []
    header_list = []
    if filename is not None:
        try:
            df = pd.read_csv(filename, sep=',', engine='python')  # read everything else into a list of rows
            header_list = df.columns.tolist()
            data = df.values.tolist()
            # print(data)
        except:
            sg.PopupError('Error reading file')
            exit(69)

    sg.SetOptions(element_padding=(0, 0))

    col_layout = [[sg.Table(values=data, headings=header_list, max_col_width=20,
                            auto_size_columns=True, justification='right', size=(None, len(data)))]]

    layout = [[sg.Column(col_layout, size=(1200, 600), scrollable=True)]]

    form = sg.FlexForm('Table', grab_anywhere=False)
    b, v = form.LayoutAndRead(layout)

    exit(69)


table_example()
