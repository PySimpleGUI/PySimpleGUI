import PySimpleGUI as sg

# This design pattern simulates button callbacks
# Note that callbacks are NOT a part of the package's interface to the
# caller intentionally.  The underlying implementation actually does use
# tkinter callbacks.  They are simply hidden from the user.

# The callback functions
def button1():
    print('Button 1 callback')

def button2():
    print('Button 2 callback')

# Create a standard form
form = sg.FlexForm('Button callback example')
# Layout the design of the GUI
layout = [[sg.Text('Please click a button', auto_size_text=True)],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.Quit()]]
# Show the form to the user
form.Layout(layout)

# Event loop. Read buttons, make callbacks
while True:
    # Read the form
    button, value = form.Read()
    # Take appropriate action based on button
    if button == '1':
        button1()
    elif button == '2':
        button2()
    elif button =='Quit' or button is None:
        break

# All done!
sg.PopupOK('Done')
