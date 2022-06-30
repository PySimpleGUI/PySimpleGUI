This demo program shows how to create a single Matplotlib graph and show it in a GUI window.

Note the it lacks an "Event Loop".
Normally instead of:

```python
event, values = window.read()
```

You would see an event loop:
```python
while True:
    event, values = window.read()
    if event is None:
        break
    ```
    
If you wanted to show multiple graphs or have other GUI elements, then you would replace that line of code with the event loop above and you'll have a "Normal" PySimpleGUI window.

<iframe src="https://trinket.io/embed/pygame/4602ef03b1" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>