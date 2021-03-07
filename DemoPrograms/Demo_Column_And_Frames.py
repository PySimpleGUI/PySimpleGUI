import PySimpleGUI as sg

"""
    Demo sg.Columns and sg.Frames
    Demonstrates using mixture of sg.Column and sg.Frame elements to create a nice window layout.
    A couple of the concepts shown here include:
    * Using sg.Columns and sg.Frames with specific sizes on them
    * Buttons that have the same text on them that arew differentiated using explicit keys
    * One way to hard-code the size of a Frame is to hard-code the size of a Column inside the frame

    CAUTION:
        Using explicit sizes on Column and Frame elements may not have the same effect on
        all computers.  Hard coding parts of layouts can sometimes not have the same result on all computers.
    
    There are 3 sg.Columns.  Two are side by side at the top and the third is along the bottom
    
    When there are multiple Columns on a row, be aware that the default is for those Columns to be
    aligned along their center.  If you want them to be top-aligned, then you need to use the
    vtop helper function to make that happen.
    
    Copyright 2021 PySimpleGUI
"""

col2 = sg.Column([[sg.Frame('Accounts:', [[sg.Column([[sg.Listbox(['Account '+str(i) for i in range(1,16)],
                                                      key='-ACCT-LIST-',size=(15,20)),]],size=(150,400))]])]],pad=(0,0))

col1 = sg.Column([
    # Categories sg.Frame
    [sg.Frame('Categories:',[[ sg.Radio('Websites', 'radio1', default=True, key='-WEBSITES-', size=(10,1)),
                            sg.Radio('Software', 'radio1', key='-SOFTWARE-',  size=(10,1))]],)],
    # Information sg.Frame
    [sg.Frame('Information:', [[sg.Text(), sg.Column([[sg.Text('Account:')],
                             [sg.Input(key='-ACCOUNT-IN-', size=(19,1))],
                             [sg.Text('User Id:')],
                             [sg.Input(key='-USERID-IN-', size=(19,1)),
                              sg.Button('Copy', key='-USERID-')],
                             [sg.Text('Password:')],
                             [sg.Input(key='-PW-IN-', size=(19,1)),
                              sg.Button('Copy', key='-PASS-')],
                             [sg.Text('Location:')],
                             [sg.Input(key='-LOC-IN-', size=(19,1)),
                              sg.Button('Copy', key='-LOC-')],
                             [sg.Text('Notes:')],
                             [sg.Multiline(key='-NOTES-', size=(25,5))],
                             ], size=(235,350), pad=(0,0))]])], ], pad=(0,0))

col3 = sg.Column([[sg.Frame('Actions:',
                            [[sg.Column([[sg.Button('Save'), sg.Button('Clear'), sg.Button('Delete'), ]],
                                        size=(450,45), pad=(0,0))]])]], pad=(0,0))

# The final layout is a simple one
layout = [[col1, col2],
          [col3]]

# A perhaps better layout would have been to use the vtop layout helpful function.
# This would allow the col2 column to have a different height and still be top aligned
# layout = [sg.vtop([col1, col2]),
#           [col3]]


window = sg.Window('Columns and Frames', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break

window.close()