## Easing into threading

I'm assuming you're on this page because you've learned something new.... that calling a lengthy function from a GUI is not a straightforward operation if you want a good user experience.

At some point in your GUI programming you're likely to run into this common, but distressing, problem of dealing with lengthy operations in a way that feels good to the user.

The PySimpleGUI Cookbook doing into this in much more detail in this section about multi-threading:

https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-long-operations-multi-threading

### Threading with some help...

To get you over the initial hump of multi-threaded programming, you can let PySimpleGUI create and manage threads for you. Like other APIs in PySimpleGUI, it's been simplified down as far as possible.

Here's the basic steps using `perform_long_operation`:

1. Pass your function name and a key to the call to `window.perform_long_operation`
2. Continue running your GUI event loop 
3. Windows pend using their typical `window.read()` call
4. You will get the event when your function returns
5. The values dictionary will contain your function's return value. They key will be the same as the event. So, `values[event]` is your function's return value.

### Detailed Example

In this example, your long operation takes a full 15 seconds.... an eternity when you're waiting with a GUI that is not operating during that timeframe.

In this Trinket you're given 2 basic ways of performing your long operations:
1. "Go" Button - This will directly call your function
2. "Threaded" Button - This will use a thread to make the call
 
Use the "Dummy" button to generate events to see if a window is responding to your clicks and typing.  Try moving the window as well.  You won't be able to when directly calling the function here on Trinket.  You'll be able to on Windows, Linux, Mac, but not here on Trinket because of how titlebars are implemented.  The details aren't important.  What's important is that your window is not happy when you directly call your function.



<iframe src='https://trinket.io/embed/pygame/9b3a04320d?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>


