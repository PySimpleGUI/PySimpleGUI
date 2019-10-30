import PySimpleGUIWeb as sg

# Basic example of PSGWeb

def main():
    layout = [
        [sg.Text('This is a text element')],
        [sg.Input()],
        [sg.Combo(['Combo 1'])],
        [sg.Text('If you close the browser tab, the app will exit gracefully')],
        [sg.InputText('Source')],
        [sg.InputText('Dest')],
        [sg.Ok(), sg.Cancel()]
    ]

    window = sg.Window('Demo window..', layout)
    i = 0
    while True:
        event, values = window.read(timeout=1)
        if event != sg.TIMEOUT_KEY:
            print(event, values)
        if event is None:
            break
        i += 1
    window.close()

main()
print('Program terminating normally')
