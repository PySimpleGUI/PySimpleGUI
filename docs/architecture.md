![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)

# PySimpleGUI Architecture

29-Nov-2018

PySimpleGUI is a "wrapper" for tkinter and Qt, with more on the way.  Their are a number of "tricks" / architecture decisions that make this package appealing to both beginners and experienced GUI developers.  Both will appreciate the simplicity.  Simple doesn't mean shallow.  There is considerable depth to the PySimpleGUI architecture.

# What is it?

PySimpleGUI is a code-generator in many ways.  When you get and configure a "Text Element (Widget)", PySimpleGUI makes ***exactly*** the same tkinter or Qt calls that a developer would.

Here is part of the code that is executed when you create a Text Widget.
```python
element.QT_Label = qlabel = QLabel(element.DisplayText, toplevel_win.QTWindow)  
if element.Justification is not None:  
    justification = element.Justification  
elif toplevel_win.TextJustification is not None:  
    justification = toplevel_win.TextJustification  
else:  
    justification = DEFAULT_TEXT_JUSTIFICATION  
if justification[0] == 'c':  
    element.QT_Label.setAlignment(Qt.AlignCenter)  
elif justification[0] == 'r':  
    element.QT_Label.setAlignment(Qt.AlignRight)  
if not auto_size_text:  
    if element_size[0] is not None:  
        element.QT_Label.setFixedWidth(element_size[0])  
    if element_size[1] is not None:  
        element.QT_Label.setFixedHeight(element_size[1])
```
The "beauty" or PySimpleGUI is the code you see above was specified with this line of code

`Text('Text', justification='left', size=(20,1))`

You can see just how little effort it took to generate, and configure on your behalf, code that resembles hand-generated Qt code.

## Architectural Decisions / Direction / Goals
* Present a GUI interface that is not object oriented
* Run an event loop within the user's application
* Events (button clicks, keystrokes, menu choices, etc) are funneled through a single interface, Window.Read()
	* Users can use simple 'if' statements to act upon the GUIs events.... if this button press, do this.
	* There are no callbacks
* Can change a widget's settings is a single call 
* Widget interaction is modeled simply, through simple widget updates
	* Change Widget A's value to value of Widget B is a single call
	* A widget's current value is returned in a dictionary when there is an event
* Can duplicate nearly any window layout created by coding directly in tkinter/Qt.
* Create complete documentation with a LOT of illustrations
* Don't try to solve all GUI problems.  
	* Be the 80% of 80/20. Leave the difficult 20% to the major frameworks. The the other 80% of GUI problems.

This is the magic combination that is PySimpleGUI.  It's a unique design that is approachable and enjoyable to use.  


# Window Definition

## Widgets (Elements in PySimpleGUI-speak)

Creating widgets and placing them into a window definition is done with a single object, named appropriately in a simple manner.  There are no "Label" widgets, but there is a "Text" one.

PySimpleGUI takes advantage of the Python named parameter feature.  Object calls and methods are loaded up with lots of potential parameters.  An IDE is a must.  Let's look at a Text widget.

```python
Text(text, size=(None, None),  auto_size_text=None, click_submits=None, relief=None, font=None, text_color=None, background_color=None, justification=None, pad=None, margins=None, key=None, tooltip=None)
```
There are 13 different values and settings that can be specified when creating a Text widget.  They are set when you create the widget, not several lines away.  

The amount of code required to set those 13 values is certainly greater than 1 line of code per value.  Closer to 2 or 3. 

Not only are you setting the visible settings for a Text widget, but you're setting some behaviors.  For example, `enable_events` will cause this Text widget to inform the application when someone clicks on the text.  In 1 parameter we've done the work of several lines of code dealing with callbacks.  Callbacks are not something PySimpleGUI have to deal with.  There are no callbacks.

## Defining a Window

Break a window can be broken down into rows like this:

