
  
  
    
      
        
        
        
        
![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)        
        
[![Downloads](http://pepy.tech/badge/pysimpleguiqt)](http://pepy.tech/project/pysimplegui)        
  
      
 ![Awesome Meter](https://img.shields.io/badge/Awesome_meter-1000-yellow.svg)  
         
 ![Python Version](https://img.shields.io/badge/Python-3.x-yellow.svg)        
        
![Python Version](https://img.shields.io/badge/PySimpleGUIQt_For_Python_3.x_Version-01.14.0-orange.svg?longCache=true&style=for-the-badge)        
        
        
        
        
# PySimpleGUIQt        

"Qt without the ugly"


 ## The Alpha Release     Version 0.18.0
 [Announcements of Latest Developments](https://github.com/MikeTheWatchGuy/PySimpleGUI/issues/142)        
              
  
        
  ----- ## Getting Started with PySimpleGUIQt  
  
Welcome to the Alpha Release of PySimpleGUI for Qt!  
  
You can use the exact same code that you are running on the older, tkinter, version of PySimpleGUI.    
  
PySimpleGUIQt uses **PySide2** OR **PyQt5** for access to Qt.  PyQt5 has been having  a number of problems recently however so tread lightly.
  
## Porting your PySimpleGUI code to PySimpleGUIQt  
  
  
To "port" your code from the tkinter implementation. Follow these steps:  
  
1. Change `import PySimpleGUI` to `PySimpleGUIQt`  
  
That's it!  OK, maybe I should have said step instead of steps.  
  
  
## Differences between PySimpleGUI and PySimpleGUIQt  
  
#### Sizes  
  
While you can use "Character-based" sizes like you did in tkinter, it's best to use pixel based sizes as that is what Qt uses.  PySimpleGUIQt does some very rough / basic conversions from the character sizes to pixel sizes.  It's enough that your elements will at least be visible.  But the conversion is likely to not be ideal.  
  
#### Fonts  
  
Fonts should be in the format (font family, size).  You can use the older string based too, but it will not work with setting like bold and italics.  PySimpleGUIQt converts from the string 'Courier 20' to the tuple ('Courier', 20) for you.  
  
  
### Installing PySimpleGUIQt for  Python 3        
        
    pip install --upgrade PySimpleGUIQt  
  On Linux systems you need to run pip3.        
        
 pip3 install --upgrade PySimpleGUIQt   
### Installing PySide2 for Python 3  
  
It is recommended that you use PySide2, however, if that cannot be found, then PyQt5 will be attempted.  To install either of these:  
  
```pip install PySide2```  

      
**Nov 26th - There has been a number of problems found using PyQt5 recently.  Unclear how if it can be supported after all.**

 ## Testing your installation        
 Once you have installed, or copied the .py file to your app folder, you can test the installation using python.  At the command prompt start up Python.        

     python3
     >>> import PySimpleGUIQt 
     >>> PySimpleGUIQt.main()

 You will see a sample window in the center of your screen.  If it's not installed correctly you are likely to get an error message during one of those commands        
        
Here is the window you should see:        
        
![sample window](https://user-images.githubusercontent.com/13696193/46097669-79efa500-c190-11e8-885c-e5d4d5d09ea6.jpg)        
        
        
        
## Prerequisites Python 3        
PySide2 or PyQt5   (experimental)
        
    
## Using  - Python 3        
 To use in your code, simply import....        
 `import PySimpleGUIQt as sg`        
 Then use the exact same code as any other PySimpleGUI program that runs on tkinter.    
  
  
## Status  
  
### FEATURE COMPLETE!   
All of the major features are DONE.  They may not have all of their options working, but they can be added to your windows.  It's been an amazing week to get here.  
  
I hope you enjoy this ALPHA release!  Please post a screenshot on the GitHub site.  There is an Issue where users have been posting their applications.  It's a place for you to show-off and a place for others to learn from your designs.  Your window does not have to be complex.... all GUIs, no matter how simple, are something we can learn from.  
  
  
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
* Change Submits parameters for most Elements  
* Table  
  * Basic display  
  * Read selected rows  
  * change_submits events  
  * Updates  
* Image as a background (new feature)  
* Graph - Draw line, draw circle, draw text  
* Image Element  
* Tree Element  
* Tabs  
* Menus  
* Menu Button Element
  
    
  
## Missing Features  
  
Notable MISSING features at the moment include:  
* Graphs Element Methods - erasing, draw arc, etc  
  
# New PySimpleGUI Features only in Qt

There are a number of new features that are only available in PySimpleGUIQt.  These include:
* ButtonMenu Element
* Dial Element
* Stretcher Element
* SystemTray feature

## SystemTray

This is a PySimpleGUIQt only feature.  Don't know of a way to do it using tkinter.  It looks likely to work on WxPython however.

In addition to running normal windows, it's now also possible to have an icon down in the system tray that you can read to get menu events.  There is a new SystemTray object that is used much like a Window object.  You first get one, then  you perform Reads in order to get events.

Here is the definition of the SystemTray object.

```python
SystemTray(menu=None, filename=None, data=None, data_base64=None, tooltip=None):  
        '''  
 SystemTray - create an icon in the system tray  
 :param menu: Menu definition 
 :param filename: filename for icon  
 :param data: in-ram image for icon  
 :param data_base64: basee-64 data for icon  
 :param tooltip: tooltip string '''
```

You'll notice that there are 3 different ways to specify the icon image.  The base-64 parameter allows you to define a variable in your .py code that is the encoded image so that you do not need any additional files.  Very handy feature.

## System Tray Design Pattern

Here is a design pattern you can use to get a jump-start.

This program will create a system tray icon and perform a blocking Read.  If the item "Open" is chosen from the system tray, then a popup is shown.

```python
import PySimpleGUIQt as sg  
  
menu_def = ['BLANK', ['&Open', '---', '&Save', ['1', '2', ['a', 'b']], '&Properties', 'E&xit']]  
  
tray = sg.SystemTray(menu=menu_def, filename=r'default_icon.ico')  
  
while True:  # The event loop  
  menu_item = tray.Read()  
    print(menu_item)  
    if menu_item == 'Exit':  
        break  
    elif menu_item == 'Open':  
        sg.Popup('Menu item chosen', menu_item)
        
```
The design pattern creates an icon that will display this menu:
![snag-0293](https://user-images.githubusercontent.com/13696193/49057441-8bbfe980-f1cd-11e8-93e7-1aeda9ccd173.jpg)

### Icons

When specifying "icons", you can use 3 different formats.  
* `filename`- filename
* `data_base64` - base64 byte string
* '`data` - in-ram bitmap or other "raw" image

You will find 3 parameters used to specify these 3 options on both the initialize statement and on the Update method.

## Menu Definition
```python
menu_def = ['BLANK', ['&Open', '&Save', ['1', '2', ['a', 'b']], '&Properties', 'E&xit']]  
```

A menu is defined using a list.  A "Menu entry" is a string that specifies:
* text shown
* keyboard shortcut
* key

See section on Menu Keys for more informatoin on using keys with menus.

An entry without a key and keyboard shortcut is a simple string
`'Menu Item'`

If you want to make the "M" be a keyboard shortcut, place an `&` in front of the letter that is the shortcut.
`'&Menu Item'`

You can add "keys" to make menu items unique or as another way of identifying a menu item than the text shown.  The key is added to the text portion by placing `::` after the text.

`'Menu Item::key'`

The first entry can be ignored.`'BLANK`' was chosen for this example. It's this way because normally you would specify these menus under some heading on a menu-bar.  But here there is no heading so it's filled in with any value you want.

**Separators**
If you want a separator between 2 items, add the entry `'---'` and it will add a separator item at that place in your menu.


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

```python
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
## Menus with Keys

PySimpleGUIQt offers the ability to add a key to your menu items.  To do so, you add :: and the key value to the end of your menu definition. 

`menu_def = ['File', ['Hide::key', '&Open::key', '&Save',['1', '2', ['a','b']], '&Properties', 'E&xit']]`

The menu definition adds a key "key" to the menu entries Hide and Open.

If you want to change the separator characters from :: top something else,change the variable `MENU_KEY_SEPARATOR`

When a menu item has a key and it is chosen, then entire string is returned.  If Hide were selected, then Hide::key would be returned from the Read.  Note that the shortcut character & is NOT returned from Reads.


# Release Notes:  
  
### 0.12.0   -   20-Nov-2018
Correctly restore stdout when Output Element is deleted  
Added Finalize ability  
**Better multi-window handling... maybe it's finally fixed!**  
Radio button default value  
Dial element default value  
Show expanded option for trees  
Titles for popups  
  
### 0.13.0 -  22-Nov-2018

Focus for Input Text and Multiline Input

 - Get focus 
 - Set focus
Window.FindElementWithFocus works
Multiline input

 - Change submits 
 - Update - disabled, append

Multiline output - Update value, append, disabled, get value
Text clicked submits
File types for open files
Initial folder, file types, for browse buttons
File types standardized on tkinter data format
Find Element With Focus now works for input and multiline input
Yet more multiwindow handling
Relief for Text element
Input text disable
Correct sizing of Comboboxes using visible items parm
Correct default values for input and multiline input
Change submits for multiline
Horizontal and Vertical separators
PopupGetFile and PopupGetFolder - no_window option works
  
### 0.14.0 - 24-Nov-2018

Slider tick positions set using relief parm
ButtonMenu Element
Multiline.Update font parm
Text.Update color and font now work
Button.Update font support
Window.Element = Window.FindElement
Better font support for all elements - underline, bold
Element padding - complete rework
Text element padding
Button padding
Input Text padding
Input Text password char
Listbox padding
Combobox padding
Multiline padding
Checkbox padding
Radio padding
Progress Bar padding
Output padding
Image padding
Graph padding
Slider - set tick marks using relief parm
Dial - set tick information using resolution and tick interval
Table padding
Tree padding
Separator padding
Force window sizing should mean windows are better sized
Popup - better layout

   
### 0.15.0 24-Nov-2018  

New SystemTray feature!
margin paramter for Text Element.  Takes 4 ints
Corrected button colors when disabled. For now am restoring them to original colors
Border Depth for all elements that support it (inputs, slider, table, tree, etc)
Fix for Element padding done incorrectly!! Sorry about this one


### 0.16.0  24-Nov-2018  

Easier forcing to use PyQt5 for testing
Predefined events for Tray Icons
* Double Clicked
* Icon Activated
* Message Clicked
* Timeout key for polling

Tray icon tooltip
Menu keys with programmable separator
Better element padding hierarchy
Menubar now returns values as does the ButtonMenu

### 0.17.0  24-Nov-2018  

Window.Hide and UnHide methods

### 0.18.0 26-Nov-2018

Tooltips for all elements
Completion of all SystemTray features
Read with or without timeout
Specify icons from 3 sources
Show message with custom or preset icons
Update 
* Menu
* Tooltip
* Icon
PopupScrolled - new location parameter, fixed bug that wasn't closing window when completed

# Design        
 ## Author 
 Mike B.        
        
# Demo Code Contributors        
   
# License        
 GNU Lesser General Public License (LGPL 3) +        
        
# Acknowledgments