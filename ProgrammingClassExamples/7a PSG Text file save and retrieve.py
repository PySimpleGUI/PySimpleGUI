#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg
import os                       #to work with windows OS

sg.ChangeLookAndFeel('GreenTan')
sg.SetOptions(font = ('Calibri', 12, 'bold'))

layout = [
    [sg.Text('Enter a Name and four Marks')],
    [sg.Text('Name:', size =(10,1)), sg.InputText(size = (12,1), key = 'name')],
     [sg.Text('Mark1:', size =(10,1)), sg.InputText(size = (6,1), key = 'm1')],
         [sg.Text('Mark2:', size =(10,1)), sg.InputText(size = (6,1), key = 'm2')],
         [sg.Text('Mark3:', size =(10,1)), sg.InputText(size = (6,1), key = 'm3')],
         [sg.Text('Mark4:', size =(10,1)), sg.InputText(size = (6,1), key = 'm4')],
    [sg.ReadButton('Save', size = (8,1),key = 'save'),  sg.Text('Press to Save to file')],
    [sg.ReadButton('Display',size = (8,1), key = 'display'), sg.Text('To retrieve and Display')],
    [sg.Multiline(size = (28,4), key = 'multiline')]]

window = sg.Window('Simple Average Finder').Layout(layout)   


while True:
    button, value = window.Read()   #value is a dictionary holding name and marks (4)
    if button is not None:  
        #initialise variables
        total = 0.0
        index = ''
        Name = value['name']        #get name 
        dirname, filename = os.path.split(os.path.abspath(__file__)) #get pathname to current file
        pathname = dirname + '\\results.txt'                         #add desired file name for saving to path
        
        #needs validation and try/catch error checking, will crash if blank or text entry for marks
        
        if button == 'save':
            for i in range (1,5):
                index = 'm' + str(i)            #create dictionary index m1 ... m4
                total += float(value[index])   
            average = total/4
            f = open(pathname, 'w')                                      #open file and save 
            print (Name, file = f)
            print (total, file = f)
            print (average, file = f)
            f.close()

        #some error checking for missing file needed here
            
        if button == 'display':
            #This loads the file line by line into a list called data.
            #the strip() removes whitespaces from beginning and end of each line.
            data = [line.strip() for line in open(pathname)]
            #create single string to display in multiline object.
            string = 'Name:  ' + data[0] +'\nTotal:  ' + str(data[1]) + '\nAverage:  ' + str(data[2])
            window.FindElement('multiline').Update(string)
    else:
        break  

