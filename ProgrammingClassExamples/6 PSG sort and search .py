#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg

sg.SetOptions (font =('Calibri',12,'bold'))    
    

#setup column (called column1) of buttons to sue in layout

column1 = [[sg.ReadButton('Original list', size = (13,1))],
           [sg.ReadButton('Default sort', size = (13,1))],
           [sg.ReadButton('Sort: selection',size = (13,1))],
           [sg.ReadButton('Sort: quick', size = (13,1))]]
           
layout =[[sg.Text('Search and Sort Demo', font =('Calibri', 20, 'bold'))],
[sg.Text('',size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color ='White',key = 'display'), sg.Column(column1)],
         [sg.Text('_'*32,font = ('Calibri', 12))],
         [sg.InputText(size = (13,1), key = 'linear'), sg.Text('  '), sg.InputText(size = (13,1), key = 'binary')],
          [sg.ReadButton('Linear Search', size = (13,1)), sg.Text(' '), sg.ReadButton('Binary Search', size = (13,1))],
         ]

window = sg.Window('Search and Sort Demo').Layout(layout)

#names for Demo, could be loaded from a file
Names= ['Roberta', 'Kylie', 'Jenny', 'Helen',
        'Andrea', 'Meredith','Deborah','Pauline',
        'Belinda', 'Wendy']

#function to display list
def displayList(List):
    global ListDisplayed          #store list in Multiline text globally
    ListDisplayed = List
    display = ''
    for l in List:                #add list elements with new line
        display = display + l + '\n'
    window.FindElement('display').Update(display)
        
#use inbuilt python sort       
def default(Names):
    L = Names[:]
    L.sort()        #inbuilt sort
    displayList(L)

#Selection sort - See Janson Ch 7 
def selSort(Names):
    L = Names[:]
    for i in range(len(L)):
        smallest = i
        for j in range(i+1, len(L)):
            if L[j] < L[smallest]:              #find smallest value
                smallest = j                    #swap it to front 
        L[smallest], L[i] = L[i], L[smallest]   #repeat from next poistion 
    displayList(L)

#Quick sort - See Janson Ch 7
def qsortHolder(Names):                         
    L = Names[:]                                #pass List, first and last
    quick_sort(L, 0, len(L) -1)                 #Start process
    displayList(L)
        
def quick_sort(L, first, last):                 #Quicksort is a partition sort
    if first >= last:
        return L
    pivot = L[first]                           
    low = first                                 
    high = last
    while low < high:
        while L[high] > pivot:
            high = high -1
        while L[low] < pivot:
            low = low + 1
        if low <= high:
            L[high], L[low] = L[low], L[high]
            low = low + 1
            high = high -1
    quick_sort(L, first, low -1)                #continue splitting - sort small lsist
    quick_sort(L, low, last)

#Linear Search - no need for Ordered list
def linearSearch():
    L = Names[:]
    found = False
    for l in L:
        if l == value['linear']:             #Check each value
            found = True
            window.FindElement('display').Update('Linear search\n' + l + ' found.')
            break
    if not found:
        window.FindElement('display').Update(value['linear'] + ' was \nNot found')

#Binary Search - only works fot ordered lists      
def binarySearch():
    L = ListDisplayed[:]              #get List currently in multiline display                    
    lo = 0
    hi = len(L)-1
    found = False                   #Start with found is Flase
    while lo <= hi:
        mid = (lo + hi) //2         #Start in middle
        if L[mid] == value['binary']:    #get the value from the search box
            window.FindElement('display').Update('Binary search\n' + L[mid] + ' found.')
            found = True            #If found display
            break                   #and stop
        elif L[mid] < value['binary']:
            lo = mid + 1            #Search in top half
        else:
            hi = mid - 1            #Search in lower half
    if not found:                   #If we get to end  - display not found
        window.FindElement('display').Update(value['binary'] + ' was \nNot found')

        
while True:
    button, value = window.Read() 
    if button is not None:  
        if button == 'Original list':
            displayList(Names)
        if button == 'Default sort':
            default(Names)
        if button == 'Sort: selection':
            selSort(Names)
        if button == 'Sort: quick':
            qsortHolder(Names)
        if button == 'Linear Search':
            linearSearch()
        if button == 'Binary Search':
            binarySearch()
    else:
        break  

