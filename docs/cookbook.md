

![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)  
    
# 2020 - Updates are in Progress

It's been a little while getting back around to the Cookbook.  As a result, some of the information was using older design patterns and some better examples need to be included.  There have been about 1/3 of the changes made so far that need to get made, so be patient.        
# The PySimpleGUI Cookbook      
      
Welcome to the PySimpleGUI Cookbook!  It's provided as but one component of a larger documentation effort for the PySimpleGUI package.  Its purpose is to give you a jump start.      
You'll find that starting with a Recipe will give you a big jump-start on creating your custom GUI.  Copy and paste one of these Recipes and modify it to match your requirements.  Study them to get an idea of some design patterns to follow.

This document is not a replacement for the main documentation at http://www.PySimpleGUI.org.  If you're looking for answers, they're most likely there in the detailed explanations and call definitions.  That document is updated much more frequently than this one.
  
See the main doc on installation.  Typically it's `pip install pysimplegui` to install.
  
# The "Demo Programs" Are Also Recipes

If you like this Cookbook, then you'll LOVE the 200 sample programs that are just like these.  You'll find them in the GitHub at http://Demos.PySimpleGUI.com.  They are located in the folder `DemoPrograms` and there is also a `Demo Programs` folder for each of the PySimpleGUI ports. 

These programs are updated frequently, much more so than this Cookbook document.  It's there that you'll find the largest potential for a big jump-start on your project.

These short Demo Programs fall into 3 categories:

1. Demonstrate a particular Element
2. Integration with another package (e.g. Matplotlib, OpenCV, etc)
3. Provide added functionality - more complex element combinations or extensions to elements

So, for example, if you're trying to use the Graph Element to create a line graph, check out the demo programs... there are 8 different demos for the Graph Element alone.


# Trinket, the Online PySimpleGUI Cookbook

More and more the recipes are moving online, away from this document and onto Trinket. http://Trinket.PySimpleGUI.org

You'll find a number of "recipes" running on Trinket.  The PySimpleGUI [Trinket Demo Programs](https://pysimplegui.trinket.io/demo-programs) are often accompanied by explanatory text.  Because it's an actively used educational capability, you'll find newer PySimpleGUI features demonstrated there.

The advantage to "live", online PySimpleGUI demos is that you can examine the source code, run it, and see the GUI in your browser window, without installing *anything* on your local machine.  No Python, no PySimpleGUI, only your browser is needed to get going.  

# [Repl.it](https://repl.it/@PySimpleGUI)... another online resource

