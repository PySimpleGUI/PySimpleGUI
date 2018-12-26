
  
  
    
      
        
        
        
        
![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)        
        
[![Downloads](http://pepy.tech/badge/pysimpleguiwx)](http://pepy.tech/project/pysimplegui)        
  
      
 ![Awesome Meter](https://img.shields.io/badge/Awesome_meter-1000-yellow.svg)  
         
 ![Python Version](https://img.shields.io/badge/Python-3.x-yellow.svg)        
        
![Python Version](https://img.shields.io/badge/PySimpleGUIWx_For_Python_3.x_Version-0.2.0-orange.svg?longCache=true&style=for-the-badge)        
        
        
        
        
# PySimpleGUIWx        

The WxPython port of PySimpleGUI


 ## The Engineering Pre-Release     Version 0.2.0
 [Announcements of Latest Developments](https://github.com/MikeTheWatchGuy/PySimpleGUI/issues/142)        
              
  
        
## SystemTray

This is the only fully functioning feature of PySimpleGUIWx.  Previously only the Qt port supported the System Tray.

Now it's possible to "tack on" the System Tray to your PySimpleGUI application. 

If you're unable to upgrade to Qt but want the System Tray feature, then adding PySimpleGUIWx to your project may be the way to go.  

You can mix your System Tray's event loop with your normal Window event loop by adding a timeout to both your Window.Read call and your SystemTray.Read call.

### Source code compatibility

PySimpleGUIWx's System Tray feature has been tested against the same PySimpleGUIQt feature.  As long as you don't use features that are not yet supported you'll find your source code will run on either PySimpleGUIQt or PySimpleGUIWx by simply changing the import statement.  
 
Source code compatibility and easy of migration between frameworks is a major design goal for PySimpleGUI.
 


## System Tray Design Pattern

Here is a design pattern you can use to get a jump-start.

This program will create a system tray icon and perform a blocking Read. 

```python
import PySimpleGUIWx as sg

tray = sg.SystemTray(menu= ['menu',['Open', ['&Save::KEY', '---', 'Issues', '!Disabled'], 'E&xit']],
                     filename=r'C:\Python\PycharmProjects\GooeyGUI\default_icon.ico')
tray.ShowMessage('My Message', 'The tray icon is up and runnning!')
while True:
    event = tray.Read()
    print(event)
    if event == 'Exit':
        break
```

## Limitations

This is the first relase of this feature and it has some limitations.

* Timeouts must be None (completely blocking) or non-zero.  A value of 0 is invalid at the moment
* Base64 and in-ram icon images are not yet supported


## Menu Definitions

See the original, full documentation for PySimpleGUI to get an understanding of how menus are defined.  


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
The `timeout` parameter specifies how long to wait for an event to take place.  If nothing happens within the timeout period, then a "timeout event" is returned.  These types of reads make it possible to run asynchronously.  To run non-blocked, specify `timeout=0`on the Read call (not yet supported).

Read returns the menu text, complete with key, for the menu item chosen.  If you specified `Open::key` as the menu entry, and the user clicked on `Open`, then you will receive the string `Open::key` upon completion of the Read.

#### Read special return values

In addition to Menu Items, the Read call can return several special values.    They include:

EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED - Tray icon was double clicked
EVENT_SYSTEM_TRAY_ICON_ACTIVATED - Tray icon was single clicked
EVENT_SYSTEM_TRAY_MESSAGE_CLICKED - a message balloon was clicked
TIMEOUT_KEY is returned if no events are available if the timeout value is set in the Read call


### ShowMessage

Just like Qt, you can create a pop-up message.  Unlike Qt, you cannot set your own custom icon in the message, at least you can't at the moment.

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

### Update

You can update any of these items within a SystemTray object
* Menu definition
* Icon (not working yet)
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

You can add a key to your menu items.  To do so, you add :: and the key value to the end of your menu definition. 

`menu_def = ['File', ['Hide::key', '&Open::key', '&Save',['1', '2', ['a','b']], '&Properties', 'E&xit']]`

The menu definition adds a key "key" to the menu entries Hide and Open.

If you want to change the separator characters from :: top something else,change the variable `MENU_KEY_SEPARATOR`

When a menu item has a key and it is chosen, then entire string is returned.  If Hide were selected, then Hide::key would be returned from the Read.  Note that the shortcut character & is NOT returned from Reads.


# Release Notes:  
  
### 0.1.0   -   25-Dec-2018

* Support for SystemTray
  * Read, with or without a timeout
  * Catch single click, double click events
  * Source code compatiable with Qt

### 0.2.0   -   26-Dec-2018

* Correctly handling base64 images
* Support for clicking message balloon
* Can Hide and  UnHide the  icon



# Design        
 ## Author 
 Mike B.        
        
# Demo Code Contributors        
   
# License        
 GNU Lesser General Public License (LGPL 3) +        
        
# Acknowledgments