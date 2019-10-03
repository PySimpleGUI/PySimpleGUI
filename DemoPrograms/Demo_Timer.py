import PySimpleGUI as sg
import time

# form that doen't block
# good for applications with an loop that polls hardware
def Timer():
    sg.ChangeLookAndFeel('Dark')
    sg.SetOptions(element_padding=(0,0))
    # Make a form, but don't use context manager
    window = sg.Window('Running Timer', no_titlebar=True, auto_size_buttons=False)
    # Create a text element that will be updated with status information on the GUI itself
    # Create the rows
    form_rows = [[sg.Text('')],
                 [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
                 [sg.Button('Pause', key='-RUN-PAUSE-'), sg.Button('Reset'), sg.Exit(button_color=('white','firebrick4'))]]
    # Layout the rows of the form and perform a read. Indicate the form is non-blocking!
    window.Layout(form_rows)
    #
    # your program's main loop
    i = 0
    paused = False
    start_time = int(round(time.time() * 100))
    while (True):
        # This is the code that reads and updates your window
        button, values = window.read(timeout=0)
        window.FindElement('text').Update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))

        if values is None or button == 'Exit':
            break

        if button == 'Reset':
            i=0
        elif button == '-RUN-PAUSE-':
            paused = not paused
            window['-RUN-PAUSE-'].Update('Run' if paused else 'Pause')

        if not paused:
            i += 1


    # Broke out of main loop. Close the window.
    window.close()

Timer()