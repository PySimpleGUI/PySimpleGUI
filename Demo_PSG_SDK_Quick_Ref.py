#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
    from tkinter import Tk
else:
    import PySimpleGUI27 as sg
    from Tkinter import Tk


desc_text = """
Text(   text
        size=(None, None)
        auto_size_text=None
        click_submits=None
        relief=None
        font=None
        text_color=None
        background_color=None
        justification=None
        pad=None
        key=None
        tooltip=None)

Shortcuts: Txt, T        
"""

desc_inputtext = """
InputText(  default_text =''
            size=(None, None)
            disabled=False
            auto_size_text=None
            password_char=''
            justification=None
            background_color=None
            text_color=None
            font=None
            tooltip=None
            do_not_clear=False
            key=None
            focus=False
            pad=None)

Shortcuts: In, Input
"""

desc_inputcombo = """
InputCombo( values
            default_value=None
            size=(None, None)
            auto_size_text=None
            background_color=None
            text_color=None
            change_submits=False
            disabled=False
            key=None
            pad=None
            tooltip=None)

Shortcuts: Combo, DropDown, Drop            
"""

desc_inputoptionmenu = """
InputOptionMenu(values
                default_value=None
                size=(None, None)
                disabled=False
                auto_size_text=None
                background_color=None
                text_color=None
                key=None
                pad=None
                tooltip=None)

Shortcuts: OptionMenu 
"""

desc_listbox = """
Listbox(values
        default_values=None
        select_mode=None
        change_submits=False
        bind_return_key=False
        size=(None, None)
        auto_size_text=None
        font=None
        background_color=None
        text_color=None
        key=None
        pad=None
        tooltip=None)
"""

desc_checkbox = """
CheckBox(   text
            default=False
            size=(None, None)
            auto_size_text=None
            font=None
            background_color=None
            text_color=None
            change_submits=False
            disabled=False
            key=None
            pad=None
            tooltip=None)

Shortcuts: CB, CBox, Check             
"""

desc_radio = """
Radio(  text
        group_id
        default=False
        disabled=False
        size=(None, None)
        auto_size_text=None
        background_color=None
        text_color=None
        font=None
        key=None
        pad=None
        tooltip=None)
"""

desc_spin = """
Spin(   values
        initial_value=None
        disabled=False
        change_submits=False
        size=(None, None)
        auto_size_text=None
        font=None
        background_color=None
        text_color=None
        key=None
        pad=None
        tooltip=None)
"""

desc_multiline = """
MultiLine(  default_text=''
            enter_submits = False
            disabled=False
            autoscroll=False
            size=(None,None)
            auto_size_text=None
            background_color=None
            text_color=None
            do_not_clear=False
            key=None
            focus=False
            pad=None
            tooltip=None)
"""

desc_output = """
Output( size=(None, None)
        background_color=None
        text_color=None
        pad=None
        font=None
        tooltip=None
        key=None)
"""

desc_button = """
Button( button_text=''
        button_type=BUTTON_TYPE_CLOSES_WIN
        target=(None, None)
        tooltip=None
        file_types=(("ALL Files", "*.*"),)
        initial_folder=None
        disabled=False
        image_filename=None
        image_size=(None, None)
        image_subsample=None
        border_width=None
        size=(None, None)
        auto_size_button=None
        button_color=None
        default_value = None
        font=None
        bind_return_key=False
        focus=False
        pad=None
        key=None)
"""

desc_progressbar = """
ProgressBar(max_value
            orientation=None
            size=(None, None)
            auto_size_text=None
            bar_color=(None, None)
            style=None
            border_width=None
            relief=None
            key=None
            pad=None)
"""

desc_image = """
Image(  filename=None
        data=None
        size=(None, None)
        pad=None
        key=None
        tooltip=None)
"""

desc_canvas = """
Canvas( canvas=None
        background_color=None
        size=(None, None)
        pad=None
        key=None
        tooltip=None)
"""

desc_graph = """
Graph(  canvas_size
        graph_bottom_left
        graph_top_right
        background_color=None
        pad=None
        key=None
        tooltip=None)
"""

desc_frame = """
Frame(  title
        layout
        title_color=None
        background_color=None
        title_location=None 
        relief=DEFAULT_FRAME_RELIEF
        size=(None, None)
        font=None
        pad=None
        border_width=None
        key=None
        tooltip=None)
"""

desc_tab = """
Tab(title
    layout
    title_color=None
    background_color=None
    font=None
    pad=None
    disabled=False
    border_width=None
    key=None
    tooltip=None)
"""

