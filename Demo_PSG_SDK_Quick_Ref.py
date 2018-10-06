import PySimpleGUI as sg

element_list = ('Text',
                'InputText',
                'CheckBox',
                'RadioButton',
                'Listbox',
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

desc_checkbox = """
CheckBox(   text,
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


descriptions = {'Text':desc_text, 'InputText':desc_inputtext, 'CheckBox':desc_checkbox}

layout = [[sg.Text('Persistent window')],
          [sg.Listbox(values=element_list, size=(15,len(element_list)), key='_in_', change_submits=True),
           sg.Text(desc_text, size=(40,15),font=('Consolas 13'), key='_out_')],
          [sg.RButton('Read'), sg.Exit()]]

window = sg.Window('Window that stays open').Layout(layout)

while True:
    button, values = window.Read()
    if button is None or button == 'Exit':
        break
    element = values['_in_'][0]
    try:
        desc = descriptions[element]
    except: desc = ''
    window.FindElement('_out_').Update(desc)
    print(button, values)