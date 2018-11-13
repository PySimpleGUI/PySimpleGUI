#PySimple examples (v 3.9)
#Tony Crewe
#Oct 2018 MacOS

import PySimpleGUI as sg

sg.SetOptions(background_color = 'LightBlue',
            element_background_color = 'LightBlue',
            text_element_background_color = 'LightBlue',
              font= ('Calibri', 14, 'bold'))  

#setup column (called column1) of buttons to use in layout

column1 = [[sg.ReadButton('Original list', size = (11,1))],
           [sg.ReadButton('Default sort', size = (11,1))],
           [sg.ReadButton('Sort: selection',size = (11,1))],
           [sg.ReadButton('Sort: quick', size = (11,1))]]
           
layout =[[sg.Text('Search and Sort Demo', font =('Calibri', 20, 'bold'))],
[sg.Text('',size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color = 'White',key = '_display_'), sg.Column(column1)],
         [sg.Text('_'*35,font = ('Calibri', 16))],
         [sg.InputText(size = (10,1), key = '_linear_'), sg.Text('   '), sg.InputText(size = (11,1), key = '_binary_')],
          [sg.ReadButton('Linear Search', size = (11,1)), sg.Text(' '), sg.ReadButton('Binary Search', size = (11,1))],
         ]

window = sg.Window('Search and Sort Demo').Layout(layout)

#names for Demo, could be loaded from a file
names= ['Roberta', 'Kylie', 'Jenny', 'Helen',
        'Andrea', 'Meredith','Deborah','Pauline',
        'Belinda', 'Wendy']

#function to display list
def display_list(list):
    #store list in Multiline text globally
    global list_displayed         
    list_displayed = list
    display = ''
    #add list elements with new line
    for l in list:                
        display = display + l + '\n'
    window.FindElement('_display_').Update(display)
        
#use inbuilt python sort       
def default(names):
    l = names[:]
    l.sort()    
    display_list(l)

#Selection sort - See Janson Ch 7 
def sel_sort(names):
    l = names[:]
    for i in range(len(l)):
        smallest = i
        for j in range(i+1, len(l)):
            #find smallest value
            if l[j] < l[smallest]:
                #swap it to front 
                smallest = j
        #repeat from next position 
        l[smallest], l[i] = l[i], l[smallest]   
    display_list(l)

#Quick sort - See Janson Ch 7
def qsort_holder(names):                         
    l = names[:]
    #pass List, first and last
    quick_sort(l, 0, len(l) -1)                 
    display_list(l)
#Quicksort is a partition sort       
def quick_sort(l, first, last):                 
    if first >= last:
        return l
    pivot = l[first]                           
    low = first                                 
    high = last
    while low < high:
        while l[high] > pivot:
            high = high -1
        while l[low] < pivot:
            low = low + 1
        if low <= high:
            l[high], l[low] = l[low], l[high]
            low = low + 1
            high = high -1
    #continue splitting - sort small list
    quick_sort(l, first, low -1)                
    quick_sort(l, low, last)

#Linear Search - no need for Ordered list
def linear_search():
    l = names[:]
    found = False
    for l in l:
        if l == value['_linear_']:           
            found = True
            window.FindElement('_display_').Update('Linear search\n' + l + ' found.')
            break
    if not found:
        window.FindElement('_display_').Update(value['_linear_'] + ' was \nNot found')

#Binary Search - only works for ordered lists      
def binary_search():
    l= list_displayed[:]                       
    lo = 0
    hi = len(l)-1
    found = False           
    while lo <= hi:
        mid = (lo + hi) //2     
        if l[mid] == value['_binary_']: 
            window.FindElement('_display_').Update('Binary search\n' + l[mid] + ' found.')
            found = True    
            break               
        elif l[mid] < value['_binary_']:
            lo = mid + 1            
        else:
            hi = mid - 1        
    if not found:           
        window.FindElement('_display_').Update(value['_binary_'] + ' was \nNot found')

        
while True:
    button, value = window.Read() 
    if button is not None:  
        if button == 'Original list':
            display_list(names)
        if button == 'Default sort':
            default(names)
        if button == 'Sort: selection':
            sel_sort(names)
        if button == 'Sort: quick':
            qsort_holder(names)
        if button == 'Linear Search':
            linear_search()
        if button == 'Binary Search':
            binary_search()
    else:
        break  

