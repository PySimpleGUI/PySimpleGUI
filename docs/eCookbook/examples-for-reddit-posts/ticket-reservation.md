Ticket Reservation Example

This program duplicates the window that this tutorial creates.

https://www.reddit.com/r/Python/comments/dk3rff/python_gui_project_ticket_reservation_style_and/

When using tkinter 41 lines of code are used.  This PySimpleGUI program uses 19
That makes the PSG program roughly 43% the size of the tkinter program, which is within the estimates of 1/2 to 1/10.  

Because this is a "data entry" type window, care was taken to clear the fields after the record was submitted and the cursor (focus) was placed back up at the name field, ready for a new record to be added.

This is a screenshot of the tkinter version

![SNAG-0505.jpg](/api/files/5dabab97793af61f3b448fe1/snag-0505.jpeg "SNAG-0505.jpg")

And this is what the PySimpleGUI window produces


![SNAG-0507.jpg](/api/files/5dabad3a793af61f3b449245/snag-0507.jpeg "SNAG-0507.jpg")


<iframe src='https://trinket.io/embed/pygame/7bfc5ce349?start=result' width='100%' height='400' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
