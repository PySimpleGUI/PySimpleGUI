# Theme Maker

## A Tool To Make PySimpleGUI "Look and Feel" Entries  

The Look and Feel themes are defined using a dictionary.  Each theme has a dictionary of colors and other settings such as the color for the text, background, input fields, buttons, etc.  Generating these themes has been a tedious and long process in the past.  This tool was created to make that process easier, more enjoyable, and perhaps something users could participate in.

This program uses over 1,700 color palettes that were downloaded from https://colorhunt.co/palettes and put into a python file as a dictionary.  You'll find the dictionary in `color_themes.py`.  

Here is how the dictionary looks when shortened to 3 entires:

```python
themes = {
	'163372': ('#f4efd3', '#cccccc', '#c2b0c9', '#9656a1', ['Yellow', 'Grey', 'Purple', 'Pastel']),
	'163318': ('#594a4e', '#e78fb3', '#ffc0ad', '#6fc1a5', ['Brown', 'Pink', 'Green', 'Vintage']),
	'163537': ('#ff8ba7', '#ffc6c7', '#faeee7', '#c3f0ca', ['Pink', 'Green', 'Bright', 'Summer']) }
```

## What It Does

Each palette, a group of 4 colors, is used to present a small "candidate theme layout".  A single "candidate" looks like this:

