import PySimpleGUI as sg
#pip install PyInstaller
#windows command prompt pyinstaller -wF 2b_makewinexe_file.py
#must CD to directory where py file is

sg.ChangeLookAndFeel('GreenTan')                #Set colour scheme
sg.SetOptions (font =('Calibri',12,'bold')  )   #and font

form = sg.FlexForm('Gym Membership')


layout = [[sg.Text('Membership Calculator', font = ('Calibri', 16, 'bold'))],
          [sg.Checkbox('CGS student?', size = (22,1)),      #value[0]
           sg.ReadButton('Display Cost', size = (14,1))],
          [sg.Radio('One Month', 'Radio1', default = True), #value[1]
          sg.Radio('Three Month', 'Radio1'),                #value[2]
        sg.Radio('One Year', 'Radio1')],                    #value[3]
          [sg.Text('', size = (30,1), justification = 'center', font =('Calibri', 16, 'bold'),  key = 'result')]]

form.Layout(layout)
while True:
    button, value = form.Read()
    if button is not None:
        if value[1]:
            cost = 50
        elif value[2]:
            cost = 100
        else:
            cost = 300
        if value[0]:
            cost = cost*0.9
        result = str(' Cost: ' + '${:.2f}'.format(cost))    #format as currency - make a string
        form.FindElement('result').Update(result)           #put the result in Textbox

    else:
        break
