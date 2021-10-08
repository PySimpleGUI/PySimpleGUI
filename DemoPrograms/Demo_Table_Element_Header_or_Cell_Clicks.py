#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string
import operator

"""
    Table Element Demo With Sorting

    The data for the table is assumed to have HEADERS across the first row.
    This is often the case for CSV files or spreadsheets

    In release 4.48.0 a new enable_click_events parameter was added to the Table Element
    This enables you to click on Column Headers and individual cells as well as the standard Row selection

    This demo shows how you can use these click events to sort your table by columns

"""

sg.theme('Light green 6')
# ------ Some functions to help generate data for the table ------
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [i, word(), *[number() for i in range(num_cols - 1)]]
    return data

# ------ Make the Table Data ------
data = make_table(num_rows=15, num_cols=6)
# headings = [str(data[0][x])+'     ..' for x in range(len(data[0]))]
headings = [f'Col {col}' for col in range(len(data[0]))]

def sort_table(table, cols):
    """ sort a table by multiple columns
        table: a list of lists (or tuple of tuples) where each inner list
               represents a row
        cols:  a list (or tuple) specifying the column numbers to sort by
               e.g. (1,0) would sort by column 1, then by column 0
    """
    for col in reversed(cols):
        try:
            table = sorted(table, key=operator.itemgetter(col))
        except Exception as e:
            sg.popup_error('Error in sort_table', 'Exception in sort_table', e)
    return table

# ------ Window Layout ------
layout = [[sg.Table(values=data[1:][:], headings=headings, max_col_width=25,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    selected_row_colors='red on yellow',
                    enable_events=True,
                    expand_x=True,
                    expand_y=True,
                    enable_click_events=True,           # Comment out to not enable header and other clicks
                    tooltip='This is a table')],
          [sg.Button('Read'), sg.Button('Double'), sg.Button('Change Colors')],
          [sg.Text('Cell clicked:'), sg.T(k='-CLICKED-')],
          [sg.Text('Read = read which rows are selected')],
          [sg.Text('Double = double the amount of data in the table')],
          [sg.Text('Change Colors = Changes the colors of rows 8 and 9'), sg.Sizegrip()]]

# ------ Create Window ------
window = sg.Window('The Table Element', layout,
                   ttk_theme='clam',
                   resizable=True)

# ------ Event Loop ------
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Double':
        for i in range(1, len(data)):
            data.append(data[i])
        window['-TABLE-'].update(values=data[1:][:])
    elif event == 'Change Colors':
        window['-TABLE-'].update(row_colors=((8, 'white', 'red'), (9, 'green')))
    if isinstance(event, tuple):
        # TABLE CLICKED Event has value in format ('-TABLE=', '+CLICKED+', (row,col))
        if event[0] == '-TABLE-':
            if event[2][0] == -1 and event[2][1] != -1:           # Header was clicked and wasn't the "row" column
                col_num_clicked = event[2][1]
                new_table = sort_table(data[1:][:],(col_num_clicked, 0))
                window['-TABLE-'].update(new_table)
                data = [data[0]] + new_table
            window['-CLICKED-'].update(f'{event[2][0]},{event[2][1]}')
window.close()
