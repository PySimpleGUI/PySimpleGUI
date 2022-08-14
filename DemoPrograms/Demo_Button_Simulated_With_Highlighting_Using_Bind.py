import PySimpleGUI as sg

"""
    Demo Program - Simulated Buttons with Mouseover Highlights

    The purpose of this demo is to teach you 5 unique PySimpleGUI constructs that when combined
    create a "Button" that highlights on mouseover regarless of the Operating System.
    Because of how tktiner works, mouseover highlighting is inconsistent across operating systems for Buttons.
    This is one (dare I say "clever") way to get this effect in your program

    1. Binding the Enter and Leave tkinter events
    2. Using Tuples as keys
    3. Using List Comprehensions to build a layout
    4. Using Text Elements to Simulate Buttons
    5. Using a "User Defined Element" to make what appears to be a new type of Button in the layout

    The KEY to making this work simply is these "Buttons" have a tuple as a key.
        The format of the key is ('-B-', button_text)

    An element's bind method will make a tuple if the original key is a tuple.
        (('-B-', button_text), 'ENTER') will be the event when the mouse is moved over the "Button"

    Copyright 2022 PySimpleGUI.org
"""

# sg.theme('dark red')

def TextButton(text):
    """
    A User Defined Element.  It looks like a Button, but is a Text element
    :param text:    The text that will be put on the "Button"
    :return:        A Text element with a tuple as the key
    """
    return sg.Text(text, key=('-B-', text), relief='raised', enable_events=True, font='_ 15',text_color=sg.theme_button_color_text(), background_color=sg.theme_button_color_background())

def do_binds(window, button_text):
    """
    This is magic code that enables the mouseover highlighting to work.
    """
    for btext in button_text:
        window[('-B-', btext)].bind('<Enter>', 'ENTER')
        window[('-B-', btext)].bind('<Leave>', 'EXIT')

def main():
    # Defines the text on the 3 buttons we're making
    button_text = ('Button 1', 'Button 2', 'Button 3')

    # The window's layout
    layout = [[TextButton(text) for text in button_text],
              [sg.Text(font='_ 14', k='-STATUS-')],
              [sg.Ok(), sg.Exit()]]

    window = sg.Window('Custom Mouseover Highlighting Buttons', layout, finalize=True)

    # After the window is finalized, then can perform the bindings
    do_binds(window, button_text)

    # The Event Looop
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        # if the event is a tuple, it's one of our TextButtons
        if isinstance(event, tuple):
            # if second item is one of the bound strings, then do the mouseeover code
            if event[1] in ('ENTER', 'EXIT'):
                button_key = event[0]
                if event[1] == 'ENTER':
                    window[button_key].update(text_color=sg.theme_button_color_background(), background_color=sg.theme_button_color_text())
                if event[1] == 'EXIT':
                    window[button_key].update(text_color=sg.theme_button_color_text(), background_color=sg.theme_button_color_background())
            else:   # a "normal" button click (Text clicked) so print the text which we put into the tuple
                window['-STATUS-'].update(f'Button pressed = {event[1]}')
    window.close()


if __name__ == '__main__':
    main()