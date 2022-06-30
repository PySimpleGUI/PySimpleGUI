## Tic Tac Toe 

In response to Reddit post:
https://www.reddit.com/r/learnpython/comments/iq4wfs/question_how_do_you_manage_events_lots_of_events/

The basic question is how to handle events coming from a large number of sources, or a large number of buttons in this case.

The answer is to use the information about the button along with a datastructure to record some information about it.  In this case, for Tic Tac Toe, the "Game Board" is where you want to record information.  You want to know if a spot is taken and if so, by who.

One simple way to do this is via a dictionary.  Record each spot that's been played in a dictionary.  The "key" will be the board location and the value will be which player played a piece there.

Because keys can be "anything" in PySimpleGUI (the exception is they cannot be lists), a tuple would be a good choice.  This gives you a (row, col) description of the piece and fits well visually too.  You can use the row, col in a loop to create the board.  Because list comprehensions can be used to create layouts, then it works out well to use row, col as the key.

This is how the window looks runnins on Windows:

![SNAG-0933.jpg](/api/files/5f5cf5e5a3ab12a454fa21dc/snag-0933.jpeg "SNAG-0933.jpg")


The main board is created with this single line of code:

```python
[[sg.Button(size=(3,1), key=(row,col)) for col in range(3)] for row in range(3)]
```

Because lists can be combined, it's possible to "build" a layout up from pieces.  In this case, there are 3 sections to the board.  There's a Text header at the top, then the board, then a couple of buttons on the bottom.  This layout can be built with 3 lines of code.   There's the initial Text Element at the top that starts the layout.  Then the board is added on and finally the buttons.  The layout creation is thus:

```python
layout =  [[sg.Text('X Starts First')]]
layout += [[sg.Button(size=(3,1), key=(row,col)) for col in range(3)] for row in range(3)]
layout += [[sg.Button('Reset'), sg.Button('Cancel')]]
```

The rest of the code is pretty self-explanatory.  It involves using a dictionary to store the locations that have been played and which player played that location.

Because the board is small, you'll want to click the upper left corner of the code display and choose the Display Full Screen option.

<iframe src='https://trinket.io/embed/pygame/09309ffae2?start=result' width='100%' height='450' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
