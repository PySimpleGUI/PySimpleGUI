### Using a Thread and a Queue To Accomplish Long Tasks

Queues are a great way for threads to communicate.  In this demo program we have a single long-operation that needs to be run.  You'll find a function named `long_function_wrapper` where is where you will place your code that takes a long time to execute.

When this function completes running, it sends a message to a Queue which is monitored by the main GUI thread.

The GUI enables you to run more than 1 of these long-running tasks if you want. It keeps track of how many have been requested and tracks when each completes executing.


<iframe src='https://trinket.io/embed/pygame/0a48f0afe8?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
