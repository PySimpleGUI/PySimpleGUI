#PySimple examples (v 3.9)
#Tony Crewe
#Oct 2018 MacOS

import PySimpleGUI as sg

#Can use a variety of themes - plus individual options
#Not on MacOS
#sg.ChangeLookAndFeel('SandyBeach')
#use set Options see previous
sg.SetOptions (font = ('Calbri', 12, 'bold'))
            

layout = [ [sg.Text('Enter a Temperature in Celcius')],
    [sg.Text('Celcius', size =(8,1)), sg.InputText(size = (6,1),key = '_input_')],
    [sg.Text('Result', size =(8,1)), sg.InputText(size = (6,1),key = '_result_')],
    [sg.ReadButton('Submit', bind_return_key = True)]]  

window = sg.Window('Temp Converter').Layout(layout) 

while True:
    button, value = window.Read() 
    if button is not None:        
        #catch program errors for text, floats or blank entry:
        #Also validation for range [0, 50]
        try:
            if float(value['_input_']) > 50 or float(value['_input_']) <0:
                sg.Popup('Error','Out of range')
            else:
                fahrenheit = round(9/5*int(value['_input_']) +32, 1)
                window.FindElement('_result_').Update(fahrenheit)
        except ValueError:
                sg.Popup('Error','Please try again')        
       
    else:
        break
