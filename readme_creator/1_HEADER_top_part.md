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


![Python Version](https://img.shields.io/badge/PySimpleGUI_For_Python_3.x_Version-4.0.0-red.svg?longCache=true&style=for-the-badge)

![Python Version](https://img.shields.io/badge/PySimpleGUI_For_Python_2.7_Version-2.0.0-blue.svg?longCache=true&style=for-the-badge)

![Python Version](https://img.shields.io/badge/PySimpleGUIQt_Version-0.26.0-orange.svg?longCache=true&style=for-the-badge)

![Python Version](https://img.shields.io/badge/PySimpleGUIWx_version-0.11.0-orange.svg?longCache=true&style=for-the-badge)

![Python Version](https://img.shields.io/badge/PySimpleGUIWeb_Version-0.28.1-orange.svg?longCache=true&style=for-the-badge)



# PySimpleGUI
## Python GUIs For Humans - Transforms tkinter, Qt, Remi, WxPython into a people-friendly Pythonic interfaces
## (Non-humans.... PySimpleGUI-Feline port planned for 2020)

## 12-July-2019 Note - This readme is undergoing major changes. It's being released a little early as not all doc strings are completed in the sourcecode.

#### Looking for a GUI package?     Are you....

* looking to take your Python code from the world of command lines and into the convenience of a GUI? 
* sitting on a Raspberry **Pi** with a touchscreen that's going to waste because you don't have the time to learn a GUI SDK?
* into Machine Learning and are sick of the command line?
* an IT guy/gal that has written some cool tools but due to corporate policies are unable to share unless an EXE file?
* wanting to distribute your Python code to Windows users as a single .EXE file that launches straight into a GUI, much like a WinForms app?
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
* Works with Qt Designer
* Built in Debugger
* Actively maintained and enhanced - 4 ports are underway, all being used by users.
* Corporate as well as home users.
* Appealing to both newcomers to Python and experiened Pythonistas. 
* The focus is entirely on the developer and making their life easier, simplified, and in control.

## GUI Development does not have to be difficult nor painful.  It can be FUN

#### What users are saying about PySimpleGUI
###### (None of these comments were solicited & are not paid endorsements - other than a huge thank you they received!)

"I've been working to learn PyQT for the past week in my off time as an intro to GUI design and how to apply it to my existing scripts... Took me ~30 minutes to figure out PySimpleGUI and get my scripts working with a GUI."

"Python has been an absolute nightmare for me and I've avoided it like the plague.  Until I saw PysimpleGUI."

"I've been pretty amazed at how much more intuitive it is than raw tk/qt. The dude developing it is super active on the project too so if you come across situations that you just can't get the code to do what you want you can make bug/enhancement issues that are almost assured to get a meaningful response."

"This library is the easiest way of gui programming in python! I'm totally in love with it ❤️"

"Wow that readme is extensive and great." (hear the love for docs often)

"Coming from R, Python is absolutely slick for GUIs. PySimpleGUI is a dream."

"I have been writing Python programs for about 4 or 5 months now. Up until this week I never had luck with any UI libraries like Tkinter, Qt, Kivy.  I went from not even being able to load a window in Tkinter reliably to making a loading screen, and full program in one night with PySimpleGUI."

"I love PySimpleGUI! I've been teaching it in my Python classes instead of Tkinter."



#### Quick Links To Help and Read Up on the Latest News and Releases

[Homepage - Lastest Readme and Code - GitHub](http://www.PySimpleGUI.com)

[Announcements of Latest Developments, Release news, Misc](https://github.com/PySimpleGUI/PySimpleGUI/issues/142)

[ReadTheDocs](http://www.PySimpleGUI.org)  <------ THE best place to read the docs due to TOC, etc. **All** the documentation in **one** place

[COOKBOOK!](http://Cookbook.PySimpleGUI.org)

[Brief Tutorial](https://pysimplegui.readthedocs.io/tutorial/)

[Latest Demos and Master Branch on GitHub](https://github.com/PySimpleGUI/PySimpleGUI)

[Repl.it Home for PySimpleGUI](https://repl.it/@PySimpleGUI)

[Lots of screenshots](https://github.com/PySimpleGUI/PySimpleGUI/issues/1)




#### Python versions
As of 9/25/2018 **both Python 3 and Python 2.7 are supported** when using **tkinter version** of PySimpleGUI! The Python 3 version is named `PySimpleGUI`. The Python 2.7 version is `PySimpleGUI27`.  They are installed separately and the imports are different. See instructions in Installation section for more info.  **None** of the other ports can use Python 2.


# Platforms

## Hardware and OS Support

PySimpleGUI runs on Windows, Linux and Mac, just like tkinter, Qt, WxPython and Remi do.  If you can get the underlying GUI Framework installed / running on your machine then PySimpleGUI will also run there.

### Hardware

* PC's, Desktop, Laptops
* Macs of all types
* Raspberry Pi
* Android devices like phones and tablets

### OS

* Windows 7, 8, 10
* Linux on PC - Tested on **many** distributions
* Linux on Raspbnerry Pi
* Linux on Android - Must use either Termux or PyDroid3
* Mac OS (Sorry I don't know much about Macs)

## Output Devices

In addition to running as a desktop GUI, you can also run your GUI in a web browser by running PySimpleGUIWeb.  

This is ideal for "headless" setups like a Raspberry Pi that is at the core of a robot or other design that does not have a normal display screen.  For these devices, run a PySimpleGUIWeb program that never exits.  

Then connect to your application by going to the Pi's IP address (and port #) using a browser and you'll be in communication with your application.  You can use it to make configuration changes or even control a robot or other piece of hardward using buttons in your GUI

## A Complete PySimpleGUI Program (Getting The Gist)

Before diving into details, here's a description of what PySimpleGUI is/does and why that is so powerful.

You keep hearing "custom window" in this document because that's what you're making and using... your own custom windows.

Wouldn't it be nice if a GUI with 3 "rows" of Widgets (Elements) was defined in 3 lines of code?  That's exactly how it's done.  Each row of Elements are a list.  Put all those lists together and you've got a window.

What about handling button clicks and stuff.  That's 5 lines of the code below beginning with the while loop.  

Now look at the `layout` variable and then look at the window graphic below.  Defining a window is taking a design you can see visually and then visually creating it in code.  One row of Elements = 1 line of code (can span more if your window is crowded).  The window is exactly what we see in the code.  A line of text, a line of text and an input area, and finally ok and cancel buttons.

This makes the coding process extremely quick and the amount of code very small

```python
import PySimpleGUI as sg
# All the stuff inside your window. This is the PSG magic code compactor...
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events"
while True:             
    event, values = window.Read()
    print(event, values)
    if event in (None, 'Cancel'):
        break

window.Close()
```

![image](https://user-images.githubusercontent.com/13696193/61077153-cdfc0b00-a3eb-11e9-9e93-d6ec2ffb442a.png)

You gotta admit that the code above is a lot more "fun" looking that tkinter code you've studied before.  Adding stuff to your GUI is trivial.  You can clearly see the "mapping" of those 3 lines of code to specific Elements laid out in a Window.   It's not a trick.  It's how easy it is to code in PySimpleGUI.  

It's a thrill to complete your GUI project way ahead of what you estimated.  Some people take that extra time to polish their GUI to make it even nicer, adding more bells and whistles because it's so easy and it's a lot of fun to see success after success as you write your program.

Others, like IT people and hackers are busily cranking out GUI program after GUI program, and creating tools that others can use.  Finally there's an easy way to throw a GUI onto your program and give it to someone.  It's a pretty big leap in capability for some people.

Elements are the term used by PySimpleGUI that map to GUI Widgets.  A "Text Element" in PySimpleGUI == "Label Widget" in tkinter.

The final bit of magic is in how Elements are created and changed.  What about Elements that have settings other than the standard system settings?   What if I want my Text to be blue, with a Helverica font on a green background.  It's written quite simply:

 ```python
 Text('This is some text', font='Helvetica 12', text_color='blue', background_color='green')
 ```

 As you'll learn in later sections that discuss the parameters to the Elements, there are a LOT of options avilable to you should you choose to use them.  The `Text Element` has 15 parameters that you can change.  This is one reason why PyCharm is suggested as your IDE... it does a fantastic job of displaying documentation as you type in your code.


## The Underlying GUI Frameworks

At the moment there are 4 acitvely developed and maintained "ports" of PySimpleGUI.  These include:
1. tkinter - Fully complete
2. Qt using Pyside2 - Alpha stage.  Not all features for all Elements are done
3. WxPython - Development stage, pre-releaser.  Not all Elements are done. Some known problems with multiple windows
4. Remi (Web browser support) - Development stage, pre-release.


While PySimpleGUI, the tkinter port, is the only 100% completed version of PySimpleGUI, the other 3 ports have a LOT of functionality in them and are in active use by a large portion of the installations.  You can see the number of Pip installs at the very top of this document to get a comparison as to the size of the install base for each port.  The "badges" are right after the logo.


# The PySimpleGUI "Family"

## What's The Big Deal? What is it?

PySimpleGUI wraps tkinter, Qt, WxPython and Remi so that you get all the same widgets, but you interact with them in a more friendly way. What does a wrapper do?  It does the layout, boilerplate code, creates and manages the GUI Widgets for you and presents you with a **simple, efficient interface.**   It replaces the Widgets in tkinter/Qt/Wx/Remi and replaces them with PySimpleGUI Elements.   It replaces the GUIs' event loop with one of our own.  

You've seen examples of the code already.  The big deal of all this is that anyone can create a GUI simply and quickly that matches GUIs written in the native GUI framework.  You can create complex layouts with complex element interactions.  And, that code you wrote to run on tkinter will also run on Qt by changing your import statement.


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


Qt was the second port after tkinter.  It is the 2nd most complete with the original PySimpleGUI (tkinter) being the most complete and is likely to continue to be the front-runner.

As mentioned previously each port has an area.  For Qt, you can learn more on the [PySimpleGUIQt GitHub site](https://github.com/MikeTheWatchGuy/PySimpleGUI/tree/master/PySimpleGUIQt).  **There is a separate Readme file for the Qt version** that you'll find there.  This is true for all of the PySimpleGUI ports.

Give it a shot if you're looking for something a bit more "modern".  PySimpleGUIQt is currently in Alpha.  All of the widgets are operational but some may not yet be full-featured.  If one is missing and your project needs it, log an Issue.  It's how new features are born.

Here is a summary of the Qt Elements with no real effort spent on design clearly.  It's an example of the "test harness" that is a part of each port. If you run the PySimpleGUI.py file itself then you'll see one of these tests.

As you can see, you've got a full array of GUI Elements to work with.  All the standard ones are there in a single window.  So don't be fooled into thinking PySimpleGUIQt is barely working or doesn't have many widgets to choose from.


![scrolling graphics](https://user-images.githubusercontent.com/13696193/48665874-8bfd0e00-ea84-11e8-880d-8e164d9fea34.gif)


## WxPython Version

[PySimpleGUIWx GitHub site](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWx).  **There is a separate Readme file for the WxPython version**.

Started in late December 2018 PySimpleGUIWx started with the SystemTray Icon feature.    This enabled the package to have one fully functioning feature that can be used along with tkinter to provide a complete program.    The System Tray feature is complete and working very well.  It was used not long ago in a corporate setting and has been performing perfectly.

The Windowing code was coming together with Reads operational which means Popups work.  The elements were getting completed on a regular basis. But I ran into multiwindow problems.  And it was at about this time that Remi was suggested as a port.

Remi (the "web port") overnight lept the WxPython effort and Web became a #1 priority and continues to be.  The thought is that the desktop was well represented with PySimpleGUI, PySimpleGUIQt, and PySimpleGUIWx.  Between those ports is a solid winowing system and 2 system tray implementations and a nearly feature complete Qt effort.  So, the team was switched over.

## Web Version (Remi)

[PySimpleGUIWeb GitHub site](https://github.com/PySimpleGUI/PySimpleGUI/tree/master/PySimpleGUIWeb).  **There is a separate Readme file for the Web version**.

New for 2019, PySimpleGUIWeb.  This is an exciting development!  PySimpleGUI in your Web Browser!

The underlying framework supplying the web capability is the Python package Remi.  https://github.com/dddomodossola/remi  Remi provides the widgets as well as a web server for you to connect to.  It's an exiting new platform to be running on and has temporarily bumped the WxPython port from the highest priority.  PySimpleGUIWeb is the current high priority project.

Use this solution for your Pi projects that don't have anything connected in terms of input devices or display.  Run your Pi in "headless" mode and then access it via the Web interface.  This allows you to easily access and make changes to your Pi without having to hook up anything to it.


## Source code compatibility

Your source code is completely portable from one platform to another by simply changing the import statement.  That's the GOAL and if OFTEN the case.  I've been stunned how many times thins works.  Seeing your code run on tkinter, then change the import to `import  PySimpleGUIWeb as sg` and instead of a tkinter window, up pops Chrome with your window running in there instead.

What does this mean?  It means it takes a trivial amount of effort to move across GUI Frameworks.  Don't like the way your GUI looks on tkinter?  No problem, change over to try PySimpleGUIQt.  Made a nice desktop app but want to bring it to the web too?  Again, no problem, use PySimpleGUIWeb

## repl.it Version

***Want to really get your mind blown?***  Check out this [PySimpleGUI program](https://repl.it/@PySimpleGUI/PySimpleGUIWeb-Demos) running in your web browser.

Thanks to the magic of repl.it and Remi it's possible to run PySimpleGUI code in a browser window without having Python running on your computer.

The programs you write using repl.it will automatically download and install the latest PySimpleGUIWeb from PyPI onto a virtual Python environment.  All that is required is to type `import PySimpleGUIWeb` you'll have a Python environment up and running with the latest PyPI release of PySimpleGUIWeb.

This is an exciting new development that's opening up all kinds of possibilities for new ways to program and learn PySimpleGUI.   Stayed tuned, much more to be posted about this in the near future.

Educators in particular should be interested.  Students can not only post their homework easily for their teacher to access, but teachers can also run the students programs online.  No downloading needed.  Run it and check the results.

Depending on how you're viewing this document, you may or may not see an embedded browser window below that is running PySimpleGUI code.  

Not only can you run PySimpleGUIWeb code using repl.it, they have a tkinter library version.  You can see a tkinter (a PySimpleGUI window) in a browser using repl.it.


## Macs

It's surprising that Python GUI code is completely cross platform from Windows to Mac to Linux.  No source code changes.  This is true for both  PySimpleGUI and PySimpleGUIQt.

However, **Macs** suck.  They suck on tkinter in particular.  The "Look and feel" calls are disabled for Macs.  Colored buttons in particular are broken.  Not in the PySimpleGUI code, of course.  Consider using Qt instead of tkinter on the Mac.  Or, if using tkinter, bring your own button images.  

I suggest looking through the open and closed issues if you're a  Mac person with a problem.

*Switching to "Light Mode" is known to fix some of the problems.*  They honestly are tkinter/Mac problems.

Make sure you're running tkinter 8.6 and up.


# Support

PySimpleGUI is an active project.  Bugs are fixed, features are added, often.  Should you run into trouble, open an issue on the [GitHub site](http://www.PySimpleGUI.com) and you'll receive help.  Posting questions on StackOverflow, Forums, Mailing lists, Reddit, etc, is not the fastest path to support and taking it may very well lead you astray as folks not familiar with the package struggle to help you.

So, [open an Issue](https://github.com/PySimpleGUI/PySimpleGUI/issues/new/choose), choose "custom form" and fill it out completely.  There are very good reasons behind all of the questions.  Cutting corners only cuts your chances of getting help and getting quality help as it's difficult enough to debug remotely.  Don't handicap people that want to help by not providing enough information.

Be sure and run your program outside of your IDE *first*.  Start your program from the shell using `python` or `python3` command.  On numerous occassions much time was spent chasing problems caused by the IDE.  By running from a command line, you take that whole question out of the problem, an important step.

### PySimpleGUI Trolls

Yea, they're out there.  Would have NEVER in a billion years guessed that there would be objection, coming from a small, but vocal, number of people.  I naively believed everyone would be supportive, see the value, hold hands around the fire, sing songs, and in the very least be truthful.  But, this ain't Kansas and the Internet is...  WTF is it with people?

If someone is actively discouraging you from using this package, then know you are on the right track and you should give it a try.  Weird stuff like this sometimes happens because the person works for a particular company or they have a GUI package of their own.... that's not popuplar.

I promise you're not going to be wrecked for life.  It will not cause you to be a bad programmer with bad habits.  It will not ruin your career.  It's not going to teach you bad habits.  One person I know got a bonus based on a PySimpleGUI program he wrote. I promise you WILL see a GUI in 5 minutes.  And you could see some pretty cool stuff running in a GUI by grabbing the GitHub and start running and hacking on files.

So fear not.  ***How about success being the goal?***  Spend time polishing your GUI and working on your primary code instead of struggling your way through the mountains of documentation in the Qt library, trying to set the color of something.  

Start with PySimpleGUI, then in the future if you want to code directly in Qt to get more control, it's not like you won't be able to pick up Qt due to your PySimpleGUI knowledge.  If anything, you'll have more knowledge going it than most people that are just starting because you'll have already built working GUIs, perhaps many of them.

### Target Audience

PySimpleGUI is trying to serve the 80% of GUI problems. The other 20% go straight onto Qt or WxPython, or whoever fills that need. 

PySimpleGUI is designed with both the beginner and the experienceed developer in mind.  Why?  Because both tend to like compact code as much as I do.  Most like people, we just want to get sh\*t done, right? 

No, you like the existing GUI architectures (they're all roughly the same, except this one), go join the 20% club just down the street.  There's plenty of room for you there.  But how about a quick stop-in for some open mindedness exercises.  Maybe you will come up with an interesting suggestion even if you don't use it.  Or maybe PySimpleGUI does something that inspires you to write something similar directly in Qt.

#### Beginners

There are a couple of reasons beginners stop in for a peek.  The first is to simply throw a simple GUI onto the front of an existing command line application.  Or maybe you need to popup a box to get a filename.  These can often be simple 1-line `Popup` calls.

If you have a more intricate, complete, perhaps multi-window design in mind, then PySimpleGUI still could be your best choice.

This package is not only great to use as your first GUI package, but it also teaches how to design and utilize a GUI.  In fact, it does it better than any existing GUI.  Why?  Because it removes the classes, callback functions, object oriented design to better get out of your way and let you focus entirely on your GUI and not how to represent it in code.  The result is 1/2 to 1/10 th the amount of code that implements the exact same layout and widgets as you would get from coding yourself directly in Qt5.

Forget syntax completely and just look on the overall activities of a PySimpleGUI programmer.  You have to design your window.... determine your inputs and your outputs, place buttons in strategic places, create menus, .... You'll be busy just doing all those things to design and define your GUI completely independent upon the underlying framework. 

#### Advanced Programmers, Code Slingers

It's not perfect, but PySimpleGUI is an amazing bit of technology. 

As mentioned, you really can write both a desktop and a web application at the same time, among other things.

What I hear from seasoned professionals is that PySimpleGUI saves them a **ton** of time.  They've written GUI code before.  They know how to lay out a window.  These folks just want to get their window working and quick.

With the help of IDE's like PyCharm, Visual STudio and Wing (the offically supported list) you get instant documentation on the calls you are making.  On PyCharm you instantly see both the call signature but also the explanations about each parameter.

Because PySimpleGUI has so many parameters to element creation calls, you really need this level of integration between code and documentation to be able to work quickly.

If the screenshots, demo programs and documentation don't convince you to at least **give it a try, once**, then you're way too busy, or .....  I dunno, I stopped guessing "why?" some time ago.  Some of the most reluctant of people to try PySimpleGUI have turned out to be some of the biggest supporters.


-------------------

# Learning Resources

The initial "get up and running" portion of PySimpleGUI should take you less than 5 minutes.  The goal is 5 minutes from your decision "I'll give it a try" to having your first window up on the screen "Oh wow, it was that easy?!" in 5 minutes or less.

The primary learning pathes for PySimpleGUI are:
 * This readme document over 100 pages of PySimpleGUI answers 
 	* http://www.PySimpleGUI.org
 * The Cookbook - Recipes to get you going 
 	* http://Cookbook.PySimpleGUI.org
 * The Demo Programs - Start hacking on one of these running soluitions
	* http://www.PySimpleGUI.com
 * The YouTube videos - If you like instructional videos, there are 15 videos
	* [5 part series of basics](https://www.youtube.com/playlist?list=PLl8dD0doyrvHMoJGTdMtgLuHymaqJVjzt)
	* [10 part series of more detail](https://www.youtube.com/playlist?list=PLl8dD0doyrvGyXjORNvirTIZxKopJr8s0)

 Everything is geared towards giving you a "quick start" whether that be a Recipe or a Demo Program.  The idea is to give you something running and let you hack away at it.  As a developer this saves tremendous amounts of time.

 You **start** with a working program, a GUI on the screen.  Then have at it.

 A high percentage of users report both learning PySimpleGUI and completing their project in a single day.  This isn't a rare event at all.  GUI programming doesn't HAVE to be difficult by definition and PySimpleGUI has certainly made it much much more approachable.

## This Readme and Cookbook

The readme and Cookbook are best viewed on ReadTheDocs.  The quickest way there is to visit:
http://www.PySimpleGUI.org

You will be auto-forwarded to the right destination.  There are multiple tabs on ReadTheDocs.  One for the main readme and one for the Cookbook.  There are other documents there like an architectural design doc

The Cookbook has approx 27 "Recipes" or short programs that can be easily copied and pastedThe addition of MANY embedded frames of repl.it frames has slowed down the page.  I'm questioning the decision to add those embedded frames and may soon remove them.

## Demo Programs

The GitHub repo has the Demo Programs.  There are ones built for plain PySimpleGUI that are usually portrable to other versions of PySimpleGUI.  And there are some that are associated with one of the other ports.  The easiest way to the GitHub:
http://www.PySimpleGUI.com

As of this writing, on 2019-07-10 there are 177 Demo Programs for you to choose from.  

These programs demonstrate to you how to use the Elements and especially how to integtate PySimpleGUI with some of the popular open source technologies such as OpenCV, PyGame, PyPlot, and Matplotlib to name a few.


---

# The Quick Tour

Let's take a super-brief tour around PySimpleGUI.  There are 2 levels of windowing support in PySimpleGUI -  High Level and Customized.

The high-level calls are those that perform a lot of work for you. These are not custom made windows (those are the other way of interacting with PySimpleGUI).

Let's use one of these high level calls, the `Popup` and use it to create our first window, the obligatory "Hello World".  It's a single line of code.  You can use these calls like print statements, adding as many parameters and types as you desire.

```python
import PySimpleGUI as sg

sg.Popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')
```


![hello world](https://user-images.githubusercontent.com/13696193/44960047-1f7f6380-aec6-11e8-9d5e-12ef935bcade.jpg)


Or how about a ***custom GUI*** in 1 line of code?  No kidding this is a valid program and it uses Widgets like you normally would in a tkinter program.  It's just been compacted together is all, strictly for demonstration purposes as there's no need to go that extreme in compactness, unless you have a reason to and then you can be thankful you can.

```python
import PySimpleGUI as sg

event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).Read()
```

![get filename](https://user-images.githubusercontent.com/13696193/44960039-f1018880-aec5-11e8-8a43-3d7f8ff93b67.jpg)


------

# Polishing Your Windows = Building "Beautiful Windows"

Your window does not have to look like the boring gray window used in the above example.

So many posts on Reddit asking which GUI is going to result in a "beautiful window", as if there's a magic GUI library that pretties things up for you.  

Beautiful windows are created, not simply given to you.  There are people that design and create artwork for user interfaces, you know that right?  Artists draw buttons, artwork that you include in the window to make it nicer.

These 2 windows are running on top of tkinter.  They've been polished and I'm sure they could be polished even further as I'm no artist nor UI expert.

![batterup2](https://user-images.githubusercontent.com/13696193/50378902-6aa2bb00-060a-11e9-8f2f-d746694fa4ee.gif)

![uno_final](https://user-images.githubusercontent.com/13696193/49945232-67952580-feba-11e8-90c8-7dc31c5f7c67.gif)

# Pi Windows

Perhaps you're looking for a way to interact with your **Raspberry Pi** in a more friendly way.  Your PySimpleGUI code will run on a Pi with no problem.  Tkinter is alive and well on the Pi platform.  The controls are a little cruder looking due to the size of the screen, etc.  You could add custom artwork, etc to make it look nicer.

This is simply an example of the many GUI Elements that are available to use on all platforms.

![raspberry pi everything demo](https://user-images.githubusercontent.com/13696193/44279694-5b58ce80-a220-11e8-9ab6-d6021f5a944f.jpg)

# Games

It's possible to create some cool games by simply using the built-in PySimpleGUI graphic primivites like those used in this game of pong.  PyGame can also be embedded into a PySimpleGUI window and code is provided to you demonstrating how.


![pong](https://user-images.githubusercontent.com/13696193/45860012-2d8d0b00-bd33-11e8-9efd-3eaf4c30f324.gif)


# Windows Programs That Look Like Windows Programs

Do you have the desire to share your code with other people in your department, or with friends and family?  Many of them may not have Python on their computer.  And in the corporate environment, it may not be possible for you to install Python on their computer.

`PySimpleGUI + PyInstaller` to the rescue!!

Combining PySimpleGUI with PyInstaller creates something truly remarkable and special, a Python program that looks like a Windows WinForms application.  

The application you see below with a working menu was created in 20 lines of Python code.  It is a single .EXE file that launches straight into the screen you see.  And more good news, the only icon you see on the taskbar is the window itself... there is no pesky shell window.  Nice, huh? 

![menu demo](https://user-images.githubusercontent.com/13696193/45923097-8fbc4c00-beaa-11e8-87d2-01a5331811c8.gif)


With a simple GUI, it becomes practical to "associate" .py files with the python interpreter on Windows.  Double click a py file and up pops a GUI window, a more pleasant experience than opening a dos Window and typing a command line.

# Background

Feel free to skip all this if you don't care to know the backstory and reasons behind decisions.

I was frustrated by having to deal with the dos prompt when I had a powerful Windows machine right in front of me.  Why is it SO difficult to do even the simplest of input/output to a window in Python??

There was a project looming and a GUI was needed.  Thus began a search for a simplified GUI package that would enable me to work with tkinter easier.  I found a few, and they were pretty popular too, but they lacked the full-compliment of Widgets and it was impossible to define my own window using those widgets.

A whacky idea came to mind... what if I wrote a simplified GUI and then used THAT to write my application.  It would be a lot less code and it would be "easy" to write my application then.

Thus PySimpleGUI was born out of necessity and it's been the necessity of others that have helped evolve it into the package it is today.  It would not be 1/2 as good without the help of the community.

Once PySimpleGUI was done, it was time to start working on "the ports".  And, of course, also this documentation.

## The Non-OO and Non-Event-Driven Model

How do you make a GUI interface easy enough for first year Python students?  Heck, first WEEK of Python was the actual goal and it still is. This meant classes could be used to build and use it, but classes can not be part of the code the user writes.  Of course, an OO design is quite possible to use with PySimpleGUI, but it's not a ***requirement***.  The sample code and docs stay away from writing new classes for the most part.

What about those pesky callbacks?  They're difficult for beginners to grasp and they're a bit of a pain in the ass to deal with.  The way PySimpleGUI got around events was to build a "message passing" architecture instead.  

Instead of a user function being called when there's some event, instead the information is "passed" to the user when they call the function `Window.Read()` Everything is returned through this call.  The callbacks still happen, but they all happen inside of PySimpleGUI where they are turned into messages to pass ot you.

In fact, all of the boilerplate, events, widgets, containers, frames, etc, are exactly the same ones that you would be writing if you wrote directly in tktiner, Qt, ....  The full complement of Widgets are available to you via PySimpleGUI Elements.  And those widgets are presented to you in a unique and fun way.

### The Result

A GUI that's appealing to a broad audience that is highly customizable, easy to program, and is solid with few bugs and rarely crashes (99% of the time it's some other error that causes a crash).

PySimpleGUI is becoming more and more popular. The number of installs and the number of successes grows daily.  Pip installs have exceeded 350,000 in the first year of existance.  Over 300 people a day visit the GitHub and the project has 1,800 stars (thank you aweesome users!)

The number of ports is up to 4.  The number of integrations with other technologies is constantly being expanded.  It's a great time to try PySimpleGUI!  You've got no more than 5 or 10 minutes to lose.


# Features

While simple to use, PySimpleGUI has significant depth to be explored by more advanced programmers.  The feature set goes way beyond the requirements of a beginner programmer, and into the  required features needed for complex GUIs.

For those of you that have heard PySimpleGUI is only good for doing the most simplest of GUIs, this feature list should put that myth to rest.  **The SIMPLE part of PySimpleGUI is how much effort _you_ expend to write a GUI.  Not the complexity of the program.**  It's literally "simple" to do... it is not limited to simple problems.

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

This one is difficult for me to define.  The code implementing PySimpleGUI isn't PEP8 compliant, but it is consistent.  The important thing was what the user saw and experienced while coding, NOT the choices for naming conventioned in the implementation code.

I ended up defining it as - attempt to use language constructs in a natural way and to exploit some of Python's interesting features.  Python's lists and optional parameters make PySimpleGUI work smoothly. 

- Windows are represented as Python lists of Elements (Term Widget reserved for the underlying GUI Frameworks' representation of the Element)
- A window is a list of rows, and a list of these rows is a window
- Return values are a list/dictionary of button presses and input values
- The SDK calls collapse down into a single line of Python code that presents a custom GUI and returns values should you want that extreme of a single-line soluition
- Elements are all classes. Users interact with elements using class methods but are not required to write their own classes
- Allow keys and other identifiers be any format you want
- While some disagree with the single source file, I find the benefits greatly outweigh the negatives

#### Lofty Goals

>  Change Python

The hope is not that ***this*** package will become part of the Python Standard Library.  The hope is that Python will become ***the*** go-to language for creating GUI programs that run on Windows, Mac, and Linux *for all levels of developer*.  Perhaps this sort of package is needed to make that happen.

> Capture Budding Graphic Designers

The hope is that beginners that are interested in graphic design, and are taking a Python course, will have an easy way to express themselves, right from the start of their Python experience.  Even if they're not the best programmers they will be able to show custom GUI layouts with ease.

> Fill the GUI Gap

There is a noticeable gap in the Python GUI solution.  Fill that gap and who knows what will happen.  At the moment, to make a tradiional GUI window using tkinter, Qt, WxPython and Remi, it takes much more than a week, or a month of Python education to use these GUI packages.  

They are out of reach of the beginners.  Often WAY out of reach.  And yet, time and time again, beginners that say they JUST STARTED with Python will ask on a Forum or Reddit for a GUI pacakage recommendation.  9 times out of 10 Qt is recommended.  (smacking head with hand).  What a waste of characters.  You might as well have just told them, "give up".

> Is There a There?

Maybe there's no "there there".  ***Or*** maybe a simple GUI API will enable Python to dominate yet another computing discipline like it has so many others.  This is one attempt to find out.  So far, it sure looks like there's PLENTY of demand in this area.


# Getting Started with PySimpleGUI

## Installing PySimpleGUI

Of course if you're installing for Qt, WxPython, Web, you'll use PySimpleGUIQt, PySimpleGUIWx, and PySimpleGUIWeb instead of straight PySimpleGUI in the instructions below.

### IDEs

Some IDEs provide virtual environments.  PyCharm is one example.  For these, you will either use their GUI interface to add packages or use their built-in terminal to do pip installs.

#### Officially Supported IDEs

A number of IDEs have **known problems with PySimpleGUI**.  IDLE, Spyder, and Thonny all have problems with intermittent or inconsistent results, especially when a program exits.  Any IDE that is based on tkinter is going to have issues with the straight PySimpleGUI port.


The official list of supported IDEs is:
1. PyCharm (or course this is THE IDE to use for use with PySimpleGUI)
2. Wing
3. Visual Studio



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

`pip install --upgrade PySimpleGUI27`
or
`pip2 install --upgrade PySimpleGUI27`

You may need to also install "future" for version 2.7

`pip install future`
or
`pip2 install future`

Python 2.7 support is relatively new and the bugs are still being worked out.  I'm unsure what may need to be done to install tkinter for Python 2.7.  Will update this readme when more info is available

Like above, you may have to install either pip or tkinter.  To do this on Python 2.7:

`sudo apt install python-pip`

`sudo apt install python-tkinter`

### Testing your installation and Troubleshooting

Once you have installed, or copied the .py file to your app folder, you can test the installation using python.  At the command prompt start up Python.

#### The Quick Test

From your commant line type:
`python -m PySimpleGUI`

Of course if you're on Linux/Mac and need to run using the command `python3` then of course type that.

This will display the same window as these instructions:


#### Instructions for Python 2.7:
```python
>>> import PySimpleGUI27
>>> PySimpleGUI27.main()
```

#### Instructions for Python 3:

```python3
>>> import PySimpleGUI
>>> PySimpleGUI.main()
```

You will see a "test harness" that exercises the SDK, tells you the version number, allows you to try 

### Finding Out Where Your PySimpleGUI Is Coming From

Sometimes when debugging, questions arise as to exactly which PySimpleGUI you are running.  The quick way to find this out is to again, run Python from the command line.  This time you'll type:


```python3
>>> import PySimpleGUI as sg
>>> sg
```

When you type sg, Python will tell you the full patch to your PySimpleGUI file / package.  This is critical information to know when debugging because it's really easy to forget you've got an old copy of PySimpleGUI laying around somewhere.

### Manual installation

If you're not connected to the net on your target machine, or pip isn't working, or you want to run the latest code from GitHub, then all you have to do is place the single PySimpleGUI source file `PySimpleGUI.py` (for tkinter port) and place it in your application's folder (the folder where the py file is that imports PySimpleGUI).  Your application will load that local copy of PySimpleGUI as if it were a package.

Be ***sure*** that you delete this PySimpleGUI.py file if you install a newer pip version.  Often the sequence of events is that a bug you've reported was fixed and checked into GitHub.  You download the PySimpleGUI.py file (or the appropriately named one for your port) and put with your app.  Then later your fix is posted with a new release on PyPI.  You'll want to delete the GitHub one before you install from pip.

### Prerequisites
Python 2.7 or Python 3
tkinter

PySimpleGUI Runs on all Python3 platforms that have tkinter running on them.  It has been tested on Windows, Mac, Linux, Raspberry Pi.  Even runs on `pypy3`.

### EXE file creation

If you wish to create an EXE from your PySimpleGUI application, you will need to install `PyInstaller`.  There are instructions on how to create an EXE at the bottom of this document.


## Using  - Python 3

To use in your code, simply import....
`import PySimpleGUI as sg`

Then use either "high level" API calls or build your own windows.

`sg.Popup('This is my first Popup')`

![first popup](https://user-images.githubusercontent.com/13696193/44957300-c7813680-ae9e-11e8-9a8c-c70198db7907.jpg)


Yes, it's just that easy to have a window appear on the screen using Python.  With PySimpleGUI, making a custom window appear isn't much more difficult.  The goal is to get you running on your GUI within ***minutes***, not hours nor days.

## Using  - Python 2.7

Those using Python 2.7 will import a different module name
`import PySimpleGUI27 as sg`

## Code to Automatically Import Correct Version

Many of the demo programs use this check to see which package to use:
```python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
```


This will automatically import the correct library based on the Python version number reported by the Python interpreter.


---

