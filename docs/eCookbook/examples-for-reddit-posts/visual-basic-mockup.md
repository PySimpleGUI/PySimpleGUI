**Visual Basic Program Duplication**

The exercise here is to duplicate a program originally written in Visual Basic.

This is the provided screenshot

![visual basic window.png](/api/files/5d9c0b50be22ab3437fb6683/visual-basic-window.png "visual basic window.png")

The first thing to do with all PySimpleGUI programs is to define what your "rows" will look like. In this case it appears as if 3 rows are present.

The bottom row is a series of "container elements" including Frame Elements and a Column Element

![visual basic window in rows.png](/api/files/5d9c0b2bbe22ab3437fb6623/visual-basic-window-in-rows.png "visual basic window in rows.png")



Here is the start of the code needed to implement this particular layout.

Information about the program's operations are displayed in the middle of the window.  It's assumed that will be perhaps a table in the future, but for now it is a handy location to route printed output to the window.

Clicking the "Process Files" buttons will print out the values of the `values` variable which is the values dictionary returned from the call to `window.read()` as can be seen in the code.


<iframe src='https://trinket.io/embed/pygame/8ea933f356?start=result' width='100%' height='550' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
