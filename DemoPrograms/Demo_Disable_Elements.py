#!/usr/bin/env python
import PySimpleGUI as sg

'''
    Usage of Disable elements
'''

sg.theme('Dark')
sg.set_options(element_padding=(0, 0))

layout = [
    [ sg.Text('Notes:', pad=((3, 0), 0)),
      sg.Input(size=(44, 1), background_color='white', text_color='black', key='notes')],

    [ sg.Text('Output:', pad=((3, 0), 0)),
      sg.Text('', size=(44, 1), text_color='white', key='output')],

    [sg.CBox('Checkbox:', default=True,  pad=((3, 0), 0), disabled=True, key='cbox'),
      sg.Listbox((1, 2, 3, 4), size=(8, 3), disabled=True, key='listbox'),
      sg.Radio('Radio 1', default=True, group_id='1', disabled=True, key='radio1'), 
      sg.Radio('Radio 2', default=False,  group_id='1', disabled=True, key='radio2')],

    [sg.Spin((1, 2, 3, 4), 1, disabled=True, key='spin'), 
      sg.OptionMenu((1, 2, 3, 4), disabled=True, key='option'), 
      sg.Combo(values=(1, 2, 3, 4), disabled=True, key='combo')],

    [sg.ML('Multiline', size=(20, 3), disabled=True, key='multi')],

    [sg.Slider((1, 10), size=(20, 20), orientation='h', disabled=True, key='slider')],

    [sg.Button('Enable', button_color=('white', 'black')),
     sg.Button('Disable', button_color=('white', 'black')),
     sg.Button('Reset', button_color=('white', '#9B0023'), key='reset'),
     sg.Button('Values', button_color=('white', 'springgreen4')),
     sg.Button('Exit', disabled=True, button_color=('white', '#00406B'), key='exit')]]

window = sg.Window("Disable Elements Demo", layout,
      default_element_size=(12, 1),
      text_justification='r',
      auto_size_text=False,
      auto_size_buttons=False, 
      keep_on_top=True, 
      grab_anywhere=False,
      default_button_element_size=(12, 1), 
      finalize=True)

key_list = 'cbox', 'listbox', 'radio1', 'radio2', 'spin', 'option', 'combo', 'reset', 'notes', 'multi', 'slider', 'exit'

# don't do this kind of for-loop
for key in key_list:
    window[key].update(disabled=True)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'exit'):
        break
    elif event == 'Disable':
        for key in key_list:
            window[key].update(disabled=True)
    elif event == 'Enable':
        for key in key_list:
            window[key].update(disabled=False)
    elif event == 'Values':
        sg.popup(values, keep_on_top=True)

window.close()