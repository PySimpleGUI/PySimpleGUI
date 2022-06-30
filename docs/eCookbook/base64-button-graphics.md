Changing your buttons from plain rectangular GUI buttons to graphic images is very easy in PySimpleGUI.  

Button graphics are specified when creating the Button, inside of your layout.

This is what the code below looks like running on Windows.

![SNAG-0552.jpg](/api/files/5dcacf3f7b21228b604a6a58/snag-0552.jpeg "SNAG-0552.jpg")


<iframe src='https://trinket.io/embed/pygame/a3dcdfc221?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>

This particular button graphic is larger than it needs to be.  It should have been edited prior to use in the program.  The size of the button as specified in the code is huge in comparison to the screenshot above.  Removing the `image_subsamble=8` from the Button creation you'll see the full size of the button graphic.

By the way, the `image_subsample` value indicated how much to "divide" the size by.  The value of "8" specified above means to use 1/8 the size of the original.  If the value was "2" then 1/2 of the original size will be shown.

![SNAG-0553.jpg](/api/files/5dcad00f7b21228b604a70ec/snag-0553.jpeg "SNAG-0553.jpg")