desc_tabgroup = """
TabGroup(   layout
            tab_location=None
            title_color=None
            selected_title_color=None
            background_color=None
            font=None
            change_submits=False
            pad=None
            border_width=None
            theme=None
            key=None
            tooltip=None)
"""

desc_slider = """
Slider( range=(None,None)
        default_value=None
        resolution=None
        orientation=None
        border_width=None
        relief=None
        change_submits=False
        disabled=False
        size=(None, None)
        font=None
        background_color=None
        text_color=None
        key=None
        pad=None
        tooltip=None)
"""


desc_spin = """
Spin(   values
        initial_value=None
        disabled=False
        change_submits=False
        size=(None, None)
        auto_size_text=None
        font=None
        background_color=None
        text_color=None
        key=None
        pad=None
        tooltip=None)
"""


desc_tree = """
Tree( data=None,
      headings=None, 
      visible_column_map=None, 
      col_widths=None, 
      col0_width=10, 
      def_col_width=10, 
      auto_size_columns=True, 
      max_col_width=20, 
      select_mode=None, 
      font=None, 
      justification='right', 
      text_color=None, 
      background_color=None, 
      num_rows=None, 
      pad=None, 
      key=None, 
      tooltip=None):
"""


desc_column = """
Column( layout
        background_color = None
        size=(None, None)
        pad=None
        scrollable=False
        key=None)
"""


desc_table = """
Table(  values
        headings=None
        visible_column_map=None
        col_widths=None
        def_col_width=10
        auto_size_columns=True
        max_col_width=20
        select_mode=None
        display_row_numbers=False
        scrollable=None
        font=None
        justification='right'
        text_color=None
        background_color=None
        size=(None, None)
        pad=None
        key=None
        tooltip=None)
"""

desc_window = """
Window( title
        default_element_size=DEFAULT_ELEMENT_SIZE
        default_button_element_size = (None, None)
        auto_size_text=None
        auto_size_buttons=None
        location=(None, None)
        button_color=None
        font=None
        progress_bar_color=(None, None)
        background_color=None
        border_depth=None
        auto_close=False
        auto_close_duration=DEFAULT_AUTOCLOSE_TIME
        icon=DEFAULT_WINDOW_ICON
        force_toplevel = False
        return_keyboard_events=False
        use_default_focus=True
        text_justification=None
        no_titlebar=False
        grab_anywhere=False
        keep_on_top=False
        resizable=False)
"""

desc_window_methods = """
Layout(rows)      
Call to set the window layout.  Must be called prior to Read.  Most likely "chained" in line with the Window creation.    
    
Finalize()    
Call to force a window to go through the final stages of initialization.  This will cause the tkinter resources to be allocated so that they can then be modified.      

Read()    
Read the Window's input values and button clicks in a blocking-fashion    
Returns event, values    

ReadNonBlocking()    
Read the Window's input values and button clicks but without blocking.  It will immediately return.    

Refresh()    
Cause changes to the window to be displayed on the screen.  Normally not needed unless the changes are immediately required or if it's going to be a while before another call to Read.    

SetIcon(icon)
Sets the window's icon that will be shown on the titlebar.    

Fill(values_dict)    
Populates the windows fields with the values shown in the dictionary.      

FindElement(key)      
Rerturns the Element that has a matching key.  If the key is not found, an Error Element is returned so that the program will not crash should the user try to perform an "update".  A Popup message will be shown    
    
SaveToDisk(filename)    
Saves the window's values to disk      

LoadFromDisk(filename)    
Fills in a window's fields based on previously saved file    
    
GetScreenDimensions()       
Returns the size (w,h) of the screen in pixels    
    
Move(x, y)
Move window to (x,y) position on the screen

Minimize()
Sends the window to the taskbar

CloseNonBlocking()    
Closes a non-blocking window    
    
Disable()    
Stops a window from  responding until Enable is called    
    
Enable()    
Re-enables a previously disabled window    
    
Hide()    
Completely hides a window, including removing from the taskbar    

UnHide()   
Restores a window hidden using Hide    

Disappear()    
Makes a window disappear while leaving the icon on the taskbar    
    
Reappear()    
Makes a window reappear that was previously made to disappear using Disappear()    
    
SetAlpha(alpha)
Sets the window's transparency.  0 is completely transparent.  1 is fully visible, normal   
"""


desc_menu= """
   Menu(menu_definition
        background_color=None
        size=(None, None)
        tearoff=True
        pad=None
        key=None)
"""

