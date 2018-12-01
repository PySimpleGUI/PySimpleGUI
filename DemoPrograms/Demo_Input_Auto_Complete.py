import sys
import re
QT = True
if QT:
    import PySimpleGUIQt as sg
else:
    import PySimpleGUI as sg

def autocomplete_popup_show(text_list ):
    autocomplete_popup_layout = [[sg.Listbox(values=text_list,
                                             size=(100,20*len(text_list)) if QT else (15, len(text_list)),
                                             change_submits=True,
                                             bind_return_key=True,
                                             auto_size_text=True,
                                             key='_FLOATING_LISTBOX_', enable_events=True)]]

    autocomplete_popup = sg.Window("Borderless Window",
                                   default_element_size=(12, 1),
                                   auto_size_text=False,
                                   auto_size_buttons=False,
                                   no_titlebar=True,
                                   grab_anywhere=True,
                                   return_keyboard_events=True,
                                   keep_on_top=True,
                                   background_color='black',
                                   location=(1320,622),
                                   default_button_element_size=(12, 1))

    window = autocomplete_popup.Layout(autocomplete_popup_layout).Finalize()
    return window


def predict_text(input, lista):
    pattern = re.compile('.*' + input + '.*')
    return [w for w in lista if re.match(pattern, w)]

choices = ['ABC' + str(i) for i in range(30)]       # dummy data

layout = [  [sg.Text('Your typed chars appear here:')],
            [sg.In(key='_INPUT_', size=(10,1), do_not_clear=True)],
            [sg.Button('Show'), sg.Button('Exit')],]

window = sg.Window('Window Title', return_keyboard_events=True).Layout(layout)

sel_item = -1
skip_event = False
while True:             # Event Loop
    event, values = window.Read(timeout=500)
    if event is None or event == 'Exit':
        break
    if event != sg.TIMEOUT_KEY:
        # print(f'ev1 {event}')
        in_val = values['_INPUT_']
        prediction_list = predict_text(str(in_val), choices)
        if prediction_list:
            try:
                fwindow.Close()
            except: pass
            fwindow = autocomplete_popup_show(prediction_list)
            list_elem = fwindow.Element('_FLOATING_LISTBOX_')
        if event == '_COMBO_':
            sg.Popup('Chose', values['_COMBO_'])
        if event.startswith('Down') or event.startswith('special 16777237'):
            sel_item = sel_item + (sel_item<len(prediction_list))
            list_elem.Update(set_to_index=sel_item)
            skip_event = True
        elif event.startswith('Up') or event.startswith('special 16777235'):
            sel_item = sel_item - (sel_item>0)
            list_elem.Update(set_to_index=sel_item)
            skip_event = True
        if event == '\r' or event.startswith('special 16777220'):
            chosen = vals2['_FLOATING_LISTBOX_']
            window.Element('_INPUT_').Update(vals2['_FLOATING_LISTBOX_'][0], select=True)
            fwindow.Close()
            sel_item = -1
        if event.startswith('Escape') or event.startswith('special 16777216'):
            window.Element('_INPUT_').Update('')

    try:
        ev2, vals2 = fwindow.Read(timeout=10)
        if ev2 == '_FLOATING_LISTBOX_' and skip_event and QT:
            skip_event = False
        elif ev2 != sg.TIMEOUT_KEY and ev2 is not None:
            # print(f'ev2 {ev2}')
            fwindow.Close()
            window.Element('_INPUT_').Update(vals2['_FLOATING_LISTBOX_'][0], select=True)
            sel_item = -1
            fwindow = None
    except: pass
window.Close()
