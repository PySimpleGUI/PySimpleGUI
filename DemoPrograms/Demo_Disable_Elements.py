#!/usr/bin/env python
import sys
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

sg.ChangeLookAndFeel('Dark')
sg.SetOptions(element_padding=(0, 0))

layout = [
          [sg.T('Notes:', pad=((3, 0), 0)), sg.In(size=(44, 1), background_color='white', text_color='black', key='notes')],
          [sg.T('Output:', pad=((3, 0), 0)), sg.T('', size=(44, 1), text_color='white', key='output')],
          [sg.CBox('Checkbox:', default=True,  pad=((3, 0), 0), disabled=True, key='cbox'), sg.Listbox((1,2,3,4),size=(8,3),disabled=True, key='listbox'),
           sg.Radio('Radio 1', default=True, group_id='1', disabled=True, key='radio1'), sg.Radio('Radio 2', default=False,  group_id='1', disabled=True, key='radio2')],
          [sg.Spin((1,2,3,4),1,disabled=True, key='spin'), sg.OptionMenu((1,2,3,4),disabled=True, key='option'), sg.Combo(values=(1,2,3,4),disabled=True,key='combo')],
          [sg.Multiline('Multiline', size=(20,3),disabled=True, key='multi')],
          [sg.Slider((1,10), size=(20,20), orientation='h', disabled=True, key='slider')],
          [sg.ReadButton('Enable', button_color=('white', 'black')),
           sg.ReadButton('Disable', button_color=('white', 'black')),
           sg.ReadButton('Reset', button_color=('white', '#9B0023'), key='reset'),
           sg.ReadButton('Values', button_color=('white', 'springgreen4')),
           sg.Button('Exit', disabled=True, button_color=('white', '#00406B'), key='exit')]]

window = sg.Window("Disable Elements Demo", default_element_size=(12, 1), text_justification='r', auto_size_text=False,
                   auto_size_buttons=False, keep_on_top=True, grab_anywhere=False,
                   default_button_element_size=(12, 1)).Layout(layout).Finalize()

key_list = 'cbox', 'listbox', 'radio1', 'radio2', 'spin', 'option', 'combo', 'reset', 'notes', 'multi', 'slider', 'exit'

for key in key_list: window.FindElement(key).Update(disabled=True)    # don't do this kind of for-loop

while True:
    event, values = window.Read()
    if event in (None, 'exit'):
        break
    elif event == 'Disable':
        for key in key_list: window.FindElement(key).Update(disabled=True)
    elif event == 'Enable':
        for key in key_list: window.FindElement(key).Update(disabled=False)
    elif event == 'Values':
        sg.Popup(values, keep_on_top=True)

sys.exit(0)
