"""
  A minimalist Notepad built with the PySimpleGUI TKinter framework
  Author:     Israel Dryer
  Contributor:    Lovelesh
  Email:      israel.dryer@gmail.com
  Modified:   2020-06-20
"""
import pathlib

import PySimpleGUI as sg
import textract

sg.ChangeLookAndFeel('BrownBlue')  # change style

WIN_W = 90
WIN_H = 25
file = None

menu_layout = [['File', ['New (Ctrl+N)', 'Open (Ctrl+O)', 'Save (Ctrl+S)', 'Save As', '---', 'Exit']],
               ['Tools', ['Word Count']],
               ['Help', ['About']]]

layout = [[sg.Menu(menu_layout)],
          [sg.Text('> New file <', font=('Consolas', 10),
                   key='_INFO_', size=(20, 1)), sg.Button('Clear',
                                                          font=("Helvetica", 10, "bold"), tooltip="Clears All Text",
                                                          auto_size_button=True, border_width=3, )],
          [sg.Multiline(font=('Consolas', 12), size=(WIN_W, WIN_H), key='_BODY_'), ]]

window = sg.Window('Notepad', layout=layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
window.maximize()
window['_BODY_'].expand(expand_x=True, expand_y=True)


def new_file():
    """Reset body and info bar, and clear filename variable"""
    window['_BODY_'].update(value='')
    window['_INFO_'].update(value='> New File <')
    file = None
    return file


def open_file():
    """Open file and update the infobar"""
    filename = sg.popup_get_file('Open', no_window=True)

    text = textract.process(filename)

    text1 = text.decode("utf-8")

    window['_BODY_'].update(value=text1)

    window['_INFO_'].update(value=filename)

    return file


def save_file(file):
    """Save file instantly if already open; otherwise use `save-as` popup"""
    if file:
        file.write_text(values.get('_BODY_'))
    else:
        save_file_as()


def save_file_as():
    """Save new file or save existing file with another name"""
    filename = sg.popup_get_file('Save As', save_as=True, no_window=True)
    if filename:
        file = pathlib.Path(filename)
        file.write_text(values.get('_BODY_'))
        window['_INFO_'].update(value=file.absolute())
        return file


def word_count():
    """Display estimated word count"""
    words = [w for w in values['_BODY_'].split(' ') if w != '\n']
    word_count = len(words)
    sg.popup_no_wait('Word Count: {:,d}'.format(word_count))


def about_me():
    """A short, pithy quote"""
    sg.popup_no_wait('"All great things have small beginnings" - Peter Senge')


while True:
    event, values = window.read()
    if event in ('Exit', None):
        break
    if event in ('New (Ctrl+N)', 'n:78'):
        file = new_file()
    if event in ('Open (Ctrl+O)', 'o:79'):
        file = open_file()
    if event in ('Save (Ctrl+S)', 's:83'):
        save_file(file)
    if event in ('Save As',):
        file = save_file_as()
    if event in ('Word Count',):
        word_count()
    if event in ('About',):
        about_me()
    if event in 'Clear':
        window['_BODY_'].update(value="")
        window['_INFO_'].update(value='> New File <')
