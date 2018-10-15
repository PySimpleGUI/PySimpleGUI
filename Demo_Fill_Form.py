#!/usr/bin/env python
import sys
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

def Everything():
    sg.ChangeLookAndFeel('TanBlue')

    column1 = [
        [sg.Text('Column 1', background_color=sg.DEFAULT_BACKGROUND_COLOR, justification='center', size=(10, 1))],
        [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1', key='spin1')],
        [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2', key='spin2')],
        [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3', key='spin3')]]

    layout = [
        [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.InputText('This is my text', key='in1', do_not_clear=True)],
        [sg.Checkbox('Checkbox', key='cb1'), sg.Checkbox('My second checkbox!', key='cb2', default=True)],
        [sg.Radio('My first Radio!     ', "RADIO1", key='rad1', default=True),
         sg.Radio('My second Radio!', "RADIO1", key='rad2')],
        [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3),
                      key='multi1', do_not_clear=True),
         sg.Multiline(default_text='A second multi-line', size=(35, 3), key='multi2', do_not_clear=True)],
        [sg.InputCombo(('Combobox 1', 'Combobox 2'), key='combo', size=(20, 1)),
         sg.Slider(range=(1, 100), orientation='h', size=(34, 20), key='slide1', default_value=85)],
        [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'), key='optionmenu')],
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3), key='listbox'),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, key='slide2', ),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75, key='slide3', ),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10, key='slide4'),
         sg.Column(column1, background_color='gray34')],
        [sg.Text('_' * 80)],
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
         sg.InputText('Default Folder', key='folder', do_not_clear=True), sg.FolderBrowse()],
        [sg.ReadButton('Exit'),
         sg.Text(' ' * 40), sg.ReadButton('SaveSettings'), sg.ReadButton('LoadSettings')]
    ]

    window = sg.Window('Form Fill Demonstration', default_element_size=(40, 1), grab_anywhere=False)
    # button, values = window.LayoutAndRead(layout, non_blocking=True)
    window.Layout(layout)

    while True:
        event, values = window.Read()

        if event is 'SaveSettings':
            filename = sg.PopupGetFile('Save Settings', save_as=True, no_window=True)
            window.SaveToDisk(filename)
            # save(values)
        elif event is 'LoadSettings':
            filename = sg.PopupGetFile('Load Settings', no_window=True)
            window.LoadFromDisk(filename)
            # load(form)
        elif event in ['Exit', None]:
            break

    # window.CloseNonBlocking()


if __name__ == '__main__':
    Everything()
