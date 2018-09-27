#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg
sg.SetOptions(font= ('Calibri', 12, 'bold'))       

layout = [
    [sg.Text('Spinner and Combo box demo', font = ('Calibri', 14, 'bold'))],
    [sg.Spin([sz for sz in range (-9,10)], initial_value = 0),
    sg.Spin([sz for sz in range (-9,10)], initial_value = 0),
    sg.Text('Pick operation', size = (13,1)),
    sg.InputCombo(['Add','Subtract','Multiply','Divide'], size = (8,6))],
    [sg.Text('Result:   ')],[sg.InputText(size = (6,1), key = 'result'),
     sg.ReadButton('Calculate', button_color = ('White', 'Red'))]]

window = sg.Window('Enter & Display Data', grab_anywhere=False).Layout(layout)

while True:
    button, value = window.Read()

    if button is not None:
        val = [int(value[0]), int(value[1])]
        if value[2] == 'Add':
            result = val[0] + val[1]
        elif value[2] == 'Multiply':
            result = val[0] * val[1]
        elif value[2] == 'Subtract':
            result = val[0] - val[1]
        elif value[2] == 'Divide':
            if val[1] ==0:
                sg.Popup('Second value can\'t be zero')
                result = 'NA'
            else:
                result = round( val[0] / val[1], 3)
        window.FindElement('result').Update(result)              
    else:
        break  
