Reddit Scraper - Status Update Front-End

If you want to see a fully functional Reddit search program that uses the Reddit PRAW APIs, then check out the [Reddit Search Demo Program](https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Reddit_Search.py) found on the PySimpleGUI GitHub.  

Waits for a Start button then simulates reading from Reddit and updating text in the window with the current posts's title.

You can choose the subs you want to read using the listbox and then click "Start Scrape" to loop through reading the subs.

If an "Abort" is desired, then a call to `window.read()` could be added and checked inside the download loop.  For now it's a simple get the list of subs and read each, displaying the information as it's read.

A progress meter runs along the bottom and varies depending on the number of entries in the sub.

Looks like this on Windows:

![Reddit Reader.gif](/api/files/5e04f4ace6d8746d7023661d/reddit-reader.gif "Reddit Reader.gif")

In response to Reddit post:

https://www.reddit.com/r/learnpython/comments/efw4c8/help_updating_tiles_on_tkinter_gui/

<iframe src='https://trinket.io/embed/pygame/833048e03d?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
