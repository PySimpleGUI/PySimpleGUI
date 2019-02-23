#PySimple examples (v 3.9)
#Tony Crewe
#Oct 2018 MacOs

import PySimpleGUI as sg
import os                       #to work with windows OS

#sg.ChangeLookAndFeel('GreenTan')

sg.SetOptions(background_color = 'LightBlue',
            element_background_color = 'LightBlue',
            text_element_background_color = 'LightBlue',
              font= ('Calibri', 14, 'bold'))   

layout = [
    [sg.Text('Enter a Name and four Marks')],
    [sg.Text('Name:', size =(8,1)), sg.InputText(size = (10,1), key = '_name_')],
     [sg.Text('Mark1:', size =(8,1)), sg.InputText(size = (5,1), key = '_m1_')],
         [sg.Text('Mark2:', size =(8,1)), sg.InputText(size = (5,1), key = '_m2_')],
         [sg.Text('Mark3:', size =(8,1)), sg.InputText(size = (5,1), key = '_m3_')],
         [sg.Text('Mark4:', size =(8,1)), sg.InputText(size = (5,1), key = '_m4_')],
    [sg.ReadButton('Save', size = (6,1),key = '_save_'),  sg.Text('Press to Save to file')],
    [sg.ReadButton('Display',size = (6,1), key = '_display_'), sg.Text('To retrieve and Display')],
    [sg.Multiline(size = (24,4), key = '_multiline_', pad = (2,15))]]

window = sg.Window('Simple Average Finder').Layout(layout)   


while True:
    button, value = window.Read()   #value is a dictionary holding name and marks (4)
    if button is not None:  
        #initialise variables
        total = 0.0
        index = ''
        name = value['_name_']
        #get pathname to current file
        dirname, filename = os.path.split(os.path.abspath(__file__))
        #add desired file name for saving to path
        pathname = os.path.join(dirname , 'results.txt' )             
        #generic catch error - blanks or wrong data types
        try:
            if button == '_save_':
                for i in range (1,5):
                    index = '_m' + str(i) + '_'         

                    #Check for values between 0 and 100
                    if float(value[index])  < 0 or float(value[index]) >100:
                        sg.Popup('Out of Range', 'Enter Marks between 0 and 100')
                    else:
                        total += float(value[index])
                        average = total/4
                        f = open(pathname, 'w')         
                        print (name, file = f)
                        print (total, file = f)
                        print (average, file = f)
                        f.close()
        except ValueError:
            sg.Popup('Error','Check entries and try again') 
            
        if button == '_display_':
            #This loads the file line by line into a list called data.
            #the strip() removes whitespaces from beginning and end of each line.
            try:
                data = [line.strip() for line in open(pathname)]
                #create single string to display in multiline object.
                string = 'Name:  ' + data[0] +'\nTotal:  ' + str(data[1]) + '\nAverage:  ' + str(data[2])
                window.FindElement('_multiline_').Update(string)
            except:
                sg.PopupError('Error', 'Problem finding or reading file') 
    else:
        break  

