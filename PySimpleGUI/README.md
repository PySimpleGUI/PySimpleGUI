<div align="center">

![PySimpleGUI Logo](https://pysimplegui.net/images/logos/Logo_Full_Transparent_Cropped.png)

</div>


# PySimpleGUI 6

6-Apr-2026

**Wait, what?**

<div>

![PySimpleGUI Logo](https://pysimplegui.net/images/emojis/question_56.png)  

</div>


As we've been winding down the commercialization effort, shutting down servers and archiving materials, I saw this week that the PySimpleGUI repositories are going to be of little use.  Everything was switched over to using PySimpleGUI 5. The documentation is PySimpleGUI5 specific as well.  So, I made a decision a couple of days ago to get the project into a state where it's at least usable and hopefully even useful.  

## Version 4 on PyPI 4.60.5.0

A first step was to put version 4.60.5 up on PyPI.  Version 4.60.5.0 was posted this week so that `pip install PySimpleGUI` will provide a version of PySimpleGUI that's solid.

## PySimpleGUI 6 - Back to LGPL3

There were several years of development that went into the PySimpleGUI 5 effort.  Rather than have those bug fixes and new features languish and be useless, I'm releasing them as Open Source.

Not all of the Version 5 code is in 6.  Things like the upgrade mechanism and of course the licensing has been removed.  As far as functionality, it matches the SDK posted in the [Docs.PySimpleGUI.com](https://Docs.PySimpleGUI.com) documentation.  

## What to expect ahead

### Applications, Demo Programs, etc

The applications `psgdemos`, `psgfiglet`, `psghotkey` have all been upgraded to 6 and posted on GitHub and PyPI.  The remaining applications are being updated as well. 

### Version 6 Uploaded to PyPI

On Tues 14-Apr-2026 PSG Version 6 was posted to PyPI.  There were a LOT of changes that have been made over the years since version 4 was released.  Hoping that it all goes well!   Feel free to open an issue if you run into trouble. 
<div>

![PySimpleGUI Logo](https://pysimplegui.net/images/emojis/fingers_crossed_56.png)

</div>


### Maintenance & Support

I don't have a firm grasp of the future beyond a few weeks at this point.  If the past 8 years is any indication, I'm not very good at making predictions.

## Installing

You can install the latest released version from PyPI with a simple:

## PyPI

`python -m pip install PySimpleGUI`  

## Github

You can install the latest version straight from the PySimpleGUI GitHub repo without downloading the repo by running:

`python -m pip install --upgrade https://github.com/PySimpleGUI/PySimpleGUI/zipball/master`  

If you want to download the repo then download/close and run in the downloaded folder:

`python -m pip install .`

## More updates coming...

Changes are rolling out onto GitHub and PyPI every few days.  They'll continue until everything gets switched over to Version 6.
