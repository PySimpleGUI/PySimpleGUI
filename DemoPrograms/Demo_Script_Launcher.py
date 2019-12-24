#!/usr/bin/env python
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
        sp = subprocess.Popen([command, expanded_args], shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
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
        sp = subprocess.Popen([command, expanded_args], shell=True,
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except:
        pass


def Launcher2():
    sg.theme('GreenTan')

    filelist = glob.glob(LOCATION_OF_YOUR_SCRIPTS+'*.py')
    namesonly = []
    for file in filelist:
        namesonly.append(ntpath.basename(file))

    layout = [
        [sg.Listbox(values=namesonly, size=(30, 19),
                    select_mode=sg.SELECT_MODE_EXTENDED, key='demolist'),
         sg.Output(size=(88, 20), font='Courier 10')],
        [sg.CBox('Wait for program to complete', default=False, key='wait')],
        [sg.Button('Run'), sg.Button('Shortcut 1'), sg.Button('Fav Program'), sg.Button('EXIT')],
    ]

    window = sg.Window('Script launcher', layout)

    # ---===--- Loop taking in user input  --- #
    while True:
        event, values = window.read()
        if event in ('EXIT', None):
            break           # exit button clicked
        if event in ('Shortcut 1', 'Fav Program'):
            print('Quickly launch your favorite programs using these shortcuts')
            print('''
                Or  copy files to your github folder.
                Or anything else you type on the command line''')
            # copyfile(source, dest)
        elif event == 'Run':
            for index, file in enumerate(values['demolist']):
                print('Launching %s' % file)
                window.refresh()          # make the print appear immediately
                if values['wait']:
                    execute_command_blocking(LOCATION_OF_YOUR_SCRIPTS + file)
                else:
                    execute_command_nonblocking(
                        LOCATION_OF_YOUR_SCRIPTS + file)

    window.close()


if __name__ == '__main__':
    Launcher2()
