```python.run
runnable code goes here
```## Collapsible Sections

Visible / Invisible settings on the plain tkinter based PySimpleGUI have been a real challenge.  In release 4.28.0 a new function, `pin`, was added that will "pin" an element to a location in your layout.  This will reserve the location for the element in the layout.  Without it, the element will move when you make it inivisible and visible again.

There is a 1-pixel "penalty" of sorts when using this capability.  A single pixel is needed to reserve and hold this spot, a small price to pay given what you can do with this new capability.

This demo shows how you can use this feature to make Column elements invisible as if a section of the window has been collapsed with the contents hidden.

Here is how the demo looks running on Windows

![Collapsable for cookbook.gif](/api/files/5f2c5d5847d1fc1c1a4d850a/collapsable-for-cookbook.gif "Collapsable for cookbook.gif")

<iframe src='https://trinket.io/embed/pygame/df2c15979e?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
