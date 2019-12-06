# PySimpleGUI Demo Programs


## One Stop Shopping For Templates and Techniques 

This folder of over 170 programs is your jump-start, spring board, boost, shove in the back, cheat sheet to get you to a solution as quickly as possible.  You can think of them as Recipes from a large PySimpleGUI Cookbook.

Programs in this folder have a range of uses and reasons for existing

* Demonstrate a particualar PySimpleGUI Element / Feature (Tables, Trees, Buttons)
* Design patterns are "official" ways to get something done (Multiple windows)
* Integrate PySimpleGUI with another package / technology (OpenCv, Matplotlib)
* Assemble PySimpleGUI elements in a useful way (Bar graphs, games)
* Additional user code that enable new functionality (ANSI color strings)
* How to deal with common GUI problems (work requiring lots of time)


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



## Ports

Not all of the programs presented here are limited to the tkinter port of PySimpleGUI.  Some programs show multiple import statements with some that are commented out.  This is done to show you that the code is capable of running more than 1 platform.  This example is from the Demo_Matplotlibe_Two_Windows.py file

```python
from matplotlib import use
# import PySimpleGUI as sg
import PySimpleGUIQt as sg; use('qt5agg')
```

This indicates that the code can be run on either the tkinter or the Qt port.  To switch ports, uncomment the one you want to run on and comment out the others.


## Running Demos Online

Recently two online Pyuthon services have been used to demonstrate using PySimpleGUI- Trinket & repl.it.  You will find not only some of the Demo Programs from this folder on these sites, but other demo programs as well.  They make good "scratch pads" for posting PySimpleGUI code.  They are superior to Pastebin because not only can you share your code, but people can run the code without having to install or do anything locally.


### Trinket

If a demo does not require another package be installed and it's not specific to a particular platform then there's a possibility that it can be run online using Trinket.  You'll find a number of these Demo Programs have been added to the PySimpleGUI Trinket pages.  

The benefits of using Trinket include

* No need to install PySimpleGUI or even Python on your local machine
* Additional explanation can be included with the code, including images

You'll find the demos that have been added to Trinket here:

http://Trinket.PySimpleGUI.org



### Repl.it

Prior to discovering Trinket PySimpleGUI demo programs were being hosted online on repl.it.  Repl.it has several advantages over Trinket including:

* Able to run both PySimpleGUI and PySimpleGUIWeb programs
* Can use other packages with PySimpleGUI
* Can pip install specific PySimpleGUI versions to use

You'll find a list of repl.it demos here:

https://repl.it/@PySimpleGUI

These programs may not be the most up to date and in fact are likely to contain old coding constructs and examples.  As a result, use them more of a demonstration of "what's possible" rather than "exactly how to do it".


## Support

These programs are not "officially" part of the PySimpleGUI code.  They are not installed when you do a pip install for example.'

They are demonstrations, examples, and as a result may not be fully built-out, completed programs.  In order to keep the code simple, they may not have all of the error checking that your program should have.

If you encounter a problem where a demo no longer functions, you are of course encouraged to open an Issue on the GitHub.  

If you encounter more subtle problems, you should take into account that these programs are demonstrations, not end-user products.  For example, if an image viewer application doesn't display all types of image files ilke JPGs, then that's more than likely a limitiation that the underlying GUI Framework has rather than a bug.  In this example, it's your repsonibility to figure out how to convert your images into a format that's understod by the framework rather than an improvement needed in the demo program that will show you how to do that.


# Author 

The PySimpleGUI Organization and PySimpleGUI users

If the code has been provide by a PySimpleGUI user, then the comments at the top of the progrm will indicate the author.


   
# License        

Copyright 2019 PySimpleGUI.org

GNU Lesser General Public License (LGPL 3) +        
