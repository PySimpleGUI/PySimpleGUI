import PySimpleGUI as sg

def ShowMainForm():

    listbox_values = ('Text', 'InputText', 'Checkbox', 'Radio Button', 'Listbox', 'Slider' )

    column2 = [ [sg.Output(size=(50, 20))],
                [sg.ReadFormButton('Show Element'), sg.SimpleButton('Exit')]]

    column1 = [[sg.Listbox(values=listbox_values, size=(20, len(listbox_values)), key='listbox')],
               [sg.Text('', size=(10, 15))]]

    layout = [[sg.Column(column1) , sg.Column(column2)]]

    form = sg.FlexForm('Element Browser')
    form.Layout(layout)
    while True:
        button, values = form.Read()
        if button is None or button == 'Exit':
            break
        sg.MsgBox(button, values['listbox'][0])


ShowMainForm()
