import PySimpleGUI as sg


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
        tooltip=None)"""

desc_inputtext = """
InputText(  default_text =''
            size=(None, None)
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
"""

desc_inputoptionmenu = """
InputOptionMenu(values
                default_value=None
                size=(None, None)
                auto_size_text=None
                background_color=None
                text_color=None
                key=None
                pad=None
                tooltip=None)
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
            key=None
            pad=None
            tooltip=None)
"""

desc_radio = """
Radio(  text
        group_id
        default=False
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
        size=(None, None)
        font=None
        background_color=None
        text_color=None
        key=None
        pad=None
        tooltip=None)
"""


desc_column = """
Column( layout
        background_color = None
        size=(None, None)
        pad=None
        scrollable=False
        key=None)
"""

desc_menu = """
Menu(   menu_definition
        background_color=None
        size=(None, None)
        tearoff=True
        pad=None
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
        keep_on_top=False)
"""

element_list = ('Window',
                'Text',
                'InputText',
                'CheckBox',
                'RadioButton',
                'Listbox',
                'InputCombo',
                'Slider',
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
                'TabGroup')



descriptions = {'Window':desc_window, 'Text':desc_text, 'InputText':desc_inputtext, 'CheckBox':desc_checkbox,
                'RadioButton' : desc_radio, 'Listbox':desc_listbox, 'Slider':desc_slider, 'Multiline':desc_multiline,
                'Output':desc_output,
                'ProgressBar':desc_progressbar,
                'OptionMenu':desc_inputoptionmenu,
                'InputCombo':desc_inputcombo,
                'Menu':desc_menu,
                'Frame':desc_frame,
                'Column': desc_column,
                'Graph':desc_graph,
                'Image':desc_image,
                'Table':desc_table,
                'Tab':desc_tab,
                'TabGroup': desc_tabgroup}

layout = [[sg.Text('The PySimpleGUI SDK Quick Reference Guide',font='Any 15', relief=sg.RELIEF_RAISED)],
          [sg.Listbox(values=element_list, size=(15,len(element_list)+3), key='_in_', change_submits=True, font=('Consolas 12')),
           sg.Text(desc_text, size=(55,25),font=('Consolas 13'), text_color='darkblue', key='_out_')],
          [sg.RButton('Read'), sg.Exit()]]

window = sg.Window('Window that stays open',
                   font = 'Any 12').Layout(layout)

while True:
    button, values = window.Read()
    if button is None or button == 'Exit':
        break
    element = values['_in_'][0]
    try:
        desc = descriptions[element]
    except: desc = ''
    window.FindElement('_out_').Update(desc)
    # print(button, values)