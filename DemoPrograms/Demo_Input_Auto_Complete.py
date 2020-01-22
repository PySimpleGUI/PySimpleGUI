import PySimpleGUI as sg
import re

'''
    Demo of using a borderless window to show possible matches for autocomplete feature
'''

def autocomplete_popup_show(text_list):
    layout = [[ sg.Listbox(values=text_list,
                            size=(15, len(text_list)),
                            change_submits=True, bind_return_key=True,
                            key='-FLOATING-LISTBOX-', enable_events=True) ]]

    return sg.Window("Borderless Window",
                                   layout,
                                   default_element_size=(12, 1),
                                   auto_size_text=False, keep_on_top=True,
                                   no_titlebar=True, grab_anywhere=True,
                                   return_keyboard_events=True,
                                   auto_size_buttons=False,
                                   background_color='black',
                                   default_button_element_size=(12, 1),
                                   location=(1320, 622), finalize=True)


def predict_text(input, lista):
    pattern = re.compile('.*' + input + '.*')
    return [w for w in lista if re.match(pattern, w)]


def main():

    choices = ['ABC' + str(i) for i in range(30)]       # dummy data

    layout = [[sg.Text('Your typed chars appear here:')],
              [sg.Input(key='-INPUT-', size=(10, 1))],
              [sg.Button('Show'), sg.Button('Exit')], ]

    window = sg.Window('Autocomplete Demo', layout, return_keyboard_events=True)

    sel_item = -1
    fwindow = list_elem = values2 = None
    while True:             # Event Loop
        event, values = window.read(timeout=500)

        if event in (None, 'Exit'):
            break

        if event != sg.TIMEOUT_KEY:
            # print(f'event1 {event}')
            in_val = values['-INPUT-']
            prediction_list = predict_text(str(in_val), choices)
            if prediction_list:
                try:
                    fwindow.close()
                except:
                    pass
                fwindow = autocomplete_popup_show(prediction_list)
                list_elem = fwindow['-FLOATING-LISTBOX-']
            if event == '_COMBO_':
                sg.popup('Chose', values['_COMBO_'])

            if event.startswith('Down') or event.startswith('special 16777237'):
                sel_item = sel_item + (sel_item < len(prediction_list))
                list_elem.update(set_to_index=sel_item)

            elif event.startswith('Up') or event.startswith('special 16777235'):
                sel_item = sel_item - (sel_item > 0)
                list_elem.update(set_to_index=sel_item)

            if event == '\r' or event.startswith('special 16777220'):
                chosen = values2['-FLOATING-LISTBOX-'] if values2 is not None else None
                if chosen:
                    window['-INPUT-'].update(chosen[0], select=True)
                fwindow.close()
                sel_item = -1

            if event.startswith('Escape') or event.startswith('special 16777216'):
                window['-INPUT-'].update('')

        try:
            event2, values2 = fwindow.read(timeout=10)
            # if event2 == '-FLOATING-LISTBOX-' and skip_event and QT:
            #     skip_event = False
            if event2 != sg.TIMEOUT_KEY and event2 is not None:
                # print(f'event2 {event2}')
                fwindow.close()
                window['-INPUT-'].update(values2['-FLOATING-LISTBOX-']
                                         [0], select=True)
                sel_item = -1
                fwindow = None
        except:
            pass

    window.close()

if __name__ == '__main__':
    main()
