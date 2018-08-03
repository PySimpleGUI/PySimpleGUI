.. figure:: https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png
   :alt: pysimplegui\_logo

   pysimplegui\_logo
|Downloads| since Jul 11, 2018 # PySimpleGUI (Ver 2.7)

Super-simple GUI to grasp... Powerfully customizable.

Note - *Python3* is required to run PySimpleGUI. It takes advantage of
some Python3 features that do not translate well into Python2.

Looking to take your Python code from the world of command lines and
into the convenience of a GUI? Have a Raspberry Pi with a touchscreen
that's going to waste because you don't have the time to learn a GUI
SDK? Look no further, you've found your GUI package.

::

    import PySimpleGUI as sg

    sg.MsgBox('Hello From PySimpleGUI!', 'This is the shortest GUI program ever!')

.. figure:: https://user-images.githubusercontent.com/13696193/43162494-33095ece-8f59-11e8-86de-b6d8bcc5a52f.jpg
   :alt: snap0136

   snap0136
Build beautiful customized forms that fit your specific problem. Let
PySimpleGUI solve your GUI problem while you solve the real problems. Do
you really want to plod through the mountains of code required to
program tkinter?

.. figure:: https://user-images.githubusercontent.com/13696193/43273880-aa1955e6-90cb-11e8-94b6-673ecdb2698c.jpg
   :alt: snap0156

   snap0156
Perhaps you're looking for a way to interact with your Raspberry Pi in a
more friendly way. The is the same form as above, except shown on a Pi.

.. figure:: https://user-images.githubusercontent.com/13696193/43298356-9cfe9008-9123-11e8-9612-14649a2f6c7f.jpg
   :alt: raspberry pi

   raspberry pi
In addition to a primary GUI, you can add a Progress Meter to your code
with ONE LINE of code. Slide this into any of your ``for`` loops and get
a nice meter like this:

::

    EasyProgressMeter('My meter title', current_value, max value)

.. figure:: https://user-images.githubusercontent.com/13696193/42695896-a37eff5c-8684-11e8-8fbb-3d756655a44b.jpg
   :alt: progress meter 2

   progress meter 2
You can build an async media player GUI with custom buttons in 30 lines
of code.

.. figure:: https://user-images.githubusercontent.com/13696193/43161977-9ee7cace-8f57-11e8-8ff8-3ea24b69dab9.jpg
   :alt: media file player

   media file player
I was frustrated by having to deal with the dos prompt when I had a
powerful Windows machine right in front of me. Why is it SO difficult to
do even the simplest of input/output to a window in Python??

There are a number of 'easy to use' Python GUIs, but they're **very**
limiting. PySimpleGUI takes the best of packages like ``EasyGUI``\ and
``WxSimpleGUI`` , both really handy but limited. The primary difference
between these and PySimpleGUI is that in addition to getting the simple
Message Boxes you also get the ability to make your own forms that are
highly customizeable. Don't like the standard Message Box? Then make
your own!

Every call has optional parameters so that you can change the look and
feel. Don't like the button color? It's easy to change by adding a
button\_color parameter to your widget.

GUI Packages with more functionality, like QT and WxPython, require
configuring and can take a ***week*** to get *reasonably familiar* with
the interfaces. Clearly there needs to be a middle ground between forms
with 1 or two input fields and a full-blown GUI. You'll be making your
own custom forms with PySimpleGUI within minutes, even Async forms.

With a simple GUI, it becomes practical to "associate" .py files with
the python interpreter on Windows. Double click a py file and up pops a
GUI window, a more pleasant experience than opening a dos Window and
typing a command line.

The ``PySimpleGUI`` package is focused on the ***developer***. How can
the desired result be achieved in as little and as simple code as
possible? This was the mantra used to create PySimpleGUI. How can it be
done is a Python-like way?

::

    Features of PySimpleGUI include:
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
        Icons
        Multi-line Text Input
        Scroll-able Output
        Images
        Progress Bar
        Async/Non-Blocking Windows
        Tabbed forms
        Persistent Windows
        Redirect Python Output/Errors to scrolling window
        'Higher level' APIs (e.g. MessageBox, YesNobox, ...)
        Single-Line-Of-Coide Proress Bar & Debug Print
        Complete control of colors, look and feel
        Button images

An example of many widgets used on a single form. A little further down
you'll find the TWENTY lines of code required to create this complex
form. Try it if you don't believe it. Start Python, copy and paste the
code below into the >>> prompt and hit enter. This will pop up...

.. figure:: https://user-images.githubusercontent.com/13696193/43097412-0a4652aa-8e8a-11e8-8e09-939484e3c568.jpg
   :alt: everything example

   everything example
