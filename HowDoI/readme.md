# PySimpleGUI-HowDoI

## Introduction
This package contains a GUI front-end to the AMAZING tool, HowDoI.  You can ask this tool any programming question and it will tap into the enormous database of programming questions and answers, StackOverflow.

This program takes you question and returns CODE as a response.

The way it works is that it searches StackOverflow, gets the results and then finds the highest voted answer.  From that answer it takes the code it finds and that is what is returned to you.  It works shockingly well.

To learn more about HowDoI, visit their GitHub site:
https://github.com/gleitz/howdoi



![snag-0081](https://user-images.githubusercontent.com/13696193/46911287-3a151580-cf25-11e8-8328-f36fda446c4b.jpg)


Check out this example.  This was not rehearsed.  While typing this readme, an example was needed and a random question, that I've never asked before, was posed. Once again this program delivered a great answer.

You can copy and paste the solution right into your code if you wish.

## Installing

When you install PySimpleGUI-HowDoI, it will install the other components that it requires. To install, on windows, type this into a command prompt:

    pip install pysimplegui-howdoi


## Running the GUI Program

Afer your Pip install completes you can run the program.  Do run it, type this into your command prompt:

    python -m pysimplegui-howdoi.pysimplegui-howdoi

Once running you simply type in your question and press enter or click the "SEND" button.  If you want to ask a question again, you can use the arrow keys or your mouse wheel to access the history of questions you've previously asked.

Ask ANY question you want for ANY programming language.  I recommend starting the question with the programming language.


## PySimpleGUI Project

This program was built as a sample application of the PySimpleGUI GUI Framework.  It quickly became a tool I was unable to live without.  I've been trying for some time to bring it to life for others to try.

## Windows Only?

This has only been tested using Windows.  I have not gotten it to work under Linux.  The linkage between the program and the howdoI package was messed up on Linux.  If you're able to get a Linux version running, please let me know at info@PySimpleGUI.org
