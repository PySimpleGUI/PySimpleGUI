import PySimpleGUI as sg

# Demo of how columns work
# Form has on row 1 a vertical slider followed by a COLUMN with 7 rows
# Prior to the Column element, this layout was not possible
# Columns layouts look identical to form layouts, they are a list of lists of elements.

# sg.ChangeLookAndFeel('BlueMono')

# Column layout
col = [[sg.Text('col Row 1', text_color='white', background_color='blue')],
       [sg.Text('col Row 2', text_color='white', background_color='blue'), sg.Input('col input 1')],
       [sg.Text('col Row 3', text_color='white', background_color='blue'), sg.Input('col input 2')]]

layout = [[sg.Listbox(values=('Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(20,3)), sg.Column(col, background_color='blue')],
          [sg.Input('Last input')],
          [sg.OK()]]

# Display the form and get values
# If you're willing to not use the "context manager" design pattern, then it's possible
# to collapse the form display and read down to a single line of code.
button, values = sg.FlexForm('Compact 1-line form with column').LayoutAndRead(layout)

sg.MsgBox(button, values, line_width=200)
