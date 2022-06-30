
It's sometimes useful to exlore what it would take to duplicate a GUI written in tkinter, especially when a nicely written article accompanies the code.

This GUI code duplicates a portion of the tkinter code posted on this page:
https://www.devmedia.com.br/tkinter-interfaces-graficas-em-python/33956

It performs performs the logic for only the "Inserir" button. 

To add the code for the remaining buttons, add `elif` statements onto the bottom of the `if` statement in the event loop.  At the moment, buttons that are not handled in the event loop causes a "Not yet implemlented" message to be shown.

On a Windows machine, the window this code produces looks like this:

![SNAG-0487.jpg](/api/files/5d9f927d852774611bccf3e1/snag-0487.jpeg "SNAG-0487.jpg")


PySimpleGUI is a package that provides an interface to GUI Frameworks that uses constructs familiar to Python programmers of all experience levels.  With PySimpleGUI you can run your source code on tkinter, Qt, WxPython and in a browser... on Windows, Mac and Linux


<iframe src='https://trinket.io/embed/pygame/c50932b36f?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>

One of the "neat tricks" that PySimpleGUI has is the ability to run on multiple GUI platforms with a minimal amount of changes to your code.  Often it is just 1 line of code to change.  

You can't do this on Trinket, in your browser because Trinket only supports tkinter.

For the example code above, running on a Windows machine, the import statement at the top was changed to use a version of PySimpleGUI that runs on Qt, WxPython and in the browser (using Remi).  Note that the windows produced are not perfect and may need a font size or other change to make it look better, but the several character change using PySimpleGUI is tiny compared to what it would take to port tkinter code to Qt.

Changed the import to run on PySide2 (Qt)
```python
import PySimpleGUIQt as sg
```

The code then created this window running on Qt

![SNAG-0488.jpg](/api/files/5d9f92e0852774611bccf5d8/snag-0488.jpeg "SNAG-0488.jpg")

Changed the import to run on WxPython
```python
import PySimpleGUIWx as sg
```

The code then created this window running on WxPython
![SNAG-0489.jpg](/api/files/5d9f92f3852774611bccf644/snag-0489.jpeg "SNAG-0489.jpg")

Changed the import to run in a browser:
```python
import PySimpleGUIWeb as sg
```

The code then created this window running in a chrome window

![SNAG-0490.jpg](/api/files/5d9f9301852774611bccf688/snag-0490.jpeg "SNAG-0490.jpg")