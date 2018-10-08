#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

#use of Column to help with layout - vertical sliders take up space

column1 = [
    [sg.Text('Pick operation', size = (15,1), font = ('Calibri', 12, 'bold'))],
    [sg.InputCombo(['Add','Subtract','Multiply','Divide'], size = (10,6))],
    [sg.Text('', size =(1,4))]]
column2 = [
    [sg.ReadButton('Submit', font = ('Calibri', 12, 'bold'), button_color = ('White', 'Red'))],
    [sg.Text('Result:', font = ('Calibri', 12, 'bold'))],[sg.InputText(size = (12,1), key = '_result_')]
    ]
            

layout = [
    [sg.Text('Slider and Combo box demo', font = ('Calibri', 14,'bold'))],
    [sg.Slider(range = (-9, 9),orientation = 'v', size = (5,20), default_value = 0),
      sg.Slider(range = (-9, 9),orientation = 'v', size = (5, 20), default_value = 0),
      sg.Text('   '), sg.Column(column1), sg.Column(column2)]]

#added grab_anywhere to when moving slider, who window doesn't move.

window = sg.Window('Enter & Display Data',grab_anywhere = False).Layout(layout)

#Get selection from combo: value[2]
#Slider values: value[0] and value[1]
while True:
    button, value = window.Read()
    if button is not None:
        if value[2] == 'Add':
            result = value[0] + value[1]
        elif value[2] == 'Multiply':
            result = value[0] * value[1]
        elif value[2] == 'Subtract':
            result = value[0] - value[1]
        elif value[2] == 'Divide':              #check for zero
            if value[1] ==0:
                sg.Popup('Second value can\'t be zero')
                result = 'NA'
            else:
                result = value[0] / value[1]
        window.FindElement('_result_').Update(result)              
    else:
        break  
