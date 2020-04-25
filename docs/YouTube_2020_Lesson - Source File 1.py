import PySimpleGUI as sg
import os
import time
import random




#  8888888b.            .d8888b.  888
#  888   Y88b          d88P  Y88b 888
#  888    888          888    888 888
#  888   d88P 888  888 888        88888b.   8888b.  888d888 88888b.d88b.
#  8888888P"  888  888 888        888 "88b     "88b 888P"   888 "888 "88b
#  888        888  888 888    888 888  888 .d888888 888     888  888  888
#  888        Y88b 888 Y88b  d88P 888  888 888  888 888     888  888  888
#  888         "Y88888  "Y8888P"  888  888 "Y888888 888     888  888  888
#                  888
#             Y8b d88P
#              "Y88P"

# Modify your color scheme.  For me, comments are super-important
# and standout like a high-lighter

def test(x,y):      # Note how "y" is grayed out
    return x




#  8888888b.
#  888   Y88b
#  888    888
#  888   d88P .d88b.  88888b.  888  888 88888b.  .d8888b
#  8888888P" d88""88b 888 "88b 888  888 888 "88b 88K
#  888       888  888 888  888 888  888 888  888 "Y8888b.
#  888       Y88..88P 888 d88P Y88b 888 888 d88P      X88
#  888        "Y88P"  88888P"   "Y88888 88888P"   88888P'
#                     888               888
#                     888               888
#                     888               888

var = (1,2,3,4)

sg.popup('This is a basic popup', 'I can have multiple item arguments', var)

while True:
    text = sg.popup_get_text('Enter "exit" to exit')
    if text == 'exit':
        break
    sg.popup('You entered:', text)

sg.popup_auto_close('Closing the program', background_color='red', text_color='white')
exit()



#   d888         888      d8b                        888b     d888          888
#  d8888         888      Y8P                        8888b   d8888          888
#    888         888                                 88888b.d88888          888
#    888         888      888 88888b.   .d88b.       888Y88888P888  .d88b.  888888 .d88b.  888d888
#    888         888      888 888 "88b d8P  Y8b      888 Y888P 888 d8P  Y8b 888   d8P  Y8b 888P"
#    888  888888 888      888 888  888 88888888      888  Y8P  888 88888888 888   88888888 888
#    888         888      888 888  888 Y8b.          888   "   888 Y8b.     Y88b. Y8b.     888
#  8888888       88888888 888 888  888  "Y8888       888       888  "Y8888   "Y888 "Y8888  888


for i in range(1000):
    sg.one_line_progress_meter('My meter', i+1, 1000, 'key', 'Message 1', 'Message 2')


for i in range(1000):
    if not sg.one_line_progress_meter('My meter', i+1, 1000, 'key', 'Message 1', 'Message 2'):
        sg.popup('ABORTED')
        break

exit()

#  8888888888                       888         8888888888               888
#  888                              888         888                      888
#  888                              888         888                      888
#  8888888 888d888 .d88b.  88888b.  888888      8888888    88888b.   .d88888
#  888     888P"  d88""88b 888 "88b 888         888        888 "88b d88" 888
#  888     888    888  888 888  888 888         888        888  888 888  888
#  888     888    Y88..88P 888  888 Y88b.       888        888  888 Y88b 888
#  888     888     "Y88P"  888  888  "Y888      8888888888 888  888  "Y88888

# A typical command line program often has a hardcoded path with a comment

my_path = r'c:\Python'          # If you want to use a different folder, change this variable

files = os.listdir(my_path)
print('\n'.join(files))


exit()

# Add popup_get_folder
# Change print to Print + Popup to stop from exiting




#  888888888        .d8888b.                    888    d8b
#  888             d88P  Y88b                   888    Y8P
#  888             Y88b.                        888
#  8888888b.        "Y888b.    .d88b.   .d8888b 888888 888  .d88b.  88888b.  .d8888b
#       "Y88b          "Y88b. d8P  Y8b d88P"    888    888 d88""88b 888 "88b 88K
#         888            "888 88888888 888      888    888 888  888 888  888 "Y8888b.
#  Y88b  d88P      Y88b  d88P Y8b.     Y88b.    Y88b.  888 Y88..88P 888  888      X88
#   "Y8888P"        "Y8888P"   "Y8888   "Y8888P  "Y888 888  "Y88P"  888  888  88888P'


# 1 - The import
import PySimpleGUI as sg

# 2 - Layout definition
layout = [[sg.Text('My layout')],
          [sg.Input(key='-INPUT-')],
          [sg.Button('OK'), sg.Button('Cancel')]]

