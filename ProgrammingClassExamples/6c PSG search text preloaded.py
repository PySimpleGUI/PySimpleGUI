#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

sg.SetOptions (font =('Calibri',12,'bold'))

#names for Demo, could be loaded from a file

Names = ['Roberta', 'Kylie', 'Jenny', 'Helen',
        'Andrea', 'Meredith','Deborah','Pauline',
        'Belinda', 'Wendy']
names = ''
for l in Names:
    names = names + l + '\n'
    
SortedNames = ['Andrea','Belinda','Deborah','Helen',
               'Jenny','Kylie','Meredith','Pauline',
            'Roberta','Wendy']

sortnames = ''
for l in SortedNames:
    sortnames = sortnames + l +'\n'
    
layout =[[sg.Text('Search Demo', font =('Calibri', 18, 'bold'))],
[sg.Text(names,size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color ='White',key = 'display1'),
 sg.Text(sortnames,size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color ='White',key = 'display2')],
         [sg.Text('_'*32,font = ('Calibri', 12))],
         [sg.InputText(size = (14,1), key = 'linear'), sg.InputText(size = (14,1), key = 'binary')],
          [sg.ReadButton('Linear Search', bind_return_key=True, size = (13,1)), sg.ReadButton('Binary Search', size = (14,1))],
         ]
window = sg.Window('Search Demo').Layout(layout)
   
#Linear Search - no need for Ordered list
def linearSearch():
    L = Names[:]
    found = False
    for l in L:
        if l == value['linear']:             #Check each value
            found = True
            sg.Popup('Linear search\n' + l + ' found.')
            break
    if not found:
        sg.Popup('Linear search\n' +(value['linear'] + ' was not found'))

#Binary Search - only works for ordered lists      
def binarySearch():
    L = SortedNames[:]                                 
    lo = 0
    hi = len(L)-1
    found = False                   #Start with found is Flase
    while lo <= hi:
        mid = (lo + hi) //2         #Start in middle
        if L[mid] == value['binary']:    #get the value from the search box
            sg.Popup('Binary search\n' + L[mid] + ' found.')
            found = True            #If found display
            break                   #and stop
        elif L[mid] < value['binary']:
            lo = mid + 1            #Search in top half
        else:
            hi = mid - 1            #Search in lower half
    if not found:                   #If we get to end  - display not found
        sg.Popup('Binary search\n' +(value['binary'] + ' was not found'))

while True:
    button, value = window.Read() 

    if button is not None:  
        if button == 'Show Names':  #show names - unordered and sorted
            displayList(Names,'display1')
            displayList(SortedNames, 'display2')
        if button == 'Linear Search':   #Find and display
            linearSearch()
        if button == 'Binary Search':   #Find and display
            binarySearch()
    else:
        break  

