import PySimpleGUI as sg
import webbrowser

"""
    Demo Cursors
    
    Demonstration of setting an Element's Cursor to use a different cursor than the standard arrow.
    Can also change Cursor at the Window level.  
    
    If you want no cursor, set the cursor to the string 'none'.

    Copyright 2021 PySimpleGUI
"""

# Here is a more complete list of cursors you can choose from
cursors = ('X_cursor', 'no', 'arrow','based_arrow_down','based_arrow_up','boat','bogosity','bottom_left_corner','bottom_right_corner','bottom_side','bottom_tee','box_spiral','center_ptr','circle','clock','coffee_mug','cross','cross_reverse','crosshair','diamond_cross','dot','dotbox','double_arrow','draft_large','draft_small','draped_box','exchange','fleur','gobbler','gumby','hand1','hand2','heart','icon','iron_cross','left_ptr','left_side','left_tee','leftbutton','ll_angle','lr_angle','man','middlebutton','mouse','no','pencil','pirate','plus','question_arrow','right_ptr','right_side','right_tee','rightbutton','rtl_logo','sailboat','sb_down_arrow','sb_h_double_arrow','sb_left_arrow','sb_right_arrow','sb_up_arrow','sb_v_double_arrow','shuttle','sizing','spider','spraycan','star','target','tcross','top_left_arrow','top_left_corner','top_right_corner','top_side','top_tee','trek','ul_angle','umbrella','ur_angle','watch','xterm','arrow','center_ptr','crosshair','fleur','ibeam','icon','sb_h_double_arrow','sb_v_double_arrow','watch','xterm','no','starting','size','size_ne_sw','size_ns','size_nw_se','size_we','uparrow','wait','arrow','cross','crosshair','ibeam','plus','watch','xterm')

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