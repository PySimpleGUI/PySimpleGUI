#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

sg.ChangeLookAndFeel('SandyBeach')    
sg.SetOptions (font = ('Calibri', 12, 'bold'))



layout0 = [[sg.ReadButton('Show/Hide window1'),sg.ReadButton('Show/Hide window2')]]
    
layout1 =[[ sg.Text('window1')], [sg.Multiline( size = (35, 10))]]
layout2 =[[ sg.Text('window2')], [sg.Multiline( size = (35, 10))]]
window0 = sg.Window('Home Window', location = (400, 150)).Layout(layout0)

window1 = sg.Window('Window1', location = (400, 250)).Layout(layout1).Finalize()
window1.Hide()
w1 = False

window2 = sg.Window('Window2', location = (800, 250)).Layout(layout2).Finalize()
window2.Hide()
w2 = False
           
while True:
    button, v = window0.Read()
    if button is not None:
        if button =='Show/Hide window1':
            if w1 == True:
                window1.Hide()
                w1 = False
            else:
                window1.UnHide()
                w1=True
        if button =='Show/Hide window2':
            if w2 == True:
                window2.Hide()
                w2 = False
            else:
                window2.UnHide()
                w2=True
    else:
        break


    
