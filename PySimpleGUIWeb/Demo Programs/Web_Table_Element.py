import PySimpleGUIWeb as sg
import random
import string

# Example with Table element

def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))

def number(max_val=1000):
    return random.randint(0,max_val)


def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for _ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data

table_data = make_table(num_rows=15, num_cols=6)

# ------------------ Create a window layout ------------------
layout = [[sg.Table(values=table_data, enable_events=True,
            display_row_numbers=True, font='Courier 14',
              row_header_text='Row #', key='_table_', text_color='red')],
          [sg.Button('Exit')],
          [sg.Text('Selected rows = '), sg.Text('', size=(30,1), key='_selected_rows_')],
          [sg.Text('Selected value = '), sg.Text('', size=(30,1), key='_selected_value_')]]

# ------------------ Create the window ------------------
window = sg.Window('Table Element Example', layout)

# ------------------ The Event Loop ------------------
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    window['_selected_rows_'].update(values['_table_'])
    window['_selected_value_'].update(window['_table_'].SelectedItem)
# ------------------ User closed window so exit ------------------
window.close()
