The classic Minesweeper game!

The user interface requirements for Minesweeper are a little unusual compared to most GUIs.  The use of the right mouse click to mark squares with flags is the most difficult part to implement in PySimpleGUI because right clicks are not normally passed along to the user.  

The specific action needed is the ability to right click on a `Button` and receive an event.  In version 4.11.0 of PySimpleGUI this capability was made easier with the addition of the `.bind` method for both Elements and Windows.  It is what is used to "bind" the right mouse button click to a button.

This implementation is based on a post made here:

https://learnku.com/articles/37714

There are 3 noteable changes:

1. Button keys were made into tuples instead of strings
2. Right mouse button clicks are received through `window.read()` calls instead of tkinter callbacks
3. Graphic images were moved into the source code by using Base64 images

The posted code was written prior to the `bind` method being available.

Because Trinket's display size is so small, the board size is limited to a 10 x 8 board.  Running on your local computer you'll want to change the display variables at the top to 24 x 14 and change the bombs from 10 to 80

On Windows the game looks really nice thanks to the author paying attention to the details and choosing nice graphics and by matching colors

![Minesweeper.png](/api/files/5df14d920dc187b112357f1a/minesweeper.png "Minesweeper.png")

To play this game in your browser using this Trinket, you'll probably want to play the "Published" version as it doesn't show the source code and provides a cleaner view of the application.

Here's the published version's linke:

https://pysimplegui.trinket.io/sites/minesweeper



<iframe src='https://trinket.io/embed/pygame/6db8011bff?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
