#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg


'''
Quickly add a GUI to your script!

This simple script shows a 1-line-GUI addition to a typical Python command line script.

Previously this script accepted 1 parameter on the command line.  When executed, that
parameter is read into the variable fname.

The 1-line-GUI shows a form that allows the user to browse to find the filename. The GUI
stores the result in the variable fname, just like the command line parsing did.
'''

if len(sys.argv) == 1:
    event, (fname,) = sg.Window('My Script').Layout([[sg.T('Document to open')],
                                                            [sg.In(), sg.FileBrowse()],
                                                            [sg.CloseButton('Open'), sg.CloseButton('Cancel')]]).Read()
else:
    fname = sys.argv[1]

if not fname:
    sg.Popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
