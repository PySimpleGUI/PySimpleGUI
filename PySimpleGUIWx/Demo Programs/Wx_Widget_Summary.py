import PySimpleGUIWx as sg
import time

sg.ChangeLookAndFeel('GreenTan')
buttons =  [sg.Radio('Radio Button 1',1, size=(12,1), default=True, enable_events=True, tooltip='radio buttton', key='_RADIO1_'),
            sg.Radio('Radio Button 2',1, default=False, key='_RADIO2_', enable_events=True, visible=True),
            sg.Radio('Radio Button 3',1, enable_events=True, key='_RADIO3_')]

layout =  [ [sg.Text('PySimpleGUIWx ', tooltip='text', font='Arial 18', text_color='red', enable_events=True, key='_Wx_') ,
             sg.Text('', key='_TEXT_', font='Arial 18', text_color='black')],
            [sg.Input('Single Line Input', do_not_clear=True, enable_events=True)],
            [sg.Multiline('Multiline Input', do_not_clear=True, size=(40,4), enable_events=True)],
            [sg.MultilineOutput('Multiline Output', size=(40,5), text_color='blue')],
            [sg.Output(size=(40,5))],
            [sg.Checkbox('Checkbox 1', enable_events=True), sg.Checkbox('Checkbox 2', default=True, enable_events=True)],
           [sg.Column([buttons], visible=True, key='COL')],
            [sg.Combo(values=['Combo 1', 'Combo 2', 'Combo 3'], default_value='Combo 2', enable_events=True, key='_COMBO_', visible=True, readonly=False, tooltip='Combo box', disabled=False, font='Courier 18', size=(12,1))],
            [sg.OK(), sg.Button('Popup')]
          ]

window = sg.Window('My PySimpleGUIWx Window',
                   default_element_size=(12,1),
                   ).Layout(layout).Finalize()

print('This is the output element where STDOUT it being routed')
start_time = int(round(time.time() * 100))
while True:
    event, values = window.Read(timeout=None)
    if event is None:
        break
    if event != sg.TIMEOUT_KEY:
        print(event, values)
    if event == 'Popup':
        sg.Popup('Here is your popup')
    current_time = int(round(time.time() * 100)) - start_time

    window.FindElement('_TEXT_').Update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                  (current_time // 100) % 60,
                                                                  current_time % 100))
window.Close()




