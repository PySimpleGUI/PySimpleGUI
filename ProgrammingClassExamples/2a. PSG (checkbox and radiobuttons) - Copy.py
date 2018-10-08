#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

#Set colour scheme and font
sg.ChangeLookAndFeel('GreenTan')                
sg.SetOptions (font =('Calibri',12,'bold')) 



#One checkbox and three radio buttons (grouped as 'Radio1')
#value[0] - checkbox, Value[1-3] radiobutton selection
layout = [[sg.Text('Membership Calculator', font = ('Calibri', 16, 'bold'))],
          [sg.Checkbox(' Student? 10% off', size = (25,1)),      
           sg.ReadButton('Display Cost', size = (14,1))],
          [sg.Radio('1 month $50', 'Radio1', default = True), 
          sg.Radio('3 months $100', 'Radio1'),                
        sg.Radio('1 year $300', 'Radio1')],                    
          [sg.Text('', size = (30,1), justification = 'center', font =('Calibri', 16, 'bold'),  key = 'result')]]

window = sg.Window('Gym Membership').Layout(layout)

while True:
    button, value = window.Read()
    if button is not None:
        if value[1]:
            cost = 50
        elif value[2]:
            cost = 100
        else:
            cost = 300
        if value[0]:
            #apply discount
            cost = cost*0.9         

        #format as currency $ symbol and 2 d.p. - make a string
        result = str(' Cost: ' + '${:.2f}'.format(cost))
         #put the result in Textbox
        window.FindElement('result').Update(result)           

    else:
        break
