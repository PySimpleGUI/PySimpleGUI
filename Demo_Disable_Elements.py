import PySimpleGUI as sg

"""
Turn off padding in order to get a really tight looking layout.
"""

sg.ChangeLookAndFeel('Dark')
sg.SetOptions(element_padding=(0, 0))
layout = [
          [sg.T('Notes:', pad=((3, 0), 0)), sg.In(size=(44, 1), background_color='white', text_color='black', key='notes')],
          [sg.T('Output:', pad=((3, 0), 0)), sg.T('', size=(44, 1), text_color='white', key='output')],
          [sg.CBox('Checkbox:', default=True,  pad=((3, 0), 0), key='cbox'), sg.Listbox((1,2,3,4),size=(8,3),key='listbox'),
           sg.Radio('Radio 1', default=True, group_id='1', key='radio1'), sg.Radio('Radio 2', default=False,  group_id='1', key='radio2')],
          [sg.Spin((1,2,3,4),1, key='spin'), sg.OptionMenu((1,2,3,4), key='option'), sg.Combo(values=(1,2,3,4),key='combo')],
          [sg.Multiline('Multiline', size=(20,3), key='multi')],
          [sg.Slider((1,10), size=(20,20), orientation='h', key='slider')],
          [sg.ReadFormButton('Enable', button_color=('white', 'black')),
           sg.ReadFormButton('Disable', button_color=('white', 'black')),
           sg.ReadFormButton('Reset', button_color=('white', '#9B0023'), key='reset'),
           sg.ReadFormButton('Values', button_color=('white', 'springgreen4')),
           sg.SimpleButton('Exit', button_color=('white', '#00406B'))]]

form = sg.FlexForm("Time Tracker", default_element_size=(12, 1), text_justification='r', auto_size_text=False,
                   auto_size_buttons=False, keep_on_top=True, grab_anywhere=False,
                   default_button_element_size=(12, 1))

form.Layout(layout)

while True:
    button, values = form.Read()
    if button is None or button == 'Exit':
        break
    elif button == 'Disable':
        form.FindElement('cbox').Update(disabled=True)
        form.FindElement('listbox').Update(disabled=True)
        form.FindElement('radio1').Update(disabled=True)
        form.FindElement('radio2').Update(disabled=True)
        form.FindElement('spin').Update(disabled=True)
        form.FindElement('option').Update(disabled=True)
        form.FindElement('combo').Update(disabled=True)
        form.FindElement('reset').Update(disabled=True)
        form.FindElement('notes').Update(disabled=True)
        form.FindElement('multi').Update(disabled=True)
        form.FindElement('slider').Update(disabled=True)
    elif button == 'Enable':
        form.FindElement('cbox').Update(disabled=False)
        form.FindElement('listbox').Update(disabled=False)
        form.FindElement('radio1').Update(disabled=False)
        form.FindElement('radio2').Update(disabled=False)
        form.FindElement('spin').Update(disabled=False)
        form.FindElement('option').Update(disabled=False)
        form.FindElement('combo').Update(disabled=False)
        form.FindElement('reset').Update(disabled=False)
        form.FindElement('notes').Update(disabled=False)
        form.FindElement('multi').Update(disabled=False)
        form.FindElement('slider').Update(disabled=False)
    elif button == 'Values':
        sg.Popup(values, keep_on_top=True)



