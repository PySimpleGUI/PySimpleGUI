"""
    Demo Language Select
    
    This example demostrates a simple technique for internationalization (i18n). When the program starts, the user
    is prompted to select a language. The program then loads in the appropriate language file, or fallback to a default
    language if the user did not choose.
    
    http://www.PySimpleGUI.org
    Copyright 2022 PySimpleGUI
"""
import PySimpleGUI as sg

# Prepare language resources
lang_dict_en = {"ask_name": "What's your name?", "ok": "OK", "quit": "Quit", "hello": "Hello" ,"thanks": "! Thanks for trying PySimpleGUI", "title": "Multi-lang Example"}
lang_dict_zh_cn = {"ask_name": "你的名字是？", "ok": "好的", "quit": "退出", "hello": "你好" ,"thanks": "！感谢使用 PySimpleGUI", "title": "多语言示例"}
lang_dicts = {"en": lang_dict_en, "zh_cn": lang_dict_zh_cn}

# Choose a default language
l = lang_dicts["en"] # language mapping (default to 'en')

# Define and create language selection window
lang_select_layout = [
    [sg.Text('Language Select')],
    [sg.Radio('English', 'LANG', key='en', default=True)],
    [sg.Radio('简体中文', 'LANG', key='zh_cn')],
    [sg.Button('OK', size=(10, 1))]
]

lang_select_window = sg.Window('Language Select', lang_select_layout)  

# Switch language using user's input
event, values = lang_select_window.read()
for language, selected in values.items():
    if selected:
        l = lang_dicts[language]
lang_select_window.close()

# Define and create main window
# note: using l[key_name] for all i18n string
layout = [[sg.Text(l["ask_name"])],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button(l["ok"]), sg.Button(l["quit"])]]

window = sg.Window(l["title"], layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == l["quit"]:
        break
    window['-OUTPUT-'].update(l["hello"] + ' ' + values['-INPUT-'] + l["thanks"])

window.close()
