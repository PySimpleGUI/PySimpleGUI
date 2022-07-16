▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓  WHAT, HOW, WHEN?  ▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
============= Format =============

## Title | shortcuts

Description

PYTHON CODE

IMAGE

init_call

methods

---

additions

<!-- Start from here -->

# PEP8 Bindings For Methods and Functions

Beginning with release 4.3 of PySimpleGUI, ***all methods and function calls*** have PEP8 equivalents.  This capability is only available, for the moment, on the PySimpleGUI tkinter port.  It is being added, as quickly as possible, to all of the ports.

As long as you know you're sticking with tkinter for the short term, it's safe to use the new bindings.

## The Non-PEP8 Methods and Functions

Why the need for these bindings?  Simply put, the PySimpleGUI SDK has a PEP8 violation in the method and function names.  PySimpleGUI uses CamelCase names for methods and functions.  PEP8 suggests using snake_case_variables instead.

This has not caused any problems and few complaints, but it's important the the interfaces into PySimpleGUI be compliant.  Perhaps one of the reasons for lack of complaints is that the Qt library also uses SnakeCase for its methods.  This practice has the effect of labelling a package as being "not Pythonic" and also suggests that this package was originally used in another language and then ported to Python.  This is exactly the situation with Qt.  It was written for C++ and the interfaces continue to use C++ conventions.

***PySimpleGUI was written in Python, for Python.***  The reason for the name problem was one of ignorance.  The PEP8 convention wasn't understood by the developers when PySimpleGUI was designed and implemented.

You can, and will be able to for some time, use both names.  However, at some point in the future, the CamelCase names will disappear.  A utility is planned to do the conversion for the developer when the old names are remove from PySimpleGUI.

The help system will work with both names as will your IDE's docstring viewing.  However, the result found will show the CamelCase names.  For example `help(sg.Window.read)` will show the CamelCase name of the method/function.  This is what will be returned:

`Read(self, timeout=None, timeout_key='__TIMEOUT__', close=False)`

## The Renaming Convention

To convert a CamelCase method/function name to snake_case, you simply place an `_` where the Upper Case letter is located.  If there are none, then only the first letter is changed.

`Window.FindElement` becomes `Window.find_element`

## Class Variables

For the time being, class variables will remain the way they are currently.  It is unusual, in PySimpleGUI, for class variables to be modified or read by the user code so the impact of leaving them is rarely seen in your code.


# High Level API Calls  - Popup's

"High level calls" are those that start with "popup".    They are the most basic form of communications with the user.   They are named after the type of window they create, a pop-up window.  These windows are meant to be short lived while, either delivering information or collecting it, and then quickly disappearing.

Think of Popups as your first windows, sorta like your first bicycle. It worked well, but was limited.  It probably wasn't long before you wanted more features and it seemed too limiting for your newly found sense of adventure.

When you've reached the point with Popups that you are thinking of filing a GitHub "Enhancement Issue" to get the Popup call extended to include a new feature that you think would be helpful.... not just to you but others is what you had in mind, right?  For the good of others.

Well, don't file that enhancement request.  Instead, it's at THIS time that you should immediately turn to the section entitled "Custom Window API Calls - Your First Window".  Congratulations, you just graduated and are now an official "GUI Designer".  Oh, never mind that you only started learning Python 2 weeks ago, you're a real GUI Designer now so buck up and start acting like one.  Write a popup function of your own.  And then, compact that function down to a **single line of code**.  Yes, these popups can be written in 1 line of code.  The secret is to use the `close` parameter on your call to `window.read()`

But, for now, let's stick with these 1-line window calls, the Popups.   This is the list of popup calls available to you:

popup_animated
popup_annoying
popup_auto_close
popup_cancel
popup_error
popup_get_file
popup_get_folder
popup_get_text
popup_no_border
popup_no_buttons
popup_no_frame
popup_no_titlebar
popup_no_wait
popup_notify
popup_non_blocking
popup_ok
popup_ok_cancel
popup_quick
popup_quick_message
popup_scrolled
popup_timed
popup_yes_no


## Popup Output

Think of the `popup` call as the GUI equivalent of a  `print` statement.  It's your way of displaying results to a user in the windowed world.  Each call to Popup will create a new Popup window.

`popup` calls are normally blocking.  your program will stop executing until the user has closed the Popup window.  A non-blocking window of Popup discussed in the async section.

Just like a print statement, you can pass any number of arguments you wish.  They will all be turned into strings and displayed in the popup window.

There are a number of Popup output calls, each with a slightly different look or functionality (e.g. different button labels, window options).

The list of Popup output functions are:
- popup
- popup_ok
- popup_yes_no
- popup_cancel
- popup_ok_cancel
- popup_error
- popup_timed, popup_auto_close, popup_quick, popup_quick_message
- popup_no_waitWait, popup_non_blocking
- popup_notify

The trailing portion of the function name after Popup indicates what buttons are shown.  `PopupYesNo` shows a pair of button with Yes and No on them.   `PopupCancel` has a Cancel button, etc..

While these are "output" windows, they do collect input in the form of buttons.  The Popup functions return the button that was clicked.  If the Ok button was clicked, then Popup returns the string 'Ok'.  If the user clicked the X button to close the window, then the button value returned is `None` or `WIN_CLOSED` is more explicit way of writing it.

The function `popup_timed` or `popup_auto_close` are popup windows that will automatically close after come period of time.

Here is a quick-reference showing how the Popup calls look.

```python
sg.popup('popup')  # Shows OK button
sg.popup_ok('popup_ok')  # Shows OK button
sg.popup_yes_no('popup_yes_no')  # Shows Yes and No buttons
sg.popup_cancel('popup_cancel')  # Shows Cancelled button
sg.popup_ok_cancel('popup_ok_cancel')  # Shows OK and Cancel buttons
sg.popup_error('popup_error')  # Shows red error button
sg.popup_timed('popup_timed')  # Automatically closes
sg.popup_auto_close('popup_auto_close')  # Same as PopupTimed
```

Preview of popups:

<p style="display: flex;justify-content: space-around;">
	<img src="https://user-images.githubusercontent.com/13696193/44957394-1380ab00-aea0-11e8-98b1-1ab7d7bd5b37.jpg">
	<img src="https://user-images.githubusercontent.com/13696193/44957400-167b9b80-aea0-11e8-9d42-2314f24e62de.jpg">
	<img src="https://user-images.githubusercontent.com/13696193/44957399-154a6e80-aea0-11e8-9580-e716f839d400.jpg">
</p>

<p style="display: flex;justify-content: space-around;">
	<img src="https://user-images.githubusercontent.com/13696193/44957398-14b1d800-aea0-11e8-9e88-c2b36a248447.jpg">
	<img src="https://user-images.githubusercontent.com/13696193/44957397-14b1d800-aea0-11e8-950b-6d0b4f33841a.jpg">
	<img src="https://user-images.githubusercontent.com/13696193/44957396-14194180-aea0-11e8-8eef-bb2e1193ecfa.jpg">
	<img src="https://user-images.githubusercontent.com/13696193/44957595-9e15da00-aea1-11e8-8909-6b6121b74509.jpg">
</p>

<!-- <+func.popup+> -->

The other output Popups are variations on parameters.  Usually the button_type parameter is the primary one changed.

The choices for button_type are (you should not specify these yourself however):

```
POPUP_BUTTONS_YES_NO
POPUP_BUTTONS_CANCELLED
POPUP_BUTTONS_ERROR
POPUP_BUTTONS_OK_CANCEL
POPUP_BUTTONS_OK
POPUP_BUTTONS_NO_BUTTONS
```

**Note that you should not call Popup yourself with different button_types.**  Rely on the Popup function named that sets that value for you.  For example `popup_yes_no` will set the button type to POPUP_BUTTONS_YES_NO for you.

### Scrolled Output
There is a scrolled version of Popups should you have a lot of information to display.

<!-- <+func.popup_scrolled+> -->


Typical usage:

```python
sg.popup_scrolled(my_text)
```


