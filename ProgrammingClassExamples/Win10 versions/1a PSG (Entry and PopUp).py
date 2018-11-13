#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

#layout, Text, Input,button on line below
layout = [
   [sg.Text('Celcius'), sg.InputText()],            
    [sg.Submit()],                                
   ]

#setup window with Title
window = sg.Window('Temperature Converter').Layout(layout)

#get value (part of a list)
button, value = window.Read()                  
if button is None:
    #windows was closed without button being pressed
    exit(0)
    
#convert and create string
fahrenheit = round(9/5*float(value[0]) +32, 1)  
result =  'Temperature in Fahrenheit is: ' + str(fahrenheit)
#display in Popup
sg.Popup('Result', result)                     







        

    
