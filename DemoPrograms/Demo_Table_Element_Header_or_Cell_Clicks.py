#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string
import operator

"""
    Table Element Demo With Sorting and Cell Editing
    NOTE: release 5.0.6.5 needed in order to use the Cell Editing features.  Comment out the parameters that contain cell_edit to remove from demo
    
    The data for the table is assumed to have HEADERS across the first row.
    This is often the case for CSV files or spreadsheets

    This demo shows how you can use these click events to sort your table by columns

    Copyright 2022-2024 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

sg.theme('Light green 6')


# ------ Some functions to help generate data for the table ------
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))


def number(max_val=1000):
    return random.randint(0, max_val)


def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for _ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [i, word(), *[number() for i in range(num_cols - 2)]]
    return data


# ------ Make the Table Data ------
data = make_table(num_rows=15, num_cols=6)
# headings = [str(data[0][x])+'     ..' for x in range(len(data[0]))]
headings = [f'Col {col}' for col in range(1, len(data[0]) + 1)]


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
layout = [[sg.Table(values=data[1:][:], headings=headings + ['Extra'], max_col_width=25,
                    auto_size_columns=True,
                    display_row_numbers=False,
                    justification='right',
                    right_click_selects=True,
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    selected_row_colors='red on yellow',
                    enable_events=True,
                    expand_x=True,
                    expand_y=True,
                    enable_click_events=True,  # Comment out to not enable header and other clicks
                    enable_cell_editing=True,  # Comment out to if your PSG version does not support cell edint
                    cell_edit_colors='white on blue', # Comment out to if your PSG version does not support cell edint
                    cell_edit_select_colors='yellow on red', # Comment out to if your PSG version does not support cell edint
                    tooltip='This is a table')],
          [sg.Button('Read'), sg.Button('Double'), sg.Button('Change Colors')],
          [sg.Text('Cell clicked:'), sg.T(k='-CLICKED-')],
          [sg.Text('Read = read which rows are selected')],
          [sg.Text('Double = double the amount of data in the table')],
          [sg.Text('Change Colors = Changes the colors of rows 8 and 9'), sg.Sizegrip()]]

# ------ Create Window ------
window = sg.Window('The Table Element', layout, resizable=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, finalize=True, print_event_values=True)


# ------ Event Loop ------
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Edit Me':
        sg.execute_editor(__file__)
    elif event == 'Version':
        sg.popup_scrolled(__file__, sg.get_versions(), location=window.current_location(), keep_on_top=True, non_blocking=True)
    if event == 'Read':
        [print(row) for row in window['-TABLE-'].values]
    if event == 'Double':
        for i in range(1, len(data)):
            data.append(data[i].copy())
        window['-TABLE-'].update(values=data[1:][:])
    elif event == 'Change Colors':
        window['-TABLE-'].update(row_colors=((8, 'white', 'red'), (9, 'green')))

    # See if was a table clicked or edited event by checking event[0] for table's key
    if event[0] == '-TABLE-':   # TABLE CELL Event has value in format ('-TABLE=', '+type of event+', (row,col))
        if event[2][0] == -1 and event[2][1] != -1:  # Header was clicked and wasn't the "row" column
            col_num_clicked = event[2][1]
            new_table = sort_table(data[1:][:], (col_num_clicked, 0))
            window['-TABLE-'].update(new_table)
            data = [data[0]] + new_table
        window['-CLICKED-'].update(f'{event[2][0]},{event[2][1]}')
window.close()
