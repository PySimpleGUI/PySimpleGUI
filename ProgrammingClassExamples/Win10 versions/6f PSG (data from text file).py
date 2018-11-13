#PySimple examples (v 3.8)
#Tony Crewe
#Sep 2018

import PySimpleGUI as sg
import os

sg.SetOptions (font =('Calibri',12,'bold'))    

#get pathname to current file

dirname, filename = os.path.split(os.path.abspath(__file__))
pathname = os.path.join(dirname, 'Names.txt')             #original data
spathname = os.path.join(dirname, 'Names(sorted).txt')    #sorted data

#Get data from file
names = [line.strip() for line in open(pathname)]

column1 = [[sg.ReadButton('Original list', size = (13,1))],
           [sg.ReadButton('Default sort', size = (13,1))],
           [sg.ReadButton('Sort: selection',size = (13,1))],
           [sg.ReadButton('Sort: quick', size = (13,1))],
            [sg.Text('______________',font = ('Calibri', 12))],
           [sg.ReadButton('Save data\ndisplayed', size = (13,2))]]
           
layout =[[sg.Text('Search and Sort Demo', font =('Calibri', 20, 'bold'))],
[sg.Listbox(values =[''], size = (14, 11),font = ('Calibri', 12), background_color ='White',key = '_display_'), sg.Column(column1)],
         [sg.Text('_'*32,font = ('Calibri', 12))],
         [sg.InputText(size = (13,1), key = '_linear_'), sg.Text('  '), sg.InputText(size = (13,1), key = '_binary_')],
          [sg.ReadButton('Linear Search', size = (13,1)), sg.Text(' '), sg.ReadButton('Binary Search', size = (13,1))],
         ]

window = sg.Window('Search and Sort Demo').Layout(layout)

#function to display list
def display_list(list):
    global list_displayed
    #store list in Multiline text globally
    list_displayed = list
    #add list elements with new line
    values = [l for l in list]          
    window.FindElement('_display_').Update(values)
        
#use inbuilt python sort       
def default(names):
    l = names[:]
    l.sort()
    display_list(l)

#Selection sort
def sel_sort(names):
    l = names[:]
    for i in range(len(l)):
        smallest = i
        for j in range(i+1, len(l)):
            if l[j] < l[smallest]:          
                smallest = j                     
        l[smallest], l[i] = l[i], l[smallest]   
    display_list(l)

#Quick sort
def qsort_holder(names):                         
    l = names[:]                            
    quick_sort(l, 0, len(l) - 1)                
    display_list(l)
        
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
    quick_sort(l, first, low -1)            
    quick_sort(l, low, last)

#Linear Search - no need for Ordered list
def linear_search():
    l = names[:]
    found = False
    for l in l:
        if l == value['_linear_']:          
            found = True
            #Create list for display
            result = ['Linear search', l + ' found']
            window.FindElement('_display_').Update(result)
            break
    if not found:
        #Create list for display
        result = [value['_linear_'], 'was not found']
        window.FindElement('_display_').Update(result)

#Binary Search     
def binary_search():
    l = list_displayed[:]                           
    lo = 0
    hi = len(l)-1
    found = False                 
    while lo <= hi:
        mid = (lo + hi) //2     
        if l[mid] == value['_binary_']:
            #Create list for display
            found = True           
            result = ['Binary search', l[mid] + ' found.']
            window.FindElement('_display_').Update(result)
            break                  
        elif l[mid] < value['_binary_']:
            lo = mid + 1           
        else:
            hi = mid - 1           
    if not found:
        #Create list for display
        result = [value['_binary_'], 'was not found']
        window.FindElement('_display_').Update(result)
     
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
        if button == 'Save data\ndisplayed':
            f = open(spathname, 'w')                                      
            for name in list_displayed:
                print (name, file = f)
            f.close()
    else:
        break  
