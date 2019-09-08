

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

As previously mentioned this is also where you should post all problems and enhancements.


## MACS + tkinter = SUCKS

Not sure why, but for over a year and a half, setting the color of buttons does not work on Macs.  There have been numerous other problems.  Checking the Issues database is the best place to see what they are.  If there was a magic wand it would have been used long ago to fix these problems, but there does not appear to be a magic fix.

This was already mentioned at the top of this document but want to make sure it's covered as a "known issue"

## Multiple threads

While not an "issue" this is a ***stern warning***

## **Do not attempt** to call `PySimpleGUI` from multiple threads! It's `tkinter` based and `tkinter` has issues with multiple threads

Tkinter also wants to be the MAIN thread in your code.  So, if you have to run multiple threads, make sure the GUI is the main thread.

Other than that, feel free to use threads with PySimpleGUI on all of the ports.  You'll find a good example for how to run "long running tasks" in your event loop by looking at the demo program: `Demo_Multithreaded_Long_Tasks.py`


# Contributing

## Core Code

***Core code changes/pull requests are not being accepted at this time.***

## Demos

You're welcome to share a PySimpleGUI program you've written that you think fits the model of a PySimpleGUI Demo Program.

## GitHub Repos

If you've created a GitHub for your project that uses PySimpleGUI then please submit it to be included in this document or on the PySimpleGUI GitHub site.  Also, you'll find a lot more people will look at your code, explore your repo if you have posted **screen shots in your readme**.  People *love* success stories and showing your GUI's screen shows you've been successful.  Everyone wins!
