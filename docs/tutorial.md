# Add GUIs to your programs and scripts easily with PySimpleGUI

## Introduction
Python has dropped the GUI ball.  While the rest of the world has been enjoying the use of a mouse, most Python programs continue to be accessed via the command line.  Why is this, does anybody care, and what can be done about it?

## GUI Frameworks
There is no shortage of GUI frameworks for Python.  tkinter, WxPython, Qt, Kivy are a few of the major packages.  In addition, there are a good number of dumbed down GUI packages that wrap one of the major packages.  These include EasyGUI, PyGUI, Pyforms, ...

The problem is that beginners (those with experience of less than 6 weeks) are not capable of learning even the simplest of the major packages.  That leaves the wrapper-packages.  Users will quickly find it difficult or impossible to build a custom GUI layout.  Or, if it's possible, pages of code are still required.

PySimpleGUI attempts to address these GUI challenges by providing a super-simple, easy to understand interface to GUIs that can be customized easily.  Even the most complex of GUIs are often less than 20 lines of code when PySimpleGUI is used.

## The Secret

What makes PySimpleGUI superior for newcomers is that the package contains the majority of the code that the user is normally expected to write.  Button callbacks are handled by PySimpleGUI, not the user's code.  Beginners struggle to grasp the concept of a function, expecting them to understand a call-back function in the first few weeks is a stretch.

With most GUIs arranging the GUI Widgets often requires several lines of code.... at least one or two lines per widget.  PySimpleGUI uses an "auto-packer" that creates the layout for the user automatically.  There is no concept of a pack nor a grid system needed to layout a GUI Window.

Finally, PySimpleGUI leverages the Python language constructs in clever ways that shortens the amount of code and returns the GUI data in a straightforward manner.  When a Widget is created in a form layout, it is configured in-place, not several lines of code away.

## What is a GUI?

Most GUIs do one thing.... they collect information from the user and return it.  From a programmer's viewpoint this could be summed up as a function call that looks like this:

    button, values = GUI_Display(gui_layout)

What's expected from most GUIs is the button that was clicked (OK, cancel, save, yes, no, etc), and the values that were input by the user.  The essence of a GUI can be boiled down into a single line of code.

This is exactly how PySimpleGUI works (for these simple kinds of GUIs).  When the call is made to display the GUI, execution does no return until a button is clicked that closes the form.

There are more complex GUIs such as those that don't close after a button is clicked.  These complex forms can also be created with PySimpleGUI.  A remote control interface for a robot and a chat window are a couple of examples.

## The 5-Minute GUI

When is PySimpleGUI useful?  Immediately, anytime you've got a GUI need.  It will take under 5 minutes for you to create and try your GUI.  With those kinds of times, what do you have to lose trying it?

