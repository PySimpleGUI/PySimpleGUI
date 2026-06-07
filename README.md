
<p align="center">
    <img height="250" src="https://pysimplegui.net/images/logos/Logo_Full_Transparent_Cropped.png">
  
</p>


# FREE Udemy Course

The Udemy course makes $10's a month, usually less. I've decided to give away the course for a while.  This coupon is good for the next 30 days.

https://www.udemy.com/course/pysimplegui/?couponCode=033334A16163C571B739

Or use code:    033334A16163C571B739


# Open Source Once Again...

Hey, it's Mike....![](https://PySimpleGUI.net/images/emojis/wave_56.png?raw=true&v=1) 


We gave commercialization a try. It was an incredible experience, but it didn’t generate the resources needed to sustain PySimpleGUI at the level we had hoped. In February 2025, we announced that PySimpleSoft would be shutting down, with support continuing through the end of 2025.

That process is now complete. The next question was what to do with the code, documentation, and repositories. I always planned to keep the repos available for reference—so the decision came down to the software itself.

See the **History** section below for a summary of the PySimpleGUI history.


# PySimpleGUI 6

<div>
<img src="https://pysimplegui.net/images/logos/psg6_logo_plain.png" height="80" alt="Alt text">
</div>


I’ve released the PySimpleGUI 5 code as open source. After removing licensing and security components, it’s now available under the LGPL3 license on GitHub and PyPI.

## Installing from PyPI

To install the latest version (v6):

```bash
python -m pip install PySimpleGUI
```


If you need the older version (4.60.5.1):


```bash
python -m pip install PySimpleGUI==4.60.5.1
```

## Installing from Github

The GitHub repo has the most up-to-date code. You can install directly without cloning:


```bash
python -m pip install --upgrade https://github.com/PySimpleGUI/PySimpleGUI/zipball/master
```

To install a specific release that's here on GitHub, change `master` to the release number.  To install version 6.1:

```bash
python -m pip install --upgrade https://github.com/PySimpleGUI/PySimpleGUI/zipball/6.1
```


Or clone/download the repo and install locally:

```bash
python -m pip install .
```

 
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


## Drag and Drop!

