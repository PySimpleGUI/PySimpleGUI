#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

layout = [
   [sg.Text('Celcius'), sg.InputText()],            #layout, Text, Input
    [sg.Submit()],                                  #button on line below
   ]

#setup window with Title
window = sg.Window('Temperature Converter').Layout(layout)

button, value = window.Read()                   #get value (part of a list)

fahrenheit = round(9/5*float(value[0]) +32, 1)  #convert and create string
result =  'Temperature in Fahrenheit is: ' + str(fahrenheit)
sg.Popup('Result', result)                      #display in Popup







        

    
