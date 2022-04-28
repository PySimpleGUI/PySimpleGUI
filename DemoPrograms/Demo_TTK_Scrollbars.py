import PySimpleGUI as sg

"""
    Demo - TTK Scrollbars
    
    Beginning in release 4.60.0 (May 2022), all scrollbars in the tkinter port use TTK Scrollbars
    
    This feature impacts all elements that have scrollbars including:
        Multiline
        Output
        Listbox
        Table
        Tree
        Column
        
    Not all elements in PySimpleGUI use TTK Widgets.  Some of the Widgets are TK Widgets.  Regardless of the
    underlying widget, if it has a scrollbar that's visible normally (one of the above elements... unlike the Combo),
    then it will use a TTK scrollbar.
    
    There are many options available to you to set for these scrollbars.  
    
    TTK Theme
    
    While the TTK Theme has been available for you to set, most users have likely not experimented much with this feature.
    This may change with these new scrollbars because the TTK Theme will impact how the scrollbars look.  Be aware that 
    the TTK Theme will also impact elements that use TTK Widgets.
    
    You can see what tkinter widgets are used for all of the elements in the documenation located here:
    https://pysimplegui.readthedocs.io/en/latest/#table-of-elements-in-tkinter-port
    
    Hierarchy of settings
    
    The scrollbar settings used for an element are picked up from one of these 4 locations.  The priority order for
    the settings is:
    1. The Element's parms in the layout (you can change individual element's scrollbars)
    2. Window parms
    3. set_options parms
    4. The Global Settings (changable by calling sg.main())

    The TTK Theme follows a similar hierarchy.  The order of priority to determine the theme is:
    1. Window parm
    2. set_options parm
    3. The Global Settings
   
    More detailed information is available in the documenation about these scrollbars.  The docstrings also tell you about
    each parm. The parm names are identical for the elements, the Window and the set_options call
        sbar_trough_color:           
            Scrollbar color of the trough
        sbar_background_color: 
            Scrollbar color of the background of the arrow buttons at the ends AND the color of the "thumb" (the thing you grab and slide). Switches to arrow color when mouse is over
        sbar_arrow_color:      
            Scrollbar color of the arrow at the ends of the scrollbar (it looks like a button). Switches to background color when mouse is over
        sbar_width:        
            Scrollbar width in pixels           
        sbar_arrow_width:             
            Scrollbar width of the arrow on the scrollbar. It will potentially impact the overall width of the scrollbar  
        sbar_frame_color: 
            Scrollbar Color of frame around scrollbar (available only on some ttk themes)     
        sbar_relief:           
            Scrollbar relief that will be used for the "thumb" of the scrollbar (the thing you grab that slides). Should be a constant that is defined at starting with "RELIEF_" - RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID

    Note that some parms can impact others.  For example, setting the relief to Ridge negates the frame color setting

    This Demo shows 2 different windows to demonstrate the parms in the Window object and set_options.

    Copyright 2022 PySimpleGUI
"""


# Our first window uses your global defaults with the Listbox element directly overriding the settings

layout = [[sg.T('Fun with TTK Scrollbars')],
          [sg.Multiline('\n'.join([str(x) for x in range(50)]), size=(40,20), expand_x=True, expand_y=True),
           sg.Listbox(list(range(40)), s=(10,15),
                     sbar_background_color='green', sbar_trough_color='red', sbar_relief='ridge', sbar_arrow_color='purple', sbar_frame_color='yellow',)],
          [sg.Button('Exit'), sg.Sizegrip()]]


window = sg.Window('TTK Scrollbars 1', layout, resizable=True)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()

# Our second window uses both set_options and the Window object to change the scrollbars


sg.set_options(sbar_width=30, sbar_arrow_width=30)

layout = [[sg.T('Fun with TTK Scrollbars 2')],
          [sg.Multiline('\n'.join([str(x) for x in range(50)]), size=(40,20), expand_x=True, expand_y=True),
           sg.Listbox(list(range(40)), s=(10,15),
                     sbar_background_color='green', sbar_trough_color='red',  sbar_arrow_color='purple', sbar_frame_color='yellow',)],
          [sg.Button('Exit'), sg.Sizegrip()]]


window = sg.Window('TTK Scrollbars 2', layout, sbar_relief=sg.RELIEF_SOLID, resizable=True)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()

