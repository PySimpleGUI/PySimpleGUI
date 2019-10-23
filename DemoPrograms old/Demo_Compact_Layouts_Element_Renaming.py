import PySimpleGUI as sg
# Import the elements individually to save space
from PySimpleGUI import InputCombo, Combo, Multiline, ML, MLine, Checkbox, CB, Check, Button, B, Btn, ButtonMenu,BMenu, Canvas, Column, Col, Combo, DropDown, Drop, DD, Frame, Graph, Image, InputText, Input, In, I, Listbox, LBox, LB,  Menu, Multiline, ML, MLine, OptionMenu, Output, Pane, ProgressBar, Prog, PBar, Radio, R, Rad, Sizer, Slider, Spin, StatusBar, Tab, TabGroup, Table, Text, Txt, T, Tree, TreeData,  VerticalSeparator, Window, Print


"""
    Demo - Compact Layouts and Element Renaming
    
    Some layouts contain many many elements such that space becomes a premium.  For experienced PySimpleGUI
    programmers, there is little additional knowledge to be gained by writing
        sg.Text('My text')
    rather than using one of the shortcuts such as 
        sg.T('My text')
    However, even with shortcut usage, you continue to have the package prefix of
        sg.
    That's 3 characters per element that are added to your layout!
    The very long import statement st the top can be copied into your code to give you the ability to write
        T('My text')
        
    If you don't want to use that very-long import or perhaps want to use your own shortcut names, you can easily
    create your shortcut by simple assignment:
        T = sg.Text
    This enables you to use T just as if you imported the Class T from PySimpleGUI.  You could develop your own
    template that you copy and paste at the top of all of your PySimpleGUI programs.  Or perhaps perform an import
    of those assignments from a .py file you create.
    
    Note that you may lose docstrings in PyCharm using these shortcuts.  You can still see the parameters when pressing
    Control+P, but the Control+Q doesn't bring up the full list of parms and their descriptions.  Looking for a fix
    for this.
    
    PLEASE OH PLEASE OH PLEASE NEVER EVER EVER do this:
        from PySimpleGUI import *
    There is a bot scanning GitHub for this statement.  If found in your code, a squad of assassins will be dispatched
    from the PySimpleGUI headquarters and you will be hunted down and forced to change your code. 
"""

# A user created shortcut....
# Suppose this user's layout contains many Multiline Elements.  It could be advantageous to have a single letter
# shortcut version for Multiline
M = sg.Multiline

# This layout uses the user defined "M" element as well as the PySimpleGUI Button shortcut, B.
layout = [[M(size=(30,3))],
          [B('OK')]]

event, values = Window('Shortcuts', layout).read()
sg.popup_scrolled(event, values)
