import csv
import PySimpleGUI as sg
import sys

filename = sg.PopupGetFile('filename to open', no_window=True, file_types=(("CSV Files","*.csv"),))
# --- populate table with file contents --- #
data = []
if filename is not None:
    with open(filename, "r") as infile:
        reader = csv.reader(infile)
        try:
            data = list(reader)  # read everything else into a list of rows
        except:
            sg.PopupError('Error reading file')
            sys.exit(69)

sg.SetOptions(element_padding=(0, 0))

col_layout = [[sg.Table(values=data[1:][:], headings=[data[0][x] for x in range(len(data[0]))], max_col_width=25,
                        auto_size_columns=True, display_row_numbers=True, justification='right', size=(None, len(data)))]]

layout = [[sg.Column(col_layout, size=(1200,600), scrollable=True)],]
window = sg.Window('Table', grab_anywhere=False).Layout(layout)

b, v = window.Read()

sys.exit(69)
