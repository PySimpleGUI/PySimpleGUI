<div align="center">

![PySimpleGUI Logo](https://pysimplegui.net/images/logos/Logo_Full_Transparent_Cropped.png)

</div>


# PySimpleGUI 6

6-Apr-2026

Wait, what?

As we've been winding down the commercialization effort, shutting down servers and archiving materials, I saw this week that the PySimpleGUI repositories are going to be of little use.  Everything was switched over to using PySimpleGUI 5. The documentation is PySimpleGUI5 specific as well.  So, I made a decision a couple of days ago to get the project into a state where it's at least usable and hopefully even useful.  

## Version 4 on PyPI

A first step was to put version 4.60.5 up on PyPI.  Version 4.60.5.0 was posted this week so that `pip install PySimpleGUI` will provide a version of PySimpleGUI that's solid.

## PySimpleGUI 6 - Back to LGPL3

There were several years of development that went into the PySimpleGUI 5 effort.  Rather than have those bug fixes and new features languish and be useless, I'm releasing them as Open Source.

Not all of the Version 5 code is in 6.  Things like the upgrade mechanism and of course the licensing has been removed.  As far as functionality, it matches the SDK posted in the [Docs.PySimpleGUI.com](https://Docs.PySimpleGUI.com) documentation.  

## What to expect ahead

### Applications, Demo Programs, etc

These all need to be modified to remove the commercial license and checks for version 5.  It shouldn't take too long to get them all changed.  In the meantime, everything is usable with minor edits.

### Upload to PyPI

I'm hoping to get PSG6 up to PyPI in the next week. I first would like to get some runtime on it with installs happening from GitHub.  When it is uploaded, because it's version 6, anyone pip installing will get it by default, so that quality needs to be checked first.


### Maintenance & Support

I don't have a firm grasp of the future beyond a few weeks at this point.  If the past 8 years is any indication, I'm not very good at making predictions.


## Installing

You can pip install straight from this Repo using the command:  
`python -m pip install git+https://github.com/PySimpleGUI/PySimpleGUI`

or if you invoke Python using `python3`:  
`python3 -m pip install git+https://github.com/PySimpleGUI/PySimpleGUI`

You can also download/clone the repo and run  
`python -m pip install .`

## More updates coming...

I'll post regular updates as progress is made.  It should progress pretty quickly.