![gui5_1](https://user-images.githubusercontent.com/13696193/44160133-6af0df80-a087-11e8-9dec-bb4d4c59393d.JPG)


Then stack row "rows"up and you've got yourself a window.

If you were to break down the sketched out window into Widgets, you would get something like this:
"Filename"
Input Text, Browse for files
Ok button, Cancel button

To create PySimpleGUI from this, you simply make a list for each row and put those lists together.

## Example Code - Simple Form-style Window
```python
    import PySimpleGUI as sg
    
    layout = [[sg.Text('Filename')],      
              [sg.Input(), sg.FileBrowse()],      
              [sg.OK(), sg.Cancel()] ]      
      
    event, values = sg.Window('Get filename example').Layout(layout).Read()    
```

![snag-0296](https://user-images.githubusercontent.com/13696193/49241117-ef683380-f3d4-11e8-9a68-20885ce0af61.jpg)

Here is a complete program that will show the example window, get the values from the user.

That's all you need. It's "simple" after all.

Your `layout` is a visual representation of your window.  You can clearly see 3 rows of widgets being defined.   If you would like your text to be red, then your layout would look like this:

```python
layout = [[sg.Text('Filename', text_color='red')],  
          [sg.Input(), sg.FileBrowse()],  
          [sg.OK(), sg.Cancel()]]
```
# Event Loops

## Example Code - Window with Event Loop

The event loop in PySimpleGUI is where all the action takes place.  There are no callbacks in PySimpleGUI.  All of the code is located in 1 place, inside the loop.

Getting user input is achieved by calling Window.Read()

A typical call to Read:
`event, values = sg.window.Read()`

`event` will be the event that happened.  values are all of the window's widgets current values, in dictionary format.

Adding an event loop to the previous example results in this code:

```python
import PySimpleGUI as sg  
  
layout = [[sg.Text('Filename', text_color='red')],  
          [sg.Input(), sg.FileBrowse()],  
          [sg.OK(), sg.Cancel()]]  
  
window = sg.Window('Get filename example').Layout(layout)  
  
# The Event Loop  
while True:  
    event, values = window.Read()  
    if event is None:  
        break
```

Within your event loop you take actions based on the event. 
Let's say you want to print whatever is in the input field when the user clicks the OK button.  The changed event loop is:
```python
# The Event Loop  
while True:  
    event, values = window.Read()  
    if event is None:  
        break  
    if event == 'OK':  
        print(values[0])
```

For buttons, when they are clicked, they return their text as the event, or you can set a "key" that will be what it returned to you when the button is clicked.  Adding a key to our OK button is done by adding the `key` parameter to the `OK()` call.

`sg.OK(key='_OK BUTTON_')`

Now when the OK button is clicked, the event value will be `_OK BUTTON_`.



# Widget Interaction

## Reading a widget

Any time that an event happens, you are provided a dictionary containing all of your widget's values.  
`event, values = window.Read()  `

The`values` return code is a dictionary of the widget's values.  Adding a `key` to the `Input` widget will cause that key to be what is used to "loop up" the value of that widget in the `values` variable.

If our `Input` widget was changed to have a key:
`sg.Input(key='_INPUT_')`

Then the value for that input field can be obtained from the `values` variable.  The value of the Input widget in this case will be:
`values['_INPUT_']`


## Changing a widget's value

Every widget has an `Update` method that will the widget's value or settings.

To update an widget, you must first get the object.  You can either save it in a variable when you create it or you can look up a widget by it's key.  Remember widgets are called Elements in PySimpleGUI.  To get the  Input Element in the previous example, you could call `Element` or `FindElement`.  
`window.Element(key)`

Once you have the element, then you can call the Update function:
`window.Element(key).Update(value and settings)`

## Widget interaction 

Building further on the `key` idea and Updating widgets, let's look at an example where the text 'Filename' is replaced by whatever you type in the input box.

The basic logic:
If button == 'OK':
    change text to input field's value
   
```python
import PySimpleGUI as sg  
  
layout = [[sg.Text('Filename', text_color='red', key='_TEXT_')],  
          [sg.Input(key='_INPUT_'), sg.FileBrowse()],  
          [sg.OK(key='_OK BUTTON_'), sg.Cancel()]]  
  
window = sg.Window('Get filename example').Layout(layout)  
  
# The Event Loop  
while True:  
  event, values = window.Read()  
  if event is None:  
        break  
  if event == '_OK BUTTON_':  
        window.Element('_TEXT_').Update(values['_INPUT_'])
```

As you can see, the pseudo-code on the real code look very similar.  

Note the statement `if event is None` is what catches the user clicking the X to close the window.  When the user does that, we want to exit the program by breaking from the event loop.

# Async Designs

Asynchronous designs are possible using PySimpleGUI.  To use async, add a `timeout` parameter to the `window.Read()` call., 

## Example

Let's say you wanted to make a GUI that displays your latest emails, checking every 30 seconds.  Rather than spin off a thread for the mail checker, run it within your GUI's event loop. Ideally we want the GUI to run as much as possible so that it's responsive.  This is how it's accomplished

```python
# The Event Loop  
while True:  
    event, values = window.Read(timeout=30000)
```

If you don't want to GUI to delay at all then set timeout=0.  Setting timeout=0 will run in a completely non-blocked, async fashion.

# Wrap-up

The overall architecture was meant to enable someone to duplicate both the GUI at a  near-pixel-level and the behavior of a program written directly in the tkinter or Qt framework.  PySimpleGUI provides a way of interacting with the native widgets in a more Python-friendly, novice-user-friendly manner.  It is not meant for large, commercial applications.  Those types of applications are in the 20% not covered by PySimpleGUI.

### Portability

Both PySimpleGUI code and the PySimpleGUI package itself are highly portable.  Taking a PySimpleGUI application from tkinter to Qt requires changing the import from `import PySimpleGUI` to `import PySimpleGUIQt`.  That really is all that is typically required.

The PySimpleGUI module itself is highly portable too.  Porting from tkinter to Qt took 1 week to get all of the widgets up and running with their basic operations.
