# Toggle Buttons with Disable

This example shows a 4-state toggle button.

Normally a toggle button has 2 states:
1. On
2. Off

Buttons can also be disabled.  When using PySimpleGUI to disable buttons, it will use the underlying GUI Framework's disable which usually adds a gray overlay or change the text to gray.

In the 4.35.0 release of PySimpleGUI, a new button state was added.... an "ignore".  This state means that the button will not generate events.  Unlike disable, ignore does not use the GUI framework's disable capability, thus it will not change the color.

This example program has these 4 states for the toggle button:
1. On
2. Off
3. On and disabled
4. Off and disabled

Disabled in this specific situation means ignore.  The program itself is making the button appear to be disabled.


<iframe src='https://trinket.io/embed/pygame/4d0aea3fb3?start=result' width='100%' height='550' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
