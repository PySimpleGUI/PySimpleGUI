#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

sg.SetOptions (font =('Calibri',12,'bold'))    
              
layout =[[sg.Text('Search Demo', font =('Calibri', 18, 'bold')), sg.ReadButton('Show Names')],
[sg.Text('',size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color ='White',key = 'display1'),
 sg.Text('',size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color ='White',key = 'display2')],
         [sg.Text('_'*32,font = ('Calibri', 12))],
         [sg.InputText(size = (14,1), key = 'linear'), sg.InputText(size = (14,1), key = 'binary')],
          [sg.ReadButton('Linear Search', size = (13,1),key = 'ls'), sg.ReadButton('Binary Search', size = (14,1),key='bs')],
         ]
window = sg.Window('Search Demo').Layout(layout)
window.Finalize()                                   #finalize allows the disabling 
window.FindElement('ls').Update(disabled=True)      #of the two buttons 
window.FindElement('bs').Update(disabled=True)

#names for Demo, could be loaded from a file
Names = ['Roberta', 'Kylie', 'Jenny', 'Helen',
        'Andrea', 'Meredith','Deborah','Pauline',
        'Belinda', 'Wendy']

SortedNames = ['Andrea','Belinda','Deborah','Helen',
               'Jenny','Kylie','Meredith','Pauline',
            'Roberta','Wendy']

#function to display list
def displayList(List, display):
    names = ''
    for l in List:                #add list elements with new line
        names = names + l + '\n'
    window.FindElement(display).Update(names)
    window.FindElement('ls').Update(disabled=False)     #enable buttons now
    window.FindElement('bs').Update(disabled=False)     #now data loaded
    
#Linear Search - no need for Ordered list
def linearSearch():
    L = Names[:]
    found = False
    for l in L:
        if l == value['linear']:             #Check each value
            found = True
            window.FindElement('display1').Update('Linear search\n' + l + ' found.')
            break
    if not found:
        window.FindElement('display1').Update(value['linear'] + ' was \nNot found')

#Binary Search - only works for ordered lists      
def binarySearch():
    L = SortedNames[:]                                 
    lo = 0
    hi = len(L)-1
    found = False                   #Start with found is Flase
    while lo <= hi:
        mid = (lo + hi) //2         #Start in middle
        if L[mid] == value['binary']:    #get the value from the search box
            window.FindElement('display2').Update('Binary search\n' + L[mid] + ' found.')
            found = True            #If found display
            break                   #and stop
        elif L[mid] < value['binary']:
            lo = mid + 1            #Search in top half
        else:
            hi = mid - 1            #Search in lower half
    if not found:                   #If we get to end  - display not found
        window.FindElement('display2').Update(value['binary'] + ' was \nNot found')

while True:
    button, value = window.Read() 
    if button is not None:  
        if button == 'Show Names':  #show names - unordered and sorted
            displayList(Names,'display1')
            displayList(SortedNames, 'display2')
        if button == 'ls':   #Find and display
            linearSearch()
        if button == 'bs':   #Find and display
            binarySearch()
    else:
        break  

