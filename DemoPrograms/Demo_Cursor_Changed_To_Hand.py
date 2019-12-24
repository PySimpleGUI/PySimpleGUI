import PySimpleGUI as sg
import webbrowser

"""
    Demonstration of setting an Element's Widget to use a different cursor than the
    standard arrow.  In this case, the cursor is changed into a hand when hovering over the Text Element.

    This implementation relies on accessing the underlying tkinter widget to change the cursor as there is currently no method provided for you to modify a widget's cursor.  Accessing an Element's tkinter widget is easy and straightforward, you simply write:
            window[key].Widget
"""

# Here is a more complete list of cursors you can choose from
cursors = ('X_cursor', 'no', 'arrow','based_arrow_down','based_arrow_up','boat','bogosity','bottom_left_corner','bottom_right_corner','bottom_side','bottom_tee','box_spiral','center_ptr','circle','clock','coffee_mug','cross','cross_reverse','crosshair','diamond_cross','dot','dotbox','double_arrow','draft_large','draft_small','draped_box','exchange','fleur','gobbler','gumby','hand1','hand2','heart','icon','iron_cross','left_ptr','left_side','left_tee','leftbutton','ll_angle','lr_angle','man','middlebutton','mouse','no','pencil','pirate','plus','question_arrow','right_ptr','right_side','right_tee','rightbutton','rtl_logo','sailboat','sb_down_arrow','sb_h_double_arrow','sb_left_arrow','sb_right_arrow','sb_up_arrow','sb_v_double_arrow','shuttle','sizing','spider','spraycan','star','target','tcross','top_left_arrow','top_left_corner','top_right_corner','top_side','top_tee','trek','ul_angle','umbrella','ur_angle','watch','xterm','arrow','center_ptr','crosshair','fleur','ibeam','icon','sb_h_double_arrow','sb_v_double_arrow','watch','xterm','no','starting','size','size_ne_sw','size_ns','size_nw_se','size_we','uparrow','wait','arrow','cross','crosshair','ibeam','plus','watch','xterm')

sg.theme('Light Blue 2')

layout = [  [sg.Text('Here is a clickable link for you')],
            [sg.Text('Notice how the cursor switches to a "hand" when hover over the link')],
            [sg.Text('www.PySimpleGUI.org', font=('default 12 underline'), text_color='blue', enable_events=True, key='-LINK-')],
            [sg.Text('Try out these additional cursors')],
            [sg.Text('watch - This makes the spinning-donut-of-death cursor on Windows', key='-WATCH-')],
            [sg.Text('fleur - The "Move" cursor', key='-FLEUR-')],
            [sg.Text('trek - Beam me up Scotty!', key='-TREK-')],
            [sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout, finalize=True)

# Directly interact with the tkinter widget, changing the cursor shown when placed cursor is over this element
window['-LINK-'].set_cursor(cursor='hand2')
window['-WATCH-'].set_cursor(cursor='watch')
window['-FLEUR-'].set_cursor(cursor='fleur')
window['-TREK-'].set_cursor(cursor='trek')
window['Exit'].set_cursor(cursor='no')

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == '-LINK-':
        # if the text was clicked, open a browser using the text as the address
        webbrowser.open(window['-LINK-'].DisplayText)   # accessing DisplayText isn't something you'll see often
window.close()
