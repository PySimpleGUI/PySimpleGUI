#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

sg.SetOptions (font =('Calibri',12,'bold'))

#names for Demo, could be loaded from a file

names = ['Roberta', 'Kylie', 'Jenny', 'Helen',
        'Andrea', 'Meredith','Deborah','Pauline',
        'Belinda', 'Wendy']
name = ''
for l in names:
    name = name + l + '\n'
    
sorted_names = ['Andrea','Belinda','Deborah','Helen',
               'Jenny','Kylie','Meredith','Pauline',
            'Roberta','Wendy']

sortname = ''
for l in sorted_names:
    sortname = sortname + l +'\n'
    
layout =[[sg.Text('Search Demo', font =('Calibri', 18, 'bold'))],
[sg.Text(name, size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color = 'White',key = '_display1_'),
 sg.Text(sortname, size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color = 'White',key = '_display2_')],
         [sg.Text('_'*32,font = ('Calibri', 12))],
         [sg.InputText(size = (14,1), key = '_linear_'), sg.InputText(size = (14,1), key = '_binary_')],
          [sg.ReadButton('Linear Search', size = (13,1)), sg.ReadButton('Binary Search', size = (14,1))],
         ]
window = sg.Window('Search Demo').Layout(layout)
   
#Linear Search - no need for Ordered list
def linear_search():
    l = names[:]
    found = False
    for l in l:
        if l == value['_linear_']:            
            found = True
            sg.Popup('Linear search\n' + l + ' found.')
            break
    if not found:
        sg.Popup('Linear search\n' +(value['_linear_'] + ' was not found'))

#Binary Search - only works for ordered lists      
def binary_search():
    l = sorted_names[:]                                 
    lo = 0
    hi = len(l)-1
    found = False           
    while lo <= hi:
        mid = (lo + hi) //2     
        if l[mid] == value['_binary_']:    
            sg.Popup('Binary search\n' + l[mid] + ' found.')
            found = True            
            break                   
        elif l[mid] < value['_binary_']:
            lo = mid + 1            
        else:
            hi = mid - 1            
    if not found:           
        sg.Popup('Binary search\n' +(value['_binary_'] + ' was not found'))

while True:
    button, value = window.Read() 

    if button is not None:  
        if button == 'Linear Search':
            linear_search()
        if button == 'Binary Search':
            binary_search()
    else:
        break  

