import PySimpleGUI as sg
import time

"""
    
    Timer Desktop Widget
    Creates a floating timer that is always on top of other windows
    You move it by grabbing anywhere on the window
    Good example of how to do a non-blocking, polling program using PySimpleGUI
    
"""


# form that doen't block
# good for applications with an loop that polls hardware
def Timer():
    sg.ChangeLookAndFeel('Dark')
    sg.SetOptions(element_padding=(0,0))
    # Make a form, but don't use context manager
    form = sg.FlexForm('Running Timer', no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True)
    # Create a text element that will be updated with status information on the GUI itself
    # Create the rows
    form_rows = [[sg.Text('')],
                 [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
                 [sg.ReadFormButton('Pause', key='button'), sg.ReadFormButton('Reset'), sg.Exit(button_color=('white','firebrick4'))]]
    # Layout the rows of the form and perform a read. Indicate the form is non-blocking!
    form.Layout(form_rows)
    #
    # your program's main loop
    i = 0
    paused = False
    while (True):
        # This is the code that reads and updates your window
        button, values = form.ReadNonBlocking()
        #form.FindElement('text').Update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
        x = divmod(i, 100)
        y = divmod(x[0], 60)
        form.FindElement('text').Update('{:02d}:{:02d}.{:02d}'.format(y[0], y[1], x[1]))
        if values is None or button == 'Exit':
            break
        #print(button)
        if button is 'Reset':
            i=0
        elif button == 'Pause':
            paused = True
            element = form.FindElement('button')
            element.Update(new_text='Run')
        elif button == 'Run':
            paused = False
            element = form.FindElement('button')
            element.Update(new_text='Pause')

        if not paused:
            i += 1
        # Your code begins here
        time.sleep(.01)

    # Broke out of main loop. Close the window.
    form.CloseNonBlockingForm()

Timer()