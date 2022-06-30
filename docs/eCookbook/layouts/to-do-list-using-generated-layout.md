**Generated Layouts - To Do List Program**

![SNAG-0492.jpg](https://user-images.githubusercontent.com/46163555/138909673-5af55647-509a-479b-9ba5-bc5d40465134.png)

This program demonstrates how you can a Python "List Comprehension" to create
a GUI layout. The layout is created in 3 steps.  
1. A title line
2. The list of checkboxes and descriptions
3. The buttons
 
That is the layout that these 3 lines of code create

```python
layout =  [[Text('My To Do List', font='Helvetica 15')]]
layout += [[Text(f'{i}. '), CBox('', key=f'-CB{i}-'), Input(k=f'-IN{i}-')] for i in range(1,6)]
layout += [[Button('Save'), Button('Load'), Button('Exit')]]
```

This program is a little different in that it imports the individual objects
being used.  Typically the import you'll find in most PySimpleGUI programs is

```python
import PySimpleGUI as sg
```

The result of importing each object is that you do not need the `sg.` before each function call, thus making the code even more compact.  The layout looks cleaner as well.

However, there are a few drawbacks.  One is being able to easily spot calls to the PySimpleGUI package.  Another is code completion.  If you type `sg.` (control+SPACE) in an IDE, it will show you a list of choices from the PySimpleGUI pacakge that are available to you.

It's being presented simply as another way of doing things.   You'll find the other demos use

```python
import PySimpleGUI as sg
```

<iframe src='https://trinket.io/embed/pygame/45e4bb64b8?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>

---

**To Do List using "normal" import (`import PySimpleGUI as sg`)**

In this version, the typical import statement is used.  The program is identical to the one above, but you'll notice that each element and PySimpleGUI object now has `sg.` in front of it.  Nearly all demo programs use this import convention and users have adopted it as well.  It's a standard of sorts at this point.


<iframe src='https://trinket.io/embed/pygame/3be33cd9ee?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