The best way to go about making your GUI in under 5 minutes is to copy one of the GUIs from the [PySimpleGUI Cookbook](https://pysimplegui.readthedocs.io/en/latest/cookbook/).  Follow these steps:
*  Find a GUI that looks similar to what you want to create
* Copy code from Cookbook
* Paste into your IDE and run

Let's look at the first recipe from the book

    import PySimpleGUI as sg

    # Very basic form.  Return values as a list
    form = sg.FlexForm('Simple data entry form')  # begin with a blank form

    layout = [
              [sg.Text('Please enter your Name, Address, Phone')],
              [sg.Text('Name', size=(15, 1)), sg.InputText('name')],
              [sg.Text('Address', size=(15, 1)), sg.InputText('address')],
              [sg.Text('Phone', size=(15, 1)), sg.InputText('phone')],
              [sg.Submit(), sg.Cancel()]
             ]

    button, values = form.LayoutAndRead(layout)

    print(button, values[0], values[1], values[2])


It's a reasonably sized form.


![super simple 2](https://user-images.githubusercontent.com/13696193/43934091-8100e29a-9c1b-11e8-8d0a-9bd2d13e6d8e.jpg)

If you only need to collect a few values and they're all basically strings, then you would copy this recipe and modify it to suit your needs.

## The 5-line GUI

Not all GUIs take 5 minutes.  Some take 5 lines of code.  This is a GUI with a custom layout contained in 5 lines of code.

    import PySimpleGUI as sg

    form = sg.FlexForm('My first GUI')

    layout = [ [sg.Text('Enter your name'), sg.InputText()],
               [sg.OK()] ]

    button, (name,) = form.LayoutAndRead(layout)


![myfirstgui](https://user-images.githubusercontent.com/13696193/44315412-d2918c80-a3f1-11e8-9eda-0d5d9bfefb0f.jpg)



## Making Your Custom GUI

That 5-minute estimate wasn't the time it takes to copy and paste the code from the Cookbook.  You should be able to modify the code within 5 minutes in order to get to your layout, assuming you've got a straightforward layout.

Widgets are called Elements in PySimpleGUI.  This list of Elements are spelled exactly as you would type it into your Python code.

### Core Element list
```
  Text
  InputText
  Multiline
  InputCombo
  Listbox
  Radio
  Checkbox
  Spin
  Output
  SimpleButton
  RealtimeButton
  ReadFormButton
  ProgressBar
  Image
  Slider
  Column
```

You can also have short-cut Elements.  There are 2 types of shortcuts.  One is simply other names for the exact same element (e.g. T instead of Text).  The second type configures an Element with particular setting, sparing the programmer from specifying all of the parameters (e.g. Submit is a button with the text "Submit" on it).
### Shortcut list

    T = Text
    Txt = Text
    In = InputText
    Input = IntputText
    Combo = InputCombo
    DropDown = InputCombo
    Drop = InputCombo

A number of common buttons have been implemented as shortcuts.  These include:
### Button  Shortcuts
    FolderBrowse
    FileBrowse
    FileSaveAs
    Save
    Submit
    OK
    Ok
    Cancel
    Quit
    Exit
    Yes
    No

The more generic button functions, that are also shortcuts
### Generic Buttons
    SimpleButton
    ReadFormButton
    RealtimeButton

These are all of the GUI Widgets you have to choose from. If it's not in this list, it doesn't go in your form layout.

### GUI Design Pattern

The stuff that tends not to change in GUIs are the calls that setup and show the Window.  It's the layout of the Elements that changes from one program to another.   This is the code from above with the layout removed:

    import PySimpleGUI as sg

    form = sg.FlexForm('Simple data entry form')
    # Define your form here (it's a list of lists)
    button, values = form.LayoutAndRead(layout)

 The flow for most GUIs is:
 * Create the Form object
 * Define GUI as a list of lists
 * Show the GUI and get results

These are line for line what you see in design pattern.

### GUI Layout

To create your custom GUI, first break your form down into "rows".  You'll be defining your form one row at a time.  Then for each for, you'll be placing one Element after another, working from left to right.

The result is a "list of lists" that looks something like this:

    layout = [  [Text('Row 1')],
                [Text('Row 2'), Checkbox('Checkbox 1', OK()), Checkbox('Checkbox 2'), OK()] ]

The layout produced this window:

![tutorial2](https://user-images.githubusercontent.com/13696193/44302312-e5259c00-a2f3-11e8-9c17-63e4eb130a9e.jpg)


## Display GUI & Get Results

Once you have your layout complete and you've copied over the lines of code that setup and show the form, it's time to look at how to display the form and get the values from the user.

This is the line of code that displays the form and provides the results:

    button, values = form.LayoutAndRead(layout)

   Forms return 2 values, the text of the button that was clicked and a ***list of values*** the user entered into the form.

If the example form was displayed and the user did nothing other than click the OK button, then the results would have been:

    button == 'OK'
    values == [False, False]

Checkbox Elements return a value of True/False.  Because these checkboxes defaulted to unchecked, the values returned were both False.

## Displaying Results

Once you have the values from the GUI it would be nice to check what values are in the variables. Rather than print them out using a `print` statement, let's stick with the GUI idea and output to a window.

PySimpleGUI has a number of Message Boxes to choose from.  The data passed to the message box will be displayed in a window.  The function takes any number of arguments.  Simply indicate all the variables you would like to see in the call.

The most-commonly used Message Box in PySimpleGUI is MsgBox.  To display the results of the previous example, one would write:

    MsgBox('The GUI returned:', button, values)

## Putting It All Together

Now that you know the basics, let's put together a form that contains as many PySimpleGUI's elements as possible.  Also, just to give it a nice look, we'll change the "look and feel" to a green and tan color scheme.

    import PySimpleGUI as sg

    sg.ChangeLookAndFeel('GreenTan')

    form = sg.FlexForm('Everything bagel', default_element_size=(40, 1))

    column1 = [[sg.Text('Column 1', background_color='#d3dfda', justification='center', size=(10,1))],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
               [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]
    layout = [
        [sg.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25))],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.InputText('This is my text')],
        [sg.Checkbox('My first checkbox!'), sg.Checkbox('My second checkbox!', default=True)],
        [sg.Radio('My first Radio!     ', "RADIO1", default=True), sg.Radio('My second Radio!', "RADIO1")],
        [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
         sg.Multiline(default_text='A second multi-line', size=(35, 3))],
        [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 3)),
         sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
         sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
         sg.Column(column1, background_color='#d3dfda')],
        [sg.Text('_'  * 80)],
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),
         sg.InputText('Default Folder'), sg.FolderBrowse()],
        [sg.Submit(), sg.Cancel()]
         ]

    button, values = form.LayoutAndRead(layout)
    sg.MsgBox(button, values)

That may seem like a lot of code, but try coding this same GUI layout directly in tkinter and you'll quickly realize that the length is tiny.

![everything for tutorial](https://user-images.githubusercontent.com/13696193/44302997-38531b00-a303-11e8-8c45-698ea62590a8.jpg)

The last line of code opens a message box. This is how it looks:

![tutorial results](https://user-images.githubusercontent.com/13696193/44303004-79e3c600-a303-11e8-8311-2f3726d364ad.jpg)


Each parameter to the message box call is displayed on a new line.  There are actually 2 lines of text in the message box.  The second line is very long and wrapped a number of times

Take a moment and pair up the results values with the GUI to get an understanding of how results are created and returned.

## Resources

### Installation
Requires Python 3

    pip install PySimpleGUI

Works on all systems that run tkinter, including the Raspberry Pi

### Documentation
[Main manual](https://pysimplegui.readthedocs.io/en/latest/)

[Cookbook](https://pysimplegui.readthedocs.io/en/latest/cookbook/)

### Home Page

www.PySimpleGUI.com
