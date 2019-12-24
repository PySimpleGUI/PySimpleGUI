# this one long import has the effect of making the code more compact as there is no 'sg.' prefix required for Elements
import PySimpleGUI as sg
from PySimpleGUI import InputCombo, Combo, Multiline, ML, MLine, Checkbox, CB, Check, Button, B, Btn, ButtonMenu, Canvas, Column, Col, Combo, Frame, Graph, Image, InputText, Input, In, Listbox, LBox, Menu, Multiline, ML, MLine, OptionMenu, Output, Pane, ProgressBar, Radio, Slider, Spin, StatusBar, Tab, TabGroup, Table, Text, Txt, T, Tree, TreeData,  VerticalSeparator, Window, Sizer

"""
    Demo Columns and Frames
    Demonstrates using mixture of Column and Frame elements to create a nice window layout.
    A couple of the concepts shown here include:
    * Using Columns and Frames with specific sizes on them
    * Importing all required classes so that "sg." is not required on any objects. This makes the code more compact and readable
    
    There are 3 columns.  Two are side by side at the top and the third is along the bottom
"""

sg.theme('GreenTan')

col2 = Column([[Frame('Accounts:', [[Column([[Listbox(['Account '+str(i) for i in range(1, 16)],
                                                      key='-ACCT-LIST-', size=(15, 20)), ]], size=(150, 400))]])]], pad=(0, 0))

col1 = Column([
    # Categories frame
    [Frame('Categories:', [[Radio('Websites', 'radio1', default=True, key='-WEBSITES-', size=(10, 1)),
                            Radio('Software', 'radio1', key='-SOFTWARE-',  size=(10, 1))]],)],
    # Information frame
    [Frame('Information:', [[Column([[Text('Account:')],
                                     [Input(key='-ACCOUNT-IN-', size=(19, 1))],
                                     [Text('User Id:')],
                                     [Input(key='-USERID-IN-', size=(19, 1)),
                                      Button('Copy', key='-USERID-')],
                                     [Text('Password:')],
                                     [Input(key='-PW-IN-', size=(19, 1)),
                                      Button('Copy', key='-PASS-')],
                                     [Text('Location:')],
                                     [Input(key='-LOC-IN-', size=(19, 1)),
                                      Button('Copy', key='-LOC')],
                                     [Text('Notes:')],
                                     [Multiline(key='-NOTES-', size=(25, 5))],
                                     ], size=(235, 350), pad=(0, 0))]])], ], pad=(0, 0))

col3 = Column([[Frame('Actions:', [[Column([[Button('Save'), Button(
    'Clear'), Button('Delete'), ]], size=(450, 45), pad=(0, 0))]])]], pad=(0, 0))

layout = [[col1, col2], [col3]]

window = Window('Passwords', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event is None:
        break

window.close()
