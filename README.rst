
# PySimpleGUI

This really is a simple GUI, but also powerfully customizable.

    import PySimpleGUI as SG

    SG.MsgBox('My Message Box', 'This is the shortest GUI program ever!')

![snap0102](https://user-images.githubusercontent.com/13696193/42781058-1d28d9fa-8913-11e8-847e-5c2afc16ca4c.jpg)

I was frustrated by having to deal with the dos prompt when I had a powerful Windows machine right in front of me.  Why is it SO difficult to do even the simplest of input/output to a window in Python??

There are a number of 'easy to use' Python GUIs, but they're quite limiting.  PySimpleGUI tried to take the best of packages like `EasyGUI`(no longer maintained) and `WxSimpleGUI` (a great package, but was too limited for my application).   `PySimpleGUI` provides similar single-call-message-box solutions as you'll see.

GUI Packages with more functionality, like QT and WxPython, require configuring and can take a ***week*** to get *reasonably familiar* with the interfaces.

With a simple GUI, it becomes practical to "associate" .py files with the python interpreter on Windows.  Double click a py file and up pops a GUI window, a more pleasant experience than opening a dos Window and typing a command line.

The `PySimpleGUI` solution is focused on the ***developer***.  How can the desired result be achieved in as little and as simple code as possible?  This was the mantra used to create PySimpleGUI.   How can it be done is a Python-like way?

You can add a GUI to your command line with a single line of code.  With 3 or 4 lines of code you can add a fully customized GUI.  And for you Machine Learning folks out there, a **single line** progress meter call that you can drop into any loop to get a graphic like this one:


![progress meter 2](https://user-images.githubusercontent.com/13696193/42695896-a37eff5c-8684-11e8-8fbb-3d756655a44b.jpg)




    Features of PySimpleGUI include:
        Text
        Single Line Input
        Buttons including these types:
            File Browse
            Folder Browse
            Non-closing return
            Close form
        Checkboxes
        Radio Buttons
        Icons
        Multi-line Text Input
        Scroll-able Output
        Progress Bar
        Async/Non-Blocking Windows
        Tabbed forms
        Persistent Windows
        Redirect Python Output/Errors to scrolling Window
        'Higher level' APIs (e.g. MessageBox, YesNobox, ...)


An example of many widgets used on a single form.  A little further down you'll find the FIFTEEN lines of code required to create this complex form.

![all widgets](https://user-images.githubusercontent.com/13696193/42604818-adb1dd5c-8542-11e8-94cb-575881590f21.jpg)

  -----
## Getting Started with PySimpleGUI

### Installing

    pip install PySimpleGUI
 or
Simply download the file - PySimpleGUI.py and import it into your code


### Prerequisites

Python 3
tkinter

Should run on all Python platforms that have tkinter running on them.  Has been thoroughly tested on Windows.  While not tested elsewhere, should work on Linux, Mac, Pi, etc.

### Using

To use in your code, simply import....
 `import PySimpleGUI as SG`

Then use either "high level" API calls or build your own forms.

    SG.MsgBox('This is my first message box')
![snap0103](https://user-images.githubusercontent.com/13696193/42844641-a04bb798-89e1-11e8-8a37-50ddd9905772.jpg)

Yes, it's just that easy to have a window appear on the screen using Python.  With PySimpleGUI, making a custom form appear isn't much more difficult.  The goal is to get you running on your GUI within ***minutes***, not hours nor days.

---
## APIs

PySimpleGUI can be broken down into 2 types of API's:
 * High Level single call functions
 * Custom form functions


### Python Language Features

 There are a couple of Python language features that PySimpleGUI utilizes heavily that should be understood first...
 * Variable number of arguments to a function call
 * Optional parameters to a function call

#### Variable Number of Arguments

 The "High Level" API calls that *output* values take a variable number of arguments so that they match a "print" statement as much as possible.  The idea is to make it simple for the programmer to output as many items as desired and in any format.  The user need not convert the variables to be output into the strings.  The PySimpleGUI functions do that for the user.

    SG.MsgBox('Variable number of parameters example', var1, var2, "etc")

Each new item begins on a new line in the Message Box

  ![snap0104](https://user-images.githubusercontent.com/13696193/42844739-ebea22ac-89e1-11e8-8dd1-e61441325701.jpg)


#### Optional Parameters to a Function Call

This feature of the Python language is utilized ***heavily*** as a method of customizing forms and form Elements.  Rather than requiring the programmer to specify every possible option for a widget, instead only the options the caller wants to override are specified.

Here is the function definition for the MsgBox function. The details aren't important.  What is important is seeing that there is a long list of potential tweaks that a caller can make.  However, they don't *have* to be specified on each and every call.

    def MsgBox(*args,
               button_color=None,
               button_type=MSG_BOX_OK,
               auto_close=False,
               auto_close_duration=None,
               icon=DEFAULT_WINDOW_ICON,
               line_width=MESSAGE_BOX_LINE_WIDTH,
               font=None):

If the caller wanted to change the button color to be black on yellow, the call would look something like this:

    SG.MsgBox('This box has a custom button color',
              button_color=('black', 'yellow'))


![snap0105](https://user-images.githubusercontent.com/13696193/42844830-2d7e8b9a-89e2-11e8-8ef4-5af9e36f30f3.jpg)


---

### High Level API Calls

The classic "input a value, print result" example.
Often command line programs simply take some value as input on the command line, do something with it and then display the results.  Moving from the command line to a GUI is very simple.
This code prompts user to input a line of text and then displays that text in a messages box:

    import PySimpleGUI_local as SG

    rc = SG.GetTextBox('Title', 'Please input something')
    SG.MsgBox('Results', 'The value returned from GetTextBox', rc)

![GetTextBox](https://user-images.githubusercontent.com/13696193/42592930-1ca1370a-8519-11e8-907e-ad73e9be7749.jpg)

![MsgBox](https://user-images.githubusercontent.com/13696193/42592929-1c7361ae-8519-11e8-8adc-411c1afee69f.jpg)

#### Message Boxes
In addition to MsgBox, you'll find a several API calls that are shortcuts to common messages boxes.  You can achieve similar results by calling MsgBox with the correct parameters.

The differences tend to be the number and types of buttons.   Here are the calls and the windows that are created.

    import PySimpleGUI as SG

  `SG.MsgBoxOK('This is an OK MsgBox')`

  ![msgboxok](https://user-images.githubusercontent.com/13696193/42599852-8dd6914e-852e-11e8-888f-f133d787210b.jpg)

    SG.MsgBoxOKCancel('This is an OK Cancel MsgBox')

![msgboxokcancel](https://user-images.githubusercontent.com/13696193/42599858-8e8eff22-852e-11e8-8d5c-3fe99237eb7f.jpg)

    SG.MsgBoxCancel('This is a Cancel MsgBox')
![msgboxcancel](https://user-images.githubusercontent.com/13696193/42599857-8e53dc4e-852e-11e8-8e83-6a8cccf8e706.jpg)

    SG.MsgBoxYesNo('This is a Yes No MsgBox')
![msgboxyesno](https://user-images.githubusercontent.com/13696193/42599856-8e304540-852e-11e8-975d-fb2b62e94300.jpg)

    SG.MsgBoxError('This is an error MsgBox')
![msgbox error](https://user-images.githubusercontent.com/13696193/42599853-8df8e078-852e-11e8-90dc-7815d69bff7e.jpg)

    SG.MsgBoxAutoClose('This is an autoclose MsgBox')

![msgbox autoclose](https://user-images.githubusercontent.com/13696193/42599855-8e147572-852e-11e8-8c23-7ec771909062.jpg)

    SG.ScrolledTextBox(my_text, height=10)

![scrolledtextbox](https://user-images.githubusercontent.com/13696193/42600800-a44f4562-8531-11e8-8c21-51dd70316879.jpg)

Take a moment to look at that last one.  It's such a simple API call and yet the result is awesome.  Rather than seeing text scrolling past on your display, you can capture that text and present it in a scrolled interface.  It's handy enough of an API call that it can also be called using the name `sprint` which is easier to remember than `ScrollectTextBox`.   Your code could contain a line like:

    sprint(f'My variables values include x={x}', f'y={y}')

This becomes a debug print of sorts that will route to a scrolled window.

#### High Level User Input

There are 3 very basic user input high-level function calls.  It's expected that for most applications, a custom input form will be created. If you need only 1 value, then perhaps one of these high level functions will work.
 - GetTextBox
 - GetFileBox
 - GetFolderBox

 `submit_clicked, value = SG.GetTextBox('Title', 'Please enter anything')`

![gettextbox](https://user-images.githubusercontent.com/13696193/42600399-1ef66a5e-8530-11e8-9bc4-78ea839213cd.jpg)

    submit_clicked, value = SG.GetFileBox('Title', 'Choose a file')

![getfilebox](https://user-images.githubusercontent.com/13696193/42600398-1ed8a122-8530-11e8-9f74-88b101efcea4.jpg)

    submit_clicked, value = SG.GetPathBox('Title', 'Choose a folder')

![getfolderbox](https://user-images.githubusercontent.com/13696193/42600397-1ea7cef8-8530-11e8-8d43-e1000c0933cd.jpg)

#### Progress Meter!
We all have loops in our code.  'Isn't it joyful waiting, watching a counter scrolling past in a text window?  How about one line of code to get a progress meter, that contains statistics about your code?
![progress meter 3](https://user-images.githubusercontent.com/13696193/42696332-dca3ca6e-8685-11e8-846b-6bee8362ee5f.jpg)

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
        SG.EasyProgressMeter('My Meter', i+1, 10000, 'Optional message')

That line of code resulted in this window popping up and updating.

![progress meter 5](https://user-images.githubusercontent.com/13696193/42696912-a5c958b8-8687-11e8-9a7d-a390a465407a.jpg)

A meter AND fun statistics to watch while your machine grinds away, all for the price of 1 line of code.
With a little trickery you can provide a way to break out of your loop using the Progress Meter form.  The cancel button results in a `False` return value from `EasyProgressMeter`.  It normally returns `True`.

    if not SG.EasyProgressMeter('My Meter', i+1, 10000, 'Optional message'):
	    break

***Be sure and add one to your loop counter*** so that your counter goes from 1 to the max value.  If you do not add one, your counter will never hit the max value.  Instead it will go from 0 to max-1.

---
# Custom Form API Calls

This is the FUN part of the programming of this GUI.  In order to really get the most out of the API, you should be using an IDE that supports auto complete or will show you the definition of the function.  This will make customizing go  smoother.

It's both not enjoyable nor helpful to immediately jump into tweaking each and every little thing available to you.   Let's start with a basic Browse for a file and do something with it.
# Copy these design patterns!
## Pattern 1 - With Context Manager

    with SG.FlexForm('SHA-1 & 256 Hash', auto_size_text=True) as form:
        form_rows = [[SG.Text('SHA-1 and SHA-256 Hashes for the file')],
                     [SG.InputText(), SG.FileBrowse()],
                     [SG.Submit(), SG.Cancel()]]
        (button, (source_filename, )) = form.LayoutAndShow(form_rows)

## Pattern 2 - No Context Manager

    form = SG.FlexForm('SHA-1 & 256 Hash', auto_size_text=True)
    form_rows = [[SG.Text('SHA-1 and SHA-256 Hashes for the file')],
                 [SG.InputText(), SG.FileBrowse()],
                 [SG.Submit(), SG.Cancel()]]
    (button, (source_filename,)) = form.LayoutAndShow(form_rows)


These 2 design patters both produce this custom form:

![sha hash](https://user-images.githubusercontent.com/13696193/42603149-a56acf3a-853a-11e8-91de-771efd3a65a8.jpg)

It's important to use the "with" context manager so that resources are freed as quickly as possible, using the currently executing thread.  PySimpleGUI uses `tkinter`.  `tkinter` is very picky about who releases objects and when.  The `with` takes care of disposing of everything properly for you.

The second design pattern is not context manager based. There are times when the context manager hides errors.  If you are struggling with an unknown error, try modifying the code to run without a context manager.

You will use these design patterns or code templates for all of your "normal" (blocking) types of input forms.  Copy it and modify it to suit your needs.  This is the quickest way to get your code up and running with PySimpleGUI.  This is the most basic / normal of the design patterns.

### Line by line explanation

Going through each line of code in the above form will help explain how to use this design patter.  Copy, modify and run it!

    with SG.FlexForm('SHA-1 & 256 Hash', auto_size_text=True) as form:
This creates a new form, storing it in the variable `form`.

        form_rows = [[SG.Text('SHA-1 and SHA-256 Hashes for the file')],
The next few rows of code lay out the rows of elements in the window to be displayed.  The variable `form_rows` holds our entire GUI window.   The first row of this form has a Text element.  These simply display text on the form.

                     [SG.InputText(), SG.FileBrowse()],
Now we're on the second row of the form.  On this row there are 2 elements.  The first is an `Input` field.  It's a place the user can enter `strings`.  The second element is a `File Browse Button`.  A file or folder browse button will always fill in the text field to it's left unless otherwise specified.  In this example, the File Browse Button will interact with the `InputText` field to its left.

				    [SG.Submit(), SG.Cancel()]]

The last line of the `form_rows` variable assignment contains a Submit and a Cancel Button.  These are buttons that will cause a form to return its value to the caller.

        (button, (source_filename, )) = form.LayoutAndShow(form_rows)
This is the code that **displays** the form, collects the information and returns the data collected.  In this example we have a button return code and only 1 input field

---
### Design Goals
> Copy, Paste, Run.

`PySimpleGUI's` goal with the API is to be easy on the programmer, and to function in a Python-like way. Since GUIs are visual, it was desirable for the SDK to visually match what's on the screen.

Forms are represented as Python lists.  There are 2 lists in particular.  One is a list of rows that form up a GUI screen.  The other is a list of Elements (or Widgets) on each row.  Each Elements is specified by names such as Text, Button, Checkbox, etc.

Some elements are shortcuts, meant to make it easy on the programmer who will write less code using them.  Rather than writing a `Button`, with  `button_name = "Submit"`, etc, the caller can simply writes `Submit`.  Some examples include: `Text` has a short-cut function named `T`.  `TextInput` has `In`.   See each API call for the shortcuts.


---

## Return values

   Return information from FlexForm, SG's primary form builder interface, is in this format:

    (button, (value1, value2, ...))

Each of the Elements that are Input Elements will have a value in the list of return values.  You can unpack your GUI directly into the variables you want to use.

    (button, (filename, folder1, folder2, should_overwrite) = form.LayoutAndShow(form_rows)


If you have a SINGLE value being returned, it is written this way:

    (button, (value1,)) = form.LayoutAndShow(form_rows)
 Another way of parsing the return values is to store the list of values into a variable representing the list of values.

     (button, (value_list)) = form.LayoutAndShow(form_rows)
     value1 = value_list[0]
     value2 = value_list[1]
     ...

---
## All Widgets / Elements
This code utilizes as many of the elements in one form as possible.

    with FlexForm('Everything bagel', auto_size_text=True, default_element_size=(30,1)) as form:
        layout = [[Text('Here they all are!', size=(30,1), font=("Helvetica", 25), text_color='red')],
                  [Text('Here is some text with font sizing', font=("Helvetica", 15))],
                  [InputText()],
                  [Checkbox('My first checkbox!'), Checkbox('My second checkbox!', default=True)],
                  [Radio('My first Radio!', "RADIO1", default=True), Radio('My second checkbox!', "RADIO1")],
                  [Multiline(DefaultText='This is the DEFAULT text should you decide not to type anything', scale=(2, 10))],
                  [InputCombo(['choice 1', 'choice 2'], size=(20, 3))],
                  [Text('_'  * 90, size=(60, 1))],
                  [Text('Choose Source and Destination Folders', size=(35,1))],
                  [Text('Source Folder', size=(15, 1), auto_size_text=False), InputText('Source'), FolderBrowse()],
                  [Text('Destination Folder', size=(15, 1), auto_size_text=False), InputText('Dest'), FolderBrowse()],
                  [SimpleButton('Your Button with any text you want')],
                  [SimpleButton('Big Text', size=(12,1), font=("Helvetica", 20))],
                  [Submit(), Cancel()]]

        (button, (values)) = form.LayoutAndShow(layout)

        MsgBox('Results', 'You clicked {}'.format(button),'The values returned from form', values , font = ("Helvetica", 15))

This is a somewhat complex form with quite a bit of custom sizing to make things line up well.  This is code you only have to write once.  When looking at the code, remember that what you're seeing is a list of lists.  Each row contains a list of Graphical Elements that are used to create the form.

![all widgets](https://user-images.githubusercontent.com/13696193/42604818-adb1dd5c-8542-11e8-94cb-575881590f21.jpg)

Clicking the Submit button caused the form call to return.  The call to MsgBox resulted in this dialog box.
![results](https://user-images.githubusercontent.com/13696193/42604952-502f64e6-8543-11e8-8045-bc10d38c5fd4.jpg)


    (button, (values)) = form.LayoutAndShow(layout)
**`Note, button value can be None`**.  The value for `button` will be the text that is displayed on the button element when it was created.  If the user closed the form using something other than a button, then `button` will be `None`.

You can see in the MsgBox that the values returned are a list.  Each input field in the form generates one item in the return values list.  All input fields return a `string` except for Check Boxes and Radio Buttons.  These return `bool`.

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
        auto_size_text=DEFAULT_AUTOSIZE_TEXT,
        scale=(None, None),
        location=(None, None),
        button_color=None,Font=None,
        progress_bar_color=(None,None),
        is_tabbed_form=False,
        border_depth=None,
        auto_close=False,
        auto_close_duration=DEFAULT_AUTOCLOSE_TIME,
        icon=DEFAULT_WINDOW_ICON):

Parameter Descriptions.  You will find these same parameters specified for each `Element` and some of them in `Row` specifications.  The `Element` specified value will take precedence over the `Row` and `Form` values.

	    default_element_size - Size of elements in form in characters (width, height)
	    auto_size_text - Bool. True is elements should size themselves according to contents
	    scale - Set size of element to be a multiple of the Element size
	    location - Location to place window in pixels
	    button_color - Default color for buttons (foreground, background). Can be text or hex
	    progress_bar_color - Foreground and background colors for progress bars
	    is_tabbed_form - Bool. If True then form is a tabbed form
	    border_depth - Amount of 'bezel' to put on input boxes, buttons, etc.
	    auto_close - Bool.  If True form will autoclose
	    auto_close_duration - Duration in seconds before form closes
	    icon - .ICO file that will appear on the Task Bar and end of Title Bar


#### Sizes
Note several variables that deal with "size".  Element sizes are measured in characters.  A Text Element with a size of 20,1 has a size of 20 characters wide by 1 character tall.

The default Element size for PySimpleGUI is `(45,1)`.

Sizes can be set at the element level, or in this case, the size variables apply to all elements in the form.  Setting `size=(20,1)` in the form creation call will set all elements in the form to that size.

In addition to `size` there is a `scale` option.  `scale` will take the Element's size and scale it up or down depending on the scale value.  `scale=(1,1)` doesn't change the Element's size.  `scale=(2,1)` will set the Element's size to be twice as wide as the size setting.


#### FlexForm - form-level variables overview
A summary of the variables that can be changed when a FlexForm is created

         default_element_size - set default size for all elements in the form
         auto_size_text- true/false autosizing turned on / off
         scale - set scale value for all elements
         button_color- default button color (foreground, background)
         font - font name and size for all text items
         progress_bar_color - progress bar colors
         is_tabbed_form - true/false indicates form is a tabbed or normal form
         border_depth - style setting for buttons, input fields
         auto_close - true/false indicates if form will automatically close
         auto_close_duration - how long in seconds before closing form
         icon - filename for icon that's displayed on the window on taskbar


## Elements
"Elements" are the building blocks used to create forms.  Some GUI APIs use the term Widget to describe these graphic elements.

     Text
     Single Line Input
     Buttons including these types:
         File Browse
         Folder Browse
         Non-closing return
         Close form
     Checkboxes
     Radio Buttons
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

    layout = [[SG.Text('This is what a Text Element looks like')]]


 ![textelem](https://user-images.githubusercontent.com/13696193/42670173-4c1fcb40-8627-11e8-851a-5a9ee4672320.jpg)


The most basic element is the Text element.  It simply displays text.  Many of the 'options' that can be set for a Text element are shared by other elements.  Size, Scale are a couple that you will see in every element.

    Text(Text,
        scale=(None, None),
        size=(None, None),
        auto_size_text=None,
        font=None,
        text_color=None)

Some commonly used elements have 'shorthand' versions of the functions to make the code more compact.  The functions `T` and `Txt` are the same as calling `Text`.

**Fonts** in PySimpleGUI are always in this format:

    (font_name, point_size)

The default font setting is

    ("Helvetica", 10)

**Color** in PySimpleGUI are always in this format:

    (foreground, background)

The values foreground and background can be the color names or the hex value formatted as a string:

    "#RRGGBB"

**auto_size_text**
A `True` value for `auto_size_text`, when placed on any Element, indicates that the width of the Element should be shrunk do the width of the text.  This is particularly useful with `Buttons` as fixed-width buttons are somewhat crude looking.  The default value is `False`.  You will often see this setting on FlexForm definitions.

**Shorthand functions**
The shorthand functions for `Text` are `Txt` and `T`


####  Multiline Text Element

    layout = [[SG.Multiline('This is what a Multi-line Text Element looks like', size=(45,5))]]
![multiline text](https://user-images.githubusercontent.com/13696193/42670464-0824c754-8629-11e8-9741-6ed08f924618.jpg)
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

![output element](https://user-images.githubusercontent.com/13696193/42704820-5446959c-869f-11e8-849e-047ea280387a.jpg)

    Output(scale=(None, None),
           size=(None, None))
.

     scale  - How much to scale size of element
     size - Size of element (width, height) in characters

###  Input Elements
  These make up the majority of the form definition.  Optional variables at the Element level override the Form level values (e.g. `size` is specified in the Element).  All input Elements create an entry in the list of return values.  A Text Input Element creates a string in the list of items returned.

#### Text Input Element

    layout = [[SG.InputText('Default text')]]
![inputtext](https://user-images.githubusercontent.com/13696193/42693515-610a716c-867d-11e8-9a00-7e7fcf771230.jpg)

      def InputText(default_text = '',
                    scale=(None, None),
                    size=(None, None),
                    auto_size_text=None,
                    password_char='')
.

     default_text - Text initially shown in the input box
     scale - Amount size is scaled by
     size - (width, height) of element in characters
     auto_size_text- Bool.  True is element should be sized to fit text
     password_char - Character that will be used to replace each entered character. Setting to a value indicates this field is a password entry field

Shorthand functions that are equivalent to `InputText` are `Input` and `In`


#### Combo Element
Also known as a drop-down list.  Only required parameter is the list of choices.  The return value is a string matching what's visible on the GUI.

    layout = [[SG.InputCombo(['choice 1', 'choice 2'])]]

![combo](https://user-images.githubusercontent.com/13696193/42694431-631c4108-8680-11e8-8e99-c1a642734464.jpg)

    InputCombo(values,
               scale=(None, None),
               size=(None, None),
               auto_size_text=None)
.

     values - Choices to be displayed. List of strings
     scale - Amount to scale size by
     size - (width, height) of element in characters
     auto_size_text - Bool. True if size should fit the text length

#### Radio Button Element
Creates one radio button that is assigned to a group of radio buttons.  Only 1 of the buttons in the group can be selected at any one time.

    layout =  [[SG.Radio('My first Radio!', "RADIO1", default=True), SG.Radio('My second radio!', "RADIO1")]]

![radio element](https://user-images.githubusercontent.com/13696193/42705705-327b4b6c-86a2-11e8-81a7-740e57646ba8.jpg)

     Radio(text,
           group_id,
           default=False,
           scale=(None, None),
           size=(None, None),
           auto_size_text=None,
           font=None)

.

     text - Text to display next to button
     group_id - Groups together multiple Radio Buttons. Can be any value
     default - Bool.  Initial state
     scale - Amount to scale size of element
     size- (width, height) size of element in characters
     auto_size_text - Bool.  True if should size width to fit text
     font - Font type and size for text display


#### Checkbox Element
Checkbox elements are like Radio Button elements.  They return a bool indicating whether or not they are checked.

    layout =  [[SG.Checkbox('My first Checkbox!', default=True), SG.Checkbox('My second Checkbox!')]]

![checkbox element](https://user-images.githubusercontent.com/13696193/42717015-655d73d2-86cc-11e8-9c69-3c810f48e578.jpg)


    Checkbox(text,
             default=False,
             scale=(None, None),
             size=(None, None),
             auto_size_text=None,
             font=None):
.

     text - Text to display next to checkbox
     default- Bool.  Initial state
     scale - Amount to scale size of element
     size - (width, height) size of element in characters
     auto_size_text- Bool.  True if should size width to fit text
     font- Font type and size for text display


#### Spin Element
An up/down spinner control.  The valid values are passed in as a list.

    layout =  [[SG.Spin([i for i in range(1,11)], initial_value=1), SG.Text('Volume level')]]

![spin element](https://user-images.githubusercontent.com/13696193/42717231-8ddb51d4-86cd-11e8-827a-75f2237477fa.jpg)

    Spin(values,
         intiial_value=None,
         scale=(None, None),
         size=(None, None),
         auto_size_text=None,
         font=None)
.

     values - List of valid values
     initial_value - String with initial value
     scale - Amount to scale size of element
     size - (width, height) size of element in characters
     auto_size_text - Bool.  True if should size width to fit text
     font - Font type and size for text display

#### Button Element
Buttons are the most important element of all!  They cause the majority of the action to happen.  After all, it's a button press that will get you out of a form, whether it but Submit or Cancel, one way or another a button is involved in all forms.  The only exception is to this is when the user closes the window using the "X" in the upper corner which means no button was involved.

The Types of buttons include:
* Folder Browse
* File Browse
* Close Form
* Read Form


 Close Form - Normal buttons like Submit, Cancel, Yes, No, etc, are "Close Form" buttons.  They cause the input values to be read and then the form is closed, returning the values to the caller.

Folder Browse - When clicked a folder browse dialog box is opened.  The results of the Folder Browse dialog box are written into one of the input fields of the form.

File Browse - Same as the Folder Browse except rather than choosing a folder, a single file is chosen.

Read Form - This is an async form button that will read a snapshot of all of the input fields, but does not close the form after it's clicked.

While it's possible to build forms using the Button Element directly, you should never need to do that.  There are pre-made buttons and shortcuts that will make life much easier.  The most basic Button element call to use is `SimpleButton`

    SimpleButton(text,
                 scale=(None, None),
                 size=(None, None),
                 auto_size_text=None,
                 button_color=None,
                 font=None)

Pre-made buttons include:

    OK
    Ok
    Submit
    Cancel
    Yes
    No
    FileBrowse
    FolderBrowse
.
    layout =  [[SG.OK(), SG.Cancel()]]

![ok cancel](https://user-images.githubusercontent.com/13696193/42717733-1803f584-86d1-11e8-9223-36b782971b9f.jpg)

The FileBrowse and FolderBrowse buttons both fill-in values into a text input field somewhere on the form.  The location of the TextInput element is specified by the `Target` variable in the function call.  The Target is specified using a grid system.  The rows in your GUI are numbered starting with 0. The target can be specified as a hard coded grid item or it can be relative to the button.

The default value for `Target` is `(ThisRow, -1)`.   ThisRow is a special value that tells the GUI to use the same row as the button.  The Y-value of -1 means the field one value to the left of the button.  For a File or Folder Browse button, the field that it fills are generally to the left of the button is most cases.

Let's examine this form as an example:

![button target example](https://user-images.githubusercontent.com/13696193/42718075-b4dcb61e-86d3-11e8-904c-d709dd364108.jpg)

The `InputText` element is located at (1,0)... row 1, column 0.  The `Browse` button is located at position (2,0).  The Target for the button could be any of these values:

    Target = (1,0)
    Target = (-1,0)
The code for the entire form could be:

    layout =  [[SG.T('Source Folder')],
               [SG.In()],
               [SG.FolderBrowse(Target=(-1,0)), SG.OK()]]

**Custom Buttons**
If you want to define your own button, you will generally do this with the Button Element `SimpleButton`.

layout =  [[SG.SimpleButton('My Button')]]

![singlebutton](https://user-images.githubusercontent.com/13696193/42718281-9453deca-86d5-11e8-83c7-4b6d33720858.jpg)

All buttons can have their text changed by changing the `button_text` variable.

**File Types**
The `FileBrowse` button has an additional setting named `file_types`.  This variable is used to filter the files shown in the file dialog box.  The default value for this setting is

    FileTypes=(("ALL Files", "*.*"),)

This code produces a form where the Browse button only shows files of type .TXT

    layout =  [[SG.In() ,SG.FileBrowse(file_types=(("Text Files", "*.txt"),))]]

  ***The ENTER key***
       The ENTER key is an important part of data entry for forms.  There's a long  tradition of the enter key being used to quickly submit forms.  PySimpleGUI implements this by tying the ENTER key to the first button that closes or reads a form.  If there are more than 1 button on a form, the FIRST button that is of type Close Form or Read Form is used.  First is determined by scanning the form, top to bottom and left to right.


---
#### ProgressBar
The `ProgressBar` element is used to build custom Progress Bar forms.  It is HIGHLY recommended that you use the functions that provide a complete progress meter solution for you.  Progress Meters are not easy to work with because the forms have to be non-blocking and they are tricky to debug.

The **easiest** way to get progress meters into your code is to use the `EasyProgessMeter` API.  This consists of a pair of functions, `EasyProgessMeter` and `EasyProgressMeterCancel`.  You can easily cancel any progress meter by calling it with the current value = max value.  This will mark the meter as expired and close the window.
You've already seen EasyProgressMeter calls presented earlier in this readme.

    SG.EasyProgressMeter('My Meter', i+1, 1000, 'Optional message')

The return value for `EasyProgressMeter` is:
`True` if meter updated correctly
`False` if user clicked the Cancel button, closed the form, or vale reached the max value.
**Customized Progress Bar**
If you want a bit more customization of your meter, then you can go up 1 level and use the calls to `ProgressMeter` and `ProgressMeterUpdate`.  These APIs behave like an object we're all used to.  First you create the `ProgressMeter` object, then you call the `Update` method to update it.

You setup the progress meter by calling

    my_meter = ProgressMeter(title,
    					     max_value,
    					     *args,
    		d			     orientantion=None,
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

    my_meter = SG.ProgressMeter('Meter Title', 100000, orentation='Vert')

    for i in range(0, 100000):
        SG.ProgressMeterUpdate(my_meter, i+1, 'Some variable', 'Another variable')


The final way of using a Progress Meter with PySimpleGUI is to build a custom form with a `ProgressBar` Element in the form.  You will need to run your form as a non-blocking form.  When you are ready to update your progress bar, you call the `UpdateBar` method for the `ProgressBar` element itself.


#### Output
The Output Element is a re-direction of Stdout.  Anything "printed" will be displayed in this element.

    Output(scale=(None, None),
           size=(None, None))

Here's a complete solution for a chat-window using an Async form with an Output Element

    import PySimpleGUI as g

    with g.FlexForm('Chat Window', auto_size_text=True, default_element_size=(30, 2)) as form:
        form.AddRow(g.Text('This is where standard out is being routed', size=[40,1]))
        form.AddRow(g.Output(size=(80, 20)))
        form.AddRow(g.Multiline(size=(70, 5), enter_submits=True), g.ReadFormButton('SEND', button_color=(g.YELLOWS[0], g.BLUES[0])), g.SimpleButton('EXIT', button_color=(g.YELLOWS[0], g.GREENS[0])))

        # ---===--- Loop taking in user input and printing it --- #
      while True:
            (button, value) = form.Read()
            if button == 'SEND':
                print(value)
            else:
                print('Exiting the form now')
                break


## Tabbed Forms
Tabbed forms are shown using the `ShowTabbedForm` call.  The call has the format

     results = ShowTabbedForm('Title for the form',
                              (form,layout,'Tab 1 label'),
                              (form2,layout2, 'Tab 2 label'))

Each of the tabs of the form is in fact a form.  The same steps are taken to create the form as before.  A `FlexForm` is created, then rows are filled with Elements, and finally the form is shown.  When calling `ShowTabbedForm`, each form is passed in as a tuple.  The tuple has  the format:  `(the form, the rows, a label shown on the tab)`

## Global Settings
**Global Settings**
You can set the global settings using the function `PySimpleGUI.SetOptions`.  Each option has an optional parameter that's used to set it.

    SetOptions(icon=None,
               button_color=(None,None),
               element_size=(None,None),
               margins=(None,None),
               element_padding=(None,None),
               auto_size_text=None,
               font=None, border_width=None,
               autoclose_time=None,
               message_box_line_width=None,
               progress_meter_border_depth=None):

Explanation of parameters

	          icon - filename of icon used for taskbar and title bar
	          button_color - button color (foreground, background)
	          element_size - element size (width, height) in characters
	          margins - tkinter margins around outsize
	          element_padding - tkinter padding around each element
	          auto_size_text - autosize the elements to fit their text
	          font - font used for elements
	          border_width - amount of bezel or border around sunken or raised elements
	          autoclose_time - time in seconds for autoclose boxes
	          message_box_line_width - number of characers in a line of text in message boxes
	          progress_meter_border_depth - amount of border around raised or lowered progress meters


These settings apply to all forms `SetOptions`.  The Row options and Element options will take precedence over these settings.  Settings can be thought of as levels of settings with the Form-level being the highest and the Element-level the lowest.  Thus the levels are:

 - Form level
 - Row level
 - Element level

Each lower level overrides the settings of the higher level

## Asynchronous (Non-Blocking) Forms
While the majority of GUIs are a simple exercise to "collect input values and return with them", there are instances where we want to continue executing while the form is open.  These are "asynchronous" forms and require special options, new SDK calls, and **great care**.


## Sample Applications
Use the example programs as a starting basis for your GUI.  Copy, paste, modify and run!  The demo files are:
`Demo DisplayHash1and256.py` - Demonstrates using High Level API calls to get a filename
`Demo DupliucateFileFinder.py` - Demonstrates High Level API to get a folder & Easy Progress Meter to show progress of the file scanning
`Demo Recipes.py` - Three sample forms including an asynchronous form
`Demo HowDoI.py` - An amazing little application.  Acts as a front-end to HowDoI.  This one program could forever change how you code. It does searches on Stack Overflow and returns the CODE found in the best answer for your query.

## Fun Stuff
Here are some things to try if you're bored or want to further customize

**Random colors**
To set a button or text to a random color, use the string `'random'` as the color value.  You can also call `PySimpleGUI.GetRandomColor`.
To get a random color pair call `PySimpleGUI.GetRandomColorPair`.  This returns a tuple containing a random color and
that color's compliment.
sprint

**sprint**
Call `sprint` with as many parameters as you want and it'll print them all out in a `ScrolledTextBox`.  This is simply a function pointing to `PySimpleGUI.ScrolledTextBox`.

---
## Known Issues
While not an "issue" this is a ***stern warning***

## **Do not attempt** to call `PySimpleGUI` from multiple threads! It's `tkinter` based and `tkinter` has issues with multiple threads

**Progress Meters** - the visual graphic portion of the meter may be off.  May return to the native tkinter progress meter solution in the future.  Right now a "custom" progress meter is used.  On the bright side, the statistics shown are extremely accurate and can tell you something about the performance of your code.

## Contributing

A MikeTheWatchGuy production... entirely responsible for this code.... unless it causes you trouble in which case I'm not at all responsible.

## Versioning
|Version | Description |
|--|--|
| 1.0.9   | July 10, 2018 - Initial Release |
| 1.0.21 | July 13, 2018 - Readme updates  |
| 2.0.0 | July 16, 2018 - ALL optional parameters renamed from CamelCase to all_lower_case

## Code Condition

    Make it run
    Make it right
    Make it fast

It's a recipe for success if done right.  PySimpleGUI has completed the "Make it run" phase.  It's far from "right" in many ways.  These are being worked on.  The module is particularly poor for PEP 8 compliance.  It was a learning exercise that turned into a somewhat complete GUI solution for lightweight problems.

While the internals to PySimpleGUI are a tad sketchy, the public interfaces into the SDK are more strictly defined and comply with PEP 8 for the most part.

## Authors
MikeTheWatchGuy

## License

This project is limited to non-commercial applications.  If you wish to use it commercially, please contact one of the authors.
For non-commercial individual, the GNU Lesser General Public License (LGPL 3)  applies.

## Acknowledgments

* Jorj McKie was the motivator behind the entire project. His wxsimpleGUI concepts sparked PySimpleGUI into existence





