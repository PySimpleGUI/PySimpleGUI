import PySimpleGUI as sg
import subprocess
import os
import sys

"""
    Demo_Toolbar - A floating toolbar with quick launcher
    
    One cool PySimpleGUI demo. Shows borderless windows, grab_anywhere, tight button layout
    You can setup a specific program to launch when a button is clicked, or use the
    Combobox to select a .py file found in the root folder, and run that file.
    
"""

ROOT_PATH = './'

def Launcher():

    def print(line):
        form.FindElement('output').Update(line)

    sg.ChangeLookAndFeel('Dark')

    namesonly = [f for f in os.listdir(ROOT_PATH) if f.endswith('.py') ]

    sg.SetOptions(element_padding=(0,0), button_element_size=(12,1), auto_size_buttons=False)
    layout =  [[sg.Combo(values=namesonly, size=(35,30), key='demofile'),
                sg.ReadFormButton('Run', button_color=('white', '#00168B')),
                sg.ReadFormButton('Program 1'),
                sg.ReadFormButton('Program 2'),
                sg.ReadFormButton('Program 3', button_color=('white', '#35008B')),
                sg.SimpleButton('EXIT', button_color=('white','firebrick3'))],
                [sg.T('', text_color='white', size=(50,1), key='output')]]

    form = sg.FlexForm('Floating Toolbar', no_titlebar=True, keep_on_top=True)

    form.Layout(layout)

    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        (button, value) = form.Read()
        if button is 'EXIT' or button is None:
            break           # exit button clicked
        if button is 'Program 1':
            print('Run your program 1 here!')
        elif button is 'Program 2':
            print('Run your program 2 here!')
        elif button is 'Run':
            file = value['demofile']
            print('Launching %s'%file)
            ExecuteCommandSubprocess('python', os.path.join(ROOT_PATH, file))
        else:
            print(button)

def ExecuteCommandSubprocess(command, *args, wait=False):
    try:
        if sys.platform == 'linux':
            arg_string = ''
            for arg in args:
                arg_string += ' ' + str(arg)
            sp = subprocess.Popen(['python3' + arg_string, ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            sp = subprocess.Popen([command, list(args)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if wait:
            out, err = sp.communicate()
            if out:
                print(out.decode("utf-8"))
            if err:
                print(err.decode("utf-8"))
    except: pass



if __name__ == '__main__':
    Launcher()

