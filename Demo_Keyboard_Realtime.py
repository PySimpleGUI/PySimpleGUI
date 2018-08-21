import PySimpleGUI as sg

# Recipe for getting a continuous stream of keys when using a non-blocking form
# If want to use the space bar, then be sure and disable the "default focus"

with sg.FlexForm('Realtime Keyboard Test', return_keyboard_events=True, use_default_focus=False) as form:
    layout = [[sg.Text('Hold down a key')],
              [sg.SimpleButton('OK')]]

    form.Layout(layout)
    # ---===--- Loop taking in user input --- #
    while True:
        button, value = form.ReadNonBlocking()

        if button == 'OK':
            print(button, value, 'exiting')
            break
        if button is not None:
            print(button)
        elif value is None:
            break