The [PySimpleGUI repl.it repository](https://repl.it/@PySimpleGUI) is also used, but it doesn't provide the same kind of capability to provide some explanatory text and screenshots with the examples.  It does, however, automatically install the latest version of PySimpleGUI for many of the examples.  It also enables the demo programs to access any package that can be pip installed.  Trinket does not have this more expansive capability.  Some older demos are located there.  You can run PySimpleGUIWeb demos using Repl.it.
      

# Cookbook Purpose

A quick explanation about this document. The PySimpleGUI Cookbook is meant to get you started quickly.  But that's only part of the purpose.  The other, probably most important one, is *coding conventions*.  The more of these examples and the programs you see in the [Demo Programs](http://Demos.PySimpleGUI.org) section on the GitHub, the more familiar certain patterns will emerge.

It's through the Cookbook and the Demo Programs that new PySimpleGUI constructs and naming conventions are "rolled out" to the user community.  If you are brand new to PySimpleGUI, then you're getting your foundation here.  That foundation changes over time as the package improves.  The old code still runs, but as more features are developed and better practices are discovered, you'll want to be using newer examples and coding conventions. 

PEP8 names are a really good example.  Previously many of the method names for the Elements were done with CamelCase which is not a PEP8 compliant way of naming those functions.  They should have been snake_case.  Now that a complete set of PEP8 bindings is available, the method names are being changed here, in the primary documentation and in the demo programs.  `window.Read()` became `window.read()`.  It's better that you see examples using the newer `windows.read()` names.

In short, it's brainwashing you to program PySimpleGUI a certain way.  The effect is that one person has no problem picking up the code from another PySimpleGUI programmer and recognizing it.  If you stick with variable names shown here, like many other PySimpleGUI users have, then you'll understand other people's code (and the demos too) quicker.  So far, the coding conventions have been used by most all users.  It's improved efficiency for everyone.



# Keys

Keys are an extremely important concept for you to understand.  They are the labels/tags/names/identifiers you give Elements.  They are a way for you to communicate about a specific element with the PySimpleGUI API calls.  

Keys are used to:

* inform you when one of them generates an event
* change an element's value or settings
* communicate their value when performing a `window.read()`

**Important** - while they are shown as strings in many examples, they can be ANYTHING (ints, tuples, lists, objects, ....)

Keys are specified when you create an element using the `key` keyword parameter.  They are used to "find elements" so that you can perform actions on them.


# GETTING STARTED - Copy these design patterns!      
      
All of your PySimpleGUI programs will utilize one of these 2 design patterns depending on the type of window you're implementing.  The two types of windows are:

1. One-shot 
2. Persistent 

The **One-shot window** is one that pops up, collects some data, and then disappears.  It is more or less a 'form' meant to quickly grab some information and then be closed.

The **Persistent window** is one that sticks around.  With these programs, you loop, reading and processing "events" such as button clicks. It's more like a typical Windows/Mac/Linux  program.

If you are writing a "typical Windows program" where the window stays open while you collect multiple button clicks and input values, then you'll want Recipe Pattern 2B.

      
## Recipe -  Pattern 1A - "One-shot Window" - (The Simplest Pattern)    



![SNAG-0682](https://user-images.githubusercontent.com/46163555/75083298-0917fe00-54e6-11ea-96c8-b9b47132d546.jpg)


![SNAG-0683](https://user-images.githubusercontent.com/46163555/75083292-04534a00-54e6-11ea-92bb-57df74e05ec7.jpg)


This will be the most common pattern you'll follow if you are not using an "event loop" (not reading the window multiple times).  The window is read and then closed.
    
When you "read" a window, you are returned a tuple consisting of an `event` and a dictionary of `values`.  

The `event` is what caused the read to return. It could be a button press, some text clicked, a list item chosen, etc, or `None` if the user closes the window using the X.

The `values` is a dictionary of values of all the input-style elements.  Dictionaries use keys to define entries. If your elements do not specificy a key, one is provided for you. These auto-numbered keys are ints starting at zero.

This design pattern does not specify a `key` for the `InputText` element, so its key will be auto-numbered and is zero in this case.  Thus the design pattern can get the value of whatever was input by referencing `values[0]`
   
```python    
import PySimpleGUI as sg      

layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      
      
window = sg.Window('Window Title', layout)    
    
event, values = window.read()    
window.close()
    
text_input = values[0]    
sg.popup('You entered', text_input)
```    

If you want to use a key instead of an auto-generated key:

```python    
import PySimpleGUI as sg      

layout = [[sg.Text('My one-shot window.')],      
                 [sg.InputText(key='-IN-')],      
                 [sg.Submit(), sg.Cancel()]]      
      
window = sg.Window('Window Title', layout)    
    
event, values = window.read()    
window.close()
    
text_input = values['-IN-']    
sg.popup('You entered', text_input)
``` 


## Recipe -  Pattern 1B - "One-shot Window" - (Self-closing, single line)    

For a much more compact window, it's possible to create, display, read, and close a window in a single line of code.

```python
import PySimpleGUI as sg

event, values = sg.Window('Login Window',
                  [[sg.T('Enter your Login ID'), sg.In(key='-ID-')],
                  [sg.B('OK'), sg.B('Cancel') ]]).read(close=True)

login_id = values['-ID-']
```

The important part of this bit of code is `close=True`.  This is the parameter that instructs PySimpleGUI to close the window just before the read returns.

This is a single line of code, broken up to make reading the window layout easier.  It will display a window, let the user enter a value, click a button and then the window will close and execution will be returned to you with the variables `event` and `values` being returned.  

Notice use of Element name "Shortcuts" (uses `B` rather than `Button`, `T` instead of `Text`, `In` rather than `InputText`, etc.).  These shortcuts are fantastic to use when you have complex layouts.  Being able to "see" your entire window's definition on a single screen of code has huge benefits.  It's another tool to help you achieve simple code.



## Recipe - Pattern 2A - Persistent window (multiple reads using an event loop)      


![image](https://user-images.githubusercontent.com/46163555/68600333-5361fb80-0470-11ea-91cb-691e32832b60.png)


The more advanced/typical GUI programs operate with the window remaining visible on the screen.  Input values are collected, but rather than closing the window, it is kept visible acting as a way to both input and output information.  In other words, a typical Window, Mac or Linux window.  

*Let this sink in for a moment....* in 10 lines of Python code, you can display and interact with your own custom GUI window.  You are writing "*real GUI code*" (as one user put it) that will look and act like other windows you're used to using daily.
    
This code will present a window and will print values until the user clicks the exit button or closes window using an X.    

      
```python    
import PySimpleGUI as sg      

sg.theme('DarkAmber')    # Keep things interesting for your users

layout = [[sg.Text('Persistent window')],      
          [sg.Input(key='-IN-')],      
          [sg.Button('Read'), sg.Exit()]]      
      
window = sg.Window('Window that stays open', layout)      
      
while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event in (None, 'Exit'):      
        break      

window.close()
```    


Here is some sample output from this code:

```
Read {'-IN-': 'typed into input field'}
Read {'-IN-': 'More typing'}
Exit {'-IN-': 'clicking the exit button this time'}
```

The first thing printed is the "event" which in this program is the buttons.  The next thing printed is the `values` variable that holds the dictionary of return values from the read.  This dictionary has only 1 entry.  The "key" for the entry is `'-IN-'` and matches the key passed into the `Input` element creation on this line of code:
```python
          [sg.Input(key='-IN-')],      
```

If the window was close using the X, then the output of the code will be:
```
None {'-IN-': None}
```

The `event` returned from the read is set to `None` and so are the input fields in the window.  This `None` event is super-important to check for.  It must be detected in your windows or else you'll be trying to work with a window that's been destroyed and your code will crash.  This is why you will find this check after ***every*** `window.read()` call you'll find in sample PySimpleGUI code.

In some cirsumstances when a window is closed with an X, both of the return values from `window.read()` will be `None`.  This is why it's important to check for `event is None` before attempting to access anything in the `values` variable.


## Recipe - Pattern 2B - Persistent window (multiple reads using an event loop + updates data in window)   

![image](https://user-images.githubusercontent.com/46163555/68633697-df9c0f00-04c0-11ea-9fb3-121a72a87a59.png)

This is a slightly more complex, but more realistic version that reads input from the user and displays that input as text in the window.  Your program is likely to be doing both of those activities so this pattern will likely be your starting point.

Do not worry yet what all of these statements mean.  Just copy the template so you can start to experiment and discover  how PySimpleGUI programs work.


```python
import PySimpleGUI as sg

sg.theme('BluePurple')

layout = [[sg.Text('Your typed chars appear here:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Input(key='-IN-')],
          [sg.Button('Show'), sg.Button('Exit')]]

window = sg.Window('Pattern 2B', layout)

while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])

window.close()
```

To modify an Element in a window, you call its `update` method.  This is done in 2 steps.  First you lookup the element, then you call that element's `update` method.

The way we're achieving output here is by changing a Text Element with this statement:

```python
window['-OUTPUT-'].update(values['-IN-'])
```

`window['-OUTPUT-']` returns the element that has the key `'-OUTPUT-'`.  Then the `update` method for that element is called so that the value of the Text Element is modified.  Be sure you have supplied a `size` that is large enough to display your output. If the size is too small, the output will be truncated. 

If you need to interact with elements prior to calling `window.read()` you will need to "finalize" your window first using the `finalize` parameter when you create your `Window`. "Interacting" means calling that element's methods such as `update`, `draw_line`, etc.

------------

## Inside your event loop

For persistent windows, after creating the window, you have an event loop that runs until you exit the window. Inside this loop you will read values that are returned from reading the window and you'll operate on elements in your window.  To operate on elements, you look them up and call their method functions such as `update`.

### Old Style Element Lookups - FindElement

The original / old-style way of looking up elements using their key was to call `window.FindElement` or the shortened `window.Element`, passing in the element's key.

These 3 lines of code do the same thing.  The first line is the currently accepted way of performing this lookup operation and what you'll find in all of the current demos.

```python
window['-OUTPUT-']
window.FindElement('-OUTPUT-')
window.find_element('-OUTPUT-')
window.Element('-OUTPUT-')
```

### Element Operations

Once you lookup an element, the most often performed operation is `update`.  There are other element methods you can call such as `set_tooltip()`.  You'll find the list of operations available for each element in the [call summary](https://pysimplegui.readthedocs.io/en/latest/#element-and-function-call-reference) at the end of the main documentation.

To call any of these other methods, you do the element lookup, then add on the call such as this call to `set_tooltip`.

```python
window[my_key].set_tooltip('New Tooltip')
```

----

# Exiting a Window

For persistent windows, you will find this if statement immediately following every `window.read` call you'll find in this document and likely all of the demo programs:

```python
if event in (None, 'Quit'):
    break
```

This is your user's "way out".  **Always** give a way out to your user or else they will be using task manager or something else, all the while cursing you.

Beginners to Python may not understand this statement and it's important to understand it so that you don't simply ignore it because you don't understand the syntax.

The if statment is identical to this if statement:
```python
if event is None or event == 'Quit':
    break
```

The `event in (None, 'Quit')` simply means is the value of the `event` variable in the list of choices shown, in this case `None` or `Quit`.  If so, then break out of the Event Loop and likely exit the program when that happens for simple programs.

You may find 'Exit' instead of 'Quit' in some programs.  Or may find only `None` is checked.  Exit & Quit in this case refer to a Quit/Exit button being clicked. If your program doesn't have one, then you don't need to include it.


## Close Your Windows

When you're done with your window, close it.

```python
window.close()
```

The reason is that for some ports, like PySimpleGUIWeb, you cannot exit the program unless the window is closed.  It's nice to clean up after yourself too.


---------------------


# Coding Conventions

By following some simple coding conventions you'll be able to copy / paste demo program code into your code with minimal or no modifications.  Your code will be understandable by other PySimpleGUI programmers as well.
 
The primary *suggested* conventions are:

* `import PySimpleGUI as sg`
* Name your Window `window`
* Name the return values from reading your window `event` and `values`
* Name your layout `layout`
* Use `window[key]` to lookup elements
* For keys that are strings, follow this pattern `'-KEY-'`

Of course you don't have to follow *any* of these.  They're suggestions, but if you do follow them, your code is a lot easier to understand by someone else.

## Coding Tips

A few tips that have worked well for others.  In the same spirit as the coding conventions, these a few observations that may speed up your development or make it easier for others to understand your code. They're guidelines / tips / suggestions / ideas... meant to help you.

* Stay ***simple*** at every opportunity
* Read or search the documentation (http://www.PySimpleGUI.org)
* Use the coding conventions outlined above
* Write compact layouts
* Use "user defined elements" when you find yourself repeating parameters many times (functions that return elements)
* Use PySimpleGUI constructs rather than other GUI frameworks' constructs
* Use reasonable timeout values (as large of non-zero values as possible... be a good CPU citizen)
* Do not try to make any PySimpleGUI call from a thread
* Close your windows before exiting
* Make linear event loops
* Use the `values` dictionary rather than `Element.get` methods
* Look through Demo Programs for more tips / techniques (http://Demos.PySimpleGUI.org)

Most of these are self-explanatory or will be understood as you learn more about PySimpleGUI.  You won't now what a timeout value is at this point, but if/when you do use reads with timeouts, then you'll understand the tip.

A little more detail on a few of them that aren't obvious.

### Write compact layouts

Try to keep your layout definitions to a single screen of code.  Don't put every parameter on a new line.  Don't add tons of whitespace.  

If you've got a lot of elements, use the shortcut names (e.g. using `sg.B` rather than `sg.Button` saves 5 characters per button in your layout).

The idea here to be able to see your entire window in your code without having to scroll.

### Use PySimpleGUI constructs

PySimpleGUI programs were not designed using the same OOP design as the other Python GUI frameworks.  Trying to force fit them into an OOP design doesn't buy anything other then lots of `self.` scattered in your code, more complexity, and possibly more confusion

Of course your overall design can be OOP.  

The point is that there is no concept of an "App" or a never-ending event loop or callback functions.  PySimpleGUI is different than tkinter and Qt.  Trying to code in that style is likely to not result in success.  If you're writing a subclass for `Window` as a starting point, it's highly likely you're doing something wrong.


-----

# Themes - Window "Beautification"

"Beautiful windows" don't just happen, but coloring your window can be accomplished with 1 line of code.

One complaint about tkinter that is often heard is how "ugly" it looks.  You can do something about that by using PySimpleGUI themes.

```python
sg.theme('Dark Green 5')
```

A call to `theme` will set the colors to be used when creating windows.  It sets text color, background color, input field colors, button color,.... 13 different settings are changed.  

The default theme is "Dark Blue 3"

## Look and Feel Theme Explosion

There are currently 140 themes to choose from (in April 2020, maybe more by the time you read this) 

![SNAG-0620](https://user-images.githubusercontent.com/46163555/71361827-2a01b880-2562-11ea-9af8-2c264c02c3e8.jpg)

To see the above preview for your version of PySimpleGUI, make this call to generate a preview of all available themes:

```python
sg.theme_previewer()
```

Even windows that are created for you, such as popups, will use the color settings you specify.  And, you can change them at any point, even mid-way through defining a window layout.

This one line of code helps, but it's not the only thing that is going to make your window attractive. 


### Theme Name Format

You can look at the table of available themes to get the name of a theme you want to try, or you can "guess" at one using this formula:

`<"Dark" | "Light"> <Color> [#]`

Where Color is one of these:

`Black, Blue, Green, Teal, Brown, Yellow, Gray, Purple`

The # is optional and is used when there is more than 1 choice for a color.  For example, for "Dark Blue" there are 12 different themes (Dark Blue, and Dark Blue 1-11).  These colors specify the rough color of the background.  These can vary wildly so you'll have to try them out to see what you like the best.


## Recipe - Built-in Theme Viewer

If you want to see a window on your system like the above theme preview screenshot, then make this call and you'll see the same window:

```python
import PySimpleGUI as sg

sg.preview_all_look_and_feel_themes()
```

### Specifying and Getting Theme Names

In addition to getting all of these new themes, the format of the string used to specify them got "fuzzy".  You no longer have to specify the ***exact*** string shown in the preview.  Now you can add spaces, change the case, even move words around and you'll still get the correct theme.

For example the theme `"DarkBrown2"` can be specified also as `"Dark Brown 2"`.

If you can't remember the names and get it wrong, you'll get a text list of the available choices printed on your console.  

You can also get the list of theme names by calling `theme_list`

```python
import PySimpleGUI as sg

theme_name_list = sg.theme_list()
```

If you guess incorrectly, then you'll be treated to a random theme instead of some hard coded default.  You were calling theme to get more color, in theory, so instead of giving you a gray window, you'll get a randomly chosen theme (and you'll get the name of this theme printed on the console).  It's a great way to discover new color combinations via a mistake.

---


# Recipe - Theme Browser

This Recipe is a "Theme Browser" that enables you to see the different color schemes.

You're first shown this window that lists all of the available "Theme" settings.  This window was created after the Theme were set to "Dark Brown".

![image](https://user-images.githubusercontent.com/46163555/69106236-bee13580-0a3b-11ea-9eaa-f5f0282b1c63.png)

If you click on an item in the list, you will immediately get a popup window that is created using the new Theme.

![SNAG-0549](https://user-images.githubusercontent.com/46163555/68547123-a8880980-03ab-11ea-92f3-cb8d3136ae07.jpg)


```python
import PySimpleGUI as sg

"""
    Allows you to "browse" through the Theme settings.  Click on one and you'll see a
    Popup window using the color scheme you chose.  It's a simple little program that also demonstrates
    how snappy a GUI can feel if you enable an element's events rather than waiting on a button click.
    In this program, as soon as a listbox entry is clicked, the read returns.
"""

sg.theme('Dark Brown')


layout = [[sg.Text('Theme Browser')],
          [sg.Text('Click a Theme color to see demo window')],
          [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
          [sg.Button('Exit')]]

window = sg.Window('Theme Browser', layout)

while True:  # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    sg.theme(values['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

window.close()
```
----

## Making Changes to Themes & Adding Your Own Themes

Modifying and creating your own theme is not difficult.

The Theme definitions are stored in a dictionary.  The underlying dictionary can be directly accessed via the variable `LOOK_AND_FEEL_TABLE`.

A single entry in this dictionary has this format (copy this code):

```python
 'LightGreen3': {'BACKGROUND': '#A8C1B4',
               'TEXT': 'black',
               'INPUT': '#DDE0DE',
               'SCROLL': '#E3E3E3',
               'TEXT_INPUT': 'black',
               'BUTTON': ('white', '#6D9F85'),
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 1,
               'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0}
```

As you can see, a single entry in the Look and Feel dictionary is itself a dictionary.

---

## Recipe - Modifying an existing Theme

Let's say you like the `LightGreeen3` Theme, except you would like for the buttons to have black text instead of white.  You can change this by modifying the theme at runtime.

Normal use of `theme` calls is to retrieve a theme's setting such as the background color.  The functions used to retrieve a theme setting can also be used to modify the setting by passing in the new setting as a parameter.

Calling `theme_background_color()` returns the background color currently in use.  Passing in the color `'blue'` as the parameter, `theme_background_color('blue')`, will change the background color for future windows you create to blue. 


```python
import PySimpleGUI as sg

sg.theme('LightGreen3')
sg.popup_no_wait('This is the standard LightGreen3 Theme', 'It has white button text')

# Modify the theme 
sg.theme_button(('black', '#6D9F85'))

sg.popup('This is the modified LightGreen3 Theme', 'It has black button text')
```

Produces these 2 windows

![image](https://user-images.githubusercontent.com/46163555/69111481-b3960600-0a4b-11ea-83dc-4833897e7250.png)

----

## Recipe - Adding Your Own Color Theme

The great thing about these themes is that you set it onces and all future Elements will use the new settings.  If you're adding the same colors in your element definitions over and over then perhaps making your own theme is in order.

Let's say that you need to match a logo's green color and you've come up with matching other colors to go with it.  To add the new theme to the standard themes this code will do it:

```python
import PySimpleGUI as sg
# Add your new theme colors and settings
sg.LOOK_AND_FEEL_TABLE['MyNewTheme'] = {'BACKGROUND': '#709053',
                                        'TEXT': '#fff4c9',
                                        'INPUT': '#c7e78b',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL': '#c7e78b',
                                        'BUTTON': ('white', '#709053'),
                                        'PROGRESS': ('#01826B', '#D0D0D0'),
                                        'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        }
# Switch to use your newly created theme
sg.theme('MyNewTheme')
# Call a popup to show what the theme looks like
sg.popup_get_text('This how the MyNewTheme custom theme looks')      
```


![image](https://user-images.githubusercontent.com/46163555/69112494-5f405580-0a4e-11ea-9f20-1ea4e93f89bd.png)


----

## More Ways to "Dress Up Your Windows"

In addition to color there are a several of other ways to potentially make your window more attractive.  A few easy ones include:

* Remove the titlebar
* Make your window semi-transparent (change opacity)
* Replace normal buttons with graphics

You can use a combination of these 3 settings to create windows that look like Rainmeter style desktop-widgets.

This window demonstrates these settings.  As you can see, there is text showing through the background of the window.  This is because the "Alpha Channel" was set to a semi-transparent setting.  There is no titlebar going across the window and there is a little red X in the upper corner, resumably to close the window.

![image](https://user-images.githubusercontent.com/46163555/68679617-35f36700-052e-11ea-93b3-4f8507e3f4ee.png)


# Recipe Removing the Titlebar & Making Semi-Transparent

Both of these can be set when you create your window.  These 2 parameters are all you need - `no_titlebar` and `alpha_channel`.

When creating a window without a titlebar you create a problem where the user is unable to move your window as they have no titlebar to grab and drag.  Another parameter to the window creation will fix this problem - `grab_anywhere`.  When `True`, this parameter allows the user to move the window by clicking anywhere within the window and dragging it, just as if they clicked the titlebar.  Some PySimpleGUI ports allow you to click on input fields and drag, others require you to grab a spot on the background of the window.  Note - you do not have to remove the titlebar in order to use `grab_anywhere`

To make your window semi-transpaerent (change the opacity) use ghe `alhpa_channel` parameter when you create the window.  The setting is a float with valid values from 0 to 1.

To create a window like the one above, your window creation call would look something like:

```python
window = sg.Window('PSG System Dashboard', layout, no_titlebar=True, alpha_channel=.5, grab_anywhere=True)
```


## Recipe - Replacing a Button with a Graphic

In PySimpleGUI you can use PNG and GIF image files as buttons.  You can also encode those files into Base64 strings and put them directly into your code.

It's a 4 step process to make a button using a graphic

1. Find your PNG or GIF graphic
2. Convert your graphic into a Base64 byte string
3. Add Base64 string to your code as a variable
4. Specify the Base64 string as the image to use when creating your button

#### Step 1 - Find your graphic

There are a LOT of places for you to find your graphics.  [This page](https://savedelete.com/design/best-free-icon-search-engines/9644/#.UINbScWWvh4) lists a number of ways to search for what you need.  Bing also has a great image search tool that you can filter your results on to get a list of PNG files (choose "Transparent" using their "filter" on the page.)

Here's the [search results](https://www.bing.com/images/search?sp=-1&pq=red+x+i&sc=8-7&sk=&cvid=CAF7086A80704229B299A829D60F330E&q=red+x+icon&qft=+filterui:photo-transparent&FORM=IRFLTR) for "red x icon" using Bing with a filter.

I chose this one from the list:
http://icons.iconarchive.com/icons/iconarchive/red-orb-alphabet/256/Letter-X-icon.png

You can download your image or get a copy of the link to it.

#### Step 2 - Convert to Base64

One of the demo programs provided on the PySimpleGUI GitHub is called "Demo_Base64_Image_Encoder.py".  This program will convert all of the images in a folder and write the encoded data to a file named `output.py`.

Another demo program, "Demo_Base64_Single_Image_Encoder.py" will convert the input file to a base64 string and place the string onto the clipboard. Paste the result into your code and assign it to a variable. 

You can also use an online conversion tool such as https://base64.guru/converter/encode/image

On that page I chose to use the "Remote URL" (see above), pasted it into the input box and clicked "Encode image to Base64". Under the encode button is an area labeled "Base64".  If your conversion was successful, you'll see it filled with data like shown here:

![SNAG-0551](https://user-images.githubusercontent.com/46163555/68682006-6ccb7c00-0532-11ea-8053-4513e32b2017.jpg)


#### Step 3 - Make Base64 String Variable

Select all of the data in the Base64 box and paste into your code by making a variable that is equal to a byte-string.

```python
red_x_base64 = b''
```

Paste the long data you got from the webpage inside the quotes after the `b`.

You can also copy and paste the byte string from the `output.py` file if you used the demo program or paste the string created using the single file encoder demo program.

#### Step 4 - Use Base64 Variable to Make Your Button

This is the Button Element that is added to the layout to create the Red X Button graphic.

You need to set the background color for your button to be the same as the background the button is being placed on if you want it to appear invisible.

```python
sg.Button('', image_data=red_x_base64,
          button_color=(sg.theme_background_color(),sg.theme_background_color()),
          border_width=0, key='Exit')

```

This is the window the code below creates using a button graphic.

![image](https://user-images.githubusercontent.com/46163555/75083869-1f27bd80-54ea-11ea-9dcd-ca3f9ec76a12.png)

You can [run similar code online on Trinket](https://pysimplegui.trinket.io/demo-programs#/window-colors-and-graphics/base64-button-graphics)


```python
import PySimpleGUI as sg
# Note that the base64 string is quite long.  You can get the code from Trinket that includes the button
red_x_base64 = b'paste the base64 encoded string here'
red_x_base64 = sg.red_x     # Using this built-in little red X for this demo

layout = [  [sg.Text('My borderless window with a button graphic')],
            [sg.Button('', image_data=red_x_base64, 
            button_color=(sg.theme_background_color(),sg.theme_background_color()),border_width=0, key='Exit')]  ]

window = sg.Window('Window Title', layout, no_titlebar=True)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
window.close()
```

When working with PNG/GIF files as button images the background you choose for the button matters.  It should match the background of whatever it is being placed upon.  If you are using the standard "themes" interfaces to build your windows, then the color of the background can be found by calling `theme_background_color()`.  Buttons have 2 colors so be sure and pass in TWO color values when specifying buttons (text color, background color).


----


# Recipe - 1 Shot Window - Simple Data Entry - Return Values - Auto Numbered   

Remember how keys are **key** to understanding PySimpleGUI elements?  Well, they are, so now you know.

If you do not specify a key and the element is an input element, a key will be provided for you in the form of an integer, starting numbering with zero.  If you don't specify any keys, it will appear as if the values returned to you are being returned as a list because the keys are sequential ints.

This example has no keys specified.  The 3 input fields will have keys 0, 1, 2.  Your first input element will be accessed as `values[0]`, just like a list would look.


![SNAG-0550](https://user-images.githubusercontent.com/46163555/68547201-cace5700-03ac-11ea-81d6-cb171629e81b.jpg)    
      
```python
import PySimpleGUI as sg

sg.theme('Topanga')      # Add some color to the window

# Very basic window.  Return values using auto numbered keys

layout = [
    [sg.Text('Please enter your Name, Address, Phone')],
    [sg.Text('Name', size=(15, 1)), sg.InputText()],
    [sg.Text('Address', size=(15, 1)), sg.InputText()],
    [sg.Text('Phone', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.close()
print(event, values[0], values[1], values[2])    # the input data looks like a simple list when auto numbered
```    


--------------------------      

# Recipe - Add GUI to Front-End of Script 


![image](https://user-images.githubusercontent.com/46163555/75084200-83e41780-54ec-11ea-9dc1-b38d382d5f50.png)

Quickly add a GUI allowing the user to browse for a filename if a filename is not supplied on the command line using this simple GUI. It's the best of both worlds.  If you want command line, you can use it.  If you don't specify, then the GUI will fire up.


```python
import PySimpleGUI as sg
import sys

if len(sys.argv) == 1:
    event, values = sg.Window('My Script',
                    [[sg.Text('Document to open')],
                    [sg.In(), sg.FileBrowse()],
                    [sg.Open(), sg.Cancel()]]).read(close=True)
    fname = values[0]
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    sg.popup('The filename you chose was', fname)
```


If you really want to compress your 1-line of GUI code, you can directly access just the entered data by using this single-line-of-code solution.  Dunno if it's the safest way to go, but it's certainly the most compact.  Single line GUIs are fun when you can get away with them.

```python
import PySimpleGUI as sg
import sys

if len(sys.argv) == 1:
    fname = sg.Window('My Script',
                    [[sg.Text('Document to open')],
                    [sg.In(), sg.FileBrowse()],
                    [sg.Open(), sg.Cancel()]]).read(close=True)[1][0]
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    sg.popup('The filename you chose was', fname)
```



---

# Recipe - The `popup_get_file` Version of Add GUI to Front-End of Script

Why recreate the wheel?  There's a `Popup` function that will get a Filename for you.  This is a single-line GUI:

```python
fname = sg.popup_get_file('Document to open')
```

Shows this window and returns the results from the user interaction with it.

![image](https://user-images.githubusercontent.com/46163555/75084218-a9712100-54ec-11ea-843c-985087995f61.png)

The entire Popup based solution for this get filename example is:


```python
import PySimpleGUI as sg
import sys

if len(sys.argv) == 1:
    fname = sg.popup_get_file('Document to open')
else:
    fname = sys.argv[1]

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    sg.popup('The filename you chose was', fname)
```


How about a GUI **_and_** traditional CLI argument in 1 line of code?  

```python
import PySimpleGUI as sg
import sys

fname = sys.argv[1] if len(sys.argv) > 1 else sg.popup_get_file('Document to open')

if not fname:
    sg.popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
else:
    sg.popup('The filename you chose was', fname)
```

-------

# Recipe - Highly Responsive Inputs

Sometimes it's desireable to begin processing input information when a user makes a selection rather than requiring the user to click an OK button.

Let's say you've got a listbox of entries and a user can select an item from it.

```python
import PySimpleGUI as sg

choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse')

layout = [  [sg.Text('What is your favorite color?')],
            [sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-')],
            [sg.Button('Ok')]  ]

window = sg.Window('Pick a color', layout)

while True:                  # the event loop
    event, values = window.read()
    if event is None:
        break
    if event == 'Ok':
        if values['-COLOR-']:    # if something is highlighted in the list
            sg.popup(f"Your favorite color is {values['-COLOR-'][0]}")
window.close()
```

![image](https://user-images.githubusercontent.com/46163555/78260531-10123300-74cc-11ea-9050-83cbdd0dc978.png)

When you choose a color and click OK, a popup like this one is shown:

![image](https://user-images.githubusercontent.com/46163555/78260638-2d470180-74cc-11ea-949a-eca2eb7f2f5d.png)


## Use `enable_events` to instantly get events

That was simple enough.  But maybe you're impatient and don't want to have to cick "Ok".  Maybe you don't want an OK button at all.  If that's you, then you'll like the `enable_events` parameter that is available for nearly all elements.  Setting `enable_events` means that like button presses, when that element is interacted with (e.g. clicked on, a character entered into) then an event is immediately generated causing your `window.read()` call to return.

If the previous example were changed such that the OK button is removed and the `enable_events` parameter is added, then the code and window appear like this:

```python
import PySimpleGUI as sg

choices = ('Red', 'Green', 'Blue', 'Yellow', 'Orange', 'Purple', 'Chartreuse')

layout = [  [sg.Text('What is your favorite color?')],
            [sg.Listbox(choices, size=(15, len(choices)), key='-COLOR-', enable_events=True)] ]

window = sg.Window('Pick a color', layout)

while True:                  # the event loop
    event, values = window.read()
    if event is None:
        break
    if values['-COLOR-']:    # if something is highlighted in the list
        sg.popup(f"Your favorite color is {values['-COLOR-'][0]}")
window.close()
```

![image](https://user-images.githubusercontent.com/46163555/78261430-38e6f800-74cd-11ea-8789-dd82919d20fb.png)


You won't need to click the OK button anymore because as soon as you make the selection in the listbox the `read()` call returns and the popup will be displayed as before.

This second example code could be used with the OK button.  It doesn't matter what event caused the `window.read()` to return. The important thing is whether or not a valid selection was made.  The check for `event == 'Ok'` is actually not needed.


------

# Recipe - Input Validation

Sometimes you want to restrict what a use can input into a field.  Maybe you have a zipcode field and want to make sure only numbers are entered and it's no longer than 5 digits.  

Perhaps you need a floating point number and only want to allow `0`-`9`, `.`, and `-`.  One way restrict the user's input to only those characters is to get an event any time the user inputs a character and if the character isn't a valid one, remove it.

You've already seen (above) that to get an event immediate when an element is interacted with in some way you set the `enable_events` parameter.

```python
import PySimpleGUI as sg

"""
    Restrict the characters allowed in an input element to digits and . or -
    Accomplished by removing last character input if not a valid character
"""

layout = [  [sg.Text('Input only floating point numbers')],
            [sg.Input(key='-IN-', enable_events=True)],
            [sg.Button('Exit')]  ]

window = sg.Window('Floating point input validation', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    # if last character in input element is invalid, remove it
    if event == '-IN-' and values['-IN-'] and values['-IN-'][-1] not in ('0123456789.-'):
        window['-IN-'].update(values['-IN-'][:-1])
window.close()
```

This code only allows entry of the correct characters.

Note that this example does not fully validate that the entry is a valid floating point number, but rather that it has the correct characters.

If you wanted to take it a step further and verify that the entry is actually a valid floating point number, then you can change the "if" statement to test for valid floating point number.

```python
import PySimpleGUI as sg

"""
    Restrict the characters allowed in an input element to digits and . or -
    Accomplished by removing last character input if not a valid character
"""

layout = [  [sg.Text('Input only floating point numbers')],
            [sg.Input(key='-IN-', enable_events=True)],
            [sg.Button('Exit')]  ]

window = sg.Window('Floating point input validation', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    # if last character in input element is invalid, remove it
    if event == '-IN-' and values['-IN-']:
        try:
            in_as_float = float(values['-IN-'])
        except:
            if len(values['-IN-']) == 1 and values['-IN-'][0] == '-':
                continue
            window['-IN-'].update(values['-IN-'][:-1])
window.close()

```


---------

# Recipe - Printing

Outputting text is a very common operation in programming.  Your first Python program may have been

```python
print('Hello World')
```

But in the world of GUIs where do "prints" fit in?  Well, lots of places!  Of course you can still use the normal `print` statement.  It will output to StdOut (standard out) which is normally the shell where the program was launched from.  

Prining to the console becomes a problem however when you launch using `pythonw` on Windows or if you launch your program in some other way that doesn't have a console.  With PySimpleGUI you have many options available to you so fear not.  

These Recipes explore how to retain *prints already in your code*.  Let's say your code was written for a console and you want to migrate over to a GUI.  Maybe there are so many print statements that you don't want to modify every one of them individually.

There are at least 3 ways to transform your `print` statements that we'll explore here
1. The Debug window
2. The Output Element
3. The Multiline Element

The various forms of "print" you'll be introduced to all support the `sep` and `end` parameters that you find on normal print statements.


## Recipe - #1/3 Printing to Debug Window

The debug window acts like a virtual console.  There are 2 operating modes for the debug window.  One re-routes stdout to the window, the other does not.

### `Print` - Print to the Debug Window

The functions `Print`, `eprint`, `EasyPrint` all refer to the same funtion.   There is no difference whic hyou use as they point to identical code.  The one you'll see used in Demo Programs is `Print`.

One method for routing your print statements to the debuyg window is to reassign the `print` keyword to be the PySimpleGUI function `Print`.  This can be done through simple assignment.  

`print = sg.Print`

You can also remap stdout to the debug window by calling `Print` with the parameter `do_not_reroute_stdout = False`.  This will reroute all of your print statements out to the debug window.

```python
import PySimpleGUI as sg

sg.Print('Re-routing the stdout', do_not_reroute_stdout=False)
print('This is a normal print that has been re-routed.')
```

![SNAG-0744](https://user-images.githubusercontent.com/46163555/78322296-4f786800-753c-11ea-94eb-6321bc046e28.jpg)

While both `print` and `sg.Print` will output text to your Debug Window.  

***Printing in color is only operational if you do not reroute stdout to the debug window.***

If color printing is important, then don't reroute your stdout to the debug window.  Only use calls to `Print` without any change to the stdout settings and you'll be able to print in color.  

```python
import PySimpleGUI as sg

sg.Print('This text is white on a green background', text_color='white', background_color='green', font='Courier 10')
sg.Print('The first call sets some window settings like font that cannot be changed')
sg.Print('This is plain text just like a print would display')
sg.Print('White on Red', background_color='red', text_color='white')
sg.Print('The other print', 'parms work', 'such as sep', sep=',')
sg.Print('To not extend a colored line use the "end" parm', background_color='blue', text_color='white', end='')
sg.Print('\nThis line has no color.')
```

![image](https://user-images.githubusercontent.com/46163555/78385546-03640c80-75aa-11ea-8051-75285a1c1348.png)


--------

## Recipe - #2/3 Print to `Output` Element

If you want to re-route your standard out to your window, then placing an `Output` Element in your layout will do just that.  When you call "print", your text will be routed to that `Output` Element.  Note you can only have 1 of these in your layout because there's only 1 stdout.

Of all of the "print" techniques, this is the best to use if you cannot change your print statements.  The `Output` element is the best choice if your prints are in another module that you don't have control over such that "redefining / reassigning" what `print` does isn't a possibility.

This layout with an `Output` element shows the results of a few clicks of the Go Button. 

```python
import PySimpleGUI as sg

layout = [  [sg.Text('What you print will display below:')],
            [sg.Output(size=(50,10), key='-OUTPUT-')],
            [sg.In(key='-IN-')],
            [sg.Button('Go'), sg.Button('Clear'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Clear':
        window['-OUTPUT-'].update('')
window.close()
```

![image](https://user-images.githubusercontent.com/46163555/78387450-5ab7ac00-75ad-11ea-8a29-321a30db0248.png)

-----------------

## Recipe - #3/3 Print to `Multiline` Element

Beginning in 4.18.0 you can "print" to any `Multiline` Element in your layouts.  The `Multiline.print` method acts similar to the `Print` function described earlier.  It has the normal print parameters `sep` & `end` and also has color options.  It's like a super-charged `print` statement.

"Converting" expring print statements to output to a `Multiline` Element can be done by either

* Adding the `Multiline` element to the `print` statment so that it's calling the `Multiline.print` method
* Redefining `print`

### 3A Appending Element to `print` Statement to print to Multiline

Let's try the first option, adding the element onto the front of an existing `print` statement as well as using the color parameters.

The most basic form of converting your exiting `print` into a `Multline` based `print` is to add the same element-lookup code that you would use when calling an element's `update` method.  Generically, that conversion looks like this:

```python
print('Testing 1 2 3')
```

If our Multiline's key is '-ML-' then the expression to look the element up is:
```python
window['-ML-']
```

Combing the two transforms the original print to a `Multline` element print:
```python
window['-ML-'].print('Testing 1 2 3')
```

Because we're using these `Multilne` elements as output only elements, we don't want to have their contents returned in the values dictionary when we call `window.read()`.  To make any element not be included in the values dictionary, add the constant `WRITE_ONLY_KEY` onto the end of your key.  This would change our previous example to:

```python
window['-ML-'+sg.WRITE_ONLY_KEY].print('Testing 1 2 3')
```
When you define the multiline element in your layout, its key will need to have this suffix added too.

Combining all of this information into a full-program we arrive at this Recipe:

```python
import PySimpleGUI as sg

layout = [  [sg.Text('Demonstration of Multiline Element Printing')],
            [sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(40,8))],
            [sg.MLine(key='-ML2-'+sg.WRITE_ONLY_KEY,  size=(40,8))],
            [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout, finalize=True)


# Note, need to finalize the window above if want to do these prior to calling window.read()
window['-ML1-'+sg.WRITE_ONLY_KEY].print(1,2,3,4,end='', text_color='red', background_color='yellow')
window['-ML1-'+sg.WRITE_ONLY_KEY].print('\n', end='')
window['-ML1-'+sg.WRITE_ONLY_KEY].print(1,2,3,4,text_color='white', background_color='green')
counter = 0

while True:             # Event Loop
    event, values = window.read(timeout=100)
    if event in (None, 'Exit'):
        break
    if event == 'Go':
        window['-ML1-'+sg.WRITE_ONLY_KEY].print(event, values, text_color='red')
    window['-ML2-'+sg.WRITE_ONLY_KEY].print(counter)
    counter += 1
window.close()
```

It produces this window:


![image](https://user-images.githubusercontent.com/46163555/78400036-fbb16180-75c3-11ea-8261-f8b80a38d2e4.png)


There are a number of tricks and techniques burried in this Recpie so study it closely as there are a lot of options being used.



### 3B Redefining `print` to Print to `Multiline`

If you want to use the `Multline` element as the destination for your print, but you don't want to go through your code and modify every print statement by adding an element lookup, then you can simply redefine your call to `print` to either be a function that adds that multline element onto the print for you or a lambda expression if you want to make it a single line of code.  Yes, it's not suggested to use a lambda expression by assignment to a vairable, but sometimes it may be easier to understand.  Find the right balanace for you and ryour projct.


If you were to use a funciton, then your code my look like this:

```python
def mprint(*args, **kwargs):
    window['-ML1-' + sg.WRITE_ONLY_KEY].print(*args, **kwargs)

print = mprint
```

A named lambda expression would perhaps resemeble this:

```python
print = lambda *args, **kwargs: window['-ML1-' + sg.WRITE_ONLY_KEY].print(*args, **kwargs)
```

Putting it all together into a single block of code for you to copy and run results in
```python

def mprint(*args, **kwargs):
    window['-ML1-'+sg.WRITE_ONLY_KEY].print(*args, **kwargs)

print = mprint

# Optionally could use this lambda instead of the mprint function
# print = lambda *args, **kwargs: window['-ML1-' + sg.WRITE_ONLY_KEY].print(*args, **kwargs)

layout = [  [sg.Text('Demonstration of Multiline Element Printing')],
            [sg.MLine(key='-ML1-'+sg.WRITE_ONLY_KEY, size=(40,8))],
            [sg.MLine(key='-ML2-'+sg.WRITE_ONLY_KEY,  size=(40,8))],
            [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Window Title', layout, finalize=True)
print(1,2,3,4,end='', text_color='red', background_color='yellow')
print('\n', end='')
print(1,2,3,4,text_color='white', background_color='green')
counter = 0

# Switch to printing to second multiline
print = lambda *args, **kwargs: window['-ML2-' + sg.WRITE_ONLY_KEY].print(*args, **kwargs)


while True:             # Event Loop
    event, values = window.read(timeout=100)
    if event in (None, 'Exit'):
        break
    if event == 'Go':
        print(event, values, text_color='red')
    print(counter)
    counter += 1
window.close()

```


--------------      

# Recipe - Save and Load Program Settings


Some programs, in particular Desktop Widget like Rainmeter-style prorams, need to retain "state" or some series of settings.

This program is a tad large for a Cookbook, but it's a commmon enough feature to go ahead and include.  Besides, it may give you some ideas.

The idea here is that your program's settings are stored in a dictionary.  This dictionary is then written to disk and loaded from disk.

One type of program where this kind of feature is a requirement is when yuou make "rainmeter" tyle Desktop Widgets.  These little programs almost always need to store some kind of state.... everything from the transprency of the widget to the zip code your program uses to look up the weather.

The architecture is quite simple.  You keep your settings ina dictionary.  Your GUI settings window modifies the dictionary and eventually it's written to disk so that the next time you run the probgram you don't have to set up everyihng that's been saved previously.

The package used to save / load that data is the JSON package.  It makes writing and reading Python dictionaries downright trivial.  I use it as a simplified database.  You can also hand edit these files easily.

The portions of this Recipe you'll need to modify to integrate into your code will be:

* the default settings at the top
* the mapping table to/from settings keys to element keys
* the settings filename
* the settings window
* replace the "main" program with yours


The simple main program is there to trigger the change settings event:

![image](https://user-images.githubusercontent.com/46163555/78509070-61832200-7759-11ea-9b3e-a36a3faadbcb.png)


The more important window in this program is the settings window

![image](https://user-images.githubusercontent.com/46163555/78509043-34367400-7759-11ea-99fa-a7b66a58ef8f.png)

You'll be converting back and forth between the settings file contents and the values that come out of reading the settings GUI window.

Notice how creation of the window is done is a separate function in this Recipe so that you get a "fresh" layout every time the window is created. It's critical that you do not try to re-use elements.

If you're considering allowing the user to change your program's theme, then this is an excellent way to do that.  All that has to be done is to close your window when a new theme is chosen.  


```python


import PySimpleGUI as sg
from json import (load as jsonload, dump as jsondump)
from os import path

"""
    A simple "settings" implementation.  Load/Edit/Save settings for your programs
    Uses json file format which makes it trivial to integrate into a Python program.  If you can
    put your data into a dictionary, you can save it as a settings file.
    
    Note that it attempts to use a lookup dictionary to convert from the settings file to keys used in 
    your settings window.  Some element's "update" methods may not work correctly for some elements.
    
    Copyright 2020 PySimpleGUI.com
    Licensed under LGPL-3
"""

SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'max_users': 10, 'user_data_folder': None , 'theme': sg.theme(), 'zipcode' : '94102'}
# "Map" from the settings dictionary keys to the window's element keys
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'max_users': '-MAX USERS-', 'user_data_folder': '-USER FOLDER-' , 'theme': '-THEME-', 'zipcode' : '-ZIPCODE-'}

##################### Load/Save Settings File #####################
def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'No settings file found... will create one for you', keep_on_top=True, background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:      # if there are stuff specified by another window, fill in those values
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:  # update window with the values read from settings file
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings from window values. Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')

##################### Make a settings window #####################
def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text): return sg.Text(text+':', justification='r', size=(15,1))

    layout = [  [sg.Text('Settings', font='Any 15')],
                [TextLabel('Max Users'), sg.Input(key='-MAX USERS-')],
                [TextLabel('User Folder'),sg.Input(key='-USER FOLDER-'), sg.FolderBrowse(target='-USER FOLDER-')],
                [TextLabel('Zipcode'),sg.Input(key='-ZIPCODE-')],
                [TextLabel('Theme'),sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
                [sg.Button('Save'), sg.Button('Exit')]  ]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:   # update window with the values read from settings file
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

    return window

##################### Main Program Window & Event Loop #####################
def create_main_window(settings):
    sg.theme(settings['theme'])

    layout = [[sg.T('This is my main application')],
              [sg.T('Add your primary window stuff in here')],
              [sg.B('Ok'), sg.B('Exit'), sg.B('Change Settings')]]

    return sg.Window('Main Application', layout)


def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS )

    while True:             # Event Loop
        if window is None:
            window = create_main_window(settings)

        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == 'Change Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)
    window.close()
main()

```

----------


## Recipe - Get 2 Files By Browsing 
      
Sometimes you just need to get a couple of filenames.  Browse to get 2 file names that can be then compared.  By using `Input` elements the user can either use the Browse button to browse to select a file or they can paste the filename into the input element directly.    
      
![image](https://user-images.githubusercontent.com/46163555/69107788-9445ab80-0a40-11ea-87e2-3c5efe893ea0.png)   
      
```python
import PySimpleGUI as sg

sg.theme('Light Blue 2')

layout = [[sg.Text('Enter 2 files to comare')],
          [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse()],
          [sg.Text('File 2', size=(8, 1)), sg.Input(), sg.FileBrowse()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('File Compare', layout)

event, values = window.read()
window.close()
print(f'You clicked {event}')
print(f'You chose filenames {values[0]} and {values[1]}')
```      

This pattern is really good any time you've got a file or folder to get from the user.  By pairing an `Input` element with a browse button, you give the user the ability to do a quick paste if they've already got the path on the clipboard or they can click "Browse" and browse to get the filename/foldername.

-------


## Recipe - Get Filename With No Input Display.  Returns when file selected

![image](https://user-images.githubusercontent.com/46163555/75084589-11c10200-54ef-11ea-9096-58201dc3fb0f.png)

There are times when you don't want to display the file that's chosen and you want the program to start when the user chooses a file.  One way of doing this is to hide the input field that's filled in by the "Browse Button".  By enabling events for the input field, you'll get an event when that field is filled in.

```python
import PySimpleGUI as sg

sg.theme('Dark Red')

layout = [[sg.Text('Browse to a file')],
          [sg.Input(key='-FILE-', visible=False, enable_events=True), sg.FileBrowse()]]

event, values = sg.Window('File Compare', layout).read(close=True)

print(f'You chose: {values["-FILE-"]}')
```



--------------- 

## Nearly All Elements with Color Theme, Menus,  (The Everything Bagel)

Example of nearly all of the Elements in a single window.  Uses a customized color scheme, lots of Elements, default values, Columns, Frames with colored text, tooltips, file browsing.  There are at least 13 different Elements used.  

Before scrolling down to the code, guess how many lines of Python code were required to create this custom layout window.

      
![latest everything bagel](https://user-images.githubusercontent.com/13696193/45920376-22d89000-be71-11e8-8ac4-640f011f84d0.jpg)      
      
      
```python      
#!/usr/bin/env Python3      
import PySimpleGUI as sg      
    
sg.ChangeLookAndFeel('GreenTan')      
    
# ------ Menu Definition ------ #      
menu_def = [['File', ['Open', 'Save', 'Exit', 'Properties']],      
            ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
            ['Help', 'About...'], ]      
    
# ------ Column Definition ------ #      
column1 = [[sg.Text('Column 1', background_color='#F7F3EC', justification='center', size=(10, 1))],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      
    
layout = [      
    [sg.Menu(menu_def, tearoff=True)],      
    [sg.Text('All graphic widgets in one window!', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],    
    [sg.Text('Here is some text.... and a place to enter text')],      
    [sg.InputText('This is my text')],      
    [sg.Frame(layout=[      
    [sg.Checkbox('Checkbox', size=(10,1)),  sg.Checkbox('My second checkbox!', default=True)],      
    [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10,1)), sg.Radio('My second Radio!', "RADIO1")]], title='Options',title_color='red', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],      
    [sg.Multiline(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),      
        sg.Multiline(default_text='A second multi-line', size=(35, 3))],      
    [sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),      
        sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],      
    [sg.InputOptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],      
    [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),      
        sg.Frame('Labelled Group',[[      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25),      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),      
        sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),      
        sg.Column(column1, background_color='#F7F3EC')]])],      
    [sg.Text('_'  * 80)],      
    [sg.Text('Choose A Folder', size=(35, 1))],      
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
        sg.InputText('Default Folder'), sg.FolderBrowse()],      
    [sg.Submit(tooltip='Click to submit this window'), sg.Cancel()]    
]      
    
    
window = sg.Window('Everything bagel', layout, default_element_size=(40, 1), grab_anywhere=False)      
    
event, values = window.read()      

window.close()    

sg.popup('Title',      
            'The results of the window.',      
            'The button clicked was "{}"'.format(event),      
            'The values are', values)      

```
      
      
#### 35 lines of code

That's what the window definition, creation, display and get values ultimately ended up being when you remove the blank lines above.  Try displaying 13 seperate "GUI Widgets" in any of the GUI frameworks.  There's $20 waiting for the person that can code up the same window in under 35 lines of Python code using tkinter, WxPython, or Qt.  For compactness, it's difficult to beat PySimpleGUI simply because the PySimpleGUI code is running a ton of "boilerplate" code on your behalf.

-------------      

      
## Asynchronous Window With Periodic Update    

### Sync Versus Async Mode

It's possible, and even easy, to run your PySimpleGUI program in an "asynchronous" way.  

What does that even mean? 

There are 2 modes sync and async.  When running normally (synchronous), calls are made into the GUI ***stay*** in the GUI until something happens.  You call `window.read()` and wait for a button or some event that causes the `read` to return.

With async calls, you wait for an event for a certain amount of time and then you return after that amount of time if there's no event.  You don't wait forever for a new event. 

When running asynchronously, you are giving the illusion that multiple things are happening at the same time when in fact they are interwoven.

It means your program doesn't "block" or stop running while the user is interacting with the window.  Your program continues to run and does things while the user is fiddling around.  

The critical part of these async windows is to ensure that you are calling either `read` or `refresh` often enough.  Just because your code is running doesn't mean you can ignore the GUI.  We've all experienced what happens when a GUI program "locks up".  We're shown this lovely window.

![image](https://user-images.githubusercontent.com/46163555/75084725-133efa00-54f0-11ea-9bde-3e49695a17d5.png)

This happens when the GUI subsystem isn't given an opportunity to run for a long time.  Adding a sleep to your event loop will cause one of these to pop up pretty quickly.

We can "cheat" a little though.  Rather than being stuck inside the GUI code, we get control back, do a little bit of work, and then jump back into the GUI code.  If this is done quickly enough, you don't get the ugly little "not responding" window.

### Async Uses - Polling

Use this design pattern for projects that need to poll or output something on a regular basis.  In this case, we're indicating we want a `timeout=10` on our `window.read` call.  This will cause the `Read` call to return a "timeout key" as the event every 10 milliseconds has passed without some GUI thing happening first (like the user clicking a button).  The timeout key is `PySimpleGUI.TIMEOUT_KEY` usually written as `sg.TIMEOUT_KEY` in normal PySimpleGUI code.

Use caution when using windows with a timeout.  You should **rarely** need to use a `timeout=0`.  A zero value is a truly non-blocking call, so try not to abuse this design pattern.  You shouldn't use a timeout of zero unless you're a realtime application and you know what you're doing.  A zero value will consume 100% of the CPU core your code is running on. Abuse it an bad things ***will*** happen.

A note about timers... this is not a good design for a stopwatch as it can very easily drift. This would never pass for a good solution in a bit of commercial code.  For better accuracy always get the actual time from a reputable source, like the operating system.  Use that as what you use to measure and display the time.  

      
![image](https://user-images.githubusercontent.com/46163555/68599926-82c43880-046f-11ea-9901-84fae885ec8d.png)

 
      
```python      
import PySimpleGUI as sg

sg.theme('DarkBrown1')

layout = [  [sg.Text('Stopwatch', size=(20, 2), justification='center')],
            [sg.Text(size=(10, 2), font=('Helvetica', 20), justification='center', key='-OUTPUT-')],
            [sg.T(' ' * 5), sg.Button('Start/Stop', focus=True), sg.Quit()]]

window = sg.Window('Stopwatch Timer', layout)

timer_running, counter = True, 0

while True:                                 # Event Loop
    event, values = window.read(timeout=10) # Please try and use as high of a timeout value as you can
    if event in (None, 'Quit'):             # if user closed the window using X or clicked Quit button
        break
    elif event == 'Start/Stop':
        timer_running = not timer_running
    if timer_running:
        window['-OUTPUT-'].update('{:02d}:{:02d}.{:02d}'.format((counter // 100) // 60, (counter // 100) % 60, counter % 100))
        counter += 1
window.close()
```          

The `focus` parameter for the Button causes the window to start with that button having focus.  This will allow you to press the return key or spacebar to control the button.
      
--------      
      
## Callback Function Simulation      
The architecture of some programs works better with button callbacks instead of handling in-line.  While button callbacks are part of the PySimpleGUI implementation, they are not directly exposed to the caller.  The way to get the same result as callbacks is to simulate them with a recipe like this one.      
      
![image](https://user-images.githubusercontent.com/46163555/69109891-0ae5a780-0a47-11ea-8cc4-9442f46c7fa7.png)

```python      
import PySimpleGUI as sg

sg.theme('Light Blue 3')
# This design pattern simulates button callbacks
# This implementation uses a simple "Dispatch Dictionary" to store events and functions

# The callback functions
def button1():
    print('Button 1 callback')

def button2():
    print('Button 2 callback')

# Lookup dictionary that maps button to function to call
dispatch_dictionary = {'1':button1, '2':button2}

# Layout the design of the GUI
layout = [[sg.Text('Please click a button', auto_size_text=True)],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Quit()]]

# Show the Window to the user
window = sg.Window('Button callback example', layout)

# Event loop. Read buttons, make callbacks
while True:
    # Read the Window
    event, value = window.read()
    if event in ('Quit', None):
        break
    # Lookup event in function dictionary
    if event in dispatch_dictionary:
        func_to_call = dispatch_dictionary[event]   # get function from dispatch dictionary
        func_to_call()
    else:
        print('Event {} not in dispatch dictionary'.format(event))

window.close()

    # All done!
sg.popup_ok('Done')
```  

      
## OneLineProgressMeter      
      
This recipe shows just how easy it is to add a progress meter to your code.      
      
![image](https://user-images.githubusercontent.com/46163555/69110052-80517800-0a47-11ea-8c59-9d86aa3e851d.png)
 
      
```python      
import PySimpleGUI as sg

sg.theme('Dark Blue 8')

for i in range(1000):   # this is your "work loop" that you want to monitor
    sg.OneLineProgressMeter('One Line Meter Example', i + 1, 1000, 'key')
```      

Unlike other progress meter Python packages, PySimpleGUI's one-line-progress-meter is 1 line of code, not 2.  Historicly you would setup the meter outside your work loop and then update that meter inside of your loop.  With PySimpleGUI you do not need to setup the meter outside the loop.  You only need to add the line of code to update the meter insdie of your loop.
     
 -------

## Minesweeper-style Grid of Buttons

There are a number of applications built using a GUI that involve a grid of buttons.  The games Minesweeper and Battleship can both be thought of as a grid of buttons.

![image](https://user-images.githubusercontent.com/46163555/68539259-b5c2db00-034e-11ea-965a-16bd7f877f5b.png)

Here is the code for the above window

```python
import PySimpleGUIWeb as sg
from random import randint

MAX_ROWS = MAX_COL = 10
board = [[randint(0,1) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

layout =  [[sg.Button('?', size=(4, 2), key=(i,j), pad=(0,0)) for j in range(MAX_COL)] for i in range(MAX_ROWS)]

window = sg.Window('Minesweeper', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    # window[(row, col)].update('New text')   # To change a button's text, use this pattern
    # For this example, change the text of the button to the board's value and turn color black
    window[event].update(board[event[0]][event[1]], button_color=('white','black'))
window.close()

```


The **most important** thing for you to learn from this recipe is that keys and events can be **any type**, not just strings.  

Thinking about this grid of buttons, doesn't it make the most sense for you to get row, column information when a button is pressed.  Well, that's exactly what setting your keys for these buttons to be tuples does for you.  It gives you the abilty to read events and finding the button row and column, and it makes updating text or color of buttons using a row, column designation.

This program also runs on PySimpleGUIWeb really well.  Change the import to PySimpleGUIWeb and you'll see this in your web browser (assuming you've installed PySimpleGUIWeb)

![image](https://user-images.githubusercontent.com/46163555/68539298-3eda1200-034f-11ea-82bd-9f2ad479465b.png)

---



## Button Graphics (Media Player)      
Buttons can have PNG of GIF images on them.  This Media Player recipe requires 4 images in order to function correctly.  The background is set to the same color as the button background so that they blend together.      
      
![media player](https://user-images.githubusercontent.com/13696193/43958418-5dd133f2-9c79-11e8-9432-0a67007e85ac.jpg)      
      

```python
#!/usr/bin/env python
import PySimpleGUI as sg

#
# An Async Demonstration of a media player
# Uses button images for a super snazzy look
# See how it looks here:
# https://user-images.githubusercontent.com/13696193/43159403-45c9726e-8f50-11e8-9da0-0d272e20c579.jpg
#
def MediaPlayerGUI():
    background = '#F0F0F0'
    # Set the backgrounds the same as the background on the buttons
    sg.SetOptions(background_color=background, element_background_color=background)
    # Images are located in a subfolder in the Demo Media Player.py folder
    image_pause = './ButtonGraphics/Pause.png'
    image_restart = './ButtonGraphics/Restart.png'
    image_next = './ButtonGraphics/Next.png'
    image_exit = './ButtonGraphics/Exit.png'

    # A text element that will be changed to display messages in the GUI


    # define layout of the rows
    layout= [[sg.Text('Media File Player',size=(17,1), font=("Helvetica", 25))],
             [sg.Text(size=(15, 2), font=("Helvetica", 14), key='output')],
             [sg.Button('', button_color=(background,background),
                                image_filename=image_restart, image_size=(50, 50), image_subsample=2, border_width=0, key='Restart Song'),
                                sg.Text(' ' * 2),
              sg.Button('', button_color=(background,background),
                                image_filename=image_pause, image_size=(50, 50), image_subsample=2, border_width=0, key='Pause'),
                                sg.Text(' ' * 2),
              sg.Button('', button_color=(background,background), image_filename=image_next, image_size=(50, 50), image_subsample=2, border_width=0, key='Next'),
                                sg.Text(' ' * 2),
              sg.Text(' ' * 2), sg.Button('', button_color=(background,background),
                                image_filename=image_exit, image_size=(50, 50), image_subsample=2, border_width=0, key='Exit')],
             [sg.Text('_'*20)],
             [sg.Text(' '*30)],
            [
             sg.Slider(range=(-10, 10), default_value=0, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(-10, 10), default_value=0, size=(10, 20), orientation='vertical', font=("Helvetica", 15)),
             sg.Text(' ' * 2),
             sg.Slider(range=(-10, 10), default_value=0, size=(10, 20), orientation='vertical', font=("Helvetica", 15))],
             [sg.Text('   Bass', font=("Helvetica", 15), size=(9, 1)),
             sg.Text('Treble', font=("Helvetica", 15), size=(7, 1)),
             sg.Text('Volume', font=("Helvetica", 15), size=(7, 1))]
             ]

    # Open a form, note that context manager can't be used generally speaking for async forms
    window = sg.Window('Media File Player', layout, default_element_size=(20, 1),
                       font=("Helvetica", 25))
    # Our event loop
    while(True):
        event, values = window.read(timeout=100)        # Poll every 100 ms
        if event == 'Exit' or event is None:
            break
        # If a button was pressed, display it on the GUI by updating the text element
        if event != sg.TIMEOUT_KEY:
            window['output'].update(event)

MediaPlayerGUI()
```

## Script Launcher - Persistent Window    
This Window doesn't close after button clicks.  To achieve this the buttons are specified as `sg.Button` instead of `sg.Button`.   The exception to this is the EXIT button.  Clicking it will close the window.  This program will run commands and display the output in the scrollable window.    
      
![launcher 2](https://user-images.githubusercontent.com/13696193/43958519-b30af218-9c79-11e8-88da-fadc69da818c.jpg)      

```python      
    import PySimpleGUI as sg      
    import subprocess      
      
    # Please check Demo programs for better examples of launchers      
    def ExecuteCommandSubprocess(command, *args):      
        try:      
            sp = subprocess.Popen([command, *args], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)      
            out, err = sp.communicate()      
            if out:      
                print(out.decode("utf-8"))      
            if err:      
                print(err.decode("utf-8"))      
        except:      
            pass      
      
      
    layout = [      
        [sg.Text('Script output....', size=(40, 1))],      
        [sg.Output(size=(88, 20))],      
        [sg.Button('script1'), sg.Button('script2'), sg.Button('EXIT')],      
        [sg.Text('Manual command', size=(15, 1)), sg.InputText(focus=True), sg.Button('Run', bind_return_key=True)]      
            ]      
      
      
    window = sg.Window('Script launcher', layout)      
      
    # ---===--- Loop taking in user input and using it to call scripts --- #      
      
    while True:      
      (event, value) = window.read()      
      if event == 'EXIT'  or event is None:      
          break # exit button clicked      
      if event == 'script1':      
          ExecuteCommandSubprocess('pip', 'list')      
      elif event == 'script2':      
          ExecuteCommandSubprocess('python', '--version')      
      elif event == 'Run':      
          ExecuteCommandSubprocess(value[0])      
```    
     

## Launch a Program With a Button

Very simple script that will launch a program as a subprocess.  Great for making a desktop launcher toolbar.

```python
import subprocess  
import PySimpleGUI as sg  
  
CHROME = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  
  
  
layout = [  [sg.Text('Text area', key='_TEXT_')],  
            [sg.Input(key='_URL_')],  
            [sg.Button('Chrome'), sg.Button('Exit')]]  
  
window = sg.Window('Window Title', layuout)  
  
while True:             # Event Loop  
  event, values = window.read()  
    print(event, values)  
    if event is None or event == 'Exit':  
        break  
 if event == 'Chrome':  
        sp = subprocess.Popen([CHROME, values['_URL_']], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
  
window.close()
```

## Machine Learning GUI      
A standard non-blocking GUI with lots of inputs.      
      
![machine learning green](https://user-images.githubusercontent.com/13696193/43979000-408b77ba-9cb7-11e8-9ffd-24c156767532.jpg)      
```python     
    import PySimpleGUI as sg      
      
    # Green & tan color scheme      
    sg.ChangeLookAndFeel('GreenTan')      
      
    sg.SetOptions(text_justification='right')      
      
    layout = [[sg.Text('Machine Learning Command Line Parameters', font=('Helvetica', 16))],      
              [sg.Text('Passes', size=(15, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1)),      
               sg.Text('Steps', size=(18, 1)), sg.Spin(values=[i for i in range(1, 1000)], initial_value=20, size=(6, 1))],      
              [sg.Text('ooa', size=(15, 1)), sg.In(default_text='6', size=(10, 1)), sg.Text('nn', size=(15, 1)),      
               sg.In(default_text='10', size=(10, 1))],      
              [sg.Text('q', size=(15, 1)), sg.In(default_text='ff', size=(10, 1)), sg.Text('ngram', size=(15, 1)),      
               sg.In(default_text='5', size=(10, 1))],      
              [sg.Text('l', size=(15, 1)), sg.In(default_text='0.4', size=(10, 1)), sg.Text('Layers', size=(15, 1)),      
               sg.Drop(values=('BatchNorm', 'other'), auto_size_text=True)],      
              [sg.Text('_'  * 100, size=(65, 1))],      
              [sg.Text('Flags', font=('Helvetica', 15), justification='left')],      
              [sg.Checkbox('Normalize', size=(12, 1), default=True), sg.Checkbox('Verbose', size=(20, 1))],      
              [sg.Checkbox('Cluster', size=(12, 1)), sg.Checkbox('Flush Output', size=(20, 1), default=True)],      
              [sg.Checkbox('Write Results', size=(12, 1)), sg.Checkbox('Keep Intermediate Data', size=(20, 1))],      
              [sg.Text('_'  * 100, size=(65, 1))],      
              [sg.Text('Loss Functions', font=('Helvetica', 15), justification='left')],      
              [sg.Radio('Cross-Entropy', 'loss', size=(12, 1)), sg.Radio('Logistic', 'loss', default=True, size=(12, 1))],      
              [sg.Radio('Hinge', 'loss', size=(12, 1)), sg.Radio('Huber', 'loss', size=(12, 1))],      
              [sg.Radio('Kullerback', 'loss', size=(12, 1)), sg.Radio('MAE(L1)', 'loss', size=(12, 1))],      
              [sg.Radio('MSE(L2)', 'loss', size=(12, 1)), sg.Radio('MB(L0)', 'loss', size=(12, 1))],      
              [sg.Submit(), sg.Cancel()]]      
      
    window = sg.Window('Machine Learning Front End', layout, font=("Helvetica", 12))      
      
    event, values = window.read()      
```
      
-------      
## Custom Progress Meter / Progress Bar      
Perhaps you don't want all the statistics that the EasyProgressMeter provides and want to create your own progress bar. Use this recipe to do just that.      
      
![custom progress meter](https://user-images.githubusercontent.com/13696193/43982958-3393b23e-9cc6-11e8-8b49-e7f4890cbc4b.jpg)      
      
      
```python
import PySimpleGUI as sg

# layout the Window
layout = [[sg.Text('A custom progress meter')],
          [sg.ProgressBar(1000, orientation='h', size=(20, 20), key='progbar')],
          [sg.Cancel()]]

# create the Window
window = sg.Window('Custom Progress Meter', layout)
# loop that would normally do something useful
for i in range(1000):
    # check to see if the cancel button was clicked and exit loop if clicked
    event, values = window.read(timeout=0)
    if event == 'Cancel' or event is None:
        break
        # update bar with loop value +1 so that bar eventually reaches the maximum
    window['progbar'].update_bar(i + 1)
# done with loop... need to destroy the window as it's still open
window.close()
``` 
      
      
----      


   
## Multiple Columns      
  
A Column is required when you have a tall element to the left of smaller elements.      
      
In this example, there is a Listbox on the left that is 3 rows high.  To the right of it are 3 single rows of text and input. These 3 rows are in a Column Element.      
      
To make it easier to see the Column in the window, the Column background has been shaded blue.  The code is wordier than normal due to the blue shading.  Each element in the column needs to have the color set to match blue background.      
      
![cookbook columns](https://user-images.githubusercontent.com/13696193/45309948-f6c52280-b4f2-11e8-8691-a45fa0e06c50.jpg)      
      
      
```python      
    import PySimpleGUI as sg      
      
    # Demo of how columns work      
    # GUI has on row 1 a vertical slider followed by a COLUMN with 7 rows    
    # Prior to the Column element, this layout was not possible      
    # Columns layouts look identical to GUI layouts, they are a list of lists of elements.    
      
    sg.ChangeLookAndFeel('BlueMono')      
      
    # Column layout      
    col = [[sg.Text('col Row 1', text_color='white', background_color='blue')],      
           [sg.Text('col Row 2', text_color='white', background_color='blue'), sg.Input('col input 1')],      
           [sg.Text('col Row 3', text_color='white', background_color='blue'), sg.Input('col input 2')]]      
      
    layout = [[sg.Listbox(values=('Listbox Item 1', 'Listbox Item 2', 'Listbox Item 3'), select_mode=sg.LISTBOX_SELECT_MODE_MULTIPLE, size=(20,3)), sg.Column(col, background_color='blue')],      
              [sg.Input('Last input')],      
              [sg.OK()]]      
      
    # Display the Window and get values    
      
    event, values = sg.Window('Compact 1-line Window with column', layout).Read()  
      
    sg.popup(event, values, line_width=200)      
```      

----

      
## Persistent Window With Text Element Updates    
      
This simple program keep a window open, taking input values until the user terminates the program using the "X" button.    
      
![math game](https://user-images.githubusercontent.com/13696193/44537842-c9444080-a6cd-11e8-94bc-6cdf1b765dd8.jpg)      
      
      
```python     
import PySimpleGUI as sg      
    
layout = [ [sg.Txt('Enter values to calculate')],      
            [sg.In(size=(8,1), key='numerator')],      
            [sg.Txt('_'  * 10)],      
            [sg.In(size=(8,1), key='denominator')],      
            [sg.Txt('', size=(8,1), key='output')  ],      
            [sg.Button('Calculate', bind_return_key=True)]]      
    
window = sg.Window('Math', layout)      
    
while True:      
    event, values = window.read()      
    
    if event is not None:      
        try:      
            numerator = float(values['numerator'])      
            denominator = float(values['denominator'])      
            calc = numerator / denominator      
        except:      
            calc = 'Invalid'      
    
        window['output'].update(calc)      
    else:      
        break      
```      
      
## One Element Updating  Another - Compound Elements

![image](https://user-images.githubusercontent.com/13696193/49649095-1be40700-f9f6-11e8-981e-f56eb8404ae7.png)
   
You can easily build "compound elements" in a single like of code.  This recipe shows you how to add a numeric value onto a slider.

```python
import PySimpleGUI as sg  
  
layout = [[sg.Text('Slider Demonstration'), sg.Text('', key='_OUTPUT_')],  
            [sg.T('0',key='_LEFT_'),  
             sg.Slider((1,100), key='_SLIDER_', orientation='h', enable_events=True, disable_number_display=True),  
             sg.T('0', key='_RIGHT_')],  
            [sg.Button('Show'), sg.Button('Exit')]]  
  
window = sg.Window('Window Title', layout)  
  
while True:             # Event Loop  
  event, values = window.read()  
    print(event, values)  
    if event is None or event == 'Exit':  
        break  
  window['_LEFT_'].update(values['_SLIDER_'])  
    window['_RIGHT_'].update(values['_SLIDER_'])  
  
window.close()
```


## Multiple Windows

This recipe is a design pattern for multiple windows where the first window is not active while the second window is showing.  The first window is hidden to discourage continued interaction.


```Python
"""  
 PySimpleGUI The Complete Course Lesson 7 - Multiple Windows"""  
import PySimpleGUI as sg  
  
# Design pattern 1 - First window does not remain active  
  
layout = [[ sg.Text('Window 1'),],  
          [sg.Input()],  
          [sg.Text('', key='_OUTPUT_')],  
          [sg.Button('Launch 2')]]  
  
win1 = sg.Window('Window 1', layout)  
win2_active=False  
while True:  
    ev1, vals1 = win1.Read(timeout=100)  
    if ev1 is None:  
        break  
  win1.['_OUTPUT_'].update(vals1[0])  
  
    if ev1 == 'Launch 2'  and not win2_active:  
        win2_active = True  
  win1.Hide()  
        layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse  
  [sg.Button('Exit')]]  
  
        win2 = sg.Window('Window 2', layout2)  
        while True:  
            ev2, vals2 = win2.Read()  
            if ev2 is None or ev2 == 'Exit':  
                win2.Close()  
                win2_active = False  
  win1.UnHide()  
                break
```
   
## tkinter Canvas Widget      
      
The Canvas Element is one of the few tkinter objects that are directly accessible.  The tkinter Canvas widget itself can be retrieved from a Canvas Element like this:      
```python      
    can = sg.Canvas(size=(100,100))      
    tkcanvas = can.TKCanvas      
    tkcanvas.create_oval(50, 50, 100, 100)      
```
      
While it's fun to scribble on a Canvas Widget, try Graph Element makes it a downright pleasant experience.  You do not have to worry about the tkinter coordinate system and can instead work in your own coordinate system.      
      
      
![canvas](https://user-images.githubusercontent.com/13696193/44632429-5266ac00-a948-11e8-9ee0-664103c40178.jpg)      
      
```python    
    import PySimpleGUI as sg      
      
    layout = [      
        [sg.Canvas(size=(100, 100), background_color='red', key= 'canvas')],      
        [sg.T('Change circle color to:'), sg.Button('Red'), sg.Button('Blue')]      
        ]      
      
    window = sg.Window('Canvas test', layout)      
    window.Finalize()      
      
    canvas = window['canvas')      
    cir = canvas.TKCanvas.create_oval(50, 50, 100, 100)      
      
    while True:      
        event, values = window.read()      
        if event is None:      
            break      
        if event == 'Blue':      
            canvas.TKCanvas.itemconfig(cir, fill="Blue")      
        elif event == 'Red':      
            canvas.TKCanvas.itemconfig(cir, fill="Red")      
```            
      
## Graph Element - drawing circle, rectangle, etc, objects      
      
Just like you can draw on a tkinter widget, you can also draw on a Graph Element.  Graph Elements are easier on the programmer as you get to work in your own coordinate system.      
      
![graph recipe](https://user-images.githubusercontent.com/13696193/45920640-751bb000-be75-11e8-9530-45b71cbae07d.jpg)      
      
```python      
    import PySimpleGUI as sg      
      
    layout = [      
               [sg.Graph(canvas_size=(400, 400), graph_bottom_left=(0,0), graph_top_right=(400, 400), background_color='red', key='graph')],      
               [sg.T('Change circle color to:'), sg.Button('Red'), sg.Button('Blue'), sg.Button('Move')]      
               ]      
      
    window = sg.Window('Graph test', layout)      
    window.Finalize()      
      
    graph = window['graph')      
    circle = graph.DrawCircle((75,75), 25, fill_color='black',line_color='white')      
    point = graph.DrawPoint((75,75), 10, color='green')      
    oval = graph.DrawOval((25,300), (100,280), fill_color='purple', line_color='purple'  )      
    rectangle = graph.DrawRectangle((25,300), (100,280), line_color='purple'  )      
    line = graph.DrawLine((0,0), (100,100))      
      
    while True:      
        event, values = window.read()      
        if event is None:      
            break      
        if event is 'Blue':      
            graph.TKCanvas.itemconfig(circle, fill = "Blue")      
        elif event is 'Red':      
            graph.TKCanvas.itemconfig(circle, fill = "Red")      
        elif event is 'Move':      
            graph.MoveFigure(point, 10,10)      
            graph.MoveFigure(circle, 10,10)      
            graph.MoveFigure(oval, 10,10)      
            graph.MoveFigure(rectangle, 10,10)      
```      
      
## Keypad Touchscreen Entry - Input Element Update      
      
This Recipe implements a Raspberry Pi touchscreen based keypad entry.  As the digits are entered using the buttons, the Input Element above it is updated with the input digits.      
There are a number of features used in this Recipe including:      
* Default Element Size      
* auto_size_buttons      
* Button      
* Dictionary Return values      
* Update of Elements in window (Input, Text)     
      
      
![image](https://user-images.githubusercontent.com/46163555/68538641-ece0be80-0345-11ea-86b2-35c6208e2840.png)

      
```python    
import PySimpleGUI as sg

layout = [[sg.Text('Enter Your Passcode')],
          [sg.Input(size=(10, 1), justification='right', key='input')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3')],
          [sg.Button('4'), sg.Button('5'), sg.Button('6')],
          [sg.Button('7'), sg.Button('8'), sg.Button('9')],
          [sg.Button('Submit'), sg.Button('0'), sg.Button('Clear')],
          [sg.Text(size=(15, 1), font=('Helvetica', 18), text_color='red', key='out')]]

window = sg.Window('Keypad', layout, default_button_element_size=(5,2), auto_size_buttons=False)

# Loop forever reading the window's values, updating the Input field
keys_entered = ''
while True:
    event, values = window.read()  # read the window
    if event is None:  # if the X button clicked, just exit
        break
    if event == 'Clear':  # clear keys if clear button
        keys_entered = ''
    elif event in '1234567890':
        keys_entered = values['input']  # get what's been entered so far
        keys_entered += event  # add the new digit
    elif event == 'Submit':
        keys_entered = values['input']
        window['out'].update(keys_entered)  # output the final string

    window['input'].update(keys_entered)  # change the window to reflect current key string   
```

----

## Matplotlib Window With GUI Window

There are 2 ways to use PySimpleGUI with Matplotlib.  Both use the standard tkinter based Matplotlib.

The simplest is when both the interactive Matplotlib window and a PySimpleGUI window are running at the same time.  

First the PySimpleGUI window appears giving you 3 options.

![image](https://user-images.githubusercontent.com/46163555/68538920-23203d00-034a-11ea-9e3d-9b2a87d47824.png)

Clicking "Plot" will create the Matplotlib window

![image](https://user-images.githubusercontent.com/46163555/68538926-2a474b00-034a-11ea-8da4-772498314656.png)

You can click the "Popup" button in the PySimpleGUI window and you'll see a popup window, proving the your GUI is still alive and operational.


```python
import PySimpleGUI as sg
import matplotlib.pyplot as plt

"""
    Simultaneous PySimpleGUI Window AND a Matplotlib Interactive Window
    A number of people have requested the ability to run a normal PySimpleGUI window that
    launches a MatplotLib window that is interactive with the usual Matplotlib controls.
    It turns out to be a rather simple thing to do.  The secret is to add parameter block=False to plt.show()
"""

def draw_plot():
    plt.plot([0.1, 0.2, 0.5, 0.7])
    plt.show(block=False)

layout = [[sg.Button('Plot'), sg.Cancel(), sg.Button('Popup')]]

window = sg.Window('Have some Matplotlib....', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    elif event == 'Plot':
        draw_plot()
    elif event == 'Popup':
        sg.popup('Yes, your application is still running')
window.close()

```


----

      
## Animated Matplotlib Graph      
      
Use the Canvas Element to create an animated graph.  The code is a bit tricky to follow, but if you know Matplotlib then this recipe shouldn't be too difficult to copy and modify.      
      
![animated matplotlib](https://user-images.githubusercontent.com/13696193/44640937-91b9ea80-a992-11e8-9c1c-85ae74013679.jpg)      
      
      
```python
from tkinter import *
from random import randint
import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, FigureCanvasAgg
from matplotlib.figure import Figure
import matplotlib.backends.tkagg as tkagg
import tkinter as Tk

fig = Figure()

ax = fig.add_subplot(111)
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.grid()

layout = [[sg.Text('Animated Matplotlib', size=(40, 1), justification='center', font='Helvetica 20')],
          [sg.Canvas(size=(640, 480), key='canvas')],
          [sg.Button('Exit', size=(10, 2), pad=((280, 0), 3), font='Helvetica 14')]]

# create the window and show it without the plot    


window = sg.Window('Demo Application - Embedding Matplotlib In PySimpleGUI', layout)
window.Finalize()  # needed to access the canvas element prior to reading the window

canvas_elem = window['canvas')

graph = FigureCanvasTkAgg(fig, master=canvas_elem.TKCanvas)
canvas = canvas_elem.TKCanvas

dpts = [randint(0, 10) for x in range(10000)]
# Our event loop      
for i in range(len(dpts)):
    event, values = window.read(timeout=20)
    if event == 'Exit' or event is None:
        exit(69)

    ax.cla()
    ax.grid()

    ax.plot(range(20), dpts[i:i + 20], color='purple')
    graph.draw()
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = Tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)

    canvas.create_image(640 / 2, 480 / 2, image=photo)

    figure_canvas_agg = FigureCanvasAgg(fig)
    figure_canvas_agg.draw()

    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)      

```
 
 ---------



## Tight Layout with Button States      
      
Saw this example layout written in tkinter and liked it so much I duplicated the interface.  It's "tight", clean, and has a nice dark look and feel.      
      
This Recipe also contains code that implements the button interactions so that you'll have a template to build from.      
      
In other GUI frameworks this program would be most likely "event driven" with callback functions being used to communicate button events.  The "event loop" would be handled by the GUI engine.  If code already existed that used a call-back mechanism, the loop in the example code below could simply call these callback functions directly based on the button text it receives in the window.read call.      
      
![timemanagement](https://user-images.githubusercontent.com/13696193/44996818-0f27c100-af78-11e8-8836-9ef6164efe3b.jpg)      
      
```python      
    import PySimpleGUI as sg      
    """      
    Demonstrates using a "tight" layout with a Dark theme.      
    Shows how button states can be controlled by a user application.  The program manages the disabled/enabled      
    states for buttons and changes the text color to show greyed-out (disabled) buttons      
    """      
      
    sg.ChangeLookAndFeel('Dark')      
    sg.SetOptions(element_padding=(0,0))      
      
    layout = [[sg.T('User:', pad=((3,0),0)), sg.OptionMenu(values = ('User 1', 'User 2'), size=(20,1)), sg.T('0', size=(8,1))],      
              [sg.T('Customer:', pad=((3,0),0)), sg.OptionMenu(values=('Customer 1', 'Customer 2'), size=(20,1)), sg.T('1', size=(8,1))],      
              [sg.T('Notes:', pad=((3,0),0)), sg.In(size=(44,1), background_color='white', text_color='black')],      
              [sg.Button('Start', button_color=('white', 'black'), key='Start'),      
               sg.Button('Stop', button_color=('white', 'black'), key='Stop'),      
               sg.Button('Reset', button_color=('white', 'firebrick3'), key='Reset'),      
               sg.Button('Submit', button_color=('white', 'springgreen4'), key='Submit')]      
              ]      
      
    window = sg.Window("Time Tracker", layout, default_element_size=(12,1), text_justification='r', auto_size_text=False, auto_size_buttons=False,      
                       default_button_element_size=(12,1))      
    window.Finalize()      
    window['Stop'].update(disabled=True)      
    window['Reset'].update(disabled=True)      
    window['Submit'].update(disabled=True)      
    recording = have_data = False      
    while True:      
        event, values = window.read()      
        print(event)      
        if event is None:      
            exit(69)      
        if event is 'Start':      
            window['Start'].update(disabled=True)      
            window['Stop'].update(disabled=False)      
            window['Reset'].update(disabled=False)      
            window['Submit'].update(disabled=True)      
            recording = True      
         elif event is 'Stop'  and recording:      
            window['Stop'].update(disabled=True)      
            window['Start'].update(disabled=False)      
            window['Submit'].update(disabled=False)      
            recording = False      
            have_data = True      
         elif event is 'Reset':      
            window['Stop'].update(disabled=True)      
            window['Start'].update(disabled=False)      
            window['Submit'].update(disabled=True)      
            window['Reset'].update(disabled=False)      
            recording = False      
            have_data = False      
         elif event is 'Submit'  and have_data:      
            window['Stop'].update(disabled=True)      
            window['Start'].update(disabled=False)      
            window['Submit'].update(disabled=True)      
            window['Reset'].update(disabled=False)      
            recording = False      
```      
      
## Password Protection For Scripts      
      
You get 2 scripts in one.      
      
Use the upper half to generate your hash code.  Then paste it into the code in the lower half.  Copy and paste lower 1/2 into your code to get password protection for your script without putting the password into your source code.      
      
![password entry](https://user-images.githubusercontent.com/13696193/45129440-ab58f000-b151-11e8-8ebe-e519a50b3ead.jpg)      
      
![password hash](https://user-images.githubusercontent.com/13696193/45129441-ab58f000-b151-11e8-8a46-c2789bb7824e.jpg)      
      
```python
    import PySimpleGUI as sg      
    import hashlib      
      
    '''      
         Create a secure login for your scripts without having to include your password    in the program.  Create an SHA1 hash code for your password using the GUI. Paste into variable in final program      
         1. Choose a password      
         2. Generate a hash code for your chosen password by running program and entering 'gui' as the password      
         3. Type password into the GUI      
         4. Copy and paste hash code Window GUI into variable named login_password_hash    
         5. Run program again and test your login!      
    '''      
      
    # Use this GUI to get your password's hash code      
    def HashGeneratorGUI():      
        layout = [[sg.T('Password Hash Generator', size=(30,1), font='Any 15')],      
                  [sg.T('Password'), sg.In(key='password')],      
                  [sg.T('SHA Hash'), sg.In('', size=(40,1), key='hash')],      
                  ]      
      
        window = sg.Window('SHA Generator', layout, auto_size_text=False, default_element_size=(10,1),      
                           text_justification='r', return_keyboard_events=True, grab_anywhere=False)  
      
      
        while True:      
            event, values = window.read()      
            if event is None:      
                  exit(69)      
      
            password = values['password']      
            try:      
                password_utf = password.encode('utf-8')      
                sha1hash = hashlib.sha1()      
                sha1hash.update(password_utf)      
                password_hash = sha1hash.hexdigest()      
                window['hash'].update(password_hash)      
            except:      
                pass      
      
    # ----------------------------- Paste this code into your program / script -----------------------------      
    # determine if a password matches the secret password by comparing SHA1 hash codes      
    def PasswordMatches(password, hash):      
        password_utf = password.encode('utf-8')      
        sha1hash = hashlib.sha1()      
        sha1hash.update(password_utf)      
        password_hash = sha1hash.hexdigest()      
        if password_hash == hash:      
            return True      
         else:      
            return False      
      
    login_password_hash = '5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8'      
    password = sg.popup_get_text('Password', password_char='*')      
    if password == 'gui':                # Remove when pasting into your program      
      HashGeneratorGUI()               # Remove when pasting into your program      
      exit(69)                         # Remove when pasting into your program      
    if PasswordMatches(password, login_password_hash):      
        print('Login SUCCESSFUL')      
    else:      
        print('Login FAILED!!')      
```      
      
## Desktop Floating Toolbar      
      
#### Hiding your windows commmand window      
For this and the Time & CPU Widgets you may wish to consider using a tool or technique that will hide your Windows Command Prompt window.  I recommend the techniques found on this site:      
      
[http://www.robvanderwoude.com/battech_hideconsole.php](http://www.robvanderwoude.com/battech_hideconsole.php)      
      
At the moment I'm using the technique that involves wscript and a script named RunNHide.vbs.  They are working beautifully.  I'm using a hotkey program and launch by using this script with the command "python.exe insert_program_here.py".   I guess the next widget should be one that shows all the programs launched this way so you can kill any bad ones.  If you don't properly catch the exit button on your window then your while loop is going to keep on working while your window is no longer there so be careful in your code to always have exit explicitly handled.    
      
      
### Floating toolbar      
      
This is a cool one!  (Sorry about the code pastes... I'm working in it)      
      
Impress your friends at what a tool-wizard you are by popping a custom toolbar that you keep in the corner of your screen.  It stays on top of all your other windows.      
      
      
      
      
![toolbar gray](https://user-images.githubusercontent.com/13696193/45324308-bfb73700-b51b-11e8-90e7-ab24f3d6e61d.jpg)      
      
You can easily change colors to match your background by changing a couple of parameters in the code.      
      
![toolbar black](https://user-images.githubusercontent.com/13696193/45324307-bfb73700-b51b-11e8-8709-6c3c23f737c4.jpg)      
      
```python      
    import PySimpleGUI as sg      
    import subprocess      
    import os      
    import sys      
      
    """      
     Demo_Toolbar - A floating toolbar with quick launcher     One cool PySimpleGUI demo. Shows borderless windows, grab_anywhere, tight button layout      
     You can setup a specific program to launch when a button is clicked, or use the Combobox to select a .py file found in the root folder, and run that file.  """      
      
    ROOT_PATH = './'      
      
    def Launcher():      
      
        def print(line):      
            window['output'].update(line)      
      
        sg.ChangeLookAndFeel('Dark')      
      
        namesonly = [f for f in os.listdir(ROOT_PATH) if f.endswith('.py') ]      
      
        sg.SetOptions(element_padding=(0,0), button_element_size=(12,1), auto_size_buttons=False)      
        layout =  [[sg.Combo(values=namesonly, size=(35,30), key='demofile'),      
                    sg.Button('Run', button_color=('white', '#00168B')),      
                    sg.Button('Program 1'),      
                    sg.Button('Program 2'),      
                    sg.Button('Program 3', button_color=('white', '#35008B')),      
                    sg.Button('EXIT', button_color=('white','firebrick3'))],      
                    [sg.T('', text_color='white', size=(50,1), key='output')]]      
      
        window = sg.Window('Floating Toolbar', layout, no_titlebar=True, keep_on_top=True)
      
        # ---===--- Loop taking in user input (events) --- #      
        while True:      
            (event, value) = window.read()      
            if event ==  'EXIT'  or event is None:      
                break # exit button clicked      
            if event ==  'Program 1':      
                print('Run your program 1 here!')      
            elif event ==  'Program 2':      
                print('Run your program 2 here!')      
            elif event ==  'Run':      
                file = value['demofile']      
                print('Launching %s'%file)      
                ExecuteCommandSubprocess('python', os.path.join(ROOT_PATH, file))      
            else:      
                print(event)      
      
    def ExecuteCommandSubprocess(command, *args, wait=False):      
        try:      
            if sys.platwindow == 'linux':      
                arg_string = ''      
                for arg in args:      
                     arg_string += ' '  + str(arg)      
                sp = subprocess.Popen(['python3'  + arg_string, ], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)      
            else:      
                sp = subprocess.Popen([command, list(args)], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)      
      
            if wait:      
                out, err = sp.communicate()      
                if out:      
                    print(out.decode("utf-8"))      
                if err:      
                    print(err.decode("utf-8"))      
        except: pass      
      
      
      
    if __name__ == '__main__':      
        Launcher()      
```      
      
      
      
## Desktop Floating Widget - Timer      
      
This is a little widget you can leave running on your desktop.  Will hopefully see more of these for things like checking email, checking server pings, displaying system information, dashboards, etc      
.      
Much of the code is handling the button states in a fancy way.  It could be much simpler if you don't change the button text based on state.      
      
![timer](https://user-images.githubusercontent.com/13696193/45336349-26a31300-b551-11e8-8b06-d1232ff8ca10.jpg)      
      
```python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
import time

"""
 Timer Desktop Widget Creates a floating timer that is always on top of other windows You move it by grabbing anywhere on the window Good example of how to do a non-blocking, polling program using SimpleGUI Can be used to poll hardware when running on a Pi
 
 While the timer ticks are being generated by PySimpleGUI's "timeout" mechanism, the actual value
  of the timer that is displayed comes from the system timer, time.time().  This guarantees an
  accurate time value is displayed regardless of the accuracy of the PySimpleGUI timer tick. If
  this design were not used, then the time value displayed would slowly drift by the amount of time
  it takes to execute the PySimpleGUI read and update calls (not good!)     
 
 NOTE - you will get a warning message printed when you exit using exit button.
 It will look something like: invalid command name \"1616802625480StopMove\"
"""


# ----------------  Create Form  ----------------
sg.ChangeLookAndFeel('Black')
sg.SetOptions(element_padding=(0, 0))

layout = [[sg.Text('')],
         [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
         [sg.Button('Pause', key='button', button_color=('white', '#001480')),
          sg.Button('Reset', button_color=('white', '#007339'), key='Reset'),
          sg.Exit(button_color=('white', 'firebrick4'), key='Exit')]]

window = sg.Window('Running Timer', layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True, grab_anywhere=True)

# ----------------  main loop  ----------------
current_time = 0
paused = False
start_time = int(round(time.time() * 100))
while (True):
    # --------- Read and update window --------
    if not paused:
        event, values = window.read(timeout=10)
        current_time = int(round(time.time() * 100)) - start_time
    else:
        event, values = window.read()
    if event == 'button':
        event = window[event).GetText()
    # --------- Do Button Operations --------
    if event is None or event == 'Exit':        # ALWAYS give a way out of program
        break
    if event is 'Reset':
        start_time = int(round(time.time() * 100))
        current_time = 0
        paused_time = start_time
    elif event == 'Pause':
        paused = True
        paused_time = int(round(time.time() * 100))
        element = window['button')
        element.update(text='Run')
    elif event == 'Run':
        paused = False
        start_time = start_time + int(round(time.time() * 100)) - paused_time
        element = window['button')
        element.update(text='Pause')

    # --------- Display timer in window --------
    window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60,
                                                                  (current_time // 100) % 60,
                                                                  current_time % 100))
```

      
## Desktop Floating Widget - CPU Utilization      
      
Like the Timer widget above, this script can be kept running.  You will need the package psutil installed in order to run this Recipe.    
  
The spinner changes the number of seconds between reads.  Note that you will get an error message printed when exiting because the window does not have have a titlebar.  It's a known problem.      
      
      
![cpu widget 2](https://user-images.githubusercontent.com/13696193/45456096-77348080-b6b7-11e8-8906-6663c31ad0eb.jpg)      
      
      
      
```python
import PySimpleGUI as sg
import psutil

# ----------------  Create Window  ----------------
sg.ChangeLookAndFeel('Black')
layout = [[sg.Text('')],
          [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')],
          [sg.Exit(button_color=('white', 'firebrick4'), pad=((15, 0), 0)),
           sg.Spin([x + 1 for x in range(10)], 1, key='spin')]]

window = sg.Window('Running Timer', layout, no_titlebar=True, auto_size_buttons=False, keep_on_top=True,
                   grab_anywhere=True)

# ----------------  main loop  ----------------
while (True):
    # --------- Read and update window --------
    event, values = window.read(timeout=0)

    # --------- Do Button Operations --------
    if event is None or event == 'Exit':
        break
    try:
        interval = int(values['spin'])
    except:
        interval = 1

    cpu_percent = psutil.cpu_percent(interval=interval)

    # --------- Display timer in window --------

    window['text'].update(f'CPU {cpu_percent:02.0f}%')

# Broke out of main loop. Close the window.
window.close()
``` 
      
## Menus      
      
Menus are nothing more than buttons that live in a menu-bar.  When you click on a menu item, you get back a "button" with that menu item's text, just as you would had that text been on a button.      
      
Menu's are defined separately from the GUI window.  To add one to your window, simply insert sg.Menu(menu_layout).  The menu definition is a list of menu choices and submenus.  They are a list of lists.  Copy the Recipe and play with it.  You'll eventually get when you're looking for.    
      
If you double click the dashed line at the top of the list of choices, that menu will tear off and become a floating toolbar.  How cool!  To enable this feature, set the parameter `tearoff=True` in your call to `sg.Menu()`  
      
      
![tear off](https://user-images.githubusercontent.com/13696193/45307668-9aabcf80-b4ed-11e8-9b2b-8564d4bf82a8.jpg)      
      
      
```python      
    import PySimpleGUI as sg      
      
    sg.ChangeLookAndFeel('LightGreen')      
    sg.SetOptions(element_padding=(0, 0))      
      
    # ------ Menu Definition ------ #      
    menu_def = [['File', ['Open', 'Save', 'Exit'  ]],      
                ['Edit', ['Paste', ['Special', 'Normal', ], 'Undo'], ],      
                ['Help', 'About...'], ]      
      
    # ------ GUI Defintion ------ #      
    layout = [      
        [sg.Menu(menu_def, )],      
        [sg.Output(size=(60, 20))]      
             ]      
      
    window = sg.Window("Windows-like program", layout, default_element_size=(12, 1), auto_size_text=False, auto_size_buttons=False,      
                       default_button_element_size=(12, 1))      
      
    # ------ Loop & Process button menu choices ------ #      
    while True:      
        event, values = window.read()      
        if event == None or event == 'Exit':      
            break      
        print('Button = ', event)      
        # ------ Process menu choices ------ #      
        if event == 'About...':      
            sg.popup('About this program', 'Version 1.0', 'PySimpleGUI rocks...')      
        elif event == 'Open':      
            filename = sg.popup_get_file('file to open', no_window=True)      
            print(filename)      
```
      
## Graphing with Graph Element      
      
Use the Graph Element to draw points, lines, circles, rectangles using ***your***  coordinate systems rather than the underlying graphics coordinates.      
      
In this example we're defining our graph to be from -100, -100 to +100,+100.  That means that zero is in the middle of the drawing.  You define this graph description in your call to Graph.      
  
      
![graph markers](https://user-images.githubusercontent.com/13696193/46113087-01eaa480-c1bb-11e8-9784-0dbb4ce728b0.jpg)  
      
      
```python  
import math    
import PySimpleGUI as sg    
    
layout = [[sg.Graph(canvas_size=(400, 400), graph_bottom_left=(-105,-105), graph_top_right=(105,105), background_color='white', key='graph', tooltip='This is a cool graph!')],]    
    
window = sg.Window('Graph of Sine Function', layout, grab_anywhere=True).Finalize()    
graph = window['graph')    
    
# Draw axis    
graph.DrawLine((-100,0), (100,0))    
graph.DrawLine((0,-100), (0,100))    
    
for x in range(-100, 101, 20):    
    graph.DrawLine((x,-3), (x,3))    
    if x != 0:    
        graph.DrawText( x, (x,-10), color='green')    
    
for y in range(-100, 101, 20):    
    graph.DrawLine((-3,y), (3,y))    
    if y != 0:    
        graph.DrawText( y, (-10,y), color='blue')    
    
# Draw Graph    
for x in range(-100,100):    
    y = math.sin(x/20)*50    
    graph.DrawCircle((x,y), 1, line_color='red', fill_color='red')    
    
event, values = window.read()  
```
  
    
      
## Tabs      
  
Tabs bring not only an extra level of sophistication to your window layout, they give you extra room to add more elements.  Tabs are one of the 3 container Elements, Elements that hold or contain other Elements.  The other two are the Column and Frame Elements.  
  
  
![tabs](https://user-images.githubusercontent.com/13696193/46049479-97732f00-c0fc-11e8-8015-5bbed8bd88bb.jpg)  
  
  
  
```python
import PySimpleGUI as sg    
    
tab1_layout =  [[sg.T('This is inside tab 1')]]    
    
tab2_layout = [[sg.T('This is inside tab 2')],    
               [sg.In(key='in')]]    
    
layout = [[sg.TabGroup([[sg.Tab('Tab 1', tab1_layout, tooltip='tip'), sg.Tab('Tab 2', tab2_layout)]], tooltip='TIP2')],    
          [sg.Button('Read')]]    
    
window = sg.Window('My window with tabs', layout, default_element_size=(12,1))    
    
while True:    
    event, values = window.read()    
    print(event,values)    
    if event is None:           # always,  always give a way out!    
        break  
```
  
  
  
## Creating a Windows .EXE File      
      
It's possible to create a single .EXE file that can be distributed to Windows users.  There is no requirement to install the Python interpreter on the PC you wish to run it on.  Everything it needs is in the one EXE file, assuming you're running a somewhat up to date version of Windows.      
      
Installation of the packages, you'll need to install PySimpleGUI and PyInstaller (you need to install only once)      
      
    pip install PySimpleGUI      
    pip install PyInstaller      
      
To create your EXE file from your program that uses PySimpleGUI, `my_program.py`,  enter this command in your  Windows command prompt:      
      
    pyinstaller -wF my_program.py      
      
You will be left with a single file, `my_program.exe`, located in a folder named `dist` under the folder where you executed the `pyinstaller` command.      
      
That's all... Run your `my_program.exe` file on the Windows machine of your choosing.      
      
> "It's just that easy."      
>      
(famous last words that screw up just about anything being referenced)      
      
Your EXE file should run without creating a "shell window".  Only the GUI window should show up on your taskbar.