Here is the code that produced the above screenshot.

::

    import PySimpleGUI as SG

    with SG.FlexForm('Everything bagel', auto_size_text=True, default_element_size=(40, 1)) as form:
        layout = [
            [SG.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
            [SG.Text('Here is some text.... and a place to enter text')],
            [SG.InputText()],
            [SG.Checkbox('My first checkbox!'), SG.Checkbox('My second checkbox!', default=True)],
            [SG.Radio('My first Radio!     ', "RADIO1", default=True), SG.Radio('My second Radio!', "RADIO1")],
            [SG.Multiline(default_text='This is the default Text shoulsd you decide not to type anything',
                          scale=(2, 10))],
            [SG.InputCombo(['Combobox 1', 'Combobox 2'], size=(20, 3)),
             SG.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],
            [SG.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6)),
             SG.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=25),
             SG.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=75),
             SG.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=10)],
            [SG.Text('_'  * 100, size=(70, 1))],
            [SG.Text('Choose Source and Destination Folders', size=(35, 1))],
            [SG.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), SG.InputText('Source'), SG.FolderBrowse()],
            [SG.Text('Destination Folder', size=(15, 1), auto_size_text=False, justification='right'), SG.InputText('Dest'),
             SG.FolderBrowse()],
            [SG.Submit(), SG.Cancel(), SG.SimpleButton('Customized', button_color=('white', 'green'))]
             ]

    button, values = form.LayoutAndRead(layout)

**A note on screen shots** You will see a number of different styles of
buttons, data entry fields, etc, in this readme. They were all made with
the same SDK, the only difference is in the settings that are specified
on a per-element, row, form, or global basis. One setting in particular,
border\_width, can make a big difference on the look of the form. Some
of the screenshots had a border\_width of 6, others a value of 1.

APIs
----

PySimpleGUI can be broken down into 2 types of API's: \* High Level
single call functions \* Custom form functions

Python Language Features
~~~~~~~~~~~~~~~~~~~~~~~~

There are a couple of Python language features that PySimpleGUI utilizes
heavily that should be understood first... \* Variable number of
arguments to a function call \* Optional parameters to a function call

Variable Number of Arguments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The "High Level" API calls that *output* values take a variable number
of arguments so that they match a "print" statement as much as possible.
The idea is to make it simple for the programmer to output as many items
as desired and in any format. The user need not convert the variables to
be output into the strings. The PySimpleGUI functions do that for the
user.

::

    SG.MsgBox('Variable number of parameters example', var1, var2, "etc")

Each new item begins on a new line in the Message Box

.. figure:: https://user-images.githubusercontent.com/13696193/42844739-ebea22ac-89e1-11e8-8dd1-e61441325701.jpg
   :alt: snap0104

   snap0104
Optional Parameters to a Function Call
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This feature of the Python language is utilized ***heavily*** as a
method of customizing forms and form Elements. Rather than requiring the
programmer to specify every possible option for a widget, instead only
the options the caller wants to override are specified.

Here is the function definition for the MsgBox function. The details
aren't important. What is important is seeing that there is a long list
of potential tweaks that a caller can make. However, they don't *have*
to be specified on each and every call.

::

    def MsgBox(*args,
               button_color=None,
               button_type=MSG_BOX_OK,
               auto_close=False,
               auto_close_duration=None,
               icon=DEFAULT_WINDOW_ICON,
               line_width=MESSAGE_BOX_LINE_WIDTH,
               font=None):

If the caller wanted to change the button color to be black on yellow,
the call would look something like this:

::

    SG.MsgBox('This box has a custom button color',
              button_color=('black', 'yellow'))

.. figure:: https://user-images.githubusercontent.com/13696193/42844830-2d7e8b9a-89e2-11e8-8ef4-5af9e36f30f3.jpg
   :alt: snap0105

   snap0105

--------------

High Level API Calls
~~~~~~~~~~~~~~~~~~~~

The classic "input a value, print result" example. Often command line
programs simply take some value as input on the command line, do
something with it and then display the results. Moving from the command
line to a GUI is very simple. This code prompts user to input a line of
text and then displays that text in a messages box:

::

    import PySimpleGUI_local as SG

    rc = SG.GetTextBox('Title', 'Please input something')
    SG.MsgBox('Results', 'The value returned from GetTextBox', rc)

.. figure:: https://user-images.githubusercontent.com/13696193/42592930-1ca1370a-8519-11e8-907e-ad73e9be7749.jpg
   :alt: GetTextBox

   GetTextBox
