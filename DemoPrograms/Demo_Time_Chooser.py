import PySimpleGUI as sg

"""
    Demo Time Chooser

    A sample window for choosing a time.

    This particular implementation uses a Spin element.  Numerous possibilities exist for entering a time of day.  Instead
    of Spin elements, Input or Combo Elements could be used.

    If you do not want your user to be able to manually enter values using the keyboard, then set readonly=True in
    the Spin elements.

    Copyright 2023 PySimpleGUI
"""



def popup_get_time(title='Time Entry', starting_hour=1, starting_minute=0, allow_manual_input=True, font=None):
    """
    Shows a window that will gather a time of day.

    :param title:               The title that is shown on the window
    :type title:                str
    :param starting_hour:       Value to initially show in the hour field
    :type starting_hour:        int
    :param starting_minute:     Value to initially show in the minute field
    :type starting_minute:      int
    :param allow_manual_input:  If True, then the Spin elements can be manually edited
    :type allow_manual_input:   bool
    :param font:                Font to use for the window
    :type font:                 str | tuple
    :return:                    Tuple with format: (hour, minute, am-pm string)
    :type:                      (int, int, str)
    """

    max_value_dict = {'-HOUR-':(1, 12), '-MIN-':(0, 59)}
    hour_list = [i for i in range(0, 15)]
    minute_list = [i for i in range(-1, 62)]

    layout = [[sg.Spin(hour_list, initial_value=starting_hour, key='-HOUR-', s=3, enable_events=True, readonly=not allow_manual_input),
               sg.Text(':'),
               sg.Spin(minute_list, initial_value=starting_minute, key='-MIN-', s=3, enable_events=True, readonly=not allow_manual_input),
               sg.Combo(['AM', 'PM'], 'AM', readonly=True, key='-AMPM-')],
              [sg.Button('Ok'), sg.Button('Cancel')]]

    window = sg.Window(title, layout, font=font)

    while True:
        event, values = window.read()
        # print(event, values)
        if event == sg.WIN_CLOSED or event == 'Cancel':
            hours = minutes = ampm = None
            break

        if event == '-HOUR-' or event == '-MIN-':
            spin_value = values[event]
            if spin_value > max_value_dict[event][1]:
                values[event] =  max_value_dict[event][0]
                window[event].update(values[event])
            elif spin_value < max_value_dict[event][0]:
                values[event] =  max_value_dict[event][1]
                window[event].update(values[event])
        if event == 'Ok':
            # Do validation on the input values to ensure they're valid
            try:
                hours = int(values["-HOUR-"])
                minutes =  int(values["-MIN-"])
                ampm = values["-AMPM-"]
            except:
                continue        # if not valid, then don't allow exiting the window using OK.
            if  1 <= hours <= 12 and 0 <= minutes < 60:     # make sure the hour and minute values are in a valid range
                break

    window.close()

    return hours, minutes, ampm

print(popup_get_time(font='_ 15'))