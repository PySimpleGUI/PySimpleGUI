#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI_Qt as sg
else:
    import PySimpleGUI27 as sg

sg.ChangeLookAndFeel('GreenTan')

# # Column layout
# col = [[sg.Text('col Row 1', text_color='white', background_color='blue')],
#        [sg.Text('col Row 2', text_color='white', background_color='blue'), sg.Input('col input 1')],
#        [sg.Text('col Row 3', text_color='white', background_color='blue'), sg.Input('col input 2')]]
# # Window layout
# layout = [  [sg.In()],
#             [sg.Text('test'), sg.Column(col, background_color='blue')],]
#
# # Display the window and get values
# event, values = sg.Window('Compact 1-line form with column').Layout(layout).Read()
#
# exit()
# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='lightblue',text_color='black', justification='center', size=(100,30))],
           [sg.Spin((1,10), size=(100,30))],
           [sg.Spin((1,10), size=(100,30))],
           [sg.Spin((1,10), size=(100,30))],]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('(Almost) All widgets in one Window!', size=(600, 50), justification='l', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.InputText('This is my text', size=(300,30))],
    [sg.Frame(layout=[
    [sg.Checkbox('Checkbox', size=(185,30)),  sg.Checkbox('My second checkbox!', default=True)],
    [sg.Radio('My first Radio!', "RADIO1", default=True, size=(180,30), ),sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags', ), sg.Stretch()],
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(300, 80)),
     sg.Multiline(default_text='A second multi-line', size=(300, 80))],
    [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(150, 30)),
     sg.Slider(range=(1, 100), orientation='h', size=(150, 30), default_value=85)],
    [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(200,100)),
     sg.Frame('Labelled Group',[[
     sg.Slider(range=(1, 100), orientation='v', default_value=25, tick_interval=25),
     sg.Slider(range=(1, 100), orientation='v', default_value=75),
     sg.Slider(range=(1, 100), orientation='v', default_value=10),
     sg.Column(column1, background_color='lightblue')]]), sg.Stretch()],
    [sg.Text('_' * 80)],
    [sg.Text('Choose A Folder')],
    [sg.Text('Your Folder', auto_size_text=True, justification='right'),
     sg.InputText('Default Folder', size=(300,30)), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to submit this form', size=(120,30)), sg.Cancel(size=(120,30))]]

window = sg.Window('Everything bagel', default_element_size=(40, 1), grab_anywhere=False, font=('Helvetica', 12)).Layout(layout)
event, values = window.Read()

sg.Popup('Title',
         'The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values)