.. figure:: https://user-images.githubusercontent.com/13696193/42592929-1c7361ae-8519-11e8-8adc-411c1afee69f.jpg
   :alt: MsgBox

   MsgBox
Message Boxes
^^^^^^^^^^^^^

In addition to MsgBox, you'll find a several API calls that are
shortcuts to common messages boxes. You can achieve similar results by
calling MsgBox with the correct parameters.

The differences tend to be the number and types of buttons. Here are the
calls and the windows that are created.

::

    import PySimpleGUI as SG

``SG.MsgBoxOK('This is an OK MsgBox')``

.. figure:: https://user-images.githubusercontent.com/13696193/42599852-8dd6914e-852e-11e8-888f-f133d787210b.jpg
   :alt: msgboxok

   msgboxok
::

    SG.MsgBoxOKCancel('This is an OK Cancel MsgBox')

.. figure:: https://user-images.githubusercontent.com/13696193/42599858-8e8eff22-852e-11e8-8d5c-3fe99237eb7f.jpg
   :alt: msgboxokcancel

   msgboxokcancel
::

    SG.MsgBoxCancel('This is a Cancel MsgBox')

.. figure:: https://user-images.githubusercontent.com/13696193/42599857-8e53dc4e-852e-11e8-8e83-6a8cccf8e706.jpg
   :alt: msgboxcancel

   msgboxcancel
::

    SG.MsgBoxYesNo('This is a Yes No MsgBox')

.. figure:: https://user-images.githubusercontent.com/13696193/42599856-8e304540-852e-11e8-975d-fb2b62e94300.jpg
   :alt: msgboxyesno

   msgboxyesno
::

    SG.MsgBoxError('This is an error MsgBox')

.. figure:: https://user-images.githubusercontent.com/13696193/42599853-8df8e078-852e-11e8-90dc-7815d69bff7e.jpg
   :alt: msgbox error

   msgbox error
::

    SG.MsgBoxAutoClose('This is an autoclose MsgBox')

.. figure:: https://user-images.githubusercontent.com/13696193/42599855-8e147572-852e-11e8-8c23-7ec771909062.jpg
   :alt: msgbox autoclose

   msgbox autoclose
::

    SG.ScrolledTextBox(my_text, height=10)

.. figure:: https://user-images.githubusercontent.com/13696193/42600800-a44f4562-8531-11e8-8c21-51dd70316879.jpg
   :alt: scrolledtextbox

   scrolledtextbox
Take a moment to look at that last one. It's such a simple API call and
yet the result is awesome. Rather than seeing text scrolling past on
your display, you can capture that text and present it in a scrolled
interface. It's handy enough of an API call that it can also be called
using the name ``sprint`` which is easier to remember than
``ScrollectTextBox``. Your code could contain a line like:

::

    sprint(f'My variables values include x={x}', f'y={y}')

This becomes a debug print of sorts that will route to a scrolled
window.

High Level User Input
^^^^^^^^^^^^^^^^^^^^^

There are 3 very basic user input high-level function calls. It's
expected that for most applications, a custom input form will be
created. If you need only 1 value, then perhaps one of these high level
functions will work. - GetTextBox - GetFileBox - GetFolderBox

``submit_clicked, value = SG.GetTextBox('Title', 'Please enter anything')``

.. figure:: https://user-images.githubusercontent.com/13696193/42600399-1ef66a5e-8530-11e8-9bc4-78ea839213cd.jpg
   :alt: gettextbox

   gettextbox
::

    submit_clicked, value = SG.GetFileBox('Title', 'Choose a file')

.. figure:: https://user-images.githubusercontent.com/13696193/42600398-1ed8a122-8530-11e8-9f74-88b101efcea4.jpg
   :alt: getfilebox

   getfilebox
::

    submit_clicked, value = SG.GetPathBox('Title', 'Choose a folder')

.. figure:: https://user-images.githubusercontent.com/13696193/42600397-1ea7cef8-8530-11e8-8d43-e1000c0933cd.jpg
   :alt: getfolderbox

   getfolderbox
Progress Meter!
^^^^^^^^^^^^^^^

We all have loops in our code. 'Isn't it joyful waiting, watching a
counter scrolling past in a text window? How about one line of code to
get a progress meter, that contains statistics about your code?

.. figure:: https://user-images.githubusercontent.com/13696193/42696332-dca3ca6e-8685-11e8-846b-6bee8362ee5f.jpg
   :alt: progress meter 3

   progress meter 3
::

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

::

    for i in range(1,10000):
        SG.EasyProgressMeter('My Meter', i+1, 10000, 'Optional message')

That line of code resulted in this window popping up and updating.

