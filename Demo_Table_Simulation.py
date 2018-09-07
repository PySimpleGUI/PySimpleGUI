import PySimpleGUI as sg

def TableSimulation():
    """
    Display data in a table format
    """
    # sg.ChangeLookAndFeel('Dark')
    sg.SetOptions(element_padding=(0,0))
    layout = [[sg.T('Table Using Combos and Input Elements', font='Any 18')],
              [sg.T('Row, Cal to change'),
               sg.In(key='inputrow', justification='right', size=(8,1), pad=(1,1), do_not_clear=True),
               sg.In(key='inputcol', size=(8,1), pad=(1,1), justification='right', do_not_clear=True),
               sg.In(key='value', size=(8,1), pad=(1,1), justification='right', do_not_clear=True)]]

    for i in range(20):
        inputs = [sg.In('{}{}'.format(i,j), size=(8, 1), pad=(1, 1), justification='right', key=(i,j), do_not_clear=True) for j in range(10)]
        inputs = [sg.Combo(('Customer ID', 'Customer Name', 'Customer Info')), *inputs]
        layout.append(inputs)

    form = sg.FlexForm('Table', return_keyboard_events=True)
    form.Layout(layout)

    while True:
        button, values = form.Read()
        if button is None:
            break
        try:
            location = (int(values['inputrow']), int(values['inputcol']))
            target_element = form.FindElement(location)
            new_value = values['value']
            if target_element is not None and new_value != '':
                target_element.Update(new_value)
        except:
            pass

TableSimulation()