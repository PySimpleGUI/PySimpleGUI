**Design Pattern 1 - The One-Shot
**
Use this design pattern to show a window, get some input values and then close the window.  The window is not meant to stick around for very long.

<iframe src='https://trinket.io/embed/pygame/87c8b8cdd6?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>


An exciting development in 2019 was the addition of the `close` parameter to the `window.read()` call.  This enables you to write single line GUIs (again), a capability that was around in the early days of PySimpleGUI but disappeared as persistent windows became the primary use.

To make a single line, one-shot-GUI, you combine the layout into the call to `Window` itself.  You also "chain" the call to read onto the end of your  `Window` call.

The result is a line that looks like this:
```python
event, values = sg.Window('My single-line GUI!',
                    [[sg.Text('My one-shot window.')],      
                     [sg.InputText(key='-IN-')],      
                     [sg.Submit(), sg.Cancel()]]).read(close=True)  
```



<iframe src='https://trinket.io/embed/pygame/d4c897136b?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>


You can take this approach one step further and parse out the input value directly into your variable by adding more code onto the end of the line.  In this case, a subscript to pick up the second location in the tuple that's returned from `read` and then the key.

```python
event, values = sg.Window('My single-line GUI!',
                    [[sg.Text('My one-shot window.')],      
                     [sg.InputText(key='-IN-')],      
                     [sg.Submit(), sg.Cancel()]]).read(close=True)[1]['-IN-']
```