desc_button_types = """
There are multiple button types / names to choose from
CloseButton = CButton = SimpleButton
Button = ReadFormButton = ReadButton = RButton
RealtimeButton
DummyButton
FolderBrowse
FileBrowse
FilesBrowse
FileSaveAs = SaveAs
CalendarButton
ColorChooserButton
    Shortcuts - Normal buttons with predefined text
Save, Open, OK, Ok, Cancel, Quit, Exit, Yes, No, Help

"""


desc_popup= """
  Popup(button_color=None
        background_color=None
        text_color=None
        button_type=POPUP_BUTTONS_OK
        auto_close=False
        auto_close_duration=None
        non_blocking=False
        icon=DEFAULT_WINDOW_ICON
        line_width=None
        font=None
        no_titlebar=False
        grab_anywhere=False
        keep_on_top=False
        location=(None,None))
"""



desc_popups = """
PopupScrolled
PopupGetFolder
PopupGetFile
PopupGetText
POopup
PopupNoButtons
PopupNonBlocking = PopupNoWait
PopupQuick
PopupNoTitleBar = PopupNoFrame = PopupNoBorder = PopupAnnoying
PopupAutoClose = PopupTimed
PopupError
PopupCancel
PopupOK
PopupOKCancel
PopupYesNo
"""



desc_one_line_progress_meter = """
   OneLineProgressMeter(title
                        current_value
                        max_value
                        key
                        *args
                        orientation=None
                        bar_color=(None,None)
                        button_color=None
                        size=DEFAULT_PROGRESS_BAR_SIZE
                        border_width=None
                        grab_anywhere=False):
"""

element_list = ('Window',
                'Text',
                'InputText',
                'CheckBox',
                'RadioButton',
                'Listbox',
                'InputCombo',
                'Slider',
                'Spinner',
                'Multiline',
                'Output',
                'ProgressBar',
                'OptionMenu',
                'Menu',
                'Frame',
                'Column',
                'Graph',
                'Image',
                'Table',
                'Tab',
                'TabGroup',
                'Button Types')

descriptions = {'Window': desc_window, 'Text': desc_text, 'InputText': desc_inputtext, 'Checkbox': desc_checkbox,
                'Radio': desc_radio, 'Listbox': desc_listbox, 'Slider': desc_slider, 'Spinner':desc_spin, 'Multiline': desc_multiline,
                'Output': desc_output, 'ProgressBar': desc_progressbar, 'OptionMenu': desc_inputoptionmenu,
                'Combo': desc_inputcombo, 'Menu': desc_menu, 'Frame': desc_frame, 'Column': desc_column,
                'Graph': desc_graph, 'Image': desc_image, 'Table': desc_table, 'Tree': desc_tree,'Tab': desc_tab,
                'TabGroup': desc_tabgroup, 'Button':desc_button, 'Button Types': desc_button_types,
                'Popup':desc_popup, 'Popups':desc_popups, 'One Line Prog Meter':desc_one_line_progress_meter}


tab_text = [[sg.Column([[sg.T('This is sample text')],[ sg.Text(desc_text,  font=('Consolas 12'))]])]]
tab_input = [[sg.Column([[sg.Input(size=(15,1))],[sg.Text(desc_inputtext, font=('Consolas 12'))]])]]
tab_checkbox = [[sg.Column([[sg.Checkbox('Checkbox', size=(15,1))],[sg.Text(desc_checkbox, font=('Consolas 12'))]])]]
tab_radio = [[sg.Column([[sg.Radio('Radio Button', group_id=1, size=(15,1))],[sg.Text(desc_radio, font=('Consolas 12'))]])]]
tab_listbox = [[sg.Column([[sg.Listbox(values=[1,2,3,4] ,size=(15,4))],[sg.Text(desc_listbox, font=('Consolas 12'))]])]]
tab_slider = [[sg.Column([[sg.Slider((1,100), orientation='h', size=(15,15))],[sg.Text(desc_slider, font=('Consolas 12'))]])]]
tab_spinner = [[sg.Column([[sg.Spin((1,2,3,4,5),initial_value=1,size=(15,1))],[sg.Text(desc_spin, font=('Consolas 12'))]])]]
tab_multiline = [[sg.Column([[sg.Multiline(size=(15,1))],[sg.Text(desc_multiline, font=('Consolas 12'))]])]]
tab_output= [[sg.Column([[sg.Text(desc_output, font=('Consolas 12'))]])]]
tab_progressbar = [[sg.Column([[sg.Text(desc_progressbar, font=('Consolas 12'))]])]]
tab_optionmenu = [[sg.Column([[sg.OptionMenu([1,2,3,4,5], size=(15,1))],[sg.Text(desc_inputoptionmenu, font=('Consolas 12'))]])]]
tab_combo = [[sg.Column([[sg.Combo([1,2,3,4,5], size=(15,1))],[sg.Text(desc_inputcombo, font=('Consolas 12'))]])]]
tab_frame = [[sg.Column([[sg.Frame('Frame',[[sg.T('     ')]], size=(15,1))],[sg.Text(desc_frame, font=('Consolas 12'))]])]]
tab_column = [[sg.Text(desc_column, font=('Consolas 12'))]]
tab_graph = [[sg.Text(desc_graph, font=('Consolas 12'))]]
tab_tab = [[sg.Text(desc_tab, font=('Consolas 12'))]]
tab_tabgroup = [[sg.Text(desc_tabgroup, font=('Consolas 12'))]]
tab_image = [[sg.Text(desc_image, font=('Consolas 12'))]]
tab_table = [[sg.Text(desc_table, font=('Consolas 12'))]]
tab_tree = [[sg.Text(desc_tree, font=('Consolas 12'))]]
tab_menu = [[sg.Text(desc_menu, font=('Consolas 12'))]]
tab_button = [[sg.Text(desc_button, font=('Consolas 12'))]]
tab_button_types = [[sg.Text(desc_button_types, font=('Consolas 12'))]]
tab_popup = [[sg.Text(desc_popup, font=('Consolas 12'))]]
tab_popups = [[sg.Text(desc_popups, font=('Consolas 12'))]]
tab_one_line_prog_meter = [[sg.Text(desc_one_line_progress_meter, font=('Consolas 12'))]]

