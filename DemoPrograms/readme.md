# PySimpleGUI Demo Programs

## One Stop Shopping For Templates and Techniques 

This folder of over 320 programs is your jump-start to getting you to a solution as quickly as possible.  You can think of them as Recipes from a large PySimpleGUI Cookbook.

Programs in this folder have a range of uses and reasons for existing

* Demonstrate a particular PySimpleGUI Element / Feature (Tables, Trees, Buttons)
* Design patterns are "official" ways to get something done (Multiple windows)
* Integrate PySimpleGUI with another package / technology (OpenCV, Matplotlib)
* Assemble PySimpleGUI elements in a useful way (Bar graphs, games)
* How to deal with common GUI problems (work requiring lots of time)


## Demo Program Browser

The best way to work with these demos is to use the Demo Program Browser.   This browser will enable you to search by filename and also enable you to search inside the demos, a particularly powerful capability.

It will enable you to run the programs or launch your editor / IDE to edit them.

### Installing from GitHub

You'll find installation instructions in the Cookbook.  It is the first Recipe in the Cookbook.  The instructions are detailed with many screenshots.

### Installation Using Pip

There are a few ways to get these programs on your system.  One of the simplest is to use `pip`:

`pip install psgdemos`

Or if on Linux / Mac (that uses `pip3`


`pip3 install psgdemos`

This will install `psgdemos` from PyPI which includes the Demo Browser and all of these Demo Program source files.

To invoke the demo browser after installing using pip, type:
`psgdemos` 

from the command line and you'll be shown the Demo Browser


## Coding Conventions

Special attention is given to the programs in this folder to ensure they conform to the latest "preferred" technique or naming convention.  In the past, when technique changed, so did all of these demo programs.  For example, the use of the `FindElement` method was replaced by using `[ ]`.  All of these Demo Programs were updated to use the new convention.  

For example, this line of code:

```python
window.FindElement('status').Update(event)
```

was replaced with:

```python
window['status'].Update(event)
```

There was a recent sweep through all of the Demo Programs where all code was changed to use the PEP8 naming conventions / bindings.  All calls to `Window.Read()` were changed to `window.read()`

PySimpleGUI is on a swift development path.  In a short amount of time a lot can change.  To help ensure that users are using the latest, preferred, methods of using the PySimpleGUI package, these Demo Programs are the vehicle in which to communicate the latest design patterns.

Take a look at the Cookbook for more information about coding conventions used.

## Ports

Not all of the programs presented here are limited to the tkinter port of PySimpleGUI.  Some programs show multiple import statements with some that are commented out.  This is done to show you that the code is capable of running more than 1 platform.  This example is from the Demo_Matplotlibe_Two_Windows.py file

```python
from matplotlib import use
# import PySimpleGUI as sg
import PySimpleGUIQt as sg; use('qt5agg')
```

This indicates that the code can be run on either the tkinter or the Qt port.  To switch ports, uncomment the one you want to run on and comment out the others.

There are Demo Programs folders under each of the ports folders in the GitHub.


## Running Demos Online

Some of the Demo Programs are included in the online eCookbook (http://eCookbook.PySimpleGUI.org).  The eCookbook has a mix of a few of these Demos along with some unique examples not in the Demo Program.


### Trinket

If a demo does not require another package be installed and it's not specific to a particular platform then there's a possibility that it can be run online using Trinket.  You'll find a number of these Demo Programs have been added to the PySimpleGUI Trinket pages.  

The benefits of using Trinket include

* No need to install PySimpleGUI or even Python on your local machine
* Additional explanation can be included with the code, including images

This link will get you to the eCookbook:

http://eCookbook.PySimpleGUI.org


## Other Sample Code in this GitHub Account

The PySimpleGUI GitHub account has a number of repos that contain larger applications that use PySimpleGUI. A few linger in the PySimpleGUI project folder like the HowDoI, chess, exemaker, and some user created programs.  They'll get moved out at some point.  Until then, browse around the repo.  Explore a little.  Some are older, some newer, but none are as important as the Demo Programs folder which is kept up to date.

## Support

These programs are not "officially" part of the PySimpleGUI code.  They are not installed when you do a pip install for example.'

They are demonstrations, examples, and as a result may not be fully built-out, completed programs.  In order to keep the code simple, they may not have all of the error checking that your program should have.

If you encounter a problem where a demo no longer functions, you are of course encouraged to open an Issue on the GitHub.  

If you encounter more subtle problems, you should take into account that these programs are demonstrations, not end-user products.  For example, if an image viewer application doesn't display all types of image files like JPGs, then that's more than likely a limitation that the underlying GUI Framework has rather than a bug.  In this example, it's your responsibility to figure out how to convert your images into a format that's understood by the framework rather than an improvement needed in the demo program that will show you how to do that.


# Author 

The PySimpleGUI Organization and a few rare examples were provided by PySimpleGUI users.

If the code has been provide by a PySimpleGUI user, then the comments at the top of the program will indicate the author.

Because the PySimpleGUI project does not accept pull requests, it's unusual for Demo Progams to originate outside the project.  The eCookbook is a better place to find user created examples.  

Of cource, GitHub is where you'll find many 1,000's of user created PySimpleGUI programs, so go take a look!  Issue #10 here on the PySimpleGUI GitHub has screenshots submitted by users and is another location you can go for examples and inspiration.
   
# License        

Copyright 2019, 2020, 2021, 2022 PySimpleGUI

GNU Lesser General Public License (LGPL 3) +  