.. figure:: https://user-images.githubusercontent.com/13696193/42696912-a5c958b8-8687-11e8-9a7d-a390a465407a.jpg
   :alt: progress meter 5

   progress meter 5
A meter AND fun statistics to watch while your machine grinds away, all
for the price of 1 line of code. With a little trickery you can provide
a way to break out of your loop using the Progress Meter form. The
cancel button results in a ``False`` return value from
``EasyProgressMeter``. It normally returns ``True``.

::

    if not SG.EasyProgressMeter('My Meter', i+1, 10000, 'Optional message'):
       break

***Be sure and add one to your loop counter*** so that your counter goes
from 1 to the max value. If you do not add one, your counter will never
hit the max value. Instead it will go from 0 to max-1. #### Debug Output
Another call in the 'Easy' families of APIs is ``EasyPrint``. It will
output to a debug window. If the debug window isn't open, then the first
call will open it. No need to do anything but stick a 'print' call in
your code. You can even replace your 'print' calls with calls to
EasyPrint by simply sticking the statement

::

    print = SG.EasyPrint

at the top of your code. There are a number of names for the same
EasyPrint function. ``Print`` is one of the better ones to use as it's
easy to remember. It is simply ``print`` with a capital P.

::

    import PySimpleGUI as SG

    for i in range(100):
        SG.Print(i)

|snap0125| Or if you didn't want to change your code:

::

    import PySimpleGUI as SG

    print=SG.Print
    for i in range(100):
        print(i)

Just like the standard print call, ``EasyPrint`` supports the ``sep``
and ``end`` keyword arguments. Other names that can be used to call
``EasyPrint`` include Print, ``eprint``, If you want to close the
window, call the function ``EasyPrintClose``.

A word of caution. There are known problems when multiple PySimpleGUI
windows are opened, particularly if the user closes them in an unusual
way. Not a reason to stay away from using it. Just something to keep in
mind if you encounter a problem.

You can change the size of the debug window using the ``SetOptions``
call with the ``debug_win_size`` parameter.

All Widgets / Elements
----------------------

This code utilizes as many of the elements in one form as possible.

::

     with SG.FlexForm('Everything bagel', auto_size_text=True, default_element_size=(40, 1)) as form:
        layout = [
            [SG.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
            [SG.Text('Here is some text.... and a place to enter text')],
            [SG.InputText()],
            [SG.Checkbox('My first checkbox!'), SG.Checkbox('My second checkbox!', default=True)],
            [SG.Radio('My first Radio!     ', "RADIO1", default=True), SG.Radio('My second Radio!', "RADIO1")],
            [SG.Multiline(default_text='This is the default Text shoulsd you decide not to type anything',
                          scale=(2, 10))],
            [SG.InputCombo(['Combobox 1', 'Combobox 2'], size=(20, 3)),
             SG.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],
            [SG.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6)),
             SG.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=25),
             SG.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=75),
             SG.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=10)],
            [SG.Text('_'  * 100, size=(70, 1))],
            [SG.Text('Choose Source and Destination Folders', size=(35, 1))],
            [SG.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), SG.InputText('Source'), SG.FolderBrowse()],
            [SG.Text('Destination Folder', size=(15, 1), auto_size_text=False, justification='right'), SG.InputText('Dest'),
             SG.FolderBrowse()],
            [SG.Submit(), SG.Cancel(), SG.SimpleButton('Customized', button_color=('white', 'green'))]
             ]

         button, values = form.LayoutAndRead(layout)

This is a somewhat complex form with quite a bit of custom sizing to
make things line up well. This is code you only have to write once. When
looking at the code, remember that what you're seeing is a list of
lists. Each row contains a list of Graphical Elements that are used to
create the form.

.. figure:: https://user-images.githubusercontent.com/13696193/43097412-0a4652aa-8e8a-11e8-8e09-939484e3c568.jpg
   :alt: everything example

   everything example
Clicking the Submit button caused the form call to return. The call to
MsgBox resulted in this dialog box. |results 2|

**``Note, button value can be None``**. The value for ``button`` will be
the text that is displayed on the button element when it was created. If
the user closed the form using something other than a button, then
``button`` will be ``None``.

You can see in the MsgBox that the values returned are a list. Each
input field in the form generates one item in the return values list.
All input fields return a ``string`` except for Check Boxes and Radio
Buttons. These return ``bool``.

ProgressBar
^^^^^^^^^^^

The ``ProgressBar`` element is used to build custom Progress Bar forms.
It is HIGHLY recommended that you use the functions that provide a
complete progress meter solution for you. Progress Meters are not easy
to work with because the forms have to be non-blocking and they are
tricky to debug.

