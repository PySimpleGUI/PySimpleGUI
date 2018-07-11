# PySimpleGUI

... is a simple GUI, but also powerfully customizable.  It's simple from the programmer's view point.  The idea is to make adding a GUI to a Python program be a simple and trivial task.

I was frustrated by having to deal with the dos prompt when I had a powerful Windows machine right in front of me.  Why is it SO difficult to do even the simplest of input/output to a window in Python??  

Python itself doesn't have a SIMPLE solution... nor did the *many* GUI packages I tried.  Most tried to do TOO MUCH, making it impossible for users to get started quickly.  Others were just plain broken, requiring multiple files or other packages.

The PySimpleGUI solution is focused on the developer.  How can the desired result be achieved in as little and as simple code as possible?  This was the mantra used to create PySimpleGUI.

You can add a GUI to your command line with a single line of code.  With 3 or 4 lines of code you can add a fully custom designed GUI.

The customization power comes from the form/dialog box builder that enables users to experience all of the normal GUI widgets without having to write a lot of code.

Features include:
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
    Scrollable Output    
    Progress Bar
    Async/Non-Blocking Windows
    Persistent Windows
    Redirect Python Output/Errors to scrolling Window
    'Higher level' APIs (e.g. MessageBox, YesNobox, ...)


## Getting Started with PySimpleGUI

To use      `import PySimpleGUI as SG`

For examples download
    
    DisplayHash.py - Shows you how to use the most basic functionality
    ColorDemo.py - COLORS are a big part of the fun of a GUI, right?
    
    HowDoI.py - More advanced 'Chat-style' windows that don't close with button clicks
    

### Prerequisites

Python 3
tkinter

Should run on all Python platforms that have tkinter running on them.  Has been thoroughly tested on Windows.  While not tested elsewhere, should work on Linux, Mac, Pi, etc.

### Installing

    pip install PySimpleGUI
 or
Simply download the file - PySimpleGUI.py and import it into your code

## Running the tests


## Deployment

PySimpleGUI can be broken down into 2 types of API's:
 * High Level single call functions
 * Custom form functions
 

**High Level API Calls**

The classic "input a value, print result" example.
Often command line programs simply take some value as input on the command line, do something with it and then display the results.  Moving from the command line to a GUI is very simple.
This code prompts user to input a line of text and then displays that text in a messages box:

    import PySimpleGUI_local as SG  
      
    rc = SG.GetTextBox('Title', 'Please input something')  
    SG.MsgBox('Results', 'The value returned from GetTextBox', rc)

![GetTextBox](https://user-images.githubusercontent.com/13696193/42592930-1ca1370a-8519-11e8-907e-ad73e9be7749.jpg)

![MsgBox](https://user-images.githubusercontent.com/13696193/42592929-1c7361ae-8519-11e8-8adc-411c1afee69f.jpg)


**Custom Form API Calls**
Here is a complete form - design, display, return information straight into caller's variables

    # -------  Form design ------- #
    layout = [[Text('The SHA-1 Hash for the file')],
              [InputText(), FileBrowse()],
              [Submit(), Cancel()]]
    # -------  Form show  ------- #
    (button, (source_filename,)) = FlexForm('Display A Hash in GooeyGUI', AutoSizeText=True).LayoutAndShow(layout)

Important initial concepts
    Return information from FlexForm, SG's primary form builder interface, is in this format:
    
    (button, (value1, value2, ...))

Don't forget all those ()'s of your values won't be coreectly assigned.

If you have a SINGLE value being returned, it is written this way:

    (button, (value1,))

Forgetting the comma will mess you up but good

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
