## Navigating Focus Using Arrow Keys

This example shows how you can navigate through your windows's elements by using the left and right arrow keys.  The down arrow key is set to exit the program.

The code that sets up the use of arrow keys are these 3 bind statements.  They cause events to be generated when those keys are pressed on the keyboard:
```python
window.bind('<Right>', '-NEXT-')
window.bind('<Left>', '-PREV-')
window.bind('<Down>', 'Exit')
```
    

<iframe src='https://trinket.io/embed/pygame/88c7cbc070?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
