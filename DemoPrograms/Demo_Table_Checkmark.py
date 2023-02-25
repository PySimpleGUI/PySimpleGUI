#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string

"""
    Demo Program - Table with checkboxes

    This clever solution was sugged by GitHub user robochopbg.
    The beauty of the simplicity is that the checkbox is simply another column in the table. When the checkbox changes
        state, then the data in the table is changed and the table is updated in the Table element.
    A big thank you again to user robochopbg!

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⠆⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⠟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀
⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠺⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠻⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠻⣿⣿⣷⣤⡀⠀⠀⣰⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣦⣼⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀

    Copyright 2023 PySimpleGUI
"""

# Characters used for the checked and unchecked checkboxes.  Feel free to change
BLANK_BOX = '☐'
CHECKED_BOX = '☑'

# ------ Some functions to help generate data for the table ------
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [BLANK_BOX if random.randint(0,2) % 2 else CHECKED_BOX] + [word(), *[number() for i in range(num_cols - 1)]]
    return data

# ------ Make the Table Data ------
data = make_table(num_rows=15, num_cols=6)
headings = [str(data[0][x])+' ..' for x in range(len(data[0]))]
headings[0] = 'Checkbox'
# The selected rows is stored in a set
selected = {i for i, row in enumerate(data[1:][:]) if row[0] == CHECKED_BOX}

# ------ Window Layout ------
layout = [[sg.Table(values=data[1:][:], headings=headings, max_col_width=25, auto_size_columns=False, col_widths=[10, 10, 20, 20 ,30, 5],
                    display_row_numbers=True, justification='center', num_rows=20, key='-TABLE-', selected_row_colors='red on yellow',
                    expand_x=False, expand_y=True, vertical_scroll_only=False, enable_click_events=True, font='_ 14'),
           sg.Sizegrip()]]

# ------ Create Window ------
window = sg.Window('Table with Checkbox', layout, resizable=True, finalize=True)

# Highlight the rows (select) that have checkboxes checked
window['-TABLE-'].update(values=data[1:][:], select_rows=list(selected))

# ------ Event Loop ------
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event[0] == '-TABLE-' and event[2][0] not in (None, -1):   # if clicked a data row rather than header or outside table
        row = event[2][0]+1
        if data[row][0] == CHECKED_BOX:     # Going from Checked to Unchecked
            selected.remove(row-1)
            data[row][0] = BLANK_BOX
        else:                               # Going from Unchecked to Checked
            selected.add(row-1)
            data[row ][0] = CHECKED_BOX
        window['-TABLE-'].update(values=data[1:][:], select_rows=list(selected))    # Update the table and the selected rows

window.close()

