#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

sg.SetOptions (background_color = 'LightBlue',
            element_background_color = 'LightBlue',
            text_element_background_color = 'LightBlue',
               font = ('Arial', 10, 'bold'),
               text_color = 'Blue',
               input_text_color ='Blue',
               button_color = ('White', 'Blue')
               )
#name inputs (key) uses dictionary- easy to see updating of results
#value[input] first input value te c...
layout = [ [sg.Text('Enter a Temperature in Celcius')],
    [sg.Text('Celcius', size =(8,1)), sg.InputText(size = (15,1),key = 'input')],
    [sg.Text('Result', size =(8,1)), sg.InputText(size = (15,1),key = 'result')],
    [sg.ReadButton('Submit', bind_return_key = True)]]  

window = sg.FlexForm('Temp Converter').Layout(layout) 

while True:
    button, value = window.Read() 
    if button is not None:        
        #catch program errors for text or blank entry:
        try:
            fahrenheit = round(9/5*float(value['input']) +32, 1)
            window.FindElement('result').Update(fahrenheit)     #put result in text box
        except ValueError:
            sg.Popup('Error','Please try again')                #display error
       
    else:
        break
