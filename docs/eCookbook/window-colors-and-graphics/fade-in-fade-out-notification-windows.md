Show a "Notification Window"

This is a very clever bit of code that was submitted by a PySimpleGUI user.  It shows a "toaster" style of window (doesn't slide up/down but instead fades in/out).  You can click on the notification window and it will immediately dismiss it.

The fade-in/fade-out effects are not visible on Trinket but are if you download the code and run on your computer.

This program demonstrates:
* Computing screensize for placement of window
* Using a no_titlebar setting to create a clean window that doesn't look like a "normal window"
* Alpha channel used to fade window in and out
* Embeds icons into the code itself thus removing the need for multiple files. Makes it possible to copy and paste the program into your code to add the feature.
* Use of `Element.Widget` member variable to extend the PySimpleGUI feature set by directly accessing a tkinter setting.  Used to create the "hand" cursor when mouse is over window
* Using a single Graph Element to draw an entire window, placing graphics and text in a very precise manner.  The entire window is a single Graph Element

<iframe src='https://trinket.io/embed/pygame/8c79640020?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
