Simple Chat program front end

This demo was kept short and simple as to provide a foundation for something more elaborate (or not).  Didn't want to make it so that you have to remove more code than you add.

This program takes input from the user and uses print statements to output information to the window.  

A couple of features may not be what you're looking for and are easy to change are:
* Enter key "sends" the message
* After every send the input element is cleared
 
This chat program is synchronous in its design.  It gathers input, "sends" it or processes it in some manner and then outputs the results.  If you need is more asynchronous, then you'll want to use a PySimpleGUI async design pattern instead of this more simple synchronous one.


<iframe src='https://trinket.io/embed/pygame/7b058a66bc?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
