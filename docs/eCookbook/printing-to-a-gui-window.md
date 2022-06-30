"Printing" to a GUI window

Demonstration of displaying your program's text information in a variety of ways.

![SNAG-0524.jpg](/api/files/5db8b43377188f5215703aec/snag-0524.jpeg "SNAG-0524.jpg")

There are a number of ways to display text information using PySimpleGUI.  A few include:

1. Use the "Debug Window" by calling sg.Print
2. Call a `popup` where the parms passed in will be shown in a new window
3. Create your window with an Output Element in it
4. Change the value of a `Text` Element by calling its `update` method
5. Change the value of a `Multiline` Element by calling its `update` method

This code demonstrates several of these ways.  You'll see 2 windows displayed.  One is the Debug Window, the other is your custom window with output and text elements.


<iframe src='https://trinket.io/embed/pygame/6b13c65907?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
