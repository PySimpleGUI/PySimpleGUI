import PySimpleGUI_Qt as sg
# sg.Popup('test 1')
# sg.Popup('test 2')
sg.ChangeLookAndFeel('GreenTan')
layout = [
        [sg.Text('Hello From PySimpleGUI_Qt!', text_color='red', tooltip='This is my tooltip', justification='c', font=('Courier', 22), key='_TEXT_')],
        [sg.Text('Input something here'),sg.Stretch(), sg.Input('This is an InputText Element', key='_INPUT_', font=('Any', 14))],
        [sg.Text('This is the new Dial Element'), sg.Dial(background_color='red'), sg.Stretch()],
        [sg.Combo(['Combo 1', 'Combo 2', 'Combo 3'], key='+COMBO+', size=(150,30), text_color='green')],
        [sg.Listbox(['Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'], key='+LIST+', size=(200,150), text_color='blue'),sg.Slider((1,100), orientation='v', key='+SLIDER 1+')],
        [sg.Slider((1,10), size=(200,30), orientation='h', key='+SLIDER 2+'), sg.Stretch()],
        [sg.Checkbox('Checkbox 1', key='+CB1+'), sg.Checkbox('Checkbox 2', key='+CB2')],
        [sg.Checkbox('Checkbox 3'), sg.Checkbox('Checkbox 4')],
        [sg.Radio('Radio1', group_id=1),sg.Radio('Radio2', group_id=1)],
        [sg.Spin((5,8), size=(100,30))],
        [sg.Multiline('This is a Multiline Element', key='+MULTI+')],
        [sg.Button('My Button', size=(120,30)), sg.Exit(), sg.Button('Change', key='_CHANGE_')],
          ]

window = sg.Window('My first QT Window', auto_size_text=True, auto_size_buttons=False,  font=('Helvetica', 16)).Layout(layout)

while True:
    event, values = window.Read()
    print(event, values)
    if event is None or event == 'Exit':
        break

    window.FindElement('_TEXT_').Update(values['_INPUT_'], font=('Helvetica', 30))
    if event == '_CHANGE_':
        window.FindElement('_CHANGE_').Update('Disabled', disabled=True, button_color=('gray', 'gray20'),)
