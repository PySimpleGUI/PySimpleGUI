#!/usr/bin/env python
import PySimpleGUI as sg

'''
    Example of GUI
'''

def main():
    sg.theme('TanBlue')

    column1 = [
        [sg.Text('Column 1', background_color=sg.DEFAULT_BACKGROUND_COLOR,
              justification='center', size=(10, 1))],
        [sg.Spin(values=('Spin Box 1', '2', '3'),
                 initial_value='Spin Box 1', key='spin1')],
        [sg.Spin(values=('Spin Box 1', '2', '3'),
                 initial_value='Spin Box 2', key='spin2')],
        [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3', key='spin3')]]

    layout = [
        [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.InputText('This is my text', key='in1')],
        [sg.CBox('Checkbox', key='cb1'), sg.CBox(
            'My second checkbox!', key='cb2', default=True)],
        [sg.Radio('My first Radio!     ', "RADIO1", key='rad1', default=True),
         sg.Radio('My second Radio!', "RADIO1", key='rad2')],
        [sg.MLine(default_text='This is the default Text should you decide not to type anything', size=(35, 3),
                  key='multi1'),
         sg.MLine(default_text='A second multi-line', size=(35, 3), key='multi2')],
        [sg.Combo(('Combobox 1', 'Combobox 2'), key='combo', size=(20, 1)),
         sg.Slider(range=(1, 100), orientation='h', size=(34, 20), key='slide1', default_value=85)],
        [sg.OptionMenu(('Menu Option 1', 'Menu Option 2',
                         'Menu Option 3'), key='optionmenu')],
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3), key='listbox'),
         sg.Slider(range=(1, 100),
                    orientation='v',
                    size=(5, 20),
                    default_value=25, key='slide2', ),
         sg.Slider(range=(1, 100),
                    orientation='v',
                    size=(5, 20),
                    default_value=75, key='slide3', ),
         sg.Slider(range=(1, 100),
                    orientation='v',
                    size=(5, 20),
                    default_value=10, key='slide4'),
         sg.Col(column1, background_color='gray34')],
        [sg.Text('_' * 80)],
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), justification='right'),
         sg.InputText('Default Folder', key='folder'), sg.FolderBrowse()],
        [sg.Button('Exit'),
         sg.Text(' ' * 40), sg.Button('SaveSettings'), sg.Button('LoadSettings')]
    ]

    window = sg.Window('Form Fill Demonstration', layout, default_element_size=(40, 1), grab_anywhere=False)

    while True:
        event, values = window.read()

        if event == 'SaveSettings':
            filename = sg.popup_get_file('Save Settings', save_as=True, no_window=True)
            window.SaveToDisk(filename)
            # save(values)
        elif event == 'LoadSettings':
            filename = sg.popup_get_file('Load Settings', no_window=True)
            window.LoadFromDisk(filename)
            # load(form)
        elif event in ('Exit', None):
            break

    window.close()


if __name__ == '__main__':
    main()
