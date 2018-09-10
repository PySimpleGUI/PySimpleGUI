import PySimpleGUI as sg

"""
    Demonstration of MENUS!
    How do menus work?  Like buttons is how.
    Check out the variable menu_def for a hint on how to 
    define menus
"""
def TestMenus():
    import PySimpleGUI as sg

    sg.ChangeLookAndFeel('LightGreen')
    sg.SetOptions(element_padding=(0, 0))

    menu_def = [['File', ['Open', 'Save',]],
                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                ['Help', 'About...'],]

    layout = [
            [sg.Menu(menu_def)],
              [sg.Output(size=(60,20))]
              ]

    form = sg.FlexForm("Windows-like program", default_element_size=(12, 1), auto_size_text=False, auto_size_buttons=False,
                       default_button_element_size=(12, 1))
    form.Layout(layout)
    form.ReadNonBlocking()          # so the print message will show up... yes, a kludge

    print('Give those menus a try!')
    while True:
        button, values = form.Read()
        if button is None or button == 'Exit':
            return
        print('Button = ', button)
        if button == 'About...':
            sg.Popup('About this program','Version 1.0', 'PySimpleGUI rocks...')
        elif button == 'Open':
            filename = sg.PopupGetFile('file to open', no_window=True)
            print(filename)


TestMenus()