### Multiple Background Threads Outputting Results in GUI

Sometimes you have situations where you have persistent threads that run constantly in the background.  These threads may need to output information to your GUI.  Becuase you cannot directly call PySimpleGUI (tkinter) from another Thread, a communication mechanism is needed for the threads to communicate with the main GUI thread.

This communication is often in the form of a queue.  This demo program runs 3 threads.  Each update their status in the GUI by sending a message to a queue that the GUI is monitoring.


<iframe src='https://trinket.io/embed/pygame/a92c0346e2?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
