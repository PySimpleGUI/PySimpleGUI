#PySimple examples (v 3.9)
#Tony Crewe
#Oct 2018 MacOs

import PySimpleGUI as sg

sg.SetOptions(background_color = 'LightBlue',
            element_background_color = 'LightBlue',
            text_element_background_color = 'LightBlue',
              font= ('Calibri', 14, 'bold'))

layout =[[sg.Text('Search Demo', font =('Calibri', 18, 'bold')), sg.ReadButton('Show Names')],
[sg.Text('',size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color ='White',key = '_display1_'),
 sg.Text('',size = (14, 11),relief=sg.RELIEF_SOLID,font = ('Calibri', 12), background_color ='White',key = '_display2_')],
         [sg.Text('_'*35,font = ('Calibri', 16))],
         [sg.InputText(size = (10,1), key = '_linear_'), sg.InputText(size = (11,1), key = '_binary_')],
          [sg.ReadButton('Linear Search', key = '_ls_',size = (11,1)), sg.ReadButton('Binary Search', key ='_bs_',size = (11,1))],
         ]
window = sg.Window('Search Demo').Layout(layout)

#finalize allows the disabling of the two buttons before .Read statement
window.Finalize()                                  
window.FindElement('_ls_').Update(disabled = True)     
window.FindElement('_bs_').Update(disabled = True)

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
    #add list elements with new line
    for l in list:                
        names = names + l + '\n'
    window.FindElement(display).Update(names)
    #enable buttons now data loaded
    window.FindElement('_ls_').Update(disabled = False)    
    window.FindElement('_bs_').Update(disabled = False)    
    
#Linear Search - no need for Ordered list
def linear_search():
    l = names[:]
    found = False
    for l in l:
        #Check each value
        if l == value['_linear_']:             
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
    #Start with found is Flase
    found = False                   
    while lo <= hi:
        #Start in middle
        mid = (lo + hi) //2
        #get the value from the search box
        if l[mid] == value['_binary_']:   
            window.FindElement('_display2_').Update('Binary search\n' + l[mid] + ' found.')
            #If found display and stop
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
        if button == '_ls_':   
            linear_search()
        if button == '_bs_':
            binary_search()
    else:
        break  

