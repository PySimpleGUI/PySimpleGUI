## "Read All Windows" - The easist multi-window approach

Beginning in release 4.27.4 / 4.28.0 you'll find a new function `read_all_windows`.  This function makes it possible to run multiple windows simultaneously without the requirement of running them with a timeout of the read call.

The concept / function is simple.  Instead of reading a window and getting back the event and values for that window, you call `read_all_windows` and get back the window, event, and values for the window that caused the event.  

This architecture makes the transition from a single to multiple windows much easier as the event loop remains exactly the same what you're used to for a single window.  

The demo program shows 2 windows that are both "live".  Each window is capable of modifying the other.  There is no timeout call made on the read, but the capability is there should you wish it put a timeout on the read all windows call.


<iframe src='https://trinket.io/embed/pygame/1063a8ff1e?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
