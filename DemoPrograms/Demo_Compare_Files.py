#!/usr/bin/env python
import PySimpleGUI as sg

'''
    Simple "diff" in PySimpleGUI
'''

sg.theme('Dark Blue 3')

def GetFilesToCompare():
    form_rows = [[sg.Text('Enter 2 files to comare')],
                 [sg.Text('File 1', size=(15, 1)),
                    sg.InputText(key='-file1-'), sg.FileBrowse()],
                 [sg.Text('File 2', size=(15, 1)), sg.InputText(key='-file2-'),
                  sg.FileBrowse(target='-file2-')],
                 [sg.Submit(), sg.Cancel()]]

    window = sg.Window('File Compare', form_rows)
    event, values = window.read()
    window.close()
    return event, values


def main():

    button, values = GetFilesToCompare()
    f1, f2 = values['-file1-'], values['-file2-']

    if any((button != 'Submit', f1 == '', f2 == '')):
        sg.popup_error('Operation cancelled')
        return

    # --- This portion of the code is not GUI related ---
    with open(f1, 'rb') as file1:
        with open(f2, 'rb') as file2:
            a = file1.read()
            b = file2.read()

        for i, x in enumerate(a):
            if x != b[i]:
                sg.popup('Compare results for files', f1, f2,
                         '**** Mismatch at offset {} ****'.format(i))
                break
        else:
            if len(a) == len(b):
                sg.popup('**** The files are IDENTICAL ****')


if __name__ == '__main__':
    main()
