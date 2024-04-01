<p align="center">
    <img src="https://pysimplegui.net/images/big_news_emoji.png">
    <br>
    For more information visit <a href="https://home.PySimpleGUI.com">PySimpleGUI.com</a>
</p>



##

<p align="center">
    <img height="250" src="https://pysimplegui.net/images/logos/Logo_Full_Transparent_Cropped.png">
    <h2 align="center">User Interfaces for Humans<sup>TM</sup></h2>
</p>

# Welcome to PySimpleGUI 5 !!

Do you use PySimpleGUI 4? [Here is what you need to know.](https://docs.pysimplegui.com/en/latest/readme/sunset/)

**PySimpleGUI creates desktop applications easily**, enhancing the tkinter, Qt, WxPython, and Remi frameworks with a much simpler programming interface:

1. PySimpleGUI user interfaces are defined using core Python data types (lists and dictionaries) that are easily understood by beginners.
2. PySimpleGUI event handling changes from a complex callback-based model to a simple message passing one.
3. PySimpleGUI uses simple Python code and has no requirement for object oriented architecture.

PySimpleGUI is more than a GUI library: PySimpleGUI simplifies much of your Python development process. Sure, it makes developing user interfaces much easier, but PySimpleGUI also tames advanced Python functionality (such as threading) and makes it easy for all users to take their Python applications to the next level. PySimpleGUI is a robust toolkit.

## Introducing PySimpleGUI 5

For the last 5 years, PySimpleGUI offered free software with the hope of sustaining the
company by donations. We appreciate the support we received, but the amount has been too
small to support the PySimpleGUI project. For this reason, PySimpleGUI is switching to a
commercial model, where commercial users are expected to pay a nominal license fee.


PySimpleGUI is now part of PySimpleSoft, Inc., whose mission is to make the best Python
application development environment much, much better. Since launching in 2018, PySimpleGUI
has helped hobbyists and professionals alike create Python GUIs in a fraction of the time.
PySimpleGUI 5 takes PySimpleGUI to the next level, providing hundreds of improvements,
including new features, enhanced security, and priority support.


PySimpleGUI 5 is licensed software. As the [License Agreement](LICENSE.txt) explains, after a trial
period, all PySimpleGUI 5 users must register at PySimpleGUI.com to obtain a Developer Key.
For most users (Hobbyist Users), the license is at NO COST. If you are a Commercial User, you must buy a license.

<p align="center">
    <img src="https://pysimplegui.net/images/pricing_summary.png">
</p>

[Register Now](https://pricing.PySimpleGUI.com) and help support the PySimpleGUI community.

## Examples

PySimpleGUI users have created thousands of amazing desktop applications. Here are a few screen shots. For more examples, see the [PySimpleGUI gallery](https://gallery.PySimpleGUI.com/).

<p align="center">
    <img height="150" src="https://pysimplegui.net/images/for_readme/gallery1.jpg" />
    <img height="150" src="https://pysimplegui.net/images/for_readme/gallery2.jpg" />
    <img height="150" src="https://pysimplegui.net/images/for_readme/gallery3.jpg" />
</p>

## Get Started at No Cost

Whether you are a Hobbyist User or Commercial User, you can start using PySimpleGUI at no cost.
To get started with a 30-day trial period, first install Python and then

    python -m pip install pysimplegui

and run some code, like

    import PySimpleGUI as sg
    layout = [ [sg.Text('Hello, world!')] ]
    window = sg.Window('Hello Example', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
    window.close()

(You might need to use `python3` instead of `python`.)

You can try PySimpleGUI for 30 days, after which you will need to register. Hobbyist users register at no cost, and Commercial Users must buy a license. For more details, see [PySimpleGUI.com/pricing](https://pricing.PySimpleGUI.com).

## Documentation

PySimpleGUI provides extensive documentation. Here are some starting points, depending on your needs and expertise:


* [FAQ](https://faq.pysimplegui.com/) - Frequently Asked Questions
* [Documentation](https://docs.pysimplegui.com/) - Extensive PySimpleGUI documentation*
* [Examples](https://examples.pysimplegui.com/) - Hundreds of sample PySimpleGUI applications.
* [SDK Reference](https://sdk.pysimplegui.com/) - details for each PySimpleGUI element
* [Home Website](https://PySimpleGUI.com) - New PySimpleGUI home page
* [GitHub Repo](https://github.PySimpleGUI.com) - Informational only. Download from PyPi with pip.
* [Updated Documentation](https://docs.PySimpleGUI.com) - Everything you need to know about the latest and best PySimpleGUI
	* [Cookbook](https://cookbook.PySimpleGUI.com) - Hundreds of basic PySimpleGUI examples. Find a starting point that is close to what you need.
	* [Call Reference](https://cookbook.PySimpleGUI.com) - Just the facts, Ma'am
* [Udemy Course](https://udemy.PySimpleGUI.com) - Become a PySimpleGUI expert in no time. Bundled with Commercial Developer License.
