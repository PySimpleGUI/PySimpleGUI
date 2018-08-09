import PySimpleGUI as sg

def GetFilesToCompare():
    with sg.FlexForm('File Compare') as form:
        form_rows = [[sg.Text('Enter 2 files to comare')],
                     [sg.Text('File 1', size=(15, 1)), sg.InputText(), sg.FileBrowse()],
                     [sg.Text('File 2', size=(15, 1)), sg.InputText(), sg.FileBrowse()],
                     [sg.Submit(), sg.Cancel()]]
        rc = form.LayoutAndShow(form_rows)
    return rc

def main():
    button, (f1, f2) = GetFilesToCompare()
    if any((button != 'Submit', f1 =='', f2 == '')):
        sg.MsgBoxError('Operation cancelled')
        exit(69)

    with open(f1, 'rb') as file1:
        with open(f2, 'rb') as file2:
            a = file1.read()
            b = file2.read()

        for i, x in enumerate(a):
            if x != b[i]:
                sg.MsgBox('Compare results for files', f1, f2, '**** Mismatch at offset {} ****'.format(i))
                break
        else:
            if len(a) == len(b):
                sg.MsgBox('**** The files are IDENTICAL ****')


if __name__ == '__main__':
    main()
