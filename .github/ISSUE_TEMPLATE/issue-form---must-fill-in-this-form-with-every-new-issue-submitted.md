---
name: Issue Form - Must fill in this form with every new issue submitted.  CLICK THE GREEN BUTTON ---------------------------------->
about: This form contains the information needed to help you solve your problem
title: "[ Enhancement/Bug/Question] My problem is..."
labels: ''
assignees: ''

---

### Type of Issues (Enhancement, Error, Bug, Question)

### Operating System

### Python version

### PySimpleGUI Port and Version

Ports = tkinter, Qt, WxPython, Web

PySimpleGUI Version:

tkinter version:

You can get these by adding this to the top of your file and running it:

```python
import PySimpleGUI as sg

print(sg)             # Location of your PySimpleGUI.py file
print(sg.version)     # PySimpleGUI version number
print(sg.tclversion_detailed)   # tkinter detailed version number (in PySimpleGUI version 4.29.0+)
print(sg.sys.version) # Python version number
```

The tkinter version number can be obtained using above code in version 4.29.0+.  If your code is prior:
```python
print(sg.tkinter.Tcl().eval('info patchlevel'))
```


### Your Experience Levels In Months or Years

_________ Python programming experience
_________ Programming experience overall
_________ Have used another Python GUI Framework (tkinter, Qt, etc) previously (yes/no is fine)?

### You have completed these steps:

- [ ] Read instructions on how to file an Issue
- [ ] Searched through main docs http://www.PySimpleGUI.org for your problem
- [ ] Searched through the readme for your specific port if not PySimpleGUI (Qt, WX, Remi)
- [ ] Looked for Demo Programs that are similar to your goal http://www.PySimpleGUI.com
- [ ] Note that there are also Demo Programs under each port on GitHub
- [ ] Run your program outside of your debugger (from a command line)
- [ ] Searched through Issues (open and closed) to see if already reported
- [ ] Try again by upgrading your PySimpleGUI.py file to use the current one on GitHub. Your problem may have already been fixed but is not yet on PyPI.

### Description of Problem / Question / Details


### Code To Duplicate

A short program that isolates and demonstrates the problem (i.e. please don't paste a link to your 400 line program.... instead paste your 10 line program in full).  

Yes, it is a pain to narrow down problems, but it's part of the debugging process.  Help me help you by providing something that can be executed so that work on getting you a fix or a workaround can immediately begin.

This pre-formatted code block is all set for you to paste in your bit of code:

```python
import PySimpleGUI as sg

## Paste your code here
```
