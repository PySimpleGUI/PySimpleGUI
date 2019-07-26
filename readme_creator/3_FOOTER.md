# "Demo Programs" Applications

There are too many to list!!

There are over 130 sample programs to give you a jump start.


You will find Demo Programs located in a subfolder named "Demo Programs" under each of the PySimpleGUI ports on GitHub.

Demo programs for plain PySimpleGUI (tkinter)
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms

Demo programs for PySimpleGUIQt:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIQt/Demo%20Programs

Demo programs for PySimpleGUIWx:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWx/Demo%20Programs

Demo programs for PySimpleGUIWeb:
https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb/Demo%20Programs


There are not many programs under each of the port's folders because the main Demo Programs should run on all of the other platforms with minimal changes (often only the import statement changes).

## Start Here

When you are just beginning to build your application, or to design it, look through the Demo Programs first to see if there is a program written that does what you're looking for.  If so, then this program could be a good starting point.  Copy it and modify it to your liking.

Even if no program perfectly matches your situation, there are still a good number of example uses of Elements or techniques that are demonstrated.  

Maybe you're going to write a program that uses the Graph Element.  In addition to reading the documentaion about the Graph Element, check to see if there's a Demo Program that uses it.   At the moment there are 7 Demo programs that match "Demo_Graph_*.py"



## Packages Used In Demos


  While the core PySimpleGUI code  does not utilize any 3rd party packages, some of the demos do.  They add a GUI to a few popular packages.  These packages include:
  * [Chatterbot](https://github.com/gunthercox/ChatterBot)
  * [Mido](https://github.com/olemb/mido)
  * [Matplotlib](https://matplotlib.org/)
  * [PyMuPDF](https://github.com/rk700/PyMuPDF)


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


## Fun Stuff
Here are some things to try if you're bored or want to further customize

**Debug Output**
Be sure and check out the EasyPrint (Print) function described in the high-level API section.  Leave your code the way it is, route your stdout and stderror to a scrolling window.

For a fun time, add these lines to the top of your script

```python
    import PySimpleGUI as sg
    print = sg.Print
```
This will turn all of your print statements into prints that display in a window on your screen rather than to the terminal.

**Look and Feel**
Dial in the look and feel that you like with the `SetOptions` function.  You can change all of the defaults in one function call.  One line of code to customize the entire GUI.
Or beginning in version 2.9 you can choose from a look and feel using pre-defined color schemes.   Call ChangeLookAndFeel with a description string.

```python
    sg.ChangeLookAndFeel('GreenTan')

```

Valid values for the  description string are:

      GreenTan
      LightGreen
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

To see the latest list of color choices, take a look at the bottom of the `PySimpleGUI.py` file where you'll find the `ChangLookAndFeel` function.

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
While not an "issue" this is a ***stern warning***

## **Do not attempt** to call `PySimpleGUI` from multiple threads! It's `tkinter` based and `tkinter` has issues with multiple threads

**Progress Meters** - the visual graphic portion of the meter may be off.  May return to the native tkinter progress meter solution in the future.  Right now a "custom" progress meter is used.  On the bright side, the statistics shown are extremely accurate and can tell you something about the performance of your code.    If you are running 2 or more progress meters at the same time using `OneLineProgressMeter`, you need to close the meter by using the "Cancel" button rather than the X

**Async windows** - these include the 'easy' windows (`OneLineProgressMeter` and EasyPrint/Print). If you start overlapping having Async windows open with normal windows then things get a littler squirrelly.  Still tracking down the issues and am making it more solid every day possible.  You'll know there's an issue when you see blank window.

**EasyPrint** - EasyPrint is a new feature that's pretty awesome.  You print and the output goes to a window, with a scroll bar, that you can copy and paste from.  Being a new feature, it's got some potential problems.  There are known interaction problems with other GUI windows.  For example, closing a Print window can also close other windows you have open.  For now, don't close your debug print window until other windows are closed too.

## Contributing

A MikeTheWatchGuy production... entirely responsible for this code.... unless it causes you trouble in which case I'm not at all responsible.

