#!/usr/bin/env python
import PySimpleGUIQt as sg

sg.ChangeLookAndFeel('GreenTan')
# sg.SetOptions(text_color='white')
# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', background_color='lightblue',text_color='black', justification='center', size=(100,22))],
           [sg.Spin((1,10), size=(100,22))],
           [sg.Spin((1,10), size=(100,22))],
           [sg.Spin((1,10), size=(100,22))],]

layout = [
    [sg.Text('(Almost) All widgets in one Window!',click_submits=True, key='TEXT', justification='c', font=("Helvetica", 25), relief=sg.RELIEF_RAISED, tooltip='Text Element')],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.InputText('This is my text', size=(400,25))],
    [sg.Frame(layout=[
        [sg.Checkbox('Checkbox', size=(185,22)),  sg.Checkbox('My second checkbox!', default=True)],
        [sg.Radio('My first Radio!', "RADIO1", default=True, size=(180,22), ),sg.Radio('My second Radio!', "RADIO1")],
        [sg.Radio('Third Radio!', "RADIO2", default=True, size=(180,22), ),
         sg.Radio('Fourth Radio!', "RADIO2")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN,
        tooltip='Use these to set flags', ), sg.Stretch()],
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything',focus=True, size=(220, 80)),
     sg.Multiline(default_text='A second multi-line', size=(220, 80))],
    [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(150, 25)), sg.Stretch(),
     sg.Slider(range=(1, 100), orientation='h', size=(300, 22), default_value=85)],
    [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(200,100), select_mode=sg.LISTBOX_SELECT_MODE_EXTENDED), sg.Stretch(),
     sg.Frame('Labelled Group',[[
     sg.Slider(range=(1, 100), orientation='v', default_value=25, tick_interval=25),
     sg.Slider(range=(1, 100), orientation='v', default_value=75),
     sg.Slider(range=(1, 100), orientation='v', default_value=10),
     sg.Column(column1, background_color='lightblue')]], ), sg.Stretch(), sg.Dial((1,100))],
    [sg.Text('_' * 50, justification='c')],
    [sg.Text('Choose A Folder')],
    [sg.Text('Your Folder'),
     sg.InputText('Default Folder', size=(300,22)), sg.FolderBrowse(), sg.Stretch()],
    [sg.Submit(tooltip='Click to submit this form',), sg.Cancel()]]

window = sg.Window('Everything bagel',
                   grab_anywhere=False,
                   font=('Helvetica', 12),
                   no_titlebar=False,
                   alpha_channel=1,
                   keep_on_top=False,
                   element_padding=(2,3),
                   default_element_size=(100, 23),
                   default_button_element_size=(120,30),
                   # background_image='C:\Python\PycharmProjects\GooeyGUI\logo500black.png',
                   ).Layout(layout)
event, values = window.Read()
print(event, values)
window.Close()

sg.Popup('Title',
         'The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values,)


