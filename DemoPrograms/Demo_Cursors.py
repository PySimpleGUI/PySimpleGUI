import PySimpleGUI as sg
import webbrowser

"""
    Demo Cursors
    
    Demonstration of setting an Element's Cursor to use a different cursor than the standard arrow.
    Can also change Cursor at the Window level.  
    
    If you want no cursor, set the cursor to the string 'none'.

    Copyright 2021, 2022 PySimpleGUI
"""

# Here is a more complete list of cursors you can choose from
cursors = sg.TKINTER_CURSORS

sg.theme('Light Blue 2')

layout = [  [sg.Text('Here is a clickable link for you')],
            [sg.Text('Notice how the cursor switches to a "hand" when hover over the link')],
            [sg.Text('www.PySimpleGUI.org', font='default 12 underline', text_color='blue', enable_events=True, key='-LINK-')],
            [sg.Text('Try out these additional cursors')],
            [sg.Text('watch - This makes the spinning-donut-of-death cursor on Windows', key='-WATCH-')],
            [sg.Text('fleur - The "Move" cursor', key='-FLEUR-')],
            [sg.Text('trek - Beam me up Scotty!', key='-TREK-')],
            [sg.Text('none - No cursor at all', key='-NONE-')],
            [sg.Text('For touchscreen applications, you may want to turn off the cursor entirely for the windw')],
            [sg.Text('Click the Hide Cursor button to turn off at the Window level.')],
            [sg.Text('Elements that have specific cursors set will continue to show those cursors')],
            [sg.Button('Hide Cursor'), sg.Button('Exit')]  ]

window = sg.Window('Cursor Demo', layout, finalize=True)

# Make sure window is finalized first.  Then set the cursor
window['-LINK-'].set_cursor(cursor='hand1')
window['-WATCH-'].set_cursor(cursor='watch')
window['-FLEUR-'].set_cursor(cursor='fleur')
window['-TREK-'].set_cursor(cursor='trek')
window['Exit'].set_cursor(cursor='no')
window['-NONE-'].set_cursor(cursor='none')

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Hide Cursor':
        window.set_cursor('none')       # special value that hides the cursor entirely
    elif event == '-LINK-':
        # if the text was clicked, open a browser using the text as the address
        webbrowser.open(window['-LINK-'].DisplayText)   # accessing DisplayText isn't something you'll see often
window.close()