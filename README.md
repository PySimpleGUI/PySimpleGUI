
<p align="center">
    <img height="250" src="https://pysimplegui.net/images/logos/Logo_Full_Transparent_Cropped.png">
  
</p>


 
# Open Source Once Again...

Hey, it's Mike....![](https://PySimpleGUI.net/images/emojis/wave_56.png?raw=true&v=1) 


We gave commercialization a try. It was an incredible experience, but it didn’t generate the resources needed to sustain PySimpleGUI at the level we had hoped. In February 2025, we announced that PySimpleSoft would be shutting down, with support continuing through the end of 2025.

That process is now complete. The next question was what to do with the code, documentation, and repositories. I always planned to keep the repos available for reference—so the decision came down to the software itself.



# PySimpleGUI 6

<div>
<img src="https://pysimplegui.net/images/logos/psg6_logo_plain.png" height="80" alt="Alt text">
</div>


I’ve released the PySimpleGUI 5 code as open source. After removing licensing and security components, it’s now available under the LGPL3 license on GitHub and PyPI.

## Installing from PyPI

To install the latest version (v6):

`python -m pip install PySimpleGUI`

If you need the older version (4.60.5.1):


`python -m pip install PySimpleGUI==4.60.5.1`

## Installing from Github

The GitHub repo has the most up-to-date code. You can install directly without cloning:


`python -m pip install --upgrade https://github.com/PySimpleGUI/PySimpleGUI/zipball/master`

Or clone/download the repo and install locally:

`python -m pip install .`
 
## Longer Term Outlook

I’m still wrapping up the transition from version 5 to 6, including the docs. After that, I’m honestly not sure what the long-term future looks like—but if the past 8 years are any indication, I’m not great at predicting it.  


For now, I’m here and happy to help.

## Thank you

PySimpleGUI has been a once-in-a-lifetime experience. It’s been amazing to see what people have built and to be a small part of it. Thanks to everyone who supported the project over the years.

---------------------------------


# What is PySimpleGUI?

PySimpleGUI is a wrapper for tkinter (and other GUI libraries) that transforms the GUI SDK into a simpler, more compact architecture while still providing detailed customization.  No prior GUI programming experience needed.

This is an entire interactive application.

```python
import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    # Output a message to the window
    window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()
```

This is the window that's created.

![win1](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Example2-1.jpg)

Here's the same window after some user interaction.

![win2](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/master/images/for_readme/Example2-2.jpg)

##  Documentation - want to learn more? 


You'll find **extensive** documentation at:

https://Docs.PySimpleGUI.com

## Contributing

PySimpleGUI has always been developed more like a proprietary product than an open source project.  Pull requests aren't accepted.


---

# What's new...

## Recently added features and activities

## Documentation

* The move of the documentation from ReadTheDocs to GitHub pages is complete.  Users should notice no difference.
* Removal of Version 5 specifics is done for the mostpart.  There may be a few spots that need cleanup
* Work has started to include PSG 6 details.  The SDK Call Reference needs upating before the next PyPO release, preferably sooner so that the code on GitHub is in there prior to PyPO release.


## New rep - PSGMicroPython

Created a new repo and added code for interfacing to a MicroPython-based microcontroller.  It works with Raspberry Pi Pico and ESP32.  It may work with other boards too.  Not meant to be robust or significant.  It's just some code I threw together that could maybe be useful to someone else... or not... 
![](https://PySimpleGUI.net/images/emojis/guess_28.png?raw=true&v=1) 



## Features & Fixes

* 6.0.2 - Fixed bug in Window.settings_save
* 6.0.3 - Added ability to "print" an image inline in a Multiline element

<img width="1081" height="538" alt="Image" src="https://github.com/user-attachments/assets/e914e1dd-e363-4124-9cc9-a065abf8e6c1" />

* 6.0.5 - The ability to upgrade to the latest Maint Release is once again built into PSG.  You can use the Home Window or the command line command`psgupgrade`.  You can see the release notes and install a new version.


<img width="499" height="256" alt="Image" src="https://github.com/user-attachments/assets/b6c4b736-0f3b-4001-88bc-040ae62208ca" />


<img width="771" height="356" alt="Image" src="https://github.com/user-attachments/assets/9b8aa416-eef4-48c8-aca6-df62673be6c0" />



* PSGWeb - PySimpleGUI running in a browser window
  * Works with most demo programs
  * To try it, go to any PySimpleGUI application on GitHub, add `psgweb.us` onto the front of the url, press enter
  * https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_All_Elements.py becomes https://psgweb.us/github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_All_Elements.py
  * There are no plans to release or expand this prototype.  It was created as part of the larger PSG 5 effort, but not released.

Here's that Demo Program running in browser:

<img width="1087" height="1184" alt="Image" src="https://github.com/user-attachments/assets/63b68e32-4a9d-4399-b8a4-00503dbcc111" />



----



## AI....

![](https://PySimpleGUI.net/images/emojis/weary_56.png?raw=true&v=1) 

Seems most projects have something to say about AI usage now.  This is my **opinion** and how I've decided to use AI.  It's what's right for me.  It might not be right for you or anyone else.

I use LLMs to search and summarize documentation, lookup errors, do research, get knowledge.  I don't use LLMs to write code.  My reason is very simple.  

### **I like to write code.**  

I fell in love with programming 50 years ago.  Writing software is my happy place.  Why would I give that to a computer to do instead of getting the enjoyment I get from doing it?  AI can generate lots of things.  The feeling I get writing software is not one of the things AI can generate.

I'm not in a hurry.  If I wanted code written for me, I would have opened the project up to pull requests years ago, but I didn't because I wanted to write the code.  It's fun!

### PySimpleGUI in the AI era

A common question in software today is whether a library is still relevant. I think for PySimpleGUI the answer is yes.  People discover and install PySimpleGUI every day.  GUI applications are often built incrementally. As features are added, layouts change, buttons move, and the code needs to evolve. That’s much easier when the code is understandable, whether it was written by a person or an AI.

I use PySimpleGUI regularly, and I can’t imagine building a Windows app without it.  I’ve recently been working on a 6502 breadboard computer. I built a bus analyzer using a couple of Raspberry Pi Picos and a PySimpleGUI app to control everything from Windows.  Coding up a windows application to be the front-end to my tools is very easy for me to do using PySimpleGUI.

That’s reason enough for me to keep working to clean up the ecosystem and keep it running well.

## License & Copyright

Copyright 2018-2026 PySimpleGUI.  All rights reserved.

Licensed under LGPL3.
