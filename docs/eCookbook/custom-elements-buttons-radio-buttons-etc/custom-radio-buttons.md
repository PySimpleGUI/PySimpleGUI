## Custom Radio Buttons

Getting a GUI that's attractive isn't impossible using PySimpleGUI.  tkinter catches a lot of "ugly" comments.  It doesn't HAVE To be though.  PySimpleGUI makes creating your own custom controls ***trivial***.

There are a number of ways to go about something like this.  I've chosen a simple approach of using an Image Element and a Text Element.

The Image Elements are used to create a simple graphic that represents the state of the radio button.  The images are included in the code as base64 encoded graphics.  Because they are based on PNG files, they have an alpha channel and will blend with whatever kind of background you place them on.  They are either on or off.

Both the Image Element and the Text Element next to it have the events enabled on those elements.  This will create an event if either of them are clicked, which mirrors the behavior of a Radio Button.  The "State" of the button is simply stored as Metadata in the Image Element.

<iframe src='https://trinket.io/embed/pygame/ec630aa227?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
