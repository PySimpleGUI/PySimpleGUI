#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

sg.ChangeLookAndFeel('BlueMono')

#use column feature with height listbox takes up
column1 = [
    [sg.Text('Add or Delete Items\nfrom a Listbox', font = ('Arial', 12, 'bold'))],
     [sg.InputText( size = (15,1), key = 'add'), sg.ReadButton('Add')],
    [sg.ReadButton('Delete selected entry')]]

List = ['Austalia', 'Canada', 'Greece']         #initial listbox entries

#add initial List  to listbox
layout = [
    [sg.Listbox(values=[l for l in List], size = (30,8), key ='listbox'),
     sg.Column(column1)]]

window = sg.Window('Listbox').Layout(layout)

while True:
    button, value = window.Read()
    if button is not None:
                                                    #value[listbox] returns a list
        if button == 'Delete selected entry':       #using value[listbox][0] give the string
            if value['listbox'] == []:               #ensure something is selected
                sg.Popup('Error','You must select a Country')
            else:
                List.remove(value['listbox'][0])    #find and remove this
        if button == 'Add':
            List.append(value['add'])           #add string in add box to list
        List.sort()                             #sort
        #update listbox
        window.FindElement('listbox').Update(List)
    else:
        break  
