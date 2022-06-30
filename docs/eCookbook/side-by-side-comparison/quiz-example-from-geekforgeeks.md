## Comparing PySimpleGUI with tkinter

These are a fun exercise to go through... compare a tkinter solution to a problem with a PySimpleGUI solution.  I like doing them because I'm basically copying an image of a window.  It's easier to work on a problem when an image of the solution is provided.

A number of sites have excellent problems for Python programmers to work through.  Creating is how programming is learned.  Project-based learning is perhaps the best way to learn to program because you're directly applying what you've learned and often you're adding something new to your knowledge as well.

This problem is from the GeekforGeeks website.

https://www.geeksforgeeks.org/python-mcq-quiz-game-using-tkinter/

![quiz screenshot.jpg](/api/files/61e6f8960aadcd77670711b1/quiz-screenshot.jpeg "quiz screenshot.jpg")

As explained on the website, the data for the quiz is located in file named data.json.

### The PySimpleGUI Solution

Because I wanted to duplicate the window exactly, the normal PySimpleGUI themes were bypassed and the default gray was used. 

The only part of the window that's been hard coded is the width of the title across the top.  This was made extra wide to match the tkinter solution's hard coded window size.  Rather than hard coding the entire window size, the preferred PySimpleGUI technique is to allow PySimpleGUI to fit the window to the content's size.  If you want a larger window, then the best way to do that is to make the contents bigger.

For spacing, the pad parameter could have been used, but to keep the program simple, I decided to simply add a Text element with spaces onto rows.  It's more readable for the user and has no actual downside.

The code is significantly shorter... The actual lines of code is 35.   The tkinter version has 75.  Some of this is due to the json package being wrapped by PySimpleGUI in the UserSettings API.  There is a lot of whitespace in the tkinter version, so counting lines in the file is definitately not fair as the tkinter version is 219 lines and the PySimpleGUI version is 47 lines.


<iframe src='https://trinket.io/embed/pygame/a25af2eede?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>



### The tkinter Solution


<iframe src='https://trinket.io/embed/pygame/3052272fae?start=result' width='100%' height='600' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
