#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string

# Yet another example of showing CSV data in Table


def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)


def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for _ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data


data = make_table(num_rows=15, num_cols=6)
# sg.set_options(element_padding=(0,0))
headings = [data[0][x] for x in range(len(data[0]))]

layout = [[sg.Table(values=data[1:][:], headings=headings, max_col_width=25, background_color='lightblue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='blue',
                    key='-table-',
                    tooltip='This is a table')],
          [sg.Button('Read'), sg.Button('Double'), sg.Button('Update')],
          [sg.Text('Read = read which rows are selected')], [sg.Text('Double = double the amount of data in the table')]]

window = sg.Window('Table', layout, grab_anywhere=False, resizable=True)

while True:
    event, values = window.read()
    print(event, values)
    if event is None:
        break
    if event == 'Double':
        for i in range(len(data)):
            data.append(data[i])
        window['-table-'].update(values=data)
    elif event == 'Update':
        window['-table-'].update(row_colors=((8, 'white',
                                              'red'), (9, 'black')))

window.close()
