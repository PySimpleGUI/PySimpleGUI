import PySimpleGUI as sg
import os

def Launcher():

    form = sg.FlexForm('Script launcher')

    layout =  [
                [sg.Text('Script output....', size=(40, 1))],
                [sg.Output(size=(88, 20))],
                [sg.ReadFormButton('script1'), sg.ReadFormButton('script2'), sg.SimpleButton('EXIT')]
              ]

    form.Layout(layout)

    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        (button, value) = form.Read()
        if button == 'EXIT' or button is None:
            break           # exit button clicked
        if button == 'script1':
            ExecuteCommandOS('python SimScript.py')
        elif button == 'script2':
            ExecuteCommandOS('python SimScript.py')
        elif button == 'Enter':
            ExecuteCommandOS(value[0])      # send string without carriage return on end


def ExecuteCommandOS(command):
    output = os.popen(command).read()
    print(output)


if __name__ == '__main__':
    Launcher()

