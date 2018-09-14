

![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)

[![Downloads](http://pepy.tech/badge/pysimplegui)](http://pepy.tech/project/pysimplegui)  since Jul 11, 2018

![Documentation Status](https://readthedocs.org/projects/pysimplegui/badge/?version=latest)

[![Python Version](https://img.shields.io/badge/Python-3-brightgreen.svg)](https://www.python.org/downloads/)


# PySimpleGUI

  (Ver 3.2.0)



[Wiki for the latest news](https://github.com/MikeTheWatchGuy/PySimpleGUI/wiki)

[Formatted ReadTheDocs Version of this Readme](http://pysimplegui.readthedocs.io/)

[COOKBOOK!](https://pysimplegui.readthedocs.io/en/latest/cookbook/)

[Brief Tutorial](https://pysimplegui.readthedocs.io/en/latest/tutorial/)

[Latest Demos and Master Branch on GitHub](https://github.com/MikeTheWatchGuy/PySimpleGUI)

Super-simple GUI to grasp... Powerfully customizable.

Create a custom GUI in 5 lines of code.

Can create a custom GUI in 1 line of code if desired.

Note - ***Python3*** is required to run PySimpleGUI.  It takes advantage of some Python3 features that do not translate well into Python2.

Looking to take your Python code from the world of command lines and into the convenience of a GUI?  Have a Raspberry **Pi** with a touchscreen that's going to waste because you don't have the time to learn a GUI SDK?  Into Machine Learning and are sick of the command line?  Look no further, **you've found your GUI package**.

    import PySimpleGUI as sg

    sg.Popup('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')


![hello world](https://user-images.githubusercontent.com/13696193/44960047-1f7f6380-aec6-11e8-9d5e-12ef935bcade.jpg)


Or how about a ***custom GUI*** in 1 line of code?

    import PySimpleGUI as sg

    button, (filename,) = sg.FlexForm('Get filename example'). LayoutAndRead([[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ])

![get filename](https://user-images.githubusercontent.com/13696193/44960039-f1018880-aec5-11e8-8a43-3d7f8ff93b67.jpg)


  Build beautiful customized forms that fit your specific problem.  Let PySimpleGUI solve your GUI problem while you solve your real problems.   Look through the Cookbook, find a matching recipe, copy, paste and be up and running with a GUI in minutes.  This is the process PySimpleGUI was designed to work within.


![borderless grayed buttons](https://user-images.githubusercontent.com/13696193/45168664-d848e980-b1c9-11e8-886e-63279ae4017f.jpg)



PySimpleGUI wraps tkinter so that you get all the same widgets as you would tkinter, but you interact with them in a more friendly way.  It does the layout and boilerplate code for you and presents you with a simple, efficient interface.

![everything dark theme](https://user-images.githubusercontent.com/13696193/44959854-b1d23800-aec3-11e8-90b6-5af915a86d15.jpg)

Perhaps you're looking for a way to interact with your **Raspberry Pi** in a more friendly way.  The same for shown as on Pi (roughly the same)

![raspberry pi everything demo](https://user-images.githubusercontent.com/13696193/44279694-5b58ce80-a220-11e8-9ab6-d6021f5a944f.jpg)



In addition to a primary GUI, you can add a Progress Meter to your code with ONE LINE of code.  Slide this into any of your `for` loops and get a nice meter like this:

    EasyProgressMeter('My meter title', current_value, max value)

  ![easyprogressmeter](https://user-images.githubusercontent.com/13696193/44960065-83099100-aec6-11e8-8aa8-96e4b100a0e4.jpg)

You can build an async media player GUI with custom buttons in 30 lines of code.

![media player 2](https://user-images.githubusercontent.com/13696193/44960091-eeebf980-aec6-11e8-884e-80d4447a83cd.jpg)


  ## Background
I was frustrated by having to deal with the dos prompt when I had a powerful Windows machine right in front of me.  Why is it SO difficult to do even the simplest of input/output to a window in Python??

There are a number of 'easy to use' Python GUIs, but they're **very** limiting.  PySimpleGUI takes the best of packages like `EasyGUI`and `WxSimpleGUI` , both really handy but limited, and adds the ability to define your own layouts.   This ability to make your own forms is the  primary difference between these and `PySimpleGUI`.

Every call has optional parameters so that you can change the look and feel.  Don't like the button color? It's easy to change by adding a button_color parameter to your widget.  The configure is done in-place.

With a simple GUI, it becomes practical to "associate" .py files with the python interpreter on Windows.  Double click a py file and up pops a GUI window, a more pleasant experience than opening a dos Window and typing a command line.

The `PySimpleGUI` package is focused on the ***developer***.  Create a custom GUI with as little and as simple code as possible.  This was the primary mantra used to create PySimpleGUI.  "Do it in a Python-like way" was the second desired outcome.

## Features

    Features of PySimpleGUI include:
        Text
        Single Line Input
        Buttons including these types:
            File Browse
            Files Browse
            Folder Browse
            SaveAs
            Non-closing return
            Close form
            Realtime
            Calendar chooser
        Checkboxes
        Radio Buttons
        Listbox
        Slider
        Icons
        Multi-line Text Input
        Scroll-able Output
        Images
        Progress Bar
        Calendar chooser
        Async/Non-Blocking Windows
        Tabbed forms
        Persistent Windows
        Redirect Python Output/Errors to scrolling window
        'Higher level' APIs (e.g. MessageBox, YesNobox, ...)
        Single-Line-Of-Code Proress Bar & Debug Print
        Complete control of colors, look and feel
        Selection of pre-defined palettes
        Button images
        Return values as dictionary
        Set focus
        Bind return key to buttons
        Group widgets into a column and place into form anywhere
        Scrollable columns
        Keyboard low-level key capture
        Mouse scroll-wheel support
        Get Listbox values as they are selected
        Get slider, spinner, combo as they are changed
        Update elements in a live form
        Bulk form-fill operation
        Save / Load form to/from disk
        Borderless (no titlebar) windows
        Always on top windows
        Menus
        No async programming required (no callbacks to worry about)


An example of many widgets used on a single form.  A little further down you'll find the TWENTY lines of code required to create this complex form.  Try it if you don't believe it.  Start Python, copy and paste the code below into the >>> prompt and hit enter. This will pop up...

![everything example](https://user-images.githubusercontent.com/13696193/43097412-0a4652aa-8e8a-11e8-8e09-939484e3c568.jpg)

Here is the code that produced the above screenshot.

    import PySimpleGUI as sg

    with sg.FlexForm('Everything bagel', auto_size_text=True, default_element_size=(40, 1)) as form:
        layout = [
            [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
            [sg.Text('Here is some text.... and a place to enter text')],
            [sg.InputText()],
            [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],
            [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
            [sg.Multiline(default_text='This is the default Text shoulsd you decide not to type anything',
                          scale=(2, 10))],
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
            [sg.Submit(), sg.Cancel(), sg.SimpleButton('Customized', button_color=('white', 'green'))]
        ]

        button, values = form.LayoutAndRead(layout)

 **A note on screen shots**
You will see a number of different styles of buttons, data entry fields, etc, in this readme. They were all made with the same SDK, the only difference is in the settings that are specified on a per-element, row, form, or global basis.  One setting in particular, border_width, can make a big difference on the look of the form.  Some of the screenshots had a border_width of 6, others a value of 1.


---
### Design Goals

> Copy, Paste, Run.

`PySimpleGUI's` goal with the API is to be easy on the programmer, and to function in a Python-like way. Since GUIs are visual, it was desirable for the code to visually match what's on the screen.

  > Be Pythonic

 Be Pythonic... Attempted to use language constructs in a natural way and to exploit some of Python's interesting features.  Python's lists and optional parameters make PySimpleGUI work.

 - Forms are represented as Python lists.
    - A form is a list of rows
   - A row is a list of elements
- Return values are a list of button presses and input values.
- Return values can also be represented as a dictionary
- The SDK calls collapse down into a single line of Python code that presents a custom GUI and returns values
-  Linear programming instead of callbacks




  -----
## Getting Started with PySimpleGUI

### Installing

    pip install --upgrade PySimpleGUI

On some systems you need to run pip3.

    pip3 install --upgrade PySimpleGUI

On a Raspberry Pi, this is should work:

    sudo pip3 install --upgrade pysimplegui

Some users have found that upgrading required using an extra flag on the pip `--no-cache-dir` and you can force the version number too by adding `==version` onto the end

    pip install --upgrade --no-cache-dir PySimpleGUI==3.0.3


If for some reason you are unable to install using `pip`, don't worry, you can still import PySimpleGUI by downloading the file PySimleGUI.py and placing it in your folder along with the application that is importing it.

`tkinter` is a requirement for PySimpleGUI (the only requirement).  Some OS variants, such as Ubuntu, do not some with `tkinter` already installed.  If you get an error similar to:
```
ImportError: No module named tkinter
```
then you need to install `tkinter`.  Be sure and get the Python 3 version.
```
sudo apt-get install python3-tk
```



### Prerequisites

Python 3
tkinter

Runs on all Python platforms that have tkinter running on them.  Thoroughly tested on Windows.  Runs on Windows, Mac, Linux, Raspberry Pi.  Even runs on `pypy3`.

### Using

To use in your code, simply import....
 `import PySimpleGUI as sg`

Then use either "high level" API calls or build your own forms.

    sg.Popup('This is my first Popup')

![first popup](https://user-images.githubusercontent.com/13696193/44957300-c7813680-ae9e-11e8-9a8c-c70198db7907.jpg)


Yes, it's just that easy to have a window appear on the screen using Python.  With PySimpleGUI, making a custom form appear isn't much more difficult.  The goal is to get you running on your GUI within ***minutes***, not hours nor days.

---
## APIs

PySimpleGUI can be broken down into 2 types of API's:
 * High Level single call functions    (The `Popup` calls)
 * Custom form functions


### Python Language Features

 There are a number of Python language features that PySimpleGUI utilizes heavily for API access that should be understood...
 * Variable number of arguments to a function call
 * Optional parameters to a function call

#### Variable Number of Arguments

 The "High Level" API calls that *output* values take a variable number of arguments so that they match a "print" statement as much as possible.  The idea is to make it simple for the programmer to output as many items as desired and in any format.  The user need not convert the variables to be output into the strings.  The PySimpleGUI functions do that for the user.

    sg.Popup('Variable number of parameters example', var1, var2, "etc")

Each new item begins on a new line in the Popup

  ![snap0179](https://user-images.githubusercontent.com/13696193/43658129-f6ca49c6-9725-11e8-9317-1f77443eb04a.jpg)



#### Optional Parameters to a Function Call

This feature of the Python language is utilized ***heavily*** as a method of customizing forms and form Elements.  Rather than requiring the programmer to specify every possible option for a widget, instead only the options the caller wants to override are specified.

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


---

### High Level API Calls  - Popup's

"High level calls" are those that start with "Popup".    They are the most basic form of communications with the user.   They are named after the type of window they create, a pop-up window.  These windows are meant to be short lived while, either delivering information or collecting it, and then quickly disappearing.

### Popup Output

Think of the `Popup` call as the GUI equivelent of a  `print` statement.  It's your way of displaying results to a user in the windowed world.  Each call to Popup will create a new Popup window.

`Popup` calls are normally blocking.  your program will stop executing until the user has closed the Popup window.  A non-blocking form of Popup discussed in the async section.

Just like a print statement, you can pass any number of arguments you wish.  They will all be turned into strings and displayed in the popup window.

There are a number of Popup output calls, each with a slightly different look (e.g. different button labels).

The list of Popup output functions are

    Popup,PopupOk
    PopupYesNo
    PopupCancel
    PopupOkCancel
    PopupError
    PopupTimed, PopupAutoClose

The trailing portion of the function name after Popup indicates what buttons are shown.  `PopupYesNo` shows a pair of button with Yes and No on them.   `PopupCancel` has a Cancel button, etc.

While these are "output" windows, they do collect input in the form of buttons.  The Popup functions return the button that was clicked.  If the Ok button was clicked, then Popup returns the string 'Ok'.  If the user clicked the X button to close the window, then the button value returned is `None`.

The function `PopupTimed` or `PopupAutoClose` are popup windows that will automatically close after come period of time.

Here is a quick-reference showing how the Popup calls look.


    sg.Popup('Popup')
    sg.PopupOk('PopupOk')
    sg.PopupYesNo('PopupYesNo')
    sg.PopupCancel('PopupCancel')
    sg.PopupOkCancel('PopupOkCancel')
    sg.PopupError('PopupError')
    sg.PopupTimed('PopupTimed')
    sg.PopupAutoClose('PopupAutoClose')



![snap0256](https://user-images.githubusercontent.com/13696193/44957394-1380ab00-aea0-11e8-98b1-1ab7d7bd5b37.jpg)

![snap0257](https://user-images.githubusercontent.com/13696193/44957400-167b9b80-aea0-11e8-9d42-2314f24e62de.jpg)

![snap0258](https://user-images.githubusercontent.com/13696193/44957399-154a6e80-aea0-11e8-9580-e716f839d400.jpg)

![snap0259](https://user-images.githubusercontent.com/13696193/44957398-14b1d800-aea0-11e8-9e88-c2b36a248447.jpg)

![snap0260](https://user-images.githubusercontent.com/13696193/44957397-14b1d800-aea0-11e8-950b-6d0b4f33841a.jpg)

![snap0261](https://user-images.githubusercontent.com/13696193/44957396-14194180-aea0-11e8-8eef-bb2e1193ecfa.jpg)

![snap0264](https://user-images.githubusercontent.com/13696193/44957595-9e15da00-aea1-11e8-8909-6b6121b74509.jpg)

#### Scrolled Output
There is a scrolled version of Popups should you have a lot of information to display.

    sg.PopupScrolled(my_text)

![scrolledtextbox 2](https://user-images.githubusercontent.com/13696193/43667324-712aa0d4-9745-11e8-83a9-a0d0570d0865.jpg)


The `PopupScrolled` will auto-fit the window size to the size of the text.  Specify `None` in the height field of a `size` parameter to get auto-sized height.

This call will create a scrolled box 80 characters wide and a height dependent upon the number of lines of text.

sg.PopupScrolled(my_text, size=(80, None))

Note that the default max number of lines before scrolling happens is set to 50. At 50 lines the scrolling will begin.

### Popup Input

There are Popup calls for single-item inputs. These follow the pattern of `Popup` followed by `Get` and then the type of item to get.

 - `PopupGetString` - get a single line of text
 - `PopupGetFile` - get a filename
 - `PopupGetFolder` - get a folder name

Rather than make  a custom form to get one data value, call the Popup input function to get the item from the user.


    import PySimpleGUI as sg

    text = sg.PopupGetText('Title', 'Please input something')
    sg.Popup('Results', 'The value returned from PopupGetText', text)

  ![popupgettext](https://user-images.githubusercontent.com/13696193/44957281-8721b880-ae9e-11e8-98cd-d06369f4187e.jpg)

![popup gettext response](https://user-images.githubusercontent.com/13696193/44957282-8721b880-ae9e-11e8-84ae-dc8bb30504a0.jpg)


    text = sg.PopupGetFile('Please enter a file name')
    sg.Popup('Results', 'The value returned from PopupGetFile', text)

![popupgetfile](https://user-images.githubusercontent.com/13696193/44957857-2fd31680-aea5-11e8-8eb7-f6b91c202cc8.jpg)

The window created to get a folder name looks the same as the get a file name.  The difference is in what the browse button does.  `PopupGetFile` shows an Open File dialog box while `PopupGetFolder`  shows an Open Folder dialog box.

    text = sg.PopupGetFolder('Please enter a folder name')
    sg.Popup('Results', 'The value returned from PopupGetFolder', text)

![popupgetfolder](https://user-images.githubusercontent.com/13696193/44957861-45484080-aea5-11e8-926c-cf607a45251c.jpg)

#### Progress Meter!
We all have loops in our code.  'Isn't it joyful waiting, watching a counter scrolling past in a text window?  How about one line of code to get a progress meter, that contains statistics about your code?


    EasyProgressMeter(title,
                      current_value,
                      max_value,
                      *args,
                      orientation=None,
                      bar_color=DEFAULT_PROGRESS_BAR_COLOR,
                      button_color=None,
                      size=DEFAULT_PROGRESS_BAR_SIZE,
                      scale=(None, None),
                      border_width=DEFAULT_PROGRESS_BAR_BORDER_WIDTH):

Here's the one-line Progress Meter in action!

    for i in range(1,10000):
        sg.EasyProgressMeter('My Meter', i+1, 10000, 'Optional message')

That line of code resulted in this window popping up and updating.

![preogress meter](https://user-images.githubusercontent.com/13696193/43667625-d47da702-9746-11e8-91e6-e5177883abae.jpg)

A meter AND fun statistics to watch while your machine grinds away, all for the price of 1 line of code.
With a little trickery you can provide a way to break out of your loop using the Progress Meter form.  The cancel button results in a `False` return value from `EasyProgressMeter`.  It normally returns `True`.

***Be sure and add one to your loop counter*** so that your counter goes from 1 to the max value.  If you do not add one, your counter will never hit the max value.  Instead it will go from 0 to max-1.

#### Debug Output
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

Just like the standard print call, `EasyPrint` supports the `sep` and `end` keyword arguments.  Other names that can be used to call `EasyPrint` include Print, `eprint`,   If you want to close the window, call the function `EasyPrintClose`.

A word of caution.  There are known problems when multiple PySimpleGUI windows are opened, particularly if the user closes them in an unusual way.  Not a reason to stay away from using it.  Just something to keep in mind if you encounter a problem.

You can change the size of the debug window using the `SetOptions` call with the `debug_win_size` parameter.

---
# Custom Form API Calls  (Your First Form)

This is the FUN part of the programming of this GUI.  In order to really get the most out of the API, you should be using an IDE that supports auto complete or will show you the definition of the function.  This will make customizing go  smoother.

This first section on custom forms is for your typical, blocking, non-persistant form.  By this I mean, when you "show" the form, the function will not return until the user has clicked a button or closed the window.  When this happens, the form's window will be automatically closed.

Two other types of forms exist.
1. Persistent form - rather than closing on button clicks, the show form function returns and the form continues to be visible.  This is good for applications like a chat window.
2. Asynchronous form - the trickiest of the lot. Great care must be exercised.  Examples are an MP3 player or status dashboard.  Async forms are updated (refreshed) on a periodic basis.

It's both not enjoyable nor helpful to immediately jump into tweaking each and every little thing available to you.

## The Form Designer
The good news to newcomers to GUI programming is that PySimpleGUI has a form designer.  Better yet, the form designer requires no training and everyone knows how to use it.

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

    button, (number,) = sg.FlexForm('Enter a number example').LayoutAndRead(layout)

    sg.Popup(button, number)

### Example 2 - Get a filename
Let's say you've got a utility you've written that operates on some input file and you're ready to use a GUI to enter than filename rather than the command line.  Follow the same steps as the previous example - draw your form on paper, break it up into rows, label the elements.

![gui4_1](https://user-images.githubusercontent.com/13696193/44160132-6a584900-a087-11e8-862f-7d791a67ee5d.JPG)
![gui5_1](https://user-images.githubusercontent.com/13696193/44160133-6af0df80-a087-11e8-9dec-bb4d4c59393d.JPG)

Writing the code for this one is just as straightforward.  There is one tricky thing, that browse for a file button.  Thankfully PySimpleGUI takes care of associating it with the input field next to it.  As a result, the code looks almost exactly like the form on the paper.

    import PySimpleGUI as sg

    layout = [[sg.Text('Filename')],
              [sg.Input(), sg.FileBrowse()],
              [sg.OK(), sg.Cancel()] ]

    button, (number,) = sg.FlexForm('Get filename example').LayoutAndRead(layout)

    sg.Popup(button, number)


Read on for detailed instructions on the calls that show the form and return your results.



# Copy these design patterns!
## Pattern 1 - With Context Manager


    with sg.FlexForm('SHA-1 & 256 Hash') as form:
        form_rows = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
                     [sg.InputText(), sg.FileBrowse()],
                     [sg.Submit(), sg.Cancel()]]
        button, (source_filename,) = form.LayoutAndRead(form_rows)

## Pattern 2 - No Context Manager


    form = sg.FlexForm('SHA-1 & 256 Hash')
    form_rows = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
                 [sg.InputText(), sg.FileBrowse()],
                 [sg.Submit(), sg.Cancel()]]
    button, (source_filename,) = form.LayoutAndRead(form_rows)

 ----

## Pattern 3 - Short Form


    form_rows = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
                 [sg.InputText(), sg.FileBrowse()],
                 [sg.Submit(), sg.Cancel()]]
    button, (source_filename,) = sg.FlexForm('SHA-1 & 256 Hash').LayoutAndRead(form_rows)



These 3 design patterns both produce this custom form:

![snap0134](https://user-images.githubusercontent.com/13696193/43162410-e7775466-8f58-11e8-8d6a-da4772c00dd8.jpg)

When you're code leaves forms open or you show many forms, then it's important to use the "with" context manager so that resources are freed as quickly as possible.  PySimpleGUI uses `tkinter`.  `tkinter` is very picky about who releases objects and when.  The `with` takes care of disposing of everything properly for you.

The second design pattern is not context manager based.  If you are struggling with an unknown error, try modifying the code to run without a context manager.   To do so, you simple remove the with, stick the form on the front of that statement, and un-indent the with-block code.

The third is the 'compact form'.  It compacts down into 2 lines of code.  One line is  your form definition. The next is the call that shows the form and returns the values.  You can use this pattern for simple, short programs where resource allocation isn't an issue.

You will use these design patterns or code templates for all of your "normal" (blocking) types of input forms.  Copy it and modify it to suit your needs.  This is the quickest way to get your code up and running with PySimpleGUI.  This is the most basic / normal of the design patterns.

### How GUI Programming in Python Should Look?  At least for beginners

Why is Python such a great teaching language and yet no GUI framework exists that lends itself to the basic building blocks of Python, the list or dictionary?  PySimpleGUI set out to be a Pythonic solution to the GUI problem.  Whether it achieved this goal is debatable, but it was an attempt just the same.

The key to custom forms in PySimpleGUI is to view forms as ROWS of Widgets (Elements).  Each row is specified as a list of these Elements.  Put the rows together and you've got a form or window.

Let's look at this one.


![snap0131](https://user-images.githubusercontent.com/13696193/43417007-df6d8408-9407-11e8-9986-30f0415f08a5.jpg)

Let's agree the form has 4 rows.

The first row only has **text** that reads `Rename files or folders`

The second row has 3 elements in it.  First the **text** `Source for Folders`, then an **input** field, then a **browse** button.

Now let's look at how those 2 rows and the other two row from Python code:

    layout = [[sg.Text('Rename files or folders')],
              [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
              [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
              [sg.Submit(), sg.Cancel()]]

See how the source code mirrors the layout?  You simply make lists for each row, then submit that table to PySimpleGUI to show and get values from.

And what about those return values?  Most people simply want to show a form, get the input values and do something with them.  So why break up the code into button callbacks, etc, when I simply want my form's input values to be given to me.

The same "row" concept applies to return values.  The form is scanned from top to bottom, left to right.  Each field that's an input field will occupy a spot in the return values.

In our example form, there are 2 fields, so the return values from this form will be a list with 2 values in it.

    button, (folder_path, file_path) = form.LayoutAndRead(layout)

In the statement that shows and reads the form, the two input fields are directly assigned to the caller's variables `folder_path` and `file_path`, ready to use.  No parsing no callbacks.

Isn't this what almost every Python programmer looking for a GUI wants??  Something easy to work with to get the values and move on to the rest of the program, where the real action is taking place.  Why write pages of tkinter code when the same layout can be achieved with PySimpleGUI in 3 or 4 lines of code.  4 lines or 40?  I chose 4.

### The Auto-Packer

Once you've laid out your elements into, it's the job of the Auto-Packer to place your elements into a window frame.

The layout of custom GUIs is made trivial by the use of the Auto-Packer.  GUI frameworks often use a grid system and sometimes have a "pack" function that's used to place widgets into a window.  It's almost always a confusing exercise to use them.

PySimpleGUI uses a "row by row" approach to building GUIs.  When you were to sketch your GUI out on a sheet of paper and then draw horizontal lines across the page under each widget then you would have a several "rows" of widgets.

For each row in your GUI, you will have a list of elements.  In Python this list is a simple Python list.  An entire GUI window is a list of rows, one after another.

This is how your GUI is created, one row at a time, with one row stacked on top of another.  This visual form of coding makes GUI creation go so much quicker.

    layout = [ [ Row 1 Elements],
               [ Row 2 Elements] ]


### Laying out your form

Your form is a 2 dimensional list in Python.  The first dimension are rows, the second is a list of Elements for each row.  The first thing you want to do is layout your form on paper.

    layout = [ [row 1],
               [row 2],
               [row 3] ]

Simple enough... a list of lists.
A row is a list of Elements.  For example this could be a row with a couple of elements on it.

    [ Input, Button]

Turning back to our example.  This GUI roughly looks like this:

    layout = [ [Text],
               [InputText, FileBrowse]
               [Submit, Cancel] ]

  Now let's put it all together into an entire program.


### Line by line explanation

Going through each line of code in the above form will help explain how to use this design patter.  Copy, modify and run it!

    with sg.FlexForm('SHA-1 & 256 Hash', auto_size_text=True) as form:
This creates a new form, storing it in the variable `form`.

    form_rows = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
The next few rows of code lay out the rows of elements in the window to be displayed.  The variable `form_rows` holds our entire GUI window.   The first row of this form has a Text element.  These simply display text on the form.

    [sg.InputText(), sg.FileBrowse()],
Now we're on the second row of the form.  On this row there are 2 elements.  The first is an `Input` field.  It's a place the user can enter `strings`.  The second element is a `File Browse Button`.  A file or folder browse button will always fill in the text field to it's left unless otherwise specified.  In this example, the File Browse Button will interact with the `InputText` field to its left.

   [sg.Submit(), sg.Cancel()]]

The last line of the `form_rows` variable assignment contains a Submit and a Cancel Button.  These are buttons that will cause a form to return its value to the caller.

    button, (source_filename, ) = form.LayoutAndRead(form_rows)
This is the code that **displays** the form, collects the information and returns the data collected.  In this example we have a button return code and only 1 input field.  The result of the form is stored directly into the variable we wish to work with.


## Return values

   As of version 2.8 there are 2 forms of return values, list and dictionary.

### Return values as a list

   By default return values are a list of values, one entry for each input field.

   Return information from FlexForm, SG's primary form builder interface, is in this format:

    button, (value1, value2, ...)

Each of the Elements that are Input Elements will have a value in the list of return values.  You can unpack your GUI directly into the variables you want to use.

    button, (filename, folder1, folder2, should_overwrite) = form.LayoutAndRead(form_rows)

  Or, you can unpack the return results separately.

    button, values = form.LayoutAndRead(form_rows)
    filename, folder1, folder2, should_overwrite = values

If you have a SINGLE value being returned, it is written this way:

    button, (value1,) = form.LayoutAndRead(form_rows)


 Another way of parsing the return values is to store the list of values into a variable representing the list of values and then index each individual value.  This is not the preferred way of doing it.

     button, value_list = form.LayoutAndRead(form_rows)
     value1 = value_list[0]
     value2 = value_list[1]
     ...

### Return values as a dictionary

If you wish to receive the return values as a dictionary rather than a simple list, then you'll have to one thing...
 * Mark each input element you wish to be in the dictionary with the keyword `key`.

If **any** element in the form has a `key`, then **all** of the return values are returned via a dictionary.  If some elements do not have a key, then they are numbered starting at zero.

This sample program demonstrates these 2 steps as well as how to address the return values (e.g. `values['name']`)


    import PySimpleGUI as sg
    form = sg.FlexForm('Simple data entry form')
    layout = [
              [sg.Text('Please enter your Name, Address, Phone')],
              [sg.Text('Name', size=(15, 1)), sg.InputText('1')],
              [sg.Text('Address', size=(15, 1)), sg.InputText('2', key='address')],
              [sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='phone')],
              [sg.Submit(), sg.Cancel()]
             ]

    button, values = form.LayoutAndRead(layout)

    sg.Popup(button, values, values[0], values['address'], values['phone'])


## The Event Loop / Callback Functions

All GUIs have a few things in common, one of them being an "event loop" of some sort.  If your program shows a single form, collects the data and then executes the primary code of the program then you likely don't need an event loop.  This simple scenarios are front-end GUIs where you call sg.GetFile for example and then call your program that does something with the file.

Event Loops are used in programs where the window stays open after button presses.  The program processes button clicks a loop.  You often hear the term event loop when discussing embedded systems or on a Raspberry Pi.  Let's take a Pi demo program as an example.  This program shows a GUI window, gets button presses, and uses them to control some LEDs.  It loops, reading user input and doing something with it.

This little program has a typical Event Loop

![pi leds](https://user-images.githubusercontent.com/13696193/45448517-8cea7b80-b6a0-11e8-8dbe-eeefea2e93c1.jpg)



    import PySimpleGUI as sg
    layout = [[sg.T('Raspberry Pi LEDs')],
              [sg.ReadFormButton('Turn LED On')],
              [sg.ReadFormButton('Turn LED Off')],
              [sg.Exit()]]

    form = sg.FlexForm('Raspberry Pi GUI', grab_anywhere=False)
    form.Layout(layout)

    # ---- Event Loop ---- #
    while True:
        button, values = form.Read()

        # ---- Process Button Clicks ---- #
       if button is None or button == 'Exit':
            break
	   if button == 'Turn LED Off':
            turn_LED_off()
       elif button == 'Turn LED On':
            turn_LED_on()

    # ---- After Event Loop ---- #
    sg.Popup('Done... exiting')



In the Event Loop we are reading the form and then doing a series of button compares to determine what to do  based on the button that was clicks (value of `button` variable)

The way buttons are presented to the caller in PySimpleGUI is ***not*** how *most* GUI frameworks handle button clicks.  Most GUI frameworks, including tkinter, use ***callback*** functions.  A function you define would be called when a button is clicked.  This requires you to write code where data is shared between these callback functions.  There is a lot more communications that have to happen between parts of your program.

One of the larger hurdles for beginners to GUI programming are these callback functions.  PySimpleGUI was specifically designed in a way that callbacks would not be required.  There is no coordination between one function and another required.  You simple read your button click and take appropriate action.

Whether or not this is a "proper" design for GUI programs can be debated.  It's not a terrible tradeoff to run your own event loop and having a functioning GUI application versus one that maybe never gets written because callback functions were too much to grasp.

---

## All Widgets / Elements
This code utilizes as many of the elements in one form as possible.

     with sg.FlexForm('Everything bagel', auto_size_text=True, default_element_size=(40, 1)) as form:
        layout = [
            [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
            [sg.Text('Here is some text.... and a place to enter text')],
            [sg.InputText()],
            [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],
            [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
            [sg.Multiline(default_text='This is the default Text shoulsd you decide not to type anything',
                          scale=(2, 10))],
            [sg.InputCombo(['Combobox 1', 'Combobox 2'], size=(20, 3)),
             sg.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],
            [sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6)),
             sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=25),
             sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=75),
             sg.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=10)],
            [sg.Text('_'  * 100, size=(70, 1))],
            [sg.Text('Choose Source and Destination Folders', size=(35, 1))],
            [sg.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Source'), sg.FolderBrowse()],
            [sg.Text('Destination Folder', size=(15, 1), auto_size_text=False, justification='right'), sg.InputText('Dest'),
             sg.FolderBrowse()],
            [sg.Submit(), sg.Cancel(), sg.SimpleButton('Customized', button_color=('white', 'green'))]
             ]

         button, values = form.LayoutAndRead(layout)

This is a somewhat complex form with quite a bit of custom sizing to make things line up well.  This is code you only have to write once.  When looking at the code, remember that what you're seeing is a list of lists.  Each row contains a list of Graphical Elements that are used to create the form.

![everything example](https://user-images.githubusercontent.com/13696193/43097412-0a4652aa-8e8a-11e8-8e09-939484e3c568.jpg)

Clicking the Submit button caused the form call to return.  The call to Popup resulted in this dialog box.
![results 2](https://user-images.githubusercontent.com/13696193/43097502-44e3ed32-8e8a-11e8-9a51-2b8af0b1a682.jpg)


**`Note, button value can be None`**.  The value for `button` will be the text that is displayed on the button element when it was created.  If the user closed the form using something other than a button, then `button` will be `None`.

You can see in the Popup that the values returned are a list.  Each input field in the form generates one item in the return values list.  All input fields return a `string` except for Check Boxes and Radio Buttons.  These return `bool`.

---
# Building Custom Forms

You will find it much easier to write code using PySimpleGUI if you use an IDE such as PyCharm.  The features that show you documentation about the API call you are making will help you determine which settings you want to change, if any.  In PyCharm, two commands are particularly helpful.

    Control-Q (when cursor is on function name) brings up a box with the function definition
    Control-P (when cursor inside function call "()") shows a list of parameters and their default values

## Synchronous Forms
The most common use of PySimpleGUI is to display and collect information from the user.  The most straightforward way to do this is using a "blocking" GUI call.  Execution is "blocked" while waiting for the user to close the GUI form/dialog box.
You've already seen a number of examples above that use blocking forms.  Anytime you see a context manager used (see the `with` statement) it's most likely a blocking form.  You can examine the show calls to be sure.  If the form is a non-blocking form, it must indicate that in the call to `form.show`.

NON-BLOCKING form call:

          form.Show(non_blocking=True)

### Beginning a Form
The first step is to create the form object using the desired form customization.

    with FlexForm('Everything bagel', auto_size_text=True, default_element_size=(30,1)) as form:

This is the definition of the FlexForm object:

    def FlexForm(title,
        default_element_size=(DEFAULT_ELEMENT_SIZE[0], DEFAULT_ELEMENT_SIZE[1]),
        default_button_element_size = (None, None),
        auto_size_text=None,
        auto_size_buttons=None,
        scale=(None, None),
        location=(None, None),
        font=None,
        button_color=None,Font=None,
        progress_bar_color=(None,None),
        background_color=None
        is_tabbed_form=False,
        border_depth=None,
        auto_close=False,
        auto_close_duration=DEFAULT_AUTOCLOSE_TIME,
        icon=DEFAULT_WINDOW_ICON,
        return_keyboard_events=False,
        use_default_focus=True,
        text_justification=None,
        no_titlebar=False,
        grab_anywhere=True
        keep_on_top=False):


Parameter Descriptions.  You will find these same parameters specified for each `Element` and some of them in `Row` specifications.  The `Element` specified value will take precedence over the `Row` and `Form` values.

       default_element_size - Size of elements in form in characters (width, height)
       default_button_element_size - Size of buttons on this form
       auto_size_text - Bool. True if elements should size themselves according to contents. Defaults to True
       auto_size_buttons - Bool. True if button elements should size themselves according to their text label
       scale - Set size of element to be a multiple of the Element size
       location - (x,y) Location to place window in pixels
       font - Font name and size for elements of the form
       button_color - Default color for buttons (foreground, background). Can be text or hex
       progress_bar_color - Foreground and background colors for progress bars
       background_color - Color of the window background
       is_tabbed_form - Bool. If True then form is a tabbed form
       border_depth - Amount of 'bezel' to put on input boxes, buttons, etc.
       auto_close - Bool.  If True form will autoclose
       auto_close_duration - Duration in seconds before form closes
       icon - .ICO file that will appear on the Task Bar and end of Title Bar
       return_keyboard_events - if True key presses are returned as buttons
       use_default_focus - if True and no focus set, then automatically set a focus
       text_justification - Justification to use for Text Elements in this form
       no_titlebar - Create window without a titlebar
       grab_anywhere - Grab any location on the window to move the window
       keep_on_top - if True then window will always stop on top of other windows on the screen.  Great for floating toolbars.


#### Window Location
PySimpleGUI computes the exact center of your window and centers the window on the screen.  If you want to locate your window elsewhere, such as the system default of (0,0), if you have 2 ways of doing this. The first is when the form is created.  Use the `location` parameter to set where the window.  The second way of doing this is to use the `SetOptions` call which will set the default window location for all windows in the future.

#### Sizes
Note several variables that deal with "size".  Element sizes are measured in characters.  A Text Element with a size of 20,1 has a size of 20 characters wide by 1 character tall.

The default Element size for PySimpleGUI is `(45,1)`.

Sizes can be set at the element level, or in this case, the size variables apply to all elements in the form.  Setting `size=(20,1)` in the form creation call will set all elements in the form to that size.

In addition to `size` there is a `scale` option.  `scale` will take the Element's size and scale it up or down depending on the scale value.  `scale=(1,1)` doesn't change the Element's size.  `scale=(2,1)` will set the Element's size to be twice as wide as the size setting.

There are a couple of widgets where one of the size values is in pixels rather than characters.  This is true for Progress Meters and Sliders.  The second parameter is the 'height' in pixels.

#### No Titlebar

Should you wish to create cool looking windows that are clean with no windows titlebar, use the no_titlebar option when creating the window.

Be sure an provide your user an "exit" button or they will not be able to close the window!  When no titlebar is enabled, there will be no icon on your taskbar for the window.  Without an exit button you will need to kill via taskmanager... not fun.

Windows with no titlebar rely on the grab anywhere option to be enabled or else you will be unable to move the window.

Windows without a titlebar can be used to easily create a floating launcher.


![floating launcher](https://user-images.githubusercontent.com/13696193/45258246-71bafb80-b382-11e8-9f5e-79421e6c00bb.jpg)


#### Grab Anywhere

This is a feature unique to PySimpleGUI.  The default is ENABLED.... unless the form is a non-blocking form.

It is turned off for non-blocking because there is a warning message printed out if the user closes a non-blocking form using a button with grab_anywhere enabled.  There is no harm in these messages, but it may be distressing to the user.    Should you wish to enable for a non-blocking form, simply get grab_anywhere = True when you create the form.

#### Always on top

To keep a window on top of all other windows on the screen, set keep_on_top = True when the form is created.  This feature makes for floating toolbars that are very helpful and always visible on your desktop.


## Elements
"Elements" are the building blocks used to create forms.  Some GUI APIs use the term "Widget" to describe these graphic elements.

     Text
     Single Line Input
     Buttons including these types:
         File Browse
         Folder Browse
         Non-closing return
         Close form
         Realtime
     Checkboxes
     Radio Buttons
     Listbox
     Slider
     Multi-line Text Input
     Scroll-able Output
     Progress Bar
     Async/Non-Blocking Windows
     Tabbed forms
     Persistent Windows
     Redirect Python Output/Errors to scrolling Window
     "Higher level" APIs (e.g. MessageBox, YesNobox, ...)


### Output Elements
Building a form is simply making lists of Elements.  Each list is a row in the overall GUI dialog box.  The definition looks something like this:

    layout = [ [row 1 element, row 1 element],
               [row 2 element, row 2 element, row 2 element] ]
The code is a crude representation of the GUI, laid out in text.

####  Text Element

    layout = [[sg.Text('This is what a Text Element looks like')]]

 ![simple text](https://user-images.githubusercontent.com/13696193/44959877-e9d97b00-aec3-11e8-9d24-b4405ee4a148.jpg)


The most basic element is the Text element.  It simply displays text.  Many of the 'options' that can be set for a Text element are shared by other elements.  Size, Scale are a couple that you will see in every element.

    Text(Text,
        scale=(None, None),
        size=(None, None),
        auto_size_text=None,
        font=None,
        text_color=None,
        justification=None)
.

    Text - The text that's displayed
    size - Element's size
    auto_size_text - Bool. Change width to match size of text
    font - Font name and size to use
    text_color - text color
    justification - Justification for the text. String - 'left', 'right', 'center'

Some commonly used elements have 'shorthand' versions of the functions to make the code more compact.  The functions `T` and `Txt` are the same as calling `Text`.

**Fonts** in PySimpleGUI are always in this format:

    (font_name, point_size)

The default font setting is

    ("Helvetica", 10)

**Color** in PySimpleGUI are in one of two format.  They can be a single color or a color pair.  Buttons are an example of a color pair.

    (foreground, background)

 Individual colors are specified using either the color names as defined in tkinter or an RGB string of this format:

    "#RRGGBB"

**auto_size_text**
A `True` value for `auto_size_text`, when placed on Text Elements, indicates that the width of the Element should be shrunk do the width of the text.   The default setting is True.

 - [ ] List item


**Shortcut functions**
The shorthand functions for `Text` are `Txt` and `T`

####  Multiline Text Element

    layout = [[sg.Multiline('This is what a Multi-line Text Element looks like', size=(45,5))]]

![multiline](https://user-images.githubusercontent.com/13696193/44959853-b139a180-aec3-11e8-972f-f52188510c88.jpg)

This Element doubles as both an input and output Element.  The `DefaultText` optional parameter is used to indicate what to output to the window.

    Multiline(default_text='',
           enter_submits = False,
           scale=(None, None),
              size=(None, None),
            auto_size_text=None)
.

    default_text - Text to display in the text box
    enter_submits - Bool. If True, pressing Enter key submits form
    scale - Element's scale
    size - Element's size
    auto_size_text - Bool. Change width to match size of text

#### Output Element
Output re-routes `Stdout` to a scrolled text box.  It's used with Async forms.  More on this later.

    form.AddRow(gg.Output(size=(100,20)))

![output](https://user-images.githubusercontent.com/13696193/44959863-b72f8280-aec3-11e8-8caa-7bc743149953.jpg)

    Output(scale=(None, None),
           size=(None, None))
.

     scale  - How much to scale size of element
     size - Size of element (width, height) in characters

###  Input Elements
  These make up the majority of the form definition.  Optional variables at the Element level override the Form level values (e.g. `size` is specified in the Element).  All input Elements create an entry in the list of return values.  A Text Input Element creates a string in the list of items returned.

#### Text Input Element

    layout = [[sg.InputText('Default text')]]

![inputtext 2](https://user-images.githubusercontent.com/13696193/44959861-b5fe5580-aec3-11e8-8040-53ec241b5079.jpg)


      def InputText(default_text = '',
                    scale=(None, None),
                    size=(None, None),
                    auto_size_text=None,
                    password_char='',
                    background_color=None,
                    text_color=None,
                    do_not_clear=False,
                    key=None,
                    focus=False
                    )
.

     default_text - Text initially shown in the input box
     scale - Amount size is scaled by
     size - (width, height) of element in characters
     auto_size_text- Bool.  True is element should be sized to fit text
     password_char - Character that will be used to replace each entered character. Setting to a value indicates this field is a password entry field
     background_color - color to use for the input field background
     text_color - color to use for the typed text
     do_not_clear - Bool. Normally forms clear when read, turn off clearing with this flag.
     key = Dictionary key to use for return values
     focus = Bool. True if this field should capture the focus (moves cursor to this field)

 There are two methods that can be called:

     InputText.Update(new_Value) - sets the input value
     Input.Text(Get() - returns the current value of the field.


Shorthand functions that are equivalent to `InputText` are `Input` and `In`


#### Combo Element
Also known as a drop-down list.  Only required parameter is the list of choices.  The return value is a string matching what's visible on the GUI.

    layout = [[sg.InputCombo(['choice 1', 'choice 2'])]]

![combobox](https://user-images.githubusercontent.com/13696193/44959860-b565bf00-aec3-11e8-82fe-dbe41252458b.jpg)

    InputCombo(values,
               scale=(None, None),
               size=(None, None),
               auto_size_text=None,
               background_color = None,
               text_color = None,
               key = None)
.

     values - Choices to be displayed. List of strings
     scale - Amount to scale size by
     size - (width, height) of element in characters
     auto_size_text - Bool. True if size should fit the text length
     background_color - color to use for the input field background
     text_color - color to use for the typed text
     key = Dictionary key to use for return values

#### Listbox Element
The standard listbox like you'll find in most GUIs.  Note that the return values from this element will be a ***list of results, not a single result***. This is because the user can select more than 1 item from the list (if you set the right mode).

    layout = [[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))]]

![listbox 2](https://user-images.githubusercontent.com/13696193/44959859-b4cd2880-aec3-11e8-881c-1e369d5c6337.jpg)


       Listbox(values,
             select_mode=None,
             scale=(None, None),
             size=(None, None),
             auto_size_text=None,
             font=None,
             background_color = None,
             text_color = None,
             key = None)
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
    scale - Amount to scale size by
    size - (width, height) of element in characters
    auto_size_text - Bool. True if size should fit the text length
    background_color - color to use for the input field background
    text_color - color to use for the typed text
    key = Dictionary key to use for return values

The `select_mode` option can be a string or a constant value defined as a variable.  Generally speaking strings are used for these kinds of options.

#### Slider Element

Sliders have a couple of slider-specific settings as well as appearance settings.  Examples include the `orientation` and `range` settings.

    layout = [[sg.Slider(range=(1,500), default_value=222, size=(20,15), orientation='horizontal', font=('Helvetica', 12))]]

![slider](https://user-images.githubusercontent.com/13696193/44959858-b4349200-aec3-11e8-9e25-c0fcf025d19e.jpg)

       Slider(range=(None,None),
              default_value=None,
              orientation=None,
              border_width=None,
              relief=None,
              scale=(None, None),
              size=(None, None),
              font=None,
              background_color = None,
              text_color = None,
              key = None) ):
.

      range - (min, max) slider's range
      default_value - default setting (within range)
      orientation - 'horizontal' or 'vertical' ('h' or 'v' work)
      border_width - how deep the widget looks
      relief - relief style. Values are same as progress meter relief values.  Can be a constant or a string:
         RELIEF_RAISED= 'raised'
         RELIEF_SUNKEN= 'sunken'
         RELIEF_FLAT= 'flat'
         RELIEF_RIDGE= 'ridge'
         RELIEF_GROOVE= 'groove'
         RELIEF_SOLID = 'solid'
      scale - Amount to scale size by
       size - (width, height) of element in characters
       auto_size_text - Bool. True if size should fit the text
       background_color - color to use for the input field background
       text_color - color to use for the typed text
       key = Dictionary key to use for return values

#### Radio Button Element

Creates one radio button that is assigned to a group of radio buttons.  Only 1 of the buttons in the group can be selected at any one time.

    layout =  [[sg.Radio('My first Radio!', "RADIO1", default=True), sg.Radio('My second radio!', "RADIO1")]]

![radio](https://user-images.githubusercontent.com/13696193/44959857-b4349200-aec3-11e8-8e2d-e6a49ffbd0b6.jpg)

     Radio(text,
           group_id,
           default=False,
           scale=(None, None),
           size=(None, None),
           auto_size_text=None,
           font=None,
           background_color = None,
           text_color = None,
           key = None)

.

     text - Text to display next to button
     group_id - Groups together multiple Radio Buttons. Can be any value
     default - Bool.  Initial state
     scale - Amount to scale size of element
     size- (width, height) size of element in characters
     auto_size_text - Bool.  True if should size width to fit text
     font - Font type and size for text display
     background_color - color to use for the background
     text_color - color to use for the text
     key = Dictionary key to use for return values


#### Checkbox Element
Checkbox elements are like Radio Button elements.  They return a bool indicating whether or not they are checked.

    layout =  [[sg.Checkbox('My first Checkbox!', default=True), sg.Checkbox('My second Checkbox!')]]


![checkbox](https://user-images.githubusercontent.com/13696193/44959906-6f5d2b00-aec4-11e8-9c8a-962c787f0286.jpg)


    Checkbox(text,
             default=False,
             scale=(None, None),
             size=(None, None),
             auto_size_text=None,
             font=None,
             background_color = None,
             text_color = None,
             key = None):
.

     text - Text to display next to checkbox
     default- Bool + None.  Initial state. True = Checked, False = unchecked, None = Not available (grayed out)
     scale - Amount to scale size of element
     size - (width, height) size of element in characters
     auto_size_text- Bool.  True if should size width to fit text
     font- Font type and size for text display
     background_color - color to use for the background
     text_color - color to use for the typed text
     key = Dictionary key to use for return values


#### Spin Element

An up/down spinner control.  The valid values are passed in as a list.

    layout =  [[sg.Spin([i for i in range(1,11)], initial_value=1), sg.Text('Volume level')]]

![spinner](https://user-images.githubusercontent.com/13696193/44959855-b1d23800-aec3-11e8-9f51-afb2109879da.jpg)

    Spin(values,
         intiial_value=None,
         scale=(None, None),
         size=(None, None),
         auto_size_text=None,
         font=None,
         background_color = None,
         text_color = None,
         key = None):
.

     values - List of valid values
     initial_value - String with initial value
     scale - Amount to scale size of element
     size - (width, height) size of element in characters
     auto_size_text - Bool.  True if should size width to fit text
     font - Font type and size for text display
     background_color - color to use for the background
     text_color - color to use for the typed text
     key = Dictionary key to use for return values

#### Button Element

Buttons are the most important element of all!  They cause the majority of the action to happen.  After all, it's a button press that will get you out of a form, whether it but Submit or Cancel, one way or another a button is involved in all forms.  The only exception is to this is when the user closes the window using the "X" in the upper corner which means no button was involved.

The Types of buttons include:
* Folder Browse
* File Browse
* Close Form
* Read Form
* Realtime
* Calendar Chooser
* Color Chooser


 Close Form - Normal buttons like Submit, Cancel, Yes, No, etc, are "Close Form" buttons.  They cause the input values to be read and then the form is closed, returning the values to the caller.

Folder Browse - When clicked a folder browse dialog box is opened.  The results of the Folder Browse dialog box are written into one of the input fields of the form.

File Browse - Same as the Folder Browse except rather than choosing a folder, a single file is chosen.

Calendar Chooser - Opens a graphical calendar to select a date.

Color Chooser - Opens a color chooser dialog

Read Form - This is an async form button that will read a snapshot of all of the input fields, but does not close the form after it's clicked.

Realtime - This is another async form button.  Normal button clicks occur after a button's click is released.  Realtime buttons report a click the entire time the button is held down.

While it's possible to build forms using the Button Element directly, you should never need to do that.  There are pre-made buttons and shortcuts that will make life much easier.  The most basic Button element call to use is `SimpleButton`

    SimpleButton(text,
			     image_filename=None,
			     image_size=(None, None),
			     image_subsample=None,
			     border_width=None,
			     bind_return_key=False,
                 scale=(None, None),
                 size=(None, None),
                 auto_size_button=None,
                 button_color=None,
                 font=None,
                 focus=False)

These Pre-made buttons are some of the most important elements of all because they are used so much.  If you find yourself needing to create a custom button often because it's not on this list, please post a request on GitHub.  (hmmm Save already comes to mind). They include:

    OK
    Ok
    Submit
    Cancel
    Yes
    No
    Exit
    Quit
    Save
    SaveAs
    FileBrowse
    FileSaveAs
    FolderBrowse
.
    layout =  [[sg.OK(), sg.Cancel()]]

![ok cancel 3](https://user-images.githubusercontent.com/13696193/44959927-aa5f5e80-aec4-11e8-86e1-5dc0b3a2b803.jpg)

  #### Button targets

The `FileBrowse`, `FolderBrowse`, `FileSaveAs` , `FilesSaveAs`, `CalendarButton`, `ColorChooserButton` buttons all fill-in values into another element located on the form.  The target can be a Text Element or an InputText Element.  The location of the element is specified by the `target` variable in the function call.  The Target is specified using a grid system.  The rows in your GUI are numbered starting with 0. The target can be specified as a hard coded grid item or it can be relative to the button.

The default value for `targe` is `(ThisRow, -1)`.   `ThisRow` is a special value that tells the GUI to use the same row as the button.  The Y-value of -1 means the field one value to the left of the button.  For a File or Folder Browse button, the field that it fills are generally to the left of the button is most cases.

If a value of `(None, None)` is chosen for the target, then the button itself will hold the information.  Later the button can be queried for the  value.

Let's examine this form as an example:


![file browse](https://user-images.githubusercontent.com/13696193/44959944-d1b62b80-aec4-11e8-8a68-9d79d37b2c81.jpg)


The `InputText` element is located at (1,0)... row 1, column 0.  The `Browse` button is located at position (2,0).  The Target for the button could be any of these values:

    Target = (1,0)
    Target = (-1,0)

The code for the entire form could be:

    layout = [[sg.T('Source Folder')],
              [sg.In()],
              [sg.FolderBrowse(target=(-1, 0)), sg.OK()]]

**Save & Open Buttons**

There are 3 different types of File/Folder open dialog box available.  If you are looking for a file to open, the `FileBrowse` is what you want. If you want to save a file, `SaveAs` is the button. If you want to get a folder name, then `FolderBrowse` is the button to use.


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
Not all buttons are created equal.  A button that closes a form is different that a button that returns from the form without closing it.  If you want to define your own button, you will generally do this with the Button Element `SimpleButton`, which closes the form when clicked.

layout =  [[sg.SimpleButton('My Button')]]

![button](https://user-images.githubusercontent.com/13696193/44959862-b696ec00-aec3-11e8-9e88-4b9af0338a03.jpg)

All buttons can have their text changed by changing the `button_text` variable in the button call.  It is this text that is returned when a form is read.  This text will be what tells you which button is called so make it unique.  Most of the convenience buttons (Submit, Cancel, Yes, etc) are all SimpleButtons. Some that are not are `FileBrowse` ,  `FolderBrowse`, `FileSaveAs`.  They clearly do not close the form. Instead they bring up a file or folder browser dialog box.

**Button Images**
Now this is an exciting feature not found in many simplified packages.... images on buttons!  You can make a pretty spiffy user interface with the help of a few button images.

Your button images need to be in PNG or GIF format.  When you make a button with an image, set the button background to the same color as the background.  There's a button color TRANSPARENT_BUTTON that you can set your button color to in order for it to blend into the background.  Note that this value is currently the same as the color as the default system background on Windows.

This example comes from the `Demo Media Player.py` example program.  Because it's a non-blocking button, it's defined as `ReadFormButton`.  You also put images on blocking buttons by using `SimpleButton`.


    sg.ReadFormButton('Restart Song', button_color=sg.TRANSPARENT_BUTTON,
                       image_filename=image_restart, image_size=(50, 50), image_subsample=2, border_width=0)

Three parameters are used for button images.

    image_filename - Filename. Can be a relative path
    image_size - Size of image file in pixels
    image_subsample - Amount to divide the size by.  2 means your image will be 1/2 the size.  3 means 1/3

Here's an example form made with button images.

![media file player](https://user-images.githubusercontent.com/13696193/43161977-9ee7cace-8f57-11e8-8ff8-3ea24b69dab9.jpg)

You'll find the source code in the file Demo Media Player.  Here is what the button calls look like to create media player form

    sg.ReadFormButton('Pause', button_color=sg.TRANSPARENT_BUTTON,
                      image_filename=image_pause, image_size=(50, 50), image_subsample=2, border_width=0)

This is one you'll have to experiment with at this point.  Not up for an exhaustive explanation.

  **Realtime Buttons**

  Normally buttons are considered "clicked" when the mouse button is let UP after a downward click on the button.  What about times when you need to read the raw up/down button values.  A classic example for this is a robotic remote control.  Building a remote control using a GUI is easy enough.  One button for each of the directions is a start.  Perhaps something like this:

![robot remote](https://user-images.githubusercontent.com/13696193/44959958-ff9b7000-aec4-11e8-99ea-7450926409be.jpg)


This form has 2 button types.  There's the normal "Simple Button" (Quit) and 4 "Realtime Buttons".

Here is the code to make, show and get results from this form:

    form = sg.FlexForm('Robotics Remote Control', auto_size_text=True)

    form_rows = [[sg.Text('Robotics Remote Control')],
                 [sg.T(' '*10), sg.RealtimeButton('Forward')],
                 [ sg.RealtimeButton('Left'), sg.T(' '*15), sg.RealtimeButton('Right')],
                 [sg.T(' '*10), sg.RealtimeButton('Reverse')],
                 [sg.T('')],
                 [sg.Quit(button_color=('black', 'orange'))]
                 ]

    form.LayoutAndRead(form_rows, non_blocking=True)

Somewhere later in your code will be your main event loop. This is where you do your polling of devices, do input/output, etc.  It's here that you will read your form's buttons.

    while (True):
        # This is the code that reads and updates your window
        button, values = form.ReadNonBlocking()
        if button is not None:
            sg.Print(button)
        if button == 'Quit'  or values is None:
            break
      time.sleep(.01)

This loop will read button values and print them.  When one of the Realtime buttons is clicked, the call to `form.ReadNonBlocking` will  return a button name matching the name on the button that was depressed.  It will continue to return values as long as the button remains depressed.  Once released, the ReadNonBlocking will return None for buttons until a button is again clicked.

**File Types**
The `FileBrowse` & `SaveAs` buttons have an additional setting named `file_types`.  This variable is used to filter the files shown in the file dialog box.  The default value for this setting is

    FileTypes=(("ALL Files", "*.*"),)

This code produces a form where the Browse button only shows files of type .TXT

    layout =  [[sg.In() ,sg.FileBrowse(file_types=(("Text Files", "*.txt"),))]]

  ***The ENTER key***
       The ENTER key is an important part of data entry for forms.  There's a long  tradition of the enter key being used to quickly submit forms.  PySimpleGUI implements this by tying the ENTER key to the first button that closes or reads a form.

The Enter Key can be "bound" to a particular button so that when the key is pressed, it causes the form to return as if the button was clicked.  This is done using the `bind_return_key` parameter in the button calls.
If there are more than 1 button on a form, the FIRST button that is of type Close Form or Read Form is used.  First is determined by scanning the form, top to bottom and left to right.

 ---
#### ProgressBar
The `ProgressBar` element is used to build custom Progress Bar forms.  It is HIGHLY recommended that you use the functions that provide a complete progress meter solution for you.  Progress Meters are not easy to work with because the forms have to be non-blocking and they are tricky to debug.

The **easiest** way to get progress meters into your code is to use the `EasyProgessMeter` API.  This consists of a pair of functions, `EasyProgessMeter` and `EasyProgressMeterCancel`.  You can easily cancel any progress meter by calling it with the current value = max value.  This will mark the meter as expired and close the window.
You've already seen EasyProgressMeter calls presented earlier in this readme.

    sg.EasyProgressMeter('My Meter', i+1, 1000, 'Optional message')

The return value for `EasyProgressMeter` is:
`True` if meter updated correctly
`False` if user clicked the Cancel button, closed the form, or vale reached the max value.
**Customized Progress Bar**

If you want a bit more customization of your meter, then you can go up 1 level and use the calls to `ProgressMeter` and `ProgressMeterUpdate`.  These APIs behave like an object we're all used to.  First you create the `ProgressMeter` object, then you call the `Update` method to update it.


You setup the progress meter by calling

    my_meter = ProgressMeter(title,
                        max_value,
                        *args,
                        orientantion=None,
                        bar_color=DEFAULT_PROGRESS_BAR_COLOR,
                        button_color=None,
                        size=DEFAULT_PROGRESS_BAR_SIZE,
                        scale=(None, None),
                        border_width=DEFAULT_PROGRESS_BAR_BORDER_WIDTH)
Then to update the bar within your loop

    return_code = ProgressMeterUpdate(my_meter,
                                     value,
                                     *args):
Putting it all together you get this design pattern

    my_meter = sg.ProgressMeter('Meter Title', 100000, orentation='Vert')

    for i in range(0, 100000):
        sg.ProgressMeterUpdate(my_meter, i+1, 'Some variable', 'Another variable')


The final way of using a Progress Meter with PySimpleGUI is to build a custom form with a `ProgressBar` Element in the form.  You will need to run your form as a non-blocking form.  When you are ready to update your progress bar, you call the `UpdateBar` method for the `ProgressBar` element itself.

![progress custom](https://user-images.githubusercontent.com/13696193/45243969-c3508100-b2c3-11e8-82bc-927d0307e093.jpg)

    # create the progress bar element
    progress_bar = sg.ProgressBar(10000, orientation='h', size=(20,20))
    # layout the form
    layout = [[sg.Text('A custom progress meter')],
              [progress_bar],
              [sg.Cancel()]]

    # create the form`
    form = sg.FlexForm('Custom Progress Meter')
    # display the form as a non-blocking form
    form.LayoutAndRead(layout, non_blocking=True)
    # loop that would normally do something useful
    for i in range(10000):
        # check to see if the cancel button was clicked and exit loop if clicked
      button, values = form.ReadNonBlocking()
        if button == 'Cancel'  or values == None:
            break
      # update bar with loop value +1 so that bar eventually reaches the maximum
      progress_bar.UpdateBar(i+1)
    # done with loop... need to destroy the window as it's still open
    form.CloseNonBlockingForm()


#### Output
The Output Element is a re-direction of Stdout.  Anything "printed" will be displayed in this element.

    Output(scale=(None, None),
           size=(None, None))

Here's a complete solution for a chat-window using an Async form with an Output Element

    import PySimpleGUI as sg
        # Blocking form that doesn't close
    def ChatBot():
        with sg.FlexForm('Chat Window', auto_size_text=True, default_element_size=(30, 2)) as form:
            layout = [[(sg.Text('This is where standard out is being routed', size=[40, 1]))],
                        [sg.Output(size=(80, 20))],
                        [sg.Multiline(size=(70, 5), enter_submits=True), sg.ReadFormButton('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0])), sg.SimpleButton('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]
            # notice this is NOT the usual LayoutAndRead call because you don't yet want to read the form
           # if you call LayoutAndRead from here, then you will miss the first button click
           form.Layout(layout)
            # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
           while True:
                button, value = form.Read()
                if button == 'SEND':
                    print(value)
                else:
                    break
-------------------
## Columns
Starting in version 2.9 you'll be able to do more complex layouts by using the Column Element.  Think of a Column as a form within a form.  And, yes, you can have a Column within a Column if you want.

Columns are specified in exactly the same way as a form is, as a list of lists.

Columns are needed when you have an element that has a height > 1 line on the left, with single-line elements on the right.  Here's an example of this kind of layout:


![column](https://user-images.githubusercontent.com/13696193/44959988-66b92480-aec5-11e8-9c26-316ed24a68c0.jpg)


This code produced the above window.


    import PySimpleGUI as sg

    # Demo of how columns work
    # Form has on row 1 a vertical slider followed by a COLUMN with 7 rows
    # Prior to the Column element, this layout was not possible
    # Columns layouts look identical to form layouts, they are a list of lists of elements.

    form = sg.FlexForm('Columns')                                   # blank form

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

    # Display the form and get values
    # If you're willing to not use the "context manager" design pattern, then it's possible
    # to collapse the form display and read down to a single line of code.
    button, values = sg.FlexForm('Compact 1-line form with column').LayoutAndRead(layout)

    sg.Popup(button, values, line_width=200)

The Column Element has 1 required parameter and 1 optional (the layout and the background color).  Setting the background color has the same effect as setting the form's background color, except it only affects the column rectangle.

    Column(layout, background_color=None)

The default background color for Columns is the same as the default window background color.  If you change the look and feel of the form, the column background will match the form background automatically.

## Tabbed Forms
Tabbed forms are shown using the `ShowTabbedForm` call.  The call has the format

     results = ShowTabbedForm('Title for the form',
                              (form,layout,'Tab 1 label'),
                              (form2,layout2, 'Tab 2 label'), ...)

Each of the tabs of the form is in fact a form.  The same steps are taken to create the form as before.  A `FlexForm` is created, then rows are filled with Elements, and finally the form is shown.  When calling `ShowTabbedForm`, each form is passed in as a tuple.  The tuple has  the format:  `(the form, the rows, a string shown on the tab)`

Results are returned as a list of lists.  For each form you'll get a list that's in the same format as a normal form. A single tab's values would be:

    (button, (values))

Recall that values is a list as well.  Multiple tabs in the form would return like this:

    ((button1, (values1)), (button2, (values2))

  ## Colors ##
Starting in version 2.5 you can change the background colors for the window and the Elements.

Your forms can go from this:

![snap0155](https://user-images.githubusercontent.com/13696193/43273879-a9fdc10a-90cb-11e8-8c20-4f6a244ebe2f.jpg)


to this... with one function call...


![snap0156](https://user-images.githubusercontent.com/13696193/43273880-aa1955e6-90cb-11e8-94b6-673ecdb2698c.jpg)



While you can do it on an element by element or form level basis, the easiest way, by far, is a call to `SetOptions`.

Be aware that once you change these options they are changed for the rest of your program's execution.  All of your forms will have that look and feel, until you change it to something else (which could be the system default colors.

This call sets all of the different color options.

    SetOptions(background_color='#9FB8AD',
               text_element_background_color='#9FB8AD',
               element_background_color='#9FB8AD',
               scrollbar_color=None,
               input_elements_background_color='#F7F3EC',
               progress_meter_color = ('green', 'blue')
               button_color=('white','#475841'))



## Global Settings
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


These settings apply to all forms `SetOptions`.  The Row options and Element options will take precedence over these settings.  Settings can be thought of as levels of settings with the Form-level being the highest and the Element-level the lowest.  Thus the levels are:

 - Form level
 - Row level
 - Element level

Each lower level overrides the settings of the higher level.  Once settings have been changed, they remain changed for the duration of the program (unless changed again).

## Persistent Forms (Window stays open after button click)

There are 2 ways to keep a window open after the user has clicked a button.  One way is to use non-blocking forms (see the next section).  The other way is to use buttons that 'read' the form instead of 'close' the form when clicked.  The typical buttons you find in forms, including the shortcut buttons, close the form.  These include OK, Cancel, Submit, etc.  The SimpleButton Element also closes the form.

The `ReadFormButton` Element creates a button that when clicked will return control to the user, but will leave the form open and visible.  This button is also used in Non-Blocking forms.  The difference is in which call is made to read the form.  The `Read` call will block, the `ReadNonBlocking` will not block.



## Asynchronous (Non-Blocking) Forms
So you want to be a wizard do ya?  Well go boldly!

Use async forms sparingly.  It's possible to have a form that appears to be async, but it is not.  **Please** try to find other methods before going to async forms.  The reason for this plea is that async forms poll tkinter over and over.  If you do not have a sleep in your loop, you will eat up 100% of the CPU time.

When to use a non-blocking form:
* A media file player like an MP3 player
* A status dashboard that's periodically updated
* Progress Meters - when you want to make your own progress meters
* Output using print to a scrolled text element. Good for debugging.

If your application doesn't follow the basic design pattern at one of those, then it shouldn't be  executed as a non-blocking form.


### Instead of ReadNonBlocking --- Use `change_submits = True` or return_keyboard_events = True

Any time you are thinking "I want an X Element to cause a Y Element to do something", then you want to use the `change_submits` option.

***Instead of polling, try options that cause the form to return to you.***  By using non-blocking forms, you are *polling*.  You can indeed create your application by polling.  It will work.  But you're going to be maxing out your processor and may even take longer to react to an event than if you used another technique.

**Examples**

One example is you have an input field that changes as you press buttons on an on-screen keypad.

![keypad 3](https://user-images.githubusercontent.com/13696193/45260275-a2198e80-b3b0-11e8-85fe-a4ce6484510f.jpg)


Another example, a slider or a spinner move changes the size of the text somewhere on the form.


![snap0272](https://user-images.githubusercontent.com/13696193/45260249-ec4e4000-b3af-11e8-853b-9b29d0bf7797.jpg)

A final example...  changing a text field as a user types into another field.



### Periodically Calling`ReadNonBlocking`

Periodically "refreshing" the visible GUI.  The longer you wait between updates to your GUI the more sluggish your forms will feel.  It is up to you to make these calls or your GUI will freeze.

There are 2 methods of interacting with non-blocking forms.
1. Read the form just as you would a normal form
2. "Refresh" the form's values without reading the form. It's a quick operation meant to show the user the latest values

 With asynchronous forms the form is shown, user input is read, but your code keeps right on chugging.  YOUR responsibility is to call `PySimpleGUI.ReadNonBlocking` on a periodic basis.  Once a second or more will produce a reasonably snappy GUI.

 #### Exiting a Non-Blocking Form
Typically when reading a form you check `if Button is None` to determine if a form was closed.  With NonBlocking forms, buttons will be None unless a button or a key was returned.  The way you determine if a window was closed in a non-blocking form  is to check **both** the button and the values are None.  Since button is normally None, you only need to test for `value is None` in your code.

The proper code to check if the user has exited the form will be a polling-loop that looks something like this:

    while True:
       button, values = form.ReadNonBlocking()
       if values is None or button == 'Quit':
          break


We're going to build an app that does the latter.  It's going to update our form with a running clock.

The basic flow and functions you will be calling are:
Setup

       form = FlexForm()
       form_rows = .....
       form.LayoutAndRead(form_rows, non_blocking=True)


Periodic refresh

    form.ReadNonBlocking()   or       form.Refresh()

If you need to close the form

    form.CloseNonBlockingForm()

Rather than the usual `form.LayoutAndRead()` call, we're manually adding the rows (doing the layout) and then showing the form.  After the form is shown, you simply call `form.ReadNonBlocking()` every now and then.

When you are ready to close the form (assuming the form wasn't closed by the user or a button click) you simply call `form.CloseNonBlockingForm()`

**Example - Running timer that updates**
See the sample code on the GitHub named Demo Media Player for another example of Async Forms.  We're going to make a form and update one of the elements of that form every .01 seconds.    Here's the entire code to do that.


    import PySimpleGUI as sg
    import time

    # form that doesn't block
    # Make a form, but don't use context manager
    form = sg.FlexForm('Running Timer', auto_size_text=True)

    # Create the layout
    form_rows = [[sg.Text('Non-blocking GUI with updates')],
                 [sg.Text('', size=(8, 2), font=('Helvetica', 20), key='output')    ],
                 [sg.SimpleButton('Quit')]]
    # Layout the rows of the form and perform a read. Indicate the form is non-blocking!
    form.LayoutAndRead(form_rows, non_blocking=True)

    #
    # Some place later in your code...
    # You need to perform a ReadNonBlocking on your form every now and then or
    # else it won't refresh
    #

    for i in range(1, 1000):
        form.FindElement('output').Update('{:02d}:{:02d}.{:02d}'.format(*divmod(int(i / 100), 60), i % 100))
        button, values = form.ReadNonBlocking()
        if values is None or button == 'Quit':
            break
        time.sleep(.01)
    else:
        form.CloseNonBlockingForm()


What we have here is the same sequence of function calls as in the description.  Get a form, add rows to it, show the form, and then refresh it every now and then.

The new thing in this example is the call use of the Update method for the Text Element.  The first thing we do inside the loop is "update" the text element that we made earlier.  This changes the value of the text field on the form.  The new value will be displayed when `form.ReadNonBlocking()` is called.  if you want to have the form reflect your changes immediately, call `form.Refresh()`.

Note the `else` statement on the for loop.  This is needed because we're about to exit the loop while the form is still open.  The user has not closed the form using the X nor a button so it's up to the caller to close the form using `CloseNonBlockingForm`.

## Keyboard & Mouse Capture
Beginning in version 2.10 you can capture keyboard key presses and mouse scroll-wheel events.   Keyboard keys can be used, for example, to detect the page-up and page-down keys for a PDF viewer.  To use this feature, there's a boolean setting in the FlexForm call `return_keyboard_events` that is set to True in order to get keys returned along with buttons.

Keys and scroll-wheel events are returned in exactly the same way as buttons.

For scroll-wheel events, if the mouse is scrolled up, then the `button` text will be `MouseWheel:Up`.   For downward scrolling, the text returned is `MouseWheel:Down`

Keyboard keys return 2 types of key events. For "normal" keys (a,b,c, etc), a single character is returned that represents that key.  Modifier and special keys are returned as a string with 2 parts:

    Key Sym:Key Code

Key Sym is a string such as 'Control_L'.  The Key Code is a numeric representation of that key.  The left control key, when pressed will return the value 'Control_L:17'

    import PySimpleGUI as sg

    # Recipe for getting keys, one at a time as they are released
    # If want to use the space bar, then be sure and disable the "default focus"

    with sg.FlexForm("Keyboard Test", return_keyboard_events=True, use_default_focus=False) as form:
        text_elem = sg.Text("", size=(18,1))
        layout = [[sg.Text("Press a key or scroll mouse")],
                  [text_elem],
                  [sg.SimpleButton("OK")]]

        form.Layout(layout)
        # ---===--- Loop taking in user input --- #
      while True:
            button, value = form.ReadNonBlocking()

            if button == "OK"  or (button is None and value is None):
                print(button, "exiting")
                break
            if button is not None:
                text_elem.Update(button)

You want to turn off the default focus so that there no buttons that will be selected should you press the spacebar.

### Realtime Keyboard Capture
Use realtime keyboard capture by calling

    import PySimpleGUI as sg

    with sg.FlexForm("Realtime Keyboard Test", return_keyboard_events=True, use_default_focus=False) as form:
        layout = [[sg.Text("Hold down a key")],
                  [sg.SimpleButton("OK")]]

        form.Layout(layout)

        while True:
            button, value = form.ReadNonBlocking()

            if button == "OK":
                print(button, value, "exiting")
                break
		    if button is not None:
                print(button)
            elif value is None:
                break

## Menus

Beginning in version 3.01 you can add a menubar to your form/window.  You specify the menus in much the same way as you do form layouts, with lists.  Menu selections are returned as button clicks, so be aware of your overall naming conventions.  If you have an Exit button and also an Exit menu option, then you won't be able to tell the difference when your form.Read returns.  Hopefully will not be a problem.

This definition:

    menu_def = [['File', ['Open', 'Save', 'Exit',]],
                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                ['Help', 'About...'],]

Note the placement of ',' and of [].  It's tricky to get the nested menus correct that implement cascading menus.  See how paste has Special and Normal as a list after it.  This means that Paste has a cascading menu with items Special and Normal.

They menu_def layout produced this window:

![menu](https://user-images.githubusercontent.com/13696193/45306723-56b7cb00-b4eb-11e8-8cbd-faef0c90f8b4.jpg)




## Updating Elements

This is a somewhat advanced topic...

Typically you perform Element updates in response to events from other Elements.  An example is that when you click a button some text on the form changes to red.  You can change the Element's attributes, or at least some of them, and the Element's value.

In some source code examples you will find an older techique for updating elements that did not involve keys.  If you see a technique in the code that does not use keys, then know that there is a version using keys that is easier.

Here's the key's version....
We have an InputText field that we want to update.  When the Element was created we used this call:

    sg.Input(key='input')

To update or change the value for that Input Element, we use this contruct:

    form.FindElement('input').Update('new text')

Using the '.' makes the code shorter.  The FindElement call returns an Element.  We then call that Element's Update function.

See the Font Sizer demo for example source code.

## Sample Applications

Use the example programs as a starting basis for your GUI.  Copy, paste, modify and run!  The demo files are:

  | Source File| Description |
|--|--|
|**Demo_All_Widgets.py**| Nearly all of the Elements shown in a single form
|**Demo_Borderless_Window.py**| Create clean looking windows with no border
|**Demo_Button_States.py**| One way of implementing disabling of buttons
|**Demo_Calendar.py** | Demo of the Calendar Chooser button
|**Demo_Canvas.py** | Form with a Canvas Element that is updated outside of the form
|**Demo_Chat.py** | A chat window with scrollable history
|**Demo_Chatterbot.py** | Front-end to Chatterbot Machine Learning project
|**Demo_Color.py** | How to interact with color using RGB hex values and named colors
|**Demo_Columns.py** | Using the Column Element to create more complex forms
|**Demo_Compare_Files.py** | Using a simple GUI front-end to create a compare 2-files utility
|**Demo_Cookbook_Browser.py** | Source code browser for all Recipes in Cookbook
|**Demo_Dictionary.py** | Specifying and using return values in dictionary format
**Demo_DOC_Viewer_PIL.py** | Display a PDF, HTML, ebook file, etc in your form
|**Demo_DisplayHash1and256.py** | Using high level API and custom form to implement a simple display hash code utility
|**Demo_DuplicateFileFinder.py** | High level API used to get a folder that is used by utility that finds duplicate files. Uses progress meter to show progress. 2 lines of code required to add GUI and meter
|**Demo_Fill_Form.py** | How to perform a bulk-fill for a form.  Saving and loading a form from disk
|**Demo Font Sizer.py** | Demonstrates Elements updating other Elements
|**Demo_Func_Callback_Simulator.py** | For the Raspberry Pi crowd. Event loop that simulates traditional GUI callback functions should you already have an architecture that uses them
|**Demo_GoodColors.py** | Using some of the pre-defined PySimpleGUI individual colors
|**Demo_HowDoI.py** | This is a utility to be experienced! It will change how you code
|**Demo_Img_Viewer.py** | Display jpg, png,tiff, bmp files
|**Demo_Keyboard.py** | Using blocking keyboard events
|**Demo_Keyboard_Realtime.py** | Using non-blocking / realtime keyboard events
|**Demo_Machine_Learning.py** | A sample Machine Learning front end
|**Demo_Matplotlib.py** | Integrating with Matplotlib to create a single graph
|**Demo_Matplotlib_Animated.py** | Animated Matplotlib line graph
|**Demo_Matplotlib_Animated_Scatter.py** | Animated Matplotlib scatter graph
|**Demo_Matplotlib_Browser.py** | Browse Matplotlib gallery
|**Demo_Media_Player.py** | Non-blocking form with a media player layout.  Demonstrates  button graphics, Update method
|**Demo_MIDI_Player.py** | GUI wrapper for Mido MIDI package. Functional MIDI player that controls attached MIDI devices
|**Demo_NonBlocking_Form.py** | a basic async form
|** Demo_OpenCV.py** | Integrated with OpenCV
|** Demo_Password_Login** | Password protection using SHA1
|**Demo_PDF_Viewer.py** | Submitted by a user!  Previews PDF documents. Uses keyboard input & mouse scrollwheel to navigate
|**Demo_Pi_LEDs.py** | Control GPIO using buttons
|**Demo_Pi_Robotics.py** | Simulated robot control using realtime buttons
|**Demo_PNG_Vierwer.py** | Uses Image Element to display PNG files
|**Demo_Recipes.py** | A collection of various Recipes.  Note these are not the same as the Recipes in the Recipe Cookbook
|**Demo_Script_Launcher.py** | Demonstrates one way of adding a front-end onto several command line scripts
|**Demo_Script_Parameters.py** | Add a 1-line GUI to the front of your previously command-line only scripts
|**Demo_Tabbed_Form.py** | Using the Tab feature
|**Demo_Table_Simulation.py** | Use input fields to display and edit tables
|**Demo_Timer.py** | Simple non-blocking form

## Packages Used In Demos


  While the core PySimpleGUI code  does not utilize any 3rd party packages, some of the demos do.  They add a GUI to a few popular packages.  These packages include:
  * [Chatterbot](https://github.com/gunthercox/ChatterBot)
  * [Mido](https://github.com/olemb/mido)
  * [Matplotlib](https://matplotlib.org/)
  * [PyMuPDF](https://github.com/rk700/PyMuPDF)

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

**Progress Meters** - the visual graphic portion of the meter may be off.  May return to the native tkinter progress meter solution in the future.  Right now a "custom" progress meter is used.  On the bright side, the statistics shown are extremely accurate and can tell you something about the performance of your code.

**Async Forms** - these include the 'easy' forms (EasyProgressMeter and EasyPrint/Print). If you start overlapping having Async forms open with normal forms then things get a littler squirrelly.  Still tracking down the issues and am making it more solid every day possible.  You'll know there's an issue when you see blank form.

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


### Release Notes
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

One change that will set PySimpleGUI apart is the parlor trick of being able to move the window by clicking on it anywhere.  This is turned on by default.  It's not a common way to interact with windows.  Normally you have to move using the titlebar.  Not so with PySimpleGUI.  Now you can drag using any part of the window.  You will want to turn this off for windows with sliders.  This feature is enabled in the FlexForm call.

Related to the Grab Anywhere feature is the no_titlebar option, again found in the call to FlexForm.  Your window will be a spiffy, borderless window.  It's a really interesting effect.  Slight problem is that you do not have an icon on the taskbar with these types of windows, so if you don't supply a button to close the window, there's no way to close it other than task manager.

3.0.2 Still making changes to Update methods with many more ahead in the future.  Continue to mess with grab anywhere option.  Needed to disable in more places such as the PopupGetText function.  Any time these is text input on a form, you generally want to turn off the grab anywhere feature.

3.2.0 Biggest change was the addition of the Table Element.  Trying to make changes so that form resizing is a possibility but unknown if will work in the long run.  Removed all MsgBox, Get* functions and replaced with Popup functions.  Popups had multiple new parameters added to change the look and feel of a popup.


### Upcoming
Make suggestions people!  Future release features

Port to other graphic engines.  Hook up the front-end interface to a backend other than tkinter.  Qt, WxPython, etc.  WxPython is higher priority.



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


## Author
MikeTheWatchGuy

## Demo Code Contributors

JorjMcKie - PDF and image viewers (plus a number of code suggestions)

## License

GNU Lesser General Public License (LGPL 3) +

## Acknowledgments

* Jorj McKie was the motivator behind the entire project. His wxsimpleGUI concepts sparked PySimpleGUI into existence
* [Fredrik Lundh](https://wiki.python.org/moin/FredrikLundh) for his work on `tkinter`
* [Ruud van der Ham](https://forum.pythonistacafe.com/u/Ruud) for all the help he's provided as a Python-mentor. Quite a few tricky bits of logic was supplied by Ruud. The dual-purpose return values scheme is Ruud's for example
* **Numerous** users who provided feature suggestions!  Many of the cool features were suggested by others.  If you were one of them and are willing to take more credit, I'll list you here if you give me permission. Most are too modest
* [moshekaplan](https://github.com/moshekaplan)/**[tkinter_components](https://github.com/moshekaplan/tkinter_components)** wrote the code for the Calendar Chooser Element. It was lifted straight from GitHub
* [Bryan Oakley](https://stackoverflow.com/users/7432/bryan-oakley) for the code that enables the `grab_anywhere` feature.


## How Do I
Finally, I must thank the fine folks at How Do I.
https://github.com/gleitz/howdoi
Their utility has forever changed the way and pace in which I can program.  I urge you to try the HowDoI.py application here on GitHub.  Trust me, **it's going to be worth the effort!**
Here are the steps to run that application

    Install howdoi:
          pip install howdoi
    Test your install:
          python -m howdoi howdoi.py
    To run it:
          Python HowDoI.py

The pip command is all there is to the setup.

The way HowDoI works is that it uses your search term to look through stack overflow posts. It finds the best answer, gets the code from the answer, and presents it as a response.  It gives you the correct answer OFTEN.  It's a miracle that it work SO well.
For Python questions, I simply start my query with 'Python'.  Let's say you forgot how to reverse a list in Python.  When you run HowDoI and ask this question, this is what you'll see.

![howdoiwithhistory](https://user-images.githubusercontent.com/13696193/45064009-5fd61180-b07f-11e8-8ead-eb0d1ff3a6be.jpg)



In the hands of a competent programmer, this tool is **amazing**.   It's a must-try kind of program that has completely changed my programming process.  I'm not afraid of asking for help!  You just have to be smart about using what you find.

The PySimpleGUI window that the results are shown in is an 'input' field which means you can copy and paste the results right into your code.



