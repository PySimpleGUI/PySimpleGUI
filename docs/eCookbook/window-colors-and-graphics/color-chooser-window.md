A "Color Picker" or "Color Chooser"

These selection windows are usually provided by the GUI framework. But let's say you wanted to replace the normal system one.  One way to do it is using a grid of colored buttons.

This code demonstrates:
* Use of ttk buttons - they have beter highlighting then normal tk buttons
* Setting border=0, padding=(0,0) and no_titlebar - makes a very minimal look
* `Buttons`, like `Text`, do not need a text parameter filled in. It defaults to `''`

Here is how the window looks running on Windows

![SNAG-0556.jpg](/api/files/5de1a2392974237844766286/snag-0556.jpeg "SNAG-0556.jpg")

Setting the button size to (None, None) results in an extremely compact version

![SNAG-0557.jpg](/api/files/5de1a2b52974237844766343/snag-0557.jpeg "SNAG-0557.jpg")

A Qt version was easy to make.  It required changing the import to `PySimpleGUIQt` and couple of tweaks to parameters.  With the Qt version it's possible to specify Button sizes in pixels so it's possible to get the specific size you're seeking.  In this case 20x20 pixel squares w3ere used.

![SNAG-0577.jpg](/api/files/5de1a64c29742378447667c9/snag-0577.jpeg "SNAG-0577.jpg")

The same code even works on PySimpleGUIWeb

![SNAG-0578.jpg](/api/files/5de1a6e629742378447668b4/snag-0578.jpeg "SNAG-0578.jpg")

And finally, the red-headed step-child port PySimpleGUIWx has no problem displying the window

![SNAG-0580.jpg](/api/files/5de1a7912974237844766950/snag-0580.jpeg "SNAG-0580.jpg")




<iframe src='https://trinket.io/embed/pygame/aefc26ee3e?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
