import PySimpleGUI as sg

with sg.FlexForm("Realtime Keyboard Test", return_keyboard_events=True, use_default_focus=False) as form:
    layout = [[sg.Text("Hold down a key")],
              [sg.SimpleButton("OK")]]

    form.Layout(layout)

    while True:
        button, value = form.ReadNonBlocking()

        if button == "OK":
            print(button, value, "exiting")
            break
        if button is not None:
            if len(button) == 1:
                print('%s - %s'%(button, ord(button)))
            else:
                print(button)
        elif value is None:
            break
