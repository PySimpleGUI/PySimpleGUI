#!/usr/bin/env python
import sys

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import random
import string


# ------------------ Create a fake table ------------------
class Fake():
    @classmethod
    def word(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

    @classmethod
    def number(self, max=1000):
        return random.randint(0,max)


def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [Fake.word() for _ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [Fake.word(), *[Fake.number() for i in range(num_cols - 1)]]
    return data

data = make_table(num_rows=15, num_cols=6)
# sg.SetOptions(element_padding=(0,0))
headings = [data[0][x] for x in range(len(data[0]))]

layout = [[sg.Table(values=data[1:][:], headings=headings, max_col_width=25, background_color='lightblue',
                        auto_size_columns=True, display_row_numbers=True, justification='right', num_rows=20, alternating_row_color='blue', key='_table_', tooltip='This is a table')],
          [sg.Button('Read'), sg.Button('Double'), sg.Button('Update')],
          [sg.T('Read = read which rows are selected')],[sg.T('Double = double the amount of data in the table')]]

window = sg.Window('Table', grab_anywhere=False, resizable=True).Layout(layout)

while True:
    event, values = window.Read()
    print(event, values)
    if event is None:
        break
    if event == 'Double':
        for i in range(len(data)):
            data.append(data[i])
        window.FindElement('_table_').Update(values = data)
    elif event == 'Update':
        window.FindElement('_table_').Update( row_colors=((8,'red'), (9,'black')))

    # sg.Popup(event, values)
    # print(event, values)
window.Close()
sys.exit(69)
