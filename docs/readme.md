
<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Logo%20with%20text%20for%20GitHub%20Top.png" alt="Python GUIs for Humans">
  <h2 align="center">Python GUIs for Humans</h2>
</p>

Transforms the tkinter, Qt, WxPython, and Remi (browser-based) GUI frameworks into a simpler interface.  The window definition is simplified by using Python core data types understood by beginners (lists and dictionaries). Further simplification happens by changing event handling from a callback-based model to a message passing one.  

Your code is not _required_ to have an object oriented architecture which makes the package usable by a larger audience. While the architecture is simple to understand, it does not *necessarily* limit you to only simple problems.  

Some programs are not well-suited for PySimpleGUI however.  By definition, PySimpleGUI implements a subset of the underlying GUI frameworks' capabilities.  It's difficult to define exactly which programs are well suited for PySimpleGUI and which are not.  It depends on the details of your program.  Duplicating Excel in every detail is an example of something not well suited for PySimpleGUI.

[Japanese version of this readme](https://github.com/PySimpleGUI/PySimpleGUI/blob/master/readme.ja.md).

<a href="https://www.buymeacoffee.com/PySimpleGUI" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>

I could use a coffee!  It fuels consultants, editors, domain registration and so many other things required for PySimpleGUI to be a thriving project.


<hr>

# Statistics :chart_with_upwards_trend:

## PyPI Installs

<p align="center">
tkinter <img src="http://pepy.tech/badge/pysimplegui?color=blue&style=for-the-badge" width="100px">
tkinter 2.7 <img src="https://pepy.tech/badge/pysimplegui27?color=blue&style=for-the-badge"><br>
Qt <img src="https://pepy.tech/badge/pysimpleguiqt?color=blue&style=for-the-badge">
WxPython<img src="https://pepy.tech/badge/pysimpleguiwx?color=blue&style=for-the-badge">
Web (Remi) <img src="https://pepy.tech/badge/pysimpleguiweb?color=blue&style=for-the-badge">
</p>


## GitHub

<p align="center">
<a href=""><img src="https://img.shields.io/github/issues-raw/PySimpleGUI/PySimpleGUI?color=blue&style=for-the-badge" alt="img" width="180px"></a>
<a href=""><img src="https://img.shields.io/github/issues-closed-raw/PySimpleGUI/PySimpleGUI?color=blue&style=for-the-badge" alt="img"  width="200px"></a>
<a href=""><img src="https://img.shields.io/github/commit-activity/m/PySimpleGUI/PySimpleGUI.svg?color=blue&style=for-the-badge" alt="img"  width="260px"></a>
<a href=""><img src="https://img.shields.io/github/last-commit/PySimpleGUI/PySimpleGUI.svg?color=blue&style=for-the-badge" alt="img"width="200px"></a>
<a href=""><img src="http://ForTheBadge.com/images/badges/makes-people-smile.svg" alt="img"width="190px"></a>
<a href=""><img src="https://img.shields.io/github/stars/PySimpleGUI/PySimpleGUI.svg?style=social&label=Star&maxAge=2592000" alt="img"width="140x"></a>
</p>


<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/?username=PySimpleGUI&bg_color=3e7bac&title_color=ffdd55&icon_color=ffdd55&text_color=ffdd55&show_icons=true&count_private=true">
</p>

## Most Recent PyPI Version



<p align="center">
tkinter
<a href="pypi tkinter"><img src="https://img.shields.io/pypi/v/pysimplegui.svg?style=for-the-badge&color=red" alt="img" align="center" width="150px"></a>
Qt
<a href="https://img.shields.io/pypi/v/pysimpleguiqt.svg?style=for-the-badge"><img src="https://img.shields.io/pypi/v/pysimpleguiqt.svg?style=for-the-badge"  alt="img" align="center" width="150px"></a>
Web
<a href="https://img.shields.io/pypi/v/pysimpleguiweb.svg?style=for-the-badge"><img src="https://img.shields.io/pypi/v/pysimpleguiweb.svg?style=for-the-badge"  alt="img" align="center" width="150px"></a>
WxPython
<a href="https://img.shields.io/pypi/v/pysimpleguiwx.svg?style=for-the-badge"><img src="https://img.shields.io/pypi/v/pysimpleguiwx.svg?style=for-the-badge"  alt="img" align="center" width="150px"></a>

</p>

<hr>

# What Is PySimpleGUI :question:

PySimpleGUI is a Python package that enables Python programmers of all levels to create GUIs.  You specify your GUI window using a "layout" which contains widgets (they're called "Elements" in PySimpleGUI).  Your layout is used to create a window using one of the 4 supported frameworks to display and interact with your window.  Supported frameworks include tkinter, Qt, WxPython, or Remi. The term "wrapper" is sometimes used for these kinds of packages.

Your PySimpleGUI code is simpler and shorter than writing directly using the underlying framework because PySimpleGUI implements much of the "boilerplate code" for you.  Additionally, interfaces are simplified to require as little code as possible to get the desired result.  Depending on the program and framework used, a PySimpleGUI program may require 1/2 to 1/10th amount of code to create an identical window using one of the frameworks directly.

While the goal is to encapsulate/hide the specific objects and code used by the GUI framework you are running on top of, if needed you can access the frameworks' dependent widgets and windows directly. If a setting or feature is not yet exposed or accessible using the PySimpleGUI APIs, you are not walled off from the framework. You can expand capabilities without directly modifying the PySimpleGUI package itself.

## Bridging the "GUI Gap"

Python has brought a large number of people into the programming community. The number of programs and the range of areas it touches is mindboggling.  But more often than not, these and technologies are out of reach of all but a handful of people.  The majority of Python programs are "command line" based. This isn't a problem for programmer-types as we're all used to interacting with computers through a text interface.  While programmers don't have a problem with command-line interfaces, most "normal people" do.  This creates a digital divide, a "GUI Gap".

Adding a GUI to a program opens that program up to a wider audience. It becomes more approachable. GUIs can also make interacting with some programs easier, even for those that are comfortable with a command-line interface.  And finally, some problems require a GUI.  


<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/GUI%20Gap%202020.png" width="600px">
</p>


<hr>

# About Me :wave:

Hi there!  I'm Mike.  You'll find me right here, on the PySimpleGUI GitHub, solving problems and continuously pushing PySimpleGUI forward.  I've dedicated my days, nights, and weekends to the project and PySimpleGUI users.  Our successes are ultimately shared.  I'm successful when you're successful.  

While a relative newcomer to Python, I've been writing software since the 70s.  The majority of my career was spent creating products in Silicon Valley. I bring to PySimpleGUI the same professionalism and dedication as I did to the corporate products I developed. You are my customers now.


## Project Goals :goal_net:

Two of the more important goals of the PySimpleGUI project:

* Having fun
* Your success 

**Fun** as a goal on a serious project sounds odd, but it's a serious goal. I find writing these GUI programs to be a lot of fun. One reason is how little time it takes to write a complete solution. If we're not enjoying the process then someone's going to give up. 

There is a significant amount of documentation, a cookbook, 100's of demo programs to get you immediately running, a detailed call reference, YouTube videos, online Trinket demos, and more... all working to create... a fun experience.

**Your Success** is a shared goal.  PySimpleGUI was built for developers. You're my peeps. It's been an unexpected reward to see the results of the combined effort of users and PySimpleGUI. Use the documentation & other materials to help build your application.  If you run into trouble, help is available by opening on [Issue on the PySimpleGUI GitHub](http://Issues.PySimpleGUI.org).  Take a look at the section on Support below.

<hr>

# Educational Resources :books:

www.PySimpleGUI.org is easy to remember and is where the documentation is located. You'll find tabs across the top that represent several different documents. The documentation is located on "Read The Docs" so that there is a table of contents for each document and they are easy to search.

There are 100s of pages of written documentation and 100s of example programs that will help you be effective very quickly.  Rather than requiring days or weeks of investment to learn a single GUI package, you may be able to complete your project in a single afternoon when using PySimpleGUI.



## Example 1 - The One-Shot Window

This type of program is called a "one-shot" window because the window is displayed one time, the values collected, and then it is closed.  It doesn't remain open for a long time like you would in a Word Processor.

### Anatomy of a Simple PySimpleGUI Program

There are 5 sections to a PySimpleGUI program

```python
import PySimpleGUI as sg                        # Part 1 - The import

# Define the window's contents
layout = [  [sg.Text("What's your name?")],     # Part 2 - The Layout
            [sg.Input()],
            [sg.Button('Ok')] ]

# Create the window
window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion
                                                
# Display and interact with the Window
event, values = window.read()                   # Part 4 - Event loop or Window.read call

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()                                  # Part 5 - Close the Window
```

The code produces this window

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-tkinter.jpg">
</p>


<hr>

## Example 2 - Interactive Window

In this example, our window will remain on the screen until the user closes the window or clicks the Quit button.  The main difference between the one-shot window you saw earlier and an interactive window is the addition of an "Event Loop". The Event Loop reads events and inputs from your window.  The heart of your application lives in the event loop.


```python
import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()
```

This is the window that Example 2 produces.
<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Example2-1.jpg">
</p>



And here's what it looks like after you enter a value into the Input field and click the Ok button.
<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Example2-2.jpg">
</p>

Let's take a quick look at some of the differences between this example and the one-shot window.

First, you'll notice differences in the layout.  Two changes in particular are important.  One is the addition of the `key` parameter to the `Input` element and one of the `Text` elements.  A `key` is like a name for an element.  Or, in Python terms, it's like a dictionary key.  The `Input` element's key will be used as a dictionary key later in the code.

Another difference is the addition of this `Text` element:
```python
          [sg.Text(size=(40,1), key='-OUTPUT-')],
```

There are 2 parameters, the `key` we already covered.  The `size` parameter defines the size of the element in characters.  In this case, we're indicating that this `Text` element is 40 characters wide, by 1 character high.  Notice that there is no text string specified which means it'll be blank.  You can easily see this blank row in the window that's created.

We also added a button,  "Quit".

The Event Loop has our familiar `window.read()` call. 

Following the read is this if statement:
```python
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
```

This code is checking to see if the user closed the window by clicking the "X" or if they clicked the "Quit" button.  If either of these happens, then the code will break out of the event loop.

If the window wasn't closed nor the Quit button clicked, then execution continues.  The only thing that could have happened is the user clicked the "Ok" button.  The last statement in the Event Loop is this one:

```python
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")
```

This statement updates the `Text` element that has the key `-OUTPUT-` with a string.  `window['-OUTPUT-']` finds the element with the key `-OUTPUT-`.  That key belongs to our blank `Text` element.  Once that element is returned from the lookup, then its `update` method is called.  Nearly all elements have an `update` method.  This method is used to change the value of the element or to change some configuration of the element. 

If we wanted the text to be yellow, then that can be accomplished by adding a `text_color` parameter to the `update` method so that it reads:
```python
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI",
                              text_color='yellow')
```

After adding the `text_color` parameter this is our new resulting window:


<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Example2-3.jpg">
</p>


The parameters available for each element are documented in both the [call reference documentation](http://calls.PySimpleGUI.org) as well as the docstrings.  PySimpleGUI has extensive documentation to help you understand all of the options available to you. If you lookup the `update` method for the `Text` element, you'll find this definition for the call:


<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/TextUpdate.jpg">
</p>


As you can see several things can be changed for a `Text` element.  The call reference documentation is a valuable resource that will make programming in PySimpleGUI, uhm, simple.

<hr>

## Layouts Are Funny LOL! :laughing:

Your window's layout is a "list of lists" (LOL).  Windows are broken down into "rows".  Each row in your window becomes a list in your layout.  Concatenate together all of the lists and you've got a layout...a list of lists.

Here is the same layout as before with an extra `Text` element added to each row so that you can more easily see how rows are defined:

```python
layout = [  [sg.Text('Row 1'), sg.Text("What's your name?")],
            [sg.Text('Row 2'), sg.Input()],
            [sg.Text('Row 3'), sg.Button('Ok')] ]
```

Each row of this layout is a list of elements that will be displayed on that row in your window.


<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/layout-with-rows.jpg">
</p>



Using lists to define your GUI has some huge advantages over how GUI programming is done using other frameworks.  For example, you can use Python's list comprehension to create a grid of buttons in a single line of code.

These 3 lines of code:

```python
import PySimpleGUI as sg

layout = [[sg.Button(f'{row}, {col}') for col in range(4)] for row in range(4)]

event, values = sg.Window('List Comprehensions', layout).read(close=True)
```

produces this window which has a 4 x 4 grid of buttons:

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/4x4grid.jpg">
</p>

Recall how "fun" is one of the goals of the project.  It's fun to directly apply Python's powerful basic capabilities to GUI problems. Instead of pages of code to create a GUI, it's a few (or often 1) lines of code.

## Collapsing Code

It's possible to condense a window's code down to a single line of code.  The layout definition, window creation, display, and data collection can all be written in this line of code:

```python
event, values = sg.Window('Window Title', [[sg.Text("What's your name?")],[sg.Input()],[sg.Button('Ok')]]).read(close=True)
```

<p align="center">
  <img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-tkinter.jpg">
</p>


The same window is shown and returns the same values as the example showing the sections of a PySimpleGUI program.  Being able to do so much with so little enables you to quickly and easily add GUIs to your Python code.  If you want to display some data and get a choice from your user, it can be done in a line of code instead of a page of code.

By using short-hand aliases, you can save even more space in your code by using fewer characters.  All of the Elements have one or more shorter names that can be used.  For example, the `Text` element can be written simply as `T`. The `Input` element can be written as `I` and the `Button` as `B`.  Your single-line window code thus becomes:

```python
event, values = sg.Window('Window Title', [[sg.T("What's your name?")],[sg.I()],[sg.B('Ok')]]).read(close=True)
```


### Code Portability

PySimpleGUI is currently capable of running on 4 Python GUI Frameworks.  The framework to use is specified using the import statement.  Change the import and you'll change the underlying GUI framework.  For some programs, no other changes are needed than the import statement to run on a different GUI framework.  In the example above, changing the import from `PySimpleGUI` to `PySimpleGUIQt`, `PySimpleGUIWx`, `PySimpleGUIWeb` will change the framework.

| Import Statement | Resulting Window |
|--|--|
| PySimpleGUI |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-tkinter.jpg) |
| PySimpleGUIQt |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-Qt.jpg) |
| PySimpleGUIWx |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-WxPython.jpg) |
| PySimpleGUIWeb |  ![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ex1-Remi.jpg) |



Porting GUI code from one framework to another (e.g. moving your code from tkinter to Qt) usually requires a rewrite of your code.  PySimpleGUI is designed to enable you to enable easy movement between the frameworks.  Sometimes some changes are required of you, but the goal is to have highly portable code with minimal changes.  

Some features, like a System Tray Icon, are not available on all of the ports.  The System Tray Icon feature is available on the Qt and WxPython ports.  A simulated version is available on tkinter.  There is no support for a System Tray icon in the PySimpleGUIWeb port.

## Runtime Environments

| Environment | Supported |
|--|--|
| Python |  Python 3.4+ |
| Operating Systems | Windows, Linux, Mac |
| Hardware | Desktop PCs, Laptops, Raspberry Pi, Android devices running PyDroid3 |
| Online | repli.it, Trinket.com (both run tkinter in a browser) |
| GUI Frameworks | tkinter, pyside2, WxPython, Remi |


## Integrations

Among the more than 200 "Demo Programs" you'll find examples of how to integrate many popular Python packages into your GUI.

Want to embed a Matplotlib drawing into your window?  No problem, copy the demo code and instantly have a Matplotlib drawing of your dreams into your GUI.  

These packages and more are ready for you to put into your GUI as there are demo programs or a demo repo available for each:

 Package | Description |
|--|--|
 Matplotlib | Many types of graphs and plots |
 OpenCV | Computer Vision (often used for AI) |
 VLC | Video playback |
 pymunk | Physics engine|
 psutil | System environment statistics |
 prawn | Reddit API |
 json | PySimpleGUI wraps a special API to store "User Settings" |
 weather | Integrates with several weather APIs to make weather apps |
 mido | MIDI playback |
 beautiful soup | Web Scraping (GitHub issue watcher example) |

<hr>

# Installing :floppy_disk:

Two common ways of installing PySimpleGUI:

1. pip to install from PyPI
2. Download the file PySimpleGUI.py and place in your application's folder

### Pip Installing & Upgrading

The current suggested way of invoking the `pip` command is by running it as a module using Python.  Previously the command `pip` or `pip3` was directly onto a command-line / shell.  The suggested way 

Initial install for Windows:

`python -m pip install PySimpleGUI`

Initial install for Linux and MacOS:

`python3 -m pip install PySimpleGUI`

To upgrade using `pip` you simply 2 parameters to the line `--upgrade --no-cache-dir`.  

Upgrade installation on Windows:

`python -m pip install --upgrade --no-cache-dir PySimpleGUI`

Upgrade for Linux and MacOS:

`python3 -m pip install --upgrade --no-cache-dir PySimpleGUI`


### Single File Installing

PySimpleGUI was created as a single .py file so that it would be very easy for you to install it, even on systems that are not connected to the internet like a Raspberry Pi.  It's as simple as placing the PySimpleGUI.py file into the same folder as your application that imports it. Python will use your local copy when performing the import.

When installing using just the .py file, you can get it from either PyPI or if you want to run the most recent unreleased version then you'll download it from GitHub.

To install from PyPI, download either the wheel or the .gz file and unzip the file.  If you rename the .whl file to .zip you can open it just like any normal zip file.  You will find the PySimpleGUI.py file in one of the folders.  Copy this file to your application's folder and you're done.

The PyPI link for the tkinter version of PySimpleGUI is:
https://pypi.org/project/PySimpleGUI/#files

The GitHub repo's latest version can be found here:
https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/PySimpleGUI.py


Now some of you are thinking, "yea, but, wait, having a single huge source file is a terrible idea".  And, yea, *sometimes* it can be a terrible idea.  In this case, the benefits greatly outweighed the downside.  Lots of concepts in computer science are tradeoffs or subjective.  As much as some would like it to be, not everything is black and white.  Many times the answer to a question is "it depends".



## Galleries :art:

Work on a more formal gallery of user-submitted GUIs as well as those found on GitHub is underway but as of this writing is not complete.  There are currently 2 places you can go to see some screenshots in a centralized way.  Hopefully, a Wiki or other mechanism can be released soon to do justice to the awesome creations people are making.

### User Submitted Gallery

The first is a [user submitted screenshots issue](https://github.com/PySimpleGUI/PySimpleGUI/issues/10) located on the GitHub.  It's an informal way for people to show off what they've made.  It's not ideal, but it was a start.

### Massive Scraped GitHub Images

The second is a [massive gallery of over 3,000 images](https://www.dropbox.com/sh/g67ms0darox0i2p/AAAMrkIM6C64nwHLDkboCWnaa?dl=0) scraped from 1,000 projects on GitHub that are reportedly using PySimpleGUI.  It's not been hand-filtered and there are plenty of old screenshots that were used in the early documentation.  But, you may find something in there that sparks your imagination.

<hr>

# Uses for PySimpleGUI :hammer:

The following sections showcase a fraction of the uses for PySimpleGUI.  There are over 1,000 projects on GitHub alone that use PySimpleGUI.  It's truly amazing the possibilities that have opened up for so many people.  Many users have spoken about previously attempting to create a GUI in Python and failing, but finally achieving their dreams when they tried PySimpleGUI.

## Your First GUI

Of course one of the best uses of PySimpleGUI is getting you into making GUIs for your Python projects.  You can start as small as requesting a filename.  For this, you only need to make a single call to one of the "high-level functions" called `popup`.  There are all kinds of popups, some collect information.

`popup` but itself makes a window to display information.  You can pass multiple parameters just like a print.  If you want to get information, then you will call functions that start with `popup_get_` such as `popup_get_filename`.

Adding a single line to get a filename instead of specifying a filename on the command line can transform your program into one that "normal people" will feel comfortable using.





```python
import PySimpleGUI as sg

filename = sg.popup_get_file('Enter the file you wish to process')
sg.popup('You entered', filename)
```


This code will display 2 popup windows.  One to get the filename, which can be browsed to or pasted into the input box.  

<p align="center">
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/First_GUI1.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/First_GUI1.jpg"  alt="img" width="400px"></a>
</p>

The other window will output what is collected.

<p align="center">
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/First_GUI2.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/First_GUI2.jpg"  alt="img" width="175px"></a>

</p>


<br>

## Rainmeter-Style Windows

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/RainmeterStyleWidgets.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/RainmeterStyleWidgets.jpg"  alt="img" align="right" width="500px"></a>
The default settings for GUI frameworks don't tend to produce the nicest looking windows.  However, with some attention to detail, you can do several things to make windows look attractive.  PySimpleGUI makes it easier to manipulate colors and features like removing the title bar.  The result is windows that don't look like your typical tkinter windows.

Here is an example of how you can create windows that don't look like your typical tkinter in windows.  In this example, the windows have their titlebars removed.  The result is windows that look much like those found when using Rainmeter, a desktop widget program.

<br><br>
You can easily set the transparency of a window as well.  Here are more examples of desktop widgets in the same Rainmeter style.  Some are dimmed appearing because they are semi-transparent.
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/semi-transparent.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/semi-transparent.jpg"  alt="img" align="right" width="500px"></a>



Both of these effects, removing the titlebar and making a window semi-transparent, are achieved by setting 2 parameters when creating the window.  This is an example of how PySimpleGUI enables easy access to features.  And because PySimpleGUI code is portable across the GUI frameworks, these same parameters work for the other ports such as Qt.


Changing the Window creation call in Example 1 to this line of code produces a similar semi-transparent window:

```python
window = sg.Window('My window', layout, no_titlebar=True, alpha_channel=0.5)
```

## Games

While not specifically written as a game development SDK, PySimpleGUI makes the development of some games quite easy.

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Chess.png"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Chess.png"  alt="img" align="right" width="500px"></a>
This Chess program not only plays chess, but it integrates with the Stockfish chess-playing AI.

<br><br><br><br><br><br><br><br><br>
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Minesweeper.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Minesweeper.gif"  alt="img" align="right" width="500px"></a>
Several variants of Minesweeper have been released by users.

<br><br><br><br>
<br><br><br><br><br>

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/minesweeper_israel_dryer.png"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/minesweeper_israel_dryer.png"  alt="img" align="right" width="500px"></a>
<br><br><br><br><br><br><br><br><br><br>


<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Solitaire.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Solitaire.gif"  alt="img" align="right" width="500px"></a>
<br><br>
Card games work well with PySimpleGUI as manipulating images is simple when using the PySimpleGUI `Graph` element.

While not specifically written as a game development SDK, PySimpleGUI makes development of some games quite easy.
<br><br>
<br><br>
<br><br><br>


## Media Capture and Playback

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/OpenCV.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/OpenCV.jpg"  alt="img" align="right" width="400px"></a>


Capturing and displaying video from your webcam in a GUI is 4 lines of PySimpleGUI code.  Even more impressive is that these 4 lines of code work with the tkinter, Qt, and Web ports.  You can display your webcam, in realtime, in a browser using the same code that displays the image using tkinter.


Media playback, audio and video, can also be achieved using the VLC player.  A demo application is provided to you so that you have a working example to start from. Everything you see in this readme is available to you as a starting point for your own creations.
<br><br><br><br><br>
<br><br><br><br><br>
<br><br>
## Artificial Intelligence


<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO_GIF.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO_GIF.gif"  alt="img" align="right" width="500px"></a>



AI and Python have long been a recognized superpower when the two are paired together. What's often missing however is a way for users to interact with these AI algorithms familiarly, using a GUI.

These YOLO demos are a great example of how a GUI can make a tremendous difference in interacting with AI algorithms.  Notice two sliders at the bottom of these windows.  These 2 sliders change a couple of the parameters used by the YOLO algorithm.  

If you were tuning your YOLO demo using only the command line, you would need to set the parameters, once, when you launch the application, see how they perform, stop the application, change the parameters, and finally restart the application with the new parameters.
<br><br><br><br>

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO%20Object%20Detection.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/YOLO%20Object%20Detection.jpg"  alt="img" align="right" width="500px"></a>

Contrast those steps against what can be done using a GUI.  A GUI enables you to modify these parameters in real-time.  You can immediately get feedback on how they are affecting the algorithm.



<br><br><br><br><br>
<br><br>
<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Colorizer.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Colorizer.jpg"  alt="img" align="right" width="500px"></a>


There are SO many AI programs that have been published that are command-line driven.  This in itself isn't a huge hurdle, but it's enough of a "pain in the ass" to type/paste the filename you want to colorize on the command line, run the program, then open the resulting output file in a file viewer.


GUIs have the power to **change the user experience**, to fill the "GUI Gap".  With this colorizer example, the user only needs to supply a folder full of images, and then click on an image to both colorize and display the result.  

The program/algorithm to do the colorization was freely available, ready to use.  What was missing is the ease of use that a GUI could bring.


<hr>

## Graphing

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/CPU%20Cores%20Dashboard%202.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/CPU%20Cores%20Dashboard%202.gif"  alt="img" align="right" width="500px"></a>

Displaying and interacting with data in a GUI is simple with PySimpleGUI.  You have several options.  

You can use the built-in drawing/graphing capabilities to produce custom graphs.  This CPU usage monitor uses the `Graph` element
<br><br>
<br><br>
<br><br>

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Matplotlib.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Matplotlib.jpg"  alt="img" align="right" width="500px"></a>


Matplotlib is a popular choice with Python users.  PySimpleGUI can enable you to embed Matplotlib graphs directly into your GUI window.  You can even embed the interactive controls into your window if you want to retain the Matplotlib interactive features.

<br><br>
<br><br>
<br><br>
<br><br>

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Matplotlib2.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Matplotlib2.jpg"  alt="img" align="right" width="500px"></a>
Using PySimpleGUI's color themes, you can produce graphs that are a notch above default graphs most people create in Matplotlib.


<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>
<br><br>

<hr>

## Front-ends


<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/JumpCutter.png"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/JumpCutter.png"  alt="img" align="right" width="500px"></a>

The "GUI Gap" mentioned earlier can be easily solved using PySimpleGUI.  You don't even need to have the source code to the program you wish to add a GUI onto.  A "front-end" GUI is one that collects information that is then passed to a command-line application.  

Front-end GUIs are a fantastic way for a programmer to distribute an application that users were reluctant to use previously because they didn't feel comfortable using a command-line interface.  These GUIs are your only choice for command-line programs that you don't have access to the source code for.

This example is a front-end for a program called "Jump Cutter".  The parameters are collected via the GUI, a command-line is constructed using those parameters, and then the command is executed with the output from the command-line program being routed to the GUI interface.  In this example, you can see in yellow the command that was executed.
<br><br>
<hr>

## Raspberry Pi

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Raspberry%20Pi.jpg"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Raspberry%20Pi.jpg"  alt="img" align="right" width="500px"></a>


Because PySimpleGUI is compatible back to Python 3.4 it is capable of creating a GUI for your Raspberry Pi projects.  It works particularly well when paired with a touchscreen.  You can also use PySimpleGUIWeb to control your Pi if it doesn't have a monitor attached.

<br><br>
<br><br>
<br><br>
<br><br><br>
<hr>

## Easy Access to Advanced Features

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Customized%20Titlebar.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Customized%20Titlebar.gif"  alt="img" align="right" width="500px"></a>


Because it's very easy to access many of the underlying GUI frameworks' features, it's possible to piece together capabilities to create applications that look nothing like those produced using the GUI framework directly.

For example, it's not possible to change the color/look-and-feel of a titlebar using tkinter or the other GUI packages, but with PySimpleGUI it's easy to create windows that appear as if they have a custom titlebar.
<br><br><br>

<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Desktop%20Bouncing%20Balls.gif"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Desktop%20Bouncing%20Balls.gif"  alt="img" align="right" width="500px"></a>

Unbelievably, this window is using tkinter to achieve what appears to be something like a screensaver.


On windows, tkinter can completely remove the background from your application.  Once again, PySimpleGUI makes accessing these capabilities trivial.  Creating a transparent window requires adding a single parameter to the call that creates your `Window`.  One parameter change can result in a simple application with this effect:


You can interact with everything on your desktop, clicking through a full-screen window.

<hr>

# Themes

Tired of the default grey GUIs?  PySimpleGUI makes it trivial for your window to look nice by making a single call to the `theme` function.  There are over 150 different color themes available for you to choose:
<p align="center">
<a href=""><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/ThemePreview.jpg"  alt="img" width="900px"></a>
</p>


With most GUI frameworks, you must specify the color for every widget you create.  PySimpleGUI takes this chore from you and will automatically color the Elements to match your chosen theme.

To use a theme, call the `theme` function with the name of the theme before creating your window. You can add spaces for readability.  To set the theme to "Dark Grey 9":

```python
import PySimpleGUI as sg

sg.theme('dark grey 9')
```

This single line of code changes the window's appearance entirely:

<p align="center">
<a href=""><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/DarkGrey.jpg"  alt="img" width="400px"></a>
</p>


The theme changed colors of the background, text, input background, input text, and button colors.  In other GUI packages to change color schemes like this, you would need to specify the colors of each widget individually, requiring numerous changes to your code.

<hr>

# Support :muscle:

Your first stop should be the [documentation](http://www.PySimpleGUI.org) and [demo programs](http://Demos.PySimpleGUI.org).  If you still have a question or need help...  no problem... help is available to you, at no cost. Simply [file an Issue](http://Issues.PySimpleGUI.org) on the PySimpleGUI GitHub repo and you'll get help.  

Nearly all software companies have a form that accompanies bug reports.  It's not a bad trade... fill in the form, get free software support.  This information helps get you an answer efficiently.

In addition to requesting information such as the version numbers of PySimpleGUI and underlying GUI frameworks, you're also given a checklist of items that may help you solve your problem.

***Please fill in the form.***  It may feel pointless to you.  It may feel painful, despite it taking just a moment.  It helps get you a solution faster.  If it wasn't useful and necessary information to help you get a speedy reply and fix, you wouldn't be asked to fill it out.  "Help me help you".


# Supporting 	<a href="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/PSGSuperHero.png"><img src="https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/PSGSuperHero.png"  alt="img"  width="90px"></a>

Financial support for the project is greatly appreciated.  To be honest, financial help is needed.  It's expensive just keeping the lights on.  The domain name registrations, a long list of subscriptions for things like Trinket, consulting help, etc., quickly add up to a sizable recurring cost.  

PySimpleGUI wasn't inexpensive to create. While a labor of love, it was very laborious. It's required over 2 years of working 7-days a week to get the software and documentation to the level you see today.

PySimpleGUI has an open-source license and it would be great if it could remain that way.  If you or your company (especially if you're using PySimpleGUI in a company) are benefiting financially by using PySimpleGUI, you have the capability of extending the life of the project for you and other users.

### Buy Me A Coffee

Buy Me a Coffee is a great way to publicly support developers.  It's quick, easy, and your contribution is recorded so that others can see that you're a supporter of PySimpleGUI.  You can also choose to make your donation private.

<a href="https://www.buymeacoffee.com/PySimpleGUI" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>



### GitHub Sponsoring



<a href="https://github.com/sponsors/PySimpleGUI" target="_blank"><img src="https://img.shields.io/static/v1?label=Sponsor&message=%E2%9D%A4&logo=GitHub&link=%3Curl%3E&color=f88379"></a>

The [GitHub recurring sponsorship](https://github.com/sponsors/PySimpleGUI) is how you can sponsor the project at varying levels of support on an ongoing basis.  It's how many Open Source developers are able to receive corporate level sponsorship.

Your help in financially contributing to the project would be greatly appreciated. Being an Open Source developer is financially challenging.  YouTube video creators are able to make a living creating videos.  It's not so easy yet for Open Source developers.


# Funding - Your help is needed

A frank discussion is needed here.  Subtle hasn't worked.

The financial part of Open Source development is not openly discussed often.  As an Open Source developer, there is no automatic form of incoming happening, especially with Python where the source code essentially has to be provided.  Creating and administrating a Commercial License is expensive.  It's a big hurdle to take a project from an Open Source License to a Commercial License.  The attorneys I've spoken with haven't heard of it happening successfully.  So, licensing is not a practical option.

It's expensive to operate an active Open Source project.  The labor involved is massive.  How does it get paid for?  Well, it comes from the developer is how.  Just like YouTube creators have expenses for camera equipment and time making their content and need supporters in order to operate, so do Open Source developers.

PySimpleGUI needs your help.  Without some kind of funding, this project will end, likely sooner than later.  The individuals with the most ability to make a financial contribution are Corporate Users.  It's not tremendously difficult nor does it pose a financial hardship on someone working for a company to make a donation to PySimpleGUI.  You're spending someone else's money.  If you get a paycheck from a corporation and you're using PySimpleGUI, you're a "corporate user".  It doesn't matter if PySimpleGUI is shipping in a product you sell.  Your company is benefitting by running PySimpleGUI.  If it wasn't, you wouldn't be using it.  The person at your company that can help the PySimpleGUI effort is you, the user.  Your CFO isn't going to automatically make a payment.  Your legal team isn't on the lookout for Open Source projects to help.  I've not struck licensing deals with your company, or any company.  It's you, the end user that is the person at your company that will need to take action and has the ability to help the project continue.

This PySimpleGUI software isn't the output from an AI bot.  Nor is the support for users that are using it.  There's a software developer (with a help from some very kind, friendly, generous people) that's doing all this work.  I do it because I love creating and enabling people to do cool things. But that love doesn't pay bills.  The energy put into the project doesn't create electricity.  I make stuff, electricity isn't one of them.

Patreon works well for YouTubers.  It typically fails miserably for developers.  But there are multiple mechanisms available including PayPal, GitHub sponsorship, and BuyMeACoffee.  They all work pretty well and take 2 minutes, if that. One thing it requires is action on the part of the PySimpleGUI user.  If you can't afford to help, it's OK.  Use the software for free.  Make cool stuff.  Make the world a better, easier to use place.  If you can afford to help, please consider donating to the project.  It's for a good cause. 

To everyone that's helped, in whatever fashion, I'm very very grateful. And thanks to everyone that takes a moment to say "thank you", it's a small price to pay and adds to the project's momentum.



# Contributing  :construction_worker:

While PySimpleGUI is currently licensed under an open-source license, the project itself is structured like a proprietary product.  Pull Requests are not accepted.

One of the best ways for you to contribute code is to write and publish applications.  Users are inspired by seeing what other users build.  Create a GitHub repo from, post the code, and include a screenshot in your repo's readme file.  

If there is a feature missing that you need or you have an enhancement to suggest, then [open an Issue](https://github.com/PySimpleGUI/PySimpleGUI/issues/new?assignees=&labels=&template=issue-form---must-fill-in-this-form-with-every-new-issue-submitted.md&title=%5B+Enhancement%2FBug%2FQuestion%5D+My+problem+is...)


# Special Thanks :pray:

This version of the PySimpleGUI readme wouldn't have come together without the help from [@M4cs](https://github.com/M4cs). He's a fantastic developer and has been a PySimpleGUI supporter since the project's launch.   [@israel-dryer](https://github.com/israel-dryer) is another long-term supporter and has written several PySimpleGUI programs that pushed the envelope of the package's capabilities.  The unique minesweeper that uses an image for the board was created by Israel.  [@jason990420](https://github.com/jason990420) surprised many when he published the first card game using PySimpleGUI that you see pictured above as well as the first minesweeper game made with PySimpleGUI.  The Japanese version of the readme was greatly improved with help from  [@okajun35](https://github.com/okajun35). [@nngogol](https://github.com/nngogol) has had a very large impact on the project, also getting involved with PySimpleGUI in the first year of initial release.  He wrote a designer, came up with the familiar window[key] lookup syntax, wrote the tools that create the documentation, designed the first set of doc strings as well as tools that generate the online documenation using the PySimpleGUI code itself.  PySimpleGUI would not be where it is today were it not for the help of these individuals.

The more than 2,200 GitHub repos that use PySimpleGUI are owed a "Thank You" as well, for it is *you* that has been the inspiration that fuels this project's engine.  

The overseas users that post on Twitter overnight are the spark that starts the day's work on PySimpleGUI. They've been a source of positive energy that gets the development engine started and ready to run every day. As a token of appreciation, this readme file has been translated into [Japanese](https://github.com/PySimpleGUI/PySimpleGUI/blob/master/readme.ja.md).

You've all been the best user community an Open Source developer could hope for.

&copy; Copyright 2021 PySimpleGUI