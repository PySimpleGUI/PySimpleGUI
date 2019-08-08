

---

# The PySimpleGUI Debugger

Starting on June 1, 2019, a built-in version of the debugger `imwatchingyou` has been shipping in every copy of PySimpleGUI.  It's been largely downplayed to gauge whether or not the added code and the added feature and the use of a couple of keys, would mess up any users.  

So far no one has reported anything at all about the debugger.  The assumption is that it is quietly lying dormant, waiting for you to press the `BREAK` or `CONTROL` + `BREAK` keys.  It's odd no one has accidently done this and freaked out, logging an Issue.

The plain PySimpleGUI module has a debugger builtin.  For the other ports, please use the package `imwatchingyou`.

## Preparing To Run the Debugger

If your program is running with blocking `Read` calls, then you will want to add a timeout to your reads.  This is because the debugger gets it's cycles by stealing a little bit of time from these async calls.

Your event loop will be modified from this:
```python
while True:
    event, values = window.Read()
```

To this:
```python
while True:
    event, values = window.Read(timeout=100)
    if event == sg.TIMEOUT_KEY:
        continue
```

This event loop will do nothing at all if a timeout occurs and will execute your normal code (that follows the if statement) when there is any event that is not a timeout.

This timeout value of 100 means that your debugger GUI will be updated 10 times a second.  If this adds too much "drag" to your application, you can make the timeout larger.  Try using 1000 instead of 100.

## Debugger Windows

There are 2 debugger windows. One is called a "Popout".  The Popout window displays all of your variables



# "Demo Programs" Applications

There are too many to list!!

There are over 170 sample programs to give you a jump start.


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

Core code pull requests are not being accepted at this time.
