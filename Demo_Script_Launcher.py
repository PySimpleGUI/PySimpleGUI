#!/usr/bin/env python
import sys
if sys.version_info[0] < 3:
    import PySimpleGUI27 as sg
else:
    import PySimpleGUI as sg
import glob
import ntpath
import subprocess

LOCATION_OF_YOUR_SCRIPTS = ''

# Execute the command.  Will not see the output from the command until it completes.
def execute_command_blocking(command, *args):
    expanded_args = []
    for a in args:
        expanded_args.append(a)
        # expanded_args += a
    try:
        sp = subprocess.Popen([command,expanded_args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except:
        out = ''
    return out

# Executes command and immediately returns.  Will not see anything the script outputs
def execute_command_nonblocking(command, *args):
    expanded_args = []
    for a in args:
        expanded_args += a
    try:
        sp = subprocess.Popen([command,expanded_args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except: pass

def Launcher2():
    sg.ChangeLookAndFeel('GreenTan')
    window = sg.Window('Script launcher')

    filelist = glob.glob(LOCATION_OF_YOUR_SCRIPTS+'*.py')
    namesonly = []
    for file in filelist:
        namesonly.append(ntpath.basename(file))

    layout =  [
                [sg.Listbox(values=namesonly, size=(30, 19), select_mode=sg.SELECT_MODE_EXTENDED, key='demolist'), sg.Output(size=(88, 20), font='Courier 10')],
                [sg.Checkbox('Wait for program to complete', default=False, key='wait')],
                [sg.ReadButton('Run'), sg.ReadButton('Shortcut 1'), sg.ReadButton('Fav Program'), sg.Button('EXIT')],
                ]

    window.Layout(layout)

    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        (button, value) = window.Read()
        if button in ('EXIT', None):
            break           # exit button clicked
        if button in ('Shortcut 1', 'Fav Program'):
            print('Quickly launch your favorite programs using these shortcuts')
            print('Or  copy files to your github folder.  Or anything else you type on the command line')
            # copyfile(source, dest)
        elif button is 'Run':
            for index, file in enumerate(value['demolist']):
                print('Launching %s'%file)
                window.Refresh()          # make the print appear immediately
                if value['wait']:
                    execute_command_blocking(LOCATION_OF_YOUR_SCRIPTS + file)
                else:
                    execute_command_nonblocking(LOCATION_OF_YOUR_SCRIPTS + file)


if __name__ == '__main__':
    Launcher2()

