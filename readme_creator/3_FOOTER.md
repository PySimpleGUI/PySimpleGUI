

---



# "Demo Programs" Applications

There are too many to list!!

There are over 170 sample programs to give you a jump start.

These programs are an integral part of the overall PySimpleGUI documentation and learning system.  They will give you a headstart in a way you can learn from and understand.  They also show you integration techiques to other packages that have been figured out for you.

You will find Demo Programs located in a subfolder named "Demo Programs" under the top level and each of the PySimpleGUI ports on GitHub.

Demo programs for plain PySimpleGUI (tkinter)
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms

Demo programs for PySimpleGUIQt:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIQt/Demo%20Programs

Demo programs for PySimpleGUIWx:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWx/Demo%20Programs

Demo programs for PySimpleGUIWeb:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb/Demo%20Programs


There are not many programs under each of the port's folders because the main Demo Programs should run on all of the other platforms with minimal changes (often only the import statement changes).


You will also find a lot of demos running on Trinket
http://Trinket.PySimpleGUI.org



## Packages Used In Demos


  While the core PySimpleGUI code  does not utilize any 3rd party packages, some of the demos do.  They add a GUI to a few popular packages.  These packages include:
  * [Chatterbot](https://github.com/gunthercox/ChatterBot)
  * [Mido](https://github.com/olemb/mido)
  * [Matplotlib](https://matplotlib.org/)
  * [PyMuPDF](https://github.com/rk700/PyMuPDF)
  * OpenCV
  * pymunk
  * psutil
  * pygame
  * Forecastio



# Creating a Windows .EXE File

It's possible to create a single .EXE file that can be distributed to Windows users. There is no requirement to install the Python interpreter on the PC you wish to run it on. Everything it needs is in the one EXE file, assuming you're running a somewhat up to date version of Windows.

Installation of the packages, you'll need to install PySimpleGUI and PyInstaller (you need to install only once)

```bash
pip install PySimpleGUI
pip install PyInstaller

```

To create your EXE file from your program that uses PySimpleGUI,  `my_program.py`, enter this command in your Windows command prompt:

```bash
pyinstaller -wF my_program.py

```

You will be left with a single file,  `my_program.exe`, located in a folder named  `dist`  under the folder where you executed the  `pyinstaller`  command.

That's all... Run your  `my_program.exe`  file on the Windows machine of your choosing.

> "It's just that easy."

(famous last words that screw up just about anything being referenced)

Your EXE file should run without creating a "shell window". Only the GUI window should show up on your taskbar.

If you get a crash with something like:
```python
ValueError: script '.......\src\tkinter' not found
```

Then try adding **`--hidden-import tkinter`** to your command

# Creating a Mac App File

There are reports that PyInstaller can be used to create App files.  It's not been officially tested.

Run this command on your Mac

> pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' your_program.py


This info was located on Reddit with the source traced back to:
https://github.com/pyinstaller/pyinstaller/issues/1350

# Debug Output

Be sure and check out the EasyPrint (Print) function described in the high-level API section.  Leave your code the way it is, route your stdout and stderror to a scrolling window.

For a fun time, add these lines to the top of your script

```python
    import PySimpleGUI as sg
    print = sg.Print
```
This will turn all of your print statements into prints that display in a window on your screen rather than to the terminal.

# Look and Feel

You can change defaults and colors of a large number of things in PySimpleGUI quite easily.

##  `ChangleLookAndFeel`

Want a quick way of making your windows look a LOT better?  Try calling `ChangeLookAndFeel`.  It will, in a single call, set various color values to widgets, background, text, etc.

Or dial in the look and feel (and a whole lot more) that you like with the `SetOptions` function.  You can change all of the defaults in one function call.  One line of code to customize the entire GUI.


```python
    sg.ChangeLookAndFeel('GreenTan')
```

Valid look and feel values are currently:

```python
SystemDefault
Reddit
Topanga
GreenTan
Dark
LightGreen
Dark2
Black
Tan
TanBlue
DarkTanBlue
DarkAmber
DarkBlue
Reds
Green
BluePurple
Purple
BlueMono
GreenMono
BrownBlue
BrightColors
NeutralBlue
Kayak
SandyBeach
TealMono
```


The way this call actually works is that it calls `SetOptions` with a LOT of color settings.  Here is the actual call that's made.  As you can see lots of stuff is defined for you.



```python
SetOptions(background_color=colors['BACKGROUND'],
            text_element_background_color=colors['BACKGROUND'],
            element_background_color=colors['BACKGROUND'],
            text_color=colors['TEXT'],
            input_elements_background_color=colors['INPUT'],
            button_color=colors['BUTTON'],
            progress_meter_color=colors['PROGRESS'],
            border_width=colors['BORDER'],
            slider_border_width=colors['SLIDER_DEPTH'],
            progress_meter_border_depth=colors['PROGRESS_DEPTH'],
            scrollbar_color=(colors['SCROLL']),
            element_text_color=colors['TEXT'],
            input_text_color=colors['TEXT_INPUT'])
```


<!-- <+func.ListOfLookAndFeelValues+> -->



<!-- <+func.ChangeLookAndFeel+> -->


To see the latest list of color choices you can call `ListOfLookAndFeelValues()`

You can also combine the `ChangeLookAndFeel` function with the `SetOptions` function to quickly modify one of the canned color schemes.  Maybe you like the colors but was more depth to your bezels.  You can dial in exactly what you want.



**ObjToString**
Ever wanted to easily display an objects contents easily?  Use ObjToString to get a nicely formatted recursive walk of your objects.
This statement:

    print(sg.ObjToSting(x))

And this was the output

    <class '__main__.X'>
        abc = abc
        attr12 = 12
        c = <class '__main__.C'>
            b = <class '__main__.B'>
                a = <class '__main__.A'>
                    attr1 = 1
                    attr2 = 2
                    attr3 = three
                attr10 = 10
                attrx = x

You'll quickly wonder how you ever coded without it.

---
# Known Issues

Well, there are a few quirks, and problems of course.  Check the [GitHub Issues database](https://github.com/PySimpleGUI/PySimpleGUI/issues) for a list of them.

As previously mentioned **this is where you should post all problems and enhancements.**

Random crashes have been rare.  The code is stable and hasn't been "quirky" nor have there been many "emergency" releases.


## MACS & tkinter

Macs and PySimpleGUI did not play well together up until Nov 2019 and the release of ttk buttons.  Prior to that buttons had to be white.  Now the Mac can use any color for buttons and they work great.  Images on buttons work as well.

The problems were the normal tk.Button was not working correctly on the Mac.  You couldn't set the button color.  If you tried it appeared as if the text was missing.

Users have recently reported the ability to install Python 3.7 from the Python.org website and not use the Homebrew version.  This resolved all of the button color problems. 

Regardless of where you get your Python / tkinter, Macs can now enjoy using all of the look and feel color themes that Windows and Linux users are able to achieve.

Many PySimpleGUI users have switched from PySimpleGUI to PySimpleGUIQt due to the button problems.  IF you're one of them, ***you should consider switching back***.  One reason to return to PySimpleGUI is that features tend to get implemented on PySimpleGUI (tkinter version) and then later on the  other ports.  There are a number of other reasons to give tkinter another try.


## Multiple threads

Consider this is a ***stern warning***

### **Do not attempt** to call `PySimpleGUI` from multiple threads! At least the `tkinter` based port because tkinter is not threadsafe and has known issues with multiple threads

Tkinter also wants to be the MAIN thread in your code.  So, if you have to run multiple threads, make sure the GUI is the main thread.

Other than that, feel free to use threads with PySimpleGUI on all of the ports.  You'll find a good example for how to run "long running tasks" in your event loop by looking at the demo program: `Demo_Multithreaded_Long_Tasks.py`.  There are several examples of using threads with PySimpleGUI.

Be sure and **delete** your windows after you close them if you are running with multiple threads.  There is a chance another thread's garbage collect will attempt to delete the window when not in the mainthread which will cause tkinter to crash.

### The dreaded "Tcl_AsyncDelete: async handler deleted by the wrong thread" error

This crash has plagued and mystified tkinter users for some time now.  It happens when the user is running multiple threads in their application.  Even if the user doesn't make any calls that are into tkinter, this problem can still cause your program to crash.

I'm thrilled to say there's a solution and it's easy to implement.  If you're getting this error, then here is what is causing it.

When you close a window and delete the layout, the tkinter widgets that were in use in the window are no longer needed.  Python marks them to be handled by the "Garbage Collector".  They're deleted but not quite gone from memory.  Then, later, while your thread is running, the Python Garbage Collect algorithm decides it's time to run garbage collect.  When it tells tkinter to free up the memory, the tkinter code looks to see what context it is running under.  It sees that it's a thread, not the main thread, and generates this exception.  

The way around this is actually quite easy.

When you are finished with a window, be sure to:

* Close the Window
* Set the `layout` variable to None
* Set the `window` variable to None
* Trigger Python's Garbage Collect to run immediately

The sequence looks like this in code:

```python
    import gc

    # Do all your windows stuff... make a layout... show your window... then when time to exit
    window.close()
    layout = None
    window = None
    gc.collect()
```
    
This will ensure that the tkinter widgets are all deleted in the context of the main-thread and another thread won't accidently run the Garbage Collect



# Contributing to PySimpleGUI

### Open Source License, but Private Development

PySimpleGUI is different than most projects on GitHub.  It is licensed using the "Open Source License" LGPL3.  However, the coding and development of the project is not "open source".

This project does not accept user submitted code.

#### Write Applications, Use PySimpleGUI, Write Tutorials, Teach Others

These are a few of the ways you can directly contribute to PySimpleGUI.  Using the package to make cool stuff and helping others learn how to use it to make cool stuff and a big help to PySimpleGUI.   **Everyone** learns from seeing other people's implementations.  It's through user's creating applications that new problems and needs are discovered.  These have had a profound and positive impact on the project in the past.

#### Pull Requests

Pull requests are *not being accepted* for the project.  This includes sending code changes via other means than "pull requests".  Plainly put, core code you send will not be used.


#### Bug Fixes

If you file an Issue for a bug, have located the bug, and found a fix in 10 lines of code or less.... and you wish to share your fix with the community, then feel free to include it with the filed Issue.  If it's longer than 10 lines and wish to discuss it, then send an email to help@PySimpleGUI.org.

## Thank You

The support from the user community has been amazing.  Your passion for creating PySimpleGUI applications is infectious.  Every "thank you" is noticed and appreciated!  Your passion for wanting to see PySimpleGUI improve is neither ignored nor unappreciated.

It's understood that this way of development of a Python package is unorthodox.  You may find it frustrating and slow, but hope you can respect the decision for it to operate in this manner and be supportive.

## GitHub Repos

If you've created a GitHub for your project that uses PySimpleGUI then please post screenshots in in the "User's Screenshots" Issue on the PySimpleGUI GitHub.  Say a little something about it and I'll also add it to the announcements. People *love* success stories and showing your GUI's screen visually communicates your success. 
