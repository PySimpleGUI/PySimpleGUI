## Sudoku In a Line

This demo began as a demonstration of the many ways a Sudoku board could be created using PySimpleGUI.  It ended up being more complete application.  The "build-a-Sudoku-board" port of the code can be represented in a somewhat boring single line of code.

```python
sg.Window('Sudoku',[[sg.Frame('',[[sg.I(random.randint(1,9), justification='r', size=(3,1),key=(frow*3+row,fcol*3+col)) for col in range(3)] for row in range(3)]) for fcol in range(3)] for frow in range(3)]+ [[sg.B('Exit')]]).read()
```

This layout uses list comprehensions to create the classic Sudoku board that is 9 boxes each consisting of 9 numbers.  The single line of code produces this window when run on Windows 10:

![SNAG-0755.jpg](/api/files/5e98e7a84732c8c7199ef189/snag-0755.jpeg "SNAG-0755.jpg")

The board isn't a "valid" one.  It's filled with random digits. 

Building it out further required adding on a board generator and then a few fun features.  The board generation was discovered by searching through GitHub.  I finally settled on this elegantly simple implementaiton found in this GitHub Repository:

https://github.com/MorvanZhou/sudoku

A big thanks is thus owed to Morvan Zhou for creating these puzzles for our enjoyment.

You begin the game with a board much like this one:

![SNAG-0756.jpg](/api/files/5e98e8ff4732c8c7199ef6b8/snag-0756.jpeg "SNAG-0756.jpg")

You can check your progress at any point by clicking `Check`.  This will color each cell depending on the status of the cell.  

* If the answer is correct, the background will be white (or whatever is normal for the theme you're using)
* If the answer is incorrect, the background color will turn red
* If the answer is blank, the background will turn yellow

![SNAG-0757.jpg](/api/files/5e98e94c4732c8c7199ef83a/snag-0757.jpeg "SNAG-0757.jpg")

It makes it easy to see what you've won the game.   There's also a popup that's displayed when you click `Check` and the board has been correctly solved.  Click `Solve` and the answers are all filled in for you.

![SNAG-0758.jpg](/api/files/5e98e94c4732c8c7199ef83b/snag-0758.jpeg "SNAG-0758.jpg")

If you wish to start a new game click `New Game`.  The "Mask Rate" determines what percentage of the cells are erased at the beginning.

If you wish to run this program using Trinket without the debugger, the "Published" version is here:

https://pysimplegui.trinket.io/sites/sudoku


<iframe src='https://trinket.io/embed/pygame/bb346ef125?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
