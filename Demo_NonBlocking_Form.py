import PySimpleGUI as sg
import time




# form that doen't block
# good for applications with an loop that polls hardware
def StatusOutputExample():
    # Make a form, but don't use context manager
    form = sg.FlexForm('Running Timer', auto_size_text=True)
    # Create a text element that will be updated with status information on the GUI itself
    output_element = sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center')
    # Create the rows
    form_rows = [[sg.Text('Non-blocking GUI with updates')],
                 [output_element],
                 [sg.ReadFormButton('LED On'), sg.ReadFormButton('LED Off'), sg.ReadFormButton('Quit')]]
    # Layout the rows of the form and perform a read. Indicate the form is non-blocking!
    form.LayoutAndRead(form_rows, non_blocking=True)

    #
    # Some place later in your code...
    # You need to perform a ReadNonBlocking on your form every now and then or
    # else it won't refresh.
    #
    # your program's main loop
    i=0
    while (True):
        # This is the code that reads and updates your window
        output_element.Update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
        button, values = form.ReadNonBlocking()
        if button == 'Quit' or values is None:
            break
        if button == 'LED On':
            print('Turning on the LED')
        elif button == 'LED Off':
            print('Turning off the LED')

        i += 1
        # Your code begins here
        time.sleep(.01)

    # Broke out of main loop. Close the window.
    form.CloseNonBlockingForm()



# This design pattern follows the uses a context manager to better control the resources
# It may not be realistic to use a context manager within an embedded (Pi) environment
# If on a Pi, then consider the above design patterns instead
def StatusOutputExample_context_manager():
    with sg.FlexForm('Running Timer', auto_size_text=True) as form:
        output_element = sg.Text('', size=(8, 2), font=('Helvetica', 20))
        form_rows = [[sg.Text('Non-blocking GUI with updates')],
                     [output_element],
                     [sg.SimpleButton('Quit')]]

        form.LayoutAndRead(form_rows, non_blocking=True)

        for i in range(1, 1000):
            output_element.Update('{:02d}:{:02d}.{:02d}'.format((i // 100) // 60, (i // 100) % 60, i % 100))
            button, values = form.ReadNonBlocking()
            if values is None or button == 'Quit':
                break
            time.sleep(.01)
        else:
            form.CloseNonBlockingForm()

def main():
    StatusOutputExample()
    sg.MsgBox('End of non-blocking demonstration')
    # StatusOutputExample_context_manager()


if __name__ == '__main__':

    main()