> [!NOTE]
> Drag and Drop support on PySimpleGUI may soon be here
> New experimental Demo Program - [Demo_Drag_and_Drop.py](https://github.com/PySimpleGUI/PySimpleGUI/blob/master/DemoPrograms/Demo_Drag_and_Drop.py)
> Femo program is in the PySimpleGUI repo as well as the psgdemos repo


To pip install psgdemos with the new demo program:

```bash
python -m pip install --upgrade https://github.com/PySimpleGUI/psgdemos/zipball/main
```
 
Drag and Drop support has been a wish for many years.  Finally may have found a way to do it such that the PySimpleGUI code is not changed.  All code is in the user code-space.


![DragDrop](https://raw.githubusercontent.com/PySimpleGUI/PySimpleGUI/refs/heads/master/images/for_readme/DragDrop2.gif)



## Documentation

* The move of the documentation from ReadTheDocs to GitHub pages is complete.  Users should notice no difference.
* Removal of Version 5 specifics is done for the mostpart.  There may be a few spots that need cleanup
* Work has started to include PSG 6 details.  The SDK Call Reference needs upating before the next PyPO release, preferably sooner so that the code on GitHub is in there prior to PyPO release.


## New repo - PSGMicroPython

Created a new repo and added code for interfacing to a MicroPython-based microcontroller.  It works with Raspberry Pi Pico and ESP32.  It may work with other boards too.  Not meant to be robust or significant.  It's just some code I threw together that could maybe be useful to someone else... or not... 
![](https://PySimpleGUI.net/images/emojis/guess_28.png?raw=true&v=1) 



## Features & Fixes

* 6.0.2 - Fixed bug in Window.settings_save
* 6.0.3 - Added ability to "print" an image inline in a Multiline element

<img width="1081" height="538" alt="Image" src="https://github.com/user-attachments/assets/e914e1dd-e363-4124-9cc9-a065abf8e6c1" />

* 6.0.5 - The ability to upgrade to the latest Maint Release is once again built into PSG.  You can use the Home Window or the command line command`psgupgrade`.  You can see the release notes and install a new version.


<img width="499" height="256" alt="Image" src="https://github.com/user-attachments/assets/b6c4b736-0f3b-4001-88bc-040ae62208ca" />


<img width="771" height="356" alt="Image" src="https://github.com/user-attachments/assets/9b8aa416-eef4-48c8-aca6-df62673be6c0" />



* 6.0.6 - Fix for bug  #5750.  Graph events was going into an infinite loop when write_event_value events
                        were received. Fix was to clear the realtime button flag. Potential for regression problems
                        should be minimal since only the Graph element conditional was changed.                                           
* 6.0.7 - Added Enhancement #6671.  Added parameter select select_node_keys to Tree.update. Enables nodes
                        in the tree to be programmatically selected as if the user selected them.
* 6.0.7 - Fixed Multiline echo_stdout_stderr feature/parameter.  Was not correctly echoing out to sys.stdout, stderr.
                        Edited docstring to document the correct behavior. It will only echo if you've rerouted stdout or stderr to the element.
                        It will not do the reroute for you.                                          
* 6.1.2 - Fix for Issue #6686 - Calendar chooser button clearing fields that should only be cleared when window.read returns.
                        Used the newly added element_that_generated_event variable from the Graph element fix above (already came in handy).
* 6.1.4 - Display the Maint Release version number in the Home Window. Moved the install button
* 6.1.5 - Added ability to specify timers using string "H:M:S" when calling Window.start_timer.
* 6.1.6 - Enhancement - support for horizontal scroll only for scrollable column element

------

## PSGWeb

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

I fell in love with programming 50 years ago.  Writing software is my happy place.  It's an "I **get to** write software" thing.
AI can generate lots of things.  The feeling I get writing software is not one of the things AI can generate.

I'm not in a hurry.  If I wanted code written for me, I would have opened the project up to pull requests years ago, but I didn't because I wanted to write the code.  It's fun!

### PySimpleGUI in the AI era

A common question in software today is whether a library is still relevant. I think for PySimpleGUI the answer is yes.  People discover and install PySimpleGUI every day. Doesn't matter **how many** people use it.  More than one is good enough.  It's a thrill that other programmers want to use what I create.  

I use PySimpleGUI regularly.  I can’t imagine building a Windows app without it.  I’ve recently been working on a 6502 breadboard computer. I built a bus analyzer using a couple of Raspberry Pi Picos and a PySimpleGUI app to control everything from Windows.  Coding up a windows application to be the front-end to my tools is very easy for me to do using PySimpleGUI.

That’s reason enough for me to keep working to clean up the ecosystem and keep it running.

---------------------------

# History

## Open Source v4 → Commercial v5 → Open Source v6

PySimpleGUI’s journey has included plenty of ups and downs, good decisions and bad ones, a few surprises, and a lot of fun along the way.

Hi, it’s Mike. I thought it might be useful to share the story from my perspective.

PySimpleGUI began in 2018 as throwaway code. I needed a GUI for a media player prototype and had no experience building GUIs or working with object-oriented GUI frameworks. My goal was simple: wrap Tkinter in a way that felt more linear and straightforward so I could get something working quickly.

There was no bigger plan. But as I used it, it started to feel genuinely useful, so I shared it.

My background is in Silicon Valley startups—building products, shipping software, and later managing teams. I had no experience with Python or open source at the time. So when I put PySimpleGUI on GitHub, I approached it the way I knew how: like a startup. It became a full-time, self-funded effort rather than a traditional open source project.

## Timeline

- July 2018 – Version 1
- June 2019 – Version 4
- January 2020 – Funding becomes a major concern; commercialization mentioned
- November 2020 – Udemy course announced; a public plea for help added
- December 2021 – Course released
- February 2024 – Version 5 (commercial launch)
- April 2026 – Version 6

There’s an [Announcements Issue](https://github.com/PySimpleGUI/PySimpleGUI/issues/142) on GitHub that I’ve used like a running blog. It has grown to over 1,700 entries documenting the project in detail. To make reading it easier, a snapshot is posted in the documnation under the tab [Announcements 2018-2024](https://docs.pysimplegui.com/githubannouncements/).  

## Funding Reality

Working full-time on an open source project creates immediate and ongoing financial pressure.

I explored the common options:

- Sponsorships and donations (GitHub Sponsors, Buy Me a Coffee). At peak, this brought in about \$150 per month.
- Education. We built an 11.5-hour Udemy course with 61 lessons. It performed well initially, reaching around \$2,000 per month for a short time, but eventually dropped below \$100.

Neither path was enough to sustain the project long term.

## Commercialization

Moving to a commercial model wasn’t a sudden decision. It had been discussed openly for years in the README and announcements.

By early 2024, after exhausting other options, Version 5 launched as a paid product. Even then, the goal was to keep things accessible, not to put up barriers.

## How Did It Go?

If the metric is financial sustainability, it didn’t go well.

If the metric is experience, learning, and relationships, it was absolutely worth it.

We didn’t lose most users after commercialization. Many companies continued using PySimpleGUI. The challenge was getting them to purchase licenses.

## The Hobbyist License

We made a deliberate choice: hobbyists and students could use PySimpleGUI for free, while companies were expected to pay.

It felt like the right balance.

In practice, the vast majority of users identified as hobbyists. Tens of thousands of corporate users registered under the free tier. It wasn’t unusual to see large companies with hundreds of users and only a handful of paid licenses.

I don’t regret the decision to offer a free option.

## A Culture of Free

My personal takeaway is that there’s a strong cultural expectation that Python tools & libraries should be free.

The issue didn’t seem to be price or dissatisfaction. People kept using PySimpleGUI—they just didn’t feel obligated to pay for it. Even clear licensing terms didn’t consistently change that behavior.

That’s my interpretation, based on what I saw. Others may see it differently.

## Having Fun

Startups fail more often than they succeed. This one didn’t achieve financial sustainability, and that’s part of the process.

From the beginning, one of the stated goals of PySimpleGUI was: have fun.

That part has held true. Writing code, building things, seeing what others create, and working with people along the way—that’s the part I’ve enjoyed the most.

Business, on the other hand, has never been the fun part for me.

## Thank You

Thank you to everyone who has supported the project over the years.

I don’t know exactly what comes next, but I’ve enjoyed the journey and I'm looking forward to whatever is ahead.

-------

## License & Copyright

Copyright 2018-2026 PySimpleGUI.  All rights reserved.

Licensed under LGPL3.
