import PySimpleGUI as sg

"""
Show a complex form, save the initial values
When the "Fill" button is clicked, the form will reset to the initial values
"""

def Everything():
    sg.ChangeLookAndFeel('Dark')


    column1 = [[sg.Text('Column 1', background_color='black', justification='center', size=(10, 1))],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]

    layout = [
        [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.InputText('This is my text')],
        [sg.Checkbox('Checkbox'),  sg.Checkbox('My second checkbox!', default=True)],
        [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
        [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
         sg.Multiline(default_text='A second multi-line', size=(35, 3))],
        [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),
         sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
        [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10, key='slider'),
         sg.Column(column1, background_color='black')],
        [sg.Text('_' * 80)],
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
         sg.InputText('Default Folder'), sg.FolderBrowse()],
        [sg.ReadFormButton('Fill'), sg.Cancel()]
    ]

    form = sg.FlexForm('Form Fill Demonstration', default_element_size=(40, 1))
    form.Layout(layout)
    button, initial_values = form.ReadNonBlocking()

    while True:
        button, values = form.Read()
        if button in (None, 'Cancel'):
            break
        form.Fill(initial_values)           # fill form with whatever initial values were

    sg.Popup('Title', 'The results of the form.', 'The button clicked was "{}"'.format(button), 'The values are', values)

Everything()
