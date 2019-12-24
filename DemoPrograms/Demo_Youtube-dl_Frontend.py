#!/usr/bin/env python
import sys
import PySimpleGUI as sg
import subprocess

"""
Simple wrapper for youtube-dl.exe.
Paste the youtube link into the GUI. The GUI link is queried when you click Get List.
Get List will populate the pulldown list with the language options available for the video.
Choose the language to download and click Download
"""
youtube_executable = 'path/to/youtube-dl'


def DownloadSubtitlesGUI():
    sg.theme('Dark')

    combobox = sg.Combo(values=['', ], size=(10, 1), key='lang')
    layout = [
        [sg.Text('Subtitle Grabber', size=(40, 1), font=('Any 15'))],
        [sg.Text('YouTube Link'), sg.Input(default_text='', size=(60, 1), key='link')],
        [sg.Output(size=(90, 20), font='Courier 12')],
        [sg.Button('Get List')],
        [sg.Text('Language Code'), combobox, sg.Button('Download')],
        [sg.Button('Exit', button_color=('white', 'firebrick3'))]
    ]

    window = sg.Window('Subtitle Grabber launcher', layout,
                       text_justification='r',
                       default_element_size=(15, 1),
                       font=('Any 14'))

    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        event, values = window.read()
        if event in ('Exit', None):
            break           # exit button clicked
        link = values['link']
        if event == 'Get List':
            print('Getting list of subtitles....')
            window.refresh()
            command = [youtube_executable + f' --list-subs {link}']
            output = ExecuteCommandSubprocess(command, wait=True, quiet=True)
            lang_list = [o[:5].rstrip()
                         for o in output.split('\n') if 'vtt' in o]
            lang_list = sorted(lang_list)
            combobox.update(values=lang_list)
            print('Done')

        elif event == 'Download':
            lang = values['lang'] or 'en'
            print(f'Downloading subtitle for {lang}...')
            window.refresh()
            command = [youtube_executable + f' --sub-lang {lang} --write-sub {link}', ]
            print(ExecuteCommandSubprocess(command, wait=True, quiet=False))
            print('Done')
    window.close()


def ExecuteCommandSubprocess(command, wait=False, quiet=True, *args):
    try:
        sp = subprocess.Popen([command, *args],
                              shell=True,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.PIPE)
        if wait:
            out, err = sp.communicate()
            if not quiet:
                if out:
                    print(out.decode("utf-8"))
                if err:
                    print(err.decode("utf-8"))
    except Exception as e:
        print('Exception encountered running command ', e)
        return ''

    return (out.decode('utf-8'))


if __name__ == '__main__':
    DownloadSubtitlesGUI()