# 3 - Create window
window = sg.Window('Design Pattern 3 - Persistent Window', layout)

# 4 - Event Loop
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Cancel'):
        break

# 5 - Close window
window.close()




#   .d88888b.                          .d8888b.  888               888
#  d88P" "Y88b                        d88P  Y88b 888               888
#  888     888                        Y88b.      888               888
#  888     888 88888b.   .d88b.        "Y888b.   88888b.   .d88b.  888888
#  888     888 888 "88b d8P  Y8b          "Y88b. 888 "88b d88""88b 888
#  888     888 888  888 88888888            "888 888  888 888  888 888
#  Y88b. .d88P 888  888 Y8b.          Y88b  d88P 888  888 Y88..88P Y88b.
#   "Y88888P"  888  888  "Y8888        "Y8888P"  888  888  "Y88P"   "Y888


layout = [[sg.Text('Name:'), sg.Input(key='-NAME-')],
          [sg.Text('Favorite Color:'), sg.Combo(['Red', 'Blue', 'Green', 'Purple'], key='-COLOR-')],
          [sg.Button('Ok')]]

event, values = sg.Window('One shot', layout).read(close=True)

sg.popup(event, values)

exit()

# Add bind return key
# Turn into single-line solution


#  888     888               888          888    d8b
#  888     888               888          888    Y8P
#  888     888               888          888
#  888     888 88888b.   .d88888  8888b.  888888 888 88888b.   .d88b.
#  888     888 888 "88b d88" 888     "88b 888    888 888 "88b d88P"88b
#  888     888 888  888 888  888 .d888888 888    888 888  888 888  888
#  Y88b. .d88P 888 d88P Y88b 888 888  888 Y88b.  888 888  888 Y88b 888
#   "Y88888P"  88888P"   "Y88888 "Y888888  "Y888 888 888  888  "Y88888
#              888                                                 888
#              888                                            Y8b d88P
#              888                                             "Y88P"


# 1 - The import
import PySimpleGUI as sg

# 2 - Layout definition
layout = [[sg.Text('My layout')],
          [sg.Input(key='-IN-')],
          [sg.Text('You entered:'), sg.Text(size=(20,1), key='-OUT-')],
          [sg.Button('OK'), sg.Button('Cancel')]]

# 3 - Create window
window = sg.Window('Update window with input value', layout)

# 4 - Event Loop
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Cancel'):
        break
    window['-OUT-'].update(values['-IN-'])
# 5 - Close window
window.close()

exit()



#  88888888888                                888
#      888                                    888
#      888                                    888
#      888   8888b.  888d888 .d88b.   .d88b.  888888 .d8888b
#      888      "88b 888P"  d88P"88b d8P  Y8b 888    88K
#      888  .d888888 888    888  888 88888888 888    "Y8888b.
#      888  888  888 888    Y88b 888 Y8b.     Y88b.       X88
#      888  "Y888888 888     "Y88888  "Y8888   "Y888  88888P'
#                                888
#                           Y8b d88P
#                            "Y88P"


