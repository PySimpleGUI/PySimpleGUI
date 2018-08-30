import PySimpleGUI as sg
import glob
import ntpath
import subprocess

LOCATION_OF_YOUR_SCRIPTS = 'C:/Python/PycharmProjects/GooeyGUI/'

def Launcher1():

    form = sg.FlexForm('Script launcher')

    layout =  [
                [sg.Text('Script output....', size=(40, 1))],
                [sg.Output(size=(88, 20), font='Courier 10')],
                [sg.ReadFormButton('script1'), sg.ReadFormButton('script2'), sg.SimpleButton('EXIT')],
                [sg.Text('Manual command', size=(15,1)), sg.InputText(focus=True), sg.ReadFormButton('Run', bind_return_key=True)]
              ]

    form.Layout(layout)

    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        (button, value) = form.Read()
        if button == 'EXIT' or button is None:
            break           # exit button clicked
        if button == 'script1':
            execute_command_blocking('pip', 'list')
        elif button == 'script2':
            execute_command_blocking('python', '--version')
        elif button == 'Run':
            execute_command_blocking(value[0])      # send string without carriage return on end


# Execute the command.  Will not see the output from the command until it completes.
def execute_command_blocking(command, *args):
    try:
        sp = subprocess.Popen([command,*args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except: pass

# Executes command and immediately returns.  Will not see anything the script outputs
def execute_command_nonblocking(command, *args):
    try:
        sp = subprocess.Popen([command,*args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except: pass

def Launcher2():
    sg.ChangeLookAndFeel('GreenTan')
    form = sg.FlexForm('Script launcher')

    filelist = glob.glob(LOCATION_OF_YOUR_SCRIPTS+'*.py')
    namesonly = []
    for file in filelist:
        namesonly.append(ntpath.basename(file))

    layout =  [
                [sg.Text('Script output....', size=(40, 1))],
                [sg.Listbox(values=namesonly, size=(30, 19), select_mode=sg.SELECT_MODE_EXTENDED, key='demolist'), sg.Output(size=(88, 20), font='Courier 10')],
                [sg.ReadFormButton('Run'), sg.ReadFormButton('Shortcut 1'), sg.ReadFormButton('Fav Program'), sg.SimpleButton('EXIT')],
                ]

    form.Layout(layout)

    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        (button, value) = form.Read()
        if button in ('EXIT', None):
            break           # exit button clicked
        if button in ('Shortcut 1', 'Fav Program'):
            print('Quickly launch your favorite programs using these shortcuts')
            print('Or  copy files to your github folder.  Or anything else you type on the command line')
            # copyfile(source, dest)
        elif button is 'Run':
            for index, file in enumerate(value['demolist']):
                print('Launching %s'%file)
                form.Refresh()          # make the print appear immediately
                execute_command_nonblocking(LOCATION_OF_YOUR_SCRIPTS + file)


if __name__ == '__main__':
    Launcher2()

