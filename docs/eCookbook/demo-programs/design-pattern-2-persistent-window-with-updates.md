**Design Pattern 2 - Persistent Windows, output updates in window**


***This is the most common design pattern you'll find in PySimpleGUI. *** 

It's the same across all of the ports of PySimpleGUI.  You'll easily be able to recognize a PySimpleGUI program by this basic structure.  

This pattern is for windows that remain open with the user interacting with them.  It's a "normal" window from a user's standpoint.

*This pattern has 4 parts:*

1. Layout definition
2. Window creation
3. Event loop - read window events and inputs
4. Window close

Each of these parts is 1 or 2 lines of Python code when working with a basic window.  The size of the event loop depends on the amount of processing you need to do when events happen in the window.

<iframe src='https://trinket.io/embed/pygame/c0bf3a6754?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>

