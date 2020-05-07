import PySimpleGUI as sg
from random import randint
import operator

"""
    Another simple table created from Input Text Elements.  This demo adds the ability to "navigate" around the drawing using
    the arrow keys. The tab key works automatically, but the arrow keys are done in the code below.
"""

sg.theme('Dark Brown 2')  # No excuse for gray windows
# Show a "splash" type message so the user doesn't give up waiting
sg.popup_quick_message('Hang on for a moment, this will take a bit to create....', auto_close=True, non_blocking=True)

MAX_ROWS, MAX_COLS, COL_HEADINGS = 15, 6, ('A', 'B', 'C', 'D', 'E', 'F',)

# A HIGHLY unusual layout definition
# Normally a layout is specified 1 ROW at a time. Here multiple rows are being contatenated together to produce the layout
# Note the " + \ " at the ends of the lines rather than the usual " , "
# This is done because each line is a list of lists
layout = [[sg.Text('Click on a column header to sort by that column', font='Default 16')]] + \
         [[sg.Text(' ' * 15)] + [sg.Text(s, key=s, enable_events=True, font='Courier 14', size=(8, 1)) for i, s in enumerate(COL_HEADINGS)]] + \
         [[sg.T(r, size=(4, 1))] + [sg.Input(randint(0, 100), justification='r', key=(r, c)) for c in range(MAX_COLS)] for r in range(MAX_ROWS)] + \
         [[sg.Button('Show Table As Lists'), sg.Button('Exit')]]

# Create the window
window = sg.Window('A Table Simulation', layout, default_element_size=(12, 1), element_padding=(1, 1), return_keyboard_events=True)

current_cell = (0, 0)
while True:  # Event Loop
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):     # If user closed the window
        break
    elem = window.find_element_with_focus()
    current_cell = elem.Key if elem and type(elem.Key) is tuple else (0, 0)
    r, c = current_cell

    if event.startswith('Down'):
        r = r + 1 * (r < MAX_ROWS - 1)
    elif event.startswith('Left'):
        c = c - 1 * (c > 0)
    elif event.startswith('Right'):
        c = c + 1 * (c < MAX_COLS - 1)
    elif event.startswith('Up'):
        r = r - 1 * (r > 0)
    elif event in COL_HEADINGS:         # Perform a sort if a column heading was clicked
        col_clicked = COL_HEADINGS.index(event)
        try:
            table = [[int(values[(row, col)]) for col in range(MAX_COLS)] for row in range(MAX_ROWS)]
            new_table = sorted(table, key=operator.itemgetter(col_clicked))
        except:
            sg.popup_error('Error in table', 'Your table must contain only ints if you wish to sort by column')
        else:
            for i in range(MAX_ROWS):
                for j in range(MAX_COLS):
                    window[(i, j)].update(new_table[i][j])
            [window[c].update(font='Any 14') for c in COL_HEADINGS]     # make all column headings be normal fonts
            window[event].update(font='Any 14 bold')                    # bold the font that was clicked
    # if the current cell changed, set focus on new cell
    if current_cell != (r, c):
        current_cell = r, c
        window[current_cell].set_focus()          # set the focus on the element moved to
        window[current_cell].update(select=True)  # when setting focus, also highlight the data in the element so typing overwrites
    # if clicked button to dump the table's values
    if event.startswith('Show Table'):
        table = [[values[(row, col)] for col in range(MAX_COLS)] for row in range(MAX_ROWS)]
        sg.popup_scrolled('your_table = [ ', ',\n'.join([str(table[i]) for i in range(MAX_ROWS)]) + '  ]', title='Copy your data from here', font='fixedsys', keep_on_top=True)
