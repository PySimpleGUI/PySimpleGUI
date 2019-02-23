#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

#Set formatting options for all elements rather than individually.
sg.SetOptions (background_color = 'LightBlue',
            element_background_color = 'LightBlue',
            text_element_background_color = 'LightBlue',
               font = ('Arial', 10, 'bold'),
               text_color = 'Blue',
               input_text_color ='Blue',
               button_color = ('White', 'Blue')
               )
#adjust widths
layout = [
   [sg.Text('Celcius', size =(12,1)), sg.InputText(size = (8,1))],
    [sg.Submit()]
   ]

window = sg.Window('Converter').Layout(layout)   
button, value = window.Read()
if button is None:
    #windows was closed without button being pressed
    exit(0)
fahrenheit = round(9/5*float(value[0]) +32, 1)
result = 'Temperature in Fahrenheit is: ' + str(fahrenheit)
sg.Popup('Result',result)







        

    
