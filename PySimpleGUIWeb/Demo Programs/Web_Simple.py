import PySimpleGUIWeb as sg

def main():
    layout = [
                [sg.Text('This is a text element')],
                [sg.Input()],
                [sg.Combo(['Combo 1'])],
                [sg.Text('If you close the browser tab, the app will exit gracefully')],
                [sg.InputText('Source', do_not_clear=True)],
                [sg.InputText('Dest', do_not_clear=True)],
                [sg.Ok(), sg.Cancel()]
            ]

    window = sg.Window('Demo window..').Layout(layout)
    i = 0
    while True:
        event, values = window.Read(timeout=1)
        if event != sg.TIMEOUT_KEY:
            print(event, values)
        if event is None:
            break
        i += 1
    window.Close()

main()
print('Program terminating normally')