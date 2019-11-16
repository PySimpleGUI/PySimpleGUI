import PySimpleGUI as sg

"""
    Another simple table created from Input Text Elements.  This demo adds the ability to "navigate" around the drawing using
    the arrow keys. The tab key works automatically, but the arrow keys are done in the code below.
"""

MAX_COLS = MAX_ROWS = 5

sg.change_look_and_feel('Dark Brown 1')     # No excuse for gray windows

# Create an Excel style window layout quickly and easily using list comprehensions
layout =  [[sg.Text(' '*11)]+[sg.Text(s+ ' '*19) for s in 'ABCDE'] ] + \
          [[sg.T(r)] + [sg.Input('0', justification='r', key=(r,c)) for c in range(MAX_COLS)] for r in range(MAX_ROWS)] + \
          [[sg.Button('Table Values'), sg.Button('Exit')]]

# Create the window and show it
window = sg.Window('A Table Simulation', layout, default_element_size=(12,1), element_padding=(1,1), return_keyboard_events=True)
current_cell = (0,0)
while True:             # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):         # If user closed the window
        break
    current_cell = window.find_element_with_focus().Key
    r,c = current_cell
    # Process arrow keys
    if event.startswith('Down'):
        r = r + 1 * (r < MAX_ROWS-1)
    if event.startswith('Left'):
        c = c - 1 *(c > 0)
    if event.startswith('Right'):
        c = c + 1 *(c < MAX_COLS-1)
    if event.startswith('Up'):
        r = r - 1 * (r > 0)
    # if the current cell changed, set focus on new cell
    if current_cell != (r,c):
      current_cell = r,c
      window[current_cell].set_focus()              # set the focus on the element moved to
      window[current_cell].update(select=True)      # when setting focus, also highlight the data in the element so typing overwrites
    # if clicked button to dump the table's values
    if event == 'Table Values':
      table = [[values[(row,col)] for col in range(MAX_COLS)] for row in range(MAX_ROWS)]
      print(f'table = {table}')