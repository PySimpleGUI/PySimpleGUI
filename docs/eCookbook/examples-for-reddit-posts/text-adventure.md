A Text Adventure GUI Mockup

A quick mockup for a GUI in response to this Reddit post:

https://www.reddit.com/r/learnpython/comments/dza038/is_there_a_way_to_request_and_save_user_input/

This program creates a window that takes in user input and displays "results" in the window.  The results are displayed using simple "print" statements.

On Windows, the window look like this:

![SNAG-0572.jpg](/api/files/5ddc0cc520a3a5c051b2c955/snag-0572.jpeg "SNAG-0572.jpg")

Note that colored text output to an `Output Element` is not currently supported.  You can have colored text in the main window itself but not in these scrolling type Elements.  However, that was a very recent change to PySimpleGUIQt that DOES allow colored text to be sent to a scrolling output Element (the Multiline).  Looking at adding it to the tkinter (plain PySimpleGUI) port very soon.


<iframe src='https://trinket.io/embed/pygame/fe2a3c3008?start=result' width='100%' height='400' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
