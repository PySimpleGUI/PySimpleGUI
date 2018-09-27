#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

#Can use a variety of themes - plus individual options
sg.ChangeLookAndFeel('SandyBeach')    
sg.SetOptions (font = ('Arial', 10, 'bold'))
            

layout = [ [sg.Text('Enter a Temperature in Celcius')],
    [sg.Text('Celcius', size =(8,1)), sg.InputText(size = (15,1),key = 'input')],
    [sg.Text('Result', size =(8,1)), sg.InputText(size = (15,1),key = 'result')],
    [sg.ReadButton('Submit', bind_return_key = True)]]  

window = sg.FlexForm('Temp Converter').Layout(layout) 

while True:
    button, value = window.Read() 
    if button is not None:        
        #catch program errors for text, floats or blank entry:
        #Also validation for range [0, 50]
        try:
            if float(value['input']) > 50 or float(value['input']) <0:
                sg.Popup('Error','Out of range')
            else:
                fahrenheit = round(9/5*int(value['input']) +32, 1)
                window.FindElement('result').Update(fahrenheit)  #put result in text box
        except ValueError:
                sg.Popup('Error','Please try again')             #display error
       
    else:
        break
