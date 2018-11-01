#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

import subprocess
import os


"""
    Demo_Toolbar - A floating toolbar with quick launcher
    
    One cool PySimpleGUI demo. Shows borderless windows, grab_anywhere, tight button layout
    You can setup a specific program to launch when a button is clicked, or use the
    Combobox to select a .py file found in the root folder, and run that file.
    
"""

ROOT_PATH = './'

def Launcher():

    # def print(line):
    #     window.FindElement('output').Update(line)

    sg.ChangeLookAndFeel('Dark')

    namesonly = [f for f in os.listdir(ROOT_PATH) if f.endswith('.py') ]

    if len(namesonly) == 0:
        namesonly = ['test 1', 'test 2', 'test 3']

    sg.SetOptions(element_padding=(0,0), button_element_size=(12,1), auto_size_buttons=False)

    layout =  [[sg.Combo(values=namesonly, size=(35,30), key='demofile'),
                sg.ReadButton('Run', button_color=('white', '#00168B')),
                sg.ReadButton('Program 1'),
                sg.ReadButton('Program 2'),
                sg.ReadButton('Program 3', button_color=('white', '#35008B')),
                sg.Button('EXIT', button_color=('white','firebrick3'))],
                [sg.T('', text_color='white', size=(50,1), key='output')]]

    window = sg.Window('Floating Toolbar', no_titlebar=True, grab_anywhere=True, keep_on_top=True).Layout(layout)


    # ---===--- Loop taking in user input and executing appropriate program --- #
    while True:
        (event, values) = window.Read()
        if event == 'EXIT' or event is None:
            break           # exit button clicked
        if event == 'Program 1':
            print('Run your program 1 here!')
        elif event == 'Program 2':
            print('Run your program 2 here!')
        elif event == 'Run':
            file = values['demofile']
            print('Launching %s'%file)
            ExecuteCommandSubprocess('python', os.path.join(ROOT_PATH, file))
        else:
            print(event)

def ExecuteCommandSubprocess(command, *args, wait=False):
    try:
        if sys.platform == 'linux':
            arg_string = ''
            arg_string = ' '.join([str(arg) for arg in args])
            # for arg in args:
            #     arg_string += ' ' + str(arg)
            print('python3 ' + arg_string)
            sp = subprocess.Popen(['python3 ', arg_string ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            arg_string = ' '.join([str(arg) for arg in args])
            sp = subprocess.Popen([command, arg_string], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # sp = subprocess.Popen([command, list(args)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if wait:
            out, err = sp.communicate()
            if out:
                print(out.decode("utf-8"))
            if err:
                print(err.decode("utf-8"))
    except: pass



if __name__ == '__main__':
    Launcher()

