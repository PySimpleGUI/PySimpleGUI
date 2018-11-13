#PySimple examples (v 3.9)
#Tony Crewe
#Oct 2018 MacOs

import PySimpleGUI as sg

    
sg.SetOptions(background_color = 'Grey',
            element_background_color = 'Grey',
            text_element_background_color = 'Grey',
              font= ('Calibri', 14, 'bold'))

layout =[[sg.Text('Search Demo', font =('Calibri', 18, 'bold')), sg.ReadButton('Show Names')],
[sg.Text('',size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color ='White',key = '_display1_'),
 sg.Text('',size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color ='White',key = '_display2_')],
         [sg.Text('_'*35,font = ('Calibri', 16))],
         [sg.InputText(size = (10,1), key = '_linear_'), sg.InputText(size = (11,1), key = '_binary_')],
          [sg.ReadButton('Linear Search', size = (11,1)), sg.ReadButton('Binary Search', size = (11,1))],
         ]
window = sg.Window('Search Demo').Layout(layout)

#names for Demo, could be loaded from a file
names = ['Roberta', 'Kylie', 'Jenny', 'Helen',
        'Andrea', 'Meredith','Deborah','Pauline',
        'Belinda', 'Wendy']

sorted_names = ['Andrea','Belinda','Deborah','Helen',
               'Jenny','Kylie','Meredith','Pauline',
            'Roberta','Wendy']

#function to display list
def display_list(list, display):
    names = ''
    for l in list:                #add list elements with new line
        names = names + l + '\n'
    window.FindElement(display).Update(names)
    
#Linear Search - no need for Ordered list
def linear_search():
    l = names[:]
    found = False
    for l in l:
        if l == value['_linear_']:             #Check each value
            found = True
            window.FindElement('_display1_').Update('Linear search\n' + l + ' found.')
            break
    if not found:
        window.FindElement('_display1_').Update(value['_linear_'] + ' was \nNot found')

#Binary Search - only works for ordered lists      
def binary_search():
    l = sorted_names[:]                                 
    lo = 0
    hi = len(l)-1
    #Start with found is False
    found = False                  
    while lo <= hi:
        #Start in middle
        mid = (lo + hi) //2
        #get the value from the search box
        if l[mid] == value['_binary_']:    
            window.FindElement('_display2_').Update('Binary search\n' + l[mid] + ' found.')
            #If found display name and stop
            found = True           
            break                   
        elif l[mid] < value['_binary_']:
            #Search in top half
            lo = mid + 1            
        else:
            #Search in lower half
            hi = mid - 1
    #If we get to end  - display not found
    if not found:                   
        window.FindElement('_display2_').Update(value['_binary_'] + ' was \nNot found')

while True:
    button, value = window.Read() 

    if button is not None:
        #show names - unordered and sorted
        if button == 'Show Names':  
            display_list(names,'_display1_')
            display_list(sorted_names, '_display2_')
        if button == 'Linear Search':
            linear_search()
        if button == 'Binary Search':
            binary_search()
    else:
        break  

