#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

# sg.SetOptions(button_color=sg.COLOR_SYSTEM_DEFAULT)

def GetFilesToCompare():
    form_rows = [[sg.Text('Enter 2 files to comare')],
                 [sg.Text('File 1', size=(15, 1)), sg.InputText(key='file1'), sg.FileBrowse()],
                 [sg.Text('File 2', size=(15, 1)), sg.InputText(key='file2'), sg.FileBrowse(target='file2')],
                 [sg.Submit(), sg.Cancel()]]

    window = sg.Window('File Compare')
    event, values = window.Layout(form_rows).Read()
    return event, values

def main():
    button, values = GetFilesToCompare()
    f1 = values['file1']
    f2 = values['file2']

    if any((button != 'Submit', f1 =='', f2 == '')):
        sg.PopupError('Operation cancelled')
        sys.exit(69)

    # --- This portion of the code is not GUI related ---
    with open(f1, 'rb') as file1:
        with open(f2, 'rb') as file2:
            a = file1.read()
            b = file2.read()

        for i, x in enumerate(a):
            if x != b[i]:
                sg.Popup('Compare results for files', f1, f2, '**** Mismatch at offset {} ****'.format(i))
                break
        else:
            if len(a) == len(b):
                sg.Popup('**** The files are IDENTICAL ****')


if __name__ == '__main__':
    main()
