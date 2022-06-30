## Using a Thread to complete a long task

The demo shows you how to use a thread to perform an operation that takes a long time to complete.  Normally if you attempt to do these operations in your GUI code, it will cause your GUI to appear to have stopped.

This examples relies on global variables for the handshake between the GUI and the worker thread.  Other demos you'll find here use Queues to communicate.   This demo is meant to be very simple so that you do not need to use a Queue.


<iframe src='https://trinket.io/embed/pygame/a656aafde4?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
