

  
    
      
      
      
      
![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)      
      
[![Downloads](http://pepy.tech/badge/pysimpleguiqt)](http://pepy.tech/project/pysimplegui)      

    
 ![Awesome Meter](https://img.shields.io/badge/Awesome_meter-1000-yellow.svg)
       
 ![Python Version](https://img.shields.io/badge/Python-3.x-yellow.svg)      
      
      
      
      
      
      
# PySimpleGUIQt      
      
      
## The Pre-Alpha Release   
      
[Announcements of Latest Developments](https://github.com/MikeTheWatchGuy/PySimpleGUI/issues/142)      
            

      
  -----      
## Getting Started with PySimpleGUIQt

Welcome to the Pre-Alpha Release of PySimpleGUI for Qt!

You can use the exact same code that you are running on the older, tkinter, version of PySimpleGUI.  

PySimpleGUIQt uses **PySide2** for access to Qt.

### Differences between PySimpleGUI and PySimpleGUIQt

#### Sizes
IMPORTANT NOTE if you are porting from tkinter to Qt - You will need to make one important change to your code.... **You must change your size parameters to be in PIXELS instead of CHARACTERS**. 

#### Fonts

Fonts should be in the format (font family, size).  The original PySimpleGUI also allowed a font string 'Family Size' but that option is not available (yet) in the Qt version.  I'll add it though so the code ports straight over.



### Installing PySimpleGUIQt for  Python 3      
      
    pip install --upgrade PySimpleGUIQt
      
On some systems you need to run pip3.      
      
    pip3 install --upgrade PySimpleGUIQt     
      

### Installing PySide2 for Python 3

```pip install PySide2```
     

    
    
      
## Testing your installation      
      
Once you have installed, or copied the .py file to your app folder, you can test the installation using python.  At the command prompt start up Python.      
```      
python3      
>>> import PySimpleGUIQt    
>>> PySimpleGUIQt.main()      
```      
      
You will see a sample window in the center of your screen.  If it's not installed correctly you are likely to get an error message during one of those commands      
      
Here is the window you should see:      
      
![sample window](https://user-images.githubusercontent.com/13696193/46097669-79efa500-c190-11e8-885c-e5d4d5d09ea6.jpg)      
      
      
      
## Prerequisites      
Python 3      
PySide2   
      
      
      
## Using  - Python 3      
      
To use in your code, simply import....      
 `import PySimpleGUIQt as sg`      
      
Then use the exact same code as any other PySimpleGUI program that runs on tkinter.  

## Status

### Functioning features
Features are being added daily to this Qt port of PySimpleGUI.  
These Elements are "complete" (a relative term... more are more complete than others):
* Text
* Input single line
* Input multiline
* Output multiline (new)
* Dial (new)
* Output - reroute stdout
* Spinner
* Sliders
* Buttons - RButtons, CButtons, Short-cut Buttons
* Checkbox
* Radio Buttons
* Listbox
* ComboBox
* Labeled Frames
* Columns - enables you to make pretty much any layout!
* Alpha channel for windows
* No Title Bar setting
* Enter submits for multiline
* Fonts
* Colors for text and background
* Timeouts for Read calls
* Change Submits parametes for most Elements
* Table
   * Basic display
   * Read selected rows
   * change_submits events
   * Updates
* Image as a background (new feature)
* Graph - Draw line, draw circle, draw text
  

## Missing Features

Notable MISSING features at the moment include:
* Graphs Element - erasing, draw arc, etc
* Image Element
* Tree Element - the more complex Elements have not yet been ported.  Stay tuned, new ones being added daily!
* Tab & tab group Elements
* Menus
* Change submits - for radio buttons


 

## Design      
            
## Author      
MikeTheWatchGuy      
      
## Demo Code Contributors      
 
      
## License      
      
GNU Lesser General Public License (LGPL 3) +      
      
## Acknowledgments      
      
