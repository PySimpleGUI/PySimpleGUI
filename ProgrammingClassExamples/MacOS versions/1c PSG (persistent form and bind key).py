#PySimple examples (v 3.8)
#Tony Crewe
#Oct 2018 MacOs

import PySimpleGUI as sg

sg.SetOptions (background_color = 'LightBlue',
            element_background_color = 'LightBlue',
            text_element_background_color = 'LightBlue',
               font = ('Arial', 12, 'bold'),
               text_color = 'Blue',
               input_text_color ='Blue',
               button_color = ('Blue', 'White')
               )
#update (via list) values and and display answers
#value[0] is celcius input, value[1] is input to place result.
#Use ReadButton with while true: - keeps window open.

layout = [ [sg.Text('Enter a Temperature in Celcius')],
    [sg.Text('Celcius', size =(8,1)), sg.InputText(size = (15,1))],
    [sg.Text('Result', size =(8,1)), sg.InputText(size = (15,1))],
    [sg.ReadButton('Submit', bind_return_key = True)]]
#Return = button press
window = sg.Window('Converter').Layout(layout) 

while True:
    #get result
    button, value = window.Read()
    #break out of loop is button not pressed.
    if button is not None:         
        fahrenheit = round(9/5*float(value[0]) +32, 1)
        #put result in 2nd input box
        window.FindElement(1).Update(fahrenheit)                  
    else:
        break
