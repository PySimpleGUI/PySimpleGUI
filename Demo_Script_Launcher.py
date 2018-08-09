import PySimpleGUI as sg
import subprocess

def Launcher():

    form = sg.FlexForm('Script launcher')

    layout =  [
                [sg.Text('Script output....', size=(40, 1))],
                [sg.Output(size=(88, 20))],
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
            ExecuteCommandSubprocess('pip','list')
        elif button == 'script2':
            ExecuteCommandSubprocess('python', '--version')
        elif button == 'Run':
            ExecuteCommandSubprocess(value[0])      # send string without carriage return on end


def ExecuteCommandSubprocess(command, *args):
    try:
        sp = subprocess.Popen([command,*args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = sp.communicate()
        if out:
            print(out.decode("utf-8"))
        if err:
            print(err.decode("utf-8"))
    except: pass


if __name__ == '__main__':
    Launcher()