![scrolledtextbox 2](https://user-images.githubusercontent.com/13696193/43667324-712aa0d4-9745-11e8-83a9-a0d0570d0865.jpg)


The `popup_scrolled` will auto-fit the window size to the size of the text.  Specify `None` in the height field of a `size` parameter to get auto-sized height.

This call will create a scrolled box 80 characters wide and a height dependent upon the number of lines of text.

`sg.popup_scrolled(my_text, size=(80, None))`

Note that the default max number of lines before scrolling happens is set to 50. At 50 lines the scrolling will begin.

If `non_blocking` parameter is set, then  the call will not blocking waiting for the user to close the window.  Execution will immediately return to the user.  Handy when you want to dump out debug info without disrupting the program flow.


### Non-Blocking Popups - popup_no_wait and the non_blocking parameter

<!-- <+func.popup_no_wait+> -->

The `popup` call `popup_no_wait` or `popup_non_blocking` will create a popup window and then immediately return control back to you.  You can turn other popup calls into non-blocking popups if they have a `non_blocking` parameter.  Setting `non_blocking` to True will cause the function to return immediately rather than waiting for the window to be closed.

This function is very handy for when you're **debugging** and want to display something as output but don't want to change the programs's overall timing by blocking.  Think of it like a `print` statement. There are no return values on one of these Popups.


### Popup Parameter Combinations

So that you don't have to specify a potentially long list common parameters there are a number of popup functions that set combinations of parameters.  For example `popup_quick_message` will show a non-blocking popup that autocloses and does not have a titlebar.  You could achieve this same end result using the plain `popup` call.



## Popup Input

There are Popup calls for single-item inputs. These follow the pattern of `popup_get` followed by the type of item to get.  There are 3 of these input Popups to choose from, each with settings enabling customization.

- `popup_get_text` - get a single line of text
- `popup_get_file` - get a filename
- `popup_get_folder` - get a folder name

Use these Popups instead of making  a custom window to get one data value, call the Popup input function to get the item from the user.  If you find the parameters are unable to create the kind of window you are looking for, then it's time for you to create your own window.


### popup_get_text
Use this Popup to get a line of text from the user.

<!-- <+func.popup_get_text+> -->


```python
import PySimpleGUI as sg
text = sg.popup_get_text('Title', 'Please input something')
sg.popup('Results', 'The value returned from PopupGetText', text)
```

![popupgettext](https://user-images.githubusercontent.com/13696193/44957281-8721b880-ae9e-11e8-98cd-d06369f4187e.jpg)

![popup gettext response](https://user-images.githubusercontent.com/13696193/44957282-8721b880-ae9e-11e8-84ae-dc8bb30504a0.jpg)

### popup_get_file

Gets one or more filenames from the user.  There are options to configure the type of dialog box to show.  Normally an "Open File" dialog box is shown.

<!-- <+func.popup_get_file+> -->


If configured as an Open File Popup then (save_as is not True)  the dialog box will look like this.

![snag-0060](https://user-images.githubusercontent.com/13696193/46761050-9831c680-cca1-11e8-8de9-68b15efe2c46.jpg)

If you set the parameter save_As to True, then the dialog box looks like this:

![snag-0061](https://user-images.githubusercontent.com/13696193/46761330-2b6afc00-cca2-11e8-953b-f6b5c5ce57f5.jpg)

If you choose a filename that already exists, you'll get a warning popup box asking if it's OK.  You can also specify a file that doesn't exist.  With an "Open" dialog box you cannot choose a non-existing file.

A typical call produces this window.

```python
text = sg.popup_get_file('Please enter a file name')
sg.popup('Results', 'The value returned from popup_get_file', text)
```

![popupgetfile](https://user-images.githubusercontent.com/13696193/44957857-2fd31680-aea5-11e8-8eb7-f6b91c202cc8.jpg)

### popup_get_folder

The window created to get a folder name looks the same as the get a file name.  The difference is in what the browse button does.  `popup_get_file` shows an Open File dialog box while `popup_get_folder`  shows an Open Folder dialog box.

<!-- <+func.popup_get_folder+> -->

This is a typical call

```python
	text = sg.popup_get_folder('Please enter a folder name')
	sg.popup('Results', 'The value returned from popup_get_folder', text)
```

![popupgetfolder](https://user-images.githubusercontent.com/13696193/44957861-45484080-aea5-11e8-926c-cf607a45251c.jpg)

### popup_animated

![ring](https://user-images.githubusercontent.com/13696193/51296743-6ee4ad00-19eb-11e9-91f5-cd8086ad1b50.gif)

The animated Popup enables you to easily display a "loading" style animation specified through a GIF file that is either stored in a file or a base64 variable.

<!-- <+func.popup_animated+> -->


***To close animated popups***, call PopupAnimated with `image_source=None`.  This will close all of the currently open PopupAnimated windows.


# Progress Meters!
We all have loops in our code.  'Isn't it joyful waiting, watching a counter scrolling past in a text window?  How about one line of code to get a progress meter, that contains statistics about your code?

<!-- <+func.one_line_progress_meter+> -->

Here's the one-line Progress Meter in action!

```python
for i in range(1,10000):
	sg.one_line_progress_meter('My Meter', i+1, 10000, 'key','Optional message')
```

That line of code resulted in this window popping up and updating.

![preogress meter](https://user-images.githubusercontent.com/13696193/43667625-d47da702-9746-11e8-91e6-e5177883abae.jpg)

A meter AND fun statistics to watch while your machine grinds away, all for the price of 1 line of code.
With a little trickery you can provide a way to break out of your loop using the Progress Meter window.  The cancel button results in a `False` return value from `one_line_progress_meter`.  It normally returns `True`.

***Be sure and add one to your loop counter*** so that your counter goes from 1 to the max value.  If you do not add one, your counter will never hit the max value.  Instead it will go from 0 to max-1.

# Debug Output (easy_print = Print = eprint)

Another call in the 'Easy' families of APIs is `EasyPrint`.  As is with other commonly used PySimpleGUI calls, there are other names for the same call.  You can use `Print` or `eprint` in addition to `EasyPrint`.  They all do the same thing, output to a debug window.  If the debug window isn't open, then the first call will open it.  No need to do anything but stick an 'sg.Print' call in your code. You can even replace your 'print' calls with calls to EasyPrint by simply sticking the statement

```python
print = sg.Print
```

at the top of your code.

`Print` is one of the better ones to use as it's easy to remember.   It is simply `print` with a capital P. `sg.Print('this will go to the debug window')`

```python
import PySimpleGUI as sg

for i in range(100):
	sg.Print(i)
```

![snap0125](https://user-images.githubusercontent.com/13696193/43114979-a696189e-8ecf-11e8-83c7-473fcf0ccc66.jpg)

Or if you didn't want to change your code:

```python
import PySimpleGUI as sg

print=sg.Print
for i in range(100):
    print(i)
```

Just like the standard print call, `easy_print` supports the `sep` and `end` keyword arguments.  Other names that can be used to call `easy_print` include `Print`, `eprint`,   If you want to close the window, call the function `easy_print_close`.

You can change the size of the debug window using the `set_options` call with the `debug_win_size` parameter.

There is an option to tell PySimpleGUI to reroute all of your stdout and stderr output to this window.  To do so call easy_print with the parameter `do_not_reroute_stdout` set to `False`.  After calling it once with this parameter set to True, all future calls to a normal `print` will go to the debug window.

If you close the debug window it will re-open the next time you Print to it.  If you wish to close the window using your code, then you can call either `easy_print_close()` or `PrintClose()`


### Printing To Multiline Elements

Another technique for outputting information that you would normally print is to use the function `Multiline.print`.  You'll find it discussed further into this document.  The basic idea is that you can easily modify your normal `print` calls to route your printed information to your window.


---
# Custom window API Calls  (Your First window)

This is the FUN part of the programming of this GUI.  In order to really get the most out of the API, you should be using an IDE that supports auto complete or will show you the definition of the function.  This will make customizing go  smoother.

This first section on custom windows is for your typical, blocking, non-persistent window.  By this I mean, when you "show" the window, the function will not return until the user has clicked a button or closed the window with an X.

Two other types of windows exist.
1. Persistent window - the `Window.read()` method returns and the window continues to be visible.  This is good for applications like a chat window or a timer or anything that stays active on the screen for a while.
2. Asynchronous window - the trickiest of the lot. Great care must be exercised.  Examples are an MP3 player or status dashboard.  Async windows are updated (refreshed) on a periodic basis.  You can spot them easily as they will have a `timeout` parameter on the call to read.     `event, values = window.read(timeout=100)`

It's both not enjoyable nor helpful to immediately jump into tweaking each and every little thing available to you.  Make some simple windows.  Use the Cookbook and the Demo Programs as a way to learn and as a "starting point".

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

```
[ sg.Text('Enter a number') ]
```

Row 2 has 1 elements, an input field.

```
[ sg.Input() ]
```

Row 3 has an OK button

```
[ sg.OK() ]
```

Now that we've got the 3 rows defined, they are put into a list that represents the entire window.

```
layout = [ [sg.Text('Enter a Number')],
           [sg.Input()],
           [sg.OK()] ]
```

Finally we can put it all together into a program that will display our window.

```python
import PySimpleGUI as sg

layout = [[sg.Text('Enter a Number')],
          [sg.Input()],
          [sg.OK()] ]

window = sg.Window('Enter a number example', layout)

event, values = window.read()

window.close()

sg.Popup(event, values[0])
```

Your call to `read` will normally return a dictionary, but will "look like a list" in how you access it.  The first input field will be entry 0, the next one is 1, etc..  Later you'll learn about the `key` parameter which allows you to use your own values to identify elements instead of them being numbered for you.



### Example 2 - Get a filename
Let's say you've got a utility you've written that operates on some input file and you're ready to use a GUI to enter than filename rather than the command line.  Follow the same steps as the previous example - draw your window on paper, break it up into rows, label the elements.

![gui4_1](https://user-images.githubusercontent.com/13696193/44160132-6a584900-a087-11e8-862f-7d791a67ee5d.JPG)
![gui5_1](https://user-images.githubusercontent.com/13696193/44160133-6af0df80-a087-11e8-9dec-bb4d4c59393d.JPG)

Writing the code for this one is just as straightforward.  There is one tricky thing, that browse for a file button.  Thankfully PySimpleGUI takes care of associating it with the input field next to it.  As a result, the code looks almost exactly like the window on the paper.

```python
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Filename')],
			[sg.Input(), sg.FileBrowse()],
			[sg.OK(), sg.Cancel()] ]

window = sg.Window('Get filename example', layout)
event, values = window.read()
window.close()

sg.Popup(event, values[0])
```

Read on for detailed instructions on the calls that show the window and return your results.

# Copy these design patterns!

All of your PySimpleGUI programs will utilize one of these 2 design patterns depending on the type of window you're implementing.

Beginning in release 4.19.0 the constant WIN_CLOSED replaced using `None` as the event signaling that a window was closed.

## Pattern 1 A - "One-shot Window" - Read a window one time then close it

This will be the most common pattern you'll follow if you are not using an "event loop" (not reading the window multiple times).  The window is read and closed.

The input fields in your window will be returned to you as a dictionary (syntactically it looks just like a list lookup)

```python
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful


layout = [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
				 [sg.InputText(), sg.FileBrowse()],
				 [sg.Submit(), sg.Cancel()]]

window = sg.Window('SHA-1 & 256 Hash', layout)

event, values = window.read()
window.close()

source_filename = values[0]     # the first input element is values[0]
```

## Pattern 1 B - "One-shot Window" - Read a window one time then close it (compact format)

Same as Pattern 1, but done in a highly compact way.  This example uses the `close` parameter in `window.read` to automatically close the window as part of the read operation (new in version 4.16.0).  This enables you to write a single line of code that will create, display, gather input and close a window.  It's really powerful stuff!

```python
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

event, values  = sg.Window('SHA-1 & 256 Hash', [[sg.Text('SHA-1 and SHA-256 Hashes for the file')],
				        [sg.InputText(), sg.FileBrowse()],
				        [sg.Submit(), sg.Cancel()]]).read(close=True)

source_filename = values[0]     # the first input element is values[0]
```


## Pattern 2 A - Persistent window (multiple reads using an event loop)

Some of the more advanced programs operate with the window remaining visible on the screen.  Input values are collected, but rather than closing the window, it is kept visible acting as a way to both output information to the user and gather input data.

This code will present a window and will print values until the user clicks the exit button or closes window using an X.

```python
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Persistent window')],
		  [sg.Input()],
		  [sg.Button('Read'), sg.Exit()]]

window = sg.Window('Window that stays open', layout)

while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Exit':
		break
	print(event, values)

window.close()
```

## Pattern 2 B - Persistent window (multiple reads using an event loop + updates data in window)

This is a slightly more complex, but maybe more realistic version that reads input from the user and displays that input as text in the window.  Your program is likely to be doing both of those activities (input and output) so this will give you a big jump-start.

Do not worry yet what all of these statements mean.   Just copy it so you can begin to play with it, make some changes.  Experiment to see how thing work.

This example introduces the concept of "keys".  Keys are super important in PySimpleGUI as they enable you to identify and work with Elements using names you want to use.  Keys can be (almost) ANYTHING, except `None` or a List (a tuple is fine).  To access an input element's data that is read in the example below, you will use `values['-IN-']` instead of `values[0]` like before.

```python
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(12,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # change the "output" element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
```

### Qt Designer

There actually is a PySimpleGUI Window Designer that uses Qt's window designer.  It's outside the scope of this document however.  You'll find the project here: https://github.com/nngogol/PySimpleGUIDesigner

I hope to start using it more soon.

## How GUI Programming in Python Should Look?  At least for beginners ?

While one goal was making it simple to create a GUI another just as important goal was to do it in a Pythonic manner. Whether it achieved these goals is debatable, but it was an attempt just the same.

The key to custom windows in PySimpleGUI is to view windows as ROWS of GUI  Elements.  Each row is specified as a list of these Elements.  Put the rows together and you've got a window.  This means the GUI is defined as a series of Lists, a Pythonic way of looking at things.

### Let's dissect this little program

```python
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [[sg.Text('Rename files or folders')],
	  [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
	  [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FileBrowse()],
	  [sg.Submit(), sg.Cancel()]]

window = sg.Window('Rename Files or Folders', layout)

event, values = window.read()
window.close()
folder_path, file_path = values[0], values[1]       # get the data from the values dictionary
print(folder_path, file_path)
```

### Themes

![image](https://user-images.githubusercontent.com/46163555/70470775-cd01ff00-1a99-11ea-8b9c-8b33c8880c99.png)

The first line of code after the import is a call to `theme`.

Until Dec 2019 the way a "theme" was specific in PySimpleGUI was to call `change_look_and_feel`.  That call has been replaced by the more simple function `theme`.


### Window contents (The Layout)

Let's agree the window has 4 rows.

The first row only has **text** that reads `Rename files or folders`

The second row has 3 elements in it.  First the **text** `Source for Folders`, then an **input** field, then a **browse** button.

Now let's look at how those 2 rows and the other two row from Python code:

```python
layout = [[sg.Text('Rename files or folders')],
          [sg.Text('Source for Folders', size=(15, 1)), sg.InputText(), sg.FolderBrowse()],
          [sg.Text('Source for Files ', size=(15, 1)), sg.InputText(), sg.FileBrowse()],
          [sg.Submit(), sg.Cancel()]]
```

See how the source code mirrors the layout?  You simply make lists for each row, then submit that table to PySimpleGUI to show and get values from.

And what about those return values?  Most people simply want to show a window, get the input values and do something with them.  So why break up the code into button callbacks, etc., when I simply want my window's input values to be given to me.

For return values the window is scanned from top to bottom, left to right.  Each field that's an input field will occupy a spot in the return values.

In our example window, there are 2 fields, so the return values from this window will be a dictionary with 2 values in it.  Remember, if you do not specify a `key` when creating an element, one will be created for you.  They are ints starting with 0.  In this example, we have 2 input elements.  They will be addressable as values[0] and values[1]

### "Reading" the window's values (also displays the window)

```python
event, values = window.read()
folder_path, file_path = values[0], values[1]
```

In one statement we both show the window and read the user's inputs.  In the next line of code the *dictionary* of return values is split into individual variables `folder_path` and `file_path`.

Isn't this what a Python programmer looking for a GUI wants? Something easy to work with to get the values and move on to the rest of the program, where the real action is taking place.  Why write pages of GUI code when the same layout can be achieved with PySimpleGUI in 3 or 4 lines of code.  4 lines or 40?  Most would choose 4.


## Return values

There are 2 return values from a call to `Window.read()`, an `event` that caused the `Read` to return and `values` a list or dictionary of values.  If there are no elements with keys in the layout, then it will be a list.  However, some elements, like some buttons, have a key automatically added to them.  **It's best to use keys on all of your input type elements.**

### Two Return Values

All Window Read calls return 2 values.  By convention a read statement is written:

```python
event, values = window.read()
```

You don't HAVE to write your reads in this way. You can name your variables however you want.  But if you want to code them in a way that other programmers using PySimpleGUI are used to, then use this statement.

## Events

The first parameter `event` describes **why** the read completed.  Events are one of these:

For all Windows:

* Button click
* Window closed using X

For Windows that have specifically enabled these.  Please see the appropriate section in this document to learn about how to enable these and what the event return values are.

* Keyboard key press
* Mouse wheel up/down
* Menu item selected
* An Element Changed (slider, spinner, etc.)
* A list item was clicked
* Return key was pressed in input element
* Timeout waiting for event
* Text was clicked
* Combobox item chosen
* Table row selected
* etc.

***Most*** of the time the event will be a button click or the window was closed.  The other Element-specific kinds of events happen when you set `enable_events=True` when you create the Element.

### Button Click Events

By default buttons will always return a click event, or in the case of realtime buttons, a button down event.  You don't have to do anything to enable button clicks.  To disable the events, disable the button using its Update method.

You can enable an additional "Button Modified" event by setting `enable_events=True` in the Button call.  These events are triggered when something 'writes' to a button, ***usually*** it's because the button is listed as a "target" in another button.

The button value from a Read call will be one of 2 values:
1. The Button's text     - Default
2. The Button's key      - If a key is specified

If a button has a key set when it was created, then that key will be returned, regardless of what text is shown on the button.  If no key is set, then the button text is returned.  If no button was clicked, but the window returned anyway, the event value is the key that caused the event to be generated.  For example, if `enable_events` is set on an `Input` Element and someone types a character into that `Input` box, then the event will be the key of the input box.

### Element Events

Some elements are capable of generating events when something happens to them.  For example, when a slider is moved, or list item clicked on or table row clicked on.  These events are not enabled by default.  To enable events for an Element, set the parameter `enable_events=True`.  This is the same as the older `click_submits` parameter.  You will find the `click_submits` parameter still in the function definition.  You can continue to use it. They are the same setting.  An 'or' of the two values is used.  In the future, click_submits will be removed so please migrate your code to using `enable_events`.


|Name|events|
| ---  | --- |
| InputText | any change |
| Combo | item chosen |
| Listbox | selection changed |
| Radio | selection changed |
| Checkbox | selection changed |
| Spinner | new item selected |
| Multiline | any change |
| Text | clicked |
| Status Bar | clicked |
| Graph | clicked |
| Graph | dragged |
| Graph | drag ended (mouse up) |
| TabGroup | tab clicked |
| Slider | slider moved |
| Table | row selected |
| Tree | node selected |
| ButtonMenu | menu item chosen |
| Right click menu | menu item chosen |


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


## Window Closed Events

Detecting and correctly handling Windows being closed is an important part of your PySimpleGUI application.  You will find in every event loop in every Demo Program an if statement that checks for the events that signal that a window has closed.

The most obvious way to close a window is to click the "X" in the upper right corner of the window (on Windows, Linux.... Mac doesn't use an "X" but still has a close button).  On Windows systems, the keyboard keys ALT+F4 will force a Window to close.  This is one way to close a window without using a mouse.  Some programs can also send a "close" command to the window.

Regardless of how the close is performed on the window, PySimpleGUI returns an event for this closure.

### WIN_CLOSED Event

**The constant WIN_CLOSED (None) is returned when the user clicks the X to close a window.**

Typically, the check for a closed window happens right after the `window.read()` call returns.  The reason for this is that operating on a closed window can result in errors.  The check for closure is an "if" statement.

**ALWAYS** include a check for a closed window in your event loop.  

### The Window Closed If Statement

There are 2 forms you'll find for this if statement in the documentation and the Demo Programs.  One is "Pythonic" the other is more understandable by beginners.  This is the format you'll see most often in the PySimpleGUI materials if the window has both a button that is used to signal the user wishes to exit.  In this example, I'm using a "Quit" button:

```python
if event == sg.WIN_CLOSED or event == 'Exit':
    break
```

The more "Pythonic" version of this same statement is:

```python
if event in (sg.WIN_CLOSED, 'Exit'):
    break
```

In case you're yelling at your screen right now that the second form should always be used, remember that many of the PySimpleGUI users are new to  Python.  If the very first example of a PySimpleGUI program they see has that if statement in it, they will instantly be lost before they can even begin their journey.  So, the decision was made to, you guessed it, go SIMPLE.  The statement with the "or" is simpler to understand.

This notion of binary choices in programming that's  crept in over the past couple decades... that there's a "BEST" or "only 1 right way"... loses the sophisticated thinking that a software engineer needs to be successful in a wide variety of situations.  Every situation, every person, every problem... is unique.   **There is no idealized best that always fits.**


### A Complete Example - Traditional Window Closed Check

Let's put this if statement into context so you can see where it goes and how it works with the event loop

```python
import PySimpleGUI as sg

layout = [[sg.Text('Very basic Window')],
          [sg.Text('Click X in titlebar or the Exit button')],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
```

Notice that the line after the while loop is a call to `window.close()`.  The reason for this is that exiting the loop can be in 2 ways. 
* The "X" is clicked
* The Exit button is clicked

If the Exit button is clicked, the window will still be open.  Get in the habit of closing your windows explicitly like this.

If the user clicked "X" and closed the window, then it will have been destroyed by the underlying framework.  You should STILL call `window.close()` because come cleanup work may be needed and there is no harm in closing an already closed window.

tkinter can generate an error/warning sometimes if you don't close the window.  For other ports, such as PySimpleGUIWeb, not closing the Window will potentially cause your program to continue to run in the background.  This can cause your program to not be visible and yet consuming 100% of the CPU time.  Not fun for your users.

### Window Close Confirmation

In 4.33.0 a new parameter, `enable_close_attempted_event`, was added to the `Window` object.  This boolean parameter indicates if you would like to receive an event that a user **wants** to close the window rather than an event that the user **has** closed the window.

To enable this feature, the `Window` is created with something like this:

```python
window = sg.Window('Window Title', layout, enable_close_attempted_event=True)
```

When the close attempted feature is enabled, when the user clicks the "X" or types ALT+F4, you will not get a WIN_CLOSED event like previously, you will instead get an event `WINDOW_CLOSE_ATTEMPTED_EVENT` and the window will remain open.  

Usually this feature is used to add a "close confirmation" popup.  The flow goes something like this:

* Window is shown
* User  clicks X
* A popup window is shown with message "Do you really want to close the window?"
* If confirmed a close is desired, the window is closed.  It not, the event loop continues on, basically ignoring the event occurred.

### A Complete Example - Window Closed Confirmation (`enable_close_attempted_event=True`)

Returning to the example used above, there has been only 2 modifications. 

1. Added the parameter `enable_close_attempted_event=True` to the call to `Window`
2. The if statement in the event loop has changed to add a confirmation

```python
import PySimpleGUI as sg

layout = [[sg.Text('Very basic Window')],
          [sg.Text('Click X in titlebar or the Exit button')],
          [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout, enable_close_attempted_event=True)

while True:
    event, values = window.read()
    print(event, values)
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break

window.close()
```

The event loop changed from a check like this:
```python
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
```

To one like this:
```python
    if (event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT or event == 'Exit') and sg.popup_yes_no('Do you really want to exit?') == 'Yes':
        break
```

Let's run this last program so you can see what all this looks like to users.

In both cases that a user previously exited the window, there is now an additional confirmation step.

![download](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Window%20Closed%20Confirmation.gif)



### Demo Programs.... A PySimpleGUI Program's Best Friend

Like all features of PySimpleGUI, one of the best resources available to you to learn about parameters, like this close attempted parameter, are the Demo Programs.  When you run into a parameter or a feature you've not used before, one way to find some examples of its use is to use the Demo Browser to search through the demo programs.  You'll find the Demo Browser described in the Cookbook.

As of this writing, the name of the Demo Program Browser is:

`Browser_START_HERE_Demo_Programs_Browser.py`

If you enter the parameter described in this section - `enable_close_attempted_event` you'll find a Demo Program that uses this parameter.

![DemoBrowser](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Demo%20Browser%20Search%20Close%20Attempted.jpg)

This demo shows you code similar to the code used in this section of the documentation. Use this Browser program!  It will make finding examples ***much easier***!

See the section up above on the pip-installable version of the demos (search for - `psgdemos`) to get the super-quick method of getting the demo programs and the Demo Browser.

### The `values` Variable - Return values as a list

The second parameter from a Read call is either a list or a dictionary of the input fields on the Window.

By default return values are a list of values, one entry for each input field, but for all but the simplest of windows the return values will be a dictionary.  This is because you are likely to use a 'key' in your layout.  When you do, it forces the return values to be a dictionary.

Each of the Elements that are Input Elements will have a value in the list of return values.  If you know for sure that the values will be returned as a list, then you could get clever and unpack directly into variables.

event, (filename, folder1, folder2, should_overwrite) = sg.Window('My title', window_rows).read()

Or, more commonly, you can unpack the return results separately.  This is the preferred method because it works for **both** list and dictionary return values.

```python
event, values = sg.Window('My title', window_rows).read()
event, value_list = window.read()
value1 = value_list[0]
value2 = value_list[1]
	 ...
```

However, this method isn't good when you have a lot of input fields.  If you insert a new element into your window then you will have to shuffle your unpacks down, modifying each of the statements to reference `value_list[x]`.

The more common method is to request your values be returned as a dictionary by placing keys on the "important" elements (those that you wish to get values from and want to interact with)

### `values` Variable - Return values as a dictionary

For those of you that have not encountered a Python dictionary, don't freak out!  Just copy and paste the sample code and modify it. Follow this design pattern and you'll be fine.  And you might learn something along the way.

For windows longer than 3 or 4 fields you will want to use a dictionary to help you organize your return values. In almost all (if not all) of the demo programs you'll find the return values being passed as a dictionary.  It is not a difficult concept to grasp, the syntax is easy to understand, and it makes for very readable code.

The most common window read statement you'll encounter looks something like this:

`window = sg.Window("My title", layout).read()`

To use a dictionary, you will need to:
* Mark each input element you wish to be in the dictionary with the keyword `key`.

If **any** element in the window has a `key`, then **all** of the return values are returned via a dictionary.  If some elements do not have a key, then they are numbered starting at zero.

Let's take a look at your first dictionary-based window.

```python
import PySimpleGUI as sg

sg.theme('Dark Blue 3')  # please make your windows colorful

layout = [
			[sg.Text('Please enter your Name, Address, Phone')],
			[sg.Text('Name', size=(15, 1)), sg.InputText('1', key='-NAME-')],
			[sg.Text('Address', size=(15, 1)), sg.InputText('2', key='-ADDRESS-')],
			[sg.Text('Phone', size=(15, 1)), sg.InputText('3', key='-PHONE-')],
			[sg.Submit(), sg.Cancel()]
			]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()

sg.Popup(event, values, values['-NAME-'], values['-ADDRESS-'], values['-PHONE-'])
```

To get the value of an input field, you use whatever value used as the `key` value as the index value.  Thus to get the value of the name field, it is written as

	values['-NAME-']

Think of the variable values in the same way as you would a list, however, instead of using 0,1,2, to reference each item in the list, use the values of the key.  The Name field in the window above is referenced by `values['-NAME-']`.

You will find the key field used quite heavily in most PySimpleGUI windows unless the window is very simple.

One convention you'll see in many of the demo programs is keys being named in all caps with an underscores at the beginning and the end.  You don't HAVE to do this... your key value may look like this:
`key = '-NAME-'`

The reason for this naming convention is that when you are scanning the code, these key values jump out at you.   You instantly know it's a key.  Try scanning the code above and see if those keys pop out.
`key = '-NAME-'`



## The Event Loop / Callback Functions

All GUIs have one thing in common, an "event loop".  Usually the GUI framework runs the event loop for you, but sometimes you want greater control and will run your own event loop.  You often hear the term event loop when discussing embedded systems or on a Raspberry Pi.

With PySimpleGUI if your window will remain open following button clicks, then your code will have an event loop. If your program shows a single "one-shot"  window, collects the data and then has no other GUI interaction, then you don't need an event loop.

There's nothing mysterious about event loops... they are loops where you take care of.... wait for it..... *events*.  Events are things like button clicks, key strokes, mouse scroll-wheel up/down.

This little program has a typical PySimpleGUI Event Loop.

The anatomy of a PySimpleGUI event loop is as follows, *generally speaking*.
* The actual "loop" part is a `while True` loop
* "Read" the event and any input values the window has
* Check to see if window was closed or user wishes to exit
* A series of `if event ....` statements


## All Elements

Here is a complete, short, program that contains *all of the PySimpleGUI Elements*.

```python
import PySimpleGUI as sg

"""
    Demo - Element List

    All 34 elements shown in 1 window as simply as possible.

    Copyright 2022 PySimpleGUI
"""

use_custom_titlebar = False

def make_window(theme=None):
    NAME_SIZE = 23

    def name(name):
        dots = NAME_SIZE-len(name)-2
        return sg.Text(name + ' ' + '•'*dots, size=(NAME_SIZE,1), justification='r',pad=(0,0), font='Courier 10')

    sg.theme(theme)

    treedata = sg.TreeData()

    treedata.Insert("", '_A_', 'Tree Item 1', [1234], )
    treedata.Insert("", '_B_', 'B', [])
    treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )

    layout_l = [[name('Text'), sg.Text('Text')],
                [name('Input'), sg.Input(s=15)],
                [name('Multiline'), sg.Multiline(s=(15,2))],
                [name('Output'), sg.Output(s=(15,2))],
                [name('Combo'), sg.Combo(sg.theme_list(), default_value=sg.theme(), s=(15,22), enable_events=True, readonly=True, k='-COMBO-')],
                [name('OptionMenu'), sg.OptionMenu(['OptionMenu',],s=(15,2))],
                [name('Checkbox'), sg.Checkbox('Checkbox')],
                [name('Radio'), sg.Radio('Radio', 1)],
                [name('Spin'), sg.Spin(['Spin',], s=(15,2))],
                [name('Button'), sg.Button('Button')],
                [name('ButtonMenu'), sg.ButtonMenu('ButtonMenu', sg.MENU_RIGHT_CLICK_EDITME_EXIT)],
                [name('Slider'), sg.Slider((0,10), orientation='h', s=(10,15))],
                [name('Listbox'), sg.Listbox(['Listbox', 'Listbox 2'], no_scrollbar=True,  s=(15,2))],
                [name('Image'), sg.Image(sg.EMOJI_BASE64_HAPPY_THUMBS_UP)],
                [name('Graph'), sg.Graph((125, 50), (0,0), (125,50), k='-GRAPH-')]  ]

    layout_r  = [[name('Canvas'), sg.Canvas(background_color=sg.theme_button_color()[1], size=(125,50))],
                [name('ProgressBar'), sg.ProgressBar(100, orientation='h', s=(10,20), k='-PBAR-')],
                [name('Table'), sg.Table([[1,2,3], [4,5,6]], ['Col 1','Col 2','Col 3'], num_rows=2)],
                [name('Tree'), sg.Tree(treedata, ['Heading',], num_rows=3)],
                [name('Horizontal Separator'), sg.HSep()],
                [name('Vertical Separator'), sg.VSep()],
                [name('Frame'), sg.Frame('Frame', [[sg.T(s=15)]])],
                [name('Column'), sg.Column([[sg.T(s=15)]])],
                [name('Tab, TabGroup'), sg.TabGroup([[sg.Tab('Tab1',[[sg.T(s=(15,2))]]), sg.Tab('Tab2', [[]])]])],
                [name('Pane'), sg.Pane([sg.Col([[sg.T('Pane 1')]]), sg.Col([[sg.T('Pane 2')]])])],
                [name('Push'), sg.Push(), sg.T('Pushed over')],
                [name('VPush'), sg.VPush()],
                [name('Sizer'), sg.Sizer(1,1)],
                [name('StatusBar'), sg.StatusBar('StatusBar')],
                [name('Sizegrip'), sg.Sizegrip()]  ]

    layout = [[sg.MenubarCustom([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)] if use_custom_titlebar else [sg.Menu([['File', ['Exit']], ['Edit', ['Edit Me', ]]],  k='-CUST MENUBAR-',p=0)],
              [sg.Checkbox('Use Custom Titlebar & Menubar', use_custom_titlebar, enable_events=True, k='-USE CUSTOM TITLEBAR-')],
              [sg.T('PySimpleGUI Elements - Use Combo to Change Themes', font='_ 18', justification='c', expand_x=True)],
              [sg.Col(layout_l), sg.Col(layout_r)]]

    window = sg.Window('The PySimpleGUI Element List', layout, finalize=True, right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True, use_custom_titlebar=use_custom_titlebar)

    window['-PBAR-'].update(30)                                                     # Show 30% complete on ProgressBar
    window['-GRAPH-'].draw_image(data=sg.EMOJI_BASE64_HAPPY_JOY, location=(0,50))   # Draw something in the Graph Element

    return window

# Start of the program...
window = make_window()

while True:
    event, values = window.read()
    sg.popup(event, values)                     # show the results of the read in a popup Window
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if values['-COMBO-'] != sg.theme():
        sg.theme(values['-COMBO-'])
        window.close()
        window = make_window()
    if event == '-USE CUSTOM TITLEBAR-':
        use_custom_titlebar = values['-USE CUSTOM TITLEBAR-']
        window.close()
        window = make_window()
window.close()


```

When you run it, assuming you've not set a default theme in the system settings, you'll see a window that looks like this (when on Windows):

![image](https://user-images.githubusercontent.com/46163555/152656799-1b5ec932-d2ec-470d-9df3-42121e6298c9.png)

The checkbox at the top that reads "Use Custom Titlebar & Menubar" will enable you to see the what the window looks like using the PySimpleGUI Custom Titlebar and Custom Menubar.

![image](https://user-images.githubusercontent.com/46163555/152656821-5b393d2c-4081-480c-9735-2297d67305d4.png)
Using this one test program, you can easily browse the PySimpleGUI Themes by choosing a new color Theme using the Combo Element.


![image](https://user-images.githubusercontent.com/46163555/152656849-6107854a-610a-4c74-a521-923e3394b9cc.png)

### But it's so UGLY!


![image](https://user-images.githubusercontent.com/46163555/152658001-3e270768-0636-48f4-90b7-1fa4bb901ab2.png)
On Windows, using straight Python, this is the non-GUI alternative.

![image](https://user-images.githubusercontent.com/46163555/152658061-fb6bbbb4-b298-41a2-a725-4352719906a4.png)

The 1970s and 1980s were a great era for computing, but I wouldn't call the user interfaces "attractive".  Borland made some great tools in the 90's for doing TUIs.  There are some excellent Python packages available for you if you're after a TUI!  If that's the look you're after, give them a try.  You may like the results.  But, it's not what PySimpleGUI is about.  

We're making GUIs for the masses, something you can give to anyone and they'll understand how to use it.  If you asked a Windows user (i.e. a normal person, not a programmer) to open a command window in the past decade then you likely got a worried look back.  Normal people aren't going to use your Python program that's command line based and be thrilled about it.  Your programming pals will love your TUI, Mary, who works in accounting, will not.

The example window may look "ugly" or dated to you.  ***It's fair to say that it looks dated***.  While PySimpleGUI Themes instantly give you a color scheme that matches, it doesn't go much further in making tkinter more attractive/"modern".  

***However***, you are far from being out of options to improve the look of your GUI.  This bare-bones program is your **starting point**.  This is where you begin the process of making an attractive user interface.  You've not yet ***started*** to make your interface look better.

No effort has been made to make it look nice. It's purely functional. There are 34 Elements in the window.  34 Elements. Considering what it does, it's miraculous or in the least incredibly impressive.  Why? Because in 65 lines of Python code that window was created, shown, and collected the results.  

Let's be clear here... this window will take a massive amount of code using the conventional Python GUI packages.  If you manage to write a tkinter, Qt or WxPython program that shows all of these Widgets in under 65 lines of Python code, then by all means send the code over.  

Fair, side by side tests, recreating the exact same application, have shown numerous times that PySimpleGUI code is at least 1/2 to 1/10th the amount of code than tkinter requires.  

There is no magic behind why it's so much shorter.  PySimpleGUI is writing all the boilerplate code on your behalf.  The same tkinter code is being executed that you would write by hand.  The difference is that the code is contained in the PySimpleGUI source code instead of in your application code.  That's all that's going on with "wrappers" like PySimpleGUI.  Code is being generated and executed for you in order to simplify your code.

A large amount of time nor code is required to create custom Buttons and other elements, including entirely new and more complex elements such a Dials or Gauges. Transforming a button from plain to an image is a parameter to the Button element.   It's... not... THAT... **HARD**.  You're a programmer, write some code, or *add a parameter* if you want more attractive interfaces.  The hooks are there waiting for you to be creative.

### Window Closed Events

**`Note, event values can be None`**.  The value for `event` will be the text that is displayed on the button element when it was created or the key for the button.  If the user closed the window using the "X" in the upper right corner of the window, then `event` will be `sg.WIN_CLOSED` which is equal to `None`.   It is ***vitally*** ***important*** that your code contain the proper checks for `sg.WIN_CLOSED`.

For "persistent windows",  **always give your users a way out of the window**.  Otherwise you'll end up  with windows that never properly close.  It's literally 2 lines of code that you'll find in every Demo Program.  While you're at it, make sure a `window.close()` call is after your event loop so that your window closes for sure.

### The `values` Dictionary

You can see in the results Popup window that the values returned are a dictionary.  Each input field in the window generates one item in the return values list.  Input fields often return a `string`. Check Boxes and Radio Buttons return `bool`.  Sliders return float or perhaps int depending on how you configured it or which port you're using.

If your window has no keys and it has no buttons that are "browse" type of buttons, then it will return values to you as a list instead of a dictionary.  If possible PySimpleGUI tries to return the values as a list to keep things simple.

Note in the list of return values in this example, many of the keys are numbers.  That's because no keys were specified on any of the elements (although one was automatically made for you).  If you don't specify a key for your element, then a number will be sequentially assigned.  For elements that you don't plan on modifying or reading values from, like a Text Element, you can skip adding keys.  For other elements, you'll likely want to add keys so that you can easily access the values and perform operations on them.

## Operations That Take a "Long Time"

If you're a Windows user you've seen windows show in their title bar "Not Responding" which is soon followed by a Windows popup stating that "Your program has stopped responding".  Well, you too can make that message and popup appear if you so wish!  All you need to do is execute an operation that takes "too long" (i.e. a few seconds) inside your event loop.

You have a couple of options for dealing this with.  If your operation can be broken up into smaller parts, then you can call `Window.refresh()` occasionally to avoid this message.  If you're running a loop for example, drop that call in with your other work.  This will keep the GUI happy and Window's won't complain.

If, on the other hand, your operation is not under your control or you are unable to add `refresh` calls, then the next option available to you is to move your long operations into a thread.


### Threading Made Simple

You've been at Python for a couple weeks, bravely ventured into GUI world, and the function you called when a button click is detected takes 20 seconds to complete.  Your window displays the "Not Responding" message.  If you ask what to do on StackOverflow, you'll be told that "all you have to do is use threads".

![image](https://user-images.githubusercontent.com/46163555/152658001-3e270768-0636-48f4-90b7-1fa4bb901ab2.png)
Two weeks into programming, and you've just been told you need to learn Threading?  

This exact scenario is why the window method `perform_long_operation` was created.  It's a way for you to "ease into" threading without learning about threading.  Forget that thread was even mentioned.  Let's just talk about "long operations" instead.

There are 2 ways you can use this call.  If your function does not take any parameters, then you can enter the name of the function (**without the parentheses!**) as the first parameter to `perform_long_operation`.    

```python
window.perform_long_operation(my_function, '-FUNCTION COMPLETED-')
```
  
If your function has parameters, then you'll need to use a lambda.  Don't freak out at hearing "lambda" (yet).  Just add it as in this example code...

```python
window.perform_long_operation(lambda: my_function_with_parms(10), '-FUNCTION COMPLETED-')
```

Write the first parameter was if you were calling your function, and then put `lambda: ` in front of that.

The second parameter to `perform_long_operation` is the event (a key) that you want to get back from `window.read()` when your function returns.

Finally, if your function has a return value, then that value will show up in the `values` dictionary with the key that you provided.  In this example, `values['-FUNCTION COMPLETED-']` will contain the return value from your function.


```python
import PySimpleGUI as sg
import time

def my_function():
    time.sleep(30)

def my_function_with_parms(duration):
    time.sleep(duration)
    return 'My Return Value'

layout = [  [sg.Text('Call a lengthy function')],
            [sg.Button('Start'), sg.Button('Start 2'), sg.Button('Exit')]  ]

window = sg.Window('Long Operation Example', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Start':
        window.perform_long_operation(my_function, '-FUNCTION COMPLETED-')
    elif event == 'Start 2':
        window.perform_long_operation(lambda: my_function_with_parms(10), '-FUNCTION COMPLETED-')
    elif event == '-FUNCTION COMPLETED-':
        sg.popup('Your function completed!')
window.close()


```

So, in summary, `window.perform_long_operation` starts and manages the thread on your behalf.  You are returned an event when your "long operation" completes.  If your function returns a value, then that value will show up in the `values` variable from your `window.read()` call.  Threading made simple.

###  `window.perform_long_operation`Has An Alias `window.start_thread`

If you're a threading pro, then maybe you would prefer the alias for  `window.perform_long_operation`.  In addition to this name for the method, you'll get the exact same results by calling  `window.start_thread`.  Since threading is becoming more popular due to the `write_event_value` capability, it makes sense to enable you to call a thread a thread if that's what you prefer... so enjoy the `start_thread` alias if that's how you roll.


### Threading the "New Way" - `Window.write_event_value`

This new function that is available currently only in the tkinter port as of July 2020 is exciting and represents the future way multi-threading is handled in PySimpleGUI.

Previously, a queue was used where your event loop would **poll** for incoming messages from a thread.

Now, threads can directly inject events into a Window so that it will show up in the `window.read()` calls.  This allows a your event loop to "pend", waiting for normal window events as well as events being generated by threads.  It is much more efficient than polling.

You can see this new capability in action in this demo:  `Demo_Multithreaded_Write_Event_Value.py`

Just use the Demo Browser to search for `write_event_value` to get more examples.  

Here is that program for your inspection and education.  It's SO nice to no longer poll for threaded events.

```python
import threading
import time
import PySimpleGUI as sg


"""
    Threaded Demo - Uses Window.write_event_value communications

    Requires PySimpleGUI.py version 4.25.0 and later

    This is a really important demo  to understand if you're going to be using multithreading in PySimpleGUI.

    Older mechanisms for multi-threading in PySimpleGUI relied on polling of a queue. The management of a communications
    queue is now performed internally to PySimpleGUI.

    The importance of using the new window.write_event_value call cannot be emphasized enough.  It will hav a HUGE impact, in
    a positive way, on your code to move to this mechanism as your code will simply "pend" waiting for an event rather than polling.

    Copyright 2020 PySimpleGUI.org
"""

THREAD_EVENT = '-THREAD-'

cp = sg.cprint

def the_thread(window):
    """
    The thread that communicates with the application through the window's events.

    Once a second wakes and sends a new event and associated value to the window
    """
    i = 0
    while True:
        time.sleep(1)
        window.write_event_value('-THREAD-', (threading.current_thread().name, i))      # Data sent is a tuple of thread name and counter
        cp('This is cheating from the thread', c='white on green')
        i += 1


def main():
    """
    The demo will display in the multiline info about the event and values dictionary as it is being
    returned from window.read()
    Every time "Start" is clicked a new thread is started
    Try clicking "Dummy" to see that the window is active while the thread stuff is happening in the background
    """

    layout = [  [sg.Text('Output Area - cprint\'s route to here', font='Any 15')],
                [sg.Multiline(size=(65,20), key='-ML-', autoscroll=True, reroute_stdout=True, write_only=True, reroute_cprint=True)],
                [sg.T('Input so you can see data in your dictionary')],
                [sg.Input(key='-IN-', size=(30,1))],
                [sg.B('Start A Thread'), sg.B('Dummy'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout, finalize=True)

    while True:             # Event Loop
        event, values = window.read()
        cp(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event.startswith('Start'):
            threading.Thread(target=the_thread, args=(window,), daemon=True).start()
        if event == THREAD_EVENT:
            cp(f'Data from the thread ', colors='white on purple', end='')
            cp(f'{values[THREAD_EVENT]}', colors='white on red')
    window.close()


if __name__ == '__main__':
    main()
```


You'll find plenty of examples to help you with these concepts if you look in the Demo Programs.  So, pip install the Demo Programs and the Demo Browser so that you can easily search and find examples of what you're trying to accomplish.

---


# Building Custom Windows

You will find it ***much easier*** to write code using PySimpleGUI if you use an IDE such as ***PyCharm***.  The features that show you documentation about the API call you are making will help you determine which settings you want to change, if any.  In PyCharm, two commands are particularly helpful.

	Control-Q (when cursor is on function name) brings up a box with the function definition
	Control-P (when cursor inside function call "()") shows a list of parameters and their default values

## Synchronous / Asynchronous Windows

The most common use of PySimpleGUI is to display and collect information from the user.  The most straightforward way to do this is using a "blocking" GUI call.  Execution is "blocked" while waiting for the user to close the GUI window/dialog box.

You've already seen a number of examples above that use blocking windows.  You'll know it blocks if the `Read` call has no timeout parameter.

A blocking Read (one that waits until an event happens) look like this:

```python
event, values = window.read()
```

A non-blocking / Async Read call looks like this:

```python
event, values = window.read(timeout=100)
```

You can learn more about these async / non-blocking windows toward the end of this document.

# Themes - Automatic Coloring of Your Windows

In Dec 2019 the function `change_look_and_feel` was replaced by `theme`.  The concept remains the same, but a new group of function calls makes it a lot easier to manage colors and other settings.

By default the PySimpleGUI color theme is now `Dark Blue 3`.  Gone are the "system default" gray colors.  If you want your window to be devoid of all colors so that the system chooses the colors (gray) for you, then set the theme to 'gray gray gray'.  This tells PySimpleGUI that you're a boring person.... no no no... I'm **just kidding!**.... it just means you want PySimpleGUI to not set any colors so that the default colors provided by the OS/tkinter will be used.  It's a memorable theme name.  There are several with "default" in the name and it got confusing which was the full-on-add-no-color name, so 'gray gray gray' was added to make it easy to recall.

There are 154 themes available.  You can preview these themes by calling `theme_previewer()` which will create a LARGE window displaying all of the color themes available.

You can see the current available themes by calling `sg.theme_previewer()`.  It creates a window that looked like this in June 2022:

![image](https://user-images.githubusercontent.com/46163555/173203488-7fef44b5-000f-48b9-b353-625c214e41d4.png)


## Default is `Dark Blue 3`

![image](https://user-images.githubusercontent.com/46163555/71362356-cd070200-2563-11ea-9455-9315b9423d7e.png)


In Dec 2019 the default for all PySimpleGUI windows changed from the system gray with blue buttons to a more complete theme using a grayish blue with white text.  Previously users were nagged into choosing  color theme other than gray.  Now it's done for you instead of nagging you.

If you're struggling with this color theme, then add a call to `theme` to change it.



## Theme Name Formula

Themes names that you specify can be "fuzzy".  The text does not have to match exactly what you see printed.  For example "Dark Blue 3" and "DarkBlue3" and "dark blue 3" all work.

One way to quickly determine the best setting for your window is to simply display your window using a lot of different themes.  Add the line of code to set the theme - `theme('Dark Green 1')`, run your code, see if you like it, if not, change the theme string to `'Dark Green 2'` and try again.  Repeat until you find something you like.

The "Formula" for the string is:

`Dark Color #`

or

`Light Color #`

Color can be Blue, Green, Black, Gray, Purple, Brown, Teal, Red.   The # is optional or can be from 1 to XX.  Some colors have a lot of choices.  There are 13 "Light Brown" choices for example.

### "System" Default - No Colors (e.g. `"Gray Gray Gray"`)

If you're bent on having no colors at all in your window, then choose `Default 1` or `System Default 1`.  Use the `"Gray Gray Gray"` theme if you really want to ensure system defaults only.

If you want the original PySimpleGUI color scheme of a blue button and everything else gray then you can get that with the theme `Default` or `System Default`.


## Theme Functions

The basic theme function call is `theme(theme_name)`.  This sets the theme.  Calling without a parameter, `theme()` will return the name of the current theme.

If you want to get or modify any of the theme settings, you can do it with these functions that you will find detailed information about in the function definitions section at the bottom of the document.  Each will return the current value if no parameter is used.

You'll find a detailed list of the theme calls in the SDK Call Reference in this section:

https://pysimplegui.readthedocs.io/en/latest/call%20reference/#themes

```python
theme
theme_add_new
theme_background_color
theme_border_width
theme_button_color
theme_button_color_background
theme_button_color_text
theme_element_background_color
theme_element_text_color
theme_global
theme_input_background_color
theme_input_text_color
theme_list
theme_previewer
theme_previewer_swatches
theme_progress_bar_border_width
theme_progress_bar_color
theme_slider_border_width
theme_slider_color
theme_text_color
theme_text_element_background_color
theme_use_custom_titlebar
```

These will help you get a list of available choices.

```python
theme_list
theme_previewer
```





# Window Object - Beginning a window

The first step is to create the window object using the desired window customizations.

## Modal Windows (only applied to tkinter port currently
)
NOTE - as of PySimpleGUI 4.25.0 Modal Windows are supported!  By default the `popup` windows that block will be marked Modal by default.  This is a somewhat risky change because your existing applications will behave differently. However, in theory, you shouldn't have been interacting with other windows while the popup is active.  All of those actions are at best queued.  It's implementation dependent.

"Modal" in this case means that you must close this "modal" window before you will be able to interact with windows created before this window.  Think about an "about" box.  You normally have to close this little popup in most programs.  So, that's what PySimpleGUI is doing now.

## Making your window modal

To make a Modal  Window you have 2 options.

1. Set the `moodel=True` parameter in your Window calls.

2. Call the method `Window.make_modal()` to chance a window from non-modal to modal.  There is no modal to non-modal.  Don't see the need for one. If one comes up, sure!


### Disabling modal windows

Popups that block are the only windows that have modal on by default. There is a modal parameter than you  can set to False to turn it off.

For the earlier than 4.25.0 and other ports of PySimpleGUI There is no direct support for "**modal windows**" in PySimpleGUI.  All windows are accessible at all times unless you manually change the windows' settings.


**IMPORTANT** - Many of the `Window` methods require you to either call `Window.read` or `Window.Finalize` (or set `finalize=True` in your `Window` call) before you call the method. This is because these 2 calls are what actually creates the window using the underlying GUI Framework.  Prior to one of those calls, the methods are likely to crash as they will not yet have their underlying widgets created.


### Window Location

PySimpleGUI computes the exact center of your window and centers the window on the screen.  If you want to locate your window elsewhere, such as the system default of (0,0), if you have 2 ways of doing this. The first is when the window is created.  Use the `location` parameter to set where the window.  The second way of doing this is to use the `SetOptions` call which will set the default window location for all windows in the future.

#### Multiple Monitors and Linux

The auto-centering (default) location for your PySimpleGUI window may not be correct if you have multiple monitors on a Linux system.  On Windows multiple monitors appear to work ok as the primary monitor the tkinter utilizes and reports on.

Linux users with multiple monitors that have a problem when running with the default location will need to specify the location the window should be placed when creating the window by setting the `location` parameter.

### Window Size

You can get your window's size by access the `Size` property.  The window has to be Read once or Finalized in order for the value to be correct. Note that it's a property, not a call.

`my_windows_size = window.Size`

To finalize your window:

```python
window = Window('My Title', layout, finalize=True)
```


### Element Sizes

There are multiple ways to set the size of Elements.  They are:

1. The global default size - change using `SetOptions` function
2. At the Window level - change using the parameter `default_element_size` in your call to `Window`
3. At the Element level - each element has a `size` parameter

Element sizes are measured in characters (there are exceptions).  A Text Element with  `size = (20,1)` has a size of 20 characters wide by 1 character tall.

The default Element size for PySimpleGUI is `(45,1)`.

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

### TTK Buttons

Beginning in release 4.7.0 PySimpleGUI supports both "normal" tk Buttons and ttk Buttons.  This change was needed so that Mac users can use colors on their buttons.  There is a bug that causes tk Buttons to not show text when you attempt to change the button color.  Note that this problem goes away if you install Python from the official Python.org site rather than using Homebrew.  A number of users have switched and are quite happy since even tk Buttons work on the Mac after the switch.

By default Mac users will get ttk Buttons when a Button Element is used.  All other platforms will get a normal tk Button.  There are ways to override this behavior.  One is by using the parameter `use_ttk_buttons` when you create your window.  If set to True, all buttons will be ttk Buttons in the window.  If set to False, all buttons will be normal tk Buttons.  If not set then the platform or the Button Element determines which is used.

If a system-wide setting is desired, then the default can be set using `set_options`.  This will affect all windows such as popups and the debug window.

### TTK Themes

tkinter has a number of "Themes" that can be used with ttk widgets.  In PySimpleGUI these widgets include - Table, Tree, Combobox, Button, ProgressBar, Tabs & TabGroups.  Some elements have a 'theme' parameter but these are no longer used and should be ignored.  The initial release of PySimpleGUI attempted to mix themes in a single window but since have learned this is not possible so instead it is set at the Window or the system level.

If a system-wide setting is desired, then the default can be set using `set_options`. This will affect all windows such as popups and the debug window.

The ttk theme choices depend on the platform. Linux has a shorter number of selections than Windows.  

The minimum list of TTK themes is:
- default
- alt
- clam
- classic

Most Windows systems have some additional themes that come standard with tkinter:
- default
- alt
- clam
- classic
- winnative
- vista
- xpnative

The list of available themes is populated automatically when you open the Global PySimpleGUI Settings window.  Previously the list of themes was hard-coded by the PySimpleGUI code.  Now the list is retrieved from tkinter. 

There are constants defined to help you with code completion to determine what your choices are.  Theme constants start with `THEME_`.  For example, the "clam" theme is `THEME_CLAM`

If you try to manually set a TTK theme while making a Window or calling `set_options` and it is not a valid theme, you will be shown the list of valid themes in the error popup.  The popup may resemble one like this:


![image](https://user-images.githubusercontent.com/46163555/167274285-14b95be3-5c5f-4edf-80e0-b8969ca3cf5c.png)


## Closing Windows

When you are completely done with a window, you should close it and then delete it so that the resources, in particular the tkinter resources, are properly cleaned up.

If you wish to do this in 1 line of code, here's your line:

```python
window.close(); del window
```

The delete helps with a problem multi-threaded application encounter where tkinter complains that it is being called from the wrong thread (not the program's main thread)

## Window Methods That Complete Formation of Window

After you have completed making your layout, stored in a variable called `layout` in these examples, you will create your window.

The creation part of a window involves 3 steps.

1. Create a `Window` object
2. Adding your Layout to the window
3. Optional - Finalize if want to make changes prior to `read` call

Over time the PySimpleGUI code has continued to compact, compress, so that as little code as possible will need to be written by the programmer.

### The Individual Calls

This is the "long form" as each method is called individually.

```python
window = sg.Window('My Title')
window.layout(layout)
window.finalize()
```

### Chaining The Calls (the old method)

The next level  of compression that was done was to chain the calls together into a single line of code.

```python
window = sg.Window('My Title').Layout(layout).finalize()
```

### Using Parameters Instead of Calls (New Preferred Method)

Here's a novel concept, instead of using chaining, something that's foreign to beginners, use parameters to the `Window` call.  And that is exactly what's happened as of 4.2 of the PySimpleGUI port.

```python
window = sg.Window('My Title', layout, finalize=True)
```

Rather than pushing the work onto the user of doing the layout and finalization calls, let the Window initialization code do it for you. Yea, it sounds totally obvious now, but it didn't a few months ago.

This capability has been added to all 4 PySimpleGUI ports but none are on PyPI just yet as there is some runtime required first to make sure nothing truly bad is going to happen.

Call to set the window layout.  Must be called prior to `Read`.  Most likely "chained" in line with the Window creation.

```python
window = sg.Window('My window title', layout)
```

#### `finalize()` or `Window` parameter `finalize=True`

Call to force a window to go through the final stages of initialization.  This will cause the tkinter resources to be allocated so that they can then be modified.  This also causes your window to appear.  If you do not want your window to appear when Finalize is called, then set the Alpha to 0 in your window's creation parameters.

If you want to call an element's `Update` method or call a `Graph` element's drawing primitives, you ***must*** either call `Read` or `Finalize` prior to making those calls.


#### read(timeout=None, timeout_key=TIMEOUT_KEY, close=False)

Read the Window's input values and button clicks in a blocking-fashion

Returns event, values.  Adding a timeout can be achieved by setting timeout=*number of milliseconds* before the Read times out after which a "timeout event" is returned.  The value of timeout_key will be returned as the event.   If you do not specify a timeout key, then the value `TIMEOUT_KEY` will be returned.

If you set the timeout = 0, then the Read will immediately return rather than waiting for input or for a timeout.  It's a truly non-blocking "read" of the window.


# Layouts

While at this point in the documentation you've not been shown very much about each Element available, you should read this section carefully as you can use the techniques you learn in here to build better, shorter, and easier to understand PySimpleGUI code.

If it feels like this layout section is too much too soon, then come back to this section after you're learned about each Element.  **Whatever order you find the least confusing is the best.**

While you've not learned about Elements yet, it makes sense for this section to be up front so that you'll have learned how to use the elements prior to learning how each element works.  At this point in your PySimpleGUI education, it is better for you to grasp time efficient ways of working with Elements than what each Element does.  By learning now how to assemble Elements now, you'll have a good model to put the elements you learn into.

There are *several* aspects of PySimpleGUI that make it more "Pythonic" than other Python GUI SDKs.  One of the areas that is unique to PySimpleGUI is how a window's "layout" is defined, specified or built.  A window's "layout" is simply a list of lists of elements.  As you've already learned, these lists combine to form a complete window.  This method of defining a window is super-powerful because lists are core to the Python language as a whole and thus are very easy to create and manipulate.

Think about that for a moment and compare/contrast with Qt, tkinter, etc..  With PySimpleGUI the location of your element in a matrix determines where that Element is shown in the window.  It's so ***simple*** and that makes it incredibly powerful.  Want to switch a row in your GUI that has text with the one below it that has an input element?  No problem, swap the lines of code and you're done.

Layouts were designed to be visual. The idea is for you to be able to envision how a window will look by simply looking at the layout in the code.  The CODE itself matches what is drawn on the screen.  PySimpleGUI is a cross between straight Python code and a visual GUI designer.

In the process of creating your window, you can manipulate these lists of elements without having an impact on the elements or on your window.  Until you perform a "layout" of the list, they are nothing more than lists containing objects (they just happen to be your window's elements).

Many times your window definition / layout will be a static, straightforward to create.

However, window layouts are not limited to being one of these statically defined list of Elements.


# Generated Layouts (For sure want to read if you have > 5 repeating elements/rows)

There are 5 specific techniques of generating layouts discussed in this section. They can be used alone or in combination with each other.

1. Layout + Layout concatenation `[[A]] + [[B]] = [[A], [B]]`
2. Element Addition on Same Row  `[[A] + [B]] = [[A, B]]`
3. List Comprehension to generate a row `[A for x in range(10)] = [A,A,A,A,A...]`
4. List Comprehension to generate multiple rows `[[A] for x in range(10)] = [[A],[A],...]`
5. User Defined Elements / Compound Elements


## Example - List Comprehension To Concatenate Multiple Rows - "To Do" List Example

Let's create a little layout that will be used to make a to-do list using PySimpleGUI.

### Brute Force

```python
import PySimpleGUI as sg

layout = [
            [sg.Text('1. '), sg.In(key=1)],
            [sg.Text('2. '), sg.In(key=2)],
            [sg.Text('3. '), sg.In(key=3)],
            [sg.Text('4. '), sg.In(key=4)],
            [sg.Text('5. '), sg.In(key=5)],
            [sg.Button('Save'), sg.Button('Exit')]
         ]

window = sg.Window('To Do List Example', layout)
event, values = window.read()
```

The output from this script was this window:

![SNAG-0451](https://user-images.githubusercontent.com/46163555/63563849-90cd8180-c530-11e9-80d7-4954b11deebd.jpg)


Take a moment and look at the code and the window that's generated.  Are you able to look at the layout and envision the Window on the screen?


### Build By Concatenating Rows

The brute force method works great on a list that's 5 items long, but what if your todo list had 40 items on it. THEN what?  Well, that's when we turn to a "generated" layout, a layout that is generated by your code.  Replace the layout= stuff from the previous example with this definition of the layout.

```python
import PySimpleGUI as sg

layout = []
for i in range(1,6):
    layout += [sg.Text(f'{i}. '), sg.In(key=i)],
layout += [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('To Do List Example', layout)
event, values = window.read()
```

It produces the exact same window of course.  That's progress.... went from writing out every row of the GUI to generating every row. If we want 48 items as suggested, change the range(1,6) to range(1,48).  Each time through the list another row is added onto the layout.

### Create Several Rows Using List Comprehension

BUT, we're not done yet!

This is **Python**, we're using lists to build something up, so we should be looking at ****list comprehensions****.  Let's change the `for` loop into a list comprehension.  Recall that our `for` loop was used to concatenate 6 rows into a layout.

```python
layout =  [[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)]
```

Here we've moved the `for` loop to inside of the list definition (a list comprehension)

### Concatenating Multiple Rows

We have our rows built using the list comprehension, now we just need the buttons.  They can be easily "tacked onto the end" by simple addition.

```python
layout =  [[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)]
layout += [[sg.Button('Save'), sg.Button('Exit')]]
```

Anytime you have 2 layouts, you can concatenate them by simple addition.  Make sure your layout is a "list of lists" layout.  In the above example, we know the first line is a generated layout of the input rows.  The last line adds onto the layout another layout... note the format being [ [ ] ].

This button definition is an entire layout, making it possible to add to our list comprehension

`[[sg.Button('Save'), sg.Button('Exit')]]`

It's quite readable code.  The 2 layouts line up visually quite well.

But let's not stop there with compressing the code.  How about removing that += and instead change the layout into a single line with just a `+` between the two sets of row.

Doing this concatenation on one line, we end up with this single statement that creates the **entire layout** for the GUI:

```python
layout =  [[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]
```

### Final "To Do List" Program

And here we have our final program... all **4** lines.

```python
import PySimpleGUI as sg

layout  = [[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('To Do List Example', layout)

event, values = window.read()
```

If you really wanted to crunch things down, you can make it a 2 line program (an import and 1 line of code) by moving the layout into the call to `Window`

```python
import PySimpleGUI as sg

event, values = sg.Window('To Do List Example', layout=[[sg.Text(f'{i}. '), sg.In(key=i)] for i in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]).read()
```


## Example - List Comprehension to Build Rows - Table Simulation - Grid of Inputs

In this example we're building a "table" that is 4 wide by 10 high using `Input` elements

The end results we're seeking is something like this:

```
HEADER 1    HEADER 2    HEADER 3    HEADER 4
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
INPUT       INPUT       INPUT       INPUT
```

Once the code is completed, here is how the result will appear:

![image](https://user-images.githubusercontent.com/46163555/63626328-b4480900-c5d0-11e9-9c81-52e3b0516bde.png)

We're going to be building each row using a list comprehension and we'll build the table by concatenating rows using another list comprehension.  That's a list comprehension that goes across and another list comprehension that goes down the layout, adding one row after another.

### Building the Header

First let's build the header.  There are 2 concepts to notice here:

```python
import PySimpleGUI as sg

headings = ['HEADER 1', 'HEADER 2', 'HEADER 3','HEADER 4']  # the text of the headings
header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]  # build header layout
```

There are 2 things in this code to note
1. The list comprehension that makes the heading elements
2. The spaces added onto the front

Let's start with the headers themselves.

This is the code that makes a row of Text Elements containing the text for the headers.  The result is a list of Text Elements, a row.

```python
[sg.Text(h, size=(14,1)) for h in headings]
```

Then we add on a few spaces to shift the headers over so they are centered over their columns.  We do this by simply adding a `Text` Element onto the front of that list of headings.

```python
header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]
```

This `header` variable is a layout with 1 row that has a bunch of `Text` elements with the headings.

### Building the Input Elements

The `Input` elements are arranged in a grid.  To do this we will be using a double list comprehension.  One will build the row the other will add the rows together to make the grid.  Here's the line of code that does that:

```python
input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]
```

This portion of the statement makes a single row of 4 `Input` Elements

```python
[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)]
```

Next we take that list of `Input` Elements and make as many of them as there are rows, 10 in this case.  We're again using Python's awesome list comprehensions to add these rows together.

```python
input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]
```

The first part should look familiar since it was just discussed as being what builds a single row.  To make the matrix, we simply take that single row and create 10 of them, each being a list.


### Putting it all together

Here is our final program that uses simple addition to add the headers onto the top of the input matrix.  To make it more attractive, the color theme is set to 'Dark Brown 1'.

```python
import PySimpleGUI as sg

sg.theme('Dark Brown 1')

headings = ['HEADER 1', 'HEADER 2', 'HEADER 3','HEADER 4']
header =  [[sg.Text('  ')] + [sg.Text(h, size=(14,1)) for h in headings]]

input_rows = [[sg.Input(size=(15,1), pad=(0,0)) for col in range(4)] for row in range(10)]

layout = header + input_rows

window = sg.Window('Table Simulation', layout, font='Courier 12')
event, values = window.read()
```

![image](https://user-images.githubusercontent.com/46163555/70472374-f7a18700-1a9c-11ea-9cd1-27d386cd9066.png)


## User Defined Elements / Compound Elements

"User Defined Elements" and "Compound Elements" are one or more PySimpleGUI Elements that are wrapped in a function definition. In a layout, they have the appearance of being a custom elements of some type.

User Defined Elements are particularly useful when you set a lot of parameters on an element that you use over and over in your layout.

### Example - A Grid of Buttons for Calculator App

Let's say you're making a calculator application with buttons that have these settings:

* font = Helvetica 20
* size = 5,1
* button color = white on blue

The code for **one** of these buttons is:

```python
sg.Button('1', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20))
```

If you have 6 buttons across and 5 down, your layout will have 30 of these lines of text.

One row of these buttons could be written:
```python
    [sg.Button('1', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20)),
     sg.Button('2', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20)),
     sg.Button('3', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20)),
     sg.Button('log', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20)),
     sg.Button('ln', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20)),
     sg.Button('-', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20))],
```

By using User Defined Elements, you can significantly shorten your layouts.  Let's call our element `CBtn`.  It would be written like this:

```python
def CBtn(button_text):
    return sg.Button(button_text, button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20))
```

Using your new `CBtn` Element, you could rewrite the row of buttons above as:
```python
[CBtn('1'), CBtn('2'), CBtn('3'), CBtn('log'), CBtn('ln'), CBtn('-')],
```

See the tremendous amount of code you do not have to write!  USE this construct any time you find yourself copying an element many times.

But let's not stop there.

Since we've been discussing list comprehensions, let's use them to create this row.  The way to do that is to make a list of the symbols that go across the row make a loop that steps through that list.  The result is a list that looks like this:

```python
[CBtn(t) for t in ('1','2','3', 'log', 'ln', '-')],
```

That code produces the same list as this one we created by hand:

```python
[CBtn('1'), CBtn('2'), CBtn('3'), CBtn('log'), CBtn('ln'), CBtn('-')],
```

### Compound Elements

Just like a `Button` can be returned from a User Defined Element, so can multiple Elements.

Going back to the To-Do List example we did earlier, we could have defined a User Defined Element that represented a To-Do Item and this time we're adding a checkbox. A single line from this list will be:

* The item # (a `Text` Element)
* A `Checkbox` Element to indicate completed
* An `Input` Element to type in what to do

The definition of our User Element is this `ToDoItem` function.  It is a single User Element that is a combination of 3 PySimpleGUI Elements.

```python
def ToDoItem(num):
    return [sg.Text(f'{num}. '), sg.CBox(''), sg.In()]
```

This makes creating a list of 5 to-do items downright trivial when combined with the list comprehension techniques we learned earlier.  Here is the code required to create 5 entries in our to-do list.

```python
layout = [ToDoItem(x) for x in range(1,6)]
```

We can then literally add on the buttons

```python
layout = [ToDoItem(x) for x in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]
```

And here is our final program
```python
import PySimpleGUI as sg

def ToDoItem(num):
    return [sg.Text(f'{num}. '), sg.CBox(''), sg.In()]

layout = [ToDoItem(x) for x in range(1,6)] + [[sg.Button('Save'), sg.Button('Exit')]]

window = sg.Window('To Do List Example', layout)
event, values = window.read()
```

And the window it creates looks like this:

![image](https://user-images.githubusercontent.com/46163555/63628682-cda28280-c5db-11e9-92a4-44ec2cb6ccf9.png)


---

# Elements

You will find information on Elements and all other classes and functions are located in the Call Reference Tab of the documentation.

"Elements" are the building blocks used to create windows.  Some GUI APIs use the term "Widget" to describe these graphic elements.  So that it's clear when a PySimpleGUI *Element* is being referenced versus an underlying GUI Framework's *Widget*.  PySimpleGUI Elements map to a GUI Framework Widget, usually in a 1-to-1 manner.  For example, a Text Element is implemented in tkinter using a Label Widget.

## Table of Elements in Tkinter Port

Each port of PySimpleGUI has a core set of Elements as well as port-specific elements.  Some port-specific elements include the Dial element in the Qt port, and the Pane element in the tkinter port.

| Element Name        | Aliases                        | tkinter Widget                          | Description                                                  |
| :------------------ | :----------------------------- | :-------------------------------------- | :----------------------------------------------------------- |
| Text                | T, Txt                         | tk.Label                                | One or more lines of Text                                    |
| Input               | I, In, InputText               | tk.Entry                                | Single line text input                                       |
| Combo               | DD, Drop, DropDown, InputCombo | ttk.Combobox                            | A "Dropdown" list that can be edited too                     |
| OptionMenu          | InputOptionMenu                | tk.OptionMenu                           | Like a Combo                                                 |
| Multiline           | ML, MLine                      | tk.Text or tk.scrolledtext.ScrolledText | Multiple lines of text for input or output                   |
| Output              |                                | tk.Text (sorta)                         | Not suggested. Multiline is better choice. Re-routes stdout  |
| Radio               | R, Rad                         | tk.Radiobutton                          | Radio Buttons - choose 1 from several                        |
| Checkbox            | CB, CBox, Check                | tk.Checkbutton                          | Checkbox - binary choice Yes/No                              |
| Spin                | Sp                             | tk.Spinbox                              | Choose 1 by using arrows. Can manually enter also            |
| Button              | B, Btn                         | tk.Button or ttk.Button                 | Button - plain or with image                                 |
| Image               | Im                             | tk.Label                                | A PNG or GIF image                                           |
| Canvas              |                                | tk.Canvas                               | A drawing area. Graph may be batter to use                   |
| Column              | Col                            | Combination Canvas & Frame              | Embeds layouts inside layouts                                |
| Frame               | Fr                             | tk.LabelFrame                           | A frame with a title and a border                            |
| Tab                 |                                | tk.Frame                                | Container used with TabGroup                                 |
| TabGroup            |                                | ttk.Notebook                            | Holds Tabs in layouts                                        |
| Pane                |                                | tk.PanedWindow                          | Sliding columns (it's kinda weird but useful)                |
| Graph               | G                              | tk.Canvas                               | A drawing area with primitives                               |
| Slider              | Sl                             | tk.Scale                                | Slider to choose from range of choices                       |
| Listbox             | LB, LBox                       | tk.Listbox                              | Listbox - a list of choices                                  |
| Menu                | MenuBar, Menubar               | tk.Menu                                 | A standard Menubar                                           |
| MenubarCustom       |                                | Combined Elements                       | Custom colors and font for menubar                           |
| ButtonMenu          | BM, BMenu                      | tk.Menubutton                           | Button that shows a menu                                     |
| Titlebar            |                                | Combined Elements                       | Custom colors for a titlebar                                 |
| ProgressBar         | PBar, Prog, Progress           | ttk.Progressbar                         |                                                              |
| Table               |                                | ttk.Treeview                            | A table with clickible cells and headers                     |
| Tree                |                                | ttk.Treeview                            | A tree with collapsible sections                             |
| VerticalSeparator   | VSep, VSeparator               | ttk.Separator                           | Vertical line                                                |
| HorizontalSeparator | HSep, HSeparator               | ttk.Separator                           | Horizontal line                                              |
| StatusBar           | SBar                           | tk.Label                                | Statusbar for bottom of window                               |
| Sizegrip            | SGrip                          | ttk.Sizegrip                            | A grip for the bottom right corner of a window               |
| Push                | P, Stretch                     | PySimpleGUI Elements                    | Pushes elements horizontally                                 |
| VPush               | VP, VStretch                   | PySimpleGUI Elements                    | Pushes rows vertically                                       |
| Sizer               |                                | Column Element                          | Creates a Width x Height number of pixels for padding/sizing |


## Layout Helper Functions

Your Window's layout is composed of lists of Elements.  In addition to elements, these Layout Help Functions may also be present in a layout definition


| Layout Helper | Description                                                                                                                               |
| :------------ | :---------------------------------------------------------------------------------------------------------------------------------------- |
| pin           | "Pins" an element to a location in a layout. If element transitions from invisible to visible, pin ensures element is in correct location |
| vtop          | Vertically align element or row of elements to the top of the row                                                                         |
| vbottom       | Vertically align element or row of elements to the bottom of the row                                                                      |
| vcenter       | Vertically align element or row of elements to the center of the row                                                                      |






- Text
- Single Line Input
- Buttons including these types:
	- File Browse
	- Folder Browse
	- Calendar picker
	- Date Chooser
	- Read window
	- Close window ("Button" & all shortcut buttons)
	- Realtime


## Keys

***Keys are a super important concept to understand in PySimpleGUI.***

If you are going to do anything beyond the basic stuff with your GUI, then you need to understand keys.

You can think of a "key" as a "name" for an element. Or an "identifier".  It's a way for you to identify and talk about an element with the PySimpleGUI library.  It's the exact same kind of key as a dictionary key.  They must be unique to a window.

Keys are specified when the Element is created using the `key` parameter.

Keys are used in these ways:
* Specified when creating the element
* Returned as events. If an element causes an event, its key will be used
* In the `values` dictionary that is returned from `window.read()`
* To make updates (changes), to an element that's in the window


After you put a key in an element's definition, the values returned from `window.read` will use that key to tell you the value.  For example, if you have an input element in your layout:

`Input(key='mykey')`

And your read looks like this: `event, values = Read()`

Then to get the input value from the read it would be: `values['mykey']`

You also use the same key if you want to call Update on an element.  Please see the section Updating Elements to understand that usage.  To get find an element object given the element's key, you can call the window method `find_element` (also written `FindElement`, `element`), or you can use the more common lookup mechanism:

```python
window['key']
```

While you'll often see keys written as strings in examples in this document, know that keys can be ***ANYTHING***.

Let's say you have a window with a grid of input elements.  You could use their row and column location as a key (a tuple)

`key=(row, col)`

Then when you read the `values` variable that's returned to you from calling `Window.read()`, the key in the `values` variable will be whatever you used to create the element. In this case you would read the values as:
`values[(row, col)]`

Most of the time they are simple text strings.  In the Demo Programs, keys are written with this convention:
`_KEY_NAME_` (underscore at beginning and end with all caps letters) or the most recent convention is to use a dash at the beginning and end (e.g. `'-KEY_NAME-'`).  You don't have to follow the convention, but it's not a bad one to follow as other users are used to seeing this format and it's easy to spot when element keys are being used.

If you have an element object, to find its key, access the member variable `.Key` for the element.  This assumes you've got the element in a variable already.

```python
text_elem = sg.Text('', key='-TEXT-')

the_key = text_elem.Key
```

### Default Keys

If you fail to place a key on an Element, then one will be created for you automatically.

For `Buttons`, the text on the button is that button's key. `Text` elements will default to the text's string (for when events are enabled and the text is clicked)

If the element is one of the input elements (one that will cause an generate an entry in the return values dictionary) and you fail to specify one, then a number will be assigned to it beginning with the number 0.  The effect will be as if the values are represented as a list even if a dictionary is used.

### Menu Keys

Menu items can have keys associated with them as well.  See the section on Menus for more information about these special keys. They aren't the same as Element keys.  Like all elements, Menu Element have one of these Element keys.  The individual menu item keys are different.

### `WRITE_ONLY_KEY` Modifier

Sometimes you have input elements (e.g. `Multiline`) that you are using as an output.  The contents of these elements may get very long.  You don't need to "read" these elements and doing so will potentially needlessly return a lot of data.

To tell PySimpleGUI that you do not want an element to return a value when `Window.read` is called, add the string `WRITE_ONLY_KEY` to your key name.

If your `Multiline` element was defined like this originally:

```python
sg.Multiline(size=(40,8), key='-MLINE-')
```

Then to turn off return values for that element, the `Multiline` element would be written like this:

```python
sg.Multiline(size=(40,8), key='-MLINE-' + sg.WRITE_ONLY_KEY)
```

## Key Errors - Key error recovery algorithm

In the primary (tkinter) port of PySimpleGUI, starting in version 4.27.0 (not yet on PyPI... but available on GitHub as 4.26.0.14+)

There are now 3 controls over key error handling and a whole new era of key reporting.

```python
SUPPRESS_ERROR_POPUPS = False
SUPPRESS_RAISE_KEY_ERRORS = False
SUPPRESS_KEY_GUESSING = False
```

You can modify these values by calling `set_options`.

```python
    sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=False, suppress_key_guessing=False)
```

A basic definition of them are:
`suppress_error_popups` - Disables error popups that are generated within PySimpleGUI itself to not be shown
`suppress_raise_key_errors` - Disables raising a key error if a key or a close match are not found
`suppress_key_guessing` - Disables the key guessing algorithm should you have a key error

With the defaults left as defined (all `False`), here is how key errors work.

This is the program being used in this example:

```python
import PySimpleGUI as sg

def main():
    sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=False, suppress_key_guessing=False)

    layout = [  [sg.Text('My Window')],
                [sg.Input(k='-IN-'), sg.Text(size=(12,1), key='-OUT-')],
                [sg.Button('Go'), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout, finalize=True)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        window['-O U T'].update(values['-IN-'])
    window.close()


def func():

    main()

func()
```

A few things to note about it:

* There are multiple levels of functions being called, not just a flat program
* There are 2 keys explicitly defined, both are text at this point (we'll change them later)
* There are 2 lookups happening, one with `window` the other with `values`

This key error recovery algorithm only applies to element keys being used to lookup keys inside of windows.  The `values` key lookup is a plain dictionary and so nothing fancy is done for that lookup.


### Example 1 - Simple text string misspelling

In our example, this line of code has an error:

```python
window['-O U T'].update(values['-IN-'])
```

There are multiple problems with the key `'-OUT-'`.  It is missing a dash and it has a bunch of extra spaces.

When the program runs, you'll first see the layout with no apparent problems:

![SNAG-0882](https://user-images.githubusercontent.com/46163555/88704649-60954800-d0dc-11ea-885a-1ebadba039b7.jpg)


Clicking the OK button will cause the program to return from `window.read()` and thus hit our bad key.  The result will be a popup window that resembles this:

![SNAG-0883](https://user-images.githubusercontent.com/46163555/88704635-5bd09400-d0dc-11ea-88a2-42e7386b076b.jpg)


Note a few things about this error popup.  Your shown your bad key and you're also shown what you likely meant.  Additionally, you're shown the filename, the line number and the line of code itself that has the error.

Because this error was recoverable, the program continues to run after you close the error popup.  The result is what you expect from this program... the output field is the same as your information input.

![SNAG-0884](https://user-images.githubusercontent.com/46163555/88704691-71de5480-d0dc-11ea-8800-9379044a3f1f.jpg)


### Example 2 - Tuple error

Keys can be a variety of types, including tuples.  In this particular program we have a tuple specified in the layout and have used an incorrect tuple in the lookup.  Once again the recovery process worked and the program continued.

![SNAG-0885](https://user-images.githubusercontent.com/46163555/88705188-2d9f8400-d0dd-11ea-9a91-f92cef9f6219.jpg)


### Example 3 - No close match found

In this example, as you can see in the error popup, there was such a mismatch that no substitution could be performed.

![SNAG-0886](https://user-images.githubusercontent.com/46163555/88705707-e6fe5980-d0dd-11ea-8fcc-bc024298705d.jpg)


This is an unrecoverable error, so a key error exception is raised.

```python

Traceback (most recent call last):
  File "C:/Users/mike/.PyCharmCE2019.1/config/scratches/scratch_978 - key error example.py", line 25, in <module>
    func()
  File "C:/Users/mike/.PyCharmCE2019.1/config/scratches/scratch_978 - key error example.py", line 23, in func
    main()
  File "C:/Users/mike/.PyCharmCE2019.1/config/scratches/scratch_978 - key error example.py", line 17, in main
    window[(1,2,3)].update(values['-IN-'])
  File "C:\Python\PycharmProjects\PSG\PySimpleGUI.py", line 8591, in __getitem__
    return self.FindElement(key)
  File "C:\Python\PycharmProjects\PSG\PySimpleGUI.py", line 7709, in FindElement
    raise KeyError(key)
KeyError: (1, 2, 3)
```

If you're running an IDE such as PyCharm, you can use the information from the assert to jump to the line of code in your IDE based on the crash data provided.


### Choose Your Desired Combination

There are enough controls on this error handling that you can control how you want your program to fail.  If you don't want any popups, and no guessing and would instead like to simply get an exception when the key error happens, then call `set_options` with this combination:


```python
    sg.set_options(suppress_raise_key_errors=False, suppress_error_popups=True, suppress_key_guessing=True)
```

This will cause Example #1 above to immediately get an exception when hitting the statement with the error.  Even though the guessing is turned off, you're still provided with the closest match to help with your debugging....

```
** Error looking up your element using the key:  -O U T The closest matching key:  -OUT-
Traceback (most recent call last):
  File "C:/Users/mike/.PyCharmCE2019.1/config/scratches/scratch_978 - key error example.py", line 25, in <module>
    func()
  File "C:/Users/mike/.PyCharmCE2019.1/config/scratches/scratch_978 - key error example.py", line 23, in func
    main()
  File "C:/Users/mike/.PyCharmCE2019.1/config/scratches/scratch_978 - key error example.py", line 17, in main
    window['-O U T'].update(values['-IN-'])
  File "C:\Python\PycharmProjects\PSG\PySimpleGUI.py", line 8591, in __getitem__
    return self.FindElement(key)
  File "C:\Python\PycharmProjects\PSG\PySimpleGUI.py", line 7709, in FindElement
    raise KeyError(key)
KeyError: '-O U T'
```




## Common Element Parameters

Some parameters that you  will see on almost all Element creation calls include:

- key   -  Used with window[key], events, and in return value dictionary
- tooltip   - Hover your mouse over the element and you'll get a popup with this text
- size  - (width, height) - usually measured in characters-wide, rows-high.  Sometimes they mean pixels
- font - specifies the font family, size, etc.
- colors - Color name or #RRGGBB string
- pad - Amount of padding to put around element
- enable_events - Turns on the element specific events
- visible - Make elements appear and disappear

#### Tooltip

Tooltips are text boxes that popup next to an element if you hold your mouse over the top of it.  If you want to be extra kind to your window's user, then you can create tooltips for them by setting the parameter `tooltip` to some text string.  You will need to supply your own line breaks / text wrapping.  If you don't want to manually add them, then take a look at the standard library package `textwrap`.

Tooltips are one of those "polish" items that really dress-up a GUI and show's a level of sophistication.  Go ahead, impress people, throw some tooltips into your GUI.  You can change the color of the background of the tooltip on the tkinter version of PySimpleGUI by setting `TOOLTIP_BACKGROUND_COLOR` to the color string of your choice.  The default value for the color is:

`TOOLTIP_BACKGROUND_COLOR = "#ffffe0"`


#### Size

Info on setting default element sizes is discussed in the Window section above.

Specifies the amount of room reserved for the Element.  For elements that are character based, such a Text, it is (# characters, # rows).  Sometimes it is a pixel measurement such as the Image element.  And sometimes a mix like on the Slider element (characters long by pixels wide).

Some elements, Text and Button, have an auto-size setting that is `on` by default. It will size the element based on the contents.  The result is that buttons and text fields will be the size of the string creating them.  You can turn it off.  For example, for Buttons, the effect will be that all buttons will be the same size in that window.

Beginning in release 4.47.0 sizes can also be an `int` in addition to a tuple.  If an int is specified, then that value is taken as the width and the height is set to 1. If given `size=12` then it's the same as `size=(12,1)`

#### Element Sizes - Non-tkinter Ports (Qt, WxPython, Web)

In non-tkinter ports you can set the specific element sizes in 2 ways.  One is to use the normal `size` parameter like you're used to using.  This will be in characters and rows.

The other way is to use a new parameter, `size_px`.  This parameter allows you to specify the size directly in pixels.  A setting of `size_px=(300,200)` will create an Element that is 300 x 200 pixels.

Additionally, you can also indicate pixels using the `size` parameter, **if the size exceeds the threshold for conversion.**  What does that mean?  It means if your width is > 20 (`DEFAULT_PIXEL_TO_CHARS_CUTOFF`), then it is assumed you're talking pixels, not characters.  However, some of the "normally large" Elements have a cutoff value of 100.  These include, for example, the `Multline` and `Output` elements.

If you're curious about the math used to do the character to pixels conversion, it's quite crude, but functional.  The conversion is completed with the help of this variable:

`DEFAULT_PIXELS_TO_CHARS_SCALING = (10,26)`

The conversion simply takes your `size[0]` and multiplies by 10 and your `size[1]` and multiplies it by 26.

##### Specifying Size as an INT

Beginning in version 4.47.0 you can specify a single int as the size.  This will set the size to be a single row in height (1).  Writing `size=10` is now the same as writing `size=(10,1)`. A tuple is created on your behalf when you specify a size and an int.  This will save a considerable amount of typing, especially for the elements where you typically have only 1 row or can only have 1 row.  

#### Colors

A string representing color.  Anytime colors are involved, you can specify the tkinter color name such as 'lightblue' or an RGB hex value '#RRGGBB'.  For buttons, the color parameter is a tuple (text color, background color)

Anytime colors are written as a tuple in PySimpleGUI, the way to figure out which color is the background is to replace the "," with the word "on".  ('white', 'red') specifies a button that is "white on red".  Works anywhere there's a color tuple.

#### Pad

The amount of room around the element in pixels. The default value is (5,3) which means leave 5 pixels on each side of the x-axis and 3 pixels on each side of the y-axis.  You can change this on a global basis using a call to SetOptions, or on an element basis.

If you want more pixels on one side than the other, then you can split the number into 2 number.  If you want 200 pixels on the left side, and 3 pixels on the right, the pad would be ((200,3), 3).  In this example, only the x-axis is split.

##### Specifying pad as an INT

Starting in version 4.47.0, it's possible to set pad to be an int rather than a tuple. If an int is specified, then the pad is set to a tuple with each position being the same as the int.  This reduces the code in your layout significantly if you use values such as (0,0) for your pad.  This is not an uncommon value.  Now you can write `pad=0` and you will get the same result as if you typed `pad=(0,0)`

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

**Font Style - Valid font styles include:**

* italic
* roman
* bold
* normal
* underline
* overstrike

An example with many styles is:

```python
font='Courier 12 italic bold underline overstrike'
```

The same styles can be used with the tuple format for fonts.


#### Key

See the section above that has full information about keys.


#### Visible

Beginning in version 3.17 you can create Elements that are initially invisible that you can later make visible.

To create an invisible Element, place the element in the layout like you normally would and add the parameter

`visible=False`.

Later when you want to make that Element visible you simply call the Element's `Update` method and pass in the parameter `visible=True`

This feature works best on Qt, but does work on the tkinter version as well.  The visible parameter can also be used with the Column and Frame "container" Elements.

Note - Tkinter elements behave differently than Qt elements in how they arrange themselves when going from invisible to visible.

tkinter elements tend to STACK themselves.

One workaround is to place the element in a Column with other elements on its row.  This will hold the place of the row it is to be placed on.  It will move the element to the end of the row however.

If you want to not only make the element invisible, on tkinter you can call `Element.

Qt elements tend to hold their place really well and the window resizes itself nicely.  It is more precise and less clunky.


## Shortcut Functions / Multiple Function Names

Perhaps not the best idea, but one that's done none the less is the naming of methods and functions.  Some of the more "Heavily Travelled Elements" (and methods/functions) have "shortcuts".

In other words, I am lazy and don't like to type. The result is multiple ways to do exactly the same thing.  Typically, the Demo Programs and other examples use the full name, or at least a longer name.  Thankfully PyCharm will show you the same documentation regardless which you use.

This enables you to code much quicker once you are used to using the SDK.  The Text Element, for example, has 3 different names `Text`, `Txt` or`T`.  InputText can also be written `Input` or `In` .

The shortcuts aren't limited to Elements.  The `Window` method `Window.FindElement` can be written as `Window.Element` because it's such a commonly used function.  BUT, even that has now been shortened to `window[key]`

It's an ongoing thing.  If you don't stay up to date and one of the newer shortcuts is used, you'll need to simply rename that shortcut in the code.  For examples Replace sg.T with sg.Text if your version doesn't have sg.T in it.


<!-- %!% -->
## Text Element | `T == Txt == Text`

Basic Element. It displays text.



```python
layout = [
            [sg.Text('This is what a Text Element looks like')],
         ]
```

![simple text](https://user-images.githubusercontent.com/13696193/44959877-e9d97b00-aec3-11e8-9d24-b4405ee4a148.jpg)


When creating a Text Element that you will later update, make sure you reserve enough characters for the new text.  When a Text Element is created without a size parameter, it is created to exactly fit the characters provided.

With proportional spaced fonts (normally the default) the pixel size of one set of characters will differ from the pixel size of a different set of characters even though the set is of the same number of characters.  In other words, not all letters use the same number of pixels.  Look at the text you're reading right now and you will see this.  An "i" takes up a less space then an "A".




---

## `Window.FindElement(key)` shortened to `Window[key]`

There's been a fantastic leap forward in making PySimpleGUI code more compact.

Instead of writing:
```python
window.FindElement(key).update(new_value)
 ```

You can now write it as:

```python
window[key].update(new_value)
 ```

This change has been released to PyPI for PySimpleGUI

MANY Thanks is owed to the nngogol that suggested and showed me how to do this.  It's an incredible find as have been many of his suggestions.


## `Element.update()` ->  `Element()` shortcut

This has to be one of the strangest syntactical constructs I've ever written.

It is best used in combination with `FindElement` (see prior section on how to shortcut `FindElement`).

Normally to change an element, you "find" it, then call its `update` method.  The code usually looks like this, as you saw in the previous section:

```python
window[key].update(new_value)
```

The code can be further compressed by removing the `.update` characters, resulting in this very compact looking call:

```python
window[key](new_value)
```

Yes, that's a valid statement in Python.

What's happening is that the element itself is being called.   You can also writing it like this:

```python
elem = sg.Text('Some text', key='-TEXT-')
elem('new text value')
```

Side note - you can also call your `window` variable directly.  If you "call" it it will actually call `Window.read`.

```python
window = sg.Window(....)
event, values = window()

# is the same as
window = sg.Window(....)
event, values = window.read()
```



It is confusing looking however so when used, it might be a good idea to write a comment at the end of the statement to help out the poor beginner programmer coming along behind you.

Because it's such a foreign construct that someone with 1 week of Python classes will not recognize, the demos will continue to use the `.update` method.

It does not have to be used in conjuction with `FindElement`.  The call works on any previously made Element.  Sometimes elements are created, stored into a variable and then that variable is used in the layout.  For example.

```python
graph_element = sg.Graph(...... lots of parms ......)

layout = [[graph_element]]
.
.
.
graph_element(background_color='blue')      # this calls Graph.update for the previously defined element
```

Hopefully this isn't too confusing.  Note that the methods these shortcuts replace will not be removed.  You can continue to use the old constructs without changes.


---

### Fonts

Already discussed in the common parameters section.  Either string or a tuple.

### Color in PySimpleGUI are in one of two formats - color name or RGB value.

Individual colors are specified using either the color names as defined in tkinter or an RGB string of this format:

	"#RRGGBB"        or          "darkblue"

### `auto_size_text      `
A `True` value for `auto_size_text`, when placed on Text Elements, indicates that the width of the Element should be shrunk do the width of the text.   The default setting is True.  You need to remember this when you create `Text` elements that you are using for output.

`Text(key='-TXTOUT-)` will create a `Text` Element that has 0 length.  Notice that for Text elements with an empty string, no string value needs to be indicated.  The default value for strings is `''` for Text Elements.  Prior to release 4.45.0 you needed to reserve enough room for your longest string. If you tried to output a string that's 5 characters, it wasn't shown in the window because there wasn't enough room.  The remedy was to manually set the size to what you expect to output

`Text(size=(15,1), key='-TXTOUT-)` creates a `Text` Element that can hold 15 characters.

With the newer versions, after 4.45.0, if you set no size at all, that is `size=(None, None)`, then both the `Text` element will grow and shrink to fit the text and so will the `Window`.  Additionally, if you indicate that the height is `None` then the element will grow and shrink in their to match the string.

The way the `Text` element now works is truly auto-sized.


### Chortcut functions
The shorthand functions for `Text` are `Txt` and `T`

### Events `enable_events`

If you set the parameter `enable_events` then you will get an event if the user clicks on the Text.


## Multiline Element
This Element doubles as both an input and output Element.


```python
layout = [[sg.Multiline('This is what a Multi-line Text Element looks like', size=(45,5))]]
```

![multiline](https://user-images.githubusercontent.com/13696193/44959853-b139a180-aec3-11e8-972f-f52188510c88.jpg)


This element has been expanded upon quite a bit over time.  Two of the more exciting additions have been

* Ability to output unique text and background colors on a per-character basis
* The `print` method that allows you to easily reroute your normally printed output to a multiline element instead

The `Multiline.print()` call is made using the same element-lookup technique you're used to using to call `update`.  One of these lookups generally appear:

```python
window['-MULTILINE KEY-']
```

To change one of your normal prints to output to your multiline element, you simply add the above lookup expression to the front of your print statement.

```python
print('My variables are', a, b, c)       # a normal print statement

window['-MULTILINE KEY-'].print('My variables are', a, b, c)     # Routed to your multiline element
```

It gets even better though.... you can add color to your prints

```python
# Outputs red text on a yellow background
window['-MULTILINE KEY-'].print('My variables are', a, b, c, text_color='red', background_color='yellow')

```


### Redefine print

Another way to use this print capability is to redefine the `print` statement itself.  This will allow you to leave your code entirely as is.  By adding this line of code your entire program will output all printed information to a multiline element.

```python
print = lambda *args, **kwargs: window['-MULTILINE KEY-'].print(*args, **kwargs)
```


## Text Input Element  | `InputText == Input == In`


```python
layout = [[sg.InputText('Default text')]]
```

![inputtext 2](https://user-images.githubusercontent.com/13696193/44959861-b5fe5580-aec3-11e8-8040-53ec241b5079.jpg)


---

#### Note about the `do_not_clear` parameter

This used to really trip people up, but don't think so anymore.  The `do_not_clear` parameter is initialized when creating the InputText Element.  If set to False, then the input field's contents will be erased after every `Window.read()` call.  Use this setting for when your window is an "Input Form" type of window where you want all of the fields to be erased and start over again every time.



## Combo Element | `Combo == InputCombo == DropDown == Drop`
Also known as a drop-down list.  Only required parameter is the list of choices.  The return value is a string matching what's visible on the GUI.


```python
layout = [[sg.Combo(['choice 1', 'choice 2'])]]
```

![combobox](https://user-images.githubusercontent.com/13696193/44959860-b565bf00-aec3-11e8-82fe-dbe41252458b.jpg)


## Listbox Element
The standard listbox like you'll find in most GUIs.  Note that the return values from this element will be a ***list of results, not a single result***. This is because the user can select more than 1 item from the list (if you set the right mode).


```python
layout = [[sg.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6))]]
```

![listbox 2](https://user-images.githubusercontent.com/13696193/44959859-b4cd2880-aec3-11e8-881c-1e369d5c6337.jpg)


---

ListBoxes can cause a window to return from a Read call.  If the flag `enable_events` is set, then when a user makes a selection, the Read immediately returns.

Another way ListBoxes can cause Reads to return is if the flag bind_return_key is set.  If True, then if the user presses the return key while an entry is selected, then the Read returns.  Also, if this flag is set, if the user double-clicks an entry it will return from the Read.

## Slider Element

Sliders have a couple of slider-specific settings as well as appearance settings. Examples include the `orientation` and `range` settings.


```python
layout = [[sg.Slider(range=(1,500),
         default_value=222,
         size=(20,15),
         orientation='horizontal',
         font=('Helvetica', 12))]]
```

![slider](https://user-images.githubusercontent.com/13696193/44959858-b4349200-aec3-11e8-9e25-c0fcf025d19e.jpg)

### Qt Sliders

There is an important difference between Qt and tkinter sliders.  On Qt, the slider values must be integer, not float.  If you want your slider to go from 0.1 to 1.0, then make your slider go from 1 to 10 and divide by 10.  It's an easy math thing to do and not a big deal.  Just deal with it.... you're writing software after all.  Presumably you know how to do these things.  ;-)

## Radio Button Element

Creates one radio button that is assigned to a group of radio buttons.  Only 1 of the buttons in the group can be selected at any one time.


```python
layout =  [
	[sg.Radio('My first Radio!', "RADIO1", default=True),
	sg.Radio('My second radio!', "RADIO1")]
]
```

![radio](https://user-images.githubusercontent.com/13696193/44959857-b4349200-aec3-11e8-8e2d-e6a49ffbd0b6.jpg)


## Checkbox Element | `CBox == CB == Check`
Checkbox elements are like Radio Button elements.  They return a bool indicating whether or not they are checked.


```python
layout =  [[sg.Checkbox('My first Checkbox!', default=True), sg.Checkbox('My second Checkbox!')]]
```
![checkbox](https://user-images.githubusercontent.com/13696193/44959906-6f5d2b00-aec4-11e8-9c8a-962c787f0286.jpg)


## Spin Element
An up/down spinner control.  The valid values are passed in as a list.


```python
layout =  [[sg.Spin([i for i in range(1,11)], initial_value=1), sg.Text('Volume level')]]
```

![spinner](https://user-images.githubusercontent.com/13696193/44959855-b1d23800-aec3-11e8-9f51-afb2109879da.jpg)


## Image Element

Images can be placed in your window provide they are in PNG, GIF, PPM/PGM format.  JPGs cannot be shown because tkinter does not naively support JPGs.  You can use the Python Imaging Library (PIL) package  to convert your image to PNG prior to calling PySimpleGUI if your images are in JPG format.

```python
layout = [
            [sg.Image(r'C:\PySimpleGUI\Logos\PySimpleGUI_Logo_320.png')],
         ]
```


![image](https://user-images.githubusercontent.com/13696193/61885709-4e326e00-aecc-11e9-8695-7193df2831ec.png)


You can specify an animated GIF as an image and can animate the GIF by calling `UpdateAnimation`.  Exciting stuff!

![loading animation](https://user-images.githubusercontent.com/13696193/51280871-d2041e80-19ae-11e9-8757-802eb95352ed.gif)

You can call the method without setting the `time_between_frames` value and it will show a frame and immediately move on to the next frame.  This enables you to do the inter-frame timing.

## Button Element

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

Most programs will use a combination of shortcut button calls (Submit, Cancel, etc.), normal Buttons which leave the windows open and CloseButtons that close the window when clicked.

Sometimes there are multiple names for the same function.  This is simply to make the job of the programmer quicker and easier.  Or they are old names that are no longer used but kept around so that existing programs don't break.

The 4 primary windows of PySimpleGUI buttons and their names are:

1. `Button`= `ReadButton` = `RButton` = `ReadFormButton` (Use `Button`, others are old methods)
2. `CloseButton` = `CButton`
3. `RealtimeButton`
4. `DummyButton`

You will find the long-form names in the older programs. ReadButton for example.

In Oct 2018, the definition of Button changed.  Previously Button would CLOSE the window when clicked.  It has been changed so the Button calls will leave the window open in exactly the same way as a ReadButton.  They are the same calls now.   To enables windows to be closed using buttons, a new button was added... `CloseButton` or `CButton`.

Your PySimpleGUI program is most likely going to contain only `Button` calls. The others are generally not found in user code.

The most basic Button element call to use is `Button`


```python
layout =  [[sg.Button('Ok'), sg.Button('Cancel')]]
```

![ok cancel 3](https://user-images.githubusercontent.com/13696193/44959927-aa5f5e80-aec4-11e8-86e1-5dc0b3a2b803.jpg)

You will rarely see these 2 buttons in particular written this way.  Recall that PySimpleGUI is focused on YOU (which generally directly means.... less typing).  As a result, the code for the above window is normally written using shortcuts found in the next section.

You will typically see this instead of calls to `Button`:

```python
layout =  [[sg.Ok(), sg.Cancel()]]
```

In reality `Button` is in fact being called on your behalf.  Behind the scenes, `sg.Ok` and `sg.Cancel` call `Button` with the text set to `Ok` and `Cancel` and returning the results that then go into the layout.  If you were to print the layout it will look identical to the first layout shown that has `Button` shown specifically in the layout.

### TTK Buttons & Macs

In 2019 support for ttk Buttons was added.  This gets around the problem of not being able to change button colors on a Mac.  There are a number of places you can control whether or not ttk buttons are used, be it on MAc or other platform.

TTK Buttons and TK Buttons operate slightly differently.  Button highlighting is one different.  How images and text are displayed at the same time is another.  You've got options now that weren't there previously.  It's nice to see that Mac users can finally use the color themes.

### Button Element Shortcuts
These Pre-made buttons are some of the most important elements of all because they are used so much.  They all basically do the same thing, **set the button text to match the function name and set the parameters to commonly used values**. If you find yourself needing to create a custom button often because it's not on this list, please post a request on GitHub. . They include:

- OK
- Ok
- Submit
- Cancel
- Yes
- No
- Exit
- Quit
- Help
- Save
- SaveAs
- Open

### "Chooser" Buttons

These buttons are used to show dialog boxes that choose something like a filename, date, color, etc.. that are filled into an `InputText` Element (or some other "target".... see below regarding targets)

- CalendarButton
- ColorChooserButton
- FileBrowse
- FilesBrowse
- FileSaveAs
- FolderBrowse

**IMPORT NOTE ABOUT SHORTCUT BUTTONS**
Prior to release 3.11.0, these buttons closed the window.  Starting with 3.11 they will not close the window.  They act like RButtons (return the button text and do not close the window)

If you are having trouble with these buttons closing your window, please check your installed version of PySimpleGUI by typing `pip list` at a command prompt.  Prior to 3.11 these buttons close your window.

Using older versions, if you want a Submit() button that does not close the window, then you would instead use RButton('Submit').   Using the new version, if you want a Submit button that closes the window like the sold Submit() call did, you would write that as `CloseButton('Submit')` or `CButton('Submit')`

### Button targets

The `FileBrowse`, `FolderBrowse`, `FileSaveAs` , `FilesSaveAs`, `CalendarButton`, `ColorChooserButton` buttons all fill-in values into another element located on the window.  The target can be a Text Element or an InputText Element or the button itself.  The location of the element is specified by the `target` variable in the function call.

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

```python
layout = [[sg.T('Source Folder')],
              [sg.In()],
              [sg.FolderBrowse(target=(-1, 0)), sg.OK()]]
```

or if using keys, then the code would be:

```python
layout = [[sg.T('Source Folder')],
              [sg.In(key='input')],
              [sg.FolderBrowse(target='input'), sg.OK()]]
```

See how much easier the key method is?

#### Invisible Targets

One very handy trick is to make your target invisible.  This will remove the ability to edit the chosen value like you normally would be able to with an Input Element.  It's a way of making things look cleaner, less cluttered too perhaps.

### Save & Open Buttons

There are 4 different types of File/Folder open dialog box available.  If you are looking for a file to open, the `FileBrowse` is what you want. If you want to save a file, `SaveAs` is the button. If you want to get a folder name, then `FolderBrowse` is the button to use. To open several files at once, use the `FilesBrowse` button.  It will create a list of files that are separated by ';'

![open](https://user-images.githubusercontent.com/13696193/45243804-2b529780-b2c3-11e8-90dc-6c9061db2a1e.jpg)

![folder](https://user-images.githubusercontent.com/13696193/45243805-2b529780-b2c3-11e8-95ee-fec3c0b11319.jpg)

![saveas](https://user-images.githubusercontent.com/13696193/45243807-2beb2e00-b2c3-11e8-8549-ba71cdc05951.jpg)


### Calendar Buttons

These buttons pop up a calendar chooser window.  The chosen date is returned as a string.

![calendar](https://user-images.githubusercontent.com/13696193/45243374-99965a80-b2c1-11e8-8311-49777835ca40.jpg)

### Color Chooser Buttons

These buttons pop up a standard color chooser window.  The result is returned as a tuple.  One of the returned values is an RGB hex representation.

![color](https://user-images.githubusercontent.com/13696193/45243375-99965a80-b2c1-11e8-9779-b71bed85fab6.jpg)


### Custom Buttons
Not all buttons are created equal.  A button that closes a window is different that a button that returns from the window without closing it.  If you want to define your own button, you will generally do this with the Button Element `Button`, which closes the window when clicked.

```python
layout =  [[sg.Button('My Button')]]
```

![button](https://user-images.githubusercontent.com/13696193/44959862-b696ec00-aec3-11e8-9e88-4b9af0338a03.jpg)

All buttons can have their text changed by changing the `button_text` parameter in the button call.  It is this text that is returned when a window is read.  This text will be what tells you which button was clicked.  However, you can also use keys on your buttons so that they will be unique.  If only the text were used, you would never be able to have 2 buttons in the same window with the same text.

```python
layout =  [[sg.Button('My Button', key='_BUTTON_KEY_')]]
```

With this layout, the event that is returned from a `Window.read()` call when the button is clicked will be "`_BUTTON_KEY_`"


### Button Images

Now this is an exciting feature not found in many simplified packages.... images on buttons!  You can make a pretty spiffy user interface with the help of a few button images.

This is one of the quickest and easiest ways to transform tkinter from a "1990s looking GUI" into a "modern GUI".  If you don't like the default buttons, then simply bring your own button images and use those instead.

Your button images need to be in PNG or GIF format.  When you make a button with an image, set the button background to the same color as the background.  You can get the theme's background color by calling `theme_background_color()`

`TRANSPARENT_BUTTON` - **Important** - This is a legacy value that is misleading.  It is currently defined as this constant value:

```python
TRANSPARENT_BUTTON = ('#F0F0F0', '#F0F0F0')
```

As you can see it is simply a tuple of 2 gray colors.  The effect is that the button text and the button background color to a specific shade of gray.  Way back in time, before you could change the background colors and all windows were gray, this value worked. But now that your button can be on any background color, you'll want to set the buttons color to match the background so that your button blends with the background color.

```python
sg.Button('Restart Song', button_color=(sg.theme_background_color(), sg.theme_background_color()),
               image_filename=image_restart, image_size=(50, 50), image_subsample=2, border_width=0)
```

There are several parameters in `Button` elements that are used for button images.

```
image_filename - Filename of image. Can be a relative path
image_data - A Base64 image
image_size - Size of image in pixels
image_subsample - Amount to divide the size by.  2 means your image will be 1/2 the size.  3 means 1/3
```

Here's an example window made with button images.

![media file player](https://user-images.githubusercontent.com/13696193/43161977-9ee7cace-8f57-11e8-8ff8-3ea24b69dab9.jpg)

You'll find the source code in the file Demo Media Player.  Here is what the button calls look like to create media player window

 ```python
sg.Button('Pause', button_color=(sg.theme_background_color(), sg.theme_background_color()),
              image_filename=image_pause,
              image_size=(50, 50),
              image_subsample=2,
              border_width=0)
```

Experimentation is sometimes required for these concepts to really sink in and they can vary depending on the underlying GUI framework.

Button Images do work so play with them.  You can use PIL to change the size of your images before passing to PySimpleGUI.

### Realtime Buttons

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

window = sg.Window('Robotics Remote Control', gui_rows)

#
# Some place later in your code...
# You need to perform a Read or Refresh call on your window every now and then or
# else it will apprear as if the program has locked up.
#
# your program's main loop
while (True):
    # This is the code that reads and updates your window
    event, values = window.read(timeout=50)
    print(event)
    if event in ('Quit', sg.WIN_CLOSED):
        break

window.close()  # Don't forget to close your window!
```

This loop will read button values and print them.  When one of the Realtime buttons is clicked, the call to `window.read` will  return a button name matching the name on the button that was depressed or the key if there was a key assigned to the button.  It will continue to return values as long as the button remains depressed.  Once released, the Read will return timeout events until a button is again clicked.

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


## ButtonMenu Element

The ButtonMenu element produces a unique kind of effect.  It's a button, that when clicked, shows you a menu.   It's like clicking one of the top-level menu items on a MenuBar.  As a result, the menu definition take the format of a single  menu entry from  a normal menu definition.  A normal menu definition is  a list of lists.  This definition is one of those lists.


```python
 ['Menu', ['&Pause Graph', 'Menu item::optional_key']]
```


The very first string normally specifies what is shown on the menu bar.  In this case, the value is **not used**.  You set the text for the button using a different parameter, the `button_text` parm.


One use of this element is to make a "fake menu bar" that has a colored background.  Normal menu bars cannot have their background color changed.  Not so with ButtonMenus.

![buttonmenu](https://user-images.githubusercontent.com/13696193/50387000-bc0d8180-06c0-11e9-8d17-3b22ed665e78.gif)

Return values for ButtonMenus are sent via the return values dictionary.  If a selection is made, then an event is generated that will equal the ButtonMenu's key value.  Use that key value to look up the value selected by the user.  This is the same mechanism as the Menu Bar Element, but differs from the pop-up (right click) menu.



## VerticalSeparator Element

This element has limited usefulness and is being included more for completeness than anything else.  It will draw a line between elements.

It works best when placed between columns or elements that span multiple rows.  If on a "normal" row with elements that are only 1 row high, then it will only span that one row.

```python
VerticalSeparator(pad=None)
```



![snag-0129](https://user-images.githubusercontent.com/13696193/47376041-a92a0100-d6bf-11e8-8f5b-0c0df56cf0f3.jpg)


## HorizontalSeparator Element

In PySimpleGUI, the tkinter port, there is no `HorizontalSeparator` Element.  One will be added as a "stub" so that code is portable.  It will likely do nothing just like the `Stretch` Element.

An easy way to get a horizontal line in PySimpleGUI is to use a `Text` Element that contains a line of underscores

```python
sg.Text('_'*30)             # make a horizontal line stretching 30 characters
```


## ProgressBar Element
The `ProgressBar` element is used to build custom Progress Bar windows.  It is HIGHLY recommended that you use OneLineProgressMeter that provides a complete progress meter solution for you.  Progress Meters are not easy to work with because the windows have to be non-blocking and they are tricky to debug.

The **easiest** way to get progress meters into your code is to use the `OneLineProgressMeter` API.  This consists of a pair of functions, `OneLineProgressMeter` and `OneLineProgressMeterCancel`.  You can easily cancel any progress meter by calling it with the current value = max value.  This will mark the meter as expired and close the window.
You've already seen OneLineProgressMeter calls presented earlier in this readme.

```python
sg.OneLineProgressMeter('My Meter', i+1, 1000,  'key', 'Optional message')
```

The return value for `OneLineProgressMeter` is:
`True` if meter updated correctly
`False` if user clicked the Cancel button, closed the window, or vale reached the max value.


#### Progress Meter in Your window
Another way of using a Progress Meter with PySimpleGUI is to build a custom window with a `ProgressBar` Element in the window.  You will need to run your window as a non-blocking window.  When you are ready to update your progress bar, you call the `UpdateBar` method for the `ProgressBar` element itself.


```python
import PySimpleGUI as sg

# layout the window
layout = [[sg.Text('A custom progress meter')],
          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progressbar')],
          [sg.Cancel()]]

# create the window`
window = sg.Window('Custom Progress Meter', layout)
progress_bar = window['progressbar']
# loop that would normally do something useful
for i in range(1000):
    # check to see if the cancel button was clicked and exit loop if clicked
    event, values = window.read(timeout=10)
    if event == 'Cancel'  or event == sg.WIN_CLOSED:
        break
  # update bar with loop value +1 so that bar eventually reaches the maximum
    progress_bar.UpdateBar(i + 1)
# done with loop... need to destroy the window as it's still open
window.close()
```

![progress custom](https://user-images.githubusercontent.com/13696193/45243969-c3508100-b2c3-11e8-82bc-927d0307e093.jpg)



## Output Element

The Output Element is a re-direction of Stdout.

If you are looking for a way to quickly add the ability to show scrolling text within your window, then adding an `Output` Element is about as quick and easy as it gets.

**Anything "printed" will be displayed in this element.**  This is the "trivial" way to show scrolling text in your window.  It's as easy as dropping an Output Element into your window and then calling print as much as you want.  The user will see a scrolling area of text inside their window.

***IMPORTANT***  You will NOT see what you `print` until you call either `window.read` or `window.Refresh`.  If you want to immediately see what was printed, call `window.Refresh()` immediately after your print statement.


```python
Output(size=(80,20))
```

![output](https://user-images.githubusercontent.com/13696193/44959863-b72f8280-aec3-11e8-8caa-7bc743149953.jpg)

----


Here's a complete solution for a chat-window using an Output Element.  To display data that's received, you would to simply "print" it and it will show up in the output area.  You'll find this technique used in several Demo Programs including the HowDoI application.

```python
import PySimpleGUI as sg

def ChatBot():
    layout = [[(sg.Text('This is where standard out is being routed', size=[40, 1]))],
              [sg.Output(size=(80, 20))],
              [sg.Multiline(size=(70, 5), enter_submits=True),
               sg.Button('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
               sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

    window = sg.Window('Chat Window', layout, default_element_size=(30, 2))

    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
    while True:
        event, value = window.read()
        if event == 'SEND':
            print(value)
        else:
            break
    window.close()
ChatBot()
```


## Column Element & Frame, Tab "Container" Elements

Columns and Frames and Tabs are all "Container Elements" and behave similarly.  This section focuses on Columns but can be applied elsewhere.

Starting in version 2.9 you'll be able to do more complex layouts by using the Column Element.  Think of a Column as a window within a window.  And, yes, you can have a Column within a Column if you want.

Columns are specified, like all "container elements", in exactly the same way as a window, as a list of lists.

Columns are needed when you want to specify more than 1 element in a single row.

For example, this layout has a single slider element that spans several rows followed by 7 `Text` and `Input` elements on the same row.

![column](https://user-images.githubusercontent.com/13696193/44959988-66b92480-aec5-11e8-9c26-316ed24a68c0.jpg)

Without a Column Element you can't create a layout like this.  But with it, you should be able to closely match any layout created using tkinter only.

```python

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

window = sg.Window('Compact 1-line window with column', layout)
event, values = window.read()
window.close()

sg.Popup(event, values, line_width=200)

```


## Columns As a Way to Modify Elements

Sometimes Columns are used to contain a single elemnet, but to give that elemously it was difficult to do these kinds of layouts, if not impossible.

justify the `Column` element's row by setting the `Column`'s `justification` parameter.

You can also justify the entire contents within a `Column` by using the Column's `element_justification` parameter.

With these parameter's it is possible to create windows that have their contents centered.  Previously this was very difficult to do.

This is currently only available in the primary PySimpleGUI port.




They can also be used to justify a group of elements in a particular way.

Placing `Column` elements inside `Columns` elements make it possible to create a multitude of




## Sizer Element

New in 4.3 is the `Sizer` Element.  This element is used to help create a container of a particular size.  It can be placed inside of these PySimpleGUI items:

* Column
* Frame
* Tab
* Window

The implementation of a `Sizer` is quite simple.  It returns an empty `Column` element that has a pad value set to the values passed into the `Sizer`.  Thus isn't not a class but rather a "Shortcut function" similar to the pre-defined Buttons.

This feature is only available in the tkinter port of PySimpleGUI at the moment.  A cross port is needed.


----

## Frame Element (Labelled Frames, Frames with a title)

Frames work exactly the same way as Columns.  You create layout that is then used to initialize the Frame.  Like a Column element, it's a "Container Element" that holds one or more elements inside.


![frame element](https://user-images.githubusercontent.com/13696193/45889173-c2245700-bd8d-11e8-8f73-1e5f1be3ddb1.jpg)

Notice how the Frame layout looks identical to a window layout. A window works exactly the same way as a Column and a Frame.  They all are "container elements" - elements that contain other elements.

*These container Elements can be nested as deep as you want.* That's a pretty spiffy feature, right?  Took a lot of work so be appreciative.  Recursive code isn't trivial.



This code creates a window with a Frame and 2 buttons.

```python
frame_layout = [
                  [sg.T('Text inside of a frame')],
                  [sg.CB('Check 1'), sg.CB('Check 2')],
               ]
layout = [
          [sg.Frame('My Frame Title', frame_layout, font='Any 12', title_color='blue')],
          [sg.Submit(), sg.Cancel()]
         ]

window = sg.Window('Frame with buttons', layout, font=("Helvetica", 12))
```



## Canvas Element

In my opinion, the tkinter Canvas Widget is the most powerful of the tkinter widget.  While I try my best to completely isolate the user from anything that is tkinter related, the Canvas Element is the one exception.  It enables integration with a number of other packages, often with spectacular results.

However, there's another way to get that power and that's through the Graph Element, an even MORE powerful Element as it uses a Canvas that you can directly access if needed.  The Graph Element has a large number of drawing methods that the Canvas Element does not have.  Plus, if you need to, you can access the Graph Element's "Canvas" through a member variable.

### Matplotlib, Pyplot Integration

**NOTE - The newest version of Matplotlib (3.1.0) no longer works with this technique. ** You must install 3.0.3 in order to use the Demo Matplotlib programs provided in the Demo Programs section.

One such integration is with Matplotlib and Pyplot.  There is a Demo program written that you can use as a design pattern to get an understanding of how to use the Canvas Widget once you get it.

    def Canvas(canvas - a tkinter canvasf if you created one. Normally not set
             background_color - canvas color
             size - size in pixels
             pad - element padding for packing
             key - key used to lookup element
             tooltip - tooltip text)

The order of operations to obtain a tkinter Canvas Widget is:
```python

    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    # define the window layout
    layout = [[sg.Text('Plot test')],
              [sg.Canvas(size=(figure_w, figure_h), key='canvas')],
              [sg.OK(pad=((figure_w / 2, 0), 3), size=(4, 2))]]

    # create the window and show it without the plot
    window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI', layout).Finalize()


    # add the plot to the window
    fig_photo = draw_figure(window['canvas'].TKCanvas, fig)

    # show it all again and get buttons
    event, values = window.read()
```


To get a tkinter Canvas Widget from PySimpleGUI, follow these steps:
* Add Canvas Element to your window
* Layout your window
* Call `window.Finalize()` - this is a critical step you must not forget
* Find the Canvas Element by looking up using key
* Your Canvas Widget Object will be the found_element.TKCanvas
* Draw on your canvas to your heart's content
* Call `window.read()` - Nothing will appear on your canvas until you call Read

See `Demo_Matplotlib.py` for a Recipe you can copy.


### Methods & Properties

TKCanvas - not a method but a property. Returns the tkinter Canvas Widget


## Graph Element

All you math fans will enjoy this Element... and all you non-math fans will enjoy it even more.

I've found nothing to be less fun than dealing with a graphic's coordinate system from a GUI Framework.  It's always upside down from what I want.  (0,0) is in the upper left hand corner.... sometimes... or was it in the lower left?  In short, it's a **pain in the ass**.

How about the ability to get your own location of (0,0) and then using those coordinates instead of what tkinter provides?  This results in a very powerful capability - working in your own units, and then displaying them in an area defined in pixels.

If you've ever been frustrated with where (0,0) is located on some surface you draw on, then fear not, your frustration ends right here.  You get to draw using whatever coordinate system you want.  Place (0,0) anywhere you want, including not anywhere on your Graph.  You could define a Graph that's all negative numbers between -2.1 and -3.5 in the X axis and -3 to -8.2 in the Y axis

There are 3 values you'll need to supply the Graph Element.  They are:

- Size of the canvas in pixels
- The lower left (x,y) coordinate of your coordinate system
- The upper right (x,y) coordinate of your coordinate system

After you supply those values you can scribble all of over your graph by creating Graph Figures.  Graph Figures are created, and a Figure ID is obtained by calling:

- DrawCircle
- DrawLine
- DrawPoint
- DrawRectangle
- DrawOval
- DrawImage

You can move your figures around on the canvas by supplying the Figure ID the **x,y delta** to move.  It does not move to an absolute position, but rather an offset from where the figure is now.  (Use Relocate to move to a specific location)

    graph.MoveFigure(my_circle, 10, 10)

You'll also use this ID to delete individual figures you've drawn:
```python
graph.DeleteFigure(my_circle)
```

### Mouse Events Inside Graph Elements

If you have enabled events for your Graph Element, then you can receive mouse click events.  If you additionally enable `drag_submits` in  your creation of the Graph Element, then you will also get events when you "DRAG" inside of a window.  A "Drag" is defined as a left button down and then the mouse is moved.

When a drag event happens, the event will be the Graph Element's key.  The `value` returned in the values dictionary is a tuple of the (x,y) location of the mouse currently.

This means you'll get a "stream" of events.  If the mouse moves, you'll get at LEAST 1 and likely a lot more than 1 event.

### Mouse Up Event for Drags

When you've got `drag_submits` enabled, there's a sticky situation that arises.... what happens when you're done dragging and you've let go of the mouse button?  How is the "Mouse Up" event relayed back to your code.

The "Mouse Up" will generate an event to you with the value:  `Graph_key` + `'+UP'`.  Thus, if your Graph Element has a key of `'_GRAPH_'`, then the event you will receive when the mouse button is released is:   `'_GRAPH_+UP'`

Yea, it's a little weird, but it works.  It's SIMPLE too.  I recommend using the `.startswith` and `.endswith` built-ins when dealing with these kinds of string values.

Here is an example of the `events` and the `values dictionary` that was generated by clicking and dragging inside of a Graph Element with the key == 'graph':

```
graph {'graph': (159, 256)}
graph {'graph': (157, 256)}
graph {'graph': (157, 256)}
graph {'graph': (157, 254)}
graph {'graph': (157, 254)}
graph {'graph': (154, 254)}
graph {'graph': (154, 254)}
graph+UP {'graph': (154, 254)}
```



## Table Element

Table and Tree Elements are of the most complex in PySimpleGUI.  They have a lot of options and a lot of unusual characteristics.

### `window.read()` return values from Table Element

The values returned from a `Window.read` call for the Table Element are a list of row numbers that are currently highlighted.

### The Qt `Table.Get()` call

New in **PySimpleGUIQt** is the addition of the `Table` method `Get`.  This method returns the table that is currently being shown in the GUI.  This method was required in order to obtain any edits the user may have made to the table.

For the tkinter port, it will return the same values that was passed in when the table was created because tkinter Tables cannot be modified by the user (please file an Issue if you know a way).


### Known `Table` visualization problem....

There has been an elusive problem where clicking on or near the table's header caused tkinter to go crazy and resize the columns continuously as you moved the mouse.

This problem has existed since the first release of the `Table` element.  It was fixed in release 4.3.

### Known table colors in Python 3.7.3, 3.7.4, 3.8, ?

The tkinter that's been released in the past several releases of Python has a bug.  Table colors of all types are not working, at all.  The background of the rows never change.  If that's important to you, you'll need to **downgrade** your Python version.  3.6 works really well with PySimpleGUI and tkinter.

### Empty Tables

If you wish to start your table as being an empty one, you will need to specify an empty table.  This list comprehension will create an empty table with 15 rows and 6 columns.

```python
data = [['' for row in range(15)]for col in range(6)]
```

### Events from Tables

There are two ways to get events generated from Table Element.
`change_submits` event generated as soon as a row is clicked on
`bind_return_key` event generate when a row is double clicked or the return key is press while on a row.

## Tree Element

The Tree Element and Table Element are close cousins.   Many of the parameters found in the Table Element apply to Tree Elements.  In particular the heading information, column widths, etc..


Unlike Tables there is no standard format for trees.  Thus the data structure passed to the Tree Element must be constructed.  This is done using the TreeData class.  The process is as follows:

- Get a TreeData Object
- "Insert" data into the tree
- Pass the filled in TreeData object to Tree Element

#### TreeData format
```python
def TreeData()
def Insert(self, parent, key, text, values, icon=None)
```

To "insert" data into the tree the TreeData method Insert is called.

```python
Insert(parent_key, key, display_text, values)
```

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

Tabs are another of PySimpleGUI "Container Elements".  It is capable of "containing" a layout just as a window contains a layout.  Other container elements include the `Column` and `Frame` elements.

Just like windows and the other container elements, the `Tab` Element has a layout consisting of any desired combination of Elements in any desired layouts.  You can have Tabs inside of Tabs inside of Columns inside of Windows, etc..

`Tab` layouts look exactly like Window layouts, that is they are **a list of lists of Elements**.

*How you place a Tab element into a window is different than all other elements.*  You cannot place a Tab directly into a Window's layout.

Also, tabs cannot be made invisible at this time.  They have a visibility parameter but calling update will not change it.

Tabs are contained in TabGroups.  They are **not** placed into other layouts.  To get a Tab into your window, first place the `Tab` Element into a `TabGroup` Element and then place the `TabGroup` Element into the Window layout.

Let's look at this Window as an example:

![tabbed 1](https://user-images.githubusercontent.com/13696193/45992808-b10f6a80-c059-11e8-9746-ac71afd4d3d6.jpg)

View of second tab:

![tabbed 2](https://user-images.githubusercontent.com/13696193/45992809-b10f6a80-c059-11e8-94e6-3bf543c9b0bd.jpg)



```python
tab1_layout =  [[sg.T('This is inside tab 1')]]

tab2_layout = [[sg.T('This is inside tab 2')],
               [sg.In(key='in')]]

```
The layout for the entire window looks like this:

```python
layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout)]])],
              [sg.Button('Read')]]
```

The Window layout has the TabGroup and within the tab Group are the two Tab elements.

One important thing to notice about all of these container Elements and Windows layouts... they all take a "list of lists" as the layout.  They all have a layout that looks like this `[[   ]]`

You will want to keep this `[[ ]]` construct in your head a you're debugging your tabbed windows.  It's easy to overlook one or two necessary ['s

As mentioned earlier, the old-style Tabs were limited to being at the Window-level only.  In other words, the tabs were equal in size to the entire window.  This is not the case with the "new-style" tabs.  This is why you're not going to be upset when you discover your old code no longer works with the new PySimpleGUI release.  It'll be worth the few moments it'll take to convert your code.

Check out what's possible with the NEW Tabs!

![tabs tabs tabs](https://user-images.githubusercontent.com/13696193/45993438-fd0fde80-c05c-11e8-9ed0-742f14d3070f.jpg)

Check out Tabs 7 and 8.  We've got a Window with a Column containing Tabs 5 and 6.  On Tab 6 are... Tabs 7 and 8.

As of Release 3.8.0, not all of *options* shown in the API definitions of the Tab and TabGroup Elements are working. They are there as placeholders.


First we have the Tab layout definitions. They mirror what you see in the screen shots.  Tab 1 has 1 Text Element in it.  Tab 2 has a Text and an Input Element.


### Reading Tab Groups

Tab Groups now return a value when a Read returns.  They return which tab is currently selected.  There is also a `enable_events` parameter that can be set that causes a Read to return if a Tab in that group is selected / changed.  The key or title belonging to the Tab that was switched to will be returned as the value




x## Pane Element

New in version 3.20 is the Pane Element, a super-cool tkinter feature.  You won't find this one in PySimpleGUIQt, only PySimpleGUI.   It's difficult to describe one of these things.  Think of them as "Tabs without labels" that you can slide.


![pane3](https://user-images.githubusercontent.com/13696193/50035040-fcd50e80-ffcd-11e8-939c-df8ab8d64712.gif)


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


While you can do it on an element by element or window level basis, the easier way is to use either the `theme` calls or `set_options`.  These calls will set colors for all window that are created.

Be aware that once you change these options they are changed for the rest of your program's execution.  All of your windows will have that Theme, until you change it to something else.

This call sets a number of the different color options.

```python
SetOptions(background_color='#9FB8AD',
       text_element_background_color='#9FB8AD',
       element_background_color='#9FB8AD',
       scrollbar_color=None,
       input_elements_background_color='#F7F3EC',
       progress_meter_color = ('green', 'blue')
       button_color=('white','#475841'))
```

# SystemTray


In addition to running normal windows, it's now also possible to have an icon down in the system tray that you can read to get menu events.  There is a new SystemTray object that is used much like a Window object.  You first get one, then you perform Reads in order to get events.

## Tkinter version

While only PySimpleGUIQt and PySimpleGUIWx offer a true "system tray" feature, there is a simulated system tray feature that became available in 2020 for the tkinter version of PySimpleGUI.  All of the same objects and method calls are the same and the effect is very similar to what you see with the Wx and Qt versions.  The icon is placed in the bottom right corner of the window.  Setting the location of it has not yet been exposed, but you can drag it to another location on your screen.

The idea of supporting Wx, Qt, and tkinter with the exact same source code is very appealing and is one of the reasons a tkinter version was developed.  You can switch frameworks by simply changing your import statement to any of those 3 ports.

The balloons shown for the tkinter version is different than the message balloons shown by real system tray icons.  Instead a nice semi-transparent window is shown.  This window will fade in / out and is the same design as the one found in the [ptoaster package](https://github.com/PySimpleGUI/ptoaster).

## SystemTray Object

Here is the definition of the SystemTray object.

```python
SystemTray(menu=None, filename=None, data=None, data_base64=None, tooltip=None,  metadata=None):
        '''
 SystemTray - create an icon in the system tray
 :param menu: Menu definition
 :param filename: filename for icon
 :param data: in-ram image for icon
 :param data_base64: basee-64 data for icon
 :param tooltip: tooltip string
 :param metadata: (Any) User metadata that can be set to ANYTHING
'''
```

You'll notice that there are 3 different ways to specify the icon image.  The base-64 parameter allows you to define a variable in your .py code that is the encoded image so that you do not need any additional files.  Very handy feature.

## System Tray Design Pattern

Here is a design pattern you can use to get a jump-start.

This program will create a system tray icon and perform a blocking Read.  If the item "Open" is chosen from the system tray, then a popup is shown.

The same code can be executed on any of the Desktop versions of PySimpleGUI (tkinter, Qt, WxPython)
```python
import PySimpleGUIQt as sg
# import PySimpleGUIWx as sg
# import PySimpleGUI as sg

menu_def = ['BLANK', ['&Open', '---', '&Save', ['1', '2', ['a', 'b']], '&Properties', 'E&xit']]

tray = sg.SystemTray(menu=menu_def, filename=r'default_icon.ico')

while True:  # The event loop
    menu_item = tray.read()
    print(menu_item)
    if menu_item == 'Exit':
        break
    elif menu_item == 'Open':
        sg.popup('Menu item chosen', menu_item)

```
The design pattern creates an icon that will display this menu:
![snag-0293](https://user-images.githubusercontent.com/13696193/49057441-8bbfe980-f1cd-11e8-93e7-1aeda9ccd173.jpg)

### Icons for System Trays

System Tray Icons are in PNG & GIF format when running on PySimpleGUI (tkinter version).  PNG, GIF, and ICO formats will work for the Wx and Qt ports.

When specifying "icons", you can use 3 different formats.
* `filename`- filename
* `data_base64` - base64 byte string
* '`data` - in-ram bitmap or other "raw" image

You will find 3 parameters used to specify these 3 options on both the initialize statement and on the Update method.

For testing you may find using the built-in PySimpleGUI icon is a good place to start to make sure you've got everything coded correctly before bringing in outside image assets. It'll tell you quickly if you've got a problem with your icon file.  To run using the default icon, use something like this to create the System Tray:

```python
tray = sg.SystemTray(menu=menu_def, data_base64=sg.DEFAULT_BASE64_ICON)
```


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


<!-- ```python
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
 -->

### Notify Class Method

In addition to being able to show messages via the system tray, the tkinter port has the added capability of being able to display the system tray messages without having a system tray object defined.  You can simply show a notification window.  This perhaps removes the need for using the ptoaster package?

The method is a "class method" which means you can call it directly without first creating an instanciation of the object.  To show a notification window, call `SystemTray.notify`.

This line of code

```python
sg.SystemTray.notify('Notification Title', 'This is the notification message')
```

Will show this window, fading it in and out:

![image](https://user-images.githubusercontent.com/46163555/74970862-2321e580-53ed-11ea-99ba-1581a05575f0.png)

This is a blocking call so expect it to take a few seconds if you're fading the window in and out.  There are options to control the fade, how long things are displayed, the alpha channel, etc..  See the call signature at the end of this document.


# Global Settings

There are multiple ways to customize PySimpleGUI.  You can think of customizations as being done in a hierarchical manner

 - Global
 - Window
 - Element

The function `set_options` is used to change settings that will apply globally.  If it's a setting that applies to Windows, then that setting will apply not only to Windows that you create, but also to popup Windows. 

Each lower level overrides the settings of the higher level.  Once settings have been changed, they remain changed for the duration of the program (unless changed again).

After Global settings are settings made at Window level.  These settings apply to a single `Window`.  Fonts are a good example of a Windows-level setting.  All elements within that `Window` will use the specified font.

The lowest level of setting is the element-level.  It will modify one particular element's setting.  Again using font as an example, if you set the `font` parameter on a `Text` element, then only that specific `Text` element will use the specified font.

# Persistent windows (Window stays open after button click)

Early versions of PySimpleGUI did not have a concept of "persisent window". Once a user clicked a button, the window would close.  After some time, the functionality was expanded so that windows remained open by default.


## Input Fields that Auto-clear
Note that `InputText` and `MultiLine` Elements can be **cleared** when performing a `read`.  If you want your input field to be cleared after a `window.read` then you can set the `do_not_clear` parameter to False when creating those elements. The clear is turned on and off on an element by element basis.

The reasoning behind this is that Persistent Windows are often "forms".  When "submitting" a form you want to have all of the fields left blank so the next entry of data will start with a fresh window.  Also, when implementing a "Chat Window" type of interface, after each read / send of the chat data, you want the input field cleared.  Think of it as a Texting application.  Would you want to have to clear your previous text if you want to send a second text?

## Basic Persistent Window Design Pattern

The design pattern for Persistent Windows was already shown to you earlier in the document... here it is for your convenience.

```python
import PySimpleGUI as sg

layout = [[sg.Text('Persistent window')],
          [sg.Input()],
          [sg.Button('Read'), sg.Exit()]]

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()
```


## read(timeout = t, timeout_key=TIMEOUT_KEY, close=False)

Read with a timeout is a very good thing for your GUIs to use in a non-blocking read situation.  If your device can wait for a little while, then use this kind of read.  The longer you're able to add to the timeout value, the less CPU time you'll be taking.

The idea to wait for some number of milliseconds before returning.  It's a trivial way to make a window that runs on a periodic basis.

One way of thinking of reads with timeouts:
> During the timeout time, you are "yielding" the processor to do other tasks.

But it gets better than just being a good citizen....**your GUI will be more responsive than if you used a non-blocking read**

Let's say you had a device that you want to "poll" every 100ms.   The "easy way out" and the only way out until recently was this:

```python
# YOU SHOULD NOT DO THIS....
while True:             # Event Loop
    event, values = window.ReadNonBlocking()   # DO NOT USE THIS CALL ANYMORE
    read_my_hardware() # process my device here
    time.sleep(.1)     # sleep 1/10 second  DO NOT PUT SLEEPS IN YOUR EVENT LOOP!
```

This program will quickly test for user input, then deal with the hardware.  Then it'll sleep for 100ms, while your gui is non-responsive, then it'll check in with your GUI again.

The better way using PySimpleGUI... using the Read Timeout mechanism, the sleep goes away.

```python
# This is the right way to poll for hardware
while True:             # Event Loop
    event, values = window.read(timeout = 100)
    read_my_hardware() # process my device here
```

This event loop will run every 100 ms.  You're making a `read` call, so anything that the use does will return back to you immediately, and you're waiting up to 100ms for the user to do something.  If the user doesn't do anything, then the read will timeout and execution will return to the program.


## sg.TIMEOUT_KEY

If you're using a read with a timeout value, then an event value of None signifies that the window was closed, just like a normal `window.read`.  That leaves the question of what it is set to when not other events are happening.  This value will be the value of `TIMEOUT_KEY`.  If you did not specify a timeout_key value in your call to read, then it will be set to a default value of:
`TIMEOUT_KEY = __timeout__`

If you wanted to test for "no event" in your loop, it would be written like this:
```python
while True:
    event, value = window.read(timeout=10)
    if event == sg.WIN_CLOSED:
        break # the use has closed the window
    if event == sg.TIMEOUT_KEY:
        print("Nothing happened")
```


Use async windows sparingly.  It's possible to have a window that appears to be async, but it is not.  **Please** try to find other methods before going to async windows.  The reason for this plea is that async windows poll tkinter over and over.  If you do not have a timeout in your Read and you've got nothing else your program will block on, then you will eat up 100% of the CPU time. It's important to be a good citizen.   Don't chew up CPU cycles needlessly.  Sometimes your mouse wants to move ya know?

### `read(timeout=0)`

You may find some PySimpleGUI programs that set the timeout value to zero.  This is a very dangerous thing to do.  If you do not pend on something else in your event loop, then your program will consume 100% of your CPU.  Remember that today's CPUs are multi-cored.  You may see only 7% of your CPU is busy when you're running with timeout of 0.  This is because task manager is reporting a system-wide CPU usage.  The single core your program is running on is likely at 100%.

A true non-blocking (timeout=0) read is generally reserved as a "last resort".  Too many times people use non-blocking reads when a blocking read will do just fine or a read with a timeout would work.

It's valid to use a timeout value of zero if you're in need of every bit of CPU horsepower in your application.  Maybe your loop is doing something super-CPU intensive and you can't afford for the GUI to use any CPU time. This is the kind of situation where a timeout of zero is appropriate.

Be a good computing citizen.  Run with a non-zero timeout so that other programs on your CPU will have time to run.

### Small Timeout Values (under 10ms)

***Do Not*** use a timeout of less than 10ms.  Otherwise you will simply thrash, spending your time trying to do some GUI stuff, only to be interrupted by a timeout timer before it can get anything done.  The results are potentially disasterous.



There is a hybrid approach... a read with a timeout.   You'll score much higher points on the impressive meter if you're able to use a lot less CPU time by using this type of read.

The most legit time to use a non-blocking window is when you're working directly with hardware.  Maybe you're driving a serial bus.  If you look at the Event Loop in the Demo_OpenCV_Webcam.py program, you'll see that the read is a non-blocking read.  However, there is a place in the event loop where blocking occurs.   The point in the loop where you will block is the call to read frames from the webcam.  When a frame is available you want to quickly deliver it to the output device, so you don't want your GUI blocking.  You want the read from the hardware to block.

Another example can be found in the demo for controlling a robot on a Raspberry Pi.  In that application you want to read the direction buttons, forward, backward, etc., and immediately take action.  If you are using RealtimeButtons, your only option at the moment is to use non-blocking windows.  You have to set the timeout to zero if you want the buttons to be real-time responsive.

However, with these buttons, adding a sleep to your event loop will at least give other processes time to execute.  It will, however, starve your GUI. The entire time you're sleeping, your GUI isn't executing.


### Periodically Calling`Read`

Let's say you do end up using non-blocking reads... then you've got some housekeeping to do.  It's up to you to periodically "refresh" the visible GUI.  The longer you wait between updates to your GUI the more sluggish your windows will feel.  It is up to you to make these calls or your GUI will freeze.

There are 2 methods of interacting with non-blocking windows.
1. Read the window just as you would a normal window
2. "Refresh" the window's values without reading the window. It's a quick operation meant to show the user the latest values

 With asynchronous windows the window is shown, user input is read, but your code keeps right on chugging.  YOUR responsibility is to call `PySimpleGUI.read` on a periodic basis.  Several times a second or more will produce a reasonably snappy GUI.

 ## Exiting (Closing) a Persistent Window

If your window has a special button that closes the window, then PySimpleGUI will automatically close the window for you.  If all of your buttons are normal `Button` elements, then it'll be up to you to close the window when done.

To close a window, call the `close` method.
```python
window.close()
```

Beginning in version 4.16.0 you can use a `close` parameter in the `window.read` call to indicate that the window should be closed before returning from the read.  This capability to an excellent way to make a single line Window to quickly get information.

This single line of code will display a window, get the user's input, close the window, and return the values as an event and a values dictionary.

```python
event, values = sg.Window('Login Window',
                  [[sg.T('Enter your Login ID'), sg.In(key='-ID-')],
                  [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)

login_id = values['-ID-']
```

You can also make a custom popup quite easily:

```python
long_string = '123456789 '* 40

event, values = sg.Window('This is my customn popup',
                  [[sg.Text(long_string, size=(40,None))],
                  [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)
```

Notice the height parameter of size is `None` in this case.  For the tkinter port of PySimpleGUI this will cause the number of rows to "fit" the contents of the string to be displayed.


## Persistent Window Example - Running timer that updates

See the sample code on the GitHub named Demo Media Player for another example of Async windows.  We're going to make a window and update one of the elements of that window every .01 seconds.    Here's the entire code to do that.

```python
import PySimpleGUI as sg
import time

# ----------------  Create Form  ----------------
sg.theme('Black')
sg.set_options(element_padding=(0, 0))

layout = [[sg.Text('')],
         [sg.Text(size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
         [sg.Button('Pause', key='button', button_color=('white', '#001480')),
          sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
          sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

window = sg.Window('Running Timer', layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True)

# ----------------  main loop  ----------------
current_time = 0
paused = False
start_time = int(round(time.time() * 100))
while (True):
    # --------- Read and update window --------
    event, values = window.read(timeout=10)
    current_time = int(round(time.time() * 100)) - start_time
    # --------- Display timer in window --------
    window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                  (current_time // 100) % 60,
                                                                  current_time % 100))
```


Previously this program was implemented using a sleep in the loop to control the clock tick.  This version uses the new timeout parameter.  The result is a window that reacts quicker then the one with the sleep and the accuracy is just as good.


## Instead of a Non-blocking Read --- Use `enable_events = True` or `return_keyboard_events = True`

Any time you are thinking "I want an X Element to cause a Y Element to do something", then you want to use the `enable_events` option.

***Instead of polling, try options that cause the window to return to you.***  By using non-blocking windows, you are *polling*.  You can indeed create your application by polling.  It will work.  But you're going to be maxing out your processor and may even take longer to react to an event than if you used another technique.

**Examples**

One example is you have an input field that changes as you press buttons on an on-screen keypad.

![keypad 3](https://user-images.githubusercontent.com/13696193/45260275-a2198e80-b3b0-11e8-85fe-a4ce6484510f.jpg)




# Updating Elements (changing element's values in an active window)

If you want to change an Element's settings in your window after the window has been created, then you will call the Element's Update method.

**NOTE** a window **must be Read or Finalized** before any Update calls can be made.  Also, not all settings available to you when you created the Element are available to you via its `update` method.

Here is an example of updating a Text Element

```python
import PySimpleGUI as sg

layout = [ [sg.Text('My layout', key='-TEXT-')],
           [sg.Button('Read')]]

window = sg.Window('My new window', layout)

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    window['-TEXT-'].update('My new text value')
```

Notice the placement of the Update call.  If you wanted to Update the Text Element *prior* to the Read call, outside of the event loop, then you must call Finalize on the window first.

In this example, the Update is done prior the Read.  Because of this, the Finalize call is added to the Window creation.
```python
import PySimpleGUI as sg

layout = [ [sg.Text('My layout', key='-TEXT-')],
           [sg.Button('Read')]]

window = sg.Window('My new window', layout, finalize=True)

window['-TEXT-'].update('My new text value')

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
```


Persistent windows remain open and thus continue to interact with the user after the Read has returned.  Often the program wishes to communicate results (output information) or change an Element's values (such as populating a List Element).

You can use Update to do things like:
* Have one Element (appear to) make a change to another Element
* Disable a button, slider, input field, etc.
* Change a button's text
* Change an Element's text or background color
* Add text to a scrolling output window
* Change the choices in a list
* etc.

The way this is done is via an Update method that is available for nearly all of the Elements.  Here is an example of a program that uses a persistent window that is updated.

![snap0272](https://user-images.githubusercontent.com/13696193/45260249-ec4e4000-b3af-11e8-853b-9b29d0bf7797.jpg)


In some programs these updates happen in response to another Element.  This program takes a Spinner and a Slider's input values and uses them to resize a Text Element.  The Spinner and Slider are on the left, the Text element being changed is on the right.


```python
# Testing async window, see if can have a slider
# that adjusts the size of text displayed

import PySimpleGUI as sg
fontSize = 12
layout = [[sg.Spin([sz for sz in range(6, 172)], font=('Helvetica 20'), initial_value=fontSize, change_submits=True, key='spin'),
           sg.Slider(range=(6,172), orientation='h', size=(10,20),
           change_submits=True, key='slider', font=('Helvetica 20')),
           sg.Text("Aa", size=(2, 1), font="Helvetica "  + str(fontSize), key='text')]]

sz = fontSize
window = sg.Window("Font size selector", layout, grab_anywhere=False)
# Event Loop
while True:
    event, values= window.read()
    if event == sg.WIN_CLOSED:
        break
    sz_spin = int(values['spin'])
    sz_slider = int(values['slider'])
    sz = sz_spin if sz_spin != fontSize else sz_slider
    if sz != fontSize:
        fontSize = sz
        font = "Helvetica "  + str(fontSize)
        window['text'].update(font=font)
        window['slider'].update(sz)
        window['spin'].update(sz)

print("Done.")
```


Inside the event loop we read the value of the Spinner and the Slider using those Elements' keys.
For example, `values['slider']` is the value of the Slider Element.

This program changes all 3 elements if either the Slider or the Spinner changes.  This is done with these statements:

```python
window['text'].update(font=font)
window['slider'].update(sz)
window['spin'].update(sz)
```

Remember this design pattern because you will use it OFTEN if you use persistent windows.

It works as follows.  The expression `window[key]` returns the Element object represented by the provided `key`.  This element is then updated by calling it's `update` method.  This is another example of Python's "chaining" feature. We could write this code using the long-form:

    text_element = window['text']
    text_element.update(font=font)

The takeaway from this exercise is that keys are key in PySimpleGUI's design.  They are used to both read the values of the window and also to identify elements.  As already mentioned, they are used in a wide variety of places.

### Locating Elements (FindElement == Element == Elem == [ ])

The Window method call that's used to find an element is:
`FindElement`
or the shortened version
`Element`
or even shorter (version 4.1+)
`Elem`

And now it's finally shortened down to:
window[key]

You'll find the pattern - `window.Element(key)` in older code.  All of code after about 4.0 uses the shortened `window[key]` notation.


### ProgressBar / Progress Meters

Note that to change a progress meter's progress, you call `update_bar`, not `update`.  A change to this is being considered for a future release.

# Cursors - Setting for Elements and Windows

It is possible to change the normal arrow cursor into something else by setting the cursor for an element or the entire window.  The result will be the cursor changing when you move the mouse over the elements or Window.

One of the best examples is URLs.  Users are accustomed to seeing a hand cursor when the mouse is moved over a link.  By setting the cursor to a hand for a Text element that has text that is in the format of a URL, it signals to the user that it's a link that can be clicked.

The `set_cursor` method is used to set the cursor for an element.  Perform an element look-up or use a variable containing an element, and call the `set_cursor` method, passing in a string that selects the cursor.  The valid cursor names are documented in the tkinter docs as this call maps directly to a tkinter call.

These cursor strings were obtained from the Tk manual and are what you pass into the `set_cursor` methods.

## Windows Level Cursor

You can also set the cursor for the Window as a whole, including the margins and areas elements don't directly fill.  Call `Window.set_cursor()` to set the cursor at the Window level.

## Valid Cursor Strings


```
X_cursor
arrow
based_arrow_down
based_arrow_up
boat
bogosity
bottom_left_corner
bottom_right_corner
bottom_side
bottom_tee
box_spiral
center_ptr
circle
clock
coffee_mug
cross
cross_reverse
crosshair
diamond_cross
dot
dotbox
double_arrow
draft_large
draft_small
draped_box
exchange
fleur
gobbler
gumby
hand1
hand2
heart
icon
iron_cross
left_ptr
left_side
left_tee
leftbutton
ll_angle
lr_angle
man
middlebutton
mouse
pencil
pirate
plus
question_arrow
right_ptr
right_side
right_tee
rightbutton
rtl_logo
sailboat
sb_down_arrow
sb_h_double_arrow
sb_left_arrow
sb_right_arrow
sb_up_arrow
sb_v_double_arrow
shuttle
sizing
spider
spraycan
star
target
tcross
top_left_arrow
top_left_corner
top_right_corner
top_side
top_tee
trek
ul_angle
umbrella
ur_angle
watch
xterm

```



## No Cursor

If you want your mouse cursor to be invisible, then use the **string** `"none"` and your element or window will not show any cursor.


## Windows OS Specific

One windows, these cursors map to native Windows cursors:

```
arrow
center_ptr
crosshair
fleur
ibeam
icon
sb_h_double_arrow
sb_v_double_arrow
watch
xterm
```

These are also available:

```
no
starting
size
size_ne_sw
size_ns
size_nw_se
size_we
uparrow
wait
```


## Mac OS Specific


```
arrow
cross
crosshair
ibeam
plus
watch
xterm
```


These additional native cursors are available for the Mac

```
copyarrow
aliasarrow
contextualmenuarrow
text
cross-hair
closedhand
openhand
pointinghand
resizeleft
resizeright
resizeleftright
resizeup
resizedown
resizeupdown
none
notallowed
poof
countinguphand
countingdownhand
countingupanddownhand
spinning
```


# Keyboard & Mouse Capture

NOTE - keyboard capture is currently formatted uniquely among the ports. For basic letters and numbers there is no great differences, but when you start adding Shift and Control or special keyus, they all behave slightly differently.  Your best bet is to simply print what is being returned to you to determine what the format for the particular port is.

Beginning in version 2.10 you can capture keyboard key presses and mouse scroll-wheel events.   Keyboard keys can be used, for example, to detect the page-up and page-down keys for a PDF viewer.  To use this feature, there's a boolean setting in the Window call `return_keyboard_events` that is set to True in order to get keys returned along with buttons.

Keys and scroll-wheel events are returned in exactly the same way as buttons.

For scroll-wheel events, if the mouse is scrolled up, then the `button` text will be `MouseWheel:Up`.   For downward scrolling, the text returned is `MouseWheel:Down`

Keyboard keys return 2 types of key events. For "normal" keys (a,b,c, etc.), a single character is returned that represents that key.  Modifier and special keys are returned as a string with 2 parts:

    Key Sym:Key Code

Key Sym is a string such as 'Control_L'.  The Key Code is a numeric representation of that key.  The left control key, when pressed will return the value 'Control_L:17'

```python
import PySimpleGUI as sg

# Recipe for getting keys, one at a time as they are released
# If want to use the space bar, then be sure and disable the "default focus"

text_elem = sg.Text(size=(18, 1))

layout = [[sg.Text("Press a key or scroll mouse")],
          [text_elem],
          [sg.Button("OK")]]

window = sg.Window("Keyboard Test", layout,  return_keyboard_events=True, use_default_focus=False)

# ---===--- Loop taking in user input --- #
while True:
    event, value = window.read()

    if event == "OK" or event == sg.WIN_CLOSED:
        print(event, "exiting")
        break
    text_elem.update(event)
```

You want to turn off the default focus so that there no buttons that will be selected should you press the spacebar.


# Menus

## MenuBar

Beginning in version 3.01 you can add a MenuBar to your window.  You specify the menus in much the same way as you do window layouts, with lists.  Menu selections are returned as events and as of 3.17, also as in the values dictionary.  The value returned will be the entire menu entry, including the key if you specified one.


```python
    menu_def = [['File', ['Open', 'Save', 'Exit',]],
                ['Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],
                ['Help', 'About...'],]
```

![menu](https://user-images.githubusercontent.com/13696193/45306723-56b7cb00-b4eb-11e8-8cbd-faef0c90f8b4.jpg)

Note the placement of ',' and of [].  It's tricky to get the nested menus correct that implement cascading menus.  See how paste has Special and Normal as a list after it.  This means that Paste has a cascading menu with items Special and Normal.

## Methods

---

To add a menu to a Window place the `Menu` or `MenuBar` element into your layout.

    layout = [[sg.Menu(menu_def)]]

It doesn't really matter where you place the Menu Element in your layout as it will always be located at the top of the window.

When the user selects an item, it's returns as the event (along with the menu item's key if one was specified in the menu definition)

## ButtonMenus

Button menus were introduced in version 3.21, having been previously released in PySimpleGUIQt.  They work exactly the same and are source code compatible between PySimpleGUI and PySimpleGUIQt.  These types of menus take a single menu entry where a Menu Bar takes a list of menu entries.

**Return values for ButtonMenus are different than Menu Bars.**

You will get back the ButtonMenu's KEY as the event.  To get the actual item selected, you will look it up in the values dictionary.  This can be done with the expression `values[event]`

## Right Click Menus

Right Click Menus were introduced in version 3.21.  Almost every element has a right_click_menu parameter and there is a window-level setting for rich click menu that will attach a right click menu to all elements in the window.

The menu definition is the same as the button menu definition, a single menu entry.

```python
right_click_menu = ['&Right', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]
```
The first string in a right click menu and a button menu is ***ignored***.  It is not used.  Normally you would put the string that is shown on the menu bar in that location.

**Return values for right click menus are the same as MenuBars.**  The value chosen is returned as the event.

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


## Disabled Menu Entries

If you want one of your menu items to be disabled, then place a '!' in front of the menu entry.  To disable the Paste menu entry in the previous examples, the entry would be:
`['!&Edit', ['Paste', ['Special', 'Normal',], 'Undo'],]`

If your want to change the disabled menu item flag / character from '!' to something else, change the variable `MENU_DISABLED_CHARACTER`

## Keys for Menus

Beginning in version 3.17 you can add a `key` to your menu entries.  The `key` value will be removed prior to be inserted into the menu.  When you receive Menu events, the entire menu entry, including the `key` is returned.  A key is indicated by adding `::` after a menu entry, followed by the key.

To add the `key` `_MY_KEY_` to the Special menu entry, the code would be:

`['&Edit', ['Paste', ['Special::_MY_KEY_', 'Normal',], 'Undo'],]`

 If you want to change the characters that indicate a key follows from '::' to something else, change the variable `MENU_KEY_SEPARATOR`


## The Menu Definitions

Having read through the Menu section, you may have noticed that the right click menu and the button menu have a format that is a little odd as there is a part of it that is not utilized (the first very string).  Perhaps the words "Not Used" should be in the examples.... But, there's a reason to retain words there that make sense.

The reason for this is an architectural one, but it also has a convienence for the user.  You can put the individual menu items (button and right click) into a list and you'll have a menu bar definition.

This would work to make a menu bar from a series of these individual menu defintions:

```python
menu_bar = [right_click_menu_1, right_click_menu_2, button_menu_def ]
```

And, of course, the direction works the opposite too.  You can take a Menu Bar definition and pull out an individual menu item to create a right click or button menu.



# TTK & TTK Scrollbars

In version 4.60.0 all of the scrollbars in PySimpleGUI were converted into TTK scrollbars.  This change enables all parts of a PySimpleGUI to match the theme.  Additionally, scrollbars can be ***further*** themed by changing the TTK Theme.

TTK Themes have been available for use in PySimpleGUI for years.  The `Window` object has a parameter to indicate which theme should be used for the window.  `set_options` has also been a way to set the theme for your application.

## TTK in Global Settings

A new third way to set the TTK theme was added in the 4.60.0 release, the PySimpleGUI Global Settings.  There is a tab dedicated to TTK in the global settings window.

![SNAG-1660](https://user-images.githubusercontent.com/46163555/167268144-b7a05b8d-6770-430a-ad92-96a10eae7d01.jpg)

## TTK Scrollbars

TTK Scrollbars are quite flexible in how they can be styled.  PySimpleGUI provides many options for these scrollbars.  Like much of PySimpleGUI, TTK Scrollbars have been simplified for you so that you are not required to set each and every option.  There is a trade-off, a payment, for the trivialization of features.  The simplification removes a few settings that are instead done on your behalf.  

All scrollbars in all elements of PySimpleGUI have been gray for 4 years and now you get not only that sweet sweet dull system-default-gray, but 1,000s of other colors ***and*** they match your PySimpleGUI theme's colors automagically.  

### "Test Scrollbar Settings"

In the Global PySimpleGUI Settings window, in the TTK tab, you'll find a button that will enable you to test/preview your settings.  When you click it, you will see the debug window open and some numbers printed so that the scrollbar changes over time.  If all PySimpleGUI defaults are used (including the PySimpleGUI theme), it will look something like this:

![SNAG-1661](https://user-images.githubusercontent.com/46163555/167268148-de075756-e585-450c-9b15-c4958629297e.jpg)


### Values of Scrollbar Settings

In the Global Settings window, you'll find this list of options for each of the TTK Scrollbar parts:
- Button Text Color
- Button Background Color
- Background Color
- Input Element Background Color
- Input Element Text Color
- Text Color
- Slider Color

![image](https://user-images.githubusercontent.com/46163555/167271981-059584f8-76ee-47b1-b3ed-7545e03bba8c.png)

These colors are from the **PySimpleGUI Theme colors**.  The term `Slider Color` means to use the color defined by the PySimpleGUI theme in use for the slider.  If the slider color is defined as "blue" in the theme, then selecting `Slider Color` will result in that part of the scrollbar being blue.

In addition to the items in the drop-down, you can type color values directly into the combo-box.  If you want your slider's trough color to be red, then you can type `red` into the setting in the settings window.  You can also use hex RGB colors, like `#FF0000` for pure red.


### Anatomy of a Scrollbar

This diagram shows the parts of a scrollbar that are discussed in the documentation and are in docstrings for parameters.  The only item not shown in the diagram is the "Frame Color".  It's left vague as it depends on which TTK Theme is chosen and it's a mash-up of multiple tkinter TTK Scrollbar parameters.  It's part of the magic-simplification mentioned above. Sticking with the default values almost always has great results.

![image](https://user-images.githubusercontent.com/46163555/167270106-9fd41032-dcc4-4867-bc8a-b4e5833b7767.png)

#### The "Thumb"

That bar in the middle that you grab in order to manually scroll quickly is sometimes called the "thumb".... so that's what I'll call it.

The question I'm sure many want to know is "how do I set just the color of the Thumb?"  I wanted to know that too!  The answer is... you can't.  It will be the same color as the background color of the buttons with the arrows. 

#### Background

The reason you see 2 lines coming out of the word "Background" in the diagram is that this color is used in 2 places.  That background setting is used to set both the thumb and the arrow background.

#### Trough

The trough is the "ditch" of the scrollbar.  The Thumb slides in the Trough. 

#### Button Arrow

The arrow color is the color of the arrow on the buttons located at the ends of the scrollbar.


#### Relief

The relief setting applies to the trough and the thumb, best I can tell.  It's most noticeable when you mouse over parts of the scrollbar.

#### Frame Width & Arrow Width

The Frame Width you can think of as the trough's width.  The Arrow Width is the width of the triangle.  It's possible to make some truly weird looking scrollbars by setting these 2 widths to be dramatically different.  This odd scrollbar has a Frame Width of 16 and an Arrow Width of 8.

![image](https://user-images.githubusercontent.com/46163555/167273502-0e5da5ec-3e65-41d5-8bee-3961458dc8da.png)
### Mouse-over Effects

The TTK Scrollbars in PySimpleGUI have a consistent mouse-over behavior.  When the mouse moves over the buttons or the thumb, the colors "swap".

"Swap" in this context means switching foreground and background colors.  The "Arrow Button Arrow Color" is the "foreground" and the "Background Color" is the "background".

These 2 examples show the effect 

The first example shows the mouse is over the top button of the scrollbar.  This button's colors have swapped the arrow color for the background color and vice versa.  See how the button at the top of the scrollbar is the "opposite" of the bottom button?

![image](https://user-images.githubusercontent.com/46163555/167273763-f6e8ff99-f83a-476d-bfab-d64f29942bbb.png)


In this second example, the mouse is over the thumb.  Normally the color of the thumb is the "background" color (i.e. the color of the arrow button's background). Thus, when the mouse is moved over it, the color will become the color of the ***arrow***.

![image](https://user-images.githubusercontent.com/46163555/167273751-87dee6db-4e23-4f0b-9de0-7ae2c0868d4c.png)

## Hierarchy of TTK Scrollbar Settings

Scrollbars have numerous places that they can be specified.  The order of priorities is determined based on whether or not a level has been set.  The order the settings are checked and thus the priority order is:

* Element
* Window
* set_options
* Global Settings

For example, if a `Multiline` element has the trough color for it's scrollbar defined in the layout, then that color will be used for that Multiline's scrollbar.  If no scrollbar settings are set for the element, then the settings for the Window the element is contained in.  Next the settings changed by a user's program calling the `set_options` function is used.  And finally, if none of those are set, then the Global Settings are used.

## Scrollbar Parameter Names

All functions and objects that have a scrollbar setting use the same names for the paramters:

* sbar_trough_color
* sbar_background_color
* sbar_arrow_color
* sbar_width
* sbar_arrow_width
* sbar_frame_color
* sbar_relief




# Running Multiple Windows

This is where PySimpleGUI continues to be simple, but the problem space just went into the realm of "Complex".

If you wish to run multiple windows in your event loop, then there are 2 methods for doing this.

1. First window does not remain active while second window is visible
2. First window remains active while second window is visible

You will find the 2 design matters in 2 demo programs in the Demo Program area of the GitHub (http://www.PySimpleGUI.com)

***Critically important***
When creating a new window you must use a "fresh" layout every time.  You cannot reuse a layout from a previous window.  As a result you will see the layout for window 2 being defined inside of the larger event loop.

If you have a window layout that you used with a window and you've closed the window, you cannot use the specific elements that were in that window.  You must RE-CREATE your `layout` variable every time you create a new window.  Read that phrase again....  You must RE-CREATE your `layout` variable every time you create a new window.  That means you should have a statemenat that begins with `layout = `.  Sorry to be stuck on this point, but so many people seem to have trouble following this simple instruction.

## THE GOLDEN RULE OF WINDOW LAYOUTS

***Thou shalt not re-use a windows's layout.... ever!***

Or more explicitly put....

> If you are calling `Window` then you should define your window layout in the statement just prior to the `Window` call.

## Demo Programs For Multiple Windows

There are several "Demo Programs" that will help you run multiple windows.  Please download these programs and FOLLOW the example they have created for you.

Here is ***some*** of the code patterns you'll find when looking through the demo programs.

## Multi-Window Design Pattern 1 - both windows active

```python
import PySimpleGUI as sg

# Design pattern 2 - First window remains active

layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)],
          [sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Button('Launch 2'), sg.Button('Exit')]]

win1 = sg.Window('Window 1', layout)

win2_active = False
while True:
    ev1, vals1 = win1.read(timeout=100)
    win1['-OUTPUT-'].update(vals1[0])
    if ev1 == sg.WIN_CLOSED or ev1 == 'Exit':
        break

     if not win2_active and ev1 == 'Launch 2':
        win2_active = True
        layout2 = [[sg.Text('Window 2')],
                   [sg.Button('Exit')]]

        win2 = sg.Window('Window 2', layout2)

    if win2_active:
        ev2, vals2 = win2.read(timeout=100)
        if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
            win2_active  = False
            win2.close()
```


## Multi-Window Design Pattern 2 - only 1 active window

```python
import PySimpleGUIQt as sg

# Design pattern 1 - First window does not remain active

layout = [[ sg.Text('Window 1'),],
          [sg.Input(do_not_clear=True)],
          [sg.Text(size=(15,1),  key='-OUTPUT-')],
          [sg.Button('Launch 2')]]

win1 = sg.Window('Window 1', layout)
win2_active=False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == sg.WIN_CLOSED:
        break
    win1.FindElement('-OUTPUT-').update(vals1[0])

    if ev1 == 'Launch 2'  and not win2_active:
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse
                   [sg.Button('Exit')]]

        win2 = sg.Window('Window 2', layout2)
        while True:
            ev2, vals2 = win2.read()
            if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
                win2.close()
                win2_active = False
                win1.UnHide()
                break
```


---


# The PySimpleGUI Debugger

Listen up if you are
* advanced programmers debugging some really hairy stuff
* programmers from another era that like to debug this way
* those that want to have "x-ray vision" into their code
* asked to use debugger to gather information
* running on a platform that lacks ANY debugger
* debugging a problem that happens only outside of a debugger environment
* finding yourself saying "but it works when running PyCharm"

Starting on June 1, 2019, a built-in version of the debugger `imwatchingyou` has been shipping in every copy of PySimpleGUI.  It's been largely downplayed to gauge whether or not the added code and the added feature and the use of a couple of keys, would mess up any users.  Over 30,000 users have installed PySimpleGUI since then and there's not be a single Issue filed nor comment/complaint made, so seems safe enough to normal users... so far....

So far no one has reported anything at all about the debugger.  The assumption is that it is quietly lying dormant, waiting for you to press the `BREAK` or `CONTROL` + `BREAK` keys.  It's odd no one has accidently done this and freaked out, logging an Issue.

The plain PySimpleGUI module has a debugger builtin.  For the other ports, please use the package `imwatchingyou`.


## What is it?  Why use it?  What the heck?  I already have an IDE.

This debugger provides you with something unique to most typical Python developers, the ability to "see" and interact with your code, **while it is running**.  You can change variable values while your code continues to run.

Print statements are cool, but perhaps you're tired of seeing a printout of `event` and `values`:
```
Push Me {0: 'Input here'}
Push Me {0: 'Input here'}
Push Me {0: 'Input here'}
```

And would prefer to see this window updating continuously in the upper right corner of your display:

![image](https://user-images.githubusercontent.com/13696193/62793751-54197900-baa0-11e9-9a98-f780259062b1.png)

Notice how easy it is, using this window alone, to get the location that your PySimpleGUI package is coming from ***for sure***, no guessing.  Expect this window to be in your debugging future as it'll get asked for from time to time.


## Preparing To Run the Debugger

If your program is running with blocking `Read` calls, then you will want to add a timeout to your reads.  This is because the debugger gets it's cycles by stealing a little bit of time from these async calls... but only when you have one of these debugger windows open so no bitching about wasted CPU time as there is none.

Your event loop will be modified from this blocking:
```python
while True:
    event, values = window.read()
```

To this non-blocking:
```python
while True:
    event, values = window.read(timeout=200)
    if event == sg.TIMEOUT_KEY:
        continue
```

These 3 lines will in no way change how your application looks and performs.  You can do this to any PySimpleGUI app that uses a blocking read and you'll not notice a difference.  The reason this is a NOP (No-operation) is that when a timeout happens, the envent will be set to `sg.TIMEOUT_KEY`.  If a timeout is returned as the event, the code simply ignores it and restarts the loop by executing a `continue` statement.

This timeout value of 200 means that your debugger GUI will be updated 5 times a second if nothing is happening.  If this adds too much "drag" to your application, you can make the timeout larger.  Try using 500 or 1000 instead of 100.

### What happens if you don't add a timeout

Let's say you're in a situation where a very intermettent bug has just happened and the debugger would really help you, but you don't have a timeout on your `windows.read()` call.  It's OK.  Recall that the way the debugger gets its "cycles" is to borrow from your `Read` calls.  What you need to do is alternate between using the debugger and then generating another pass through your event loop.

Maybe it's an OK button that will cause your loop to execute again (without exiting).  If so, you can use it to help move the debugger along.

Yes, this is a major pain in the ass, but it's not THAT bad and compared to nothing in a time of crisis and this is potentially your "savior tool" that's going to save your ass, pressing that OK button a few times is going to look like nothing to you.  You just want to dump out the value of a variable that holds an instance of your class!

## A Sample Program For Us To Use

Now that you understand how to add the debugger to your program, let's make a simple little program that you can use to follow these examples:

```python
import PySimpleGUI as sg

window = sg.Window('Testing the Debugger', [[sg.Text('Debugger Tester'), sg.In('Input here'), sg.B('Push Me')]])

while True:
    event, values = window.read(timeout=500)
    if event == sg.TIMEOUT_KEY:
        continue
    if event == sg.WIN_CLOSED:
        break
    print(event, values)
window.close()
```

## Debugger Windows


### "Popout Debugger Window"

There are 2 debugger windows. One is called the "Popout" debugger window.  The Popout window displays as many currently in-scope local variables as possible.  This window is not interactive.  It is meant to be a frequently updated "dashboard" or "snapshot" of your variables.

One "variable" shown in the popout window that is an often asked for piece of information when debugging Issues and that variable is `sg` (or whatever you named the PySimpleGUI pacakge when you did your import). The assumption is that your import is `import PySimpleGUI as sg`.  If your import is different, then you'll see a different variable.  The point is that it's shown here.

Exiting this window is done via the little red X, **or using the rickt-click menu** which is also used as one way to launch the Main Debugger Window

#### Ways of Launching the Popout Window

There are 3 ways of opening the Popout window.

1. Press the `BREAK` key on your keyboard.
2. Call the function `show_debugger_popout_window(location=(x,y))`
3. Add `Debug()` button to your layout - adds a little purple and yellow PySimpleGUI logo to your window


#### When you are asked for the "Location of your PySimpleGUI package or PySimpleGUI.py file" do this

If you wish to use the debugger to find the location of THIS running program's PySimpleGUI package / the PySimpleGUI.py file, then all you need to do is:
* Press the `BREAK` key on your keyboard.
    * This is sometimes labelled as the `Cancel` key
    * May also have `Pause` printed on key
    * On some US keyboards, it is located next to `Scroll Lock` and/or above `PageUp` key
* This will open a window located in the upper right corner of your screen that looks something like this:
![image](https://user-images.githubusercontent.com/13696193/62793751-54197900-baa0-11e9-9a98-f780259062b1.png)
* The information you are seeking is shown next to the `sg` in the window
You don't need to modify your program to get this info using this technique.

If your variable's value is too long and doesn't fit, then you'lll need to collect this information using the "Main Debugger Window"

#### What's NOT Listed In The Popout Debugger Window

The Popup window is a "Snapshot" of your local variables at the time the window was opened. This means **any variables that did not exist at the time the Popout was created will not be shown**.   This window does **NOT** expand in size by adding new variables.  Maybe in the future.


### The "Main Debugger Window"

Now we're talking serious Python debugging!

Ever wish you had a `repl>>>` prompt that you could run while your program is running.  Well, that's pretty much what you're getting with the PySimpleGUI debugger Main Window!  Cool, huh?  If you're not impressed, go get a cup of coffee and walk off that distraction in your head before carring on because we're in to some seriously cool shit here....

You'll find that this window has 2 tabs, one is labelled `Variables` and the other is labelled `REPL & Watches`

#### Ways of Opening the Main Debugger Window

There are 3 ways to open the Main Debugger Window

1. Press `Control` + `Break` on your PC keyboard
2. From the Popout Debug Window, right click and choose `Debugger` from the right click menu
3. From your code call `show_debugger_window(location=(x,y))`


#### The "Variables" Tab of Main Debugger Window

![SNAG-0440](https://user-images.githubusercontent.com/13696193/62797391-a01ceb80-baa9-11e9-845d-3cd02ca0dbcc.jpg)

Notice the the "frame" surrounding this window is labelled "Auto Watches" in blue.  Like the Popup window, this debugger window also "Watches" variables, which means continuously updates them as often as you call `Window.read`.

The maximum number of "watches" you can have any any one time is 9.

##### Choosing variables to watch

You can simply click "Show All Variable" button and the list of watched variables will be automatically populard by the first 9 variables it finds.  Or you can click the "Choose Variables to Auto Watch" button where you can individually choose what variables, **and expressions** you wish to display.

![SNAG-0442](https://user-images.githubusercontent.com/13696193/62797520-e96d3b00-baa9-11e9-8ba0-794e479b6fc5.jpg)


In this window we're checking checkboxes to display these variables:

`event`, `sg`, `values`, `window`, `__file__`

![SNAG-0443](https://user-images.githubusercontent.com/13696193/62797518-e8d4a480-baa9-11e9-8575-5256dcf6b5ab.jpg)

Additionally, you can see at the bottom of the window a "Custom Watch" has been defined.  This can be any experession you want.  Let's say you have a window with a LOT of values.  Rather than looking through the `values` variable and finding the entry with the key you are looking for, the values variable's entry for a specific key is displayed.

In this example the Custom Watch entered was `values[0]`.  After clicking on the "OK" button, indicating the variables are chosen that we wish to watch, this is the Main window that is shown:

![SNAG-0444](https://user-images.githubusercontent.com/13696193/62797514-e8d4a480-baa9-11e9-9a86-cfe99342dedb.jpg)

We can see the variables we checked as well as the defined expression `values[0]`.  If you leave this window open, these values with continuously be updated, on the fly, every time we call the line in our example code `window.read(timeout=500)`.  This means that the Main Debugger Window and these variables we defined will be updated every 500 milliseconds.



#### The REPL & Watches Tab

![SNAG-0441](https://user-images.githubusercontent.com/13696193/62797507-e7a37780-baa9-11e9-93c4-6ff0c8acb11d.jpg)


This tab is provided to you as a way to interact with your running program on a real-time basis.

If you want to quickly look at the values of variables, nearly ANY variables, then type the information into one of the 3 spaces provided to "Watch" either variables or experessions.  In this example, the variable window was typed into the first slow.

***Immediately*** after typing the character 'w', the information to the right was displayed.  No button needs to be clicked.  You merely need to type in a valid experession and it will be displayed to you.... and it will be displayed on an on-going, constantly-refreshing-basis.

![SNAG-0447](https://user-images.githubusercontent.com/13696193/62797393-a0b58200-baa9-11e9-8016-1cadca4d97e7.jpg)


If the area to the right of the input field is too small, then you can click on the "Detail" button and you will be shown a popup, scrolled window with all of the information displayed as if it were printed.

I'm sure you've had the lovely experience of printing an object.  When clicking the "Detail" button next to the `window` variable being shown, this window is shown:

![SNAG-0449](https://user-images.githubusercontent.com/13696193/62801423-b0d25f00-bab3-11e9-829a-aebb429521cd.jpg)

Oh, Python, -sigh-.  I just want to see my `window` object printed.

#### `Obj` Button to the Rescue!

PySimpleGUI has a fun and very useful function that is discussed in the docs named `ObjToString` which takes an object and converts it's **contents** it into a nicely formatted string.  This function is used to create the text output when you click the `Obj` button.  The result is this instead of the tiny window shown previously:

![SNAG-0446](https://user-images.githubusercontent.com/13696193/62797508-e7a37780-baa9-11e9-96bf-b2c066e72d78.jpg)


## The REPL Prompt

While not **really** a Python REPL prompt, this window's `REPL >>>` prompt is meant to act as much like one as possible.  Here you can enter experessions and code too.

The uses for this prompt are so numerous and diverse that listing them all won't be attempted.

### Your "XRay" and "Endoscope" into Your Program

Think of this prompt as a way to get specific diagnostics information about your ***running*** program.  It cannot be stressed enough that the power and the usefullness of this tool is in its ability to diagnose a running program, after you've already started it running.

### Execute Code

In addition to displaying information, getting paths to packages, finding version information, you can execute code from the PySimpleGUI Debugger's `REPL >>>` prompt.  You can type in any expression as well as any **executable statement**.

For example, want to see what `PopupError` looks like while you're running your program.  From the REPL prompt, type:
`sg.PopupError('This is an error popup')`

The result is that you are shown a popup window with the text you supplied.

### KNOW Answers to Questions About Your Program

Using this runtime tool, you can be confident in the data you collect.  Right?

***There's no better way to find what version of a package that your program is using than to ask your program.***  This is so true.  Think about it.  Rather than go into PyCharm, look at your project's "Virtual Environment", follow some path to get to a window that lists packages installed for that project, get the verstion and your're done, right?  Well, maybe.  But are you CERTAIN your program is using THAT version of the package in question?

SO MUCH time has been wasted in the past  when people KNEW, for sure, what version they were running. Or, they had NO CLUE what version, or no clue to find out.  There's nothing wrong with not knowing how to do something.  We ALL start there.  Geeez..

A real world example.....

## How To Use the Debugger to Find The Version Number of a Package

Let's pull together everything we've learned to now and use the debugger to solve a problem that happens often and sometimes it's not at all obvious how to find the answer.

We're using ***Matplotlib*** and want to find the "Version".

For this example, the little 12-line program in the section "A Sample Program For Us To Use" is being used.

That program does not import `matplotlib`.  We have a couple of choices, we can change the code, we can can import the package from the debugger.  Let's use the debgger.

Pull up the Main Debugger Window by pressing `CONTROL+BREAK` keys.  Then click the "REPL * Watches" tab.  At the `>>>` prompt we'll first import the package by typing:
`import matplotlib as m`

The result returned from Python calls that don't return anything is the value None.  You will see the command you entered in the output area followed by "None", indicating success.

finally, type:
`m.__version__`

The entire set of operations is shown in this window:

![SNAG-0448](https://user-images.githubusercontent.com/13696193/62797392-a0b58200-baa9-11e9-97f4-9ef74cbb86f7.jpg)

By convention you'll find many modules have a variable `__version__` that has the package's version number.  PySimpleGUI has one.  As you can see matplotlib has one.  The `requests` module has this variable.

For maximum compatibility, PySimpleGUI not only uses `__version__`, but also has the version contained in another variable `version` which has the version number because in some situations the `__version__` is not available but the `version` variable is avaiable.

**It is recommended that you use the variable `version` to get the PySimpleGUI version** as it's so far been the most successful method.

tkinter, however does NOT.... of course.... follow this convention.  No, to get the tkinter version, you need to look at the variable:
`TkVersion`

Here's the output from the REPL in the debugger showing the tkinter version:

```
>>> import tkinter as t
None
>>> t.TkVersion
8.6
>>> t.__version__
Exception module 'tkinter' has no attribute '__version__'
```
---

# User Settings API

In release 4.30.0 there is a new set of API calls available to help with "user settings".  Think of user settings as a dictionary that is automatically written to your hard drive.  That's basically what it is.  

In release 4.50.0 support for INI files was added in addition to the existing JSON file format.

While using JSON or config files to save and load a settings dictionary isn't very difficult, it is still code you'll need to write if you want to save settings as part of your GUI.  Since having "settings" for a GUI based program isn't uncommon, it made sense to build this capability into PySimpleGUI.  Clearly you can still use your own method for saving settings, but if you're looking for a simple and easy way to do it, these calls are likely about as easy as it gets.

There have already been some demo programs written that use JSON files to store settings.  You can expect that this capability will begin to show up in more demos in the future since it's now part of PySimpleGUI.

User settings are stored in a Python dictionary which is saved to / loaded from disk.  Individual settings are thus keys into a dictionary.  **You do not need to explicitly read nor write the file**.  Changing any entry will cause the file to be saved.  Reading any entry will cause the file to be read if it hasn't already been read.

## Two Interfaces

There are 2 ways to access User Settings

1. User Settings function calls
2. The `UserSettings` class

They both offer the same basic operations.  The class interface has an added benefit of being able to access the individual settings using the same syntax as Python dictionary.

If you want to use INI files, then you'll need to use the object interface.

## List of Calls for Function Interface

|Function|Description|
| ---  | --- |
|user_settings|Returns settings as a dictionary|
|user_settings_delete_entry|Deletes a setting|
|user_settings_delete_filename|Deletes the settings file|
|user_settings_file_exists|Returns True if settings file specified exists|
|user_settings_filename|Returns full path and filename of current settings file|
|user_settings_get_entry|Returns value for a setting. If no setting found, then specified default value is returned|
|user_settings_load|Loads dictionary from the settings file. This is not normally needed||
|user_settings_save|Saves settings to current or newly specified file. Not normally needed|
|user_settings_set_entry|Sets an entry to a particular value
|user_settings_write_new_dictionary|Writes a specified dictionary to settings file|


## Operations

There are 2 categories that the calls can be divided into.

1. File operations
2. Settings operations

File operations involve working with the JSON file itself.  They include:
* Setting the path and/or filename
* Load/save the file (these are somewhat optional as the saving loading/saving is done automatically)
* Deleting the settings file
* Checking if settings file exists

Generally speaking, a setting is specified with a key which is generally a string.  Settings operations are for working with the individual settings and include:
* Get the value of a setting (returns a default value if not found)
* Set the value of a setting (also saves the settings to disk)

Any setting operation may cause the file to be written. This is because a "get" operation can include returning a default value if the setting isn't found.  This means a new entry is made in your settings dictionary is one didn't exist before.  Since a new entry is made, that means it needs to be also be written to disk.

## Filenames

The settings filename defaults the filename of your Python file making the call with the extension ".json" added.  If your Python program is called `test.py` then your default settings filename will be `test.json`.

In addition to the filename having a default value, the path to the file also has a default value.  The default depends on your operating system.

|Operating System|Default Path|
| ---  | --- |
| Windows | \user\user_name\AppData\Local\PySimpleGUI\settings |
| Linux | ~/.config/PySimpleGUI/settings |
| Mac | ~/Library/Application Support/PySimpleGUI/settings |

When calling the User Settings APIs, if a parameter is named `filename`, you can specify a full path or just the filename.  This will save you the trouble of having to split up your path and filename in your code.  If you specify only the path, the the filename will be added to that path and named as defined earlier.

Like the rest of PySimpleGUI, the idea is for you to write as little code as possible.  The default values for the filename and path should be fine for you to use.  They will be stored in a location on your system that is meant to store user settings.


### Setting Filename

If you want to see what the current filename is for your settings, then you can call `user_settings_filename()` with no parameters and you'll get back an absolute path and filename.

To make the code for specifying the folder and filename as simple as possible, the 2 parts are separated in the call specifying the name of the settings file.  However, it is possible to supply a full and complete folder + filename as well.

The default filename for your settings file is the name of the file that makes the call to the User Settings API's with the `.py` extension changed to a `.json` extension. If your source file is called `demo.py`,  then your settings filename will be `demo.json`.

#### Setting only the filename

If you want to control the name of the file and/or the path to the settings file, then you will use the `user_settings_filename` call.  This function takes 2 parameters.

```python
user_settings_filename(filename=None, path=None)
```

If you set only the path, then the filename will default to the value already described.  If you set only the filename, then the path will be the default path is dependent on your operating system.  See the table above for the locations for each OS.

```python
import PySimpleGUI as sg

sg.user_settings_filename(filename='my_settings.json')
print(sg.user_settings_filename())
```

If you are running on Windows, then the result of running this code will be this printed on the console:

```
C:\Users\your_use_name\AppData\Local\PySimpleGUI\settings\my_settings.json
```

You are not restricted to naming your settings file to an extension of .json.  That is simply the default extension that's used by PySimpleGUI.  You can use any extension you would like, including no extension.

#### Setting only the path

Maybe you don't care about the settings filename itself, but you do care about where the settings are stored.  Let's say you want the settings to be stored in the same folder as your Python source file.  Specifying `path='.'` will achieve this.


#### Setting a fully qualified filename

If you want to specify the full absolute path and filename of the settings file, you can do it by using the filename parameter.  Instead of passing the filename only, pass in a fully qualified path and filename.  If you want to name your settings file `a:\temp\my_settings`, then your call will look like this:


```python
sg.user_settings_filename(filename=r'a:\temp\my_settings')
```

You are not required to break your file down into 2 parameters.  You could if you wanted to however.  The equivalent to the above call using 2 parameters would be:

```python
sg.user_settings_filename(filename='my_settings' , path=r'a:\temp')
```


### Getting the current filename

Calling `user_settings_filename` with no parameters will return the full path and filename of your settings file as a single string.


### File Loading / Saving

Generally speaking you will not need to load or save your settings file.  It is automatically saved after every change.

Note that reading a setting can also cause the file to be written.  If you read a setting and the setting did not exist, then your call to `user_settings_get_entry` will return the default value you specified.  As a result, the dictionary is updated with this default value and in return the file is written with this value as well.

One of the situations where you may want to explicitly read/load the settings file is if you're expecting it to be modified by another program.

Like so much of PySimpleGUI, as much as possible is automatically done on your behalf.  This includes the requirement of saving and loading your settings file.  Even naming your settings file is optional.

## The `UserSettings` Class Interface

The `UserSettings` class makes working with settings look like a Python dictionary.  The familiar [ ] syntax is used to read, write and delete entries.

### Creating a `UserSettings` Object

The first step is to create your setting object.  The parameters are the same as calling the `user_settings_filename` function.  If you want to use the default values, then leave the parameters unchanged.

```python
settings = sg.UserSettings()
```

This is the same as calling `sg.user_settings_filename()`


### Reading, Writing, and Deleting an Individual Settings Using [ ] Syntax

The first operation will be to create the User Settings object.

```python
settings = sg.UserSettings()
```

To read a setting the dictionary-style [ ] syntax is used.  If the item's name is `'-item-'`, then reading the value is achieved by writing

```python
item_value = settings['-item-']
```

Writing the setting is the same syntax except the expression is reversed.

```python
settings['-item-'] = new_value
```

To delete an item, again the dictionary style syntax is used.

```python
del settings['-item-']
```

You can also call the delete_entry method to delete the entry.

```python
settings.delete_entry('-item-')
```

### `UserSettings` Methods

You'll find all of the `UserSettings` methods available to you detailed in the Call Reference documentation.

One operation in particular that is not achievable using the [ ] notation is a "get" operation with a default value.  For dictionaries, this method is `get` and for the `UserSettings` class the method is also called `get`.  They both have an optional second parameter that represents a "default value" should the key not be found in the dictionary.

If you would like a setting with key `'-item-'` to return an empty string `''` instead of `None` if they key isn't found, then you can use this code to achieve that:

```python
value = settings.get('-item-', '')
```

It's the same kind of syntax that you're used to using with dictionaries.


### Default Value

Normally the default value will be `None` if a key is not found and you get the value of the entry using the bracket format:

```python
item_value = settings['-item-']
```

You can change the default value by calling `settings.set_default_value(new_default)`.  This will set the default value to return in the case when no key is found.  Note that an exception is not raised when there is a key error (see next section on error handling).  Instead, the default value is returned with a warning displayed.


## Displaying the Settings Dictionary

The class interface makes it easy to dump out the dictionary.  If you print the UserSettings object you'll get a printout of the dictionary.

Note that you'll need to "load" the settings from disk if you haven't performed any operations on the settings.

```python
settings = sg.UserSettings()
settings.load()
print(settings)
```

If you were to print the dictionary after creating the object, then the `load` is not needed

```python
settings = sg.UserSettings()
print(settings['-item-'])
print(settings)
```

To print the dictionary using the function call interface:

```python
print(sg.user_settings())
```

## Error Handling for User Settings

From a GUI perspective, user settings are not critical to the GUI operations itself.  There is nothing about settings that will cause your window to not function.  As a result, errors that occur in the User Settings are "soft errors".  An error message is displayed along with information about how you called the function, when possible, and then execution continues.

One reason for treating these as soft errors and thus not raising an exception is that raising an exception will crash your GUI.  If you have redirected your output, which many GUIs do, then you will see no error information and your window will simply disappear.  If you double clicked a .py file to launch your GUI, both the GUI and the console window will instantly disappear if the GUI crashes, leaving you no information to help you debug the problem.

The only time errors can occur are during file operations.  Typically these errors happen because you've specified a bad path or you don't have write permission for the path you specified.

Example error message.  If you executed this code:

```python
def main():
    sg.user_settings_filename(path='...')
    sg.user_settings_set_entry('-test-',123)
```

Then you'll get an error when trying to set the '-test-' entry because `'...'` is not a valid path.

```
*** Error saving settings to file:***
 ...\scratch_1065.json [Errno 2] No such file or directory: '...\\scratch_1065.json'
The PySimpleGUI internal reporting function is save
The error originated from:
  File "C:/Users/mike/.PyCharmCE2019.1/config/scratches/scratch_1065.py"
line 8
in main
    sg.user_settings_set_entry('-test-',123)
```

You should be able to easily figure out these errors as they are file operations and the error messages are clear in detailing what's happened and where the call originated.

### Silencing the Errors

If you're the type that doesn't want to see any error messages printed out on your console, then you can silence the error output.

When using the class interface, there is a parameter `silent_on_error` that you can set to `True`.

For the function interface, call the function `user_settings_silent_on_error()` and set the parameter to `True`


## Config INI File Support

Using INI files has some advantages over JSON, particularly  when humans are going to be modifying the settings files directly.

To specify use of INI files instead of JSON, set the parameter `use_config_file=True` when creating your `UserSetting` object.

```python
settings = sg.UserSettings('my_config.ini', use_config_file=True, convert_bools_and_none=True)
```

Note the 2 parameters that are specific for .ini files:
* `use_config_file` - Set to `True` to indicate you're using an INI file
* `convert_bools_and_none` - Defaults to `True`. Normally all settings from INI files are strings. This parameter will convert 'True', 'False', and 'None' to Python values `True`, `False`, `None`

There is also an additional method added `delete_section` which will delete an entire section from your INI file.

### Example File

Let's use this as our example INI file:

```
[My Section]
filename = test1234
filename2 = number 2
filename3 = number 3

[Section 2]
var = 123

[Empty]

[last section]
bool = True
```


### Getting / Setting Entries

Just like the JSON files, you can access the individual settings using the UserSettings class by using the `[ ]` notation or by calling `get` and `set` methods.

The big difference with the INI file support is the addition of an extra lookup / parameter, the section name.

To access the entry `var` in section `Section 2`, you can use wither of these:

```python
settings['Section 2']['var']
settings['Section 2'].get('var', 'Default Value')
```


The advantage of using the `get` method is that if the entry is not present, a default value will be returned instead.

To set an entry, you also have 2 choices:

```python
settings['Section 2']['var'] = 'New Value'
settings['Section 2'].set('var', 'New Value')
```

### Accessing INI File Sections

Once you have created your `UserSettings` object, then you'll be accessing entries using 2 keys instead of 1 like JSON uses.


To access an entire section, you'll write:

`settings['section']`

To get all of 'My Section' it will be:

`settings['My Section']` which returns a section object that behaves much like a dictionary.

To access a value within a section, add on one more lookup.  To get the value of the `filename` setting in the `My Section` section, it's done with this code:

`settings['My Section']['filename']`

### Deleting Entries

To delete an individual entry, you can use several different techniques.  One is to use `del`

```python
del settings['My Section1']['test']
```

This deletes the setting `test` in the section `My Section1`

You can also do this by calling the `delete_entry` method

```python
settings.delete_entry(section='My Section1', key='test')
```


### Deleting Sections

If you want to delete an entire section, you have 2 methods for doing this.  One is to call the method `UserSettings.delete_section` and pass in the name of the section to be deleted.

```python
settings.delete_section(section='My Section1')
```

The other is to lookup the section and then call `delete_section` on that section.

```python
settings['My Section1'].delete_section()
```


### Printing Settings for INI Files

If you print (or cast to a string) a section or a UserSettings object for an INI file, then you will get a nicely formated output that shows the sections and what settings are in each section.

Going back to the example INI file from earlier.  Printing the UserSettings object for this file produces this output:

```
My Section:
          filename : test1234
          filename2 : number 2
          filename3 : number 3
Section 2:
          var : 123
Empty:
last section:
          bool : True
```


### INI File Comments (WARNING)

If you have created an INI file using a test editor or it was created output of Python, then when the file is written, your comments will be stripped out.  Code is being added to PySimpleGUI to merge back your comments, but the code isn't done yet.   You'll either live with this limitation for now or write your own merge code.

Yea, I know, it's a bummer, but the plan is to overcome this Python limitation.

## Coding Convention for User Settings Keys

The User Settings prompted a new coding convention that's been added to PySimpleGUI examples.  As you're likely aware, keys in layouts have the format `'-KEY-`'.  For UserSettings, a similar format is used, but instead of the string being in all upper case, the characters are lower case.  In the example below, the user setting for "filename" has a User Setting key of `'-filename-'`.  Coding conventions are a good thing to have in your projects.  You don't have to follow this one of course, but you're urged to create your own for places in your code that it makes sense.  You could say that PEP8 is one giant coding convention for the Python language as a whole.  You don't have to follow it, but most Python programmers do.  We follow it "by convention".

The reason this is done in PySimpleGUI is so that the keys are immediately recognizable.  Perhaps your application has dictionaries that you use.  If you follow the PySimpleGUI coding convention of Element keys have the format `'-KEY-'` and User Settings keys have the format of `'-key-'`, then you'll immediately understand what a specific key is used for.  Your company may have its own coding conventions so follow those if appropriate instead of what you see in the PySimpleGUI examples.

## Example User Settings Usage

One of the primary places settings are likely to be used is for filenames / folder names.  How many times have you run the same program and needed to enter the same filename?  Even if the name of the file is on your clipboard, it's still a pain in the ass to paste it into the input field every time you run the code.  Wouldn't it be so much simpler if your program remembered the last value you entered?  Well, that's exactly why this set of APIs was developed.... again it was from laziness that this capability gained life.

If you want your `Input` elements to default to an entry from your settings, then you simply set the first parameter (`default_text`) to the value of a setting from your settings file.

Let's say your layout had this typical file input row:

```python
[sg.Input(key='-IN-'), sg.FileBrowse()]
```

To automatically fill in the `Input` to be the last value entered, use this layout row:

```python
[sg.Input(sg.user_settings_get_entry('-filename-', ''), key='-IN-'), sg.FileBrowse()]
```

When your user clicks OK or closes the window in a way that is in a positive way (instead of cancelling), then add this statement to save the value.

```python
sg.user_settings_set_entry('-filename-', values['-IN-'])
```

Here's an entire program demonstrating this way of using user settings

![image](https://user-images.githubusercontent.com/46163555/96048583-cde78800-0e44-11eb-87fe-c2465e1b6cf8.png)

```python
import PySimpleGUI as sg

layout = [[sg.Text('Enter a filename:')],
          [sg.Input(sg.user_settings_get_entry('-filename-', ''), key='-IN-'), sg.FileBrowse()],
          [sg.B('Save'), sg.B('Exit Without Saving', key='Exit')]]

window = sg.Window('Filename Example', layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event == 'Save':
        sg.user_settings_set_entry('-filename-', values['-IN-'])

window.close()
```

In 2 lines of code you've just made life for your user so much easier.  And, by not specifying a location and name for your file, the settings are stored out of sight / out of mind.  If you wanted to have the settings be stored with your program file so that it's more visible, then add this statement before your layout:

```python
sg.user_settings_filename(path='.')
```

## Example Using UserSettings Class with [ ] Syntax

The same example can be written using the `UserSettings` class and the [ ] lookup syntax.

Here's the same program as above.

```python
import PySimpleGUI as sg

settings = sg.UserSettings()

layout = [[sg.Text('Enter a filename:')],
          [sg.Input(settings.get('-filename-', ''), key='-IN-'), sg.FileBrowse()],
          [sg.B('Save'), sg.B('Exit Without Saving', key='Exit')]]

window = sg.Window('Filename Example', layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, 'Exit'):
        break
    elif event == 'Save':
        settings['-filename-'] = values['-IN-']

window.close()
```

If you were to place these 2 examples in the same file so that one ran after the other, you will find that the same settings file is used and thus the value saved in the first example will be read by the second one.

There was one additional line of code added:

```python
settings.set_default_value('')      # Set the default not-found value to ''

```

Strictly speaking, this line isn't needed because the Input Element now takes `None` to be the same as a value of `''`, but to produce identical results I added this line of code.


## Demo Programs

There are a number of demo programs that show how to use UserSettings to create a richer experience for your users by remember the last value input into input elements or by adding a Combobox with a history of previously entered values.  These upgrades make for a much easier to use GUI, especially when you find yourself typing in the same values or using the same files/folders.


## Brief Caution - User Settings Stick Around

If you're using the default path, remember that previous runs of your file may have old settings that are still in your settings file.  It can get confusing when you've forgotten that you previously wrote a setting.  Not seeing the filename can have drawbacks like this.

Also, because the settings automatically save after every update, it can be easy to accidently overwrite a previously saved setting.  If you want to avoid this, then perhaps it's best that you work with a dictionary within your code and then explicitly save your dictionary when you're ready to commit it to disk.

To save your Python dictionary to a settings file, simply call `user_settings_write_new_dictionary(dict)`, passing in your dictionary as the parameter.


-------------------------


# Extending PySimpleGUI

PySimpleGUI doesn't and can't provide every single setting available in the underlying GUI framework.  Not all tkinter options are available for a `Text` Element.  Same with PySimpleGUIQt and the other ports.

There are a few of reasons for this.

1. Time & resource limits - The size of the PySimpleGUI development team is extremely small
2. PySimpleGUI provides a "Unified API".  This means the code is, in theory, portable across all of the PySimpleGUI ports without chaning the user's code (except for the import)
3. PySimpleGUI is meant, by design, to be simple and cover 80% of the GUI problems.

However, PySimpleGUI programs are ***not*** dead ends!!  Writing PySimpleGUI code and then getting to a point where you really really feel like you need to extend the Listbox to include the ability to change the "Selected" color.  Maybe that's super-critical to your project.  And maybe you find out late that the base PySimpleGUI code doesn't expose that tkinter capability.  Fear not!  The road does continue!!

## Widget Access

Most of the user extensions / enhancements are at the "Element" level.  You want some Element to do a trick that you cannot do using the existing PySimpleGUI APIs.  It's just not possible.  What to do?

What you need is access to the underlying GUI framework's "Widget".  The good news is that you HAVE that access ready and waiting for you, for all of the ports of PySimpleGUI, not just the tkinter one.

### `Element.Widget` is The GUI Widget

The class variable `Widget` contains the tkinter, Qt, WxPython, or Remi widget.  With that variable you can modify that widget directly.

***You must first `Read` or `Finalize` the window before accessing the `Widget` class variable***

The reason for the Finalize requirement is that until a Window is Read or is Finalized it is not actually created and populated with GUI Widgets.  The GUI Widgets are created when you do these 2 operations.

Side note - You can stop using the `.Finalize()` call added onto your window creation and instead use the `finalize` parameter in the `Window` call.

OLD WAY:
```python
window = sg.Window('Window Title', layout).Finalize()

```

THE NEW WAY:
```python
window = sg.Window('Window Title', layout, finalize=True)

```

It's cleaner and less confusing for beginners who aren't necessarily trained in how chaining calls work.  Py**Simple**GUI.


### Example Use of `Element.Widget`

So far there have been 2 uses of this capability.  One already mentioned is adding a new capability.  The other way it's been used has been to fix a bug or make a workaround for a quirky behavior.

A recent Issue posted was that focus was always being set on a button in a tab when you switch tabs in tkinter.  The user didn't want this to happen as it was putting an ugly black line around their nicely made graphical button.

There is no current way in PySimpleGUI to "disable focus" on an Element.  That's essentially what was needed, the ability to tell tkinter that this widget should never get focus.

There is a way to tell tkinter that a widget should not get focus.  The downside is that if you use your tab key to navigate, that element will never get focus.  So, it's not only blocking focus for this automatic problem, but blocking it for all uses.  Of course you can still click on the button.

The way through for this user was to modify the tkinter widget directly and tell it not to get focus.  This was done in a single line of code:

```python
window[button_key].Widget.config(takefocus=0)
```

The absolute beauty to this solution is that tkinter does NOT need to be imported into the user's program for this statement to run.  Python already know what kind of object `.Widget` is and can thus show you the various methods and class variables for that object.  Most all tkinter options are strings so you don't need to import tkinter to get any enums.

### Finding Your Element's Widget Type

Of course, in order to call the methods or access the object's class variables, you need to know the type of the underlying Widget being used.  This document could list them all, but the downside is the widget could change types (not a good thing for people using the .Widget already!).  It also saves space and time in getting this documentation published and available to you.

So, here's the way to get your element's widget's type:

```python
    print(type(window[your_element_key].Widget))
```

In the case of the button example above, what is printed is:

`<class 'tkinter.Button'>`

I don't think that could be any clearer.  Your job at this point is to look at the tkinter documentation to see what the methods are for the tkinter `Button` widget.

## Window Level Access

For this one you'll need some specific variables for the time being as there is no `Window` class variable that holds the window's representation in the GUI library being used.

For tkinter, at the moment, the window's root object is this:

```python
sg.Window.TKroot
```

The type will vary in PySimpleGUI.  It will either be:
`tkinter.Tk()`
`tkinter.Toplevel()`

Either way you'll access it using the same `Window` variable `sg.Window.TKroot`

Watch this space in the future for the more standardized variable name for this object.  It may be something like `Window.Widget` as the Elements use or something like `Window.GUIWindow`.


## Binding tkiner "events"

If you wish to receive events directly from tkinter, but do it in a PySimpleGUI way, then you can do that and get those events returned to you via your standard `Window.read()` call.

Both the Elements and Window objects have a method called `bind`. You specify 2 parameters to this function. One is the string that is used to tell tkinter what events to bind. The other is a "key modifier" for Elements and a "key" for Windows.

The `key_modifier` in the `Element.bind` call is something that is added to your key. If your key is a string, then this modifier will be appended to your key and the event will be a single string.

If your element's key is not a string, then a tuple will be returned as the event (your_key, key_modifier)

This will enable you to continue to use your weird, non-string keys. Just be aware that you'll be getting back a tuple instead of your key in these situations.

The best example of when this can happen is in a Minesweeper game where each button is already a tuple of the (x,y) position of the button. Normal left clicks will return (x,y). A right click that was generated as a result of bind call will be ((x,y), key_modifier).

It'll be tricky for the user to parse these events, but it's assumed you're an advanced user if you're using this capability and are also using non-string keys.

An Element member variable `user_bind_event` will contain information that tkinter passed back along with the event. It's not required for most operations and none of the demos currently use this variable, but it's there just in case. The contents of the variable are tkinter specific and set by tkinter so you'll be digging into the tkinter docs if you're using an obscure binding of some kind.

tkinter events must be in between angle brackets

```python
window['-KEY-'].bind('<TKINTER EVENT>', 'STRING TO APPEND')
```

Events can also be binded to the window
```python
window.bind('<TKINTER EVENT>', 'STRING TO APPEND')
```


List of tkinter events:

| Event                            | Description                                                  |
| :------------------------------- | ------------------------------------------------------------ |
| Button-1  / ButtonPress-1 / 1    | Left button is pressed over an element. 1 corresponds to the left button, 2 to the middle button, 3 to the right button. <br>Buttons can go up to 5 |
| ButtonRelease-1                  | Left button is released over an element.                     |
| Double-Button-1                  | An element was double clicked. The 'Double' modifier was used. See below for more modifiers. |
| B1-Motion                        | Left button is held and moved around over an element.        |
| Motion                           | Mouse pointer is moved over an element                       |
| Enter                            | Mouse pointer entered the element                            |
| Leave                            | Mouse pointer left the element                               |
| Key / KeyPress<br>Keypress-a / a | A key was pressed. [Keysyms](https://www.tcl.tk/man/tcl8.6/TkCmd/keysyms.htm) can be used to bind specific key/s. <br>When using keysyms, 'Key' or 'KeyPress' can be omitted. <br> |
| KeyReleased                      | A key was released.                                          |
| FocusIn                      | Keyboard has focused on element.       |
| FocusOut                      | Keyboard switched focus from element.  |
| Visibility | Some part of the element is seen on screen |

Modifier keys can be put in front of events.

| Windows | MacOS   |
| ------- | ------- |
| Control | Command |
| Alt     | Option  |
| Shift            |<==|
| Double  | <== |
| Triple | <== |
| Quadruple | <== |

The following will bind Ctrl+z to the window:
```python
window.bind('<Control-z>', 'STRING TO APPEND')
```

To unbind an event from an element, use the `unbind` method.
```python
window['-KEY-'].unbind('TKINTER EVENT')
```

Here is sample code that shows these bindings in action.

Four main things are occurring.

1. Any button clicks in the window will return an event "Window Click" from window.read()
2. Right clicking the "Go" buttons will return an event "Go +RIGHT CLICK+" from window.read()
3. When the second Input Element receives focus, an event "-IN2- +FOCUS+" will be returned from window.read()
4. If the "Unbind " button is pressed, the right click binding of the "Go" button will be unbinded.

```python
import PySimpleGUI as sg

sg.theme('Dark Green 2')

layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN1-')],
            [sg.Input(key='-IN2-')],
            [sg.Button('Go'), sg.Button('Unbind'),sg.Button('Exit')]
              ]

window = sg.Window('Window Title', layout, finalize=True)

window.bind("<Button-1>", 'Window Click')
window['Go'].bind("<Button-3>", ' +RIGHT CLICK+')
window['-IN2-'].bind("<FocusIn>", ' +FOCUS+')

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Unbind':
        window['Go'].unbind('<Button-3>')

window.close()
```

[Tkinter bindings documentation](https://tcl.tk/man/tcl8.6/TkCmd/bind.htm#M18)


------------------

# Troubleshooting

![](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/emojis/frust_112.png)  


This section was added in early 2022, so it's a bit late in arriving, but it's a start.  This section meant to be found when searching for common errors.  
  
Some errors are too broad to cover here like module not found.  That one has a huge number of possible root causes.  
  
Instead, we're covering errors that are likely problems in your source code and they cannot be found by the PySimpleGUI code.  
  
If it's any consolation, I run into these same errors frequently!  We're programmers and mistakes happen.



## TypeError: list indices must be integers or slices, not ...

You'll get this error when you miss adding a comma at the end of a row in your layout.

Having extra commas isn't a problem and sometimes can be helpful to prevent this error.  By leaving an extra comma on the last row, then you'll be able to add more rows without the fear of this error.

This is a **good** layout:

```python
import PySimpleGUI as sg

layout = [[sg.Text('Row 1')],
          [sg.Text('Row 2')],]

event, values =  sg.Window('Window Title', layout).read(close=True)

```

This one is **not good**
If the commas are removed from the layout, then we'll get this TypeError...

```python
import PySimpleGUI as sg

layout = [[sg.Text('Row 1')]
          [sg.Text('Row 2')]]

event, values =  sg.Window('Window Title', layout).read(close=True)

```

Generates the TypeErrpr:

```
Traceback (most recent call last):
  File "scratch_356.py", line 4, in <module>
    [sg.Text('Row 2')]]
TypeError: list indices must be integers or slices, not Text

Process finished with exit code 1
```

