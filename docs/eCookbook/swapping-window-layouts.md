**(Simulated) Swapping of Entire Window Contents**

While it's not possible to make layouts that are truly dynamic in PySimpleGUI, you can make things appear they do.

In this demo the goal is to swap out the entire window, except for the bottom row of buttons, with a completely different "layout".  

The way this is accomplished is to create multiple `Column` Elements that are all hidden except for the currently visible one.


<iframe src='https://trinket.io/embed/pygame/90e0dd133c?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