The **easiest** way to get progress meters into your code is to use the
``EasyProgessMeter`` API. This consists of a pair of functions,
``EasyProgessMeter`` and ``EasyProgressMeterCancel``. You can easily
cancel any progress meter by calling it with the current value = max
value. This will mark the meter as expired and close the window. You've
already seen EasyProgressMeter calls presented earlier in this readme.

::

    SG.EasyProgressMeter('My Meter', i+1, 1000, 'Optional message')

The return value for ``EasyProgressMeter`` is: ``True`` if meter updated
correctly ``False`` if user clicked the Cancel button, closed the form,
or vale reached the max value. **Customized Progress Bar** If you want a
bit more customization of your meter, then you can go up 1 level and use
the calls to ``ProgressMeter`` and ``ProgressMeterUpdate``. These APIs
behave like an object we're all used to. First you create the
``ProgressMeter`` object, then you call the ``Update`` method to update
it.

You setup the progress meter by calling

::

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

::

    return_code = ProgressMeterUpdate(my_meter,
                                     value,
                                     *args):

Putting it all together you get this design pattern

::

    my_meter = SG.ProgressMeter('Meter Title', 100000, orentation='Vert')

    for i in range(0, 100000):
        SG.ProgressMeterUpdate(my_meter, i+1, 'Some variable', 'Another variable')

The final way of using a Progress Meter with PySimpleGUI is to build a
custom form with a ``ProgressBar`` Element in the form. You will need to
run your form as a non-blocking form. When you are ready to update your
progress bar, you call the ``UpdateBar`` method for the ``ProgressBar``
element itself.

Output
^^^^^^

The Output Element is a re-direction of Stdout. Anything "printed" will
be displayed in this element.

::

    Output(scale=(None, None),
           size=(None, None))

Here's a complete solution for a chat-window using an Async form with an
Output Element

::

    import PySimpleGUI as SG
        # Blocking form that doesn't close
    def ChatBot():
        with SG.FlexForm('Chat Window', auto_size_text=True, default_element_size=(30, 2)) as form:
            layout = [[(SG.Text('This is where standard out is being routed', size=[40, 1]))],
                        [SG.Output(size=(80, 20))],
                        [SG.Multiline(size=(70, 5), enter_submits=True), SG.ReadFormButton('SEND', button_color=(SG.YELLOWS[0], SG.BLUES[0])), SG.SimpleButton('EXIT', button_color=(SG.YELLOWS[0], SG.GREENS[0]))]]
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

Tabbed Forms
------------

Tabbed forms are shown using the ``ShowTabbedForm`` call. The call has
the format

::

     results = ShowTabbedForm('Title for the form',
                              (form,layout,'Tab 1 label'),
                              (form2,layout2, 'Tab 2 label'), ...)

Each of the tabs of the form is in fact a form. The same steps are taken
to create the form as before. A ``FlexForm`` is created, then rows are
filled with Elements, and finally the form is shown. When calling
``ShowTabbedForm``, each form is passed in as a tuple. The tuple has the
format: ``(the form, the rows, a string shown on the tab)``

Results are returned as a list of lists. For each form you'll get a list
that's in the same format as a normal form. A single tab's values would
be:

::

    (button, (values))

Recall that values is a list as well. Multiple tabs in the form would
return like this:

