
# PySimpleGUI  
  
This really is a simple GUI, but also powerfully customizable.  

![GetTextBox](https://user-images.githubusercontent.com/13696193/42592930-1ca1370a-8519-11e8-907e-ad73e9be7749.jpg)

I was frustrated by having to deal with the dos prompt when I had a powerful Windows machine right in front of me.  Why is it SO difficult to do even the simplest of input/output to a window in Python??    

With a simple GUI, it becomes practical to "associate" .py files with the python interpreter on Windows.  Double click a py file and up pops a GUI window, a much more pleasant experience than opening a dos Window.
  
Python itself doesn't have a simple GUI solution... nor did the *many* GUI packages I tried.  Most tried to do TOO MUCH, making it impossible for users to get started quickly.  Others were just plain broken, requiring multiple files or other packages that were missing.
  
The PySimpleGUI solution is focused on the ***developer***.  How can the desired result be achieved in as little and as simple code as possible?  This was the mantra used to create PySimpleGUI. 
  
You can add a GUI to your command line with a single line of code.  With 3 or 4 lines of code you can add a fully customized GUI.  
  
The customization power comes from the form/dialog box builder that enables users to experience all of the normal GUI widgets without having to write a lot of code.  
  

> Features of PySimpleGUI include:  
>     Text  
>     Single Line Input  
>     Buttons including these types:      File Browse      Folder Browse      Non-closing return      Close form  
>     Checkboxes  
>     Radio Buttons  
>     Icons  
>     Multi-line Text Input  
>     Scroll-able Output      
>     Progress Bar  
>     Async/Non-Blocking Windows  
>     Tabbed forms
>     Persistent Windows  
>     Redirect Python Output/Errors to scrolling Window  
>     'Higher level' APIs (e.g. MessageBox, YesNobox, ...)

  
An example of many widgets used on a single form.  A little further down you'll find the FIFTEEN lines of code required to create this complex form.
![all widgets](https://user-images.githubusercontent.com/13696193/42604818-adb1dd5c-8542-11e8-94cb-575881590f21.jpg)



  
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

To us in your code, simply import....
 `import PySimpleGUI as SG`  

Then use either "high level" API calls or build your own forms.  

    SG.MsgBox('This is my first message box')
![simple msgbox](https://user-images.githubusercontent.com/13696193/42597824-1749b160-8528-11e8-9114-374bf9731b30.jpg)

Yes, it's just that easy to have a window appear on the screen using Python.

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
     
    SG.MsgBox('Variable number of parameters example', my_variable, second_variable, "etc")

Each new item begins on a new line in the Message Box

  ![variablearguments](https://user-images.githubusercontent.com/13696193/42598375-022bc51e-852a-11e8-8f77-4d664ae1a560.jpg)
  
#### Optional Parameters to a Function Call
 
This feature of the Python language is utilized ***heavily*** as a method of customizing forms and part of forms.  Rather than requiring the programmer to specify every possible option for a widget, instead only the options the caller wants to override are specified.

Here is the function definition for the MsgBox function. The details aren't important.  What is important is seeing that there is a long list of potential tweaks that a caller can make.  However, they don't have to be specified on each and every call.  

    def MsgBox(*args, 
               ButtonColor=None, 
               ButtonType=MSG_BOX_OK,  
               AutoClose=False, 
               AutoCloseDuration=None, 
               Icon=DEFAULT_WINDOW_ICON, 
               LineWidth=MESSAGE_BOX_LINE_WIDTH,
               Font=None):

If the caller wanted to change the button color to be black on yellow, the call would look something like this:

    SG.MsgBox('This box has a custom button color',   
              ButtonColor=('black', 'yellow'))

![custombuttoncolor](https://user-images.githubusercontent.com/13696193/42599212-84f3fe2e-852c-11e8-8a60-4aad669a1fd6.jpg)

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

    SG.ScrolledTextBox(my_text, Height=10)

![scrolledtextbox](https://user-images.githubusercontent.com/13696193/42600800-a44f4562-8531-11e8-8c21-51dd70316879.jpg)

Take a moment to look at that last one.  It's such a simple API call and yet the result is awesome.  Rather than seeing text scrolling past on your display, you can capture that text and present it in a scrolled interface.  It's handy enough of an API call that it can also be called using the name `sprint` which is easier to remember than `ScrollectTextBox`. 

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



# Custom Form API Calls

This is the FUN part of the programming of this GUI.  In order to really get the most out of the API, you should be using an IDE that supports auto complete or will show you the definition of the function.  This will make customizing go  smoother.

It's both not enjoyable nor helpful to immediately jump into tweaking each and every little thing available to you.   Let's start with a basic Browse for a file and do something with it.

## COPY THIS DESIGN PATTERN!

    with SG.FlexForm('SHA-1 & 256 Hash', AutoSizeText=True) as form:  
        form_rows = [[SG.Text('SHA-1 and SHA-256 Hashes for the file')],  
                     [SG.InputText(), SG.FileBrowse()],  
                     [SG.Submit(), SG.Cancel()]]  
        (button, (source_filename, )) = form.LayoutAndShow(form_rows)

This context manager contains all of the code needed to specify, show and retrieve results for this form:
![sha hash](https://user-images.githubusercontent.com/13696193/42603149-a56acf3a-853a-11e8-91de-771efd3a65a8.jpg)

It's important to use the "with" context manager.  PySimpleGUI uses `tkinter`.  `tkinter` is very picky about who releases objects and when.  The `with` takes care of disposing of everything properly for you.

You will use this design pattern or code template for all of your "normal" (blocking) types of input forms.  

PySimpleGUI's goal with the API is to be easy on the programmer.  An attempt was made to make the program's code visually match the window on the screen.  The way this is done is that a GUI is broken up into "Rows".  Then each row is broke up into "Elements" or "Widgets".  Each element is specified by names such as Text, Button, Checkbox, etc. 

Some elements are shortcuts, again meant to make it easy on the programmer.  Rather than writing a `Button`, with  name = "Submit", etc, the caller simply writes `Submit`.

Going through each line of code

    with SG.FlexForm('SHA-1 & 256 Hash', AutoSizeText=True) as form:  
This creates a new form, storing it in the variable `form`.  

        form_rows = [[SG.Text('SHA-1 and SHA-256 Hashes for the file')],  
The next few rows of code lay out the rows of elements in the window to be displayed.  The variable `form_rows` holds our entire GUI window.   The first row of this form has a Text element.  These simply display text on the form.

                     [SG.InputText(), SG.FileBrowse()],  
Now we're on the second row of the form.  On this row there are 2 elements.  The first is an `Input` field.  It's a place the user can enter `strings`.  The second element is a `File Browse Button`.  A file or folder browse button will always fill in the text field to it's left unless otherwise specified.  In this example, the File Browse Button will interact with the `InputText` field to its left.

				    [SG.Submit(), SG.Cancel()]]

The last line of the `form_rows` variable assignment contains a Submit and a Cancel Button.  These are buttons that will cause a form to return its valueso the caller.

        (button, (source_filename, )) = form.LayoutAndShow(form_rows)
This is the code that **displays** the form, collects the information and returns the data collected.  In this example we have a button return code and only 1 input field.

## Return values

   Return information from FlexForm, SG's primary form builder interface, is in this format:  
      
    (button, (value1, value2, ...))  
  
Don't forget all those ()'s of your values won't be coreectly assigned.  
  
If you have a SINGLE value being returned, it is written this way:  
  
    (button, (value1,)) = form.LayoutAndShow(form_rows)
 Another way of parsing the return values is to store the list of values into a variable that is then referenced.

     (button, (value)) = form.LayoutAndShow(form_rows)  
     value1 = values[0]
     value2 = values[1]
     ...
     

## All Widgets / Elements
This code utilizes as many of the elements in one form as possible.

    with FlexForm('Everything bagel', AutoSizeText=True, DefaultElementSize=(30,1)) as form:  
        layout = [[Text('Here they all are!', Size=(30,1), Font=("Helvetica", 25), TextColor='red')],  
                  [Text('Here is some text with font sizing', Font=("Helvetica", 15))],  
                  [InputText()],  
                  [Checkbox('My first checkbox!'), Checkbox('My second checkbox!', Default=True)],  
                  [Radio('My first Radio!', "RADIO1", Default=True), Radio('My second checkbox!', "RADIO1")],  
                  [Multiline(DefaultText='This is the DEFAULT text should you decide not to type anything', Scale=(2, 10))],  
                  [InputCombo(['choice 1', 'choice 2'], Size=(20, 3))],  
                  [Text('_'  * 90, Size=(60, 1))],  
                  [Text('Choose Source and Destination Folders', Size=(35,1))],  
                  [Text('Source Folder', Size=(15, 1), AutoSizeText=False), InputText('Source'), FolderBrowse()],  
                  [Text('Destination Folder', Size=(15, 1), AutoSizeText=False), InputText('Dest'), FolderBrowse()],  
                  [SimpleButton('Your Button with any text you want')],  
                  [SimpleButton('Big Text', Size=(12,1), Font=("Helvetica", 20))],  
                  [Submit(), Cancel()]]  
      
        (button, (values)) = form.LayoutAndShow(layout)




        MsgBox('Results', 'You clicked {}'.format(button),'The values returned from form', values , Font = ("Helvetica", 15))

This is a somewhat complex form with quite a bit of custom sizing to make things line up well.  This is code you only have to write once.  When looking at the code, remember that what you're seeing is a list of lists.  Each row contains a list of Graphical Elements that are used to create the form.

![all widgets](https://user-images.githubusercontent.com/13696193/42604818-adb1dd5c-8542-11e8-94cb-575881590f21.jpg)

Clicking the Submit button caused the form call to return.  The call to MsgBox resulted in this dialog box.
![results](https://user-images.githubusercontent.com/13696193/42604952-502f64e6-8543-11e8-8045-bc10d38c5fd4.jpg)

One important aspect of this example is the return codes:

    (button, (values)) = form.LayoutAndShow(layout)
The value for `button` will be the text that is displayed on the button element when it was created.  If the user closed the form using something other than a button, then `button` will be `None`.

You can see in the MsgBox that the values returned are a list.  Each input field in the form generates one item in the return values list.  All input fields return a `string` except for Check Boxes.  These return `bool`.  



# Building Custom Forms
You will find it much easier to write code using PySimpleGUI is you use features that show you documentation about the API call you are making.  In PyCharm 2 commands are helpful.

> Control-Q (when cursor is on function name) brings up a box with the
> function definition 
> Control-P (when cursor inside function call "()")
> shows a list of parameters and their default values

## Synchronous Forms
The most common use of PySimpleGUI is to display and collect information from the user.  The most straightforward way to do this is using a "blocking" GUI call.  Execution is "blocked" while waiting for the user to close the GUI form/dialog box.
You've already seen a number of examples above that use blocking forms.  Anytime you see a context manager used (see the `with` statement) it's most likely a blocking form.  You can examine the show calls to be sure.  If the form is a non-blocking form, it must indicate that in the call to `form.show`.

NON-BLOCKING form call:

		    form.Show(NonBlocking=True)

### Beginning a Form
The first step is to create the form object using the desired form customization.

    with FlexForm('Everything bagel', AutoSizeText=True, DefaultElementSize=(30,1)) as form:  
Let's go through the options available when creating a form.

    def __init__(self, title, 
        DefaultElementSize=(DEFAULT_ELEMENT_SIZE[0], DEFAULT_ELEMENT_SIZE[1]),
        AutoSizeText=DEFAULT_AUTOSIZE_TEXT,
        Scale=(None, None),
        Size=(None, None),
        Location=(None, None),
        ButtonColor=None,Font=None,
        ProgressBarColor=(None,None),
        IsTabbedForm=False,
        BorderDepth=None,
        AutoClose=False,
        AutoCloseDuration=DEFAULT_AUTOCLOSE_TIME,
        Icon=DEFAULT_WINDOW_ICON):
    

#### Sizes
Note several variables that deal with "size".  Element sizes are measured in characters.  A Text Element with a size of 20,1 has a size of 20 characters wide by 1 character tall.

Sizes can be set at the element level, or in this case, the size variables apply to all elements in the form.  Setting `Size=(20,1)` in the form creation call will set all elements in the form to that size.
In addition to `size` there is a `scale` option.  Scale will take the Element's size and scale it up or down depending on the scale value.  `scale=(1,1)` doesn't change the Element's size.  `scale=(2,1)` will set the Element's size to be twice as wide as the size setting.

#### FlexForm - form-level variables overview
A summary of the variables that can be changed when a FlexForm is created

>         DefaultElementSize - set default size for all elements in the form
>         AutoSizeText - true/false autosizing turned on / off
>         Scale - set scale value for all elements
>         ButtonColor - default button color (foreground, background)
>         Font - font name and size for all text items
>         ProgressBarColor - progress bar colors
>         IsTabbedForm - true/false indicates form is a tabbed or normal form
>         BorderDepth - style setting for buttons, input fields
>         AutoClose - true/false indicates if form will automatically close
>         AutoCloseDuration - how long in seconds before closing form
>         Icon - filename for icon that's displayed on the window on taskbar

## Built With  
  
  
## Contributing  
  
A MikeTheWatchGuy production... entirely responsible for this code  
  
## Versioning  
  
1.0.9 - July 10, 2018 - Initial Release  
      
  
## Authors  
  
  
## License  
  
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details  
  
## Acknowledgments  
  
* Jorj McKie was the motivator behind the entire project. His wxsimpleGUI concepts sparked PySimpleGUI into existence





