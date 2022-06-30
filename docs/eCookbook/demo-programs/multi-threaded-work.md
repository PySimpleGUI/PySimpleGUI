**Multi-Threaded Work - Running long tasks inside of a GUI**

This program demonstrates one way of using a combination of Python's Thread
and Queue objects to implement a GUI that performs work that takes too long
to directly perform inside of the event loop.

An example use would be if you have a button that you want to use to start
some code that will take several seconds to run, then this technique is a
good pattern to use.

Take a moment to examine the code dealing with the Thread and the Queue.  These
constructs are nothing to fear as the amount of code that uses them is only a 
handul of lines of code are needed.  And they are simple enough that you'll
be able to understand them.

***"Thread-safe"*** - This is an important term to consider any time you are using threads in your program.  There are 2 things to check out:
1. You must make sure that the calls you make from your thread are OK to call from a thread
2. If you are running multiple threads, then the calls you make must be "thread-safe"

The authors of libraries you are using often tell you if their code is "thread-safe".  

PySimpleGUI code is not thread safe.  For the tkinter version (i.e. plain PySimpleGUI versus PySimpleGUIQt), you cannot run PySimpleGUI as a thread.  To put that in simpler terms, you cannot make any calls into the PySimpleGUI package from a thread.  For example, you cannot call `update` for any of your elements from a thread.  This is why you see the updates happening from the main thread only.

Screenshot:

![SNAG-0491.jpg](/api/files/5da0877e2299175412c57964/snag-0491.jpeg "SNAG-0491.jpg")


<iframe src='https://trinket.io/embed/pygame/8f2aeea67b?start=result' width='100%' height='650' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
