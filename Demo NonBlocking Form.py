import PySimpleGUI as sg
import time

def main():
    StatusOutputExample()

# form that doen't block
def StatusOutputExample_context_manager():
    with sg.FlexForm('Running Timer', auto_size_text=True) as form:
        output_element = sg.Text('', size=(8, 2), font=('Helvetica', 20))
        form_rows = [[sg.Text('Non-blocking GUI with updates')],
                     [output_element],
                     [sg.SimpleButton('Quit')]]

        form.LayoutAndRead(form_rows, non_blocking=True)

        for i in range(1, 1000):
            output_element.Update('{:02d}:{:02d}.{:02d}'.format(*divmod(int(i/100), 60), i%100))
            button, values = form.ReadNonBlocking()
            if values is None or button == 'Quit':
                break
            time.sleep(.01)
        else:
            form.CloseNonBlockingForm()


# form that doen't block
def StatusOutputExample():
    # Make a form, but don't use context manager
    form = sg.FlexForm('Running Timer', auto_size_text=True)
    # Create a text element that will be updated with status information on the GUI itself
    output_element = sg.Text('', size=(8, 2), font=('Helvetica', 20))
    # Create the rows
    form_rows = [[sg.Text('Non-blocking GUI with updates')],
                 [output_element],
                 [sg.SimpleButton('Quit')]]
    # Layout the rows of the form and perform a read. Indicate the form is non-blocking!
    form.LayoutAndRead(form_rows, non_blocking=True)

    #
    # Some place later in your code...
    # You need to perform a ReadNonBlocking on your form every now and then or
    # else it won't refresh
    #

    for i in range(1, 1000):
        output_element.Update('{:02d}:{:02d}.{:02d}'.format(*divmod(int(i / 100), 60), i % 100))
        button, values = form.ReadNonBlocking()
        if values is None or button == 'Quit':
            break
        time.sleep(.01)
    else:
        form.CloseNonBlockingForm()



if __name__ == '__main__':

    main()
