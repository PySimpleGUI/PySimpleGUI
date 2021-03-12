import PySimpleGUI as sg

"""
    Extending PySimpleGUI using the tkinter event bindings

    The idea here is to enable you to receive tkinter "Events" through the normal place you
    get your events, the window.read() call.

    Both elements and windows have a bind method.
    window.bind(tkinter_event_string, key)   or   element.bind(tkinter_event_string, key_modifier)
    First parameter is the tkinter event string.  These are things like <FocusIn> <Button-1> <Button-3> <Enter>
    Second parameter for windows is an entire key, for elements is something added onto a key.  This key or modified key is what is returned when you read the window.
    If the key modifier is text and the key is text, then the key returned from the read will be the 2 concatenated together.  Otherwise your event will be a tuple containing the key_modifier value you pass in and the key belonging to the element the event happened to.
    
    Copyright 2021 PySimpleGUI
"""
sg.theme('Dark Blue 3')

def main():
    layout = [  [sg.Text('Move mouse over me', key='-TEXT-')],
                [sg.In(key='-IN-')],
                [sg.Button('Right Click Me', key='-BUTTON-'), sg.Button('Right Click Me2', key=(2,3)),sg.Button('Exit'),]]

    window = sg.Window('Window Title', layout, finalize=True)

    window.bind('<FocusOut>', '+FOCUS OUT+')

    window['-BUTTON-'].bind('<Button-3>', '+RIGHT CLICK+')
    window[(2,3)].bind('<Button-3>', '+RIGHT CLICK+')
    window['-TEXT-'].bind('<Enter>', '+MOUSE OVER+')
    window['-TEXT-'].bind('<Leave>', '+MOUSE AWAY+')
    window['-IN-'].bind('<FocusIn>', '+INPUT FOCUS+')
    window.bind('<Enter>', '* WINDOW ENTER *')
    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close()


if __name__ == '__main__':
    main()