tab_window = [[ sg.TabGroup([[sg.Tab('Parms',[[sg.Text(desc_window, font=('Consolas 12'))]]),
                              sg.Tab('Methods', [[sg.Column([[sg.Text(desc_window_methods)]], size=(500,500), scrollable=True, )]])]])]]

layout = [[sg.TabGroup([[sg.Tab('Window',tab_window),
                         sg.Tab('Text',tab_text),
                         sg.Tab('InputText', tab_input),
                         sg.Tab('Checkbox', tab_checkbox),
                         sg.Tab('Radio',tab_radio),
                         sg.Tab('Listbox', tab_listbox),
                         sg.Tab('Slider', tab_slider),
                         sg.Tab('Spinner',tab_spinner),
                         sg.Tab('Multiline', tab_multiline),
                         sg.Tab('OptionMenu', tab_optionmenu),
                         sg.Tab('Combo', tab_combo),
                         sg.Tab('Image', tab_image),
                         sg.Tab('Output', tab_output),
                         sg.Tab('Table', tab_table),
                         sg.Tab('Tree', tab_tree),
                         sg.Tab('Graph', tab_graph),
                         sg.Tab('ProgressBar', tab_progressbar),
                         sg.Tab('Frame', tab_frame),
                         sg.Tab('Column', tab_column),
                         sg.Tab('Tab', tab_tab),
                         sg.Tab('TabGroup', tab_tabgroup),
                         sg.Tab('Menu', tab_menu),
                         sg.Tab('Button', tab_button),
                         sg.Tab('Button Types', tab_button_types),
                         sg.Tab('Popup', tab_popup),
                         sg.Tab('Popups', tab_popups),
                         sg.Tab('One Line Prog Meter', tab_one_line_prog_meter),
                         ]], tab_location='lefttop', title_color='blue', selected_title_color='red', key='_TABS_')],
                        [sg.Button('Copy')]          ]

# layout = [[sg.Text('The PySimpleGUI SDK Quick Reference Guide', font='Any 15', relief=sg.RELIEF_RAISED)],
#           [sg.Listbox(values=element_list, size=(15, len(element_list) + 2), key='_in_', change_submits=True,
#                       font=('Consolas 12')),
#            sg.Text(desc_text, size=(55, 25), font=('Consolas 13'), text_color='darkblue', key='_out_')]]

window = sg.Window('PySimpleGUI SDK Quick Reference',
                   font='Consolas 12',
                   ).Layout(layout)

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    elif event == 'Methods':
        sg.PopupScrolled(desc_window_methods, size=(50,20))
    elif event == 'Copy':
        tab = values['_TABS_']
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(descriptions[tab])
        r.update()  # now it stays on the clipboard after the window is closed
        r.destroy()

    # element = values['_in_'][0]
    # try:
    #     desc = descriptions[element]
    # except:
    #     desc = ''
    # window.FindElement('_out_').Update(desc)

    # print(button, values)