::

    ((button1, (values1)), (button2, (values2))

## Colors ## Starting in version 2.5 you can change the background
colors for the window and the Elements.

Your forms can go from this: |snap0155|

to this... with one function call...

.. figure:: https://user-images.githubusercontent.com/13696193/43273880-aa1955e6-90cb-11e8-94b6-673ecdb2698c.jpg
   :alt: snap0156

   snap0156
While you can do it on an element by element or form level basis, the
easiest way, by far, is a call to ``SetOptions``.

Be aware that once you change these options they are changed for the
rest of your program's execution. All of your forms will have that look
and feel, until you change it to something else (which could be the
system default colors.

This call sets all of the different color options.

::

    SetOptions(background_color='#9FB8AD',
               text_element_background_color='#9FB8AD',
               element_background_color='#9FB8AD',
               scrollbar_color=None,
               input_elements_background_color='#F7F3EC',
               progress_meter_color = ('green', 'blue')
               button_color=('white','#475841'))

Global Settings
---------------

**Global Settings** Let's have some fun customizing! Make PySimpleGUI
look the way you want it to look. You can set the global settings using
the function ``PySimpleGUI.SetOptions``. Each option has an optional
parameter that's used to set it.

::

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
               background_color=None
               element_background_color=None
               text_element_background_color=None
               input_elements_background_color=None
               scrollbar_color=None, text_color=None
               debug_win_size=(None,None)
               window_location=(None,None)

Explanation of parameters

::

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
             scrollbar_color - Color for scrollbars (may not always work)
             text_color - Text element default text color
             text_justification - justification to use on Text Elements. Values are strings - 'left', 'right', 'center'
             debug_win_size - size of the Print output window
             window_location - location on the screen (x,y) of window's top left cornder

These settings apply to all forms ``SetOptions``. The Row options and
Element options will take precedence over these settings. Settings can
be thought of as levels of settings with the Form-level being the
highest and the Element-level the lowest. Thus the levels are:

-  Form level
-  Row level
-  Element level

Each lower level overrides the settings of the higher level. Once
settings have been changed, they remain changed for the duration of the
program (unless changed again).

Asynchronous (Non-Blocking) Forms
---------------------------------

So you want to be a wizard do ya? Well go boldly! While the majority of
GUIs are a simple exercise to "collect input values and return with
them", there are instances where we want to continue executing while the
form is open. These are "asynchronous" forms and require special
options, new SDK calls, and **great care**. With asynchronous forms the
form is shown, user input is read, but your code keeps right on
chugging. YOUR responsibility is to call ``PySimpleGUI.ReadNonBlocking``
on a periodic basis. Once a second or more will produce a reasonably
snappy GUI.

When do you use a non-blocking form? A couple of examples are \* A media
file player like an MP3 player \* A status dashboard that's periodically
updated \* Progress Meters - when you want to make your own progress
meters \* Output using print to a scrolled text element. Good for
debugging.

Word of warning... version 2.2, the currently released, and upcoming
version 2.3 differ in the return code for the ``ReadNonBlocking`` call.
Previously the function returned 2 values, except when the form is
closed using the "X" which returned a single value of ``None``. The
*new* way is that ``ReadNonBlocking`` always returns 2 values. If the
user closed the form with the "X" then the return values will be None,
None. You will want to key off the second value to catch this case. The
proper code to check if the user has exited the form will be a
polling-loop that looks something like this:

::

    while True:
       button, values = form.ReadNonBlocking()
       if values is None or button == 'Quit':
          break

We're going to build an app that does the latter. It's going to update
our form with a running clock.

The basic flow and functions you will be calling are: Setup

::

    form = FlexForm()
    form_rows = .....
    form.LayoutAndRead(form_rows, non_blocking=True)

Periodic refresh

::

    form.ReadNonBlocking()

If you need to close the form

::

    form.CloseNonBlockingForm()

Rather than the usual ``form.LayoutAndRead()`` call, we're manually
adding the rows (doing the layout) and then showing the form. After the
form is shown, you simply call ``form.ReadNonBlocking()`` every now and
then.

When you are ready to close the form (assuming the form wasn't closed by
the user or a button click) you simply call
``form.CloseNonBlockingForm()``

**Example - Running timer that updates** See the sample code on the
GitHub named Demo Media Player for another example of Async Forms. We're
going to make a form and update one of the elements of that form every
.01 seconds. Here's the entire code to do that.

::

    import PySimpleGUI as sg
    import time

    # form that doesn't block
    # Make a form, but don't use context manager
    form = sg.FlexForm('Running Timer', auto_size_text=True)
    # Create a text element that will be updated with status information on the GUI itself
    output_element = sg.Text('', size=(8, 2), font=('Helvetica', 20))
    # Create the rows
    form_rows = [[sg.Text('Non-blocking GUI with updates')],
                 [output_element],
                 [sg.SimpleButton('Quit')]]
    # Layout the rows of the form and perform a read. Indicate the form is non-blocking!
    form.LayoutAndRead(form_rows, non_blocking=True)

    #
    # Some place later in your code...
    # You need to perform a ReadNonBlocking on your form every now and then or
    # else it won't refresh
    #

    for i in range(1, 1000):
        output_element.Update('{:02d}:{:02d}.{:02d}'.format(*divmod(int(i / 100), 60), i % 100))
        button, values = form.ReadNonBlocking()
        if values is None or button == 'Quit':
            break
        time.sleep(.01)
    else:
        form.CloseNonBlockingForm()

What we have here is the same sequence of function calls as in the
description. Get a form, add rows to it, show the form, and then refresh
it every now and then.

The new thing in this example is the call use of the Update method for
the Text Element. The first thing we do inside the loop is "update" the
text element that we made earlier. This changes the value of the text
field on the form. The new value will be displayed when
``form.ReadNonBlocking()`` is called.

Note the ``else`` statement on the for loop. This is needed because
we're about to exit the loop while the form is still open. The user has
not closed the form using the X nor a button so it's up to the caller to
close the form using ``CloseNonBlockingForm``.

That's it... this example follows the async design pattern well.

Sample Applications
-------------------

Use the example programs as a starting basis for your GUI. Copy, paste,
modify and run! The demo files are:

``Demo Recipes.py`` - Sample forms for all major form types and
situations. This is the place to get your code template from. Includes
asynchronous forms, etc.

``Demo DisplayHash1and256.py`` - Demonstrates using High Level API calls
to get a filename

``Demo DupliucateFileFinder.py`` - Demonstrates High Level API to get a
folder & Easy Progress Meter to show progress of the file scanning

``Demo HowDoI.py`` - An amazing little application. Acts as a front-end
to HowDoI. This one program could forever change how you code. It does
searches on Stack Overflow and returns the CODE found in the best answer
for your query. If anyone wants to help me package this application up,
I could use a hand.

Fun Stuff
---------

Here are some things to try if you're bored or want to further customize

**Colors - Random and predefined** To set a button or text to a random
color, use the string ``'random'`` as the color value. You can also call
``PySimpleGUI.GetRandomColor``. To get a random color pair call
``PySimpleGUI.GetRandomColorPair``. This returns a tuple containing a
random color and that color's compliment.

**Debug Output** Be sure and check out the EasyPrint (Print) function
described in the high-level API section. Leave your code the way it is,
route your stdout and stderror to a scrolling window.

For a fun time, add these lines to the top of your script

::

    import PySimpleGUI as sg
    print = sg.Print

This will turn all of your print statements into prints that display in
a window on your screen rather than to the terminal.

**Look and Feel** Dial in the look and feel that you like with the
``SetOptions`` function. You can change all of the defaults in one
function call. One line of code to customize the entire GUI.

**ObjToString** Ever wanted to easily display an objects contents
easily? Use ObjToString to get a nicely formatted recursive walk of your
objects. This statement:

::

    print(sg.ObjToSting(x))

And this was the output

::

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

--------------

Known Issues
============

While not an "issue" this is a ***stern warning***

**Do not attempt** to call ``PySimpleGUI`` from multiple threads! It's ``tkinter`` based and ``tkinter`` has issues with multiple threads
-----------------------------------------------------------------------------------------------------------------------------------------

**Progress Meters** - the visual graphic portion of the meter may be
off. May return to the native tkinter progress meter solution in the
future. Right now a "custom" progress meter is used. On the bright side,
the statistics shown are extremely accurate and can tell you something
about the performance of your code.

**Async Forms** - these include the 'easy' forms (EasyProgressMeter and
EasyPrint/Print). If you start overlapping having Async forms open with
normal forms then things get a littler squirrelly. Still tracking down
the issues and am making it more solid every day possible. You'll know
there's an issue when you see blank form.

**EasyPrint** - EasyPrint is a new feature that's pretty awesome. You
print and the output goes to a window, with a scroll bar, that you can
copy and paste from. Being a new feature, it's got some potential
problems. There are known interaction problems with other GUI windows.
For example, closing a Print window can also close other windows you
have open. For now, don't close your debug print window until other
windows are closed too.

Contributing
------------

A MikeTheWatchGuy production... entirely responsible for this code....
unless it causes you trouble in which case I'm not at all responsible.

Versions
--------

+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Version   | Description                                                                                                                                      |
+===========+==================================================================================================================================================+
| 1.0.9     | July 10, 2018 - Initial Release                                                                                                                  |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 1.0.21    | July 13, 2018 - Readme updates                                                                                                                   |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 2.0.0     | July 16, 2018 - ALL optional parameters renamed from CamelCase to all\_lower\_case                                                               |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 2.1.1     | July 18, 2018 - Global settings exposed, fixes                                                                                                   |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 2.2.0     | July 20, 2018 - Image Elements, Print output                                                                                                     |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 2.3.0     | July 23, 2018 - Changed form.Read return codes, Slider Elements, Listbox element. Renamed some methods but left legacy calls in place for now.   |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 2.4.0     | July 24, 2018 - Button images. Fixes so can run on Raspberry Pi                                                                                  |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 2.5.0     | July 26, 2018 - Colors. Listbox scrollbar. tkinter Progress Bar instead of homegrown.                                                            |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 2.6.0     | July 27, 2018 - auto\_size\_button setting. License changed to LGPL 3+                                                                           |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 2.6.5     | Aug XX, 2018 - window\_location default setting                                                                                                  |
+-----------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Release Notes
~~~~~~~~~~~~~

2.3 - Sliders, Listbox's and Image elements (oh my!)

If using Progress Meters, avoid cancelling them when you have another
window open. It could lead to future windows being blank. It's being
worked on.

New debug printing capability. ``sg.Print``

2.5 Discovered issue with scroll bar on ``Output`` elements. The bar
will match size of ROW not the size of the element. Normally you never
notice this due to where on a form the ``Output`` element goes.

Listboxes are still without scrollwheels. The mouse can drag to see more
items. The mouse scrollwheel will also scroll the list and will
``page up`` and ``page down`` keys.

Upcoming
~~~~~~~~

Make suggestions people! Future release features

Columns. How multiple columns would be specified in the SDK interface
are still being designed.

Port to other graphic engines. Hook up the front-end interface to a
backend other than tkinter. Qt, WxPython, etc.

Code Condition
--------------

::

    Make it run
    Make it right
    Make it fast

It's a recipe for success if done right. PySimpleGUI has completed the
"Make it run" phase. It's far from "right" in many ways. These are being
worked on. The module is particularly poor for PEP 8 compliance. It was
a learning exercise that turned into a somewhat complete GUI solution
for lightweight problems.

While the internals to PySimpleGUI are a tad sketchy, the public
interfaces into the SDK are more strictly defined and comply with PEP 8
for the most part.

Please log bugs and suggestions in the GitHub! It will only make the
code stronger and better in the end, a good thing for us all, right?

Design
------

A moment about the design-spirit of ``PySimpleGUI``. From the beginning,
this package was meant to take advantage of Python's capabilities with
the goal of programming ease.

**Single File** While not the best programming practice, the
implementation resulted in a single file solution. Only one file is
needed, PySimpleGUI.py. You can post this file, email it, and easily
import it using one statement.

**Functions as objects** In Python, functions behave just like object.
When you're placing a Text Element into your form, you may be sometimes
calling a function and other times declaring an object. If you use the
word Text, then you're getting an object. If you're using ``Txt``, then
you're calling a function that returns a ``Text`` object.

**Lists** It seemed quite natural to use Python's powerful list
constructs when possible. The form is specified as a series of lists.
Each "row" of the GUI is represented as a list of Elements. When the
form read returns the results to the user, all of the results are
presented as a single list. This makes reading a form's values
super-simple to do in a single line of Python code.

Authors
-------

MikeTheWatchGuy

License
-------

GNU Lesser General Public License (LGPL 3) +

Acknowledgments
---------------

-  Jorj McKie was the motivator behind the entire project. His
   wxsimpleGUI concepts sparked PySimpleGUI into existence
-  `Fredrik Lundh <https://wiki.python.org/moin/FredrikLundh>`__ for his
   work on ``tkinter``

How Do I
--------

Finally, I must thank the fine folks at How Do I.
https://github.com/gleitz/howdoi Their utility has forever changed the
way and pace in which I can program. I urge you to try the HowDoI.py
application here on GitHub. Trust me, **it's going to be worth the
effort!** Here are the steps to run that application

::

    Install howdoi:
          pip install howdoi
    Test your install:
          python -m howdoi howdoi.py
    To run it:
          Python HowDoI.py

The pip command is all there is to the setup.

The way HowDoI works is that it uses your search term to look through
stack overflow posts. It finds the best answer, gets the code from the
answer, and presents it as a response. It gives you the correct answer
OFTEN. It's a miracle that it work SO well. For Python questions, I
simply start my query with 'Python'. Let's say you forgot how to reverse
a list in Python. When you run HowDoI and ask this question, this is
what you'll see. |snap0109|

In the hands of a competent programmer, this tool is **amazing**. It's a
must-try kind of program that has completely changed my programming
process. I'm not afraid of asking for help! You just have to be smart
about using what you find.

The PySimpleGUI window that the results are shown in is an 'input' field
which means you can copy and paste the results right into your code.

.. |Downloads| image:: http://pepy.tech/badge/pysimplegui
   :target: http://pepy.tech/project/pysimplegui
.. |snap0125| image:: https://user-images.githubusercontent.com/13696193/43114979-a696189e-8ecf-11e8-83c7-473fcf0ccc66.jpg
.. |results 2| image:: https://user-images.githubusercontent.com/13696193/43097502-44e3ed32-8e8a-11e8-9a51-2b8af0b1a682.jpg
.. |snap0155| image:: https://user-images.githubusercontent.com/13696193/43273879-a9fdc10a-90cb-11e8-8c20-4f6a244ebe2f.jpg
.. |snap0109| image:: https://user-images.githubusercontent.com/13696193/42916444-4199b16c-8ad3-11e8-8423-d12e61a58d3d.jpg
