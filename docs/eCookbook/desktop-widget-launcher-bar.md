## Desektop Widget - Launcher Bar

### Trivial Operations - Changing layouts

This demo has a nice little "minimize" feature.  You click on a downarrow and the entire interface will "minimize" down into a single image.

Here is the code that does those minimize and restore operations:


```python
        elif event == sg.SYMBOL_DOWN_ARROWHEAD:
            window['-BUTTON COL-'].update(visible=False)
            window['-MINIMIZED COL-'].update(visible=True)
        elif event == '-MINIMIZED IMAGE-':
            window['-BUTTON COL-'].update(visible=True)
            window['-MINIMIZED COL-'].update(visible=False)
```
            
If you're minimizing, then you want to hide the buttons and show the image.  If you're restoring, then you're hiding the image and showing the panel of buttons.

A simple thing to describe means less code for you and less complexity too.  

### The Button Bar

Add a floating bar that enables easy launching of all programs on your system.  Or launch your Python program or anything you want because you're a Python programmer.

This is a copy of the Demo Program you'll find on the PySimpleGUI Repo:

https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Desktop_Widget_Launcher_Bar.py

It's a simple "launcher" application that you can run, move anywhere you want, and it'll return there next time you run it.

Add your own buttons, images, etc, to launch your favorite programs, Python code, or call functions.  Anything's possible when you write your own utilities 

![thumb_112.png](/api/files/61574bc56525133c451d4a2a/thumb_112.png "thumb_112.png")

For this Trinket, I matched the background color and used the settings feature to set it.  This is why you will see a JSON file with the Trinket.


<iframe src='https://trinket.io/embed/pygame/2593918099?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>

