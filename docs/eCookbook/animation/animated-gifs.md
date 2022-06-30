**Animated GIFs**

Animated GIFs are shown by repeatedly calling a PySimpleGUI function or method on a frequent basis.  

***A critical fact to understand ***is that you must make a call for every frame you wish to show.  These functions are not **ones** that automatically playback and entire GIF on your behalf.  You must make a call for every frame to be displayed.

The timing of the calls is not important for your application to keep track of.  PySimpleGUI will figure out if enough time has elapsed for the next frame to be shown.  In other words, your application does not have to accurately measure the time between frames and perform delays.  

Instead of the application keeping track of the time, PySimpleGUI keeps track of how much time has elapsed since the last frame was shown. If enough time has elapsed that another frame should be shown, then the next frame will be shown.  It not enough time has passed, then nothing about the image is changed.  The last frame shown will remain the one showing.


This program will shows animations using 2 different methods.
1. By calling `popup_animated`
2. By calling `Image.update_animation`

In both cases, a loop is involved.  

The first animation played uses `popup_animated`.  You cannot interrupt this particular animation.  It plays until complete.  The remaining animations can be clicked in order to advance to the next animation.  When the last GIF is reached, clicking it will do nothing. It will play forever.

<iframe src='https://trinket.io/embed/pygame/02b174d0e8?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
