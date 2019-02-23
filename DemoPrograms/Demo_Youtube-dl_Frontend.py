#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import subprocess

"""
Simple wrapper for youtube-dl.exe. 
Paste the youtube link into the GUI. The GUI link is queried when you click Get List.
Get List will populate the pulldown list with the language options available for the video.
Choose the language to download and click Download
"""

def DownloadSubtitlesGUI():
    sg.ChangeLookAndFeel('Dark')

    combobox = sg.InputCombo(values=['',], size=(10,1), key='lang')
    layout =  [
                [sg.Text('Subtitle Grabber', size=(40, 1), font=('Any 15'))],
                [sg.T('YouTube Link'),sg.In(default_text='',size=(60,1), key='link', do_not_clear=True) ],
                [sg.Output(size=(90,20), font='Courier 12')],
                [sg.ReadButton('Get List')],
                [sg.T('Language Code'), combobox, sg.ReadButton('Download')],
                [sg.Button('Exit', button_color=('white', 'firebrick3'))]
                ]

    window = sg.Window('Subtitle Grabber launcher', text_justification='r', default_element_size=(15,1), font=('Any 14')).Layout(layout)

    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        event, values = window.Read()
        if event in ('Exit', None):
            break           # exit button clicked
        link = values['link']
        if event == 'Get List':
            print('Getting list of subtitles....')
            window.Refresh()
            command = [f'C:/Python/PycharmProjects/GooeyGUI/youtube-dl --list-subs {link}',]
            output = ExecuteCommandSubprocess(command, wait=True, quiet=True)
            lang_list = [o[:5].rstrip() for o in output.split('\n') if 'vtt' in o]
            lang_list = sorted(lang_list)
            combobox.Update(values=lang_list)
            print('Done')

        elif event is 'Download':
            lang = values['lang']
            if lang is '':
                lang = 'en'
            print(f'Downloading subtitle for {lang}...')
            window.Refresh()
            command = (f'C:/Python/PycharmProjects/GooeyGUI/youtube-dl --sub-lang {lang} --write-sub {link}',)
            ExecuteCommandSubprocess(command, wait=True)
            print('Done')


def ExecuteCommandSubprocess(command, wait=False, quiet=True, *args):
    try:
        sp = subprocess.Popen([command,*args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if wait:
            out, err = sp.communicate()
            if not quiet:
                if out:
                    print(out.decode("utf-8"))
                if err:
                    print(err.decode("utf-8"))
    except: return ''

    return (out.decode('utf-8'))


if __name__ == '__main__':
    DownloadSubtitlesGUI()

