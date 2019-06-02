
![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)      
      
[![Downloads](http://pepy.tech/badge/pysimplegui)](http://pepy.tech/project/pysimplegui)        tkinter
[![Downloads ](https://pepy.tech/badge/pysimplegui27)](https://pepy.tech/project/pysimplegui27)      tkinter 2.7
[![Downloads](https://pepy.tech/badge/pysimpleguiqt)](https://pepy.tech/project/pysimpleguiqt)   Qt
[![Downloads](https://pepy.tech/badge/pysimpleguiwx)](https://pepy.tech/project/pysimpleguiWx)    WxPython
[![Downloads](https://pepy.tech/badge/pysimpleguiweb)](https://pepy.tech/project/pysimpleguiWeb)   Web (Remi)
![Documentation Status](https://readthedocs.org/projects/pysimplegui/badge/?version=latest)      
 ![Awesome Meter](https://img.shields.io/badge/Awesome_meter-100-yellow.svg)      
 ![Python Version](https://img.shields.io/badge/Python-2.7_3.x-yellow.svg)      
      

      
# PySimpleGUI      
      
   
            
## Supports both Python 2.7 & 3 when using tkinter

## Supports both PySide2 and PyQt5 (limited support)

## Effortlessly move across tkinter, Qt, WxPython, and the Web (Remi) by changing only the import statement

## The *only* way to write both desktop and web based GUIs at the same time



![Python Version](https://img.shields.io/badge/PySimpleGUI_For_Python_3.x_Version-3.37.0-red.svg?longCache=true&style=for-the-badge)      
      
![Python Version](https://img.shields.io/badge/PySimpleGUI_For_Python_2.7_Version-1.37.0-blue.svg?longCache=true&style=for-the-badge)      
  
![Python Version](https://img.shields.io/badge/PySimpleGUIQt_Version-0.31.0-orange.svg?longCache=true&style=for-the-badge)    
      
![Python Version](https://img.shields.io/badge/PySimpleGUIWx_version-0.11.0-orange.svg?longCache=true&style=for-the-badge)

![Python Version](https://img.shields.io/badge/PySimpleGUIWeb_Version-0.28.1-orange.svg?longCache=true&style=for-the-badge)

[Announcements of Latest Developments](https://github.com/MikeTheWatchGuy/PySimpleGUI/issues/142)      
      
[ReadTheDocs](http://pysimplegui.readthedocs.io/)      
      
[COOKBOOK!](https://pysimplegui.readthedocs.io/cookbook/)      
      
[Brief Tutorial](https://pysimplegui.readthedocs.io/tutorial/)      
      
[Latest Demos and Master Branch on GitHub](https://github.com/MikeTheWatchGuy/PySimpleGUI)      
      
[Docs in PDF Format](https://github.com/MikeTheWatchGuy/PySimpleGUI/tree/master/docs)      
      
[Repl.it Home for PySimpleGUI](https://repl.it/@PySimpleGUI)
      
Super-simple GUI to use... Powerfully customizable    
      
Home of the 1-line custom GUI & 1-line progress meter      
    
The native GUI framework for perfectionists with deadlines    

Actively developed and supported (It's 2019 and still going strong)
      
#### Note regarding Python versions      
As of 9/25/2018 **both Python 3 and Python 2.7 are supported**!   The Python 3 version is named `PySimpleGUI`. The Python 2.7 version is `PySimpleGUI27`.  They are installed separately and the imports are different. See instructions in Installation section for more info.      
      
# Qt Version


Check out the new PySimpleGUI port to the Qt GUI Framework.  You can learn more on the [PySimpleGUIQt GitHub site](https://github.com/MikeTheWatchGuy/PySimpleGUI/tree/master/PySimpleGUIQt).  **There is a separate Readme file for the Qt version** that you'll find there.  

Give it a shot if you're looking for something a bit more "modern".  PySimpleGUIQt is currently in Alpha.  All of the widgets are operational but some may not yet be full-featured.  If one is missing and your project needs it, log an Issue and you'll likely get priority support. 

Here is a summary of the Qt Elements

![scrolling graphics](https://user-images.githubusercontent.com/13696193/48665874-8bfd0e00-ea84-11e8-880d-8e164d9fea34.gif)

Are there enough things on there to cover your GUI solution?


## Source code compatibility
Your source code is completely portable from one platform to another by simply changing the import statement.

# WxPython Version

 [PySimpleGUIWx GitHub site](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWx).  **There is a separate Readme file for the WxPython version**.

Started in late December 2018 PySimpleGUIWx started with the SystemTray Icon feature.    This enabled the package to have one fully functioning feature that can be used along with tkinter to provide a complete program.    The System Tray feature is complete and working very well.

The Windowing code is coming together with Reads now operational which means Popups work.  The elements are getting completed on a regular basis.  3 more were just checked in. At least 1 new element is getting completed a week.  

# Web Version (Remi)

 [PySimpleGUIWeb GitHub site](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb).  **There is a separate Readme file for the Web version**.

New for 2019, PySimpleGUIWeb.  This is an exciting development!  PySimpleGUI in your Web Browser!

The underlying framework supplying the web capability is the Python package Remi.  https://github.com/dddomodossola/remi  Remi provides the widgets as well as a web server for you to connect to.  It's an exiting new platform to be running on and has temporarily bumped the WxPython port from the highest priority.  PySimpleGUIWeb is the current high priority project.

Read on and you'll understand even more why this is an important project...

# repl.it Version

***Want to really get your mind blown?***  Check out this [PySimpleGUI program](https://repl.it/@PySimpleGUI/PySimpleGUIWeb-Demos) running in your web browser.

Thanks to the magic of repl.it and Remi it's possible to run PySimpleGUI code in a browser window without having Python running on your computer.  

The programs you write using repl.it will automatically download and install the latest PySimpleGUIWeb from PyPI onto a virtual Python environment.  All that is required is to type `import PySimpleGUIWeb` you'll have a Python environment up and running with the latest PyPI release of PySimpleGUIWeb.  

This is an exciting new development that's opening up all kinds of possibilities for new ways to program and learn PySimpleGUI.   Stayed tuned, much more to be posted about this in the near future.  

Educators in particular should be interested.  Students can not only post their homework easily for their teacher to access, but teachers can also run the students programs online.  No downloading needed.  Run it and check the results.

Depending on how you're viewing this document, you may or may not see an embedded browser window below that is running PySimpleGUI code.

<iframe height="1000px" width="100%" src="https://repl.it/@PySimpleGUI/PySimpleGUIWeb-Demos?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

# Support

PySimpleGUI is an active project.  Bugs are fixed, features are added, often.  Should you run into trouble, open an issue on the GitHub site and you'll receive help by someone in the community.  

# Platforms
 
  It's surprising that Python GUI code is completely cross platform from Windows to Mac to Linux.  No source code changes.  This is true for both  PySimpleGUI and PySimpleGUIQt.
  
However, **Macs** suck.  They suck on tkinter in particular.  The "Look and feel" calls are disabled for Macs.  Colored buttons in particular are broken.  Not in the PySimpleGUI code, of course.    It's mostly because Macs suck.  Consider using Qt instead of tkinter on the Mac.  Or, if using tkinter, bring your own button images. 
      
------------------------------------------------------------------------      
      
      
Looking for a GUI package?     Are you 

* looking to take your Python code from the world of command lines and into the convenience of a GUI?  *      
* sitting on a Raspberry **Pi** with a touchscreen that's going to waste because you don't have the time to learn a GUI SDK?      
* into Machine Learning and are sick of the command line?      
* wanting to distribute your Python code to Windows users as a single .EXE file that launches straight into a GUI, much like a WinForms app?      
* would like to run a program in the system tray?
* a teacher wanting to teach your students how to program using a GUI?
* a student that wants to put a GUI onto their project?
* looking for an active project?
      
Look no further, **you've found your GUI package**.      
      
    import PySimpleGUI as sg      
      
    sg.Popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')      
      
      
![hello world](https://user-images.githubusercontent.com/13696193/44960047-1f7f6380-aec6-11e8-9d5e-12ef935bcade.jpg)      
      
      
Or how about a ***custom GUI*** in 1 line of code?      
      
    import PySimpleGUI as sg      
      
    event, (filename,) = sg.Window('Get filename example'). Layout([[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).Read()    
      
![get filename](https://user-images.githubusercontent.com/13696193/44960039-f1018880-aec5-11e8-8a43-3d7f8ff93b67.jpg)      
      
      
  Build beautiful customized windows that fit your specific problem.  Let PySimpleGUI solve your GUI problem while you solve your real problems.   Look through the Cookbook, find a matching recipe, copy, paste, run within minutes.  This is the process PySimpleGUI was designed to facilitate.      

Your windows don't have to look like "boring" old windows.  Add a few custom graphics to your windows to polish things up.
      
![batterup2](https://user-images.githubusercontent.com/13696193/50378902-6aa2bb00-060a-11e9-8f2f-d746694fa4ee.gif)
    

![uno_final](https://user-images.githubusercontent.com/13696193/49945232-67952580-feba-11e8-90c8-7dc31c5f7c67.gif)     
      


PySimpleGUI wraps tkinter or Qt so that you get all the same widgets as you would tkinter/Qt, but you interact with them in a more friendly way.  It does the layout and boilerplate code for you and presents you with a simple, efficient interface.      
      
           
![everything dark theme](https://user-images.githubusercontent.com/13696193/44959854-b1d23800-aec3-11e8-90b6-5af915a86d15.jpg)      
      
Perhaps you're looking for a way to interact with your **Raspberry Pi** in a more friendly way.  The same for shown as on Pi (roughly the same)      
      
![raspberry pi everything demo](https://user-images.githubusercontent.com/13696193/44279694-5b58ce80-a220-11e8-9ab6-d6021f5a944f.jpg)      
      
      
 

 
In addition to a primary GUI, you can add a Progress Meter to your code with ONE LINE of code.  Slide this line into any of your `for` loops and get a nice meter:      
      
    OneLineProgressMeter('My meter title', current_value, max value, 'key')      
      
  ![easyprogressmeter](https://user-images.githubusercontent.com/13696193/44960065-83099100-aec6-11e8-8aa8-96e4b100a0e4.jpg)      
      
It's simple to show animated GIFs. 
      
![loading animation](https://user-images.githubusercontent.com/13696193/51280871-d2041e80-19ae-11e9-8757-802eb95352ed.gif)      
      
      
How about embedding a game inside of a GUI?  This game of Pong is written in tkinter and then dropped into the PySimpleGUI window creating a game that has an accompanying GUI.      
      
![pong](https://user-images.githubusercontent.com/13696193/45860012-2d8d0b00-bd33-11e8-9efd-3eaf4c30f324.gif)      
      
      
Combining PySimpleGUI with PyInstaller creates something truly remarkable and special, a Python program that looks like a Windows WinForms application.  This application with working menu was created in 20 lines of Python code.  It is a single .EXE file that launches straight into the screen you see.  And more good news, the only icon you see on the taskbar is the window itself... there is no pesky shell window.      
      
![menu demo](https://user-images.githubusercontent.com/13696193/45923097-8fbc4c00-beaa-11e8-87d2-01a5331811c8.gif)      
      
      
  ## Background      
I was frustrated by having to deal with the dos prompt when I had a powerful Windows machine right in front of me.  Why is it SO difficult to do even the simplest of input/output to a window in Python??      
      
There are a number of 'easy to use' Python GUIs, but they were too limited for my requirements.  PySimpleGUI aims for the same simplicity found in packages like `EasyGUI`and `WxSimpleGUI` , both really handy but limited, and adds the ability to define your own layouts.   This ability to make your own windows using a large palette of widgets is but one difference  between the existing "simple" packages and `PySimpleGUI`.      
      
With a simple GUI, it becomes practical to "associate" .py files with the python interpreter on Windows.  Double click a py file and up pops a GUI window, a more pleasant experience than opening a dos Window and typing a command line.      
      
The `PySimpleGUI` package is focused on the ***developer***.      
> Create a custom GUI with as little and as simple code as possible.      
      
This was the primary focus used to create PySimpleGUI.      
      
> "Do it in a Python-like way"      
      
was the second.      
      
## Features      
      
While simple to use, PySimpleGUI has significant depth to be explored by more advanced programmers.  The feature set goes way beyond the requirements of a beginner programmer, and into the  required features needed for complex GUIs.      
      
    Features of PySimpleGUI include:      
        Support for Python versions 2.7 and 3      
        Text      
        Single Line Input      
        Buttons including these types:      
            File Browse      
            Files Browse      
            Folder Browse      
            SaveAs      
            Non-closing return      
            Close window      
            Realtime      
            Calendar chooser      
            Color chooser   
            Button Menu   
        Checkboxes      
        Radio Buttons      
        Listbox      
        Option Menu 
        Menubar
        Button Menu     
        Slider      
        Dial
        Graph      
        Frame with title      
        Icons      
        Multi-line Text Input      
        Scroll-able Output      
        Images      
        Tables    
        Trees    
        Progress Bar            Async/Non-Blocking Windows      
        Tabbed windows      
        Paned windows
        Persistent Windows      
        Redirect Python Output/Errors to scrolling window      
        'Higher level' APIs (e.g. MessageBox, YesNobox, ...)      
        Single-Line-Of-Code Proress Bar & Debug Print      
        Complete control of colors, look and feel      
        Selection of pre-defined palettes      
        Button images      
        Horizontal and Verticle Separators
        Return values as dictionary      
        Set focus      
        Bind return key to buttons      
        Group widgets into a column and place into window anywhere      
        Scrollable columns      
        Keyboard low-level key capture      
        Mouse scroll-wheel support      
        Get Listbox values as they are selected      
        Get slider, spinner, combo as they are changed      
        Update elements in a live window      
        Bulk window-fill operation      
        Save / Load window to/from disk      
        Borderless (no titlebar) windows      
        Always on top windows      
        Menus with ALT-hotkey    
        Right click pop-up menu  
        Tooltips      
        Clickable links    
        Transparent windows
        Movable windows  
        Animated GIFs
        No async programming required (no callbacks to worry about)      
      
      
An example of many widgets used on a single window.  A little further down you'll find the 21 lines of code required to create this complex window.  Try it if you don't believe it.  Install PySimpleGUI then :      
      
>Start Python, copy and paste the code below into the >>> prompt and hit enter. This will pop up...      
>      
      
![everything example](https://user-images.githubusercontent.com/13696193/43097412-0a4652aa-8e8a-11e8-8e09-939484e3c568.jpg)      
      
      
      
    import PySimpleGUI as sg      
      
    layout = [[sg.Text('All graphic widgets in one window!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],      
       [sg.Text('Here is some text.... and a place to enter text')],      
       [sg.InputText()],      
       [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],      
       [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],      
       [sg.Multiline(default_text='This is the default Text shoulsd you decide not to type anything',)],      
    [sg.InputCombo(['Combobox 1', 'Combobox 2'], size=(20, 3)),      
     sg.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],      
    [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6)),      
     sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=25),      
     sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=75),      
     sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=10)],      
    [sg.Text('_'  * 100, size=(70, 1))],      
    [sg.Text('Choose Source and Destination Folders', size=(35, 1))],      
    [sg.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Source'),      
     sg.FolderBrowse()],      
    [sg.Text('Destination Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Dest'),      
     sg.FolderBrowse()],      
    [sg.Submit(), sg.Cancel(), sg.Button('Customized', button_color=('white', 'green'))]]      
      
    event, values  = sg.Window('Everything bagel', auto_size_text=True, default_element_size=(40, 1)).Layout(layout).Read()    
      
      
      
---      
### Design Goals      
      
> Copy, Paste, Run.      
      
`PySimpleGUI's` goal with the API is to be easy on the programmer, and to function in a Python-like way. Since GUIs are visual, it was desirable for the code to visually match what's on the screen.  By providing a significant amount of documentation and an easy to use Cookbook, it's possible to see your first GUI within 5 minutes of beginning the installation.      
      
  > Be Pythonic      
      
 Be Pythonic... Attempted to use language constructs in a natural way and to exploit some of Python's interesting features.  Python's lists and optional parameters make PySimpleGUI work smoothly.      
      
 - windows are represented as Python lists.      
    - A window is a list of rows      
   - A row is a list of elements      
- Return values are a list of button presses and input values.      
- Return values can also be represented as a dictionary      
- The SDK calls collapse down into a single line of Python code that presents a custom GUI and returns values      
-  Linear programming instead of callbacks      
      
 #### Lofty Goals      
      
>  Change Python      
      
The hope is not that ***this*** package will become part of the Python Standard Library.      
      
The hope is that Python will become ***the*** go-to language for creating GUI programs that run on Windows, Mac, and Linux *for all levels of developer*.      
      
The hope is that beginners that are interested in graphic design will have an easy way to express themselves, right from the start of their Python experience.      
      
There is a noticeable gap in the Python GUI solution.  Fill that gap and who knows what will happen.      
      
Maybe there's no "there there".  ***Or*** maybe a simple GUI API will enable Python to dominate yet another computing discipline like it has so many others.   This is my attempt to find out.      
      
      
  -----      
# Getting Started with PySimpleGUI      
      
## Installing PySimpleGUI

### Installing  Python 3      
      
    pip install --upgrade PySimpleGUI      
      
On some systems you need to run pip3.      
      
    pip3 install --upgrade PySimpleGUI      
      
On a Raspberry Pi, this is should work:      
      
    sudo pip3 install --upgrade pysimplegui      
      
Some users have found that upgrading required using an extra flag on the pip `--no-cache-dir`.      
      
    pip install --upgrade --no-cache-dir      
      
On some versions of Linux you will need to first install pip.  Need the Chicken before you can get the Egg (get it... Egg?)      
      
`sudo apt install python3-pip `      
      
If for some reason you are unable to install using `pip`, don't worry, you can still import PySimpleGUI by downloading the file PySimleGUI.py and placing it in your folder along with the application that is importing it.      
      
`tkinter` is a requirement for PySimpleGUI (the only requirement).  Some OS variants, such as Ubuntu, do not some with `tkinter` already installed.  If you get an error similar to:      
```      
ImportError: No module named tkinter      
```      
then you need to install `tkinter`. 
For python 2.7

```sudo apt-get install python-tk  ```   

For python 3
```sudo apt-get install python3-tk  ```      

More information about installing tkinter can be found here: https://www.techinfected.net/2015/09/how-to-install-and-use-tkinter-in-ubuntu-debian-linux-mint.html
      
      
### Installing for Python 2.7      
      
`  pip install --upgrade PySimpleGUI27`    
  or    
` pip2 install --upgrade PySimpleGUI27`    
    
You may need to also install "future" for version 2.7    
    
    pip install future    
  or     
`      pip2 install future`    
    
    
Python 2.7 support is relatively new and the bugs are still being worked out.  I'm unsure what may need to be done to install tkinter for Python 2.7.  Will update this readme when more info is available      
      
Like above, you may have to install either pip or tkinter.  To do this on Python 2.7:      
      
`sudo apt install python-pip`      
      
`sudo apt install python-tkinter`      
    
    
      
### Testing your installation      
      
Once you have installed, or copied the .py file to your app folder, you can test the installation using python.  At the command prompt start up Python.      
      
#### Instructions for Python 2.7:      
```      
python      
>>> import PySimpleGUI27      
>>> PySimpleGUI27.main()      
```      
      
#### Instructions for Python 3:      
      
```      
python3      
>>> import PySimpleGUI      
>>> PySimpleGUI.main()      
```      
      
You will see a sample window in the center of your screen.  If it's not installed correctly you are likely to get an error message during one of those commands      
      
Here is the window you should see:      
      
![sample window](https://user-images.githubusercontent.com/13696193/46097669-79efa500-c190-11e8-885c-e5d4d5d09ea6.jpg)      
      
      
      
### Prerequisites      
Python 2.7 or Python 3      
tkinter      
      
PySimpleGUI Runs on all Python3 platforms that have tkinter running on them.  It has been tested on Windows, Mac, Linux, Raspberry Pi.  Even runs on `pypy3`.      
      
### EXE file creation      
      
If you wish to create an EXE from your PySimpleGUI application, you will need to install `PyInstaller`.  There are instructions on how to create an EXE at the bottom of this ReadMe      
      

## Using  - Python 3      
      
To use in your code, simply import....      
 `import PySimpleGUI as sg`      
      
Then use either "high level" API calls or build your own windows.      
      
    sg.Popup('This is my first Popup')      
      
![first popup](https://user-images.githubusercontent.com/13696193/44957300-c7813680-ae9e-11e8-9a8c-c70198db7907.jpg)      
      
      
Yes, it's just that easy to have a window appear on the screen using Python.  With PySimpleGUI, making a custom window appear isn't much more difficult.  The goal is to get you running on your GUI within ***minutes***, not hours nor days.      
      
## Using  - Python 2.7      
      
Those using Python 2.7 will import a different module name      
 `import PySimpleGUI27 as sg`      
      
## Code Samples Assume Python 3      
      
While all of the code examples you will see in this Readme and the  Cookbook assume Python 3 and thus have an `import PySimpleGUI` at the top, you can run ***all*** of this code on Python 2.7 by changing the import statement to `import PySimpleGUI27`      
      
---      
# APIs      
      
PySimpleGUI can be broken down into 2 types of API's:      
 * High Level single call functions    (The `Popup` calls)      
 * Custom window functions      
      
      
### Python Language Features      
      
 There are a number of Python language features that PySimpleGUI utilizes heavily for API access that should be understood...      
 * Variable number of arguments to a function call      
 * Optional parameters to a function call      
 * Dictionaries      
      
#### Variable Number of Arguments      
      
 The "High Level" API calls that *output* values take a variable number of arguments so that they match a "print" statement as much as possible.  The idea is to make it simple for the programmer to output as many items as desired and in any format.  The user need not convert the variables to be output into the strings.  The PySimpleGUI functions do that for the user.      
      
    sg.Popup('Variable number of parameters example', var1, var2, "etc")      
      
Each new item begins on a new line in the Popup      
      
  ![snap0179](https://user-images.githubusercontent.com/13696193/43658129-f6ca49c6-9725-11e8-9317-1f77443eb04a.jpg)      
      
      
      
#### Optional Parameters to a Function Call      
      
This feature of the Python language is utilized ***heavily*** as a method of customizing windows and window Elements.  Rather than requiring the programmer to specify every possible option for a widget, instead only the options the caller wants to override are specified.      
      
Here is the function definition for the Popup function. The details aren't important.  What is important is seeing that there is a long list of potential tweaks that a caller can make.  However, they don't *have* to be specified on each and every call.      
      
    def Popup(*args,      
               button_color=None,      
               button_type=MSG_BOX_OK,      
               auto_close=False,      
               auto_close_duration=None,      
               icon=DEFAULT_WINDOW_ICON,      
               line_width=MESSAGE_BOX_LINE_WIDTH,      
               font=None):      
      
If the caller wanted to change the button color to be black on yellow, the call would look something like this:      
      
    sg.Popup('This box has a custom button color', button_color=('black', 'yellow'))      
      
      
![snap0180](https://user-images.githubusercontent.com/13696193/43658171-13a72bfe-9726-11e8-8c7a-0a46e46fb202.jpg)      
      
      
#### Dictionaries      
      
Dictionaries are used by more advanced PySimpleGUI users.  You'll know that dictionaries are being used if you see a `key` parameter on any Element.  Dictionaries are used in 2 ways:      
1. To identify values when a window is read      
2. To identify Elements so that they can be "updated"      
      
---      
      
# High Level API Calls  - Popup's      
      
"High level calls" are those that start with "Popup".    They are the most basic form of communications with the user.   They are named after the type of window they create, a pop-up window.  These windows are meant to be short lived while, either delivering information or collecting it, and then quickly disappearing.      
      
## Popup Output      
      
Think of the `Popup` call as the GUI equivalent of a  `print` statement.  It's your way of displaying results to a user in the windowed world.  Each call to Popup will create a new Popup window.      
      
`Popup` calls are normally blocking.  your program will stop executing until the user has closed the Popup window.  A non-blocking window of Popup discussed in the async section.      
      
Just like a print statement, you can pass any number of arguments you wish.  They will all be turned into strings and displayed in the popup window.      
      
There are a number of Popup output calls, each with a slightly different look (e.g. different button labels).      
      
The list of Popup output functions are      
      
    Popup      
    PopupOk      
    PopupYesNo      
    PopupCancel      
    PopupOkCancel      
    PopupError      
    PopupTimed, PopupAutoClose      
    PopupNoWait, PopupNonBlocking      
      
The trailing portion of the function name after Popup indicates what buttons are shown.  `PopupYesNo` shows a pair of button with Yes and No on them.   `PopupCancel` has a Cancel button, etc.      
      
While these are "output" windows, they do collect input in the form of buttons.  The Popup functions return the button that was clicked.  If the Ok button was clicked, then Popup returns the string 'Ok'.  If the user clicked the X button to close the window, then the button value returned is `None`.      
      
The function `PopupTimed` or `PopupAutoClose` are popup windows that will automatically close after come period of time.      
      
Here is a quick-reference showing how the Popup calls look.      
      
      
    sg.Popup('Popup')  - Shows OK button    
    sg.PopupOk('PopupOk')  - Shows OK button    
    sg.PopupYesNo('PopupYesNo')  - Shows Yes and No buttons    
    sg.PopupCancel('PopupCancel')  - Shows Cancelled button    
    sg.PopupOKCancel('PopupOKCancel')  - Shows OK and Cancel buttons    
    sg.PopupError('PopupError')  - Shows red error button    
    sg.PopupTimed('PopupTimed')  - Automatically closes    
    sg.PopupAutoClose('PopupAutoClose')  - Same as PopupTimed    
      
      
      
![snap0256](https://user-images.githubusercontent.com/13696193/44957394-1380ab00-aea0-11e8-98b1-1ab7d7bd5b37.jpg)      
      
![snap0257](https://user-images.githubusercontent.com/13696193/44957400-167b9b80-aea0-11e8-9d42-2314f24e62de.jpg)      
      
![snap0258](https://user-images.githubusercontent.com/13696193/44957399-154a6e80-aea0-11e8-9580-e716f839d400.jpg)      
      
![snap0259](https://user-images.githubusercontent.com/13696193/44957398-14b1d800-aea0-11e8-9e88-c2b36a248447.jpg)      
      
![snap0260](https://user-images.githubusercontent.com/13696193/44957397-14b1d800-aea0-11e8-950b-6d0b4f33841a.jpg)      
      
![snap0261](https://user-images.githubusercontent.com/13696193/44957396-14194180-aea0-11e8-8eef-bb2e1193ecfa.jpg)      
      
![snap0264](https://user-images.githubusercontent.com/13696193/44957595-9e15da00-aea1-11e8-8909-6b6121b74509.jpg)      
      
    
    Popup(*args,  Variable number of arguments you want to display    
        button_color=None, Color of buttons (text_color, background_color)    
        background_color=None, Color of background    
        text_color=None, Color of text    
        button_type=POPUP_BUTTONS_OK, Type of button layout    
        auto_close=False, If True window will automatically close    
        auto_close_duration=None, Number of seconds for autoclose    
        non_blocking=False, If True returns immediately    
        icon=DEFAULT_WINDOW_ICON, Icon to use on the taskbar    
        line_width=None, Width of lines in characters    
        font=None, Font to use for characters    
        no_titlebar=False, If True no titlebar will be shown    
        grab_anywhere=False, If True can move window by grabbing anywhere    
        keep_on_top=False, If True window will be on top of other windows    
        location=(None,None)): (x,y) coordinates to show the window    
    
    
The other output Popups are variations on parameters.  Usually the button_type parameter is the primary one changed.      
    
The choices for button_type are:    
```    
POPUP_BUTTONS_YES_NO    
POPUP_BUTTONS_CANCELLED    
POPUP_BUTTONS_ERROR    
POPUP_BUTTONS_OK_CANCEL    
POPUP_BUTTONS_OK    
POPUP_BUTTONS_NO_BUTTONS    
```    
Note that you should not call Popup yourself with different button_types.  Rely on the Popup function named that sets that value for you.  For example PopupYesNo will set the button type to POPUP_BUTTONS_YES_NO for you.    
    
    
#### Scrolled Output      
There is a scrolled version of Popups should you have a lot of information to display.      

```python
PopupScrolled(*args, button_color=None, yes_no=False, auto_close=False, auto_close_duration=None, size=(None, None), location=(None, None), title=None, non_blocking=False)
```      
Typical usage:

    sg.PopupScrolled(my_text)  

    
      
![scrolledtextbox 2](https://user-images.githubusercontent.com/13696193/43667324-712aa0d4-9745-11e8-83a9-a0d0570d0865.jpg)      
      
      
The `PopupScrolled` will auto-fit the window size to the size of the text.  Specify `None` in the height field of a `size` parameter to get auto-sized height.      
      
This call will create a scrolled box 80 characters wide and a height dependent upon the number of lines of text.      
      
sg.PopupScrolled(my_text, size=(80, None))      
      
Note that the default max number of lines before scrolling happens is set to 50. At 50 lines the scrolling will begin.     

If `non_blocking` parameter is set, then  the call will not blocking waiting for the user to close the window.  Execution will immediately return to the user.  Handy when you want to dump out debug info without disrupting the program flow.
      
### PopupNoWait      
      
The Popup call PopupNoWait or PopupNonBlocking will create a popup window and then immediately return control back to you.  All other popup functions will block, waiting for the user to close the popup window.      
      
This function is very handy for when you're **debugging** and want to display something as output but don't want to change the programs's overall timing by blocking.  Think of it like a `print` statement. There are no return values on one of these Popups.    
      
      
      
## Popup Input      
      
There are Popup calls for single-item inputs. These follow the pattern of `Popup` followed by `Get` and then the type of item to get.  There are 3 of these input Popups to choose from, each with settings enabling customization.    
      
 - `PopupGetText` - get a single line of text      
 - `PopupGetFile` - get a filename      
 - `PopupGetFolder` - get a folder name      
      
Use these Popups instead of making  a custom window to get one data value, call the Popup input function to get the item from the user.  If you find the parameters are unable to create the kind of window you are looking for, then it's time for you to create your own window.    
      
### PopupGetText      
    
Use this Popup to get a line of text from the user.    
    
```    
PopupGetText(message,The message you wish to display with the input field    
           default_text='', Text to initially fill into the input field    
           password_char='', Passwork character if this is a password field    
           size=(None,None), Size of the window    
           button_color=None, Color to use for buttons (foreground, background)    
           background_color=None, Background color for window    
           text_color=None, Text color for window    
           icon=DEFAULT_WINDOW_ICON, Icon to display on taskbar    
           font=None, Font to use for text    
           no_titlebar=False, If True no titlebar will be shown    
           grab_anywhere=False, If True can grab anywhere to move the window    
           keep_on_top=False, If True window will stay on top of other windows    
           location=(None,None))  Location on screen to display window    
```        
    
    import PySimpleGUI as sg      
      
    text = sg.PopupGetText('Title', 'Please input something')      
    sg.Popup('Results', 'The value returned from PopupGetText', text)      
      
  ![popupgettext](https://user-images.githubusercontent.com/13696193/44957281-8721b880-ae9e-11e8-98cd-d06369f4187e.jpg)      
      
![popup gettext response](https://user-images.githubusercontent.com/13696193/44957282-8721b880-ae9e-11e8-84ae-dc8bb30504a0.jpg)      
      
### PopupGetFile      
    
Gets a filename from the user.  There are options to configure the type of dialog box to show.  Normally an "Open File" dialog box is shown    
```    
PopupGetFile(message, Message to show in the window    
          default_path='', Path browsing should start from    
          default_extension='', Which filetype is the default    
          save_as=False, Determines which dialog box stype to show    
          file_types=(("ALL Files", "*.*"),), Which filetypes are displayed    
          no_window=False, if True no window is displayed except the dialog box    
          size=(None,None), Size of window    
          button_color=None, Color of buttons    
          background_color=None, Color of window background    
          text_color=None, Color of text in window    
          icon=DEFAULT_WINDOW_ICON, Icon to show on taskbar    
          font=None, Font to use    
          no_titlebar=False, If True does not display a titlebar    
          grab_anywhere=False, if True can grab window anywhere to move it    
          keep_on_top=False, if True window will be on top of others    
          location=(None,None)) Location on screen to show window    
```    
    
If configured as an Open File Popup then (save_as is not True)  the dialog box will look like this    
    
    
![snag-0060](https://user-images.githubusercontent.com/13696193/46761050-9831c680-cca1-11e8-8de9-68b15efe2c46.jpg)    
    
    
    
If you set the parameter save_As to True, then the dialog box looks like this:    
    
![snag-0061](https://user-images.githubusercontent.com/13696193/46761330-2b6afc00-cca2-11e8-953b-f6b5c5ce57f5.jpg)    
    
If you choose a filename that already exists, you'll get a warning popup box asking if it's OK.  You can also specify a file that doesn't exist.  With an "Open" dialog box you cannot choose a non-existing file.    
    
A typical call produces this window.    
    
    text = sg.PopupGetFile('Please enter a file name')      
    sg.Popup('Results', 'The value returned from PopupGetFile', text)      
      
![popupgetfile](https://user-images.githubusercontent.com/13696193/44957857-2fd31680-aea5-11e8-8eb7-f6b91c202cc8.jpg)      
      
    
    
### PopupGetFolder    
    
The window created to get a folder name looks the same as the get a file name.  The difference is in what the browse button does.  `PopupGetFile` shows an Open File dialog box while `PopupGetFolder`  shows an Open Folder dialog box.      
    
```    
PopupGetFolder(message,  Message to display in window    
            default_path='',  Path to start browsing    
            no_window=False,  If True no window will be shown    
            size=(None,None), Size of window    
            button_color=None, Color of buttons    
            background_color=None, Background color of window    
            text_color=None,  Color of window text    
            icon=DEFAULT_WINDOW_ICON, Icon to show on taskbar    
            font=None,  Font to use for window    
            no_titlebar=False,  If True no titlebar will be shown    
            grab_anywhere=False,  If True can grab anywhere on window to move    
            keep_on_top=False,  If True window will be on top    
            location=(None, None))  Location on screen to create window    
```    
    
This is a typpical call    
      
    text = sg.PopupGetFolder('Please enter a folder name')      
    sg.Popup('Results', 'The value returned from PopupGetFolder', text)      
      
![popupgetfolder](https://user-images.githubusercontent.com/13696193/44957861-45484080-aea5-11e8-926c-cf607a45251c.jpg)      
      
    
### PopupAnimated
 
 ![ring](https://user-images.githubusercontent.com/13696193/51296743-6ee4ad00-19eb-11e9-91f5-cd8086ad1b50.gif)

The animated Popup enables you to easily display a "loading" style animation specified through a GIF file that is either stored in a file or a base64 variable.

```python
def PopupAnimated(image_source, 
			      message=None,
			      background_color=None, 
			      text_color=None, 
			      font=None, 
			      no_titlebar=True, 
			      grab_anywhere=True, 
			      keep_on_top=True, 
			      location=(None, None), 
			      alpha_channel=.8,
			      time_between_frames=0)
```
image_source - The GIF file specified as a string filename or a base64 variable
message - optional text message to be displayed under the animation
background_color - the background color to use for the window and all of the other parts of the window
text_color - color to use for optional text
font - font to use for the optional text
no_titlebar - no titlebar window setting
location - location to show the window
alpha_channel - alpha channel to use for the window
time_between_frames - amount of time in milliseconds to use between frames

***To close animated popups***, call PopupAnimated with `image_source=None`.  This will close all of the currently open PopupAnimated windows.
    

# Progress Meters!      
We all have loops in our code.  'Isn't it joyful waiting, watching a counter scrolling past in a text window?  How about one line of code to get a progress meter, that contains statistics about your code?      
      
      
    OneLineProgressMeter(title,      
                      current_value,      
                      max_value,      
                      key,      
                      *args,      
                      orientation=None,      
                      bar_color=DEFAULT_PROGRESS_BAR_COLOR,      
                      button_color=None,      
                      size=DEFAULT_PROGRESS_BAR_SIZE,      
                      border_width=DEFAULT_PROGRESS_BAR_BORDER_WIDTH):      
      
Here's the one-line Progress Meter in action!      
      
    for i in range(1,10000):      
        sg.OneLineProgressMeter('My Meter', i+1, 10000, 'key','Optional message')      
      
That line of code resulted in this window popping up and updating.      
      
![preogress meter](https://user-images.githubusercontent.com/13696193/43667625-d47da702-9746-11e8-91e6-e5177883abae.jpg)      
      
A meter AND fun statistics to watch while your machine grinds away, all for the price of 1 line of code.      
With a little trickery you can provide a way to break out of your loop using the Progress Meter window.  The cancel button results in a `False` return value from `OneLineProgressMeter`.  It normally returns `True`.      
      
***Be sure and add one to your loop counter*** so that your counter goes from 1 to the max value.  If you do not add one, your counter will never hit the max value.  Instead it will go from 0 to max-1.      
      
# Debug Output      
Another call in the 'Easy' families of APIs is `EasyPrint`.  It will output to a debug window.  If the debug window isn't open, then the first call will open it.  No need to do anything but stick a 'print' call in your code. You can even replace your 'print' calls with calls to EasyPrint by simply sticking the statement      
      
    print = sg.EasyPrint      
      
at the top of your code.      

There are a number of names for the same EasyPrint function.  `Print` is one of the better ones to use as it's easy to remember.   It is simply `print` with a capital P.      
      
    import PySimpleGUI as sg      
      
    for i in range(100):      
        sg.Print(i)      
      
![snap0125](https://user-images.githubusercontent.com/13696193/43114979-a696189e-8ecf-11e8-83c7-473fcf0ccc66.jpg)      
    
Or if you didn't want to change your code:      
      
    import PySimpleGUI as sg      
      
    print=sg.Print      
    for i in range(100):      
        print(i)      
      
Just like the standard print call, `EasyPrint` supports the `sep` and `end` keyword arguments.  Other names that can be used to call `EasyPrint` include `Print`, `eprint`,   If you want to close the window, call the function `EasyPrintClose`.      
       
You can change the size of the debug window using the `SetOptions` call with the `debug_win_size` parameter.      
    
There is an option to tell PySimpleGUI to reroute all of your stdout and stderr output to this window.  To do so call EasyPrint with the parameter `do_not_reroute_stdout` set to True.  After calling it once with this parameter set to True, all future calls to a normal`print` will go to the debug window.
    
If you close the debug window it will re-open the next time you Print to it.
      
---      
# Custom window API Calls  (Your First window)      
      
This is the FUN part of the programming of this GUI.  In order to really get the most out of the API, you should be using an IDE that supports auto complete or will show you the definition of the function.  This will make customizing go  smoother.      
      
This first section on custom windows is for your typical, blocking, non-persistent window.  By this I mean, when you "show" the window, the function will not return until the user has clicked a button or closed the window.  When this happens, the window will be automatically closed.      
      
Two other types of windows exist.      
1. Persistent window - rather than closing on button clicks, the show window function returns and the window continues to be visible.  This is good for applications like a chat window.      
2. Asynchronous window - the trickiest of the lot. Great care must be exercised.  Examples are an MP3 player or status dashboard.  Async windows are updated (refreshed) on a periodic basis.      
      
It's both not enjoyable nor helpful to immediately jump into tweaking each and every little thing available to you.      
      
## The window Designer      
    
The good news to newcomers to GUI programming is that PySimpleGUI has a window designer.  Better yet, the window designer requires no training, no downloads, and everyone knows how to use it.      
      
![gui0_1](https://user-images.githubusercontent.com/13696193/44159598-e2257400-a085-11e8-9b02-343e72cc75c3.JPG)      
      
It's a manual process, but if you follow the instructions, it will take only a minute to do and the result will be a nice looking GUI.  The steps you'll take are:      
1. Sketch your GUI on paper      
2. Divide your GUI up into rows      
3. Label each Element with the Element name      
4. Write your Python code using the labels as pseudo-code      
      
Let's take a couple of examples.      
      
**Enter a number**.... Popular beginner programs are often based on a game or logic puzzle that requires the user to enter something, like a number.  The "high-low" answer game comes to mind where you try to guess the number based on high or low tips.      
      
**Step 1- Sketch the GUI**      
![gui1_1](https://user-images.githubusercontent.com/13696193/44160127-6a584900-a087-11e8-8fec-09099a8e16f6.JPG)      
      
**Step 2 - Divide into rows**      
      
![gui2_1](https://user-images.githubusercontent.com/13696193/44160128-6a584900-a087-11e8-9973-af866fb94c56.JPG)      
      
Step 3 - Label elements      
      
![gui6_1](https://user-images.githubusercontent.com/13696193/44160116-64626800-a087-11e8-8b57-671c0461b508.JPG)      
      
Step 4 - Write the code      
The code we're writing is the layout of the GUI itself.  This tutorial only focuses on getting the window code written, not the stuff to display it, get results.      
      
We have only 1 element on the first row, some text.  Rows are written as a "list of elements", so we'll need [  ] to make a list.  Here's the code for row 1      
      
    [ sg.Text('Enter a number') ]      
      
Row 2 has 1 elements, an input field.      
      
    [ sg.Input() ]      
Row 3 has an OK button      
      
    [ sg.OK() ]      
      
Now that we've got the 3 rows defined, they are put into a list that represents the entire window.      
      
    layout = [ [sg.Text('Enter a Number')],      
               [sg.Input()],      
               [sg.OK()] ]      
      
Finally we can put it all together into a program that will display our window.      
      
    import PySimpleGUI as sg      
      
    layout = [[sg.Text('Enter a Number')],      
              [sg.Input()],      
              [sg.OK()] ]      
      
    event, (number,) = sg.Window('Enter a number example').Layout(layout).Read()    
      
    sg.Popup(event, number)      
      
### Example 2 - Get a filename      
Let's say you've got a utility you've written that operates on some input file and you're ready to use a GUI to enter than filename rather than the command line.  Follow the same steps as the previous example - draw your window on paper, break it up into rows, label the elements.      
      
![gui4_1](https://user-images.githubusercontent.com/13696193/44160132-6a584900-a087-11e8-862f-7d791a67ee5d.JPG)      
![gui5_1](https://user-images.githubusercontent.com/13696193/44160133-6af0df80-a087-11e8-9dec-bb4d4c59393d.JPG)      
      
Writing the code for this one is just as straightforward.  There is one tricky thing, that browse for a file button.  Thankfully PySimpleGUI takes care of associating it with the input field next to it.  As a result, the code looks almost exactly like the window on the paper.      
      
    import PySimpleGUI as sg      
      
    layout = [[sg.Text('Filename')],      
              [sg.Input(), sg.FileBrowse()],      
              [sg.OK(), sg.Cancel()] ]      
      
    event, (number,) = sg.Window('Get filename example').Layout(layout).Read()    
      
    sg.Popup(event, number)      
      
      
Read on for detailed instructions on the calls that show the window and return your results.      
      
      
      
# Copy these design patterns!      
      
All of your PySimpleGUI programs will utilize one of these 2 design patterns depending on the type of window you're implementing.      
      
      
## Pattern 1 - "One-shot Window" - Read into list or dictionary (**The Most Common** Pattern)    
      
This will be the most common pattern you'll follow if you are not using an "event loop" (not reading the window multiple times).  The window is read and closes.
    
It's unusual to assign the values returned from the read call directly into user variables.  Usually the variables are grouped together into a list or dictionary of multiple return values.    
    
```python    
import PySimpleGUI as sg      
    
window_rows = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],      
                 [sg.InputText(), sg.FileBrowse()],      
                 [sg.Submit(), sg.Cancel()]]      
      
window = sg.Window('SHA-1 & 256 Hash').Layout(window_rows)    
    
event, values = window.Read()    
window.Close()
    
source_filename = values[0]    
```    
    
    
## Pattern 2 A - Persistent window (multiple reads using an event loop)      
      
Some of the more advanced programs operate with the window remaining visible on the screen.  Input values are collected, but rather than closing the window, it is kept visible acting as a way to both output information to the user and gather input data.      
    
This code will present a window and will print values until the user clicks the exit button or closes window using an X.    
      
```python    
import PySimpleGUI as sg      
      
layout = [[sg.Text('Persistent window')],      
          [sg.Input(do_not_clear=True)],      
          [sg.Button('Read'), sg.Exit()]]      
      
window = sg.Window('Window that stays open').Layout(layout)      
      
while True:      
    event, values = window.Read()      
    if event is None or event == 'Exit':      
        break      
    print(event, values)    

window.Close()
```    

## Pattern 2 B - Persistent window (multiple reads using an event loop + updates data in window)   

This is a slightly more complex, but maybe more realistic version that reads input from the user and displays that input as text in the window.  Your program is likely to be doing both of those activities so this will give you a big jump-start.

Do not worry yet what all of these statements mean.   Just copy it so you can begin to play with it, make some changes.  Experiment to see how thing work.

A final note... the parameter `do_not_clear` in the input call determines the action of the input field after a button event.  If this value is True, the input value remains visible following button clicks.  If False, then the input field is CLEARED of whatever was input.  If you are building a "Form" type of window with data entry, you likely want False, the default setting (you can remove the parameter completely).

```python
import sys  
if sys.version_info[0] >= 3:  
    import PySimpleGUI as sg  
else:  
    import PySimpleGUI27 as sg  
  
layout = [[sg.Text('Your typed chars appear here:'), sg.Text('', key='_OUTPUT_') ],  
          [sg.Input(do_not_clear=True, key='_IN_')],  
          [sg.Button('Show'), sg.Button('Exit')]]  
  
window = sg.Window('Window Title').Layout(layout)  
  
while True:                 # Event Loop  
  event, values = window.Read()  
  print(event, values)
  if event is None or event == 'Exit':  
      break  
  if event == 'Show':  
      # change the "output" element to be the value of "input" element  
      window.FindElement('_OUTPUT_').Update(values['_IN_'])

window.Close()
```

     
      
## How GUI Programming in Python Should Look?  At least for beginners ?    
      
While one goal was making it simple to create a GUI another just as important goal was to do it in a Pythonic manner. Whether it achieved these goals is debatable, but it was an attempt just the same.      
      
The key to custom windows in PySimpleGUI is to view windows as ROWS of GUI  Elements.  Each row is specified as a list of these Elements.  Put the rows together and you've got a window.  This means the GUI is defined as a series of Lists, a Pythonic way of looking at things.    
      
 Let's dissect this little program     
 ```python    
    import PySimpleGUI as sg      
      
    layout = [[sg.Text('Rename files or folders')],      
              [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],      
              [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],      
              [sg.Submit(), sg.Cancel()]]      
      
    window = sg.Window('Rename Files or Folders')      
      
    event, values = window.Layout(layout).Read()    
   ```    
      
      
![snap0131](https://user-images.githubusercontent.com/13696193/43417007-df6d8408-9407-11e8-9986-30f0415f08a5.jpg)      
      
Let's agree the window has 4 rows.      
      
The first row only has **text** that reads `Rename files or folders`      
      
The second row has 3 elements in it.  First the **text** `Source for Folders`, then an **input** field, then a **browse** button.      
      
Now let's look at how those 2 rows and the other two row from Python code:      
      
    layout = [[sg.Text('Rename files or folders')],      
              [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],      
              [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],      
              [sg.Submit(), sg.Cancel()]]      
      
See how the source code mirrors the layout?  You simply make lists for each row, then submit that table to PySimpleGUI to show and get values from.      
      
And what about those return values?  Most people simply want to show a window, get the input values and do something with them.  So why break up the code into button callbacks, etc, when I simply want my window's input values to be given to me.      
      
For return values the window is scanned from top to bottom, left to right.  Each field that's an input field will occupy a spot in the return values.      
      
In our example window, there are 2 fields, so the return values from this window will be a list with 2 values in it.      
  ```python    
  event, values = window.Read()    
  folder_path, file_path = values    
  ```    
      
In one statement we both show the window and read the user's inputs.  In the next the *list* of return values is split into individual variables `folder_path` and `file_path`.    
      
Isn't this what a Python programmer looking for a GUI wants? Something easy to work with to get the values and move on to the rest of the program, where the real action is taking place.  Why write pages of GUI code when the same layout can be achieved with PySimpleGUI in 3 or 4 lines of code.  4 lines or 40?  Most would choose 4.    
      
      
## Return values      
      
   As of version 2.8 there are 2 forms of return values, list and dictionary.   
  
### Two Return Values     
  
All Window Read calls return 2 values.  By convention a read statement is written:  
```python  
event, values = window.Read()      
```  
  
You don't HAVE to write your reads in this way. You can name your variables however you want.  But if you want to code them in a way that other programmers using PySimpleGUI are used to, then use these statements.  

## Events
  
The first parameter `event` describes **why** the read completed.  Events are one of these:  
  
For all Windows:  
  
* Button click  
* Window closed using X  
  
For Windows that have specifically enabled these.  Please see the appropriate section in this document to learn about how to enable these and what the event return values are.  
  
* Keyboard key press  
* Mouse wheel up/down  
* Menu item selected  
* An Element Changed (slider, spinner, etc)  
* A list item was clicked  
* Return key was pressed in input element  
* Timeout waiting for event
* Text was clicked
* Combobox item chosen
* Table row selected
* etc

***Most*** of the time the event will be a button click or the window was closed.  
  
### Window closed event
    
Another convention to follow is the check for windows being closed with an X.  This is an important event to catch.  If you don't check for this and you attempt to use the window, your program will crash.  Please check for closed window and exit your program gracefully.  
  
To check for a closed window use this line of code:  
  
    if event is None:  
  
Putting it all together we end up with an "event loop" that looks something like this:
```python
while True:
    event, values = window.Read()
    if event is None:
        break
```
### Button Click Events

By default buttons will always return a click event, or in the case of realtime buttons, a button down event.  You don't have to do anything to enable button clicks.  To disable the events, disable the button using its Update method.

You can enable an additional "Button Modified" event by setting `enable_events=True` in the Button call.  These events are triggered when something 'writes' to a button, ***usually*** it's because the button is listed as a "target" in another button.
   
The button value from a Read call will be one of 2 values:      
1. The Button's text      - Default
2. The Button's key      - If a key is specified
  
If a button has a key set when it was created, then that key will be returned.  If no key is set, then the button text is returned.  If no button was clicked, but the window returned anyway, the event value is None.      
      
### **None is returned when the user clicks the X to close a window.**      
      
If your window has an event loop where it is read over and over, remember to give your user an "out".  You should ***always check for a None value*** and it's a good practice to provide an Exit button of some kind. Thus design patterns often resemble this Event Loop:      
      
    while True:      
        event, values = window.Read()      
        if event is None or event == 'Quit':      
            break      
      

### Element Events

Some elements are capable of generating events when something happens to them.  For example, when a slider is moved, or list item clicked on or table row clicked on.  These events are not enabled by default.  To enable events for an Element, set the parameter `enable_events=True`.  This is the same as the older `click_submits` parameter.  You will find the `click_submits` parameter still in the function definition.  You can continue to use it. They are the same setting.  An 'or' of the two values is used.  In the future, click_submits will be removed so please migrate your code to using `enable_events`.

InputText - any change
Combo - item chosen
Option menu - item chosen
Listbox - selection changed
Radio - selection changed
Checkbox - selection changed
Spinner - new item selected
Multiline - any change
Text - clicked
Status Bar - clicked
Graph - clicked
TabGroup - tab clicked
Slider - slider moved
Table - row selected
Tree - node selected
ButtonMenu - menu item chosen
Right click menu - menu item chosen

### Other Events

#### Menubar menu item chosen for MenuBar menus and ButtonMenu menus

You will receive the key for the MenuBar and ButtonMenu.  Use that key to read the value in the return values dictionary.  The value shown will be the full text plus key for the menu item chosen.  Remember that you can put keys onto menu items.  You will get the text and the key together as you defined it in the menu
 definition.

#### Right Click menu item chosen

Unlike menu bar and button menus, you will directly receive the menu item text and its key value.  You will not do a dictionary lookup to get the value.  It is the event code returned from WindowRead().


#### Windows - keyboard, mouse scroll wheel

Windows are capable of returning keyboard events.  These are returned as either a single character or a string if it's a special key.  Experiment is all I can say. The mouse scroll wheel events are also strings.  Put a print in your code to see what's returned.

#### Timeouts

If you set a timeout parameter in your read, then the system TIMEOUT_KEY will be returned.  If you specified your own timeout key in the Read call then that value will be what's returned instead.
  
### The `values` Variable - Return values as a list      
      
The second parameter from a Read call is either a list or a dictionary of the input fields on the Window.  
  
   By default return values are a list of values, one entry for each input field.      
        
Each of the Elements that are Input Elements will have a value in the list of return values.  You can unpack your GUI directly into the variables you want to use.      
      
    event, (filename, folder1, folder2, should_overwrite) = sg.Window('My title').Layout(window_rows).Read()    
      
  Or, more commonly, you can unpack the return results separately.      
      
```python    
event, values = sg.Window('My title').Layout(window_rows).Read()    
event, value_list = window.Layout(window_rows).Read()      
value1 = value_list[0]      
value2 = value_list[1]      
     ...     
```         
However, this method isn't good when you have a lot of input fields.  If you insert a new element into your window then you will have to shuffle your unpacks down, modifying each of the statements to reference `value_list[x]    `.  
  
The more common / advanced method is to request your values be returned as a dictionary.  
  
### `values` Variable - Return values as a dictionary      
      
For those of you that have not encountered a Python dictionary, don't freak out!  Just copy and paste the sample code and modify it. Follow this design pattern and you'll be fine.  And you might learn something along the way.  
  
For windows longer than 3 or 4 fields you will want to use a dictionary to help you organize your return values. In almost all (if not all) of the demo programs you'll find the return values being passed as a dictionary.  It is not a difficult concept to grasp, the syntax is easy to understand, and it makes for very readable code.      
      
The most common window read statement you'll encounter looks something like this:      
      
window = sg.Window("My title").Layout(layout).Read()    
  
      
  To use a dictionary, you will need to:      
 * Mark each input element you wish to be in the dictionary with the keyword `key`.      
      
If **any** element in the window has a `key`, then **all** of the return values are returned via a dictionary.  If some elements do not have a key, then they are numbered starting at zero.      
      
Let's take a look at your first dictionary-based window.      
      
    import PySimpleGUI as sg      
    window = sg.Window('Simple data entry window')      
    layout = [      
              [sg.Text('Please enter your Name, Address, Phone')],      
              [sg.Text('Name', size=(15, 1)), sg.InputText('1', key='_name_')],      
              [sg.Text('Address', size=(15, 1)), sg.InputText('2', key='_address_')],      
              [sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='_phone_')],      
              [sg.Submit(), sg.Cancel()]      
             ]      
      
    event, values = window.Layout(layout).Read()    
      
    sg.Popup(event, values, values['_name_'], values['_address_'], values['_phone_'])      
      
To get the value of an input field, you use whatever value used as the `key` value as the index value.  Thus to get the value of the name field, it is written as      
      
    values['name']      
      
Think of the variable values in the same way as you would a list, however, instead of using 0,1,2, to reference each item in the list, use the values of the key.  The Name field in the window above is referenced by `values['_name_']`.    
  
You will find the key field used quite heavily in most PySimpleGUI windows unless the window is very simple.      
  
Another  convention you'll see in some of the demo programs is keys being named with an underscore at the beginning and the end.  You don't HAVE to do this... your key value may look like this:  
`key = 'name'`  
  
The reason for this naming convention is that when you are scanning the code, these key values jump out at you.   You instantly know it's a key.  Try scanning the code above and see if those keys pop out.  
`key = '_name_'`  
  
  
  


## The Event Loop / Callback Functions      
      
All GUIs have one thing in common, an "event loop".  Usually the GUI framework runs the event loop for you, but sometimes you want greater control and will run your own event loop.  You often hear the term event loop when discussing embedded systems or on a Raspberry Pi.      
    
With PySimpleGUI if your window will remain open following button clicks, then your code will have an event loop. If your program shows a single "one-shot"  window, collects the data and then has no other GUI interaction, then you don't need an event loop.    
      
There's nothing mysterious about event loops... they are loops where you take care of.... wait for it..... *events*.  Events are things like button clicks, key strokes, mouse scroll-wheel up/down.        
      
Let's take a Pi demo program as an example.  This program shows a GUI window, gets button presses, and uses them to control some LEDs.  It loops, reading user input and doing something with it.      
      
This little program has a typical Event Loop      
      
![readme example](https://user-images.githubusercontent.com/13696193/46566965-f4d65f80-c8f6-11e8-91a3-8cebad0cba90.jpg)    
      
      
      
```python    
import PySimpleGUI as sg      
      
layout = [[sg.Text('Click read to read the input value')],      
          [sg.Input()],      
          [sg.RButton('Read'), sg.Exit()]]      
      
window = sg.Window('Persistent GUI Window').Layout(layout)      
      
while True:      
    event, values = window.Read()      
    if event is None or event == 'Exit':      
        break      
    print(event, values)   
window.Close()
```    
       
In the Event Loop we are reading the window and then doing a series of button compares to determine what to do  based on the button that was clicks (value of `button` variable)      
      
The way buttons are presented to the caller in PySimpleGUI is ***not*** how *most* GUI frameworks handle button clicks.  Most GUI frameworks, including tkinter, use ***callback*** functions, a function you define would be called when a button is clicked.  This requires you to write asynchronous code, a concept beginners often stumble on and one that presents a barrier.    
      
There is a more communications that have to happen between parts of your program when using callbacks.  Callbacks break apart your program's logic apart and scatter it.  One of the larger hurdles for beginners to GUI programming are these callback functions.      
      
PySimpleGUI was specifically designed in a way so that callbacks would not be required.  There is no coordination between one function and another required.  You simply read your button click and take appropriate action at the same location in the code as when you read the button value.      
      
Whether or not this is a "proper" design for GUI programs can be debated.  It's not a terrible trade-off to run your own event loop and having a functioning GUI application versus one that maybe never gets written because callback functions were too much to grasp.      
      
  ---      
      
## All Widgets / Elements      
      
This code utilizes many of the common Elements.  It does not include Tabs/Tab Groups.    
```python      
    import PySimpleGUI as sg      
      
    sg.ChangeLookAndFeel('GreenTan')      
      
    # ------ Menu Definition ------ #      
    menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
                ['Help', 'About...'], ]      
      
    # ------ Column Definition ------ #      
    column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      
      
    layout = [      
        [sg.Menu(menu_def, tearoff=True)],      
        [sg.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],      
        [sg.Text('Here is some text.... and a place to enter text')],      
        [sg.InputText('This is my text')],      
        [sg.Frame(layout=[      
        [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],      
        [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],      
        [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),      
         sg.Multiline(default_text='A second multi-line', size=(35, 3))],      
        [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),      
         sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],      
        [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],      
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),      
         sg.Frame('Labelled Group',[[      
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),      
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),      
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),      
         sg.Column(column1, background_color='#F7F3EC')]])],      
        [sg.Text('_'  * 80)],      
        [sg.Text('Choose A Folder', size=(35, 1))],      
        [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
         sg.InputText('Default Folder'), sg.FolderBrowse()],      
        [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]      
    ]      
      
      
    window = sg.Window('Everything bagel', default_element_size=(40, 1), grab_anywhere=False).Layout(layout)      
      
    event, values = window.Read()      
      
    sg.Popup('Title',      
             'The results of the window.',      
             'The button clicked was "{}"'.format(event),      
             'The values are', values)      
```      
This is a somewhat complex window with quite a bit of custom sizing to make things line up well.  This is code you only have to write once.  When looking at the code, remember that what you're seeing is a list of lists.  Each row contains a list of Graphical Elements that are used to create the window.      
      
   ![everything bagel](https://user-images.githubusercontent.com/13696193/45914128-87163800-be0e-11e8-9a83-7ee5960e88b9.jpg)      
      
Clicking the Submit button caused the window call to return.  The call to Popup resulted in this window.      
      
![everything bagel reseults](https://user-images.githubusercontent.com/13696193/45914129-87aece80-be0e-11e8-8aae-9a483a9ad4a6.jpg)      
      
      
**`Note, button value can be None`**.  The value for `button` will be the text that is displayed on the button element when it was created.  If the user closed the window using something other than a button, then `button` will be `None`.   It is ***vitally*** ***important*** that your code contain the proper checks for None.  Always give your users a way out of the window.  Otherwise you'll end up  with windows that never properly close.    
      
You can see in the results Popup window that the values returned are a list.  Each input field in the window generates one item in the return values list.  All input fields return a `string` except for Check Boxes and Radio Buttons.  These return `bool`.      
      
---      
# Building Custom Windows      
      
You will find it ***much easier*** to write code using PySimpleGUI if you use an IDE such as PyCharm.  The features that show you documentation about the API call you are making will help you determine which settings you want to change, if any.  In PyCharm, two commands are particularly helpful.      
      
    Control-Q (when cursor is on function name) brings up a box with the function definition      
    Control-P (when cursor inside function call "()") shows a list of parameters and their default values      
      
## Synchronous windows      
The most common use of PySimpleGUI is to display and collect information from the user.  The most straightforward way to do this is using a "blocking" GUI call.  Execution is "blocked" while waiting for the user to close the GUI window/dialog box.      
You've already seen a number of examples above that use blocking windows.  A truly non-blocking Read call looks like this:
```python
event, values = window.Read(timeout=0)
```
    
You can learn more about these async / non-blocking windows toward the end of this document.    
    
      
# Window Object - Beginning a window      
The first step is to create the window object using the desired window customization.      
        
This is the definition of the Window object:      
      
   
```python
Window( title, 
		default_element_size=DEFAULT_ELEMENT_SIZE,
		default_button_element_size=(None,None),
		auto_size_text=None,
		auto_size_buttons=None,
		location=(None,None),
		size=(None,None),
		element_padding=None,
		button_color=None,
		font=None,
		progress_bar_color=(None,None),
		background_color=None,
		border_depth=None,
		auto_close=False,
		auto_close_duration=DEFAULT_AUTOCLOSE_TIME,
		icon=DEFAULT_WINDOW_ICON,
		force_toplevel=False,
		alpha_channel=1,
		return_keyboard_events=False,
		use_default_focus=True,
		text_justification=None,
		no_titlebar=False,
		grab_anywhere=False,
		keep_on_top=False,
		resizable=False,
		disable_close=False,
		disable_minimize=False,
		right_click_menu=None):     
```      
          
Parameter Descriptions.  You will find these same parameters specified for each `Element` and some of them in `Row` specifications.  The `Element` specified value will take precedence over the `Row` and `window` values.      
      
       default_element_size - Size of elements in window in characters (width, height)      
       default_button_element_size - Size of buttons on this window      
       auto_size_text - Bool. True if elements should size themselves according to contents. Defaults to True      
       auto_size_buttons - Bool. True if button elements should size themselves according to their text label      
       location - (x,y) Location to place window in pixels  
       size - (w,h) forces a window to be a paricular size
       element_padding - (w,h) default padding amount for elements
       font - Font name and size for elements of the window      
       button_color - Default color for buttons (foreground, background). Can be text or hex      
       progress_bar_color - Foreground and background colors for progress bars      
       background_color - Color of the window background      
       border_depth - Amount of 'bezel' to put on input boxes, buttons, etc.      
       auto_close - Bool.  If True window will autoclose      
       auto_close_duration - Duration in seconds before window closes      
       icon - .ICO file that will appear on the Task Bar and end of Title Bar      
       force_top_level - Bool. If set causes a tk.Tk window to be used as primary window rather than tk.TopLevel. Used to get around Matplotlib problem    
       alpha_channel - Float 0 to 1. 0 is invisible, 1 is fully visible, Anything between will be semi-transparent 
       return_keyboard_events - if True key presses are returned as buttons      
       use_default_focus - if True and no focus set, then automatically set a focus      
       text_justification - Justification to use for Text Elements in this window      
       no_titlebar - Create window without a titlebar      
       grab_anywhere - Grab any location on the window to move the window      
       keep_on_top - if True then window will always stop on top of other windows on the screen.  Great for floating toolbars.     
       resizable - if True - user can manually changge the wize of the window.  Defaults to False
       disable_close - if True user will not be able to close using the X. 
       disable_minimize - if True user will not be able to minimize the window
       right_click_menu - menu definition that will be used on wall elements that support right click. If a  definition is specified on an element then it will be used instead.
      
      
### Window Location      
PySimpleGUI computes the exact center of your window and centers the window on the screen.  If you want to locate your window elsewhere, such as the system default of (0,0), if you have 2 ways of doing this. The first is when the window is created.  Use the `location` parameter to set where the window.  The second way of doing this is to use the `SetOptions` call which will set the default window location for all windows in the future.      

### Window Size

You can get your window's size by access the `Size`property.  The window has to be Read once or Finalized in order for the value to be correct. Note that it's a property, not a call.

`my_windows_size = window.Size`

To finalize your window:

```pytyhon
window = Window('My Title').Layout(layout).Finalize()
```
      

### Element Sizes      
Note several variables that deal with "size".  Element sizes are measured in characters.  A Text Element with a size of 20,1 has a size of 20 characters wide by 1 character tall.      
      
The default Element size for PySimpleGUI is `(45,1)`.      
      
Sizes can be set at the element level, or in this case, the size variables apply to all elements in the window.  Setting `size=(20,1)` in the window creation call will set all elements in the window to that size.      
      
There are a couple of widgets where one of the size values is in pixels rather than characters.  This is true for Progress Meters and Sliders.  The second parameter is the 'height' in pixels.      
      
### No Titlebar      
      
Should you wish to create cool looking windows that are clean with no windows titlebar, use the no_titlebar option when creating the window.      
      
Be sure an provide your user an "exit" button or they will not be able to close the window!  When no titlebar is enabled, there will be no icon on your taskbar for the window.  Without an exit button you will need to kill via taskmanager... not fun.      
      
Windows with no titlebar rely on the grab anywhere option to be enabled or else you will be unable to move the window.      
      
Windows without a titlebar can be used to easily create a floating launcher.      
      
Linux users!  Note that this setting has side effects for some of the other Elements.  Multi-line input doesn't work at all, for example  So, use with caution.      
      
      
![floating launcher](https://user-images.githubusercontent.com/13696193/45258246-71bafb80-b382-11e8-9f5e-79421e6c00bb.jpg)      
      
      
### Grab Anywhere      
      
This is a feature unique to PySimpleGUI.      
      
Note - there is a warning message printed out if the user closes a non-blocking window using a button with grab_anywhere enabled.  There is no harm in these messages, but it may be distressing to the user.    Should you wish to enable for a non-blocking window, simply get grab_anywhere = True when you create the window.      
      
### Always on top      
      
To keep a window on top of all other windows on the screen, set keep_on_top = True when the window is created.  This feature makes for floating toolbars that are very helpful and always visible on your desktop.      
      
### Focus

PySimpleGUI will set a default focus location for you.  This generally means the first input field.  You can set the focus to a particular element.  If you are going to set the focus yourself, then you should turn off the automatic focus by setting `use_default_focus=False` in your Window call.


### Window Methods (things you can do with a Window object)      
      
There are a few methods (functions) that you will see in this document that act on Windows.  The ones you will primarily be calling are:      
      
    window.Layout(layout) - Turns your definition of the Window into Window      
    window.Finalize() - creates the tkinter objects for the Window. Normally you do not call this      
    window.Read() - Read the Windows values and get the button / key that caused the Read to return. Can have an optional timeout      
    window.ReadNonBlocking() - NO LONGER USED!  
    window.Refresh() - Use if updating elements and want to show the updates prior to the nex Read      
    window.Fill(values_dict) - Fill each Element with entry from the dictionary passed in      
    window.SaveToDisk(filename) - Save the Window's values to disk      
    window.LoadFromDisk(filename) - Load the Window's values from disk      
    window.Close() - To close your window, if a button hasn't already closed it    
    window.Disable() - Use to disable the window inputwhen opening another window on top of the primnary  Window      
    window.Enable() - Re-enable a Disabled window      
    window.FindElement(key, silent_on_error=False) - Returns the element that has a matching key value  
    window.Move(x,y) - Moves window to location x,y on screen'
    window.SetAlpha(alpha) - Changes window transparency
    window.BringToFront() - Brings the window to the top of other windows on the screen
    window.Disappear(), Reappear() - Uses alpha channel to make window disappear
    window.Hide(), UnHide() - Hides a window
    window.CurrentLocation() - Returns current window location
    window.Size = w,h - Forces a window to be a particular size. Note this is a property not a method
    window.Size - Tuple (w,h)The size of the current window. Note this is a property
	window.Minimize() - Minimizes window to taskbar        
      
## Window Methods     
    
There are a number of operations you can do on a window after you've created the window.  You call these after creating your Windows object.    
    
#### Layout(rows)    
    
Call to set the window layout.  Must be called prior to Read.  Most likely "chained" in line with the Window creation.    
    
```python    
window = sg.Window('My window title').Layout(layout)    
```    
#### Finalize()    
    
Call to force a window to go through the final stages of initialization.  This will cause the tkinter resources to be allocated so that they can then be modified.    This also causes your window to appear.  If you do not want your window to appear when Finalize is called, then set the Alpha to 0 in your window's creation parameters.

If you want to call an element's Update method or call a Graph element's drawing primitives, you ***must*** either call `Read` or `Finalize` prior to making those calls.

    
#### Read(timeout=None, timeout_key='__TIMEOUT_ _ ')    
    
Read the Window's input values and button clicks in a blocking-fashion    

Returns event, values.  Adding a timeout can be achieved by setting timeout=number of milliseconds before the Read times out after which a "timeout event" is returned.  The value of timeout_key will be returned as the event.   If you do not specify a timeout key, then the value `TIMEOUT_KEY` will be returned.

If you set the timeout = 0, then the Read will immediately return rather than waiting for input or for a timeout. This is the same as the old ReadNonBlocking call.
    
#### ReadNonBlocking()    (NO LONGER USED)
    
While this call will technically still work, it is being removed.  If you want to get the same result, call Read with timeout = 0.
    
Read the Window's input values and button clicks but without blocking.  It will immediately return.    **Consider using Read with non-zero timeout instead!**

Will consume 100% of your CPU if you do not have other blocking calls in your event loop.
    
#### Refresh()    
Cause changes to the window to be displayed on the screen.  Normally not needed unless the changes are immediately required or if it's going to be a while before another call to Read.    

#### SetIcon(icon, pngbase64)
Sets the window's icon that will be shown on the titlebar.    Can either be a filename or a base64 string.

#### Fill(values_dict)    
Populates the windows fields with the values shown in the dictionary.      
    
#### Element(key, silent_on_error=False)         (shorthand version)
#### FindElement(key, silent_on_error=False)    
    
Returns the Element that has a matching key.  If the key is not found, an Error Element is returned so that the program will not crash should the user try to perform an "update".  A Popup message will be shown    
    
#### FindElementWithFocus()    

Returns the Element that currently has the focus.  Returns None if no Elements were found.

#### SaveToDisk(filename)    
    
Saves the window's values to disk    
    
#### LoadFromDisk(filename)    
    
Fills in a window's fields based on previously saved file    
    
#### GetScreenDimensions()    
    
Returns the size (w,h) of the screen in pixels    
    
#### CurrentLocation()
Returns current screen position (x,y) 

#### Move(x, y)
Move window to (x,y) position on the screen

#### Minimize()
Sends the window to the taskbar

#### Close()

Closes a window, blocking or non-blocking

#### CloseNonBlocking()    (NO LONGER USED.. use Close instead)
    
Closes a non-blocking window    
    
#### Disable()    
    
Stops a window from  responding until Enable is called    
    
#### Enable()    
    
Re-enables a previously disabled window    
    
#### Hide()    
    
Completely hides a window, including removing from the taskbar    
    
#### UnHide()    
    
Restores a window hidden using Hide    
    
#### Disappear()    
    
Makes a window disappear while leaving the icon on the taskbar    
    
#### Reappear()    
    
Makes a window reappear that was previously made to disappear using Disappear()    
    
#### SetAlpha(alpha)

Sets the window's transparency.  0 is completely transparent.  1 is fully visible, normal .  Can also use the property Window.AlphaChannel instead of method function call

    
    
      
# Elements      
"Elements" are the building blocks used to create windows.  Some GUI APIs use the term "Widget" to describe these graphic elements.      
      
     Text      
     Single Line Input      
     Buttons including these types:      
         File Browse      
         Folder Browse      
         Calendar picker      
         Date Chooser      
         Read window      
         Close window ("Button" & all shortcut buttons)     
         Realtime      
     Checkboxes      
     Radio Buttons      
     Listbox      
     Slider      
     Multi-line Text Input/Output
     Multi-line Text Output (Qt only)   
     Scroll-able Output  
     Vertical Separator    
     Progress Bar      
     Option Menu      
     Menu
     ButtonMenu      
     Frame      
     Column      
     Graph      
     Image      
     Table      
     Tree    
     Tab, TabGroup    
     StatusBar
     Pane
     Stretch (Qt only)
       

      
## Common Element Parameters      
Some parameters that you  will see on almost all Elements are:      
    
 - key   -  Used with window.FindElement and with return values    
 - tooltip   - Hover your mouse over the elemnt and you'll get a popup with this text    
 - size  - (width, height) - usually measured in characters-wide, rows-high.  Sometimes they mean pixels    
 - font - specifies the font family, size, etc    
 - colors - Color name or #RRGGBB string    
 - pad - Amount of padding to put around element    
 - enable_events - Turns on the element specific events    
      
#### Tooltip    
Tooltips are text boxes that popup next to an element if you hold your mouse over the top of it.  If you want to be extra kind to your window's user, then you can create tooltips for them by setting the parameter `tooltip` to some text string.  You will need to supply your own line breaks / text wrapping.  If you don't want to manually add them, then take a look at the standard library package `textwrap`.      
      
Tooltips are one of those "polish" items that really dress-up a GUI and show's a level of sophistication.  Go ahead, impress people, throw some tooltips into your GUI.      
      
#### Size    
Specifies the amount of room reserved for the Element.  For elements that are character based, such a Text, it is (# characters, # rows).  Sometimes it is a pixel measurement such as the Image element.  And sometimes a mix like on the Slider element (characters long by pixels wide).      
    
#### Colors    
A string representing color.  Anytime colors are involved, you can specify the tkinter color name such as 'lightblue' or an RGB hex value '#RRGGBB'.  For buttons, the color parameter is a tuple (text color, background color)    
    
#### Pad    
The amount of room around the element in pixels. The default value is (5,3) which means leave 5 pixels on each side of the x-axis and 3 pixels on each side of the y-axis.  You can change this on a global basis using a call to SetOptions, or on an element basis.    
    
If you want more pixels on one side than the other, then you can split the number into 2 number.  If you want 200 pixels on the left side, and 3 pixels on the right, the pad would be ((200,3), 3).  In this example, only the x-axis is split.    
    
#### Font    
Specifies the font family, size, and style.  Font families on Windows include:    
* Arial    
* Courier    
* Comic,    
* Fixedsys    
* Times    
* Verdana    
* Helvetica (the default I think)    
    
The fonts will vary from system to system, however, Tk 8.0 automatically maps Courier, Helvetica and Times to their corresponding native family names on all platforms.  Also, font families cannot cause a font specification to fail on Tk 8.0 and greater.  

If you wish to leave the font family set to the default, you can put anything not a font name as the family.  The PySimpleGUI Demo programs and documentation use the family 'Any' to demonstrate this fact..  You could use "default" if that's more clear to you.    
    
There are 2 formats that can be used to specify a font... a string, and a tuple    
Tuple - (family, size, styles)    
String - "Family Size Styles"    
    
To specify an underlined, Helvetica font with a size of 15 the values:    
('Helvetica', 15, 'underline italics')    
'Helvetica 15 underline italics'    
    
#### Key    

If you are going to do anything beyond the basic stuff with your GUI, then you need to understand keys.    
Keys are a way for you to "tag" an Element with a value that will be used to identify that element.  After you put a key in an element's definition, the values returned from Read will use that key to tell you the value.  For example, if you have an input field:    
Input(key='mykey')    
And your read looks like this:    
event, values = Read()    
Then to get the input value from the read it would be:    
values['mykey']    
You also use the same key if you want to call Update on an element.  Please see the section below on Updates to understand that usage.    
    
#### Visible
Beginning in version 3.17 you can create Elements that are initially invisible that you can later make visible.

To create an invisible Element, place the element in the layout like you normally would and add the parameter `visible=False`.  

Later when you want to make that Element visible you simply call the Element's `Update` method and pass in the parameter `visible=True`

This feature works best on Qt, but does work on the tkinter version as well.  The visible parameter can also be used with the Column and Frame "container" Elements.

      
### Output Elements      
Building a window is simply making lists of Elements.  Each list is a row in the overall GUI dialog box.  The definition looks something like this:      
      
    layout = [ [row 1 element, row 1 element],      
               [row 2 element, row 2 element, row 2 element] ]      
The code is a crude representation of the GUI, laid out in text.      
## Shortcut Functions / Multiple Function Names

Many of the main method calls and Element names have shortcuts.  This enables you to code much quicker once you are used to using the SDK.  The Text Element, for example, has 3 different names `Text`, `Txt` or`T`.  InputText can also be written `Input` or `In` .  `FindElement` was recently renamed to `Element` because it's a commonly used function.

      
##  Text Element      
      
    layout = [[sg.Text('This is what a Text Element looks like')]]      
      
 ![simple text](https://user-images.githubusercontent.com/13696193/44959877-e9d97b00-aec3-11e8-9d24-b4405ee4a148.jpg)      
      
      
The most basic element is the Text element.  It simply displays text.  Many of the 'options' that can be set for a Text element are shared by other elements.      
```python
   Text(text,
		size=(None, None), 
		auto_size_text=None,
		click_submits=False, 
        enable_events=False,
        relief=None,
		font=None, 
		text_color=None, 
		background_color=None, 
		justification=None, 
		pad=None, 
		key=None, 
		right_click_menu=None, 
		tooltip=None, 
		visible=True)
```			      
.      
      
    Text - The text that's displayed      
    size - Element's size      
    click_submits - if clicked will cause a read call to return the key value of the button      
    enable_events - same as click_submits
    relief - relief to use around the text      
    auto_size_text - Bool. Change width to match size of text      
    font - Font name and size to use      
    text_color - text color      
    background_color - background color      
    justification - Justification for the text. String - 'left', 'right', 'center'      
    pad - (x,y) amount of padding in pixels to use around element when packing      
    key - used to identify element.  This value will return as button if click_submits True     
    right_click_menu - menu definition to display if right clicked
    tooltip - string representing tooltip      
      
Some commonly used elements have 'shorthand' versions of the functions to make the code more compact.  The functions `T` and `Txt` are the same as calling `Text`.      
      
### Fonts
      
	Already discussed in the common parameters section.  Either string or a tuple.  
      
### Color in PySimpleGUI are in one of two formats - color name or RGB value.    
      
 Individual colors are specified using either the color names as defined in tkinter or an RGB string of this format:      
      
    "#RRGGBB"        or          "darkblue"
      
### `auto_size_text      `
A `True` value for `auto_size_text`, when placed on Text Elements, indicates that the width of the Element should be shrunk do the width of the text.   The default setting is True.      
      
      
### Chortcut functions      
The shorthand functions for `Text` are `Txt` and `T`      
 
### Events `enable_events`

 If you set the parameter `enable_events` or `click_submits` then you will get an event if the user clicks on the Text.  


### Text Methods     
    
#### Update    


If you want to change the text, font, or colors after the element has been created, then use the `Update` method.

```python    
 Update(value = None, background_color=None, text_color=None, font=None, visible=None)    
```    
value - new value to set text element to    
background_color - new background color    
text_color - text color to display    
font - font to use to display 
visible - visibility   
    
    
##  Multiline Text Element      
      
    layout = [[sg.Multiline('This is what a Multi-line Text Element looks like', size=(45,5))]]      
      
![multiline](https://user-images.githubusercontent.com/13696193/44959853-b139a180-aec3-11e8-972f-f52188510c88.jpg)      
      
This Element doubles as both an input and output Element.      
      
```python
Multiline(	default_text='',
			enter_submits=False,
			disabled=False,
			autoscroll=False,
			size=(None, None),
			auto_size_text=None,
			background_color=None,
			text_color=None,
			change_submits=False,
			enable_events=False,
			do_not_clear=False,
			key=None,
			focus=False,
			font=None,
			pad=None,
			tooltip=None
			right_click_menu=None,
			visible=True)
'''
```   
      
    default_text - Text to display in the text box      
    change_submits - Bool. If True, pressing Enter key submits window 
    anable_events - Bool. same as change_submits
    autoscroll - Bool.  Causes "cursor" to always be at the end of the text   
    size - Element's size  
    right_click_menu - menu definition to displat if right clicked    
    auto_size_text - Bool. Change width to match size of text      
      
### Multiline Methods    
```python    
Update(	value=None,
		disabled=None,
		append=False,
		font=None,
		text_color=None,
		background_color=None)

Update(self, value=None, disabled=None, append=False, font=None, text_color=None, background_color=None)value=None, disabled=None, append=False):    
```    
value - string to set the text field to    
disabled - set to True to disable the element    
append - rather than replacing the current text with new text, add the new text onto the end    
    
## Output Element      
Output re-routes `Stdout` to a scrolled text box. 

Whatever you print will show up in this window.  

Note that you will NOT see what you print until you call either window.Read or window.Refresh.  If you want to immediately see what was printed, call window.Refresh() immediately after your print statement.

    layout = [[sg.Output(size=(80,10)]]         
      
![output](https://user-images.githubusercontent.com/13696193/44959863-b72f8280-aec3-11e8-8caa-7bc743149953.jpg)      

```python
Output(	size=(None, None),
		background_color=None,
		text_color=None,
		pad=None,
		font=None,
		tooltip=None,
		right_click_menu=None,
		key=None,
		visible=True)
```

size - Size of Output Element (width, height) in characters
You should be quite familiar with these parameters by now.  If not, read able another element or read about common parameters.

  
      
##  Input Elements      
  These make up the majority of the window definition.  Optional variables at the Element level override the window level values (e.g. `size` is specified in the Element).  All input Elements create an entry in the list of return values.  A Text Input Element creates a string in the list of items returned.      
      
## Text Input Element    Shortcuts (Input, In)  
      
    layout = [[sg.InputText('Default text')]]      
      
![inputtext 2](https://user-images.githubusercontent.com/13696193/44959861-b5fe5580-aec3-11e8-8040-53ec241b5079.jpg)      
      
```python
      def InputText(default_text ='',    
                    size=(None, None),    
                    disabled=False,     
                    auto_size_text=None,    
                    password_char='',      
                    justification=None,    
                    background_color=None,    
                    text_color=None,    
                    font=None,    
                    tooltip=None,    
                    change_submits=False
                    do_not_clear=False,    
                    key=None,    
                    focus=False,  
                    right_click_menu=None,  
                    pad=None,
                    vitible=True):      
```
      
.      
      
     default_text - Text initially shown in the input box      
     size - (width, height) of element in characters      
     auto_size_text- Bool.  True is element should be sized to fit text      
     disabled - Bool If True the input is disabled    
     password_char - Character that will be used to replace each entered character. Setting to a value indicates this field is a password entry field      
     background_color - color to use for the input field background      
     text_color - color to use for the typed text      
     font - font used for the element
     tooltip - what is shown when hovered over element (doesn't appear to work)
     change_submits - if True, will cause a Window.Read to return if a button fills in the value
     do_not_clear - Bool. Normally windows clear when read, turn off clearing with this flag.      
     key = Dictionary key to use for return values      
     focus = Bool. True if this field should capture the focus (moves cursor to this field)      
     pad - amount of room in pixels to leave around the element
      
 There are two methods that can be called:      
      
     Input.Update(new_Value) - sets the input to new_value      
     Input.Get() - returns the current value of the field.      
      
      
Shorthand functions that are equivalent to `InputText` are `Input` and `In`      

#### `do_not_clear` Parameter
      
**Important** - This trips a lot of people up.  If you do not set the `do_not_clear` parameter then the input field will clear when an event takes place.   The behavior is a "forms" style window development.  The assumption is that you want the field to clear.  If you are writing a chat program then you're thankful.  The rest of you, I'm sorry.
    
### TextInput Methods    
```python    
Update(value=None, disabled=None):    
Get()    
```    
Update - Change the Element    
value - new value to display in field    
disabled - if True will disable the element    
    
Get - Returns the current value for the element (you can get also from a call to Read)    
      
      
## Combo Element      
Also known as a drop-down list.  Only required parameter is the list of choices.  The return value is a string matching what's visible on the GUI.      
      
    layout = [[sg.InputCombo(['choice 1', 'choice 2'])]]      
      
![combobox](https://user-images.githubusercontent.com/13696193/44959860-b565bf00-aec3-11e8-82fe-dbe41252458b.jpg)      
      
    InputCombo(values,    ,      
               default_value=None      
               size=(None, None)      
               auto_size_text=None      
               background_color=None      
               text_color=None      
               change_submits=False 
               enable_events=False
               readonly=True     
               disabled=False      
               key=None      
               pad=None      
               tooltip=None   
               visible=True)   
.      
      
     values - Choices to be displayed. List of strings      
     default_value - which value should be initially chosen      
     size - (width, height) of element in characters      
     auto_size_text - Bool. True if size should fit the text length      
     background_color - color to use for the input field background      
     text_color - color to use for the typed text      
     change_submits - Bool. If set causes Read to immediately return if the selected value changes      
     disabled - Bool. If set will disable changes   
     readonly - Bool. If set user cannot change the values to choose from   
     key - Dictionary key to use for return values      
     pad - (x,y) Amount of padding to put around element in pixels      
     tooltip -  Text string. If set, hovering over field will popup the text      
      
Shortcut functions - Combo, DropDown, Drop    
    
### Combo Methods    
```python    
Update(value=None, values=None, set_to_index=None, disabled=None, readonly=None)    
```    
value - change which value is current selected    
values - change list of choices    
set_to_index - change selection to a particular choice    
disable - if True will disable element    
readonly - if True will make element readonly
    
## Listbox Element      
The standard listbox like you'll find in most GUIs.  Note that the return values from this element will be a ***list of results, not a single result***. This is because the user can select more than 1 item from the list (if you set the right mode).      
      
    layout = [[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))]]      
      
![listbox 2](https://user-images.githubusercontent.com/13696193/44959859-b4cd2880-aec3-11e8-881c-1e369d5c6337.jpg)      
      
      
         Listbox(values      
                 default_values=None      
                 select_mode=None      
                 change_submits=False      
                 bind_return_key=False      
                 size=(None, None)      
                 disabled = False,    
                 auto_size_text=None      
                 font=None      
                 background_color=None      
                 text_color=None      
                 key=None      
                 pad=None      
		 		 right_click_menu=None                
                 tooltip=None,
                 visible=True):      
      
.      
      
    values - Choices to be displayed. List of strings      
    select_mode - Defines how to list is to operate.      
         Choices include constants or strings:      
         Constants version:      
       LISTBOX_SELECT_MODE_BROWSE      
       LISTBOX_SELECT_MODE_EXTENDED      
       LISTBOX_SELECT_MODE_MULTIPLE      
       LISTBOX_SELECT_MODE_SINGLE - the default      
       Strings version:      
       'browse'      
       'extended'      
       'multiple'      
       'single'      
    change_submits - if True, the window read will return with a button value of ''      
    bind_return_key - if the focus is on the listbox and the user presses return key, or if the user double clicks an item, then the read will return      
    size - (width, height) of element in characters      
    disapled - Bool. If True element is disabled    
    auto_size_text - Bool. True if size should fit the text length      
    background_color - color to use for the input field background      
    font - font to use for items in list      
    text_color - color to use for the typed text      
    key - Dictionary key to use for return values and to find element      
    pad - amount of padding to use when packing      
    tooltip - tooltip text      
      
The `select_mode` option can be a string or a constant value defined as a variable.  Generally speaking strings are used for these kinds of options.      
      
ListBoxes can cause a window to return from a Read call.  If the flag change_submits is set, then when a user makes a selection, the Read immediately returns.      
Another way ListBoxes can cause Reads to return is if the flag bind_return_key is set.  If True, then if the user presses the return key while an entry is selected, then the Read returns.  Also, if this flag is set, if the user double-clicks an entry it will return from the Read.      
      
### Listbox Methods    
```python    
Update(values=None, disabled=None)    
SetValue(values)    
GetListValues()    
    
```    
Update - Change element    
values - new list of choices    
disabled - if True disables the element    
    
SetValue - Sets selection to one or more values    
    
GetListValues - Return the list of values to choose from    
    
    
## Slider Element      
      
Sliders have a couple of slider-specific settings as well as appearance settings.  Examples include the `orientation` and `range` settings.      
      
    layout = [[sg.Slider(range=(1,500), default_value=222, size=(20,15), orientation='horizontal', font=('Helvetica', 12))]]      
      
![slider](https://user-images.githubusercontent.com/13696193/44959858-b4349200-aec3-11e8-9e25-c0fcf025d19e.jpg)      
      
       Slider(range=(None,None),    
            default_value=None,    
            resolution=None,     
            orientation=None,    
            border_width=None,     
            relief=None,    
            change_submits=False,    
            disabled=False,     
            size=(None, None),    
            font=None,     
            background_color=None,     
            text_color=None,     
            key=None,     
            pad=None,    
            tooltip=None,
            visible=True)    
    
.      
      
      range - (min, max) slider's range      
      default_value - default setting (within range)      
      resolution - how much each 'tick' should represent. Default = 1    
      orientation - 'horizontal' or 'vertical' ('h' or 'v' work)      
      border_width - how deep the widget looks      
      relief - relief style. Values are same as progress meter relief values.  Can be a constant or a string:      
         RELIEF_RAISED= 'raised'      
         RELIEF_SUNKEN= 'sunken'      
         RELIEF_FLAT= 'flat'      
         RELIEF_RIDGE= 'ridge'      
         RELIEF_GROOVE= 'groove'      
         RELIEF_SOLID = 'solid'      
       size - (width, height) of element in characters      
       disabled - Bool If True slider is disabled    
       auto_size_text - Bool. True if size should fit the text      
       background_color - color to use for the input field background      
       text_color - color to use for the typed text      
       change_submits - causes window read to immediately return if the checkbox value changes      
       key- Dictionary key to use for return values      
       tooltip - Tooltip to display when hovered over wlement    
      
### Qt Sliders

There is an important difference between Qt and tkinter sliders.  On Qt, the slider values must be integer, not float.  If you want your slider to go from 0.1 to 1.0, then make your slider go from 1 to 10 and divide by 10.  It's an easy math thing to do and not a big deal.  Just deal with it.... you're writing software after all.  Presumably you know how to do these things.  ;-)


### Slider Methods    
```python    
Update(self, value=None, range=(None, None), disabled=None, visible=None):    
```    
value - set current selection to value    
range - change range of valid values    
disabled - if True disables element    
    
    
## Radio Button Element      
      
Creates one radio button that is assigned to a group of radio buttons.  Only 1 of the buttons in the group can be selected at any one time.      
      
    layout =  [[sg.Radio('My first Radio!', "RADIO1", default=True), sg.Radio('My second radio!', "RADIO1")]]      
      
![radio](https://user-images.githubusercontent.com/13696193/44959857-b4349200-aec3-11e8-8e2d-e6a49ffbd0b6.jpg)      
      
     Radio(text,      
           group_id,      
           default=False,      
           size=(None, None),      
           disabled = False,    
           auto_size_text=None,      
           font=None,      
           background_color = None,      
           text_color = None,      
           key = None,    
           pad = None,    
           tooltip = None,
           visible=True)      
      
.      
      
     text - Text to display next to button      
     group_id - Groups together multiple Radio Buttons. Can be any value      
     default - Bool.  Initial state      
     size - (width, height) size of element in characters      
     auto_size_text - Bool.  True if should size width to fit text      
     font - Font type and size for text display      
     background_color - color to use for the background      
     text_color - color to use for the text      
     key - Dictionary key to use for return values      
     pad - padding around element    
     tooltip - tooltip to show when mouse hovered over element    
      
      
### Radio Button Methods    
```python    
Update(value=None, disabled=None, visible=None)    
```    
value - bool - if True change to selected    
disabled - if True disables the element    
    
    
## Checkbox Element      
Checkbox elements are like Radio Button elements.  They return a bool indicating whether or not they are checked.      
      
    layout =  [[sg.Checkbox('My first Checkbox!', default=True), sg.Checkbox('My second Checkbox!')]]      
      
      
![checkbox](https://user-images.githubusercontent.com/13696193/44959906-6f5d2b00-aec4-11e8-9c8a-962c787f0286.jpg)      
      
      
    Checkbox(text,      
             default=False,      
             size=(None, None),      
             auto_size_text=None,      
             font=None,      
             background_color = None,      
             text_color = None,      
             change_submits = False      
             disabled = False,    
             key = None,    
             pad = None,    
             tooltip = None,
             visible=True):      
.      
      
     text - Text to display next to checkbox      
     default- Bool + None.  Initial state. True = Checked, False = unchecked, None = Not available (grayed out)      
     size - (width, height) size of element in characters      
     auto_size_text- Bool.  True if should size width to fit text      
     disabled - Bool. If True element is disabled    
     font- Font type and size for text display      
     background_color - color to use for the background      
     text_color - color to use for the typed text      
     change_submits - causes window read to immediately return if the checkbox value changes      
     key = Dictionary key to use for return values      
     pad - Padding around element in window    
     tooltip - text to show when mouse is hovered over element    
    
Shortcut functions -   CBox, CB, Check    
    
### Checkbox Methods    
```python    
Update(value=None, disabled=None, visible=None)    
Get()    
```    
Update - changes the element    
value - Bool if True checks the checkbox    
disabled - if True disables the element    
    
Get - returns current state    
    
      
## Spin Element      
      
An up/down spinner control.  The valid values are passed in as a list.      
      
    layout =  [[sg.Spin([i for i in range(1,11)], initial_value=1), sg.Text('Volume level')]]      
      
![spinner](https://user-images.githubusercontent.com/13696193/44959855-b1d23800-aec3-11e8-9f51-afb2109879da.jpg)      
      
    Spin(values,      
         intiial_value=None,     
         disabled = False,     
         size=(None, None),      
         change_submits = False,    
         auto_size_text=None,      
         font=None,      
         background_color = None,      
         text_color = None,      
         key = None.    
         pad = None,    
         tooltip = None,
         visible=True):      
    
    
    
Parameter definitions    
      
     values - List of valid values      
     initial_value - String with initial value      
     size - (width, height) size of element in characters      
     auto_size_text - Bool.  True if should size width to fit text      
     font - Font type and size for text display      
     disabled - Bool. If True element is disabled    
     background_color - color to use for the background      
     text_color - color to use for the typed text      
     change_submits - causes window read to immediately return if the spinner value changes      
     key = Dictionary key to use for return values      
     pad - padding around element in the window    
     tooltip - text to show when mouse hovered over element         


### Qt Differences - `values` is a range!

Note that Qt does not allow arbitrary spinner values.  With PySimpleGUI-tkinter you can have any values in your list.  In Qt they must be integers.  Yea, it kinda sucks.  I'm working on it.

On Qt values is a tuple representing a range.  On plain PySimpleGUI this value is a list of items.  Make sure on the plain version you specify items as a list using [] and not a generator using ().

      
### Spin Methods    
```python    
Update(value=None, values=None, disabled=None, visible=None)    
```    
value - set the current value    
values - set available choices    
disabled - if True disables the element    
    
## Image Element    
    
Images can be placed in your window provide they are in PNG, GIF, PPM/PGM format.  JPGs cannot be shown because tkinter does not naively support JPGs.  You can use the Python Imaging Library (PIL) package  to convert your image to PNG prior to calling PySimpleGUI if your images are in JPG format.    
```python   
  Image(filename=None,
		data=None,
		data_base64=None,
		background_color=None,
		size=(None,None),
		pad=None,
		key=None,
		tooltip=None,
		click_submits=False,
		enable_events=False,
		visible=True,
		right_click_menu=None,		
		size_px=(None,None)  
		visible=True)  
```          
Parameter definitions    
            
    filename - file name if the image is in a file    
    data - if image is in RAM (PIL format?)  
    data_base64 - image in base64 format  
    background_color - Color of background    
    size - Size (Width, Height) of image in pixels    
    pad - Padding around Element in the window    
    key - Key used to find the element    
    tooltip - text to show when mouse if hovered over image    
    click_submits, enable_events - if True returns event when image is clicked
    visible - if False will create image as hidden
    size_px - size of image in pixels
    
### `Update` Method
    
Like other Elements, the Image Element has an `Update` method.  Call Update if you want to change the image.    
    
    def Update(self, filename=None, data=None, visible=None):    
    
    
Choose **either** a filename or in-ram data image to use to replace current image    

### `UpdateAnimation` Method  for Animated GIFs

![loading animation](https://user-images.githubusercontent.com/13696193/51280871-d2041e80-19ae-11e9-8757-802eb95352ed.gif)


Starting in version 3.23 you can specify an animated GIF as an image and can animate the GIF by calling `UpdateAnimation`.  Exciting stuff!

```python
UpdateAnimation(source,
	         	time_between_frames=0)
```
`source` can be a filename ***or*** a base64 bytes variable (unlike other calls that split out the filename parameter and base64 parameter into 2 parameters.

`time_between_frames` is an optional parameter.  It will keep track of the amount of time between frame changes for you to give you a smooth animation.  With this parameter you can call the function as often as you want and it will advance to the next frame only after the correct amount of time has lapsed. 

You can call the method without setting the `time_between_frames` value and it will show a frame and immediately move on to the next frame.  This enables you to do the inter-frame timing.



    
## Button Element      
      
**MAC USERS** - Macs suck when it comes to tkinter and button colors.  It sucks so badly with colors that the `LookAndFeel` call is disabled.  You cannot change button colors for Macs.  You're stuck with the system default color if you are using the tkinter version of PySimpleGUI.  The Qt version does not have this issue.
      
Buttons are the most important element of all!  They cause the majority of the action to happen.  After all, it's a button press that will get you out of a window, whether it be Submit or Cancel, one way or another a button is involved in all windows.  The only exception is to this is when the user closes the window using the "X" in the upper corner which means no button was involved.      
      
The Types of buttons include:      
* Folder Browse      
* File Browse      
* Files Browse      
* File SaveAs      
* File Save      
* Close window  (normal button)      
* Read window      
* Realtime      
* Calendar Chooser      
* Color Chooser      
      
      
Close window - Normal buttons like Submit, Cancel, Yes, No, do NOT close the window... they used to.  Now to close a window you need to use a CloseButton / CButton.
      
Folder Browse - When clicked a folder browse dialog box is opened.  The results of the Folder Browse dialog box are written into one of the input fields of the window.      
      
File Browse - Same as the Folder Browse except rather than choosing a folder, a single file is chosen.      
      
Calendar Chooser - Opens a graphical calendar to select a date.      
      
Color Chooser - Opens a color chooser dialog      
      
Read window - This is a window button that will read a snapshot of all of the input fields, but does not close the window after it's clicked.      
      
Realtime - This is another async window button.  Normal button clicks occur after a button's click is released.  Realtime buttons report a click the entire time the button is held down.      
      
Most programs will use a combination of shortcut button calls (Submit, Cancel, etc), normal Buttons which leave the windows open and CloseButtons that close the window when clicked.
      
Sometimes there are multiple names for the same function.  This is simply to make the job of the programmer quicker and easier.  Or they are old names that are no longer used but kept around so that existing programs don't break.   
      
The 4 primary windows of PySimpleGUI buttons and their names are:      
      
 1. `Button`= `ReadButton` = `RButton` = `ReadFormButton` (old style... use Button instead)      
 2. `CloseButton` = `CButton`
 3. `RealtimeButton`      
 4. `DummyButton`
      
You will find the long-form names in the older programs. ReadButton for example. 

In Oct 2018, the definition of Button changed.  Previously Button would CLOSE the window when clicked.  It has been changed so the Button calls will leave the window open in exactly the same way as a ReadButton.  They are the same calls now.   To enables windows to be closed using buttons, a new button was added... `CloseButton` or `CButton`.
      
The most basic Button element call to use is `Button`      
      
    Button(button_text=''      
           button_type=BUTTON_TYPE_CLOSES_WIN      
           target=(None, None)      
           tooltip=None      
           file_types=(("ALL Files", "*.*"),)      
           initial_folder=None      
           disabled = False    
           image_filename=None      
           image_data=None    
           image_size=(None, None)      
           image_subsample=None      
           border_width=None      
           size=(None, None)      
           auto_size_button=None      
           button_color=None      
           default_value = None      
           font=None      
           bind_return_key=False      
           focus=False      
           pad=None      
           key=None,
           visible=True):      
      
Parameters      
      
    button_text - Text to be displayed on the button      
    button_type - You  should NOT be setting this directly      
    target - key or (row,col) target for the button      
    tooltip - tooltip text for the button      
    file_types - the filetypes that will be used to match files      
    initial_folder - starting path for folders and files      
    disabled = Bool If True button is disabled    
    image_filename - image filename if there is a button image      
    image_data - in-RAM image to be displayed on button    
    image_size - size of button image in pixels      
    image_subsample - amount to reduce the size of the image      
    border_width - width of border around button in pixels      
    size - size in characters      
    auto_size_button - True if button size is determined by button text      
    button_color - (text color, backound color)      
    default_value - initial value for buttons that hold information      
    font - font to use for button text      
    bind_return_key - If True the return key will cause this button to fire      
    focus - if focus should be set to this button      
    pad - (x,y) padding in pixels for packing the button      
    key - key used for finding the element      
      
### Shortcut, Pre-defined Buttons      
These Pre-made buttons are some of the most important elements of all because they are used so much.  They all basically do the same thing, set the button text to match the function name and set the parameters to commonly used values. If you find yourself needing to create a custom button often because it's not on this list, please post a request on GitHub. . They include:      
      
    OK      
    Ok      
    Submit      
    Cancel      
    Yes      
    No      
    Exit      
    Quit      
    Help      
    Save      
    SaveAs      
    FileBrowse      
    FilesBrowse      
    FileSaveAs      
    FolderBrowse      

**IMPORT NOTE ABOUT SHORTCUT BUTTONS**
Prior to release 3.11.0, these buttons closed the window.  Starting with 3.11 they will not close the window.  They act like RButtons (return the button text and do not close the window)

If you are having trouble with these buttons closing your window, please check your installed version of PySimpleGUI by typing `pip list` at a command prompt.  Prior to 3.11 these buttons close your window.  

Using older versions, if you want a Submit() button that does not close the window, then you would instead use RButton('Submit').   Using the new version, if you want a Submit button that closes the window like the sold Submit() call did, you would write that as `CloseButton('Submit')` or `CButton('Submit')`


    layout =  [[sg.OK(), sg.Cancel()]]      
      
![ok cancel 3](https://user-images.githubusercontent.com/13696193/44959927-aa5f5e80-aec4-11e8-86e1-5dc0b3a2b803.jpg)      
      


### Button targets      
      
The `FileBrowse`, `FolderBrowse`, `FileSaveAs` , `FilesSaveAs`, `CalendarButton`, `ColorChooserButton` buttons all fill-in values into another element located on the window.  The target can be a Text Element or an InputText Element.  The location of the element is specified by the `target` variable in the function call.      
      
The Target comes in two forms.      
1. Key      
2. (row, column)      
      
Targets that are specified using a key will find its target element by using the target's key value.  This is the "preferred" method.      
      
If the Target is specified using (row, column) then it utilizes a grid system.  The rows in your GUI are numbered starting with 0. The target can be specified as a hard coded grid item or it can be relative to the button.      
      
The (row, col) targeting can only target elements that are in the same "container".  Containers are the Window, Column and Frame Elements.  A File Browse button located inside of a Column is unable to target elements outside of that Column.      
      
The default value for `target` is `(ThisRow, -1)`.   `ThisRow` is a special value that tells the GUI to use the same row as the button.  The Y-value of -1 means the field one value to the left of the button.  For a File or Folder Browse button, the field that it fills are generally to the left of the button is most cases.    (ThisRow, -1) means the Element to the left of the button, on the same row.      
      
If a value of `(None, None)` is chosen for the target, then the button itself will hold the information.  Later the button can be queried for the  value by using the button's key.      
      
Let's examine this window as an example:      
      
      
![file browse](https://user-images.githubusercontent.com/13696193/44959944-d1b62b80-aec4-11e8-8a68-9d79d37b2c81.jpg)      
      
      
The `InputText` element is located at (1,0)... row 1, column 0.  The `Browse` button is located at position (2,0).  The Target for the button could be any of these values:      
      
    Target = (1,0)      
    Target = (-1,0)      
      
The code for the entire window could be:      
      
    layout = [[sg.T('Source Folder')],      
              [sg.In()],      
              [sg.FolderBrowse(target=(-1, 0)), sg.OK()]]      
      
or if using keys, then the code would be:      
      
    layout = [[sg.T('Source Folder')],      
              [sg.In(key='input')],      
              [sg.FolderBrowse(target='input'), sg.OK()]]      
      
See how much easier the key method is?      
      
**Save & Open Buttons**      
      
There are 4 different types of File/Folder open dialog box available.  If you are looking for a file to open, the `FileBrowse` is what you want. If you want to save a file, `SaveAs` is the button. If you want to get a folder name, then `FolderBrowse` is the button to use. To open several files at once, use the `FilesBrowse` button.  It will create a list of files that are separated by ';'      
      
      
![open](https://user-images.githubusercontent.com/13696193/45243804-2b529780-b2c3-11e8-90dc-6c9061db2a1e.jpg)      
      
      
![folder](https://user-images.githubusercontent.com/13696193/45243805-2b529780-b2c3-11e8-95ee-fec3c0b11319.jpg)      
      
      
![saveas](https://user-images.githubusercontent.com/13696193/45243807-2beb2e00-b2c3-11e8-8549-ba71cdc05951.jpg)      
      
      
      
**Calendar Buttons**      
      
These buttons pop up a calendar chooser window.  The chosen date is returned as a string.      
      
![calendar](https://user-images.githubusercontent.com/13696193/45243374-99965a80-b2c1-11e8-8311-49777835ca40.jpg)      
      
**Color Chooser Buttons**      
      
These buttons pop up a standard color chooser window.  The result is returned as a tuple.  One of the returned values is an RGB hex representation.      
      
![color](https://user-images.githubusercontent.com/13696193/45243375-99965a80-b2c1-11e8-9779-b71bed85fab6.jpg)      
      
      
**Custom Buttons**      
Not all buttons are created equal.  A button that closes a window is different that a button that returns from the window without closing it.  If you want to define your own button, you will generally do this with the Button Element `Button`, which closes the window when clicked.      
      
layout =  [[sg.Button('My Button')]]      
      
![button](https://user-images.githubusercontent.com/13696193/44959862-b696ec00-aec3-11e8-9e88-4b9af0338a03.jpg)      
      
All buttons can have their text changed by changing the `button_text` variable in the button call.  It is this text that is returned when a window is read.  This text will be what tells you which button is called so make it unique.  Most of the convenience buttons (Submit, Cancel, Yes, etc) are all Buttons. Some that are not are `FileBrowse` ,  `FolderBrowse`, `FileSaveAs`.  They clearly do not close the window. Instead they bring up a file or folder browser dialog box.      
      
**Button Images**      
Now this is an exciting feature not found in many simplified packages.... images on buttons!  You can make a pretty spiffy user interface with the help of a few button images.      
      
Your button images need to be in PNG or GIF format.  When you make a button with an image, set the button background to the same color as the background.  There's a button color TRANSPARENT_BUTTON that you can set your button color to in order for it to blend into the background.  Note that this value is currently the same as the color as the default system background on Windows.  If you want to set the button background color to the current system default, use the value COLOR_SYSTEM_DEFAULT as the background color.
      
This example comes from the `Demo Media Player.py` example program.  Because it's a non-blocking button, it's defined as `RButton`.  You also put images on blocking buttons by using `Button`.      
      
      
    sg.RButton('Restart Song', button_color=sg.TRANSPARENT_BUTTON,      
                       image_filename=image_restart, image_size=(50, 50), image_subsample=2, border_width=0)      
      
Three parameters are used for button images.      
      
    image_filename - Filename. Can be a relative path      
    image_size - Size of image file in pixels      
    image_subsample - Amount to divide the size by.  2 means your image will be 1/2 the size.  3 means 1/3      
      
Here's an example window made with button images.      
      
![media file player](https://user-images.githubusercontent.com/13696193/43161977-9ee7cace-8f57-11e8-8ff8-3ea24b69dab9.jpg)      
      
You'll find the source code in the file Demo Media Player.  Here is what the button calls look like to create media player window          
 ```python
    sg.RButton('Pause', button_color=sg.TRANSPARENT_BUTTON,      
                      image_filename=image_pause, 
                      image_size=(50, 50),
                      image_subsample=2, 
                      border_width=0)      
 ```
This is one you'll have to experiment with at this point.  Not up for an exhaustive explanation.      
      
  **Realtime Buttons**      
      
  Normally buttons are considered "clicked" when the mouse button is let UP after a downward click on the button.  What about times when you need to read the raw up/down button values.  A classic example for this is a robotic remote control.  Building a remote control using a GUI is easy enough.  One button for each of the directions is a start.  Perhaps something like this:      
      
![robot remote](https://user-images.githubusercontent.com/13696193/44959958-ff9b7000-aec4-11e8-99ea-7450926409be.jpg)      
      
      
This window has 2 button types.  There's the normal "Read Button" (Quit) and 4 "Realtime Buttons".      
      
Here is the code to make, show and get results from this window:      

```python
import PySimpleGUI as sg  
  
gui_rows = [[sg.Text('Robotics Remote Control')],  
            [sg.T(' '  * 10), sg.RealtimeButton('Forward')],  
            [sg.RealtimeButton('Left'), sg.T(' '  * 15), sg.RealtimeButton('Right')],  
            [sg.T(' '  * 10), sg.RealtimeButton('Reverse')],  
            [sg.T('')],  
            [sg.Quit(button_color=('black', 'orange'))]  
            ]  
  
window = sg.Window('Robotics Remote Control', auto_size_text=True).Layout(gui_rows)  
  
#  
# Some place later in your code...  
# You need to perform a Read or Refresh call on your window every now and then or  
# else it will apprear as if the program has locked up.  
#  
# your program's main loop  
while (True):  
    # This is the code that reads and updates your window  
    event, values = window.Read(timeout=0)  
    if event is not None:  
        print(event)  
    if event == 'Quit'  or values is None:  
        break       
  
window.Close()  # Don't forget to close your window!
```

This loop will read button values and print them.  When one of the Realtime buttons is clicked, the call to `window.Read` will  return a button name matching the name on the button that was depressed or the key if there was a key assigned to the button.  It will continue to return values as long as the button remains depressed.  Once released, the Read will return timeout events until a button is again clicked.      
      
**File Types**      
The `FileBrowse` & `SaveAs` buttons have an additional setting named `file_types`.  This variable is used to filter the files shown in the file dialog box.  The default value for this setting is      
      
    FileTypes=(("ALL Files", "*.*"),)      
      
This code produces a window where the Browse button only shows files of type .TXT      
      
    layout =  [[sg.In() ,sg.FileBrowse(file_types=(("Text Files", "*.txt"),))]]      
      
NOTE - Mac users will not be able to use the file_types parameter.  tkinter has a bug on Macs that will crash the program is a file_type is attempted so that feature had to be removed.  Sorry about that!

  ***The ENTER key***      
       The ENTER key is an important part of data entry for windows.  There's a long  tradition of the enter key being used to quickly submit windows.  PySimpleGUI implements this by tying the ENTER key to the first button that closes or reads a window.      
      
The Enter Key can be "bound" to a particular button so that when the key is pressed, it causes the window to return as if the button was clicked.  This is done using the `bind_return_key` parameter in the button calls.      
If there are more than 1 button on a window, the FIRST button that is of type Close window or Read window is used.  First is determined by scanning the window, top to bottom and left to right.      
      
    
### Button Methods    
```python    
Update(text=None, button_color=(None, None), disabled=None, image_data=None, image_filename=None, visible=None)

GetText()    
```    
Update - Change the button element    

		text - sets button text    
		button color - (text, background)    
		disabled - if True disables the button    
		image_data - sets button image to in-ram image    
		image_filename - sets button image using a file    
    
GetText - Returns the current text shown on a button


## ButtonMenu Element

The ButtonMenu element produces a unique kind of effect.  It's a button, that when clicked, shows you a menu.   It's like clicking one of the top-level menu items on a MenuBar.  As a result, the menu definition take the format of a single  menu entry from  a normal menu definition.  A normal menu definition is  a list of lists.  This definition is one of those lists.

Here is a sample definition:
```python
 ['Menu', ['&Pause Graph', 'Menu item::optional_key']]
```
The very first string normally specifies what is shown on the menu bar.  In this case, the value is **not used**.  You set the text for the button using a different parameter, the `button_text` parm.


```python
ButtonMenu( button_text,
			menu_def, 
			tooltip=None,
			disabled=False, 
			image_filename=None, 
			image_data=None, 
			image_size=(None, None), 
			image_subsample=None,
			border_width=None,
			size=(None, None), 
			auto_size_button=None, 
			button_color=None, 
			font=None, 
			pad=None, 
			key=None, 
			visible=True, 
			size_px=(None,None)):
```

One use of this element is to make a "fake menu bar" that has a colored background.  Normal menu bars cannot have their background color changed.  Not so with ButtonMenus.

This is the effect:

![buttonmenu](https://user-images.githubusercontent.com/13696193/50387000-bc0d8180-06c0-11e9-8d17-3b22ed665e78.gif)

Return values for ButtonMenus are sent via the return values dictionary.  If a selection is made, then an event is generated that will equal the ButtonMenu's key value.  Use that key value to look up the value selected by the user.  This is the same mechanism as the Menu Bar Element, but differs from the pop-up (right click) menu.





## Vertical Separator Element    
This element has limited usefulness and is being included more for completeness than anything else.  It will draw a line between elements.
```python
VerticalSeparator(pad=None)
```
  
![snag-0129](https://user-images.githubusercontent.com/13696193/47376041-a92a0100-d6bf-11e8-8f5b-0c0df56cf0f3.jpg)
      
It works best when placed between columns or elements that span multiple rows.  If on a "normal" row with elements that are only 1 row high, then it will only span that one row.




## ProgressBar  Element    
The `ProgressBar` element is used to build custom Progress Bar windows.  It is HIGHLY recommended that you use OneLineProgressMeter that provides a complete progress meter solution for you.  Progress Meters are not easy to work with because the windows have to be non-blocking and they are tricky to debug.      
      
The **easiest** way to get progress meters into your code is to use the `OneLineProgressMeter` API.  This consists of a pair of functions, `OneLineProgressMeter` and `OneLineProgressMeterCancel`.  You can easily cancel any progress meter by calling it with the current value = max value.  This will mark the meter as expired and close the window.      
You've already seen OneLineProgressMeter calls presented earlier in this readme.      
      
    sg.OneLineProgressMeter('My Meter', i+1, 1000,  'key', 'Optional message')      
      
The return value for `OneLineProgressMeter` is:      
`True` if meter updated correctly      
`False` if user clicked the Cancel button, closed the window, or vale reached the max value.      
      
#### Progress Mater in Your window      
Another way of using a Progress Meter with PySimpleGUI is to build a custom window with a `ProgressBar` Element in the window.  You will need to run your window as a non-blocking window.  When you are ready to update your progress bar, you call the `UpdateBar` method for the `ProgressBar` element itself.      
      
![progress custom](https://user-images.githubusercontent.com/13696193/45243969-c3508100-b2c3-11e8-82bc-927d0307e093.jpg)      
      
    import PySimpleGUI as sg      
      
    # layout the window      
    layout = [[sg.Text('A custom progress meter')],      
              [sg.ProgressBar(10000, orientation='h', size=(20, 20), key='progressbar')],      
              [sg.Cancel()]]      
      
    # create the window`      
    window = sg.Window('Custom Progress Meter').Layout(layout)      
    progress_bar = window.FindElement('progressbar')      
    # loop that would normally do something useful      
    for i in range(10000):      
        # check to see if the cancel button was clicked and exit loop if clicked      
      event, values = window.Read(timeout=0)      
        if event == 'Cancel'  or event is None:      
            break      
      # update bar with loop value +1 so that bar eventually reaches the maximum      
      progress_bar.UpdateBar(i + 1)      
    # done with loop... need to destroy the window as it's still open      
    window.Close())      
      
      
#### Output      
The Output Element is a re-direction of Stdout.  Anything "printed" will be displayed in this element.      
      
    Output(size=(None, None))      
      
Here's a complete solution for a chat-window using an Async window with an Output Element      
      
    import PySimpleGUI as sg      
      
    # Blocking window that doesn't close      
    def ChatBot():      
        layout = [[(sg.Text('This is where standard out is being routed', size=[40, 1]))],      
                  [sg.Output(size=(80, 20))],      
                  [sg.Multiline(size=(70, 5), enter_submits=True),      
                   sg.RButton('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0])),      
                   sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]      
      
      window = sg.Window('Chat Window', default_element_size=(30, 2)).Layout(layout)      
      
        # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #      
      while True:      
            event, value = window.Read()      
            if event == 'SEND':      
                print(value)      
            else:      
                break      
      
    ChatBot()      
      
### ProgressBar Methods    
```python    
UpdateBar(current_count, max=None)    
```    
current_count - sets the current value    
max - changes the max value    
    
    
## Column Element    
Starting in version 2.9 you'll be able to do more complex layouts by using the Column Element.  Think of a Column as a window within a window.  And, yes, you can have a Column within a Column if you want.      
      
Columns are specified in exactly the same way as a window is, as a list of lists.      
   
```python
Column(  layout, 
		 background_color=None,
		 size=(None, None), 
		 pad=None, 
		 scrollable=False, 
		 vertical_scroll_only=False,
		 right_click_menu=None, 
		 key=None,
		 visible=True)
```      
   
      
      
Columns are needed when you have an element that has a height > 1 line on the left, with single-line elements on the right.  Here's an example of this kind of layout:      
      
      
![column](https://user-images.githubusercontent.com/13696193/44959988-66b92480-aec5-11e8-9c26-316ed24a68c0.jpg)      
      
      
This code produced the above window.      
      
      
    import PySimpleGUI as sg      
      
    # Demo of how columns work      
    # window has on row 1 a vertical slider followed by a COLUMN with 7 rows      
    # Prior to the Column element, this layout was not possible      
    # Columns layouts look identical to window layouts, they are a list of lists of elements.      
      
    window = sg.Window('Columns')                                   # blank window      
      
    # Column layout      
    col = [[sg.Text('col Row 1')],      
           [sg.Text('col Row 2'), sg.Input('col input 1')],      
           [sg.Text('col Row 3'), sg.Input('col input 2')],      
           [sg.Text('col Row 4'), sg.Input('col input 3')],      
           [sg.Text('col Row 5'), sg.Input('col input 4')],      
           [sg.Text('col Row 6'), sg.Input('col input 5')],      
           [sg.Text('col Row 7'), sg.Input('col input 6')]]      
      
    layout = [[sg.Slider(range=(1,100), default_value=10, orientation='v', size=(8,20)), sg.Column(col)],      
              [sg.In('Last input')],      
              [sg.OK()]]      
      
    # Display the window and get values      
    # If you're willing to not use the "context manager" design pattern, then it's possible      
    # to collapse the window display and read down to a single line of code.      
    event, values = sg.Window('Compact 1-line window with column').Layout(layout).Read()      
      
    sg.Popup(event, values, line_width=200)      
      
The Column Element has 1 required parameter and 1 optional (the layout and the background color).  Setting the background color has the same effect as setting the window's background color, except it only affects the column rectangle.      
      
    Column(layout, background_color=None)      
      
The default background color for Columns is the same as the default window background color.  If you change the look and feel of the window, the column background will match the window background automatically.      
      
      
      
----      
## Frame Element (Labelled Frames, Frames with a title)      
      
Frames work exactly the same way as Columns.  You create layout that is then used to initialize the Frame.      

```python
Frame(  title, 
		layout, 
		title_color=None, 
		background_color=None, 
		title_location=None,
		relief=DEFAULT_FRAME_RELIEF, 
		size=(None, None), 
		font=None,
		pad=None, 
		border_width=None,
		key=None, 
		tooltip=None, 
		right_click_menu=None, 
		visible=True)
```      
    def Frame(title - the label / title to put on frame      
                  layout - list of rows of elements the frame contains      
                  title_color - color of the title text      
                  background_color - color of background      
                  title_location - locations to put the title      
                  relief - type of relief to use      
                  size - size of Frame in characters. Do not use if you want frame to autosize      
                  font - font to use for title      
                  pad - element padding  to use when packing      
                  border_width - how thick the line going around frame should be      
                  key - key used to location the element      
                  tooltip - tooltip text      
      
      
      
This code creates a window with a Frame and 2 buttons.      
      
    frame_layout = [      
                      [sg.T('Text inside of a frame')],      
                      [sg.CB('Check 1'), sg.CB('Check 2')],      
                   ]      
    layout = [      
              [sg.Frame('My Frame Title', frame_layout, font='Any 12', title_color='blue')],      
              [sg.Submit(), sg.Cancel()]      
             ]      
      
    window = sg.Window('Frame with buttons', font=("Helvetica", 12)).Layout(layout)      
      
      
![frame element](https://user-images.githubusercontent.com/13696193/45889173-c2245700-bd8d-11e8-8f73-1e5f1be3ddb1.jpg)      
      
      
      
Notice how the Frame layout looks identical to a window layout.  A window works exactly the same way as a Column and a Frame.  They all are "container elements".  Elements that contain other elements.      
      
*These container Elements can be nested as deep as you want.* That's a pretty spiffy feature, right?  Took a lot of work so be appreciative.  Recursive code isn't trivial.      
      
## Canvas Element      
      
```python
Canvas(canvas=None,
	   background_color=None, 
	   size=(None, None),
	   pad=None, 
	   key=None, 
	   tooltip=None, 
	   right_click_menu=None, 
	   visible=True)
```

In my opinion, the tkinter Canvas Widget is the most powerful of the tkinter widget.  While I try my best to completely isolate the user from anything that is tkinter related, the Canvas Element is the one exception.  It enables integration with a number of other packages, often with spectacular results.      
      
### Matplotlib, Pyplot Integration      
      
One such integration is with Matploplib and Pyplot.  There is a Demo program written that you can use as a design pattern to get an understanding of how to use the Canvas Widget once you get it.      
      
    def Canvas(canvas - a tkinter canvasf if you created one. Normally not set      
             background_color - canvas color      
             size - size in pixels      
             pad - element padding for packing      
             key - key used to lookup element      
             tooltip - tooltip text      
      
The order of operations to obtain a tkinter Canvas Widget is:      
      
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds      
    # define the window layout      
    layout = [[sg.Text('Plot test')],      
              [sg.Canvas(size=(figure_w, figure_h), key='canvas')],      
              [sg.OK(pad=((figure_w / 2, 0), 3), size=(4, 2))]]      
      
    # create the window and show it without the plot      
    window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI').Layout(layout).Finalize()      
      
      
    # add the plot to the window      
    fig_photo = draw_figure(window.FindElement('canvas').TKCanvas, fig)      
      
    # show it all again and get buttons      
    event, values = window.Read()      
      
To get a tkinter Canvas Widget from PySimpleGUI, follow these steps:      
* Add Canvas Element to your window      
* Layout your window      
* Call `window.Finalize()` - this is a critical step you must not forget      
* Find the Canvas Element by looking up using key      
* Your Canvas Widget Object will be the found_element.TKCanvas      
* Draw on your canvas to your heart's content      
* Call `window.Read()` - Nothing will appear on your canvas until you call Read      
      
See `Demo_Matplotlib.py` for a Recipe you can copy.      
      
      
### Canvas Methods    
    
TKCanvas - not a method but a property. Returns the tkinter Canvas Widget    
    
    
    
## Graph Element      
      
All you math fans will enjoy this Element... and all you non-math fans will enjoy it too.      
      
I've found nothing to be less fun than dealing with a graphic's coordinate system from a GUI Framework.  It's always upside down from what I want.  (0,0) is in the upper left hand corner.  In short, it's a **pain in the ass**.      
      
Graph Element to the rescue.  A Graph Element creates a pixel addressable canvas using YOUR coordinate system.  *You* get to define the units on the X and Y axis.      
      
There are 3 values you'll need to supply the Graph Element.  They are:      
* Size of the canvas in pixels      
* The lower left (x,y) coordinate of your coordinate system      
* The upper right (x,y) coordinate of your coordinate system      
      
After you supply those values you can scribble all of over your graph by creating Graph Figures.  Graph Figures are created, and a Figure ID is obtained by calling:      
* DrawCircle      
* DrawLine      
* DrawPoint      
* DrawRectangle      
* DrawOval      
* DrawImage
      
You can move your figures around on the canvas by supplying the Figure ID the x,y amount to move.      
      
    graph.MoveFigure(my_circle, 10, 10)      
      
This Element is relatively new and may have some parameter additions or deletions.  It shouldn't break your code however.      
      
```python
  Graph(canvas_size, 
		graph_bottom_left, 
		graph_top_right, 
		background_color=None, 
		pad=None,
		change_submits=False,
		drag_submits=False
		enable_events=False,
		key=None,
		tooltip=None,
		right_click_menu=None, 
		visible=True)
```    
      
### Graph Methods    
```python    
DrawLine(self, point_from, point_to, color='black', width=1)    
DrawPoint(self, point, size=2, color='black')    
DrawCircle(self, center_location, radius, fill_color=None, line_color='black')    
DrawOval(self, top_left, bottom_right, fill_color=None, line_color=None)    
DrawArc(self, top_left, bottom_right, extent, start_angle, style=None, arc_color='black')    
DrawRectangle(self, top_left, bottom_right, fill_color=None, line_color=None)    
DrawText(self, text, location, color='black', font=None, angle=0)    
Erase(background_color)    
DeleteFigure(figure_id)
Update()    
Move(self, x_direction, y_direction)    
MoveFigure(self, figure, x_direction, y_direction)  
RelocateFigure(self, figure, x, y)  
TKCanvas    
```    
All of the Drawing methods return a "***figure***" that can be used move and delete the figure    
    
DrawLine - draws a line    
DrawPoint - draws a single point    
DrawCircle - draws a circle    
DrawOval - draws an oval    
DrawArc - draws an arc    
DrawRectangle - draws a rectangle    
DrawText - draws text    
DrawImage - places an image onto the graph
Erase - erases entire graph    
Update - changes background color    
Move - moves everything an x,y direction    
MoveFigure - moves an individual figure by some delta
RelocateFigure - moves figure to an absolute location    
DeleteFigure - delete an individual figure
    
      
## Table Element      
      
Out of all of the Elements, it's the Table and the Tree that are the most "problematic" in the tkinter inter and Qt implementations.  They're hard is my only defense.

### Known visualization problem....

If you click on the header, it can go into spasms for some tables. I don't understand what's causing it and it's been there evidently since the first release of Tables.
   
```python
Table(  values,
		headings=None,
		visible_column_map=None,
		col_widths=None,
		def_col_width=10,
		auto_size_columns=True,
		max_col_width=20,
		select_mode=None,
		display_row_numbers=False,
		num_rows=None,
		row_height=None,
		font=None,
		justification='right',
		text_color=None,
		background_color=None,
		alternating_row_color=None,
		row_colors=None,
		vertical_scroll_only=True,
		size=(None,None),
		change_submits=False,
		enable_events=False,
		bind_return_key=False,
		pad=None,
		key=None,
		tooltip=None,
		right_click_menu=None,
		visible=True):

```

values - Your table's array      
headings - list of strings representing your headings, if you have any      
visible_column_map - list of bools. If True, column in that position is shown.  Defaults to all columns      
col_widths - list of column widths      
def_col_width - default column width. defaults to 10      
auto_size_columns - bool. If True column widths are determined by table contents      
max_col_width - maximum width of a column. defaults to 25      
select_mode - table rows can be selected, but doesn't currently do anything      
display_row_numbers - bool. If True shows numbers next to rows
num_rows = the number of rows to display at a time (same as size[0])      
row_height = number of pixels high a row should be. Normally left as default value  
font - font for table entries      
justification - left, right, center      
text_color - color of text      
alternating row color - if set will change background color for alternating rows
row_colors - list of tuples representing (row_number, color) e.g. row_colors = ((5, 'white', 'blue'), (0,'red'), (15,'yellow'))
vertical_scroll_only - if True will not show a horizontal scrollbar.   NOTE - will have to disable to get horizontal scrollbars
background_color - cell background color      
size - (None, number of rows) - don't use, use num_rows instead
enable_events - will return a 'row selected' event when row is selected
change_submits - the old way of indicating enable_events
bind_return_key - returns event if a double click or a return key is pressed while row is highlighted
pad - element padding for packing      
key - key used to lookup element      
tooltip - tooltip text      
      
### Read return values from Table Element

The values returned from a `Window.Read` call for the Tree Element are a list of row numbers that are currently highlighted.

### Update Call

The Update method can be used to make changes to a table that's already been displayed.  The call takes a single parameter, values, which is the new table to display.  The entire table is replaced.

```python
def Update(self, values=None):
```
`values` is a table containing your rows just like you passed in when creating the Table Element.

## Tree Element    
    
The Tree Element and Table Element are close cousins.   Many of the parameters found in the Table Element apply to Tree Elements.  In particular the heading information, column widths, etc.    
    
```python
Tree(   data=None,
		headings=None, 
		visible_column_map=None, 
		col_widths=None, 
		col0_width=10,
		def_col_width=10,
		auto_size_columns=True, 
		max_col_width=20, 
		select_mode=None, 
		show_expanded=False, 
		change_submits=False, 
		enable_events=False, 
		font=None,
		justification='right', 
		text_color=None, 
		background_color=None,
		num_rows=None,
		row_height=None,
		pad=None, 
		key=None, 
		tooltip=None,
		right_click_menu=None, 
		visible=True)
```
```    
class Tree(data=None - data in TreeData format    
         headings=None - list of strings representing your headings    
         visible_column_map=None - list of bools indicating which columns to display    
         col_widths=None - list of column widths    
         col0_width=10 - width of the first column which has the text data    
         def_col_width=10 - default column width    
         auto_size_columns=True - if true will autosize columns (currenly only sizes to col heading width)    
         max_col_width=20 - max width for columns in characters    
         select_mode=None - not yet used    
         show_expanded - Bool - if True the tree will be fully expanded when shown
         font=None - the display font    
         justification='right' - justification for data display    
         text_color=None- color of text to display    
         background_color=None - background color    
         num_rows=None - number of rows to display   
         row_height=None - height of rows in pixels 
         pad=None - element padding    
         key=None - key for element    
         tooltip=None - tooltip    
```           
    
Unlike Tables there is no standard format for trees.  Thus the data structure passed to the Tree Element must be constructed.  This is done using the TreeData class.  The process is as follows:    
* Get a TreeData Object    
* "Insert" data into the tree    
* Pass the filled in TreeData object to Tree Element    

#### TreeData format
```python
def TreeData()
def Insert(self, parent, key, text, values, icon=None)
```

To "insert" data into the tree the TreeData method Insert is called.    
    
`Insert(parent_key, key, display_text, values)`    
    
To indicate insertion at the head of the tree, use a parent key of "".  So, every top-level node in the tree will have a parent node = ""    
    
This code creates a TreeData object and populates with 3 values    
```python    
treedata = sg.TreeData()    
    
treedata.Insert("", '_A_', 'A', [1,2,3])      
treedata.Insert("", '_B_', 'B', [4,5,6])      
treedata.Insert("_A_", '_A1_', 'A1', ['can','be','anything'])    
```    
    
Note that you ***can*** use the same values for display_text and keys.  The only thing you have to watch for is that you cannot repeat keys.    
    
When Reading a window the Table Element will return a list of rows that are selected by the user.  The list will be empty is no rows are selected.    
    
#### Icons on Tree Entries

If you wish to show an icon next to a tree item, then you specify the icon in the call to `Insert`.  You pass in a filename or a Base64 bytes string using the optional `icon` parameter.

Here is the result of showing an icon with a tree entry.

![image](https://user-images.githubusercontent.com/13696193/51087270-2b561e80-171f-11e9-8260-6142ea9b1137.png)

      
## Tab and Tab Group Elements      
      
Tabs have been a part of PySimpleGUI since the initial release.  However, the initial implementation applied tabs at the top level only. The entire window had to be tabbed.  There with other limitations that came along with that implementation.  That all changed in version 3.8.0 with the new elements - Tab and TabGroup.  The old implementation of Tabs was removed in version 3.8.0 as well.      
      
Tabs are another "Container Element".  The other Container Elements include:      
* Frame      
* Column      
      
You layout a Frame in exactly the same way as a Frame or Column elements, by passing in a list of elements.      
      
How you place a Tab into a Window is different than Graph or Frame elements.  You cannot place a tab directly into a Window's layout.  It much first be placed into a TabGroup.  The  TabGroup can then be placed into the Window.      
      
Let's look at this Window as an example:      
      
![tabbed 1](https://user-images.githubusercontent.com/13696193/45992808-b10f6a80-c059-11e8-9746-ac71afd4d3d6.jpg)      
      
View of second tab:      
      
![tabbed 2](https://user-images.githubusercontent.com/13696193/45992809-b10f6a80-c059-11e8-94e6-3bf543c9b0bd.jpg)      
      
      
First we have the Tab layout definitions. They mirror what you see in the screen shots.  Tab 1 has 1 Text Element in it.  Tab 2 has a Text and an Input Element.      
      
      
    tab1_layout =  [[sg.T('This is inside tab 1')]]      
      
    tab2_layout = [[sg.T('This is inside tab 2')],      
                   [sg.In(key='in')]]      
      
The layout for the entire window looks like this:      
      
    layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],      
              [sg.RButton('Read')]]      
      
The Window layout has the TabGroup and within the tab Group are the two Tab elements.      
      
One important thing to notice about all of these container Elements... they all take a "list of lists" at the layout.  They all have a layout that starts with `[[`      
      
You will want to keep this `[[ ]]` construct in your head a you're debugging your tabbed windows.  It's easy to overlook one or two necessary ['s      
      
As mentioned earlier, the old-style Tabs were limited to being at the Window-level only.  In other words, the tabs were equal in size to the entire window.  This is not the case with the "new-style" tabs.  This is why you're not going to be upset when you discover your old code no longer works with the new PySimpleGUI release.  It'll be worth the few moments it'll take to convert your code.      
      
Check out what's possible with the NEW Tabs!      
      
![tabs tabs tabs](https://user-images.githubusercontent.com/13696193/45993438-fd0fde80-c05c-11e8-9ed0-742f14d3070f.jpg)      
      
      
Check out Tabs 7 and 8.  We've got a Window with a Column containing Tabs 5 and 6.  On Tab 6 are... Tabs 7 and 8.      
      
As of Release 3.8.0, not all of *options* shown in the API definitions of the Tab and TabGroup Elements are working. They are there as placeholders.      
      
The definition of a TabGroup is      
      
     TabGroup(layout,      
               title_color=None      
               background_color=None      
               font=None      
               pad=None      
               border_width=None      
               change_submits = False      
               key=None      
               tooltip=None)      
      
The definition of a Tab Element is      
      
    Tab(title,      
        layout,      
        title_color=None,      
        background_color=None,      
        font=None,      
        pad=None      
        disabled=False    
        border_width=None      
        key=None      
        tooltip=None)      
      
      
### Reading Tab Groups      
      
Tab Groups now return a value when a Read returns.  They return which tab is currently selected.  There is also a change_submits parameter that can be set that causes a Read to return if a Tab in that group is selected / changed.  The key or title belonging to the Tab that was switched to will be returned as the value      
      
      
### Tab Element Methods    
```python    
Update(disabled = None, visible=None)    
```    
WARNING - This Update method may not be working correctly
    
## Pane Element

New in version 3.20 is the Pane Element, a super-cool tkinter feature.  You won't find this one in PySimpleGUIQt, only PySimpleGUI.   It's difficult to describe one of these things.  Think of them as "Tabs without labels" that you can slide.

![pane3](https://user-images.githubusercontent.com/13696193/50035040-fcd50e80-ffcd-11e8-939c-df8ab8d64712.gif)

```python
  
Pane(pane_list, background_color=None, size=(None, None), pad=None, orientation='vertical', show_handle=True, relief=RELIEF_RAISED, handle_size=None, border_width=None, key=None, visible=True):
```    

***Each "Pane" of a Pane Element must be a Column Element***.  The parameter `pane_list` is a list of Column Elements.

Calls can get a little hairy looking if you try to declare everything in-line as you can see in this example.

```python
sg.Pane([col5, sg.Column([[sg.Pane([col1, col2, col4], handle_size=15, orientation='v',  background_color=None, show_handle=True, visible=True, key='_PANE_', border_width=0,  relief=sg.RELIEF_GROOVE),]]),col3 ], orientation='h', background_color=None, size=(160,160), relief=sg.RELIEF_RAISED, border_width=0)
```

Combing these with *visibility* make for an interesting interface with entire panes being hidden from view until neded by the user.  It's one way of producing "dynamic" windows.


## Colors    
Starting in version 2.5 you can change the background colors for the window and the Elements.      
      
Your windows can go from this:      
      
![snap0155](https://user-images.githubusercontent.com/13696193/43273879-a9fdc10a-90cb-11e8-8c20-4f6a244ebe2f.jpg)      
      
      
to this... with one function call...      
      
      
![snap0156](https://user-images.githubusercontent.com/13696193/43273880-aa1955e6-90cb-11e8-94b6-673ecdb2698c.jpg)      
      
      
      
While you can do it on an element by element or window level basis, the easiest way, by far, is a call to `SetOptions`.      
      
Be aware that once you change these options they are changed for the rest of your program's execution.  All of your windows will have that look and feel, until you change it to something else (which could be the system default colors.      
      
This call sets all of the different color options.      
      
    SetOptions(background_color='#9FB8AD',      
               text_element_background_color='#9FB8AD',      
               element_background_color='#9FB8AD',      
               scrollbar_color=None,      
               input_elements_background_color='#F7F3EC',      
               progress_meter_color = ('green', 'blue')      
               button_color=('white','#475841'))      
      
# SystemTray

This is a PySimpleGUIQt and PySimpleGUIWx only feature.  Don't know of a way to do it using tkinter.  Your source code for SystemTray is identical for the Qt and Wx implementations.  You can switch frameworks by simply changing your import statement.

In addition to running normal windows, it's now also possible to have an icon down in the system tray that you can read to get menu events.  There is a new SystemTray object that is used much like a Window object.  You first get one, then  you perform Reads in order to get events.

Here is the definition of the SystemTray object.

```python
SystemTray(menu=None, filename=None, data=None, data_base64=None, tooltip=None):  
        '''  
 SystemTray - create an icon in the system tray  
 :param menu: Menu definition 
 :param filename: filename for icon  
 :param data: in-ram image for icon  
 :param data_base64: basee-64 data for icon  
 :param tooltip: tooltip string '''
```

You'll notice that there are 3 different ways to specify the icon image.  The base-64 parameter allows you to define a variable in your .py code that is the encoded image so that you do not need any additional files.  Very handy feature.

## System Tray Design Pattern

Here is a design pattern you can use to get a jump-start.

This program will create a system tray icon and perform a blocking Read.  If the item "Open" is chosen from the system tray, then a popup is shown.

```python
import PySimpleGUIQt as sg  
  
menu_def = ['BLANK', ['&Open', '---', '&Save', ['1', '2', ['a', 'b']], '&Properties', 'E&xit']]  
  
tray = sg.SystemTray(menu=menu_def, filename=r'default_icon.ico')  
  
while True:  # The event loop  
  menu_item = tray.Read()  
    print(menu_item)  
    if menu_item == 'Exit':  
        break  
    elif menu_item == 'Open':  
        sg.Popup('Menu item chosen', menu_item)
        
```
The design pattern creates an icon that will display this menu:
![snag-0293](https://user-images.githubusercontent.com/13696193/49057441-8bbfe980-f1cd-11e8-93e7-1aeda9ccd173.jpg)

### Icons

When specifying "icons", you can use 3 different formats.  
* `filename`- filename
* `data_base64` - base64 byte string
* '`data` - in-ram bitmap or other "raw" image

You will find 3 parameters used to specify these 3 options on both the initialize statement and on the Update method.

## Menu Definition
```python
menu_def = ['BLANK', ['&Open', '&Save', ['1', '2', ['a', 'b']], '!&Properties', 'E&xit']]  
```

A menu is defined using a list.  A "Menu entry" is a string that specifies:
* text shown
* keyboard shortcut
* key

See section on Menu Keys for more information on using keys with menus.

An entry without a key and keyboard shortcut is a simple string
`'Menu Item'`

If you want to make the "M" be a keyboard shortcut, place an `&` in front of the letter that is the shortcut.
`'&Menu Item'`

You can add "keys" to make menu items unique or as another way of identifying a menu item than the text shown.  The key is added to the text portion by placing `::` after the text.

`'Menu Item::key'`

The first entry can be ignored.`'BLANK`' was chosen for this example. It's this way because normally you would specify these menus under some heading on a menu-bar.  But here there is no heading so it's filled in with any value you want.

**Separators**
If you want a separator between 2 items, add the entry `'---'` and it will add a separator item at that place in your menu.

**Disabled menu entries**

If you want to disable a menu entry, place a `!` before the menu entry


## SystemTray Methods

### Read - Read the context menu or check for events

```python
def Read(timeout=None)
    '''  
 Reads the context menu  
 :param timeout: Optional.  Any value other than None indicates a non-blocking read
 :return:   String representing meny item chosen. None if nothing read.  
    '''
```
The `timeout` parameter specifies how long to wait for an event to take place.  If nothing happens within the timeout period, then a "timeout event" is returned.  These types of reads make it possible to run asynchronously.  To run non-blocked, specify `timeout=0`on the Read call.

Read returns the menu text, complete with key, for the menu item chosen.  If you specified `Open::key` as the menu entry, and the user clicked on `Open`, then you will receive the string `Open::key` upon completion of the Read.

#### Read special return values

In addition to Menu Items, the Read call can return several special values.    They include:

EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED - Tray icon was double clicked
EVENT_SYSTEM_TRAY_ICON_ACTIVATED - Tray icon was single clicked
EVENT_SYSTEM_TRAY_MESSAGE_CLICKED - a message balloon was clicked
TIMEOUT_KEY is returned if no events are available if the timeout value is set in the Read call


### Hide

Hides the icon.  Note that no message balloons are shown while an icon is hidden.

```python
def Hide() 
```

### Close

Does the same thing as hide
```python
def Close()
```


### UnHide

Shows a previously hidden icon

```python
def UnHide()
```

### ShowMessage

Shows a balloon above the icon in the system tray area.  You can specify your own icon to be shown in the balloon, or you can set `messageicon` to one of the preset values.  

This message has a custom icon.

![snag-0286](https://user-images.githubusercontent.com/13696193/49057459-a85c2180-f1cd-11e8-9a66-aa331d7e034c.jpg)

The preset `messageicon` values are:

    SYSTEM_TRAY_MESSAGE_ICON_INFORMATION 
    SYSTEM_TRAY_MESSAGE_ICON_WARNING
    SYSTEM_TRAY_MESSAGE_ICON_CRITICAL 
    SYSTEM_TRAY_MESSAGE_ICON_NOICON

```python
ShowMessage(title, message, filename=None, data=None, data_base64=None, messageicon=None, time=10000):  
    '''  
 Shows a balloon above icon in system tray  
 :param title:  Title shown in balloon  
 :param message: Message to be displayed  
 :param filename: Optional icon filename  
 :param data: Optional in-ram icon  
 :param data_base64: Optional base64 icon  
 :param time: How long to display message in milliseconds  :return:  
 '''
```
Note, on windows it may be necessary to make a registry change to enable message balloons to be seen.  To fix this, you must create the DWORD you see in this screenshot.

![snag-0285](https://user-images.githubusercontent.com/13696193/49056144-6381bc00-f1c8-11e8-9f44-199394823369.jpg)


### Update

You can update any of these items within a SystemTray object
* Menu definition
* Icon
* Tooltip

 Change them all or just 1.

```python
Update(menu=None, tooltip=None,filename=None, data=None, data_base64=None,)
    '''  
 Updates the menu, tooltip or icon  
 :param menu: menu defintion  
 :param tooltip: string representing tooltip  
 :param filename:  icon filename  
 :param data:  icon raw image  
 :param data_base64: icon base 64 image  
 :return:  
 '''
```
      
      
# Global Settings      
**Global Settings**      
Let's have some fun customizing!  Make PySimpleGUI look the way you want it to look. You can set the global settings using the function `PySimpleGUI.SetOptions`.  Each option has an optional parameter that's used to set it.      
      
    SetOptions(icon=None      
            button_color=(None,None)      
            element_size=(None,None),      
            margins=(None,None),      
            element_padding=(None,None)      
            auto_size_text=None      
            auto_size_buttons=None      
            font=None      
            border_width=None      
            slider_border_width=None      
            slider_relief=None      
            slider_orientation=None      
            autoclose_time=None      
            message_box_line_width=None      
            progress_meter_border_depth=None      
            progress_meter_style=None      
            progress_meter_relief=None      
            progress_meter_color=None      
            progress_meter_size=None      
            text_justification=None      
            text_color=None      
            background_color=None      
            element_background_color=None      
            text_element_background_color=None      
            input_elements_background_color=None      
            element_text_color=None      
            input_text_color=None      
            scrollbar_color=None, text_color=None      
            debug_win_size=(None,None)      
            window_location=(None,None)      
            tooltip_time = None      
      
Explanation of parameters      
      
             icon - filename of icon used for taskbar and title bar      
             button_color - button color (foreground, background)      
             element_size - element size (width, height) in characters      
             margins - tkinter margins around outsize      
             element_padding - tkinter padding around each element      
             auto_size_text - autosize the elements to fit their text      
             auto_size_buttons - autosize the buttons to fit their text      
             font - font used for elements      
             border_width - amount of bezel or border around sunken or raised elements      
             slider_border_width - changes the way sliders look      
             slider_relief - changes the way sliders look      
             slider_orientation - changes orientation of slider      
             autoclose_time - time in seconds for autoclose boxes      
             message_box_line_width - number of characers in a line of text in message boxes      
             progress_meter_border_depth - amount of border around raised or lowered progress meters      
             progress_meter_style - style of progress meter as defined by tkinter      
             progress_meter_relief - relief style      
             progress_meter_color - color of the bar and background of progress meters      
             progress_meter_size - size in (characters, pixels)      
             background_color - Color of the main window's background      
             element_background_color - Background color of the elements      
             text_element_background_color - Text element background color      
             input_elements_background_color - Input fields background color      
             element_text_color - Text color of elements that have text, like Radio Buttons      
             input_text_color - Color of the text that you type in      
             scrollbar_color - Color for scrollbars (may not always work)      
             text_color - Text element default text color      
             text_justification - justification to use on Text Elements. Values are strings - 'left', 'right', 'center'      
             debug_win_size - size of the Print output window      
             window_location - location on the screen (x,y) of window's top left cornder      
             tooltip_time - time in milliseconds to wait before showing a tooltip. Default is 400ms      
      
      
These settings apply to all windows `SetOptions`.  The Row options and Element options will take precedence over these settings.  Settings can be thought of as levels of settings with the window-level being the highest and the Element-level the lowest.  Thus the levels are:      
      
 - window level      
 - Row level      
 - Element level      
      
Each lower level overrides the settings of the higher level.  Once settings have been changed, they remain changed for the duration of the program (unless changed again).      
      
# Persistent windows (Window stays open after button click)      
      
Apologies that the next few pages are perhaps confusing.  There have been a number of changes recently in PySimpleGUI's Read calls that added some really cool stuff, but at the expense of being not so simple.  Part of the issue is an attempt to make sure existing code doesn't break.  These changes are all in the area of non-blocking reads and reads with timeouts.

There are 2 ways to keep a window open after the user has clicked a button.  One way is to use non-blocking windows (see the next section).  The other way is to use buttons that 'read' the window instead of 'close' the window when clicked.  The typical buttons you find in windows, including the shortcut buttons, close the window.  These include OK, Cancel, Submit, etc.  The Button Element also closes the window.      
      
The `RButton` Element creates a button that when clicked will return control to the user, but will leave the window open and visible.  This button is also used in Non-Blocking windows.  The difference is in which call is made to read the window.  The normal `Read` call with no parameters will block, a call with a `timeout` value of zero will not block.

Note that `InputText` and `MultiLine` Elements will be **cleared**   when performing a `Read`.  If you do not want your input field to be cleared after a `Read` then you can set the `do_not_clear` parameter to True when creating those elements. The clear is turned on and off on an element by element basis.  

The reasoning behind this is that Persistent Windows are often "forms".  When "submitting" a form you want to have all of the fields left blank so the next entry of data will start with a fresh window.  Also, when implementing a "Chat Window" type of interface, after each read / send of the chat data, you want the input field cleared.  Think of it as a Texting application.  Would you want to have to clear your previous text if you want to send a second text?

The design pattern for Persistent Windows was already shown to you earlier in the document... here it is for your convenience.

```python    
import PySimpleGUI as sg      
      
layout = [[sg.Text('Persistent window')],      
          [sg.Input()],      
          [sg.RButton('Read'), sg.Exit()]]      
      
window = sg.Window('Window that stays open').Layout(layout)      
      
while True:      
    event, values = window.Read()      
    if event is None or event == 'Exit':      
        break      
    print(event, values)    

window.Close()
```    
    
  
## Read(timeout = t, timeout_key='timeout')

Read with a timeout is a very good thing for your GUIs to use in a read non-blocking situation, if you can use them.  If your device can wait for a little while, then use this kind of read.  The longer you're able to add to the timeout value, the less CPU time you'll be taking.

One way of thinking of reads with timeouts:  
> During the timeout time, you are "yielding" the processor to do other tasks.  

But it gets better than just being a good citizen....**your GUI will be more responsive than if you used a non-blocking read**

Let's say you had a device that you want to "poll" every 100ms.   The "easy way out" and the only way out until recently was this:

```python
# YOU SHOULD NOT DO THIS....
while True:             # Event Loop  
	event, values = window.ReadNonBlocking()   # DO NOT USE THIS CALL ANYMORE
	read_my_hardware() # process my device here  
	time.sleep(.1)     # sleep 1/10 second
```

This program will quickly test for user input, then deal with the hardware.  Then it'll sleep for 100ms, while your gui is non-responsive, then it'll check in with your GUI again.  I fully realize this is a crude way of doing things.  We're talking dirt simple stuff without trying to use threads, etc to 'get it right'.  It's for demonstration purposes.

The new and better way.... 
using the Read Timeout mechanism, the sleep goes away.

```python
# This is the right way to poll for hardware
while True:             # Event Loop  
	event, values = window.Read(timeout = 100) 
	read_my_hardware() # process my device here
```

This event loop will run every 100 ms.  You're making a Read call, so anything that the use does will return back to you immediately, and you're waiting up to 100ms for the user to do something.  If the user doesn't do anything, then the read will timeout and execution will return to the program.


## Non-Blocking Windows   (Asynchronous reads)

There are TWO ways to perform a non-blocking read.

The "old way" was:
```python
event, values = sg.ReadNonBlocking()
```
The new way
```python
event, values = sg.Read(timeout=0)
```
You should use the new way if you're reading this for the first time.

The difference in the 2 calls is in the value of event.  For ReadNonBlocking, event will be `None` if there are no other events to report.  There is a "problem" with this however.  With normal Read calls, an event value of None signified the window was closed.  For ReadNonBlocking, the way a closed window is returned is via the values variable being set to None.  


## sg.TIMEOUT_KEY

If you're using the new, timeout=0 method, then an event value of None signifies that the window was closed, just like a normal Read.  That leaves the question of what it is set to when not other events are happening.  This value will be the value of `timeout_key`.  If you did not specify a timeout_key value in your call to read, then it will be set to a default value of:
TIMEOUT_KEY = '__timeout__'

If you wanted to test for "no event" in your loop, it would be written like this:
```python
while True:  
    event, value = window.Read(timeout=0)  
    if event is None:  
        break # the use has closed the window  
    if event == sg.TIMEOUT_KEY:  
        print("Nothing happened")
```


Use async windows sparingly.  It's possible to have a window that appears to be async, but it is not.  **Please** try to find other methods before going to async windows.  The reason for this plea is that async windows poll tkinter over and over.  If you do not have a sleep in your loop, you will eat up 100% of the CPU time.      It's important to be a good citizen.   Don't chew up CPU cycles needlessly.

Non-blocking is generally reserved as a "last resort".  Too many times people use non-blocking reads when a blocking read will do just fine.

There is a hybrid approach... a read with a timeout.   You'll score much higher points on the impressive meter if you're able to use a lot less CPU time by using this type of read.
     
The most legit time to use a non-blocking window is when you're working directly with hardware.  Maybe you're driving a serial bus.  If you look at the Event Loop in the Demo_OpenCV_Webcam.py program, you'll see that the read is a non-blocking read.  However, there is a place in the event loop where blocking occurs.   The point in the loop where you will block is the call to read frames from the webcam.  When a frame is available you want to quickly deliver it to the output device, so you don't want your GUI blocking.  You want the read from the hardware to block.
        
Another example can be found in the demo for controlling a robot on a Raspberry Pi.  In that application you want to read the direction buttons, forward, backward, etc, and immediately take action.  If you are using RealtimeButtons, your only option at the moment is to use non-blocking windows.  You have to set the timeout to zero if you want the buttons to be real-time responsive.

However, with these buttons, adding a sleep to your event loop will at least give other processes time to execute.  It will, however, starve your GUI. The entire time you're sleeping, your GUI isn't executing.

      
### Periodically Calling`Read`      
      
Let's say you do end up using non-blocking reads... then you've got some housekeeping to do.  It's up to you to periodically "refresh" the visible GUI.  The longer you wait between updates to your GUI the more sluggish your windows will feel.  It is up to you to make these calls or your GUI will freeze.      
      
There are 2 methods of interacting with non-blocking windows.      
1. Read the window just as you would a normal window      
2. "Refresh" the window's values without reading the window. It's a quick operation meant to show the user the latest values      
      
 With asynchronous windows the window is shown, user input is read, but your code keeps right on chugging.  YOUR responsibility is to call `PySimpleGUI.Read` on a periodic basis.  Several times a second or more will produce a reasonably snappy GUI.      
      
 ## Exiting (Closing) a Persistent Window
      
If your window has a button that closes the window, then PySimpleGUI will automatically close the window for you.  If all of your buttons are ReadButtons, then it'll be up to you to close the window when done.  
To close a window, call the `Close` method.
```python
window.Close()
```
 
## Persistent Window Example - Running timer that updates
   
See the sample code on the GitHub named Demo Media Player for another example of Async windows.  We're going to make a window and update one of the elements of that window every .01 seconds.    Here's the entire code to do that.      

```python 
    import PySimpleGUI as sg  
    import time  
      
    # ----------------  Create Form  ----------------  
    sg.ChangeLookAndFeel('Black')  
    sg.SetOptions(element_padding=(0, 0))  
      
    layout = [[sg.Text('')],  
             [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],  
             [sg.ReadButton('Pause', key='button', button_color=('white', '#001480')),  
              sg.ReadButton('Reset', button_color=('white', '#007339'), key='Reset'),  
              sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]  
      
    window = sg.Window('Running Timer', no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True).Layout(layout)  
      
    # ----------------  main loop  ----------------  
    current_time = 0  
    paused = False  
    start_time = int(round(time.time() * 100))  
    while (True):  
        # --------- Read and update window --------  
        event, values = window.Read(timeout=10)  
        current_time = int(round(time.time() * 100)) - start_time  
        # --------- Display timer in window --------  
        window.FindElement('text').Update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,  
                                                                      (current_time // 100) % 60,  
                                                                      current_time % 100))
```      
  

Previously this program was implemented using a sleep in the loop to control the clock tick.  This version uses the new timeout parameter.  The result is a window that reacts quicker then the one with the sleep and the accuracy is just as good. 
    

## Instead of a Non-blocking Read --- Use `change_submits = True` or return_keyboard_events = True      
      
Any time you are thinking "I want an X Element to cause a Y Element to do something", then you want to use the `change_submits` option.      
      
***Instead of polling, try options that cause the window to return to you.***  By using non-blocking windows, you are *polling*.  You can indeed create your application by polling.  It will work.  But you're going to be maxing out your processor and may even take longer to react to an event than if you used another technique.      
      
**Examples**      
      
One example is you have an input field that changes as you press buttons on an on-screen keypad.      
      
![keypad 3](https://user-images.githubusercontent.com/13696193/45260275-a2198e80-b3b0-11e8-85fe-a4ce6484510f.jpg)      
      
      
                         
    
# Updating Elements (changing elements in active window)      

If you want to change Elements in your window after the window has been created, then you will call the Element's Update method.

**NOTE** a window **must be Read or Finalized** before any Update calls can be made.  

Here is an example of updating a Text Element

```python
import PySimpleGUI as sg  
  
layout = [ [sg.Text('My layout', key='_TEXT_')],  
           [sg.Button('Read')]]  
  
window = sg.Window('My new window').Layout(layout)  
  
while True:             # Event Loop  
  event, values = window.Read()  
    if event is None:  
        break  
  window.Element('_TEXT_').Update('My new text value')
```

Notice the placement of the Update call.  If you wanted to Update the Text Element *prior* to the Read call, outside of the event loop, then you must call Finalize on the window first.

In this example, the Update is done prior the Read.  Because of this, the Finalize call is added to the Window creation.
```python
import PySimpleGUI as sg  
  
layout = [ [sg.Text('My layout', key='_TEXT_')],  
           [sg.Button('Read')]  
         ]  
  
window = sg.Window('My new window').Layout(layout).Finalize()  
  
window.Element('_TEXT_').Update('My new text value')  
  
while True:             # Event Loop  
  event, values = window.Read()  
    if event is None:  
        break
```


Persistent windows remain open and thus continue to interact with the user after the Read has returned.  Often the program wishes to communicate results (output information) or change an Element's values (such as populating a List Element).      
    
You can use Update to do things like:      
* Have one Element (appear to) make a change to another Element      
* Disable a button, slider, input field, etc      
* Change a button's text      
* Change an Element's text or background color      
* Add text to a scrolling output window      
* Change the choices in a list      
* etc        
    
The way this is done is via an Update method that is available for nearly all of the Elements.  Here is an example of a program that uses a persistent window that is updated.      
      
![snap0272](https://user-images.githubusercontent.com/13696193/45260249-ec4e4000-b3af-11e8-853b-9b29d0bf7797.jpg)      
      
      
In some programs these updates happen in response to another Element.  This program takes a Spinner and a Slider's input values and uses them to resize a Text Element.  The Spinner and Slider are on the left, the Text element being changed is on the right.      
        
      
    # Testing async window, see if can have a slider      
    # that adjusts the size of text displayed      
      
    import PySimpleGUI as sg      
    fontSize = 12      
    layout = [[sg.Spin([sz for sz in range(6, 172)], font=('Helvetica 20'), initial_value=fontSize, change_submits=True, key='spin'),      
               sg.Slider(range=(6,172), orientation='h', size=(10,20),      
               change_submits=True, key='slider', font=('Helvetica 20')),      
               sg.Text("Aa", size=(2, 1), font="Helvetica "  + str(fontSize), key='text')]]      
      
    sz = fontSize      
    window = sg.Window("Font size selector", grab_anywhere=False).Layout(layout)      
    # Event Loop      
    while True:      
        event, values= window.Read()      
        if event is None:      
            break      
        sz_spin = int(values['spin'])      
        sz_slider = int(values['slider'])      
        sz = sz_spin if sz_spin != fontSize else sz_slider      
        if sz != fontSize:      
            fontSize = sz      
            font = "Helvetica "  + str(fontSize)      
            window.FindElement('text').Update(font=font)      
            window.FindElement('slider').Update(sz)      
            window.FindElement('spin').Update(sz)      
      
    print("Done.")      
      
      
Inside the event loop we read the value of the Spinner and the Slider using those Elements' keys.      
For example, `values['slider']` is the value of the Slider Element.      
      
This program changes all 3 elements if either the Slider or the Spinner changes.  This is done with these statements:      
      
        window.FindElement('text').Update(font=font)      
        window.FindElement('slider').Update(sz)      
        window.FindElement('spin').Update(sz)      
      
Remember this design pattern because you will use it OFTEN if you use persistent windows.      
      
It works as follows.  The call to `window.FindElement` returns the Element object represented by they provided `key`.  This element is then updated by calling it's `Update` method.  This is another example of Python's "chaining" feature. We could write this code using the long-form:      
      
    text_element = window.FindElement('text')      
    text_element.Update(font=font)      
      
The takeaway from this exercise is that keys are key in PySimpleGUI's design.  They are used to both read the values of the window and also to identify elements.  As already mentioned, they are used as targets in  Button calls.      

### Locating Elements

The Window method call that's used to find an element is:
`FindElement`
or the shortened version
`Element`

When you see a call to window.FindElement or window.Element, then you know an element is being addressed.  Normally this is done so you can call the element's Update method.  


### ProgressBar / Progress Meters

Note that to change a progress meter's progress, you call UpdateBar, not Update.      It's an old naming convention that's left over from before the Update calls were implemented.
   
      
      
# Keyboard & Mouse Capture      
Beginning in version 2.10 you can capture keyboard key presses and mouse scroll-wheel events.   Keyboard keys can be used, for example, to detect the page-up and page-down keys for a PDF viewer.  To use this feature, there's a boolean setting in the Window call `return_keyboard_events` that is set to True in order to get keys returned along with buttons.      
      
Keys and scroll-wheel events are returned in exactly the same way as buttons.      
      
For scroll-wheel events, if the mouse is scrolled up, then the `button` text will be `MouseWheel:Up`.   For downward scrolling, the text returned is `MouseWheel:Down`      
      
Keyboard keys return 2 types of key events. For "normal" keys (a,b,c, etc), a single character is returned that represents that key.  Modifier and special keys are returned as a string with 2 parts:      
      
    Key Sym:Key Code      
      
Key Sym is a string such as 'Control_L'.  The Key Code is a numeric representation of that key.  The left control key, when pressed will return the value 'Control_L:17'      
      
    import PySimpleGUI as sg  
      
    # Recipe for getting keys, one at a time as they are released  
    # If want to use the space bar, then be sure and disable the "default focus"  
      
    with sg.Window("Keyboard Test", return_keyboard_events=True, use_default_focus=False) as window:  
        text_elem = sg.Text("", size=(18, 1))  
        layout = [[sg.Text("Press a key or scroll mouse")],  
                  [text_elem],  
                  [sg.Button("OK")]]  
      
        window.Layout(layout)  
        # ---===--- Loop taking in user input --- #  
    while True:  
        event, value = window.Read()  
      
        if event == "OK"  or event is None:  
            print(event, "exiting")  
            break  
       text_elem.Update(event)

      
      
You want to turn off the default focus so that there no buttons that will be selected should you press the spacebar.      
      
### Realtime Keyboard Capture      
Use realtime keyboard capture by calling      
      
    import PySimpleGUI as sg  
      
    with sg.Window("Realtime Keyboard Test", return_keyboard_events=True, use_default_focus=False) as window:  
        layout = [[sg.Text("Hold down a key")],  
                  [sg.Button("OK")]]  
      
        window.Layout(layout)  
      
        while True:  
            event, value = window.Read(timeout=0)  
            if event == "OK"  or event is None:  
                print(event, value, "exiting")  
                break  
            if event != sg.TIMEOUT_KEY:  
                print(event)


# Menus      

## MenuBar
      
Beginning in version 3.01 you can add a MenuBar to your window.  You specify the menus in much the same way as you do window layouts, with lists.  Menu selections are returned as events and as of 3.17, also as in the values dictionary.  The value returned will be the entire menu entry, including the key if you specified one.

      
This definition:      
      
    menu_def = [['File', ['Open', 'Save', 'Exit',]],      
                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],      
                ['Help', 'About...'],]      
      
Note the placement of ',' and of [].  It's tricky to get the nested menus correct that implement cascading menus.  See how paste has Special and Normal as a list after it.  This means that Paste has a cascading menu with items Special and Normal.      
      
They menu_def layout produced this window:      
      
![menu](https://user-images.githubusercontent.com/13696193/45306723-56b7cb00-b4eb-11e8-8cbd-faef0c90f8b4.jpg)      
      

To add a menu to a Window place the `Menu` or `MenuBar` element into your layout.

    layout = [[sg.Menu(menu_def)]]

It doesn't really matter where you place the Menu Element in your layout as it will always be located at the top of the window.

## ButtonMenus

Button menus were introduced in version 3.21, having been previously released in PySimpleGUIQt.  They work exactly the same and are source code compatible between PySimpleGUI and PySimpleGUIQt.  These types of menus take a single menu entry where a Menu Bar takes a list of menu entries.

## Right Click Menus

Right Click Menus were introduced in version 3.21.  Almost every element has a right_click_menu parameter and there is a window-level setting for rich click menu that will attach a right click menu to all elements in the window.

The menu definition is the same a s the button menu definition, a single menu entry.

```python
right_click_menu = ['&Right', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]
```
The first string in a right click menu and a button menu is ***ignored***.  It is not used.  Normally you would put the string that is shown on the menu bar in that location.

**Return values for right click menus are different than menu bars and button menus.**  Instead of the value being returned through the values dictionary, it is instead sent back as an Event.  You will not
     
## Menu Shortcut keys      
You have used ALT-key in other Windows programs to navigate menus.  For example Alt-F+X exits the program.  The Alt-F pulls down the File menu.  The X selects the entry marked Exit.      
      
The good news is that PySimpleGUI allows you to create the same kind of menus!  Your program can play with the big-boys.  And, it's trivial to do.      
      
All that's required is for your to add an "&" in front of the letter you want to appear with an underscore.  When you hold the Alt key down you will see the menu with underlines that you marked.      
      
One other little bit of polish you can add are separators in your list.  To add a line in your list of menu choices, create a menu entry that looks like this: ` '---'`      
      
This is an example Menu with underlines and a separator.      
      
```      
# ------ Menu Definition ------ #      
menu_def = [['&File', ['&Open', '&Save', '---', 'Properties', 'E&xit'  ]],      
            ['&Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],      
            ['&Help', '&About...'],]      
```      
  And this is the spiffy menu it produced:      
  ![menus with shortcuts](https://user-images.githubusercontent.com/13696193/46251674-f5b74f00-c427-11e8-95c6-547adc59041b.jpg)      


##  Disabled Menu Entries

If you want one of your menu items to be disabled, then place a '!' in front of the menu entry.  To disable the Paste menu entry in the previous examples, the entry would be:
`['!&Edit', ['Paste', ['Special', 'Normal',], 'Undo'],]`

If your want to change the disabled menu item flag / character from '!' to something else, change the variable `MENU_DISABLED_CHARACTER`

## Keys for Menus

Beginning in version 3.17 you can add a `key` to your menu entries.  The `key` value will be removed prior to be inserted into the menu.  When you receive Menu events, the entire menu entry, including the `key` is returned.  A key is indicated by adding `::` after a menu entry, followed by the key.

To add the `key` `_MY_KEY_` to the Special menu entry, the code would be:

`['&Edit', ['Paste', ['Special::_MY_KEY_', 'Normal',], 'Undo'],]`
      
 If you want to change the characters that indicate a key follows from '::' to something else, change the variable `MENU_KEY_SEPARATOR`   


# Running Multiple Windows

If you wish to run multiple windows in your event loop, then there are 2 methods for doing this.  

1. First window does not remain active while second window is visible
2. First window remains active while second window is visible

You will find the 2 design matters in 2 demo programs in the Demo Program area of the GitHub (http://www.PySimpleGUI.com)

***Critically important***
When creating a new window you must use a "fresh" layout every time.  You cannot reuse a layout from a previous window.  As a result you will see the layout for window 2 being defined inside of the larger event loop.

A rule of thumb to follow:

> If you are calling `Window` then you should define your window layout
> in the statement just prior to the `Window` call.


## Multi-Window Design Pattern 1 - both windows active

```python
import PySimpleGUI as sg  
  
# Design pattern 2 - First window remains active  
  
layout = [[ sg.Text('Window 1'),],  
          [sg.Input(do_not_clear=True)],  
          [sg.Text('', key='_OUTPUT_')],  
          [sg.Button('Launch 2'), sg.Button('Exit')]]  
  
win1 = sg.Window('Window 1').Layout(layout)  
  
win2_active = False  
while True:  
    ev1, vals1 = win1.Read(timeout=100)  
    win1.FindElement('_OUTPUT_').Update(vals1[0])  
    if ev1 is None or ev1 == 'Exit':  
        break  
  
     if not win2_active and ev1 == 'Launch 2':  
        win2_active = True  
        layout2 = [[sg.Text('Window 2')],  
                   [sg.Button('Exit')]]  
  
        win2 = sg.Window('Window 2').Layout(layout2)  
  
    if win2_active:  
        ev2, vals2 = win2.Read(timeout=100)  
        if ev2 is None or ev2 == 'Exit':  
            win2_active  = False  
            win2.Close()
```


## Multi-Window Design Pattern 2 - only 1 active window

```python
import PySimpleGUIQt as sg  
  
# Design pattern 1 - First window does not remain active  
  
layout = [[ sg.Text('Window 1'),],  
          [sg.Input(do_not_clear=True)],  
          [sg.Text('', key='_OUTPUT_')],  
          [sg.Button('Launch 2')]]  
  
win1 = sg.Window('Window 1').Layout(layout)  
win2_active=False  
while True:  
    ev1, vals1 = win1.Read(timeout=100)  
    if ev1 is None:  
        break  
    win1.FindElement('_OUTPUT_').Update(vals1[0])  
  
    if ev1 == 'Launch 2'  and not win2_active:  
        win2_active = True  
        win1.Hide()  
        layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse  
                   [sg.Button('Exit')]]  
  
        win2 = sg.Window('Window 2').Layout(layout2)  
        while True:  
            ev2, vals2 = win2.Read()  
            if ev2 is None or ev2 == 'Exit':  
                win2.Close()  
                win2_active = False  
                win1.UnHide()  
                break
```
    
# Sample Applications      
      
There are too many to list!!

There are over 130 sample programs to give you a jump start.

## Packages Used In Demos      
      
      
  While the core PySimpleGUI code  does not utilize any 3rd party packages, some of the demos do.  They add a GUI to a few popular packages.  These packages include:      
  * [Chatterbot](https://github.com/gunthercox/ChatterBot)      
  * [Mido](https://github.com/olemb/mido)      
  * [Matplotlib](https://matplotlib.org/)      
  * [PyMuPDF](https://github.com/rk700/PyMuPDF)      
      
      
# Creating a Windows .EXE File      
      
It's possible to create a single .EXE file that can be distributed to Windows users. There is no requirement to install the Python interpreter on the PC you wish to run it on. Everything it needs is in the one EXE file, assuming you're running a somewhat up to date version of Windows.      
      
Installation of the packages, you'll need to install PySimpleGUI and PyInstaller (you need to install only once)      
      
```      
pip install PySimpleGUI      
pip install PyInstaller      
      
```      
      
To create your EXE file from your program that uses PySimpleGUI,  `my_program.py`, enter this command in your Windows command prompt:      
      
```      
pyinstaller -wF my_program.py      
      
```      
      
You will be left with a single file,  `my_program.exe`, located in a folder named  `dist`  under the folder where you executed the  `pyinstaller`  command.      
      
That's all... Run your  `my_program.exe`  file on the Windows machine of your choosing.      
      
> "It's just that easy."      
      
(famous last words that screw up just about anything being referenced)      
      
Your EXE file should run without creating a "shell window". Only the GUI window should show up on your taskbar.      
      
If you get a crash with something like:      
```      
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
      
    import PySimpleGUI as sg      
    print = sg.Print      
      
This will turn all of your print statements into prints that display in a window on your screen rather than to the terminal.      
      
**Look and Feel**      
Dial in the look and feel that you like with the `SetOptions` function.  You can change all of the defaults in one function call.  One line of code to customize the entire GUI.      
Or beginning in version 2.9 you can choose from a look and feel using pre-defined color schemes.   Call ChangeLookAndFeel with a description string.      
      
    sg.ChangeLookAndFeel('GreenTan')      
      
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
      
## Versions      
|Version | Description |      
|--|--|      
| 1.0.9   | July 10, 2018 - Initial Release |      
| 1.0.21 | July 13, 2018 - Readme updates  |      
| 2.0.0 | July 16, 2018 - ALL optional parameters renamed from CamelCase to all_lower_case      
| 2.1.1 | July 18, 2018 - Global settings exposed, fixes      
| 2.2.0| July 20, 2018 - Image Elements, Print output      
| 2.3.0 | July 23, 2018 - Changed form.Read return codes, Slider Elements, Listbox element. Renamed some methods but left legacy calls in place for now.      
| 2.4.0 | July 24, 2018 - Button images. Fixes so can run on Raspberry Pi      
| 2.5.0 | July 26, 2018 - Colors. Listbox scrollbar. tkinter Progress Bar instead of homegrown.      
| 2.6.0 | July 27, 2018 - auto_size_button setting.  License changed to LGPL 3+      
| 2.7.0 | July 30, 2018 - realtime buttons, window_location default setting      
| 2.8.0 | Aug 9, 2018 - New None default option for Checkbox element, text color option for all elements, return values as a dictionary, setting focus, binding return key      
| 2.9.0 | Aug 16,2018 - Screen flash fix, `do_not_clear` input field option, `autosize_text` defaults to `True` now, return values as ordered dict, removed text target from progress bar, rework of return values and initial return values, removed legacy Form.Refresh() method (replaced by Form.ReadNonBlockingForm()), COLUMN elements!!, colored text defaults      
| 2.10.0 | Aug 25, 2018 - Keyboard & Mouse features (Return individual keys as if buttons, return mouse scroll-wheel as button, bind return-key to button, control over keyboard focus), SaveAs Button, Update & Get methods for InputText, Update for Listbox, Update & Get for Checkbox, Get for Multiline, Color options for Text Element Update, Progess bar Update can change max value, Update for Button to change text & colors, Update for Image Element, Update for Slider, Form level text justification, Turn off default focus, scroll bar for Listboxes, Images can be from filename or from in-RAM, Update for Image).  Fixes - text wrapping in buttons, msg box, removed slider borders entirely and others      
| 2.11.0 | Aug 29, 2018 - Lots of little changes that are needed for the demo programs to work. Buttons have their own default element size, fix for Mac default button color, padding support for all elements, option to immediately return if list box gets selected, FilesBrowse button, Canvas Element, Frame Element, Slider resolution option, Form.Refresh method, better text wrapping, 'SystemDefault' look and feel settin      
| 2.20.0 | Sept 4, 2018 - Some sizable features this time around of interest to advanced users.  Renaming of the MsgBox functions to Popup. Renaming GetFile, etc, to PopupGetFile. High-level windowing capabilities start with Popup, PopupNoWait/PopupNonblocking, PopupNoButtons, default icon, change_submits option for Listbox/Combobox/Slider/Spin/, New OptionMenu element, updating elements after shown, system defaul color option for progress bars, new button type (Dummy Button) that only closes a window, SCROLLABLE Columns!! (yea, playing in the Big League now), LayoutAndShow function removed, form.Fill - bulk updates to forms, FindElement - find element based on key value (ALL elements have keys now), no longer use grid packing for row elements (a potentially huge change), scrolled text box sizing changed, new look and feel themes (Dark, Dark2, Black, Tan, TanBlue, DarkTanBlue, DarkAmber, DarkBlue, Reds, Green)      
| 2.30.0 | Sept 6, 2018 - Calendar Chooser (button), borderless windows, load/save form to disk      
| 3.0.0 | Sept 7, 2018 - The "fix for poor choice of 2.x numbers" release. Color Chooser (button), "grab anywhere" windows are on by default, disable combo boxes, Input Element text justification (last part needed for 'tables'), Image Element changes to support OpenCV?, PopupGetFile and PopupGetFolder have better no_window option      
| 3.01.01 | Sept 10, 2018 - Menus! (sort of a big deal)      
| 3.01.02 | Step 11, 2018 - All Element.Update functions have a `disabled` parameter so they can be disabled.  Renamed some parameters in Update function (sorry if I broke your code), fix for bug in Image.Update. Wasn't setting size correctly, changed grab_anywhere logic again,added grab anywhere option to PupupGetText (assumes disabled)      
| 3.02.00 | Sept 14, 2018 - New Table Element (Beta release), MsgBox removed entirely, font setting for InputText Element, **packing change** risky change that allows some Elements to be resized,removed command parameter from Menu Element, new function names for ReadNonBlocking (Finalize, PreRead), change to text element autosizing and wrapping (yet again), lots of parameter additions to Popup functions (colors, etc).      
| 3.03.00 | New feature - One Line Progress Meters, new display_row_numbers for Table Element, fixed bug in EasyProgresssMeters (function will soon go away), OneLine and Easy progress meters set to grab anywhere but can be turned off.      
| 03,04.00 | Sept 18, 2018 - New features - Graph Element, Frame Element, more settings exposed to Popup calls.  See notes below for more.      
| 03.04.01 | Sept 18, 2018 - See release notes      
| 03.05.00 | Sept 20, 2018 - See release notes      
| 03.05.01 | Sept 22, 2018 - See release notes      
| 03.05.02 | Sept 23, 2018 - See release notes      
| 03.06.00 | Sept 23, 2018 - Goodbye FlexForm, hello Window      
| 03.08.00 | Sept 25, 2018 - Tab and TabGroup Elements\      
| 01.00.00 for 2.7 | Sept 25, 2018 - First release for 2.7      
| 03.08.04 | Sept 30, 2018 - See release notes      
| 03.09.00 | Oct 1, 2018 |    
| 2.7 01.01.00 | Oct 1, 2018    
| 2.7 01.01.02 | Oct 8, 2018    
| 03.09.01 | Oct 8, 2018    
| 3.9.3 & 1.1.3 | Oct 11, 2018   
| 3.9.4 & 1.1.4 | Oct 16, 2018 
| 3.10.1 & 1.2.1 | Oct 20, 2018 
| 3.10.3 & 1.2.3 | Oct 23, 2018     
| 3.11.0 & 1.11.0 | Oct 28, 2018    
| 3.12.0 & 1.12.0 | Oct 28, 2018
| 3.13.0 & 1.13.0 | Oct 29, 2018
| 3.14.0 & 1.14.0 | Nov 2, 2018
| 3.15.0 & 1.15.0 | Nov 20, 2018
| 3.16.0 & 1.16.0 | Nov 26, 2018
| 3.17.0 & 1.17.0 | Dec 1, 2018
      
## Release Notes      
2.3 - Sliders, Listbox's and Image elements (oh my!)      
      
If using Progress Meters, avoid cancelling them when you have another window open.  It could lead to future windows being blank. It's being worked on.      
      
New debug printing capability.  `sg.Print`      
      
2.5 Discovered issue with scroll bar on `Output` elements.  The bar will match size of ROW not the size of the element.  Normally you never notice this due to where on a form the `Output` element goes.      
      
Listboxes are still without scrollwheels. The mouse can drag to see more items.  The mouse scrollwheel will also scroll the list and will `page up` and `page down` keys.      
      
2.7 Is the "feature complete" release. Pretty much all features are done and in the code      
      
2.8 More text color controls.  The caller has more control over things like the focus and what buttons should be clicked when enter key is pressed. Return values as a dictionary! (NICE addition)      
      
2.9 COLUMNS!  This is the biggest feature and had the biggest impact on the code base.  It was a difficult feature to add, but it was worth it.  Can now make even more layouts. Almost any layout is possible with this addition.      
      
.................. insert releases 2.9 to 2.30 .................      
      
3.0 We've come a long way baby!  Time for a major revision bump.  One reason is that the numbers started to confuse people  the latest release was 2.30, but some people read it as 2.3 and thought it went backwards.  I kinda messed up the 2.x series of numbers, so why not start with a clean slate.  A lot has happened anyway so it's well earned.      
      
One change that will set PySimpleGUI apart is the parlor trick of being able to move the window by clicking on it anywhere.  This is turned on by default.  It's not a common way to interact with windows.  Normally you have to move using the titlebar.  Not so with PySimpleGUI.  Now you can drag using any part of the window.  You will want to turn off for windows with sliders.  This feature is enabled in the Window call.      
      
Related to the Grab Anywhere feature is the no_titlebar option, again found in the call to Window.  Your window will be a spiffy, borderless window.  It's a really interesting effect.  Slight problem is that you do not have an icon on the taskbar with these types of windows, so if you don't supply a button to close the window, there's no way to close it other than task manager.      
      
3.0.2 Still making changes to Update methods with many more ahead in the future.  Continue to mess with grab anywhere option.  Needed to disable in more places such as the PopupGetText function.  Any time these is text input on a form, you generally want to turn off the grab anywhere feature.      
      
#### 3.2.0      
 Biggest change was the addition of the Table Element.  Trying to make changes so that form resizing is a possibility but unknown if will work in the long run.  Removed all MsgBox, Get* functions and replaced with Popup functions.  Popups had multiple new parameters added to change the look and feel of a popup.      
      
#### 3.3.0      
OneLineProgressMeter function added which gives you not only a one-line solution to progress meters, but it also gives you the ability to have more than 1 running at the same time, something not possible with the EasyProgressMeterCall      
      
#### 3.4.0      
      
* Frame - New Element - a labelled frame for grouping elements. Similar      
   to Column      
* Graph (like a Canvas element except uses the caller's      
   coordinate system rather than tkinter's).      
* initial_folder - sets starting folder for browsing type buttons (browse for file/folder).      
* Buttons return  key value rather than button text **If** a `key` is specified,      
*      
   OneLineProgressMeter!  Replaced EasyProgressMeter (sorry folks that's      
   the way progress works sometimes)      
 * Popup - changed ALL of the Popup calls to   provide many more customization settings      
    * Popup      
    * PopupGetFolder      
    * PopupGetFile      
    * PopupGetText      
    * Popup      
    * PopupNoButtons      
    * PopupNonBlocking      
    * PopupNoTitlebar      
    * PopupAutoClose      
    * PopupCancel      
    * PopupOK      
    * PopupOKCancel      
    * PopupYesNo      
      
#### 3.4.1      
* Button.GetText - Button class method.  Returns the current text being shown on a button.      
* Menu - Tearoff option. Determines if menus should allow them to be torn off      
* Help - Shorcut button. Like Submit, cancel, etc      
* ReadButton - shortcut for ReadFormButton      
      
#### 3.5.0      
* Tool Tips for all elements      
* Clickable text      
* Text Element relief setting      
* Keys as targets for buttons      
* New names for buttons:      
   * Button = SimpleButton      
   * RButton = ReadButton = ReadFormButton      
* Double clickable list entries      
* Auto sizing table widths works now      
* Feature DELETED - Scaling. Removed from all elements      
      
#### 3.5.1      
* Bug fix for broken PySimpleGUI if Python version < 3.6 (sorry!)      
* LOTS of Readme changes      
      
#### 3.5.2      
* Made `Finalize()` in a way that it can be chained      
* Fixed bug in return values from Frame Element contents      
      
#### 3.6.0      
* Renamed FlexForm to Window      
* Removed LookAndFeel capability from Mac platform.      
      
#### 3.8.0      
* Tab and TabGroup Elements - awesome new capabilities      
      
#### 1.0.0 Python 2.7      
It's official.  There is a 2.7 version of PySimpleGUI!      
      
#### 3.8.2      
* Exposed `TKOut` in Output Element      
* `DrawText` added to Graph Elements      
* Removed `Window.UpdateElements`      
* `Window.grab_anywere` defaults to False      
      
#### 3.8.3      
* Listbox, Slider, Combobox, Checkbox,  Spin, Tab Group - if change_submits is set, will return the Element's key rather than ''      
* Added change_submits capability to Checkbox, Tab Group      
* Combobox - Can set value to an Index into the Values table rather than the Value itself      
* Warnings added to Drawing routines for Graph element (rather than crashing)      
* Window - can "force top level" window to be used rather than a normal window.  Means that instead of calling Tk to get a window, will call TopLevel to get the window      
* Window Disable / Enable - Disables events (button clicks, etc) for a Window.  Use this when you open a second window and want to disable the first window from doing anything. This will simulate a 'dialog box'      
* Tab Group returns a value with Window is Read.  Return value is the string of the selected tab      
* Turned off grab_anywhere for Popups      
* New parameter, default_extension, for PopupGetFile      
* Keyboard shortcuts for menu items. Can hold ALT key to select items in men      
* Removed old-style Tabs - Risky change because it hit fundamental window packing and creation. Will also break any old code using this style tab (sorry folks this is how progress happens)      
      
#### 3.8.6      
      
* Fix for Menus.      
* Fixed table colors. Now they work      
* Fixed returning keys for tabs      
* Window Hide / UnHide methods      
* Changed all Popups to remove context manager      
* Error checking for Graphing objects and for Element Updates      
    
### 3.9.0 & 1.1.0    
* The FIRST UNIFIED version of the code!    
* Python 2.7 got a TON of features . Look back to 1.0 release for the list    
* Tab locations - Can place Tabs on top, bottom, left, right now instead of only the top    
    
### 3.9.1 & 1.1.2    
* Tab features    
   * Themes    
   * Enable / Disable    
   * Tab text colors    
   * Selected tab color    
* New GetListValues method for Listbox    
* Can now have multiple progress bars in 1 window    
* Fix for closing debug-output window with other windows open    
* Topanga Look and Feel setting    
* User can create new look and feel settings / can access the look and feel table    
* New PopupQuick call. Shows a non-blocking popup window with auto-close    
* Tree Element partially done (don't use despite it showing up)    
    
### 3.9.3 & 1.1.3    
    
* Disabled setting when creating element for:    
   * Input    
  * Combo    
  * Option Menu    
  * Listbox    
  * Radio    
  * Checkbox    
  * Spinner    
  * Multiline    
  * Buttons    
  * Slider    
* Doc strings on all Elements updated    
* Buttons can take image data as well as image files    
* Button Update can change images    
* Images can have background color    
* Table element new num_rows parameter    
* Table Element new alternating_row_color parameter    
* Tree Element    
* Window Disappear / Reappear methods    
* Popup buttons resized to same size    
* Exposed look and feel table    
    
###  3.9.4 & 1.1.4

* Parameter order change for Button.Update so that new button ext is at front
* New Graph.DrawArc method
* Slider tick interval parameter for labeling sliders
* Menu tearoff now disabled by default
* Tree Data printing simplified and made prettier
* Window resizable parameter.  Defaults to not resizable
* Button images can have text over them now
* BUG fix in listbox double-click.  First bug fix in months
* New Look And Feel capability.  List predefined settings using ListOfLookAndFeelValues

### 3.10.1 & 1.2.1
* Combobox new readonly parameter in init and Update
* Better default sizes for Slider
* Read of Tables now returns which rows are selected (big damned deal feature)
* PARTIAL support of Table.Update with new values (use at your own peril)
* Alpha channel setting for Windows
* Timeout setting for Window.Read (big damned deal feature)
* Icon can be base64 image now in SetIcon call
* Window.FindElementWithFocus call
* Window.Move allows moving window anywhere on screen
* Window.Minimize will minimize to taskbar
* Button background color can be set to system default (i.e. not changed)

### 3.10.2 & 1.2.2
Emergency patch release... going out same day as previous release
* The timeout timer for the new Read with timer wasn't being properly shut down
* The Image.Update method appears to not have been written correctly.  It didn't handle base64 images like the other elements that deal with images (buttons)


### 3.10.3 & 1.2.3

* New element - Vertical Separator
* New parameter for InputText - change_submits. If True will cause Read to return when a button fills in the InputText element
* Read with timeout = 0 is same as read non blocking and is the new preferred method
  * Will return event == None if window closed
* New Close method will close all window types
* Scrollbars for Tables automatically added (no need for a Column Element)
* Table Update method complete
* Turned off expand when packing row frame... was accidentally turned on (primary reason for this release)
* Try added to Image Update so won't crash if bad image passed in

### 3.11.0 & 1.11.0
* Syncing up the second digit of the releases so that they stay in sync better.  the 2.7 release is built literally from the 3.x code so they really are the same
* Reworked Read call... significantly.
* Realtime buttons work with timeouts or blocking read
* Removed default value parm on Buttons and Button Updates
* New Tree Element parm show_expanded. Causes Tree to be shown as fully expanded
* Tree Element now returns which rows are selected when Read
* New Window method BringToFront
* Shortcut buttons no longer close windows!
* Added CloseButton, CButton that closes the windows

### 3.12.0 & 1.12.0
* Changed Button to be the same as ReadButton which means it will no longer close the window
* All shortcut buttons no longer close the window
* Updating a table clears selected rows information in return values
* Progress meter uses new CloseButton
* Popups use new CloseButton

### 3.13.0 & 1.13.0
* Improved multiple window handling of Popups when the X is used to close
* Change submits added for:
  * Multiline
  * Input Text
  * Table
  * Tree
 * Option to close calendar chooser when date selected
 * Update for Tree Element
 * Scroll bars for Trees
 

### 3.14.0 & 1.14.0
* More windowing changes... 
	* using a hidden root windowing (Tk())
	* all children are Toplevel() windows
* Read only setting for:
	* Input Text
	* Multiline
* Font setting for InputCombo, Multiline
* change_submits setting for Radio Element
* SetFocus for multiline, input elements
* Default mon, day, year for calendar chooser button
* Tree element update, added ability to change a single key
* Message parm removed from ReadNonBlocking
* Fix for closing windows using X
* CurrentLocation method for Windows
* Debug Window options
	* location
	* font
	* no_button
	* no_titlebar
	* grab_anywhere
	* keep_on_top
* New Print / EasyPrint options
	* location
	* font
	* no_button
	* no_titlebar
	* grab_anywhere
	* keep_on_top
* New popup, PopupQuickMessage
* PopupGetFolder, PopupGetFile new initial_folder parm


### 3.15.0 & 1.15.0

* Error checking for InputText.Get method
* Text color, background color added to multiline element.Update
* Update method for Output Element - gives ability to clear the output
* Graph Element - Read returns values if new flages set
	* Change submits, drag submits
	*	Returns x,y coordinates
* Column element new parm vertical_scroll_only
* Table element new parm - bind return key - returns if return or double click
* New Window parms - size, disable_close
* "Better" multiwindow capabilities
* Window.Size property
* Popups - new title parm, custom_text
	* title sets the window title
	* custom_text - single string or tuple string sets text on button(s)

### 3.16.0 & 1.16.0
* Bug fix in PopupScrolled
* New `Element` shortcut function for `FindElement`
* Dummy Stretch Element made for backwards compatibility with Qt
* Timer function prints in milliseconds now, was seconds

### 3.17.0 &1.17.0 2-Dec-2018
3.17.0 2-Dec-2017
* Tooltip offset now programmable.  Set variable DEFAULT_TOOLTIP_OFFSET.  Defaults to (20,-20)
* Tooltips are always on top now
* Disable menu items
* Menu items can have keys
* StatusBar Element (preparing for a real status bar in Qt)
* enable_events parameter added to ALL Elements capable of generating events
* InputText.Update select parameter will select the input text
* Listbox.Update - set_to_index parameter will select a single items
* Menus can be updated!
* Menus have an entry in the return values
* LayoutAndRead depricated
* Multi-window support continues (X detection)
* PopupScrolled now has a location parameter
* row_height parameter to Table Element
* Stretch Element (DUMMY) so that can be source code compatible with Qt
* ButtonMenu Element (DUMMY) so can be source code compat with Qt.  Will implement eventually

## 3.18.0  11-Dec-2018

 NOTE - **Menus are broken** on version 2.7.  Don't know how long they've been this way.  Please get off legacy Python if that's what you're running.
 
* Default progress bar length changed to shorter
* Master window and tracking of num open windows moved from global to Window class variable
* Element visibility setting (when created and when Updating element)
* Input text visiblity
* Combo visiblity
* Combo replaces InputCombo as the primary class name
* Option menu visibility
* Listbox visiblity
* Listbox new SetFocus method
* Radio visibility
* Checkbox visibility
* Spin visiblity
* Spin new Get method returns current value
* Multiline visiblity
* Text visibility
* StatusBar visiblity
* Output visibility
* Button visibility
* Button SetFocus
* ProgressBar - New Update method (used only for visibility)
* Image - clickable images!  enable_events parameter
* Image visibility
* Canvas visibility
* Graph visibility
* Graph - new DrawImage capability (finally)
* Frame visibility
* Tab visibility (may not be fully functional)
* TabGroup visibility
* Slider visibility
* Slider - new disable_number_display parameter
* Column visibilty
* Menu visibility - Not functional
* Table visibility
* Table - new num_rows parm for Update - changes number of visible rows
* Tree visiblity
* Window - New element_padding parameter will get padding for entire window
* OneLineProgressMeter - Completely REPLACED the implementation
* OneLineProgressMeter - can get reason for the cancellation (cancel button versus X)
* EasyProgressMeter - completely removed. Use OneLineProgressMeter instead
* Debug window, EasyPrint, Print - debug window will re-open if printed to after being closed
* SetOptions - can change the error button color
* Much bigger window created when running PySimpleGUI.py by itself.  Meant to help with regression testing

## 3.19.2  13-Dec-2018

* Warning for Mac's when trying to change button color
* New parms for Button.Update - image_size and image_subsample
* Buttons - remove highlight when border depth == 0
* OneLineProgressMeter - better layout implementation

## 3.20.0 & 1.20.0 18-Dec-2018

* New Pane Element
* Graph.DeleteFigure method
* disable_minimize - New parameter for Window
* Fix for 2.7 menus
* Debug Window no longer re-routes stdout by default
* Can re-route by specifying in Print / EasyPrint call
* New non-blocking for PopupScrolled
* Can set title for PopupScrolled window


## 3.21.0 & 1.21.0 28-Dec-2018

* ButtonMenu Element
* Embedded base64 default icon
* Input Text Right click menu
* Disabled Input Text are now 'readonly' instead of disabled
* Listbox right click menu
* Multiline right click menu
* Text right click menu
* Output right click menu
* Image right click menu
* Canvas right click menu
* Graph right click menu
* Frame right click menu
* Tab, tabgroup right click menu (unsure if works correctly)
* Column right click menu
* Table right click menu
* Tree right click menu
* Window level right click menu
* Window icon can be filename or bytes (Base64 string)
* Window.Maximize method
* Attempted to use Styles better with Combobox
* Fixed bug blocking setting bar colors in OneLineProgressMeter

# 3.22.0 PySimpleGUI / 1.22.0 PySimpleGUI27

* Added type hints to some portions of the code
* Output element can be made invisible
* Image sizing and subsample for Button images
* Invisibility for ButtonMenusup
* Attempt at specifying size of Column elements (limited success)
* Table Element
  * New row_colors parameter
  * New vertical_scroll_only parameter - NOTE - will have to disable to get horizontal scrollbars
* Tree Element
  * New row_height parameter
  * New feature - Icons for tree entries using filename or Base64 images
* Fix for bug sending back continuous mouse events
* New parameter silence_on_error for FindElement / Element calls
* Slider returns float now
* Fix for Menus when using Python 2.7
* Combobox Styling (again)


# 3.2.0 PySimpleGUI /  1.23.0 PySimpleGUI27 16-Jan-2019

* Animated GIFs!
* Calendar Chooser stays on top of other windows
* Fixed bug of no column headings for Tables
* Tables now use the font parameter

# 3.24.0 1.24.0 16-Jan-2019

* PopupAnimated - A popup call for showing "loading" type of windows

# 3.25 & 1.25 20-Feb-2019

* Comments :-)
* Convert Text to string right away
* Caught exceptions when main program shut down with X
* Caught exceptions in all of the graphics primitives
* Added parameter exportselection=False to Listbox so can use multiple listboxes
* OneLineProgressMeter - Can now change the text on every call if desired


## 3.27.0 PySimpleGUI  31-Mar-2019

Mixup.... 3.26 changes don't appear to have been correctly released so releasing in 3.27 now

* do_not_clear now defaults to TRUE!!!
  * Input Element
  * Multiline Element
* Enable Radio Buttons to be in different containers
* Ability to modify Autoscroll setting in Multiline.Update call
* PopupGetFolder, PopupGetFile, PopupGetText - title defaults to message if none provided
* PopupAnimated - image_source can be a filename or bytes (base64)
* Option Menu can now have values updated

## 3.28.0 11-Apr-2019 PySimpleGUI

* NEW Window Parameter - layout - second parameter. Can pass in layout directly now!
* New shortcuts
	* I = InputText
	* B = Btn = Butt = Button
* Convert button text to string when creating buttons
* Buttons are returned now as well as input fields when searching for element with focus

## 3.29 22-Apr-2019

* New method for `Graph` - `RelocateFigure`
* Output Element no longer accepts focus

## 3.32.0 PySimpleGUI 24-May-2019

* Rework of ALLL Tooltips. Was always displaying at uttuper left part of element. Not displays closer to where mouse entered or edited
* New Element.Widget base class variable. Brings tkinter into the newer architecture of user accessibility to underlying GUI Frameworks' widgets
* New SetTooltip Element method. Means all Elements gain this method. Can set the tooltip on the fly now for all elements
* Include scroll bar when making visible / invisible Listbox Elements
* New Radio Element method - `Radio.ResetGroup()` sets all elements in the Radio Group to False* Added borderwidth to Multiline Element
* `Button.Click()` - new method - Generates a button click even as if a user clicked a button (at the tkinter level)
* Made a Graph.Images dictionary to keep track of images being used in a graph.  When graph is deleted, all of the accociated images should be deleted too.'
* Added `Graph.SetFocus()` to give a Graph Element the focus just as you can input elements 
* Table new parameter - `hide_vertical_scroll` if True will hide the table's vertical bars 
* Window - new parameter - `transparent_color`. Causes a single color to become completely transparent such that you see through the window, you can click through the window. Its like tineows never was there.
* The new `Window.AllKeysDict = {}` has been adopted by all PySimpleGUI ports.  It's a new method of automatically creating missing keys, storing and retrieving keys in general for a window.
* Changed how `window.Maximize` is implemented previously used the '-fullscreen' attribute.  Now uses the 'zoomed' state
* Window gets a new `Normal()` method to return from Maximize state.  Sets root.state('normal')
* Window.Close() now closes the special `Window.hidden_master_root` window when the "last" window is closed
* `Window.SetTransparentColor` method added.  Same effect as if window was created with parameter set
* An Element's Widget stored in `.Widget` attribute
* Making ComboBox's ID unique by using it's Key
* Changed Multiline to be sunken and have a border depth setting now
* Removed a second canvas that was being used for Graph element.  
* Changed how no titlebar is implemented running on Linux versus Windows. -type splash now used for Linux
* PopupScrolled - Added back using CloseButton to close the window
* Fixed PopupGetFolder to use correct PySimpleGUI program constructs (keys)
* PopupGetText populated values carrectly using the value variable, used keys
* PopupAnimated finally gets a completely transparent background


## 3.33.0 and 1.33 PySimpleGUI 25-May-2019

* Emergency fix due to debugger.  Old bug was that Image Element was not testing for COLOR_SYSTEM_DEFAULT correctly.


## 3.34.0 PySimpleGUI & 1.34.0 PySimpleGUI27 25-May-2019

  pip rhw  w cenf
* Fixed Window.Maximize and Window.Normal - needed special code for Linux
* Check for DEFAULT_SCROLLBAR_COLOR not being the COLOR_SYSTEM_DEFAULT (crashed)


## 3.35 PySimpleGUI & 1.35 PySimpleGUI27 27-May-2019

* Bug fix - when setting default for Checkbox it was also disabling the element!


## 3.36 PySimpleGUI & 1.36 PySimpleGUI27 29-May-2019

A combination of user requests, and needs of new `imwatchingyou` debugger

* New Debugger Icon for future built-in debugger
* Fixed bug in FindBoundReturnKey - needed to also check Panes
* NEW Window functions to turn on/off the Grab Anywhere feature
	* `Window.GrabAnyWhereOn()`
	* `Window.GrabAnyWhereOff()`
* New "Debugger" button that's built-in like other buttons.  It's a TINY button with a logo. For future use when a debugger is built into PySimpleGUI itself (SOON!)
* Change Text Element Wrap Length calculation.  Went fromn +40 pixels to +10 pixels in formula
* PopupGetFile has new parameter - `multiple_files`. If True then allows selection of multiple files


## 3.37 PySimpleGUI & 1.37 PySimpleGUI27 1-June-2019

* The built-in debugger is HERE - might not WORK exactly yet, but a lot of code went into te PySimpleGUI.py file for this.  At the moment, the `imwatchingyou` package is THE way to use a PySimpleGUI debugger. But soon enough you won't need that project in order to debug your program.
* Some strange code reformatting snuck in.  There are 351 differences between this and previous release.  I'm not sure what happened but am looking at every change by hand.
* New Calendar Button features
    * locale, format - new parameters to TKCalendar call
    * Use custom icon for window if one has been set
    * New parameters to CalendarButton - `locale`, `format`
* The bulk of the built-in PySimpleGUI debugger has been added but is not yet "officially supported".  Try pressing "break" or "ctrl+break" on your keyboard.
    * New bindings for break / pause button and debugger
    * New Debug button will launch debugger.     
    * New parameter `debugger_enabled` added to Window call.  Default is __enabled__.
    * Your progam's call to Read is all that's needed to refresh debugger
    * New `Window` methods to control debugger access
        * `EnableDebugger` - turns on HOTKEYS to debugger
        * `DisableDebugger` - turns off HOTKEYS to debugger
* Restored wrap len for Text elements back from +10 to +40 pixels
* `PopupGetFolder`, `PopupGetFile` - fixed so that the "hidden" master window stays hidden (a Linux problem)
* Added support for Multiple Files to `PopupGetFiles` when no_window option has been set.




### Upcoming      
Make suggestions people!  Future release features      
         
         
## Code Condition      
      
    Make it run      
    Make it right      
    Make it fast      
      
It's a recipe for success if done right.  PySimpleGUI has completed the "Make it run" phase.  It's far from "right" in many ways.  These are being worked on.  The module is particularly poor for PEP 8 compliance.  It was a learning exercise that turned into a somewhat complete GUI solution for lightweight problems.      
      
While the internals to PySimpleGUI are a tad sketchy, the public interfaces into the SDK are more strictly defined and comply with PEP 8 for the most part.      
      
Please log bugs and suggestions in the GitHub!  It will only make the code stronger and better in the end, a good thing for us all, right?      
      
## Design      
      
A moment about the design-spirit of `PySimpleGUI`.  From the beginning, this package was meant to take advantage of Python's capabilities with the goal of programming ease.      
      
**Single File**      
While not the best programming practice, the implementation resulted in a single file solution.  Only one file is needed, PySimpleGUI.py.  You can post this file, email it, and easily import it using one statement.      
      
**Functions as objects**      
In Python, functions behave just like object. When you're placing a Text Element into your form, you may be sometimes calling a function and other times declaring an object.  If you use the word Text, then you're getting an object.  If you're using `Txt`, then you're calling a function that returns a `Text` object.      
      
**Lists**      
It seemed quite natural to use Python's powerful list constructs when possible.  The form is specified as a series of lists.  Each "row" of the GUI is represented as a list of Elements. When the form read returns the results to the user, all of the results are presented as a single list.  This makes reading a form's values super-simple to do in a single line of Python code.      
      
**Dictionaries**      
Want to view your form's results as a dictionary instead of a list... no problem, just use the `key` keyword on your elements.  For complex forms with a lot of values that need to be changed frequently, this is by far the best way of consuming the results.      
      
You can also look up elements using their keys.  This is an excellent way to update elements in reaction to another element.  Call `form.FindElement(key)` to get the Element.      
    
**Named / Optional Parameters**    
This is a language feature that is featured **heavily**  in all of the API calls, both functions and classes.  Elements are configured, in-place, by setting one or more optional parameters.  For example, a Text element's color is chosen by setting the optional `text_color` parameter.    

**tkinter**
tkinter is the "official" GUI that Python supports.  It runs on Windows, Linux, and Mac.  It was chosen as the first target GUI framework due to its ***ubiquity***.  Nearly all Python installations, with the exception of Ubuntu Linux, come pre-loaded with tkinter.   It is the "simplest" of the GUI frameworks to get up an running (among Qt, WxPython, Kivy, etc).

From the start of the PSG project, tkinter was not meant to be the only underlying GUI framework for PySimpleGUI.  It is merely a starting point.  All journeys begin with one step forward and choosing tkinter was the first of many steps for PySimpleGUI.  Now there are 4 ports up and running - tkinter, WxPython, Qt and Remi (web support)

      
## Author      
Mike - who wrote PySimpleGUI is not important. It's the software that's important
      

## License      
      
GNU Lesser General Public License (LGPL 3) +      
      
## Acknowledgments      

#### SORRY!! Will add these back.  Lost due to file length limitation
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIxNjg5MDM1Niw4NjQ5Nzg3NjUsLTEwNj
U5NzgxMjYsNTE5MDU1OTQsMjA1MzEyNTE0OSwtMTU3ODc0NjU4
OCwyNjA1ODQ4MTQsMTEwMjA4ODMzMywxNjc5ODUwOTkyLC0xND
YxNDI4MSwtNjA2MzcxMTgsLTUwOTM1OTEyMywtMjQ4OTc2Mjks
MTMwNzY5MjU5LC0yOTY3ODM1NSwtNzc0MDc0MjMwLDI2NjM2ND
QxNyw0NDk0MzMyNDMsLTExNDg0OTA2MjNdfQ==
-->