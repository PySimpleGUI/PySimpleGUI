## Graph Element - Draw a square, drag it around

This program is meant to show just how simple the Graph element can be to work with.  The code has been trimmed down to a base minimum. 

The number of lines of code is 22 lines of actual program code, many of those are because of putting parameters on separate lines to make it easy for you to see them.  It's 16 lines of code if you're counting "statements".  The number isn't important.  The simplicity is.

Like many Demo Programs, this was written to demonstrate a bug that was happening.  Testing new features or replicating bugs have been an excellent genesis for many of the Demo Programs.

The high level summary of the code is:
* Create the layout that is a single Graph Element of size 400 x 400 pixels
* Make the window
* Draw a square on the Graph Element
* Event loop
    * `window.read()`
    * If the event is the Graph element's key, then it's a mouse click or drag event
        * Move the center of the square to where the mouse is located


<iframe src='https://trinket.io/embed/pygame/bef90956a6?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
