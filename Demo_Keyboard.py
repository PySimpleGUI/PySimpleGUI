import PySimpleGUI as sg

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"

with sg.FlexForm("Keyboard Test", return_keyboard_events=True, use_default_focus=False) as form:
    text_elem = sg.Text("", size=(18,1))
    layout = [[sg.Text("Press a key or scroll mouse")],
              [text_elem],
              [sg.SimpleButton("OK")]]

    form.Layout(layout)
    # ---===--- Loop taking in user input --- #
    while True:
        button, value = form.Read()

        if button == "OK" or (button is None and value is None):
            print(button, "exiting")
            break
        if len(button) == 1:
            text_elem.Update(new_value='%s - %s'%(button, ord(button)))
        if button is not None:
            text_elem.Update(button)


