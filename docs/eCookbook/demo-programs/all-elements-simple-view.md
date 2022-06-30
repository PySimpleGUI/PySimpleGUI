## All Elements - Listed in 1 Window

This program is a slightly modified version of the Demo Program found in the PySimpleGUI repo:

`Demo_All_Elements_Simple.py`


The view of this window here on Trinket looks a little different than the code when run on Windows

### Trinket

![SNAG-1569](https://user-images.githubusercontent.com/46163555/152375251-3568f77c-915f-4c87-89b9-47f79dc4c9b9.jpg)


### Windows 10

![image](https://user-images.githubusercontent.com/46163555/152372558-f5656419-fb6d-4a6f-bc46-8c5fd31c3a1c.png)

### Titlebar and Menubar

The thing I want to draw your attention to is the Titlebar and the Menubar.

Because Trinket does not provide a Titlebar (it's the operating system's job to do this), PySimpleGUI provides one for you automatically.  PySimpleGUI doesn't automatically switch your Menubar to a MenubarCustom which is what you need to use on Trinket for the 2 to match.  The code in this Trinket has been modified to add the custom Menubar for you.


### The code

This demo was written to show you the "pallet of elements" that you have available to paint your GUI window with.  It doesn't tell the full story however as you can expand these GREATLY by using PIL, the graph element, images for buttons, etc.  What it does do is list all of the elements using 1 line of code per element.  It can't get much simpler than that.


### Theme Previewer

This proram has a secondary function... you can see what all of the elements look like using the many PySimpleGUI Themes.  Choose a new theme from the Combo element shown and the window will be remade with the new theme.

For example, I chose the "Dark Grey 11" theme and was shown this window:

![SNAG-1570](https://user-images.githubusercontent.com/46163555/152375250-ba12f1a3-e3fa-429f-babd-69762dd05bea.jpg)


<iframe src='https://trinket.io/embed/pygame/f72e2992d2?start=result' width='100%' height='700' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
