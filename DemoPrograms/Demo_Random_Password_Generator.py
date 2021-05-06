Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@LP-Codes 
LP-Codes
/
Python-Random-Password-GUI
1
10
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
Python-Random-Password-GUI/PasswordGenerator.py /
Cannot retrieve contributors at this time
52 lines (44 sloc)  1.92 KB
  
import random
import string
# ! module allows us to copy and paste text to and from the clipboard to your computer
import pyperclip
import PySimpleGUI as sg

sg.theme("Darkbrown")
# Defining the window's contents
layout = [[sg.Text("Random Password Generator", font=("Helvetica", 25, "bold"))],
          [sg.Text("Select Password Length", key='-OUTPUT1-', font=("Helvetica", 10, "bold"))],
          [sg.Spin([i for i in range(1, 11)], initial_value=1,
                   size=(30, 4), key='-INPUT-')],
          #   [sg.Input(key='-INPUT-' "sd")],
          [sg.Text(size=(40, 1), key='-OUTPUT-', font=("Helvetica", 25, "bold"))],
          [sg.Button('Generate', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold")),
           sg.Button('Copy', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold")
                     # Defining the window's contents
                     ), sg.Button('Quit', border_width=5, pad=(25, 10), font=("Helvetica", 10, "bold"))]]

window = sg.Window('Lp Password Generator', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()

    if event == 'Generate':
        useript = values['-INPUT-']
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation
        all = lower + upper + num + symbols
        temp = random.sample(all, useript)
        password = "".join(temp)
        print(password)
        sg.popup(password)
        window['-OUTPUT-'].update(password)

        window["-INPUT-"].update("1")

    if event == "Copy":
        op = window['-OUTPUT-'].get()
        pyperclip.copy(op)
        # Output a message to the window
        sg.popup("Password is copied to your clipboard")

    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

# Finish up by removing from the screen
window.close()

