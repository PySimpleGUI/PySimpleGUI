import csv
import PySimpleGUI as sg

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
            exit(69)

sg.SetOptions(element_padding=(0, 0))

col_layout = [[sg.Table(values=data, headings=[x for x in range(len(data[0]))], max_col_width=8,
                        auto_size_columns=False, justification='right', size=(8, len(data)))]]

layout = [[sg.Column(col_layout, size=(1200,600), scrollable=True)],]

form = sg.FlexForm('Table', grab_anywhere=False)
b, v = form.LayoutAndRead(layout)

exit(69)
