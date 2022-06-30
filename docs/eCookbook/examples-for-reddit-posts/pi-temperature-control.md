A super-quick mockup of a replacement GUI that was originally written in tkinter.

It's meant to run on a Raspberry Pi but has the GPIO stuff not present at the moment.  It's only the GUI.

It would be best to completely separate the hardware / GPIO code into functions.  This will allow the GUI to be run and tested on platforms other than the Pi that don't support GPIO.  For those platforms the functions that do GPIO can simply return.



The original tkinter code can be found here:

https://www.reddit.com/r/learnpython/comments/e2qcdz/pid_interface_keeps_crashing/

When run on Windows the code produces this GUI 

![SNAG-0574.jpg](/api/files/5de005ba971ab57562da09c6/snag-0574.jpeg "SNAG-0574.jpg")

Running on the Pi it looks nearly identical 

![SNAG-0576_2.jpg](/api/files/5de0b9a29c2e1f9417ffe0a5/snag-0576-_2.jpeg "SNAG-0576_2.jpg")

<iframe src='https://trinket.io/embed/pygame/73280f3dc5?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
