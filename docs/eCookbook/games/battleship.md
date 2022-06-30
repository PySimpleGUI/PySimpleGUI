**A GUI front-end for a Battleship or Minesweeper game**

This is not a complete game but rather a GUI that's ready for you to add your game logic to it.

There are 3 versions of this code, each with different levels of use of list comprehensions.

This window is a grid of buttons with each key being the row and column of the button.

It takes in clicks and will randomly change the button color and text that was clicked to either an "M" for Missing or "H" for hit. 

The idea here is to drop in the code for the hit/miss logic and call this code when a button is clicked.

The `layout` definition is unusual in this example compared to other PySimpleGUI programs.  Normally the layout is done all at one time, in a single statement `layout = [[.....]]`.  This code uses a "contactenated layout" because the buttons are created using a list comprehension.  

Note that these programs are using the new expanded Look and Feel Themes released in version 4.6 of PySimpleGUI.

Screenshot from Windows:

![BattleshipDarkBlue3.jpg](/api/files/5dd56d04cb1d4c4205acfe8f/battleshipdarkblue3.jpeg "BattleshipDarkBlue3.jpg")

**Implementation 1 - List Comprehension for Board**

<iframe src='https://trinket.io/embed/pygame/288c9a4396?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>

**Implementation 2 - List Comprehension for Board Rows**


<iframe src='https://trinket.io/embed/pygame/bcbf86a590?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>


**Implementation 3 - No List Comprehension**


<iframe src='https://trinket.io/embed/pygame/242e2828a4?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
