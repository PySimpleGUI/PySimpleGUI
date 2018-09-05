import PySimpleGUI as sg

# Demo of how columns work
# Form has on row 1 a vertical slider followed by a COLUMN with 7 rows
# Prior to the Column element, this layout was not possible
# Columns layouts look identical to form layouts, they are a list of lists of elements.

# sg.ChangeLookAndFeel('BlueMono')


def ScrollableColumns():
    # sg.ChangeLookAndFeel('Dark')

    column1 = [[sg.Text('Column 1', justification='center', size=(20, 1))],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1', key='spin1', size=(30,1))],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3', key='spin3')]]


    column2 = [[sg.T('Table Test')]]

    for i in range(50):
        column2.append([sg.T(f'{i}{j}', size=(4, 1), background_color='gray25', text_color='white', pad=(1, 1)) for j in range(10)])

    layout = [[sg.Column(column2, scrollable=True), sg.Column(column1, scrollable=True, size=(200,150))],
              [sg.OK()]]

    form = sg.FlexForm('Form Fill Demonstration', default_element_size=(40, 1))
    b, v = form.LayoutAndRead(layout)

    sg.Popup(v)

def NormalColumns():
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

    sg.Popup(button, values, line_width=200)

NormalColumns()
ScrollableColumns()