 
![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)        
        
![Downloads](http://pepy.tech/badge/pysimpleguiweb)
  
      
 ![Awesome Meter](https://img.shields.io/badge/Awesome_meter-10,000-yellow.svg)  
         
 ![Python Version](https://img.shields.io/badge/Python-3.x-yellow.svg)        
        
![Python Version](https://img.shields.io/badge/PySimpleGUIWeb_-0..0-orange.svg?longCache=true&style=for-the-badge)        
        
                
        
# PySimpleGUIWeb     

PySimpleGUI running in your web browser!

Your source code will work on tkinter, Qt, WxPython and now in a browser (thanks to Remi)

Check out [repl.it](https://repl.it/@PySimpleGUI/PySimpleGUIWeb-Demos), the new way to run your PySimpleGUI code in a browser!

## Primary PySimpleGUI Documentation

To get instructions on how use PySimpleGUI's APIs, please reference the [main documentation](http://www.PySimpleGUI.org). 
This Readme is for information ***specific to*** the Web port of PySimpleGUI.


## What is PySimpleGUIWeb?

PySimpleGUIWeb enables you to run your PySimpleGUI programs in your web browser.  It utilizes a package called Remi to achieve this amazing package.


## Engineering Pre-Release   Version 0..0
 
 [Announcements of Latest Developments](https://github.com/MikeTheWatchGuy/PySimpleGUI/issues/142)        

Having trouble? Visit the [GitHub site ](http://www.PySimpleGUI.com) and log an Issue.
        
        
## Installation

Installation is quite simple:

`pip install pysimpleguiweb`

Should this not work, you can copy and paste the file PySimpleGUIWeb.py into your application folder.

## Using PySimpleGUIWeb

There are a lot of examples in the PySimpleGUI Cookbook as well as on the GitHub site.  At the moment very few will work due to the limited number of features of the 0.1.0 release.  It shouldn't be too long before they'll work.

To use PySimpleGUIWeb you need to import it:
`import PySimpleGUIWeb as sg`

From there follow the code examples in the Cookbook and the Demo Programs.  The only difference in those programs is the import statement.  The remainder of the code should work without modification.

             
## Requirements

PySimpleGUIWeb is based on the Remi project.  You will need to install Remi prior to running PySimpleGUIWeb:

`pip install remi`

You can learn more about Remi on its homepage.

https://github.com/dddomodossola/remi

PySimpleGUIWeb runs only on Python 3. Legacy Python (2.7) is not supported.
  
   
## What Works

* Text Element
* Input Text Element
* Button Element
* Combobox Element
* Checkbox Element
* Listbox Element
* Spinner Element (sorta... numbers 0 to 100 only now)
* Column Element
* Window background color
* Element padding
* Read with timeout
* Read with timeout = 0
* Popup Windows
* Multiple windows



# Running online using repl.it

This is something truly unique and amazing.   You can run your PySimpleGUI code in a web browser on a computer, phone, tablet without having Python installed on that computer.  Through the magic of repl.it and Remi you can run PySimpleGUI code anywhere you can run a browser.   Not only that, but you can embed these programs into web pages. In fact, this markdown document has one of these programs embedded in it.  

Here is where the iframe is inserted.  You may not see the page in some instances (like on GitHub).  

Here's your sample program:

<iframe height="400px" width="100%" src="https://repl.it/@PySimpleGUI/PySimpleGUIWeb-Demos?lite=true" scrolling="no" frameborder="no" allowtransparency="true" allowfullscreen="true" sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts allow-modals"></iframe>

# Release Notes:  
  
## 0.1.0 PySimpleGUIWeb 22-Jan-2019

* Initial release
* Text Element
* Input Text Element
* Button Element
* Window class


## 0.2.0 PySimpleGUIWeb 23-Jan-2019

Day 2 of development brings fonts, sizes, and colors...

* For all elements (Text, Input Text, Button):
	* Font family
	* Font size
	* Text Color
	* Background Color
	* Disable
	* Size
* Button Color
* Read timeouts (zero, non-zero, None/pend)
* Window close
* Window background color

## 0.3.0 PySimpleGUIWeb 24-Jan-2019

* Checkbox Element
* Combobox Element
* Listbox Element
* Element padding for all elements

## 0.4.0 PySimpleGUIWeb 26-Jan-2019

Functioning Elements
* Text
* Single line text input
* Multiline Input 
* Multiline Output 
* Listbox 
* Combobox
* Checkbox
* Slider
* Spinner (numbers only...hardcoded to 0 to 100)

New features
* Tooltips for all elements (so cool this works)
* Input Text events
* Text clicked event
* Listbox selected event
* Combobox selected event
* Checkbox Update
* Disable parameter for all elements
* Window.Close shuts down the server
* Enabled exceptions during packing operation
* New test harness exercises all element types

## 0.5.0 PySimpleGUIWeb  1-Feb-2019

* New default font size. Was Helvetica 10, now Helvetica 15
* InputText Element single character events working! (Finally)
* Listbox simple Update (values only)
* Column Element!  New!
* Column element experimental justification setting doesn't work yet
* Element background colors now picked up from container, not top level window
* Autosize Text
* Autosize Button Text


## 0.6.0 PySimpleGUIWeb  3-Feb-2019

* Changed Remi port to 0 so will always get a new free port

## 0.7.0 PySimpleGUIWeb  3-Feb-2019

* Completed `InputText.Update` method so that more demos can be run

## 0.8.0 PySimpleGUIWeb 8-Feb-2019

* Popup support!
* Support for multiple windows

## 0.9.0 PySimpleGUIWeb 14-Feb-2019

* Support for Window.Hide, Window.UnHide (better multi-window support)


# Design        
# Author 
 Mike B.        
        
   
# License        
 GNU Lesser General Public License (LGPL 3) +        
        
# Acknowledgments
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjAxMzEzNTUxOSw0NzU4NjU2NzYsLTEwNT
cxMDM2NDMsMTIxMzM1MjYzNiwtMTE2MDY4NDMzOV19
-->