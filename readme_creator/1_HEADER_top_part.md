<!--
HOW DO I INSERT IMAGES ???
	easy.

	■■■ 1 pic at CENTER ■■■

	<div align="center" style="padding: 5px;">
		<img src="...">
	</div>

	■■■ N pic, inline, Space around ■■■

	<p style="display: flex;justify-content: space-around;">
		<img src="...">
	</p>

	■■■ N pic, inline, padding ■■■

	<p style="display: flex;justify-content: space-around;">
		<img style="padding:10px;" src="..." >
		<img style="padding:10px;" src="..." >
		<img style="padding:10px;" src="..." >
	</p>


 -->

![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)

[![Downloads](http://pepy.tech/badge/pysimplegui)](http://pepy.tech/project/pysimplegui) tkinter

[![Downloads ](https://pepy.tech/badge/pysimplegui27)](https://pepy.tech/project/pysimplegui27) tkinter 2.7

[![Downloads](https://pepy.tech/badge/pysimpleguiqt)](https://pepy.tech/project/pysimpleguiqt) Qt

[![Downloads](https://pepy.tech/badge/pysimpleguiwx)](https://pepy.tech/project/pysimpleguiWx) WxPython

[![Downloads](https://pepy.tech/badge/pysimpleguiweb)](https://pepy.tech/project/pysimpleguiWeb) Web (Remi)


![Documentation Status](https://readthedocs.org/projects/pysimplegui/badge/?version=latest)
![Awesome Meter](https://img.shields.io/badge/Awesome_meter-100-yellow.svg)
![Python Version](https://img.shields.io/badge/Python-2.7_3.x-yellow.svg)

[![PyPI Version](https://img.shields.io/pypi/v/pysimplegui.svg?style=for-the-badge)](https://pypi.org/project/pysimplegui/) tkinter
[![PyPI Version](https://img.shields.io/pypi/v/pysimpleguiqt.svg?style=for-the-badge)](https://pypi.org/project/pysimpleguiqt/) Qt
[![PyPI Version](https://img.shields.io/pypi/v/pysimpleguiweb.svg?style=for-the-badge)](https://pypi.org/project/pysimpleguiweb/) Web
[![PyPI Version](https://img.shields.io/pypi/v/pysimpleguiwx.svg?style=for-the-badge)](https://pypi.org/project/pysimpleguiwx/) Wx
![GitHub issues](https://img.shields.io/github/issues-raw/PySimpleGUI/PySimpleGUI?color=blue)  ![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/PySimpleGUI/PySimpleGUI?color=blue)
[![Commit activity](https://img.shields.io/github/commit-activity/m/PySimpleGUI/PySimpleGUI.svg?style=for-the-badge)](../../commits/master)
[![Last commit](https://img.shields.io/github/last-commit/PySimpleGUI/PySimpleGUI.svg?style=for-the-badge)](../../commits/master)



# PySimpleGUI User's Manual


## Python GUI For Humans - Transforms tkinter, Qt, Remi, WxPython into portable people-friendly Pythonic interfaces

### This manual is crammed full of answers so start your search for answers here. Read/Search this prior to opening an Issue on GitHub.  Press Control F and type.
---

# Jump-Start

## Install

```
pip install pysimplegui
or
pip3 install pysimplegui
```

### This Code

```python
import PySimpleGUI as sg

sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event in (None, 'Cancel'):	# if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
```

### Makes This Window

and returns the value input as well as the button clicked.

![image](https://user-images.githubusercontent.com/46163555/68713283-7cb38200-056b-11ea-990a-aa1603af5a11.png)



### Any Questions?  It's that simple.

---


#### Looking for a GUI package?     Are you....

* looking to take your Python code from the world of command lines and into the convenience of a GUI? 
* sitting on a Raspberry **Pi** with a touchscreen that's going to waste because you don't have the time to learn a GUI SDK?
* into Machine Learning and are sick of the command line?
* an IT guy/gal that has written some cool tools but due to corporate policies are unable to share unless an EXE file?
* want to share your program with your friends or families (that aren't so freakish that they have Python running)
* wanting to run a program in your system tray?
* a teacher wanting to teach your students how to program using a GUI?
* a student that wants to put a GUI onto your project that will blow away your teacher?
* looking for a GUI package that is "supported" and is being constantly developed to improve it?
* longing for documentation and scores of examples?

**Look no further, you've found your GUI package**.

#### The basics

* Create windows that look and operate _identically_ to those created directly with tkinter, Qt, WxPython, and Remi.
* Requires 1/2 to 1/10th the amount of code as underlying frameworks.
* One afternoon is all that is required to learn the PySimpleGUI package _and_ write your first custom GUI.
* Students can begin using within their first week of Python education.
* No callback functions. You do not need to write the word `class` _anywhere_ in your code.
* Access to nearly every underlying GUI Framework's Widgets.
* Supports both Python 2.7 & 3 when using tkinter
* Supports both PySide2 and PyQt5 (limited support)
* Effortlessly move across tkinter, Qt, WxPython, and the Web (Remi) by changing only the import statement
* The *only* way to write both desktop and web based GUIs at the same time in Python
* Developed from nothing as a pure Python impelementation with Python friendly interfaces.
* Run your program in the System Tray using WxPython. Or, change the import and run it on Qt with no other changes.
* Works with Qt Designer
* Built in Debugger
* Actively maintained and enhanced - 4 ports are underway, all being used by users.
* Corporate as well as home users.
* Appealing to both newcomers to Python and experiened Pythonistas. 
* The focus is entirely on the developer (you) and making their life easier, simplified, and in control.
* 170+ Demo Programs teach you how to integrate with many popular packages like OpenCV, Matplotlib, PyGame, etc. 
* 200 pages of documentation, a Cookbook, built-in help using docstrings, in short it's heavily documented

#### July-2019 Note - This readme is being generated from the PySimpleGUI.py file located on GitHub.  As a result, some of the calls or parameters may not match the PySimpleGUI that you pip installed.

## GUI Development does not have to be difficult nor painful.  It can be (and is) FUN

#### What users are saying about PySimpleGUI

***(None of these comments were solicited & are not paid endorsements - other than a huge thank you they received!)***

"I've been working to learn PyQT for the past week in my off time as an intro to GUI design and how to apply it to my existing scripts... Took me ~30 minutes to figure out PySimpleGUI and get my scripts working with a GUI."

"Python has been an absolute nightmare for me and I've avoided it like the plague.  Until I saw PysimpleGUI."

"I've been pretty amazed at how much more intuitive it is than raw tk/qt. The dude developing it is super active on the project too so if you come across situations that you just can't get the code to do what you want you can make bug/enhancement issues that are almost assured to get a meaningful response."

"This library is the easiest way of gui programming in python! I'm totally in love with it"

"Wow that readme is extensive and great." (hear the love for docs often)

"Coming from R, Python is absolutely slick for GUIs. PySimpleGUI is a dream."

"I have been writing Python programs for about 4 or 5 months now. Up until this week I never had luck with any UI libraries like Tkinter, Qt, Kivy.  I went from not even being able to load a window in Tkinter reliably to making a loading screen, and full program in one night with PySimpleGUI."

"I love PySimpleGUI! I've been teaching it in my Python classes instead of Tkinter."

"I wish PySimpleGUI was available for every friggin programming language"


### START HERE - User Manual with Table of Contents

[ReadTheDocs](http://www.PySimpleGUI.org)  <------ THE best place to read the docs due to TOC, all docs in 1 place, and better formatting. START here in your education.  Easy to remember PySimpleGUI.org.

#### Quick Links To Help and The Latest News and Releases


[Homepage - Lastest Readme and Code - GitHub](http://www.PySimpleGUI.com)  Easy to remember: PySimpleGUI.com

[Announcements of Latest Developments, Release news, Misc](https://github.com/PySimpleGUI/PySimpleGUI/issues/142)

[COOKBOOK!](http://Cookbook.PySimpleGUI.org)

[Trinket an online Cookbook](http://Trinket.PySimpleGUI.org)

[Brief Tutorial](http://Tutorial.PySimpleGUI.org)

[Latest Demos and Master Branch on GitHub](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/DemoPrograms)

[Repl.it Home for PySimpleGUI](https://repl.it/@PySimpleGUI)

[Lots of screenshots](https://www.bountysource.com/issues/60766522-screen-shots)

[How to submit an Issue](https://github.com/PySimpleGUI/PySimpleGUI/issues/1646)


The YouTube videos - If you like instructional videos, there are over 15 videos made by PySimpleGUI project
- [5 part series of basics](https://www.youtube.com/playlist?list=PLl8dD0doyrvHMoJGTdMtgLuHymaqJVjzt)
- [10 part series of more detail](https://www.youtube.com/playlist?list=PLl8dD0doyrvGyXjORNvirTIZxKopJr8s0)
- [The Naked Truth (An updaate on the technology)](https://youtu.be/BFTxBmihsUY)
- There are numerous short videos also on that channel that demonstrate PySimpleGUI being used

YouTube Videos made by others.  These have much higher production values than the above videos.

- A ***fantastic*** tutorial [PySimpleGUI Concepts - Video 1](https://youtu.be/cLcfLm_GgiM)
- Build a calculator [Python Calculator with GUI | PySimpleGUI | Texas Instruments DataMath II](https://youtu.be/x5LSTDdffFk)
- Notepad [Notepad in Python - PySimpleGUI](https://youtu.be/JQY641uynKo)
- File Search Engine [File Search Engine | Project for Python Portfolio with GUI | PySimpleGUI](https://youtu.be/IWDC9vcBIFQ)

# About The PySimpleGUI Documentation System

This User's Manual (also the project's readme) is one ***vital*** part of the PySimpleGUI programming environment.  

If you are a professional or skilled in how to develop software, then you understand the role of documentation in the world of technology development.  You can skip this bit.... look for the bold "**GO TO HERE**" below.

RTFM is not a new acronym. It stretches back to 1979, the dawn of the computer-era and in particular the microprocessor.  The point is that this is not a new problem.  It's a very old problem.

Bluntness is required here as the subtle approach has not worked in the past:

***It WILL be required, at times, for you to read or search this document in order to be successful.***

Re-read that statement.  This **will** be a serious problem for you if you're the type of person that finds it "quicker and easier to post on StackOverflow rather than reading documentation".  

If you have not yet matured to the point you are able to understand this skill or choose to not follow it, then please save ***everyone*** the pain of doing **for you** what you, as a developer, software engineer, or wanna be coder, must do on your own.  It's a vital skill for you to learn.  

Want to be a "real engineer"? Then follow "real engineering practices" such as "reading".  You are learning a NEW GUI package.  You've not seen anything like it.  Don't be so arrogant as to believe you will never need to read documentation.

UGH, why does this need to be said?

***GO TO HERE*** if instructed above.

I appologize to the other 95% of you that this..... pathetic.... reminder needs to be added, but sadly there's a need for it.

There are 5 resources that work together to provide to you the fastest path to success.  They are:

1. This User's Manual
2. The Cookbook
3. The 170+ Demo Programs
4. Docstrings enable you to access help directly from Python or your IDE
5. Searching the GitHub Issues as a last resort (search both open and closed issues)

Pace yourself.  The intial progress is exciting and FAST PACED.  However, GUIs take time and thought to build.  Take a deep breath and use the provided materials and you'll do fine.  Don't skip the design phase of your GUI after you run some demos and get the hang of things.  If you've tried other GUI frameworks before, successful or not, then you know you're already way ahead of the game using PySimpleGUI versus the underlying GUI frameworks.  It may feel like the 3 days you've been working on your code has been forever, but by comparison of 3 days learning Qt, PySimpleGUI will look trivial to learn.

It is not by accident that this section, about documentation, is at the TOP of this document.

This documentation is not HUGE in length for a package this size. In fact it's still one document and it's the readme for the GitHub.  It's not written in complex english.  It is understandable by complete beginners.  And pressing `Control+F` is all you need to do to search this document.  USUALLY you'll find less than 6 matches.

## Documentation and Demos Get Out of Date

Sometimes the documenation doesn't match exactly the version of the code you're running.  Sometimes demo programs haven't been updated to match a change made to the SDK.  Things don't happen simultaneously generally speaking.  So, it may very well be that you find an error or inconsistency or something no longer works with the latest version of an external library.

If you've found one of these problems, and you've searched to make sure it's not a simple mistake on your part, then by ALL means log an Issue on the GitHub.  Don't be afraid to report problems if you've taken the simple steps of checking out the docs first.


# Platforms

## Hardware and OS Support

PySimpleGUI runs on Windows, Linux and Mac, just like tkinter, Qt, WxPython and Remi do.  If you can get the underlying GUI Framework installed / running on your machine then PySimpleGUI will also run there.

### Hardware

* PC's, Desktop, Laptops
* Macs of all types
* Raspberry Pi
* Android devices like phones and tablets
* Virtual machine online (no hardware) - repl.it

### OS

* Windows 7, 8, 10
* Linux on PC - Tested on several distributions
* Linux on Raspbnerry Pi
* Linux on Android - Can use either Termux or PyDroid3
* Mac OS


#### Python versions

As of 9/25/2018 **both Python 3 and Python 2.7 are supported** when using **tkinter version** of PySimpleGUI! The Python 3 version is named `PySimpleGUI`. The Python 2.7 version is `PySimpleGUI27`.  They are installed separately and the imports are different. See instructions in Installation section for more info.  **None** of the other ports can use Python 2.

###### Python 2.7 Code will be deleted from this GitHub on Dec 31, 2019

Note that the 2.7 port will *cease to exist on this GitHub* on Jan 1, 2020.  If you would like to know how much time you have to move over to the Python 3 version of PySimpleGUI, then go here: https://pythonclock.org/.  The only thing that will be available is an unsupported PyPI release of PySimpleGUI27.

By "will cease to exist on this GitHub" I mean, it will be deleted entirely.  No source code, no supporting programs.  Nothing.  If you're stuck using 2.7 in December, it would behoove you to fork the 2.7 code on Dec 31, 2019.  Legacy Python doesn't have a permanent home here.  It sounds cruel, but experts in security particularly says 2.7 is a huge risk. Furthering it use only hurts the computing world.

#### Warning - tkinter + Python 3.7.3 and later, including 3.8 has problems

The version of tkinter that is being supplied with the 3.7.3 and later versions of Python is known to have a problem with table colors.  Basically, they don't work.  As a result, if you want to use the plain PySimpleGUI running on tkinter, you should be using 3.7.2 or less.  3.6 is the version PySimpleGUI has chosen as the recommended version for most users.

## Output Devices

In addition to running as a desktop GUI, you can also run your GUI in a web browser by running PySimpleGUIWeb. 

This is ideal for "headless" setups like a Raspberry Pi that is at the core of a robot or other design that does not have a normal display screen.  For these devices, run a PySimpleGUIWeb program that never exits.  

Then connect to your application by going to the Pi's IP address (and port #) using a browser and you'll be in communication with your application.  You can use it to make configuration changes or even control a robot or other piece of hardward using buttons in your GUI

## A Complete PySimpleGUI Program (Getting The Gist)

Before diving into details, here's a description of what PySimpleGUI is/does and why that is so powerful.

You keep hearing "custom window" in this document because that's what you're making and using... your own custom windows.

**ELEMENTS** is a word you'll see everywhere... in the code, documentation, ... Elements == PySimpleGUI's Widgets.  As to not confuse a tkinter Button Widget with a PySimpleGUI Button Element, it was decided that PySimpleGUI's Widgets will be called Elements to avoid confusion.

Wouldn't it be nice if a GUI with 3 "rows" of Elements was defined in 3 lines of code?  That's exactly how it's done.  Each row of Elements is a list.  Put all those lists together and you've got a window.

What about handling button clicks and stuff.  That's 4 lines of the code below beginning with the while loop.  

Now look at the `layout` variable and then look at the window graphic below.  Defining a window is taking a design you can see visually and then visually creating it in code.  One row of Elements = 1 line of code (can span more if your window is crowded).  The window is exactly what we see in the code.  A line of text, a line of text and an input area, and finally ok and cancel buttons.

This makes the coding process extremely quick and the amount of code very small

```python
import PySimpleGUI as sg
sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events"
while True:             
    event, values = window.read()
    if event in (None, 'Cancel'):
        break

window.close()
```

![image](https://user-images.githubusercontent.com/46163555/68713283-7cb38200-056b-11ea-990a-aa1603af5a11.png)



You gotta admit that the code above is a lot more "fun" looking that tkinter code you've studied before.  Adding stuff to your GUI is ***trivial***.  You can clearly see the "mapping" of those 3 lines of code to specific Elements laid out in a Window.   It's not a trick.  It's how easy it is to code in PySimpleGUI.  With this simple concept comes the ability to create any window layout you wish.  There are parameters to move elements around inside the window should you need more control.

It's a thrill to complete your GUI project way ahead of what you estimated.  Some people take that extra time to polish their GUI to make it even nicer, adding more bells and whistles because it's so easy and it's a lot of fun to see success after success as you write your program.

Some are more advanced users and push the boundaries out and extend PySimpleGUI using their own extensions.

Others, like IT people and hackers are busily cranking out GUI program after GUI program, and creating tools that others can use.  Finally there's an easy way to throw a GUI onto your program and give it to someone.  It's a pretty big leap in capability for some people.  It's GREAT to hear these successes.  It's motivating for everyone in the end.  Your success can easily motivate the next person to give it a try and also potentially be successful.

Usually there's a one to one mapping of a PySimpleGUI Element to a GUI Widget. A "Text Element" in PySimpleGUI == "Label Widget" in tkinter.  What remains constant for you across all PySimpleGUI platforms is that no matter what the underlying GUI framework calls the thing that places text in your window, you'll always use the PySimpleGUI Text Element to access it.

### The final bit of magic is in how Elements are created and changed.  

So far you've seen simply layouts with no customization of the Elements.  Customizing and configuring Elements is another place PySimpleGUI utilizes the Python language to make your life easier.  

What about Elements that have settings other than the standard system settings?   What if I want my Text to be blue, with a Courier font on a green background.  It's written quite simply:

```python
Text('This is some text', font='Courier 12', text_color='blue', background_color='green')
```

The Python named parameters are ***extensively*** in PySimpleGUI. They are key in making the code compact, readable, and trivial to write.

As you'll learn in later sections that discuss the parameters to the Elements, there are a LOT of options avilable to you should you choose to use them.  The `Text Element` has 15 parameters that you can change.  This is one reason why PyCharm is suggested as your IDE... it does a fantastic job of displaying documentation as you type in your code.


### That's *The* *Basics*

What do you think?  Easier so far than your previous run-ins with GUIs in Python?  Some programs, many in fact, are as simple as this example has been.

But PySimpleGUI certainly does **not** end here.  This is the beginning. The scaffolding you'll build upon.


## The Underlying GUI Frameworks & Status of Each

At the moment there are 4 acitvely developed and maintained "ports" of PySimpleGUI.  These include:

1. tkinter - Fully complete
2. Qt using Pyside2 - Alpha stage.  Not all features for all Elements are done
3. WxPython - Development stage, pre-releaser.  Not all Elements are done. Some known problems with multiple windows
4. Remi (Web browser support) - Development stage, pre-release.


While PySimpleGUI, the tkinter port, is the only 100% completed version of PySimpleGUI, the other 3 ports have a LOT of functionality in them and are in active use by a large portion of the installations.  You can see the number of Pip installs at the very top of this document to get a comparison as to the size of the install base for each port.  The "badges" are right after the logo.


# The PySimpleGUI "Family"

## What's The Big Deal? What is it?

PySimpleGUI wraps tkinter, Qt, WxPython and Remi so that you get all the same widgets, but you interact with them in a more friendly way that's common across the ports. 

What does a wrapper do (Yo! PSG in the house!)?  It does the layout, boilerplate code, creates and manages the GUI Widgets for you and presents you with a **simple, efficient interface.**   Most importantly, it maps the Widgets in tkinter/Qt/Wx/Remi into PySimpleGUI Elements.  Finally, it replaces the GUIs' event loop with one of our own.  

You've seen examples of the code already.  The big deal of all this is that anyone can create a GUI simply and quickly that matches GUIs written in the native GUI framework.  You can create complex layouts with complex element interactions.  And, that code you wrote to run on tkinter will also run on Qt by changing your import statement.

If you want a deeper explanation about the [architecture of PySimpleGUI](https://pysimplegui.readthedocs.io/en/latest/architecture/), you'll find it on ReadTheDocs in the same document as the Readme & Cookbook. There is a tab at the top with labels for each document.

## The "Ports"

There are distinct ports happening as mentioned above.  Each have their own location on GitHub under the main project.  They have their own Readme with is an *augmentation* of this document... they are meant to be used together.

PySimpleGUI is released on PyPI as 5 distinct packages.
1. PySimpleGUI - tkinter version
2. PySimpleGUI27 - tkinter version that runs on 2.7
3. PySimpleGUIWx - WxPython version
4. PySimpleGUIQt - PySided2 version
5. PySimpleGUIWeb - The web (Remi) version

You will need to install them separately

There is also an accompanying debugger known as `imwatchingyou`.  If you are running the tkinter version of PySimpleGUI, you will not need to install the debugger as there is a version embedded directly into PySimpleGUI.

## Qt Version


Qt was the second port after tkinter.  It is the 2nd most complete with the original PySimpleGUI (tkinter) being the most complete and is likely to continue to be the front-runner.  All of the Elements are available on PySimpleGUIQt.

As mentioned previously each port has an area.  For Qt, you can learn more on the [PySimpleGUIQt GitHub site](https://github.com/MikeTheWatchGuy/PySimpleGUI/tree/master/PySimpleGUIQt).  **There is a separate Readme file for the Qt version** that you'll find there.  This is true for all of the PySimpleGUI ports.

Give it a shot if you're looking for something a bit more "modern".  PySimpleGUIQt is currently in **Alpha**.  *All of the widgets are operational but some may not yet be full-featured.*  If one is missing and your project needs it, log an Issue.  It's how new features are born.

Here is a summary of the Qt Elements with no real effort spent on design clearly.  It's an example of the "test harness" that is a part of each port. If you run the PySimpleGUI.py file itself then you'll see one of these tests.

As you can see, you've got a full array of GUI Elements to work with.  All the standard ones are there in a single window.  So don't be fooled into thinking PySimpleGUIQt is barely working or doesn't have many widgets to choose from.  You even get TWO "Bonus Elements" - `Dial` and `Stretch`


## WxPython Version

[PySimpleGUIWx GitHub site](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWx).  **There is a separate Readme file for the WxPython version**.

Started in late December 2018 PySimpleGUIWx started with the SystemTray Icon feature.    This enabled the package to have one fully functioning feature that can be used along with tkinter to provide a complete program.    The System Tray feature is complete and working very well.  It was used not long ago in a corporate setting and has been performing with few problems reported.

The Windowing code was coming together with Reads operational.  The elements were getting completed on a regular basis. But I ran into multiwindow problems.  And it was at about this time that Remi was suggested as a port.

Remi (the "web port") overnight lept the WxPython effort and Web became a #1 priority and continues to be.  The thought is that the desktop was well represented with PySimpleGUI, PySimpleGUIQt, and PySimpleGUIWx.  Between those ports is a solid winowing system and 2 system tray implementations and a nearly feature complete Qt effort.  So, the team was switched over to PySimpleGUIWeb.

## Web Version (Remi)

[PySimpleGUIWeb GitHub site](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb).  **There is a separate Readme file for the Web version**.

New for 2019, PySimpleGUIWeb.  This is an exciting development!  PySimpleGUI in your Web Browser!

The underlying framework supplying the web capability is the Python package Remi.  https://github.com/dddomodossola/remi  Remi provides the widgets as well as a web server for you to connect to.  It's an exiting new platform to be running on and has temporarily bumped the WxPython port from the highest priority.  PySimpleGUIWeb is the current high priority project.

**Use this solution for your Pi projects** that don't have anything connected in terms of input devices or display.  Run your Pi in "headless" mode and then access it via the Web interface.  This allows you to easily access and make changes to your Pi without having to hook up anything to it.

****It's not meant to "serve up web pages"****

PySimpleGUIWeb is first and foremost a **GUI**, a program's front-end. It is designed to have a single user connect and interact with the **GUI**.

If more than 1 person connects at a time, then both users will see the exact same stuff and will be interacting with the program as if a single user was using it.

## Android Version

PySimpleGUI runs on Android devices with the help of either the PyDroid3 app or the Termux app.  Both are capable of running tkinter programs which means both are capable of running PySimpleGUI.

To use with PyDroid3 you will need to add this import to the top of all of your PySimpleGUI program files:

```python
import tkinter
```

This evidently triggers PyDroid3 that the application is going to need to use the GUI.

You will also want to create your windows with the `location` parameter set to `(0,0)`.

Here's a quick demo that uses OpenCV2 to display your webcam in a window that runs on PyDroid3:

```python
import tkinter
import cv2, PySimpleGUI as sg
USE_CAMERA = 0      # change to 1 for front facing camera
window, cap = sg.Window('Demo Application - OpenCV Integration', [[sg.Image(filename='', key='image')], ], location=(0, 0), grab_anywhere=True), cv2.VideoCapture(USE_CAMERA)
while window(timeout=20)[0] is not None:
    window['image'](data=cv2.imencode('.png', cap.read()[1])[1].tobytes())
```

You will need to pip install opencv-python as well as PySimpleGUI to run this program.

Also, you must be using the Premium, yes paid, version of PyDroid3 in order to run OpenCV.  The cost is CHEAP when compared to the rest of things in life.  A movie ticket will cost you more.  Which is more fun, seeing **your Python program** running on your phone and using your phone's camera, or some random movie currently playing?  From experience, the Python choice is a winner.  If you're cheap, well, then you won't get to use OpenCV. No, there is no secret commercial pact between the PySimpleGUI project and the PyDroid3 app team.  


## Source code compatibility

In theory, your source code is completely portable from one platform to another by simply changing the import statement.  That's the GOAL and suprisingly many times this 1-line change works.  Seeing your code run on tkinter, then change the import to `import  PySimpleGUIWeb as sg` and instead of a tkinter window, up pops your default browser with your window running on it is an incredible feeling.

But, ***caution is advised.***  As you've read already, some ports are further along than others.  That means when you move from one port to another, some features may not work.  There also may be some alignment tweaks if you have an application that precisely aligns Elements.

What does this mean, assuming it works?  It means it takes a trivial amount of effort to move across GUI Frameworks.  Don't like the way your GUI looks on tkinter?  No problem, change over to try PySimpleGUIQt.  Made a nice desktop app but want to bring it to the web too?  Again, no problem, use PySimpleGUIWeb.

## repl.it Version

***Want to really get your mind blown?***  Check out this [PySimpleGUI program](https://repl.it/@PySimpleGUI/PySimpleGUIWeb-Demos) running in your web browser.

Thanks to the magic of repl.it and Remi it's possible to run PySimpleGUI code in a browser window without having Python running on your computer.  This should be viewed as a teaching and demonstration aid.  It is not meant to be a way of serving up web pages. It wouldn't work any way as each user forks and gets their own, completely different, workspace.

There are 2 ports of PySimpleGUI that run on repl.it - PySimpleGUI and PySimpleGUIWeb.

### PySimpleGUI (tkinter based)

The primary PySimpleGUI port works very well on repl.it due to the fact they've done an outstanding job getting tkinter to run on these virtual machines.  Creating a program from scratch, you will want to choose the "Python with tkinter" project type.

The virtual screen size for the rendered windows isn't very large, so be mindful of your window's size or else you may end up with buttons you can't get to.

You may have to "install" the PySimpleGUI package for your project.  If it doesn't automatically install it for you, then click on the cube along the left edge of the browser window and then type in PySimpleGUI or PySimpleGUIWeb depending on which you're using.

### PySimpleGUIWeb (Remi based)

For PySimpleGUIWeb programs you run using repl.it will automatically download and install the latest PySimpleGUIWeb from PyPI onto a virtual Python environment.  All that is required is to type `import PySimpleGUIWeb` you'll have a Python environment up and running with the latest PyPI release of PySimpleGUIWeb.

### Creating a repl.it project from scratch / troubleshooting

To create your own repl.it PySimpleGUI project from scratch, first choose the type of Python virtual machine you want.  For PySimpleGUI programs, choose the "Python with tkinter" project type.  For PySimpleGUIWeb, choose the normal Python project.

There have been times where repl.it didn't do the auto import thing.  If that doesn't work for some reason, you can install packages by clicking on the package button on the left side of the interface, typing in the package name (PySimpleGUI or PySimpleGUIWeb) and install it. 

### Why this is so cool (listen up Teachers, tutorial writers)

***Educators*** in particular should be interested.  Students can not only post their homework easily for their teacher to access, but teachers can also run the students programs online.  No downloading needed.  Run it and check the results.

For people wanting to share their code, especially when helping someone with a problem, it's a great place to do it.  Those wishing to see your work do not have to be running Python nor have PySimpleGUI installed.

The way I use it is to first write my PySimpleGUI code on Windows, then copy and paste it into Repl.it.

Finally, you can embed these Repl.it windows into web pages, forum posts, etc.  The "Share" button is capable of giving you the block of code for an "iframe" that will render into a working repl.it program in your page.  It's amazing to see, but it can be slow to load.

### Repl.it is NOT a web server for you to "deploy" applications!

Repl.it is not meant to serve up applications and web pages.  Trying to use it that way will not ressult in satisfactory results.  It's simply too slow and too technical of an interface for trying to "deploy" using it.  PySimpleGUIWeb isn't a great choice in serving web pages.  It's purpose is more to build a GUI that runs in a browser.


## Macs

It's surprising that Python GUI code is completely cross platform from Windows to Mac to Linux.  No source code changes.  This is true for both  PySimpleGUI and PySimpleGUIQt.

Historicly, PySimpleGUI using tkinter have struggled on Macs.  This was because of a problem setting button colors on the Mac.  However, two events has turned this problem around entirely.

1. Use of ttk Buttons for Macs
2. Ability for Mac users to install Python from python.org rather than the Homebrew version with button problems

It's been a long road for Mac users with many deciding to use PySimpleGUIQt so that multi-colored windows could be made.  It's completely understandable to want to make attractive windows that utilitize colors.  

PySimpleGUI now supports Macs, Linux, and Windows equally well. They all are able to use the "Themes" that automatically add color to your windows.  

Be aware that Macs default to using ttk buttons.  You can override this setting at the Window and Button levels.  If you installed Python from python.org, then it's likely you can use the non-ttk buttons should you wish.



# Support

## Don't Suffer Silently

The GitHub Issues are checked *often*.  Very often.  **Please** post your questions and problems there and there only.  Please don't post on Reddit, Stackoverflow, on forums, until you've tried posting on the GitHub.

Why?  *It will get you the best support possible.*  Second, you'll be helping the project as what you're experiencing might very well be a bug, or even a *known* bug. Why spend hours thrashing, fighting against a known bug?

It's not a super-buggy package, but users do experience problems just the same.  Maybe something's not explained well enough in the docs.  Maybe you're making a common mistake.  Maybe that feature isn't complete yet.

You won't look stupid posting an Issue on GitHub.  It's just the opposite.


### How to log issues

**PySimpleGUI is an active project.**  Bugs are fixed, features are added, often.  Should you run into trouble, **open an issue** on the [GitHub site](http://www.PySimpleGUI.com) and you'll receive help.  Posting questions on StackOverflow, Forums, Mailing lists, Reddit, etc, is not the fastest path to support and taking it may very well lead you astray as folks not familiar with the package struggle to help you. You may also run into the common response of "I don't know PySimpleGUI (and perhaps dislike it as a result), but I know you can do that with Qt".

Why only 1 location?  It's simple.... it's where the bugs, enhancements, etc are tracked.  It's THE spot on the Internet for this project.  There's not driven by a freakish being in control, telling people how to do things, reasoning.  It's so that YOU get the best and quickest support possible.

So, [open an Issue](https://github.com/PySimpleGUI/PySimpleGUI/issues/new/choose), choose "custom form" and fill it out completely.  There are very good reasons behind all of the questions.  Cutting corners only cuts your chances of getting help and getting quality help as it's difficult enough to debug remotely.  Don't handicap people that want to help by not providing enough information.

**Be sure and run your program outside of your IDE** ***first***.  Start your program from the shell using `python` or `python3` command.  On numerous occassions much time was spent chasing problems caused by the IDE.  By running from a command line, you take that whole question out of the problem, an important step.

***Don't sit and stew, trying the same thing over and over***, until you hate life... stop, and post an Issue on the GitHub.  Someone **WILL** answer you.  Support is included in the purchase price for this package (the quality level matches the price as well I'm afraid).  Just don't be too upset when your free support turns out to be a little bit crappy, but it's free and typically good advice.


### Target Audience

PySimpleGUI is trying to serve the 80% of GUI *problems*. The other 20% go straight to tkinter, Qt, WxPython, Remi, or whatever fills that need.  That 80% is **a huge problem space**.  

***The "Simple" of PySimpleGUI describes how easy it is to use, not the nature of the problem space it solves.***  Note that people are not part of that description.  It's not trying to solve GUI problems for 80% of the people trying it.  PySimpleGUI tries to solve 80% of GUI ***problems***, regardless of the programmer's experience level.

Is file I/O in Python limited to only certain people?  Is starting a thread, building a multi-threaded Python program incredibly difficult such that it takes a year to learn?  No.  It's quite easy.  Like most things Python, you import the object from package and you use it.  It is 2 lines of Python code to create and start a thread.

Why can't it be 2 lines of code to show a GUI window?  What's SO special about the Python GUI libraries that they require you to follow a specific Object Oriented model of development?  Other parts and packages of Python don't tend to do that.  

The reason is because they didn't originate in Python. They are strangers in a strange land and they had to be "adapted".  They started as C++ programs / SDKs, and remain that way too.  There's a vaneer of Python slapped onto the top of them, but that sure didn't make them fit the language as well as they could have.

PySimpleGUI is designed with both the beginner and the experienceed developer in mind.  Why?  Because both tend to like compact code.  Most like people, we just want to get sh\*t done, right?  And, why not do it in a way that's like how most of Python works?

The beginners can begin working with GUIs ***in their first week of Python education***.  The professionals can jump right into the deep end of the pool to use the entire array of Elements and their capabilities to build stuff like a database application.

Here's a good example of how PySimpleGUI serves these 2 groups.... the `InputText` Element has 16 potential parameters, yet you'll find 0 or 1 parameters set by beginners. Look at the examples throughout this document and you'll see the code fragments utilize a tiny fraction of the potential parameters / settings.  Simple... **keep it simple for the default case**.  This is part of the PySimpleGUI mission.  

Some developers are heavily wedded to the existing GUI Framework Architectures (Qt, WxPyton, tkinter).  They like the existing GUI architectures (they're all roughly the same, except this one).  If you're in that crowd, join the "20% Club" just down the street.  There's plenty of room there with plenty of possible solutions.

But how about a quick stop-in for some open mindedness exercises.  Maybe you will come up with an interesting suggestion even if you don't use it.  Or maybe PySimpleGUI does something that inspires you to write something similar directly in Qt.  And please, at least be civil about it.  There is room for multiple architectures.  Remember, you will not be *harmed* by writing some PySimpleGUI code just like you won't by writing some tkinter or Qt code.  Your chances of feeling harmed is more likely from one of those 2.

#### Beginners & Easier Programs

There are a couple of reasons beginners stop in for a look.  The first is to simply throw a simple GUI onto the front of an existing command line application.  Or maybe you need to popup a box to get a filename.  These can often be simple 1-line `Popup` calls.  Of course, you don't have to be a beginner to add a GUI onto one of your existing command line programs.  Don't feel like because you're an advanced programmer, you need to have an advanced solution.

If you have a more intricate, complete, perhaps multi-window design in mind, then PySimpleGUI still could be your best choice.

This package is not only great to use as your first GUI package, but it also teaches how to design and utilize a GUI. It does it better than the existing GUIs by removing the syntax, and lengthy code that can take an otherwise very simple appearing program into something that's completely unrecognizable.  With PySimpleGUI your 'layout' is all you need to examine to see the different GUI Elements that are being used.

Why does PySimpleGUI make it any easier to learn about GUIs?  Because it removes the classes, callback functions, object oriented design to better get out of your way and let you focus entirely on your GUI and not how to represent it in code.  

The result is 1/2 to 1/10 th the amount of code that implements the exact same layout and widgets as you would get from coding yourself directly in Qt5.  It's been tested many times... again and again, PySimpleGUI produces significantly less code than Qt and the frameworks it runs on.

Forget syntax completely and just look on the overall activities of a PySimpleGUI programmer.  You have to design your window.... determine your inputs and your outputs, place buttons in strategic places, create menus, .... You'll be busy just doing all those things to design and define your GUI completely independent upon the underlying framework. 

After you get all those design things done and are ready to build your GUI, it's then that you face the task of learning a GUI SDK.  Why not start with the easy one that gives you many successes?  You're JUST getting ***started***, so cut yourself a break and use PySimpleGUI so that you can quickly get the job done and move on to the next GUI challenge.

#### Advanced Programmers, Sharp Old-Timers, Code Slingers and Code Jockeys

It's not perfect, but PySimpleGUI is an amazing bit of technology.  It's the programmer, the computer scientist, that has experience working with GUIs in the past that will recognize the power of this simple architecture.

What I hear from seasoned professionals is that PySimpleGUI saves them a **ton** of time.  They've written GUI code before.  They know how to lay out a window.  These folks just want to get their window working and quick.

With the help of IDE's like PyCharm, Visual Studio and Wing (the offically supported IDE list) you get instant documentation on the calls you are making.  On PyCharm you instantly see both the call signature but also the explanations about each parameter.

If the screenshots, demo programs and documentation don't convince you to at least **give it a try, once**, then you're way too busy, or .....  I dunno, I stopped guessing "why?" some time ago.  

Some of the most reluctant of people to try PySimpleGUI have turned out to be some of the biggest supporters.

#### A Moment of Thanks To The PySimpleGUI Users

I want to thank the early users of PySimpleGUI that started in 2018.  Your suggestions helped shape the package and have kept it moving forward at a fast pace.

For all the users, while I can't tell you the count of the number of times someone has said "thank you for PySimpleGUI" as part of logging and Issue, or a private message or email, but I can tell you that it's been significant.

***EVERY one of those "thank you" phrases, no matter how small you may think it is, helps tremendously.***

Sometimes it's what gets me past a problem or gets me to write yet more documentation to try and help people understand quicker and better.  Let's just say the effect is always positive and often significant.

PySimpleGUI users have been super-nice.  I doubt all Open Source Projects are this way, but I could be wrong and every GitHub repository has awesome users.  If so, that's even more awesome!

**THANK YOU PySimpleGUI USERS!**

-------------------


# Learning Resources

***This document.... you must be willing to read this document if you expect to learn and use PySimpleGUI.*** 

If you're unwilling to even try to figure out how to do something or find a solution to a problem and have determined it's "easier to post a question first than to look at the docs", then this is not the GUI package for you.  *If you're unwilling to help yourself, then don't expect someone else to try first.*  You need to hold up your end of the bargain by at least doing some searches of this document.

While PySimpleGUI enables you to write code easily, it doesn't mean that it magically fills your head with knowledge on how to use it.  The built-in docstrings help, but they can only go so far.  

***Searching this document is as easy as pressing Control + F.***

This document is on the GitHub homepage, as the readme. http://www.PySimpleGUI.com will get you there.  If you prefer a version with a Table of Contents on the left edge then you want to go to http://www.PySimpleGUI.org .  

## The PySimpleGUI, Developer-Centric Model

You may think that you're being fed a line about all these claims that PySimpleGUI is built specifically to make your life easier and a lot more fun than the alternatives.... especially after reading the bit above about reading this manual.

### Psychological Warfare

Brainwashed. Know that there is an active campaign to get you to be successful using PySimpleGUI.  The "Hook" to draw you in and keep you working on your program until you're satisfied is to work on the dopamine in your brain. Yes, your a PySimpleGUI rat, pressing on that bar that drops a food pellet reward in the form of a working program.

The way this works is to give you success after success, with very short intervals between.  For this to work, what you're doing must work.  The code you run must work.  Make small changes to your program and run it over and over and over instead of trying to do one big massive set of changes.  Turn one knob at a time and you'll be fine.

Find the keyboard shortcut for your IDE to run the currently shown program so that running the code requires 1 keystroke.  On PyCharm, the key to run what you see is Control + Shift + F10.  That's a lot to hold down at once.  I programmed a hotkey on my keyboard so that it emits that combination of keys when I press it.  Result is a single button to run.

### Tools

These tools were created to help you achieve a steady stream of these little successses.

* This readme and its example pieces of code
* The Cookbook - Copy, paste, run, success
* Demo Programs - Copy these small programs to give yourself an instant headstart
* Documentation shown in your IDE (docstrings) means you do not need to open any document to get the full assortment of options available to you for each Element & function call


The initial "get up and running" portion of PySimpleGUI should take you less than 5 minutes.  The goal is 5 minutes from your decision "I'll give it a try" to having your first window up on the screen "Oh wow, it was that easy?!"

The primary learning pathes for PySimpleGUI are:

* This readme document over 100 pages of PySimpleGUI User Manual 
	* http://www.PySimpleGUI.org
* The Cookbook - Recipes to get you going and quick
	* http://Cookbook.PySimpleGUI.org
* The Demo Programs - Start hacking on one of these running soluitions
	* http://www.PySimpleGUI.com
* The YouTube videos - If you like instructional videos, there are 15+ videos
	* [5 part series of basics](https://www.youtube.com/playlist?list=PLl8dD0doyrvHMoJGTdMtgLuHymaqJVjzt)
	* [10 part series of more detail](https://www.youtube.com/playlist?list=PLl8dD0doyrvGyXjORNvirTIZxKopJr8s0)

Everything is geared towards giving you a "quick start" whether that be a Recipe or a Demo Program.  The idea is to give you something running and let you hack away at it.  As a developer this saves tremendous amounts of time.

You **start** with a working program, a GUI on the screen.  Then have at it.  If you break something (`"a happy little accident"` as Bob Ross put it), then you can always backtrack a little to a known working point.

A high percentage of users report both learning PySimpleGUI and completing their project in a single day.
 
This isn't a rare event and it's not bragging.  GUI programming doesn't HAVE to be difficult by definition and PySimpleGUI has certainly made it much much more approachable and easier (not to mention simpler).

But, you need to look at this document when pushing into new, unknown territory.  Don't guess... or more specifically, don't guess and then give up when it doesn't work.

## This Readme and Cookbook

The readme and Cookbook, etc are best viewed on ReadTheDocs.  The quickest way there is to visit:
http://www.PySimpleGUI.org

You will be auto-forwarded to the right destination.  There are multiple tabs on ReadTheDocs.  One for the main readme and one for the Cookbook.  There are other documents there like an architectural design doc.

The Cookbook has approx 27 "Recipes" or short programs that can be easily copied and pasted.

## Demo Programs

The GitHub repo has the Demo Programs.  There are ones built for plain PySimpleGUI that are usually portrable to other versions of PySimpleGUI.  And there are some that are associated with one of the other ports.  The easiest way to the GitHub:

http://www.PySimpleGUI.com

As of this writing, on 2019-07-10 there are 177 Demo Programs for you to choose from.  

These programs demonstrate to you how to use the Elements and especially how to integtate PySimpleGUI with some of the popular open source technologies such as OpenCV, PyGame, PyPlot, and Matplotlib to name a few.

Many Demo Programs that are in the main folder will run on multiple ports of PySimpleGUI.  There are alse port-specific Demo Programs.  You'll find those in the folder with the port.  So, Qt specific Demo Programs are in the PySimpleGUIQt folder.

---

# The Quick Tour

Let's take a super-brief tour around PySimpleGUI before digging into the details.  There are 2 levels of windowing support in PySimpleGUI -  High Level and Customized.

The high-level calls are those that perform a lot of work for you. These are not custom made windows (those are the other way of interacting with PySimpleGUI).

Let's use one of these high level calls, the `Popup` and use it to create our first window, the obligatory "Hello World".  It's a single line of code.  You can use these calls like print statements, adding as many parameters and types as you desire.

```python
import PySimpleGUI as sg

sg.Popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')
```

![hello world](https://user-images.githubusercontent.com/13696193/44960047-1f7f6380-aec6-11e8-9d5e-12ef935bcade.jpg)


Or how about a ***custom GUI*** in 1 line of code?  No kidding this is a valid program and it uses Elements and produce the same Widgets like you normally would in a tkinter program.  It's just been compacted together is all, strictly for demonstration purposes as there's no need to go that extreme in compactness, unless you have a reason to and then you can be thankful it's possible to do.

```python
import PySimpleGUI as sg

event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).read(close=True)
```

![get filename](https://user-images.githubusercontent.com/13696193/44960039-f1018880-aec5-11e8-8a43-3d7f8ff93b67.jpg)


## The Beauty of Simplicity


> One day I will find the right words, and they will be simple.
― Jack Kerouac


That's nice that you can crunch things into 1 line, like in the above example, but it's not readable.  Let's add some whitespace so you can see the **beauty** of the PySimpleGUI code.

Take a moment and look at the code below.  Can you "see" the window looking at the `layout` variable, knowing that each line of code represents a single row of Elements?  There are 3 "rows" of Elements shown in the window and there are 3 lines of code that define it.

Creating and reading the user's inputs for the window occupy the last 2 lines of code, one to create the window, the last line shows the window to the user and gets the input values (what button they clicked, what was input in the Input Element)


```python
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your creations colorful

layout = [	[sg.Text('Filename')],
          	[sg.Input(), sg.FileBrowse()], 
	  		[sg.OK(), sg.Cancel()]] 

window = sg.Window('Get filename example', layout)

event, values = window.read()
window.close()
```

![get filename](https://user-images.githubusercontent.com/13696193/44960039-f1018880-aec5-11e8-8a43-3d7f8ff93b67.jpg)

Unlike other GUI SDKs, you can likely understand every line of code you just read, even though you have not yet read a single instructional line from this document about how you write Elements in a layout.

There are no pesky classes you are *required* to write, no callback functions to worry about.  None of that is required to show a window with some text, an input area and 2 buttons using PySimpleGUI.  

The same code, in tktinter, is 5 times longer and I'm guessing you won't be able to just read it and understand it.  While you were reading through the code, did you notice there are no comments, yet you still were able to understand, using intuition alone.

You will find this theme of Simple everywhere in and around PySimpleGUI.  It's a way of thinking as well as an architecture direction.  Remember, you, Mr./Ms. Developer, are at the center of the package.  So, from your vantage point, of course everything should look and feel simple.

Not only that, it's the Pythonic thing to do.  Have a look at line 3 of the "Zen of Python".

> The Zen of Python, by Tim Peters
>
> Beautiful is better than ugly.
> Explicit is better than implicit.
> Simple is better than complex.
> Complex is better than complicated.
> Flat is better than nested.
> Sparse is better than dense.
> Readability counts.
> Special cases aren't special enough to break the rules.
> Although practicality beats purity.
> Errors should never pass silently.
> Unless explicitly silenced.
> In the face of ambiguity, refuse the temptation to guess.
> There should be one-- and preferably only one --obvious way to do it.
> Although that way may not be obvious at first unless you're Dutch.
> Now is better than never.
> Although never is often better than *right* now.
> If the implementation is hard to explain, it's a bad idea.
> If the implementation is easy to explain, it may be a good idea.
> Namespaces are one honking great idea -- let's do more of those!


I just hope reading all these pages of documentation is going to make you believe that we're breaking suggestion:
> If the implementation is hard to explain, it's a bad idea.
> If the implementation is easy to explain, it may be a good idea.

I don't think PySimpleGUI is ***difficult*** to explain, but I am striving to fully explain it so that you don't do this:

> In the face of ambiguity, refuse the temptation to guess.
 
Sometimes you can guess and be fine.  Other times, things may work, but the side effects are potentially significant.  There may be a much better way to solve a problem - Log an Issue on GitHub!  


------


# Some Examples

## Polishing Your Windows = Building "Beautiful Windows"

And STILL the Zen of Python fits:

> Beautiful is better than ugly.

but this fits too:

> Although practicality beats purity.

Find a balance that works for you.

"But tkinter sucks"
"It looks like the 1990s" (this one is often said by people that were not alive in the 1990s)
"What Python GUI SDK will make my window look beautiful?"  (posted to Reddit at least every 2 weeks)

These windows below were ALL made using PySimpleGUI, the tkinter version and they look good enough to not be simply scoffed at and dismissed.  Remember, developer, you have a rather significant hand in how your application looks and operates.  You certainly cannot pin it all on the GUIs you're using.

So many posts on Reddit asking which GUI is going to result in a "beautiful window", as if there's a magic GUI library that pretties things up for you.  There are some calls in PySimpleGUI that will help you.  For example, you can make a single call to "Chang the look and feel" which loads predefined color pallets so your windows can have some instant color and it matches.

Beautiful windows are created, not simply given to you.  There are people that design and create artwork for user interfaces, you know that right?  Artists draw buttons, artwork that you include in the window to make it nicer.

Some of these have been "polished", others like the Matplotlib example is more a functional example to show you it works.

![batterup](https://user-images.githubusercontent.com/46163555/77781297-b624ef80-702b-11ea-857a-b0809f061dc9.png)

![Uno](https://user-images.githubusercontent.com/46163555/77781360-d05ecd80-702b-11ea-90f9-cb9fb3339c05.png)


This chess program is capable of running multiple AI chess engines and was written by another user using PySimpleGUI.

![image](https://user-images.githubusercontent.com/13696193/61083102-e9214780-a3f8-11e9-9d1d-7c0a388625be.png)

This downloader can download files as well as YouTube videos and metadata.  If you're worried about multiple windows working, don't.  Worried your project is "too much" or "too complex" for PySimpleGUI?  Do an initial assessment if you want.  Check out what others have done.  

Your program have 2 or 3 windows and you're concerned?  Below you'll see 11 windows open, each running independently with multiple tabs per window and progress meters that are all being updated concurrently.  

![concurrent_windows](https://user-images.githubusercontent.com/13696193/62832448-3eb96180-bbfc-11e9-8777-6f2669566c93.png)


![pyplot 1](https://user-images.githubusercontent.com/13696193/44683336-11d46480-aa14-11e8-9d6c-f656796fc915.jpg)

Just because you can't match a pair of socks doesn't mean your windows have to all look the same gray color.  Choose from over 100 different "Themes".  Add 1 line call to `theme` to instantly transform your window from gray to something more visually pleasing to interact with.  If you mispell the theme name badly or specify a theme name is is missing from the table of allowed names, then a theme will be randomly assigned for you.  Who knows, maybe the theme chosen you'll like and want to use instead of your original plan.

In PySimpleGUI release 4.6 the number of themes was dramatically increased from a couple dozen to over 100.  To use the color schemes shown in the window below, add a call to `theme('Theme Name)` to your code, passing in the name of thd desired color theme. To see this window and the list of available themes on your releeae of softrware, call the function `theme_previewer()`.  This will create a window with the frames like those below.  It will shows you exactly what's available in your version of PySimpleGUI.

In release 4.9 another 32 Color Themes were added... here are the current choices

![Dec 2019 Look And Feel Themes](https://user-images.githubusercontent.com/46163555/70382042-796da500-1923-11ea-8432-80d08cd5f503.jpg)

Make beautiful looking, alpha-blended (partially transparent) Rainmeter-style Desktop Widgets that run in the background.

![cpumeter](https://user-images.githubusercontent.com/46163555/77781418-ec626f00-702b-11ea-90b3-668fb71d63b5.png)

Want to build a Crossword Puzzle?  No problem, the drawing primitives are there for you.

![snag-0185](https://user-images.githubusercontent.com/13696193/47968340-98ba4480-e036-11e8-9d44-8a39ac174533.jpg)

There are built-in drawing primitives

![snag-0168](https://user-images.githubusercontent.com/13696193/47753225-2ed42080-dc6d-11e8-88d1-cf833db6c7ef.jpg)


Frame from integration with a YOLO Machine Learning program that does object identification in realtime while allowing the user to adjust the algorithms settings using the sliders under the image.  This level of interactivity with an AI algorithm is still unusual to find due to difficulty of merging the technologies of AI and GUI.  It's no longer difficult.  This program is under 200 lines of code.

![snag-0278](https://user-images.githubusercontent.com/13696193/48845583-e4752980-ed6a-11e8-9b2f-6c3d5d2442ba.jpg)



# Pi Windows

Perhaps you're looking for a way to interact with your **Raspberry Pi** in a more friendly way.  Your PySimpleGUI code will run on a Pi with no problem.  Tkinter is alive and well on the Pi platform. Here is a selection of some of the Elements shown on the Pi.  You get the same Elements on the Pi as you do Windows and Linux.

![raspberry pi everything demo](https://user-images.githubusercontent.com/13696193/44279694-5b58ce80-a220-11e8-9ab6-d6021f5a944f.jpg)


You can add custom artwork to make it look nice, like the Demo Program - Weather Forecast shown in this image:

![weather pi](https://user-images.githubusercontent.com/13696193/47305324-1d4ca200-d5f7-11e8-8584-24a3992283ee.jpg)

![weather alone](https://user-images.githubusercontent.com/13696193/47305323-1d4ca200-d5f7-11e8-8fb1-44b0a7a4580f.jpg)

One thing to be aware of with Pi Windows, you cannot make them semi-transparent.  This means that the `Window.Disappear` method will not work.  Your window will not disappear.  Setting the Alpha Channel will have no effect.

Don't forget that you can use custom artwork anywhere, including on the Pi.  The weather application looks beautiful on the Pi.  Notice there are no buttons or any of the normal looking Elements visible.  It's possible to build nice looking applications, even on the lower-end platforms.


# Games

It's possible to create some cool games by simply using the built-in PySimpleGUI graphic primivites like those used in this game of pong.  PyGame can also be embedded into a PySimpleGUI window and code is provided to you demonstrating how.  There is also a demonstration of using the pymunk physics package that can also be used for games.

Games haven't not been explored much, yet, using PySimpleGUI.

![pong](https://user-images.githubusercontent.com/46163555/77781526-1c117700-702c-11ea-901b-4cb5f7a34cb4.png)


# Windows Programs That Look Like Windows Programs

***Do you have the desire to share your code with other people in your department, or with friends and family?*** Many of them may not have Python on their computer.  And in the corporate environment, it may not be possible for you to install Python on their computer.

`PySimpleGUI + PyInstaller` to the rescue!!

Combining PySimpleGUI with PyInstaller creates something truly remarkable and special, a Python program that looks like a Windows WinForms application.  

The application you see below with a working menu was created in 20 lines of Python code.  It is a single .EXE file that launches straight into the screen you see.  And more good news, the only icon you see on the taskbar is the window itself... there is no pesky shell window.  Nice, huh? 

![windowsprogram](https://user-images.githubusercontent.com/46163555/77781479-03a15c80-702c-11ea-9408-903e022e0418.png)


With a simple GUI, it becomes practical to "associate" .py files with the python interpreter on Windows.  Double click a py file and up pops a GUI window, a more pleasant experience than opening a dos Window and typing a command line.

There is even a PySimpleGUI program that will take your PySimpleGUI program and turn it into an EXE.  It's nice because you can use a GUI to select your file and all of the output is shown in the program's window, in realtime.

# Background - Why PySimpleGUI Came to Be

Feel free to skip all this if you don't care to know the backstory and reasons behind decisions.

There was a project looming and a GUI was needed.  It wasn't a very complex GUI so thus began a search for a simplified GUI package that would enable me to work with tkinter easier.  I found a few, and they were pretty popular too, but they lacked the full-compliment of Widgets and it was impossible to define my own window using those widgets.

A whacky idea came to mind... what if I wrote a simplified GUI and then used THAT to write my application.  It would be a lot less code and it would be "easy" to write my application then.  And that is exactly what was done.

First an early version of PySimpleGUI was written that had a subset of the Elements avaiable today.  It had just enough for my application.  Then I wrote my application in PySimpleGUI.

Thus PySimpleGUI was born out of necessity and it's been the necessity of others that have helped evolve it into the package it is today.  It would not be 1/2 as good without the help of the community.

Once PySimpleGUI was done, it was time to start working on "the ports".  And, of course, also this documentation.

## The Non-OO and Non-Event-Driven Model

The two "advanced concepts" that beginning Python students have with GUIs are the use of classes and callbacks with their associated communication and coordination mechanisms (semaphores, queues, etc)

How do you make a GUI interface easy enough for first WEEK Python students? 

This meant classes could be used to build and use it, but classes can not be part of the code the user writes.  Of course, an OO design is quite possible to use with PySimpleGUI, but it's not a ***requirement***.  The sample code and docs stay away from writing new classes in the user space for the most part.

What about those pesky callbacks?  They're difficult for beginners to grasp and they're a bit of a pain in the ass to deal with.  The way PySimpleGUI got around events was to utilize ***a "message passing" architecture*** instead.  

Instead of a user function being called when there's some event, instead the information is "passed" to the user when they call the function `Window.read()` 

***Everything*** is returned through this `Window.read` call.  Of course the underlying GUI frameworks still perform callbacks, but they all happen inside of PySimpleGUI where they are turned into messages to pass to you.

All of the boilerplate code, the event handling, widget creation, frames containing widgets, etc, are **exactly the same** objects and calls that you would be writing if you wrote directly in tktiner, Qt, etc.  With all of this code out of the way and done for you, that leaves you with the task of doing something useful with the information the user entered.  THAT, afterall, is the goal here.... getting user information and acting on it.

The full complement of Widgets are available to you via PySimpleGUI Elements.  And those widgets are presented to you in a unique and fun way.

If you wish to learn more about the Architecture of PySimpleGUI, take a look at the [Architecture document located on ReadTheDocs](https://pysimplegui.readthedocs.io/en/latest/architecture/).

### The Result

A GUI that's appealing to a broad audience that is highly customizable, easy to program, and is solid with few bugs and rarely crashes (99% of the time it's some other error that causes a crash).

PySimpleGUI is becoming more and more popular. The number of installs and the number of successes grows daily.  Pip installs have exceeded 350,000 in the first year of existance.  Over 300 people a day visit the GitHub and the project has 1,800 stars (thank you aweesome users!)

The number of ports is up to 4.  The number of integrations with other technologies is constantly being expanded.  It's a great time to try PySimpleGUI!  You've got no more than 5 or 10 minutes to lose.

Caution is needed, however, when working with the unfinished ports.  PySimpleGUI, the tkinter version, is the only fully complete port.  Qt is next.  All of its Elements are completed, but not all of the options of each element are done.  PySimpleGUIWeb is next in order of completness and then finally PySimpleGUIWx.


# Features

While simple to use, PySimpleGUI has significant depth to be explored by more advanced programmers.  The feature set goes way beyond the requirements of a beginner programmer, and into the  required features needed for complex multi-windowed GUIs.

For those of you that have heard PySimpleGUI is only good for doing the most simplest of GUIs, this feature list should put that myth to rest.  **The SIMPLE part of PySimpleGUI is how much effort _you_ expend to write a GUI, not the complexity of the program you are able to create.**  It's literally "simple" to do... and it is not limited to simple problems.

Features of PySimpleGUI include:

- Support for Python versions 2.7 and 3
- Text
- Single Line Input
- Buttons including these types:
	- File Browse
	- Files Browse
	- Folder Browse
	- SaveAs
	- Normal button that returns event
	- Close window
	- Realtime
	- Calendar chooser
	- Color chooser
	- Button Menu
- TTK Buttons or "normal" TK Buttons
- Checkboxes
- Radio Buttons
- Listbox
- Option Menu
- Menubar
- Button Menu
- Slider
- Spinner
- Dial
- Graph
- Frame with title
- Icons
- Multi-line Text Input
- Scroll-able Output
- Images
- Tables
- Trees
- Progress Bar            Async/Non-Blocking Windows
- Tabbed windows
- Paned windows
- Persistent Windows
- Multiple Windows - Unlimited number of windows can be open at the same time
- Redirect Python Output/Errors to scrolling window
- 'Higher level' APIs (e.g. MessageBox, YesNobox, ...)
- Single-Line-Of-Code Proress Bar & Debug Print
- Complete control of colors, look and feel
- Selection of pre-defined palettes
- Button images
- Horizontal and Verticle Separators
- Return values as dictionary
- Set focus
- Bind return key to buttons
- Group widgets into a column and place into window anywhere
- Scrollable columns
- Keyboard low-level key capture
- Mouse scroll-wheel support
- Get Listbox values as they are selected
- Get slider, spinner, combo as they are changed
- Update elements in a live window
- Bulk window-fill operation
- Save / Load window to/from disk
- Borderless (no titlebar) windows (very classy looking)
- Always on top windows
- Menus with ALT-hotkey
- Right click pop-up menu
- Tooltips
- Clickable text
- Transparent windows
- Movable windows
- Animated GIFs
- No async programming required (no callbacks to worry about)
- Built-in debugger and REPL
- User expandable by accessing underlying GUI Framework widgets directly

---

## Design Goals

With the developer being the focus, the center of it all, it was important to keep this mindset at all times, including now, today.  Why is this such a big deal?  Because this package was written so that the universe of Python applications can grow and can **include EVERYONE into the GUI tent.**  

> Up in 5 minutes

Success #1 has to happen immediately.  Installing and then running your first GUI program.  FIVE minutes is the target.  The Pip install is under 1 minute.  Depending on your IDE and development environment, running your first piece of code could be a copy, paste, and run.  This isn't a joke target; it's for real serious.


> Beginers and Advanted Together

Design an interface that both the complete beginner can understand and use that has enough depth that an advanced programmer can make some very nice looking GUIs amd not feel like they're playing with a "toy".

> Success After Success

Success after success.... this is the model that will win developer's hearts.  This is what users love about PySimpleGUI.  Make your development progress in a way you can run and test your code often.  Add a little bit, run it, see it on your screen, smile, move on.

> Copy, Paste, Run.

The Cookbook and Demo Programs are there to fulfill this goal.  First get the user seeing on their screen a working GUI that's similar in some way to what they want to create.  

If you're wanting to play with OpenCV download the OpenCV Demo Programs and give them a try.  Seeing your webcam running in the middle of a GUI window is quite a thrill if you're trying to integrate with the OpenCV package.  

"Poof" instant running OpenCV based application == Happy Developer

> Make Simpler Than Expected Interfaces

The Single Line Progress Meter is a good example. It requires one and only 1 line of code.  Printing to a debug window is as easy as replacing `print` with `sg.Print` which will route your console output to a scrolling debug window.

> Be Pythonic

Be Pythonic... 

This one is difficult for me to define.  The code implementing PySimpleGUI isn't PEP8 compliant, but it is consistent.  The important thing was what the user saw and experienced while coding, NOT the choices for naming conventions in the implementation code.  The user interface to PySimpleGUI now has a PEP8 compliant interface.  The methods are snake_case now (in addition to retaining the older CamelCase names)

I ended up defining it as - attempt to use language constructs in a natural way and to exploit some of Python's interesting features.  It's Python's lists and optional parameters make PySimpleGUI work smoothly. 

Here are some Python-friendly aspects to PySimpleGUI:

- Windows are represented as Python lists of Elements 
- Return values are an "event" such a button push and a list/dictionary of input values
- The SDK calls collapse down into a single line of Python code that presents a custom GUI and returns values should you want that extreme of a single-line soluition
- Elements are all classes. Users interact with elements using class methods but are not required to write their own classes
- Allow keys and other identifiers be any format you want. Don't limit user to particular types needlessly.
- While some disagree with the single source file, I find the benefits greatly outweigh the negatives

#### Lofty Goals

> Teach GUI Programming to Beginners

By and large PySimpleGUI is a "pattern based" SDK.  Complete beginners can copy these standard design patterns or demo programs and modify them without necessarily understanding all of the nuts and bolts of what's happening.  For example, they can modify a layout by adding elements even though they may not yet grasp the list of lists concept of layouts.  

Beginners certainly can add more `if event == 'my button':` statements to the event loop that they copied from the same design pattern.  They will not have to write classes to use this package.

> Capture Budding Graphic Designers & Non-Programmers

The hope is that beginners that are interested in graphic design, and are taking a Python course, will have an easy way to express themselves, right from the start of their Python experience.  Even if they're not the best programmers they will be able express themselves to show custom GUI layouts, colors and artwork with ease.

> Fill the GUI Gap (Democratize GUIs)

There is a noticeable gap in the Python GUI solution.  Fill that gap and who knows what will happen.  At the moment, to make a tradiional GUI window using tkinter, Qt, WxPython and Remi, it takes much more than a week, or a month of Python education to use these GUI packages.  

They are out of reach of the beginners.  Often WAY out of reach.  And yet, time and time again, beginners that say they JUST STARTED with Python will ask on a Forum or Reddit for a GUI pacakage recommendation.  9 times out of 10 Qt is recommended.  (smacking head with hand).  What a waste of characters.  You might as well have just told them, "give up".

> Is There a There?

Maybe there's no "there there".  ***Or*** maybe a simple GUI API will enable Python to dominate yet another computing discipline like it has so many others.  This is one attempt to find out.  So far, it sure looks like there's PLENTY of demand in this area.


# Getting Started with PySimpleGUI

There is a "Troubleshooting" section towards the end of this document should you run into real trouble.  It goes into more detail about what you can do to help yourself.

## Installing PySimpleGUI

Of course if you're installing for Qt, WxPython, Web, you'll use PySimpleGUIQt, PySimpleGUIWx, and PySimpleGUIWeb instead of straight PySimpleGUI in the instructions below.  You should already have the underlying GUI Framework installed and perhaps tested.  This includes tkinter, PySide2, WxPython, Remi


### Installing on Python 3

`pip install --upgrade PySimpleGUI`

On some systems you need to run pip3. (Linux and Mac)

`pip3 install --upgrade PySimpleGUI`

On a Raspberry Pi, this is should work:

`sudo pip3 install --upgrade pysimplegui`

Some users have found that upgrading required using an extra flag on the pip `--no-cache-dir`.

`pip install --upgrade --no-cache-dir PySimpleGUI`

On some versions of Linux you will need to first install pip.  Need the Chicken before you can get the Egg (get it... Egg?)

`sudo apt install python3-pip`

`tkinter` is a requirement for PySimpleGUI (the only requirement).  Some OS variants, such as Ubuntu, do not some with `tkinter` already installed.  If you get an error similar to:

`ImportError: No module named tkinter`

then you need to install `tkinter`.

For python 2.7

`sudo apt-get install python-tk`

For python 3
`sudo apt-get install python3-tk`

More information about installing tkinter can be found here: https://www.techinfected.net/2015/09/how-to-install-and-use-tkinter-in-ubuntu-debian-linux-mint.html


### Installing for Python 2.7

**IMPORTANT** PySimpleGUI27 will disappear from the GitHub on Dec 31, 2019. PLEASE migrate to 3.6 at least.  It's not painful for most people.

`pip install --upgrade PySimpleGUI27`
or
`pip2 install --upgrade PySimpleGUI27`

You may need to also install "future" for version 2.7

`pip install future`
or
`pip2 install future`


Like above, you may have to install either pip or tkinter.  To do this on Python 2.7:

`sudo apt install python-pip`

`sudo apt install python-tkinter`

### Upgrading from GitHub Using PySimpleGUI

Starting in version 4.17.0 there is code in the PySimpleGUI package that upgrades your previously pip installed package using the latest version checked into GitHub.  

Previously if you wanted to run the GitHub version, you would:
* Download the PySimpleGUI.py file from GitHub
* Place it in your applications's folder

This required you to go back later and delete this file when you want to move on to the next version released to PyPI.  

The new capability is the ability to overwrite your PySimpleGUI.py file that you installed using `pip` with the currently posted version on GitHub.  Using this method when you're ready to install the next version from PyPI or you want to maybe roll back to a PyPI release, you only need to run `pip`.  You don't have to find and delete any PySimpleGUI.py files.

***Important - Linux Users*** - There is currently a problem using this utility on Linux systems.  It's being worked on and a patch will be released as soon as something is figured out.


#### Command Line Upgrade

To upgrade PySimpleGUI from the command line type this command into your dos window

`python -m PySimpleGUI upgrade`

You will first be shown a confirmation window:

![image](https://user-images.githubusercontent.com/46163555/77477572-f0f01300-6df2-11ea-812f-98a36e7c28e0.png)

If you choose yes, then the new version will be installed and you'll see a red "completed" window


![image](https://user-images.githubusercontent.com/46163555/77477619-006f5c00-6df3-11ea-8b01-44b1bea22989.png)


#### GUI Upgrade

The PySimpleGUI Test Harness is another mechanism you can use to upgrade.  To start the test harness you "run" the PySimpleGUI package.  

`python -m PySimpleGUI.PySimpleGUI`

Of course if you're running Linux you may run `python3` instead.

From your code you can call `PySimpleGUI.main()`.  This window may not look exactly like the one you see, but the thing that should be there is the red "Install" button.

![image](https://user-images.githubusercontent.com/46163555/77478381-437dff00-6df4-11ea-994e-a443ff967917.png)


Clicking the install button will bring up the same confirmation window shown as the command line upgrade above.

### Testing your installation and Troubleshooting

Once you have installed, or copied the .py file to your app folder, you can test the installation using python.  At the command prompt start up Python.

#### The Quick Test

The PySimpleGUI Test Harness pictured in the previous section on GUI upgrades is the short program that's built into PySimpleGUI that serves multiple purposes.  It exercises many/most of the available Elements, displays version and location data and works as a quick self-test.

From your command line type:
`python -m PySimpleGUI.PySimpleGUI`

If you're on Linux/Mac and need to run using the command `python3` then of course type that.

This will display the test harnes window.  

You can also test by using the REPL....

#### Instructions for Testing Python 2.7:
```python
>>> import PySimpleGUI27
>>> PySimpleGUI27.main()
```

#### Instructions for Testing Python 3:

```python3
>>> import PySimpleGUI
>>> PySimpleGUI.main()
```

You will see a "test harness" that exercises the SDK, tells you the version number, allows you to try 

### Finding Out Where Your PySimpleGUI Is Coming From

It's **critical** for you to be certain where your code is coming from and which version you're running.

Sometimes when debugging, questions arise as to exactly which PySimpleGUI you are running.  The quick way to find this out is to again, run Python from the command line.  This time you'll type:


```python3
>>> import PySimpleGUI as sg
>>> sg
```

When you type sg, Python will tell you the full patch to your PySimpleGUI file / package.  This is critical information to know when debugging because it's really easy to forget you've got an old copy of PySimpleGUI laying around somewhere.


### Finding Out Where Your PySimpleGUI Is Coming From (from within your code)

If you continue to have troubles with getting the right version of PySimpleGUI loaded, THE ***definitive*** way to determine where your program is getting PySimpleGUI from is to add a print to your program.  It's that *simple*!  You can also get the version you are running by also printing

```python
import PySimpleGUI as sg

print(sg)
print(sg.version)
```

Just like when using the REPL >>> to determine the location, this `print` in your code will display the same path information.


### Manual installation

If you're not connected to the net on your target machine, or pip isn't working, or you want to run the latest code from GitHub, then all you have to do is place the single PySimpleGUI source file `PySimpleGUI.py` (for tkinter port) and place it in your application's folder (the folder where the py file is that imports PySimpleGUI).  Your application will load that local copy of PySimpleGUI as if it were a package.

Be ***sure*** that you delete this PySimpleGUI.py file if you install a newer pip version.  Often the sequence of events is that a bug you've reported was fixed and checked into GitHub.  You download the PySimpleGUI.py file (or the appropriately named one for your port) and put with your app.  Then later your fix is posted with a new release on PyPI.  You'll want to delete the GitHub one before you install from pip.

### Prerequisites

Python 2.7 or Python 3
tkinter

PySimpleGUI Runs on all Python3 platforms that have tkinter running on them.  It has been tested on Windows, Mac, Linux, Raspberry Pi.  Even runs on `pypy3`.

### EXE file creation

If you wish to create an EXE from your PySimpleGUI application, you will need to install `PyInstaller`.  There are instructions on how to create an EXE at the bottom of this document.


## IDEs

A lot of people ask about IDEs, and many outright fear PyCharm.  Listen up.... compared to your journey of learning Python, learning to use PyCharm as your IDE is NOTHING.  It's a DAY typically (from 1 to 8 hours).  Or, if you're really really new, perhaps as much as a week *to get used to*.  So, we're not talking about you needing to learn to flap your arms and fly.

To sum up that paragraph, stop whining like a little b*tch.  You're a grown man/woman, act like it.  "But it's hard..."  If you found this package, then you're a bright person :-)  Have some confidence in yourself for Christ sake.... I do.  Not going to lead you off some cliff, promise!

Some IDEs provide virtual environments, but it's optional.  PyCharm is one example.  For these, you will either use their GUI interface to add packages or use their built-in terminal to do pip installs.  **It's not recommended for beginners to be working with Virtual Environments.**  They can be quite confusing.  However, if you are a seasoned professional developer and know what you're doing, there is nothing about PySimpleGUI that will prevent you from working this way.  It's mostly a caution for beginners because more often than not, they get really messed up and confused.

### Officially Supported IDEs

A number of IDEs have **known problems with PySimpleGUI**.  IDLE, Spyder, and Thonny all have known, demonstrable, problems with intermittent or inconsistent results, **especially when a program exits** and you want to continue to work with it. *** Any IDE that is based on tkinter is going to have issues with the straight PySimpleGUI port.***  This is NOT a PySimpleGUI problem.


The official list of supported IDEs is:
1. PyCharm (or course this is THE IDE to use for use with PySimpleGUI)
2. Wing
3. Visual Studio

If you're on a Raspberry Pi or some other limited environment, then you'll may have to use IDLE or Thonny.  Just be aware there could be problems using the debugger to debug due to both using tkinter.


### Using The Docstrings (Don't skip this section)

Beginning with the 4.0 release of PySimpleGUI, the tkinter port, a whole new world opened up for PySimpleGUI programmers, one where referencing the readme and ReadTheDocs documentation is no longer needed.  PyCharm and Wing both support these docstrings REALLY well and I'm sure Visual Studio does too.  Why is this important?  Because it will teach you the PySimpleGUI SDK as you use the package.  

Don't know the parameters and various options for the `InputText` Element?  It's a piece of cake with PyCharm.  You can set PyCharm to automatically display documentation about the class, function, method, etc, that your cursor is currently sitting on.  You can also manually bring up the documentation by pressing CONTROL+Q.  When you do, you'll be treated to a window similar to this:

![image](https://user-images.githubusercontent.com/13696193/61997565-46f89500-b071-11e9-968e-83a99ecb718a.png)


Note that my cursor is on `InputText`.  On the left side of the screen, the `InputText` element's parameters are not just shown to you, but they are each individually described to you, and, the type is shown as well.  *I mean, honestly, how much more could you ask for?*

OK, I suppose you could ask for a smaller window that just shows the parameters are you're typing them in.  Well, OK, in PyCharm, when your cursor is between the  `(   )` press CONTROL+P.  When you do, you'll be treated to a little window like this one:

![image](https://user-images.githubusercontent.com/13696193/61997590-aa82c280-b071-11e9-8d76-7d9c811f8fcc.png)

See.... written with the "Developer" in mind, at all times.  It's about YOU, Mr/Ms Developer!  So enjoy your package.

The other ports of PySimpleGUI (Qt, WxPython, Web) have not yet had their docstrings updated.  They're NEXT in line to be better documented.  Work on a tool has already begun to make that happen sooner than later.


#### Type Checking With Docstrings

In version 4.17.0 a new format started being used for docstrings.  This new format more clearly specified the types for each parameter.  It will take some time to get all of the parameter types correctly identied and documented.  

Pay attention when you're working with PyCharm and you'll see where you may have a mismatch... or where there's a bad docstring, take your pick. It will shade your code in a way that makes mismatched types very clear to see.


## Using  - Python 3

To use in your code, simply import....
`import PySimpleGUI as sg`

Then use either "high level" API calls or build your own windows.

`sg.Popup('This is my first Popup')`

![first popup](https://user-images.githubusercontent.com/13696193/44957300-c7813680-ae9e-11e8-9a8c-c70198db7907.jpg)


Yes, it's just that easy to have a window appear on the screen using Python.  With PySimpleGUI, making a custom window appear isn't much more difficult.  The goal is to get you running on your GUI within ***minutes***, not hours nor days.


### Python 3.7

If you must run 3.7, try 3.7.2.  It does work with PySimpleGUI with no known issues.

***PySimpleGUI with Python 3.7.3 and 3.7.4+.***  tkinter is having issues with all the newer releases.  Things like Table colors stopped working entirely.  

March 2020 - Still not quite sure if all issues have been ironed out with tkinter in the 3.7 and 3.8 releases.


## Python 2.7

On December 31, 2019 the Python 2.7 version of PySimpleGUI will be **deleted** from the GitHub.  Sorry but Legacy Python has no permanent home here.  The security experts claim that supporting 2.7 is doing a diservice to the Python community.  I understand why.  There are some very narrow cases where 2.7 is required.  If you have one, make a copy of PySimpleGUI27.py quickly before it disappears for good.


---

