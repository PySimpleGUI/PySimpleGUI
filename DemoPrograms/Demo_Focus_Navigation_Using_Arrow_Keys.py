import PySimpleGUI as sg


"""
    Demo - Navigating a window's focus using arrow keys
    
    This Demo Program has 2 features of PySimpleGUI in use:
    1. Binding the arrow keys
    2. Navigating a window's elements using focus
    
    The first step is to bind the left, right and down arrows to an event.
    The call to window.bind will cause events to be generated when these keys are pressed
    
    The next step is to add the focus navigation to your event loop.
    When the right key is pressed, the focus moves to the element that should get focus next
    When the left arrow key is pressed, the focus moves to the previous element
    And when the down arrow is pressed the program exits


    Copyright 2022 PySimpleGUI
"""



def main():
    layout = [  [sg.Text('My Window')],
                [sg.Input(key='-IN-')],
                [sg.Input(key='-IN2-')],
                [sg.Input(key='-IN3-')],
                [sg.Input(key='-IN4-')],
                [sg.Input(key='-IN5-')],
                [sg.Input(key='-IN6-')],
                [sg.Input(key='-IN7-')],
                [sg.Button('Go'), sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, finalize=True)

    # Bind the Left, Right and Down arrow keys to events
    window.bind('<Right>', '-NEXT-')
    window.bind('<Left>', '-PREV-')
    window.bind('<Down>', 'Exit')

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        # Right arrow pressed, so move to the next element that should get focus
        if event == '-NEXT-':
            next_element = window.find_element_with_focus().get_next_focus()
            next_element.set_focus()

        # Left arrow pressed, so move to the previous element that should get focus
        if event == '-PREV-':
            prev_element = window.find_element_with_focus().get_previous_focus()
            prev_element.set_focus()
    window.close()

if __name__ == '__main__':
    main()