layout = [  [sg.Text('Choose a file/Folder')],
            [sg.Text('Choose output folder'), sg.FolderBrowse(target='-IN3-')],
            [sg.Input(key='-IN-'), sg.FileBrowse()],
            [sg.Input(key='-IN2-', visible=False), sg.FileBrowse()],
            [sg.Input(key='-IN3-')],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
window.close()

# Enable events




#  888888b.                              888    d8b  .d888          888
#  888  "88b                             888    Y8P d88P"           888
#  888  .88P                             888        888             888
#  8888888K.   .d88b.   8888b.  888  888 888888 888 888888 888  888 888
#  888  "Y88b d8P  Y8b     "88b 888  888 888    888 888    888  888 888
#  888    888 88888888 .d888888 888  888 888    888 888    888  888 888
#  888   d88P Y8b.     888  888 Y88b 888 Y88b.  888 888    Y88b 888 888
#  8888888P"   "Y8888  "Y888888  "Y88888  "Y888 888 888     "Y88888 888
#
#
#
#  888       888 d8b               888
#  888   o   888 Y8P               888
#  888  d8b  888                   888
#  888 d888b 888 888 88888b.   .d88888  .d88b.  888  888  888 .d8888b
#  888d88888b888 888 888 "88b d88" 888 d88""88b 888  888  888 88K
#  88888P Y88888 888 888  888 888  888 888  888 888  888  888 "Y8888b.
#  8888P   Y8888 888 888  888 Y88b 888 Y88..88P Y88b 888 d88P      X88
#  888P     Y888 888 888  888  "Y88888  "Y88P"   "Y8888888P"   88888P'

exit_button = b'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'

layout = [  [sg.Text('My Window')],
            [sg.Button('Go'),
             sg.Button(image_data=exit_button, border_width=0,
                       button_color=(sg.theme_background_color(), sg.theme_background_color()),
                       key='Exit')]]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
window.close()

# no titlebar, grab anywhere, alpht .8, black
exit()





#   .d8888b.           888
#  d88P  Y88b          888
#  888    888          888
#  888         .d88b.  888 888  888 88888b.d88b.  88888b.  .d8888b
#  888        d88""88b 888 888  888 888 "888 "88b 888 "88b 88K
#  888    888 888  888 888 888  888 888  888  888 888  888 "Y8888b.
#  Y88b  d88P Y88..88P 888 Y88b 888 888  888  888 888  888      X88
#   "Y8888P"   "Y88P"  888  "Y88888 888  888  888 888  888  88888P'


# Problem - How to get multiple rows next to an element that consumes multiple rows?

layout = [  [sg.Listbox(list(range(10)), size=(10,5), key='-LBOX-')],
            [sg.T('Name'), sg.In()],
            [sg.T('Address'), sg.In()],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout,auto_size_text=False, default_element_size=(12,1))

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
window.close()

exit()



#  8888888888 888                                          888
#  888        888                                          888
#  888        888                                          888
#  8888888    888  .d88b.  88888b.d88b.   .d88b.  88888b.  888888 .d8888b
#  888        888 d8P  Y8b 888 "888 "88b d8P  Y8b 888 "88b 888    88K
#  888        888 88888888 888  888  888 88888888 888  888 888    "Y8888b.
#  888        888 Y8b.     888  888  888 Y8b.     888  888 Y88b.       X88
#  8888888888 888  "Y8888  888  888  888  "Y8888  888  888  "Y888  88888P'


import PySimpleGUI as sg


sg.theme('Dark Red')

# ------ Menu Definition ------ #
menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
            ['&Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],
            ['&Help', '&About...'], ]

# ------ Column Definition ------ #
column1 = [[sg.Text('Column 1', justification='center', size=(10, 1))],
           [sg.Spin(values=('Spin Box 1', 'Spin Box 2', 'Spin Box 3'),
                    initial_value='Spin Box 1')],
           [sg.Spin(values=['Spin Box 1', 'Spin Box 2', 'Spin Box 3'],
                    initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', 'Spin Box 2', 'Spin Box 3'), 
                    initial_value='Spin Box 3')]]

layout = [
    [sg.Menu(menu_def, tearoff=True)],
    [sg.Text('(Almost) All widgets in one Window!', size=(
        30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
    [sg.Text('Here is some text.... and a place to enter text')],
    [sg.InputText('This is my text')],
    [sg.Frame(layout=[
        [sg.CBox('Checkbox', size=(10, 1)),
         sg.CBox('My second checkbox!', default=True)],
        [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10, 1)),
         sg.Radio('My second Radio!', "RADIO1")]], title='Options', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
    [sg.MLine(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
     sg.MLine(default_text='A second multi-line', size=(35, 3))],
    [sg.Combo(('Combobox 1', 'Combobox 2'),default_value='Combobox 1', size=(20, 1)),
     sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
    [sg.OptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
     sg.Frame('Labelled Group', [[
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, tick_interval=25),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
         sg.Col(column1)]])
    ],
    [sg.Text('_' * 80)],
    [sg.Text('Choose A Folder', size=(35, 1))],
    [sg.Text('Your Folder', size=(15, 1), justification='right'),
     sg.InputText('Default Folder'), sg.FolderBrowse()],
    [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()]]

window = sg.Window('Everything bagel', layout)

event, values = window.read()
sg.popup('Title',
         'The results of the window.',
         'The button clicked was "{}"'.format(event),
         'The values are', values)
window.close()
exit()


#  888     888
#  888     888
#  888     888
#  888     888 .d8888b   .d88b.  888d888
#  888     888 88K      d8P  Y8b 888P"
#  888     888 "Y8888b. 88888888 888
#  Y88b. .d88P      X88 Y8b.     888
#   "Y88888P"   88888P'  "Y8888  888
#
#
#
#  8888888b.            .d888 d8b                        888
#  888  "Y88b          d88P"  Y8P                        888
#  888    888          888                               888
#  888    888  .d88b.  888888 888 88888b.   .d88b.   .d88888
#  888    888 d8P  Y8b 888    888 888 "88b d8P  Y8b d88" 888
#  888    888 88888888 888    888 888  888 88888888 888  888
#  888  .d88P Y8b.     888    888 888  888 Y8b.     Y88b 888
#  8888888P"   "Y8888  888    888 888  888  "Y8888   "Y88888
#
#
#
#  8888888888 888                                          888
#  888        888                                          888
#  888        888                                          888
#  8888888    888  .d88b.  88888b.d88b.   .d88b.  88888b.  888888 .d8888b
#  888        888 d8P  Y8b 888 "888 "88b d8P  Y8b 888 "88b 888    88K
#  888        888 88888888 888  888  888 88888888 888  888 888    "Y8888b.
#  888        888 Y8b.     888  888  888 Y8b.     888  888 Y88b.       X88
#  8888888888 888  "Y8888  888  888  888  "Y8888  888  888  "Y888  88888P'
#
#
#

# Without user defined element

layout = [  [sg.Text('Enter your information', font='Any 20')],
            [sg.Text('Name', size=(8,1), justification='r', font='Any 14'), sg.Input(key='-NAME-')],
            [sg.Text('Address', size=(8,1), justification='r', font='Any 14'), sg.Input(key='-ADDRESS-')],
            [sg.Text('Phone', size=(8,1), justification='r', font='Any 14'), sg.Input(key='-PHONE-')],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
window.close()


##########################################################################################

# User defined element that defines an entire row

def InfoIn(text, key):
    return [sg.Text(text, size=(8, 1), justification='r', font='Any 14'), sg.Input(key=key)]

layout = [  [sg.Text('Enter your information', font='Any 20')],
            InfoIn('Name', '-NAME-'),
            InfoIn('Address', '-ADDRESS-'),
            InfoIn('Phone', '-PHONE-'),
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
window.close()

exit()


#  888888b.            d8b 888      888
#  888  "88b           Y8P 888      888
#  888  .88P               888      888
#  8888888K.  888  888 888 888  .d88888
#  888  "Y88b 888  888 888 888 d88" 888
#  888    888 888  888 888 888 888  888
#  888   d88P Y88b 888 888 888 Y88b 888
#  8888888P"   "Y88888 888 888  "Y88888
#
#
#
#  888                                          888
#  888                                          888
#  888                                          888
#  888       8888b.  888  888  .d88b.  888  888 888888 .d8888b
#  888          "88b 888  888 d88""88b 888  888 888    88K
#  888      .d888888 888  888 888  888 888  888 888    "Y8888b.
#  888      888  888 Y88b 888 Y88..88P Y88b 888 Y88b.       X88
#  88888888 "Y888888  "Y88888  "Y88P"   "Y88888  "Y888  88888P'
#                         888
#                    Y8b d88P
#                     "Y88P"



import PySimpleGUI as sg

# Build layout using list comprehension

# Make a grid of buttons
layout = [[sg.B(' X ',key=(r,c)) for r in range(3)]for c in range(4)]

# Add on an OK button
layout += [[sg.OK()]]

window = sg.Window('title', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event is None:
        break



# Build layout using loops

layout = [[]]
for row in range(5):
    row_layout = []
    for col in range(5):
        row_layout.append(sg.Button('X', key=(row,col)))
    layout.append(row_layout)

layout += [[sg.Button('OK'), sg.Button('Cancel')]]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Go':
        window['-OUT-'].update(values['-IN-'])
window.close()

exit()


#   .d8888b.                888          888               
#  d88P  Y88b               888          888               
#  Y88b.                    888          888               
#   "Y888b.   888  888  .d88888  .d88b.  888  888 888  888 
#      "Y88b. 888  888 d88" 888 d88""88b 888 .88P 888  888 
#        "888 888  888 888  888 888  888 888888K  888  888 
#  Y88b  d88P Y88b 888 Y88b 888 Y88..88P 888 "88b Y88b 888 
#   "Y8888P"   "Y88888  "Y88888  "Y88P"  888  888  "Y88888 

sg.Window('Sudoku',[[sg.Frame('',[[sg.I(random.randint(1,9), justification='r', size=(3,1),key=(frow*3+row,fcol*3+col)) for col in range(3)] for row in range(3)]) for fcol in range(3)] for frow in range(3)]+ [[sg.B('Exit')]]).read()

exit()



#         d8888                                          888       888 d8b
#        d88888                                          888   o   888 Y8P
#       d88P888                                          888  d8b  888
#      d88P 888 .d8888b  888  888 88888b.   .d8888b      888 d888b 888 888 88888b.
#     d88P  888 88K      888  888 888 "88b d88P"         888d88888b888 888 888 "88b
#    d88P   888 "Y8888b. 888  888 888  888 888           88888P Y88888 888 888  888
#   d8888888888      X88 Y88b 888 888  888 Y88b.         8888P   Y8888 888 888  888
#  d88P     888  88888P'  "Y88888 888  888  "Y8888P      888P     Y888 888 888  888
#                             888
#                        Y8b d88P
#                         "Y88P"
#  88888888888 d8b                                          888
#      888     Y8P                                          888
#      888                                                  888
#      888     888 88888b.d88b.   .d88b.   .d88b.  888  888 888888 .d8888b
#      888     888 888 "888 "88b d8P  Y8b d88""88b 888  888 888    88K
#      888     888 888  888  888 88888888 888  888 888  888 888    "Y8888b.
#      888     888 888  888  888 Y8b.     Y88..88P Y88b 888 Y88b.       X88
#      888     888 888  888  888  "Y8888   "Y88P"   "Y88888  "Y888  88888P'


import PySimpleGUI as sg

layout = [  [sg.Text('My Timer')],
            [sg.Text(size=(12,1), key='-OUT-')],
            [sg.Button('Exit')]  ]

window = sg.Window('Timer', layout, font='Any 20')

counter = 0

while True:             # Event Loop
    event, values = window.read(timeout=100)
    # print(event, values)
    if event in (None, 'Exit'):
        break
    window['-OUT-'].update(counter)

    counter += 1
window.close()

exit()


#   .d8888b.                    888                      88888888888
#  d88P  Y88b                   888                          888
#  Y88b.                        888                          888
#   "Y888b.   888  888 .d8888b  888888 .d88b.  88888b.d88b.  888  888d888 8888b.  888  888
#      "Y88b. 888  888 88K      888   d8P  Y8b 888 "888 "88b 888  888P"      "88b 888  888
#        "888 888  888 "Y8888b. 888   88888888 888  888  888 888  888    .d888888 888  888
#  Y88b  d88P Y88b 888      X88 Y88b. Y8b.     888  888  888 888  888    888  888 Y88b 888
#   "Y8888P"   "Y88888  88888P'  "Y888 "Y8888  888  888  888 888  888    "Y888888  "Y88888
#                  888                                                                 888
#             Y8b d88P                                                            Y8b d88P
#              "Y88P"                                                              "Y88P"

# import PySimpleGUIWx as sg
# import PySimpleGUIQt as sg
import PySimpleGUI as sg

tray = sg.SystemTray(menu=['UNUSED', ['My', 'Simple', '---', 'Menu', 'Exit']], data_base64=sg.DEFAULT_BASE64_ICON)

while True:
    event = tray.read()
    if event == 'Exit':
        tray.show_message('Exiting', 'Exiting the program', messageicon=sg.SYSTEM_TRAY_MESSAGE_ICON_INFORMATION)
        break
      
exit()


#  8888888b.           888
#  888  "Y88b          888
#  888    888          888
#  888    888  .d88b.  88888b.  888  888  .d88b.   .d88b.   .d88b.  888d888
#  888    888 d8P  Y8b 888 "88b 888  888 d88P"88b d88P"88b d8P  Y8b 888P"
#  888    888 88888888 888  888 888  888 888  888 888  888 88888888 888
#  888  .d88P Y8b.     888 d88P Y88b 888 Y88b 888 Y88b 888 Y8b.     888
#  8888888P"   "Y8888  88888P"   "Y88888  "Y88888  "Y88888  "Y8888  888
#                                             888      888
#                                        Y8b d88P Y8b d88P
#                                         "Y88P"   "Y88P"


import PySimpleGUI as sg

layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)
count = 0
while True:             # Event Loop
    event, values = window.read(timeout=100)
    if event in (None, 'Exit'):
        break
    count += 1
window.close()



#  8888888888          888                          888 d8b
#  888                 888                          888 Y8P
#  888                 888                          888
#  8888888    888  888 888888 .d88b.  88888b.   .d88888 888 88888b.   .d88b.
#  888        `Y8bd8P' 888   d8P  Y8b 888 "88b d88" 888 888 888 "88b d88P"88b
#  888          X88K   888   88888888 888  888 888  888 888 888  888 888  888
#  888        .d8""8b. Y88b. Y8b.     888  888 Y88b 888 888 888  888 Y88b 888
#  8888888888 888  888  "Y888 "Y8888  888  888  "Y88888 888 888  888  "Y88888
#                                                                         888
#                                                                    Y8b d88P
#                                                                     "Y88P"

import PySimpleGUI as sg

window = sg.Window('test', layout=[[sg.ProgressBar(max_value=100, size=(30, 10), key='bar')]], finalize=True)

window['bar'].Widget.config(mode='indeterminate')

while True:
    event, values = window.read(timeout=100)
    if event is None:
        break
    window['bar'].Widget['value'] += 5