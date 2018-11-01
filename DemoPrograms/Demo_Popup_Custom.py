#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

'''
   Use this code as a starting point for creating your own Popup functions.  
   Rather than creating a long list of Popup high-level API calls, PySimpleGUI provides
   you with the tools to easily create your own.  If you need more than what the standard PopupGetText and
   other calls provide, then it's time for you to graduate into making your own windows.  Or, maybe you need
   another window that pops-up over your primary window.  Whatever the need, don't hesitate to dive in
   and create your own Popup call.
   
   This example is for a DropDown / Combobox Popup.  You provide it with a title, a message and the list
   of values to choose from. It mimics the return values of existing Popup calls (None if nothing was input)
'''


def PopupDropDown(title, text, values):
    window = sg.Window(title).Layout([[sg.Text(text)],
                                      [sg.DropDown(values, key='_DROP_')],
                                      [sg.OK(), sg.Cancel()]])
    event, values = window.Read()
    return None if event != 'OK' else values['_DROP_']


# -----------------------  Calling your PopupDropDown function -----------------------

values = ['choice {}'.format(x) for x in range(30)]

print(PopupDropDown('My Title', 'Please make a selection', values))
