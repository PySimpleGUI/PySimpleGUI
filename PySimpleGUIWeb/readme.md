 
![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)        
        
![Downloads](http://pepy.tech/badge/pysimpleguiweb)]       
  
      
 ![Awesome Meter](https://img.shields.io/badge/Awesome_meter-1000-yellow.svg)  
         
 ![Python Version](https://img.shields.io/badge/Python-3.x-yellow.svg)        
        
![Python Version](https://img.shields.io/badge/PySimpleGUIWeb_Version-0.1.0-orange.svg?longCache=true&style=for-the-badge)        
        
                
        
# PySimpleGUIWeb     

PySimpleGUI running in your web browser

## Primary PySimpleGUI Documentation

To get instructions on how use PySimpleGUI's APIs, please reference the [main documentation](http://www.PySimpleGUI.org). 
This Readme is for information ***specific to*** the Web port of PySimpleGUI.


## What is PySimpleGUIWeb?

PySimpleGUIWeb enables you to run your PySimpleGUI programs in your web browser.  It utilizes a package called Remi to achieve this amazing package.

At the moment (22-Jan-2019) the port has barely begun but it's far enough along to see that it's going to work.  The Text, Input Text and Button elements are "functional".  You can run simple PySimpleGUI programs and they actually WORK correctly.

## Engineering Pre-Release   Version 0.1.0
 
 [Announcements of Latest Developments](https://github.com/MikeTheWatchGuy/PySimpleGUI/issues/142)        

Having trouble? Visit the [GitHub site ](http://www.PySimpleGUI.com) and log an Issue.
        
        
## Installation

Installation is quite simple:

`pip install pysimpleguiweb`

Should this not work, you can copy and paste the file PySimpleGUIWeb.py into your application folder.

## Using

There are a lot of examples in the PySimpleGUI Cookbook as well as on the GitHub site.  At the moment very few will work due to the limited number of features of the 0.1.0 release.  It shouldn't be too long before they'll work.

To use PySimpleGUIWeb you need to import it:
`import PySimpleGUIWeb as sg`

From there follow the code examples in the Coookbook and the Demo Programs.  The only difference in those programs is the import statement.  The remainder of the code should work without modification.

             
## Requirements

PySimpleGUIWeb is based on the Remi project.  You will need to install Remi prior to running PySimpleGUIWeb:

`pip install remi`

You can learn more about Remi on its homepage.

https://github.com/dddomodossola/remi

PySimpleGUIWeb runs only on Python 3. Legacy Python is not supported.
  
  
  
## What Works

Text Element
Input Text Element
Button Element

Things like colors, fonts, etc, are not yet completed.  This is SO early in the process, but it's exciting to see at the same time.

# Release Notes:  
  
### 0.1.0   -   22-Jan-2019

* Initial release
* Text Element
* Input Text Element
* Button Element
* Window class


# Design        
# Author 
 Mike B.        
        
   
# License        
 GNU Lesser General Public License (LGPL 3) +        
        
# Acknowledgments
