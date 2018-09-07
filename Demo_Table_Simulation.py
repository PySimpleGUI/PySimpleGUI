import PySimpleGUI as sg

def TableSimulation():
    """
    Display data in a table format
    """
    # sg.ChangeLookAndFeel('Dark')

    layout = [[sg.T('Table Using Combos and Input Elements', font='Any 18')]]

    for i in range(20):
        inputs = [sg.In('{}{}'.format(i,j), size=(8, 1), pad=(1, 1), justification='right') for j in range(10)]
        inputs = [sg.Combo(('Customer ID', 'Customer Name', 'Customer Info')), *inputs]
        layout.append(inputs)

    sg.FlexForm('Table').LayoutAndRead(layout)


TableSimulation()