![SNAG-0587](https://user-images.githubusercontent.com/46163555/69909821-c820b980-13ce-11ea-95fb-03460e7d3873.jpg)

For each palette you will be presented with 4 of those layouts.  Two are "Dark" and two are "Light".  You can choose options in each of these layouts and choose to save it.

The program generates text in a debug window and also appends the text to an output file.  This text can be used directly in a look and feel table.


## Installing

There is no installation if you already have PySimpleGUI installed.  Simply download the 2 .py files in this folder and run the one named Theme_Maker.py

## Running - Initial Window

The first window you're presented with collects information from you regarding how you would like the theme generation window to be laid out and where to start in the palette dictionary.

![SNAG-0584](https://user-images.githubusercontent.com/46163555/69909830-0322ed00-13cf-11ea-88da-999d6e901002.jpg)




![SNAG-0586](https://user-images.githubusercontent.com/46163555/69909820-c820b980-13ce-11ea-94db-0e36af813e25.jpg)




Program that is used to create new themes for use with PySimpleGUI's "Look and Feel" settings.
You are presented with a grid of mini-windows that is created for color palettes downloaded from https://colorhunt.co/palettes
The file color_themes.py contains a large dictionary of approx 1780 palettes.

For each palette you are shown 4 candidate themes, 2 "light" and 2 "dark".  The window shows 5 palettes so you'll have a
total of 20 candidate themes displayed in total. 
Each candidate theme has a 3 options - The button color (text and background), the text color for Input/Multiline elements,
and the name of the theme when you save it.  These you choose using the radio buttons and one input field.
To "save" one of these candidate themes, check the checkbox to the left of the layout, choose the radio buttons for button
& text settings and optionally change the theme name that is shown above the grid of OK buttons.  By default the name starts
with either "Dark" or "Light" and is followed by the first 2 "tags" that were posted with the palette on the colorhunt site.     

After you've selected the themes you want to save from the window of 20 click any "OK" button in the window or close the 
window with the "X".  You will see the dictionary text in the Debug Window and the values will also be written to a file.
You'll then be shown the next group of 20 candidate themes.

If you want to exit the program entirely, click any "Cancel" button the page.  Note - cliicking "Cancel" will not save any
theme you have checked with the checkbox.  You should only exit from a window you have not selected any themes for saving    
    
If a Theme is selected for saving, then the values for the LOOK_AND_FEEL dictionary are displayed in a debug window and are 
also appended to the file new_theme_dict.py.  You will need to edit the new_theme_dict.py file to get the syntax correct.
A "," or "}" may need to be added in order to make the table be correct.

If you're using this program it's assumed you know what you're doing and understand the LOOK_AND_FEEL dictionary and can 
figure out how to get the syntax correct for adding it to the main dictionary of themes.

## Choosing and Saving New Themes

Let's say you were working with these candidate themes:

![SNAG-0556](https://user-images.githubusercontent.com/46163555/70284016-94f47680-1790-11ea-9e08-1fe7804eaf1a.jpg)


You like the first 2 themes on the second row, so you

* Mark the checkbox next to each of those 2 themes
* Click the 2 radio buttons indicating choice for input text choice and button color
* Enter a name to be used for the theme
* Click OK anywhere on the screen

Here is how my choices appear for those 2 entries:

![SNAG-0577](https://user-images.githubusercontent.com/46163555/70284014-94f47680-1790-11ea-9373-28f80c8a4d31.jpg)

The result will be that a debug window will open and display the text for the 2 new theme entries for the look and feel theme dictionary.

![SNAG-0578](https://user-images.githubusercontent.com/46163555/70284013-94f47680-1790-11ea-8be8-507ed929c867.jpg)

Similar text will be appended to the end of the file "new_theme_dict.py".


## Integrating the New Themes

Now that you've got the text for the themes it's time to integrate it into your PySimpleGUI environment.  The way you do this is that you add your themes direcvtly to the look and feel dictionary.

Begin by copying the text from either the .py file or the debug window:

```python
'DarkGreenArmy' : {'BACKGROUND': '#3b503d', 'TEXT': '#f1edb3', 'INPUT': '#c8cf94', 'TEXT_INPUT': '#000000', 'SCROLL': '#c8cf94', 'BUTTON': ('#f1edb3', '#3b503d'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#3b503d', '#4a746e', '#c8cf94', '#f1edb3'], 'DESCRIPTION': ['Green', 'Turquoise', 'Yellow']}
 
'LightGreenArmy' : {'BACKGROUND': '#f1edb3', 'TEXT': '#3b503d', 'INPUT': '#4a746e', 'TEXT_INPUT': '#f1edb3', 'SCROLL': '#3b503d', 'BUTTON': ('#f1edb3', '#3b503d'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#3b503d', '#4a746e', '#c8cf94', '#f1edb3'], 'DESCRIPTION': ['Green', 'Turquoise', 'Yellow']}
```

This code is written as if you were going to directly add the code inside the PySimpleGUI.py file itself.  Instead you'll be adding them directly from your user code rather than modifying the PySimpleGUI.py file.

Adding the entries to the table can be accomplished using simple assignment to a new dictionary entry.  The look and feel dictionary in PySimpleGUI is named `sg.LOOK_AND_FEEL_TABLE`.  Here is a sample user program that adds these 2 new themes to the table and then uses one of them to display a window and another to display a popup.


```python
import PySimpleGUI as sg

sg.LOOK_AND_FEEL_TABLE['DarkGreenArmy'] = {'BACKGROUND': '#3b503d', 'TEXT': '#f1edb3', 'INPUT': '#c8cf94', 'TEXT_INPUT': '#000000', 'SCROLL': '#c8cf94',
                  'BUTTON': ('#f1edb3', '#3b503d'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                  'COLOR_LIST': ['#3b503d', '#4a746e', '#c8cf94', '#f1edb3'], 'DESCRIPTION': ['Green', 'Turquoise', 'Yellow']}

sg.LOOK_AND_FEEL_TABLE['LightGreenArmy'] = {'BACKGROUND': '#f1edb3', 'TEXT': '#3b503d', 'INPUT': '#4a746e', 'TEXT_INPUT': '#f1edb3', 'SCROLL': '#3b503d',
                   'BUTTON': ('#f1edb3', '#3b503d'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                   'COLOR_LIST': ['#3b503d', '#4a746e', '#c8cf94', '#f1edb3'], 'DESCRIPTION': ['Green', 'Turquoise', 'Yellow']}

sg.change_look_and_feel('Dark Green Army')


layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN-')],
            [sg.Button('Popup'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Popup':
        sg.ChangeLookAndFeel('Light Green Army')
        sg.popup('This popup is using a new "Light Green Army" look and feel theme')
window.close()
```

## Displaying the New Themes

When the above program is executed, you are first prsented with a window that's created using the new "DarkGreenArmy" theme.  Notice that you can use the "fuzzy theme matching" to make your code more readable by referencing to the theme as "Dark Green Army" when calling `change_look_and_feel`

![image](https://user-images.githubusercontent.com/46163555/70284546-59f34280-1792-11ea-9a4a-d3aeeb121381.png)

Clicking the popup causes the light look and feel theme to be loaded prior to calling `popup` to display a window.  This will cause the popup to use the light theme and creates this window:

![image](https://user-images.githubusercontent.com/46163555/70284679-da19a800-1792-11ea-9701-88989cc93ae2.png)

## Go Make The World More Colorful!!

Now that you've created some of your very own Look and Feel themes, go use them to create some nice looking windows!  **Anything** is better than a default gray window.    



# Author 

The PySimpleGUI Organization


   
# License        

Copyright 2019 PySimpleGUI.org

 GNU Lesser General Public License (LGPL 3) +        
