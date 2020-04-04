
  
  
    
      
        
        
        
        
![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)        
        
[![Downloads](http://pepy.tech/badge/pysimpleguiqt)](http://pepy.tech/project/pysimplegui)        
  
      
 ![Awesome Meter](https://img.shields.io/badge/Awesome_meter-1000-yellow.svg)  
         
 ![Python Version](https://img.shields.io/badge/Python-3.x-yellow.svg)        
        
PySimpleGUIQt on PyPI...
        
[![PyPI Version](https://img.shields.io/pypi/v/pysimpleguiqt.svg?style=for-the-badge)](https://pypi.org/project/pysimpleguiqt/) 
     
        
        
        
        
# PySimpleGUIQt        

"Qt without the ugly"

(For newbies... "Qt" is prouncounced "Cute")

## The Alpha Release    
 [Announcements of Latest Developments](https://github.com/MikeTheWatchGuy/PySimpleGUI/issues/142)        
              
  
        
  ----- 
## Getting Started with PySimpleGUIQt  
  
Welcome to the Alpha Release of PySimpleGUI for Qt!  
  
You can use the exact same code that you are running on the older, tkinter, version of PySimpleGUI.    
  
PySimpleGUIQt uses **PySide2** OR **PyQt5** for access to Qt.  **PyQt5 has been having  a number of problems recently however so tread lightly.**

## To minimize potential problems and broken features, if at all possible, use pyside2 instead of PyQt5.
  
## Porting your PySimpleGUI code to PySimpleGUIQt  
  
  
To "port" your code from the tkinter implementation. Follow these steps:  
  
1. Change `import PySimpleGUI` to `PySimpleGUIQt`  
  
That's it!  OK, maybe I should have said step instead of steps.  It may not be that simple in all cases, but it's pretty simple generally speaking.
  
  
## Differences between PySimpleGUI and PySimpleGUIQt  
  
#### Sizes  
  
While you can use "Character-based" sizes like you did in tkinter, it's best to use pixel based sizes as that is what Qt uses.  PySimpleGUIQt does some very rough / basic conversions from the character sizes to pixel sizes.  It's enough that your elements will at least be visible.  But the conversion is likely to not be ideal.  
  
#### Fonts  
  
Fonts should be in the format (font family, size).  You can use the older string based too, but it will not work with setting like bold and italics.  PySimpleGUIQt converts from the string 'Courier 20' to the tuple ('Courier', 20) for you.  
  
  
### Installing PySimpleGUIQt for  Python 3        
        
    pip install --upgrade PySimpleGUIQt  
  On Linux systems you need to run pip3.        
        
 pip3 install --upgrade --no-cache-dir PySimpleGUIQt   
 
### Installing PySide2 for Python 3  
  
It is _highly_ recommended that you use PySide2.  The code will attempt to use PyQt5 is pyside2 isn't found.  PyQt5 is **not** recommended.  
 
To install Pyside2:  
  
```pip install PySide2```  

      
**PyQt5 is no longer supported.  Only PySide2 is supported**

Too many differences were causing a lot of headaches.  Supporting just 1 Qt port is difficult enough.  Parsing out the differences between pyside2 and pyqt5 was simply getting to be too much
    
    

## Testing your installation        
Once you have installed, or copied the .py file to your app folder, you can test the installation using python.  At the command prompt start up Python.        

```
  python3
    >>> import PySimpleGUIQt 
    >>> PySimpleGUIQt.main()
```

You will see a sample window in the center of your screen.  If it's not installed correctly you are likely to get an error message during one of those commands        
        
Here is the window you should see:        
        
![image](https://user-images.githubusercontent.com/46163555/71421852-7c6ad400-264b-11ea-9adc-15f6aa4248e8.png)
       
        
        
        
## Prerequisites Python 3        
PySide2 or PyQt5   (experimental)
        
    
## Using  - Python 3        
 To use in your code, simply import....        
 `import PySimpleGUIQt as sg`        
 Then use the exact same code as any other PySimpleGUI program that runs on tkinter.    
  
  
## Status  

### Documentation

For the primary PySimpleGUI documentation go to http://www.PySimpleGUI.org.  HOWEVER, bear in mind that is the tkinter version.  But it's the best documentation for the package at the moment.  Docstrings are coming to this Qt Release, but it's going to take some time to get them done.  When they are, then this readme will also be fabulous.s
  
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
* Tree element - returns rows selected, but a little difficult to map those values to something meaningful for the user.
  
# New PySimpleGUI Features only in Qt (or first introduced in Qt)

There are a number of new features that are only available in PySimpleGUIQt.  These include:
* ButtonMenu Element
* Dial Element
* Stretcher Element (used to "push elements around" within a widnow)
* SystemTray feature
* "Dynamic" windows that grow and shrink (uses invisible elements)

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


## Stretch Element for Justifying Elements

Use the `Stretch` Element to left justify, right justify or center justify one or more elements within their container.

If a single `Stretch` Element is on a row, then it will push the other elements on the row to either the left or right.  If `Stretch` is on the left, then the elements to the rigth will be pushed to the right.

To center elements, place a `Stretch` Element on each side of them (2 `Stretch` Elements will be on the same row)

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


## Dynamic Windows (Element Visibility)

Finally, the ability to grow and shrink has been added as of release 0.20.0

While the window **appears** to be dynamic, the reality is that the elements are created up front, when you define the window layout.  You will create these "extra" elements with the flag `visible=False`.  Then, when you wish to show those elements, call the element's `Update` method setting `visible=True`.  

After you call the `Update` method, it's important to call `window.VisibilityChanged()` so that your window can change sizes.  Without that call your window will not shrink. It will grow properly, but it will not shrink.  While this could have been done by PySimpleGUI on the user's behalf, the thought was that perhaps the user wants the window size to remain the same and the element simply appears and disappears, leaving a blank spot.  If the window automatically grew and shrank, this would not be possible.  Just buck-up and make the call to `VisibilityChanged`.

## `enable_events` Parameter

All elements that are capable of producing events now have a parameter `enable_events`.  This is *identical* to the old parameter `change_submits` or `click_submits`.  The idea is to standardize on 1 name that all elements use.  The old parameters will continue to work, but the documentation and sample programs will steer you away from them and towards enable_events.

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

### 0.19.0 28-Nov-2018

Ability to disable menu items by adding ! to the front
Disable menu works for menus, button menus, system tray menus
Combo - Update Method - Value, values, disabled, font
Listbox - Update Method - Values, disabled
Listbox - SetValue Method - sets the selected items
Radio Button - Update Method - value, disabled
Checkbox - Update Method - value, disabled
Spinner - Update Method - value, values, disabled
Spinner - change_submits works
Image - New feature!  click_submits option (acts like a button in a way)
Window - Get screen dimensions
Slider - disable
Dial - disable

### 0.20.0 6-Dec-2018

* Ability to change calculations between characters and pixels
* size_px added to ALL elements that have a size parameter
* General Element.Update(widget, background_color, text_color, font, visible)
* visible parameter added to ALL elements
* enable_events flag
* Input text - enable events, visibility, size_px
* Input text update added capabilities
	* ability to highlight the input string
	* background, text colors and font
* Combo - enable events, visibility, size_px
* Combo - auto complete feature
* Combo - added to Update - background color, text color, font, visible
* Listbox - enable events, visibility, size_px
* Listbox - better scaling from characters to pixels
* Listbox - ability to Update with set to index, text color, font, visibility
* Radio - enable events, visibility, size_px
* Radio - Update additions - background_color, text_color, font, visibility
* Checkbox - enable events, visibility, size_px
* Checkbox - Update additions - background_color, text_color, font, visibility
* Spin - enable events, visibility, size_px
* Spin - Update additions - background_color, text_color, font, visibility
* Multiline input - enable events, visibility, size_px
* Multiline input - Update additions - background_color, text_color, font, visibility
* Multiline input better character to pixel scaling
* Multiline output - enable events, visibility, size_px
* Multiline output - Update additions - background_color, text_color, visibility
* Text - enable events, size in pixels
* Text - Update addition of visibility
* Output - visible, size_px
* Output - added update capability with new value, background_color, text_color, font, visibility
* Button - enable events, visible, size_px
* Button - Color Chooser feature completed
* Button - Color Chooser can target (None, None) which will store the value to be returned with the values from Read()
* Button - fixed bug in SaveAs button code.  Bad filter variable
* Button - Updated added font, visibility
* Button - new SetFocus() method will set the focus onto the button
* ButtonMenu - Update method implemented that includes menu definition changes, text, button color, font, visibility
* ProgressBar - added visibility, size_px
* ProgressBar - added Update method for changing the visibility
* Images - events, size_pix, visibility
* Images - can now get click events for images!
* Images - Update added visibility
* Graph - visibility, size_px
* Graph - Update method for changing visibility
* Frame - visibility, size_px
* Frame - Update method added that controls visibility
* ALL elements inside of a Frame that's invisible will also be invisible
* Tab - visible parameter added, however not yet functional!
* TabGroup - enable events, visibility
* TabGroup - Update for controlling visibility
* Slider - enable events, size_px
* Slider - Update method now includes visibility
* Dial - enable events, size_px, visibility
* Dial - Update method added visibilty control
* Column - visibility added
* Column - Added Update method to control visibility
* ALL elements inside of an invisible Column Element will also be invisible
* MenuBar - added visibility
* MenuBar - Update can now change menu definitions at runtime, and control visibility
* Table - enable events, size_px, visibility
* Table - Update method can control visibility
* Tree - enable events, size_px, visibility
* Tree - Update method can control visibility
* VisibilityChanged() function that must be called when using Qt so that the window will shrink or grow
* window.GetScreenDimensions can now be called prior to window creation
* window.Size property
* enable_events added to all of the shortcut buttons and browse buttons
* Ability to set a button image from a file
* Combo - ability to set a default value
* Combo - Read only setting.  Allows for user editing of value
* Menus - Ability to disable / enable any part of a menu by adding a ! before the entry name
* Tabs - ability to set tab text color, background color, background color of selected tab
* Tabs - ability to set widget area's background color
* Sliders - paging works properly (using page-up page-down or slider slider area to advance slider)
* Tree - Setting number of visible rows implemented
* Added 5 pixels to every window.  Have been having issues with text being cutoff on the right side
* SetOptions - ability to change default error button color for popups

### 0.21.0 - 9-Dec-2018
 
* Removed use of global variabels - using static class variabels instead
* Listbox.Get() will return current listbox value
* Progressbar now has color support
* Progressbar can be vertical now
* Can change bar or back and background color
* (barcolor, background color - None if use default)
* Table num_rows parameter implemented
* Table.Update - can change number of visible rows
* Window resizable parm - implemented, default changed from False to True
* Window.Move - implemented
* Window.Minimize - implemented
* Window.Disable - implemented
* Window.Enable - implemented
* Window.CurrentLocation - implemented
* Fixed too small scrollbar in Combobox
* Fixed too small scrollbar in Listbox
* Changed "text" window to a complex one for quick regression testing (try running PySimpleGUIQt.py by itself)

### 0.22.0 - 9-Dec-2018

* Spin.Get method - get the current spinner value

### 0.23.0 PySimpleGUIQt

* Fixed crash that was happening with latest pyside2 release!!!!
* Huge update to OneLineProgressMeter
* Debug window got title and do-not-reroute-std-out option
* Popups get a title option
* PopupScrolled getr non-blocking option
* Default logo included in Base64 Format
* Changed Chars to pixels scaling.  Went from (10,25) to (10,35)
* Changed pixel to chars cutoff from 10 to 12
* Change progress bar default size to 200 from 250
* Reworked the _my_windows global variable / class to use Window class variables
* Change in how Elements / Widgets are updated. Need to use {} correctly
* InputText supports drag and drop
* Support for Checkbox.Get()
* Support for strings in spinbox
* Added Update method to Output element
* Changed Button default file_types from *.* to *
* Support for Tab enable_events so they now generate events
* Table.Update can change the number of rows of table
* Window class now manages the list of active popups, user defined icon, QTApplication, num open windows
* Window resizable parameter default changed from False to True
* Window new parameter -  disable_minimize
* Window.GetScreenDimensions added
* Window.Move added
* Window.Minimize added
* Window.Maximize added
* Window.Disable added
* Window.Enable added
* Window.BringToFront added
* Window.CurrentLocation added
* TabGroup now returns which tab is selected in the return values
* Completely new Style generation class and functions (I hope it works!!!!)
* Style reworked for Column, Text, Button, Input, Combobox, Listbox, Input Multiline, Output Multiline, Progress Bar, Spinbox, Output, 
* Progress Bar colors are now correct
* Events generated when tabs are changed
* "Better" Table support.   Uses num_rows now and styles the scrollbar
* Tree element can support multiple types of icons including base64
* Fixed tree element scroll bar
* Icon ccan be set using SetOptions
* main for PySimpleGUIQt.py gets a nice test harness that shows lots of Elements


## 0.24.0 PySimpleGUIQt

* do_not_clear defaults to TRUE! for Input and MultilineInput/Output
* Key events for tables (unsure what's actually implemented)
* Tree icons can now be bytes in addition to filename!  (More Base64 support)


## 0.25.0 PySimpleGUIQt 5-Apr-2019

* Uses built-in Default Base64 Logo! (no more .ico file needed)
* New shortcuts for Elements
	* I = InputText
	* B = Butt = Btn = Button
* Convert user supplied button text to string just in case not a string
* Parameter `icon` in `Window` call can be Base64 byte string in addition to filename

  
## 0.26.0 11-Apr-2019 PySimpleGUIQt

* NEW Window parameter layout so can skip calling Layout

## 0.28.0 PySimpleGUIQt 5-Sep-2019

It's been a LONG LONG LONG time coming

* PEP8-ified!  All methods and functions have PEP8 equivalents!! It's a BFD
* Version numbers in the code
* New key dictionary - Window.AllKeysDict has all of the windows keys in 1 place for FASTER lookups
* Element.Widget provides access to low level Qt Widget
* Multiline scaling in addition to single line
* Raised default pixel cutoff for single line scaling to 15 from 12
* Pixel conversion done in Elements and passed through to Element class as size_px
* Renamed lots of private functions and methods to begin with _
* "Callable" Elements - element(new_value) will cause element.update(new_value) to be called
* Removed all __del__ except for the Output Element one
* Button - Click method added.  Your program can click a button as if a user did
* ButtonbMenu - Click mehtod also added like in Button element
* Graph Element
	* Added DrawRectangle method
	* Added RelocateFigure method
	* Added return of ID to DrawLine, DrawCircle, DrawText
	* Added Erase method to erase entire graph
* Tab - added Select method so can select a Tab as if user clicked it
* TabGroup - added Get method. Returns key of currently selected Tab, or text of Tab if no key set
* Table - Get method returns the table - GREAT way to enable users to edit a table and get the results
* SystemTray - uses default base64 icon if no icon supplied when creating
* Window - new finalize parameter removes need to add chained call to finalize
* Window.FindElement - added silent_on_error parameter
* Window[key] is the same as Window.FindElement(key)
* Calling a Window object calls Read for that window
* Fix for filetypes. Bug caused (*) to be added onto filetypes when browsing for files
* Combo returns exact value that was provided using an index into Values list instead of string from Qt
* Listbox returns actual supplied items
* Spinner returns avtual supplied item
* Tabgroup returns Tab key
* Finding element with focus now returns element regardless of type (any type of element can be returned)
* Radio Buttons now return events if enabled
* Graph element background colors added, uses new style class
* Table headings supported (where not supported before??)
* Popups switched to using new layout parm in Window call and uses keys too


## 0.30.0 PySimpleGUIQt 16-Nov-2019

* THEMES!! Over 100 new Look and Feel themes to choose from!
* New func preview_all_look_and_feel_themes() that will display a large window with all possible themes shown
* Metadata!  Now available on all elements when creating and accessable directly by program
* Metadata added to SystemTray objects and Window objects
* Metadata parameter added to all shortcut buttons and funcs
* Completed removal of PyQt5 code
* ML, MLine shortcuts added for Multiline (input)
* MLineOut shortcut for MultilineOutput
* Text element text is optional now
* Fixed bug in BrowseFiles button.  Was only getting first item in list instead of full list of filenames
* BMenu shortcut for ButtonMenu
* PBar, Prog shortcuts for ProgressBar
* Range is now properly set in Slider.Update
* Background color supported for MenuBars now
* Added 5 extra pixels to window size. Now adding a total of 10 so things don't get cut off


## 0.31.0 PySimpleGUIQt 23-Dec-2019

Themes and more!

* Added port string so can identify which port is being used (PySimpleGUIQt)
* Removed the Mac speific button and system color settings. Not sure why they existed at all since it's Qt, not tkinter
* Like all PySimpleGUI ports, the default theme is now "DarkBlue3"
* TRANSPARENT_BUTTON redefined as an a string explaining that if you're using it, you're not getting what you thought you were
* BROWSE_FILES_DELIMETER so that it can be changed to something other than ';' for systems that ';' is a valid char for filenames
* Can drag and drop into a Multiline Input Element!
* Colored text output for Multiline (hmmm...but not MultilineOutput.. may have to add it)
* Tree Element
	* Support for enable_events
	* Returns selected rows when reading
* Window - better error checking and warnings for window layouts
* Button - changes to help with getting animations back
* TabGroup - Tab positions now supporrted
	* left, right, top, bottom, lefttop, leftbottom, righttop, rightbottom, bottomleft, bottomright, topleft, topright
* Tables & Trees - text color and background color now work.  Don't appear to have worked before


## 0.32.0 PySimpleGUIQt 4-Apr-2020

The "Jeez... it's been way too LONG since a release" release

Highlights - Read with close (Single line GUIs!), Print to Multiline, Scrollable columns

* Listbox.update fix
* Added Graph.change_coordinates
* Added Image.Widget
* Return correct value when Comboxbox has manual data entered
* Multiline.print - new printing capabilities
* Multiline move cursor to end
* Scrollable columns
* Added Listbox.get
* Fix for visible ignored in Text Element
* Window.read - close parameter (YES! Single line GUIs again)
* Multiline readonly parm on update
* Print fixed sep char to act line normal print
* Print (Multiline) added autoscroll parm



# Design        
 ## Author 
 
The PySimpleGUI Organization 
PySimpleGUI.org
        
# Demo Code Contributors        
   
# License        
GNU Lesser General Public License (LGPL 3) +        

Copytight 2018, 2019 PySimpleGUI

# Acknowledgments