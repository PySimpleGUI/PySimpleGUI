import PySimpleGUI as sg
import time

# form that doen't block
# good for applications with an loop that polls hardware
def Timer():
    sg.ChangeLookAndFeel('TealMono')
    # Make a form, but don't use context manager
    form = sg.FlexForm('Running Timer', auto_size_text=True)
    # Create a text element that will be updated with status information on the GUI itself
    # Create the rows
    form_rows = [[sg.Text('Stopwatch')],
                 [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
                 [sg.ReadFormButton('Pause/Resume'), sg.ReadFormButton('Reset')]]
    # Layout the rows of the form and perform a read. Indicate the form is non-blocking!
    form.LayoutAndRead(form_rows, non_blocking=True)

    #
    # Some place later in your code...
    # You need to perform a ReadNonBlocking on your form every now and then or
    # else it won't refresh.
    #
    # your program's main loop
    i = 0
    paused = False
    while (True):
        # This is the code that reads and updates your window
        form.FindElement('text').Update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
        button, values = form.ReadNonBlocking()

        if values is None:
            break

        if button is 'Reset':
            i=0
        elif button is 'Pause/Resume':
            paused = not paused

        if not paused:
            i += 1
        # Your code begins here
        time.sleep(.01)

    # Broke out of main loop. Close the window.
    form.CloseNonBlockingForm()

Timer()