## Custom Titlebars &  Custom Menubars - Bringing Some Style to Windows

One problem with running on Trinket is the lack of titlebars. Titlebars and Menubars are provided by the OS.  Like all things software, it's a wonferfully terrible thing.

Wonderful that they just work.  Terrible that the colors are not changable.

As Trinket has become a more and more important tool in the edcuation of PySimpleGUI programmers, the lack of a Titlebar wsa becoming a serious problem.  Additionally, that aforementioned lack of color and other controls means your wonderful dark themed PySimpleGUI window is likely to have an entirely non-matching titlebar.

Let's look at both the default PySimpleGUI theme and a "Dark Red" theme.  

```python
import PySimpleGUI as sg

sg.theme('dark red')

layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN-')],
            [sg.Button('Go'), sg.Button('Exit')]  ]

sg.Window('Window Title', layout).read(close=True)

```

If no theme is set for the window, we get this lovely window

![SNAG-1072.jpg](/api/files/608d3ed645fe6aba0d762647/snag-1072.jpeg)

Setting "Dark Red" produces this one

![SNAG-1075.jpg](/api/files/608d3ed645fe6aba0d762645/snag-1075.jpeg)


They're not terrible by ANY stretch, espcecially given they're all of 4 lines long.  But, they can certainly be made a bit more attractive and this is where the custom titlebar comes in.  Not only does it solve a problem of a missting titlebar entirely on Trinket, but it also gives us very attractive windows on all platforms

By adding the parameter `use_custom_titlebar=True`....

```python
sg.Window('Window Title', layout, use_custom_titlebar=True).read(close=True)

```

Our windows become these on Windows

![SNAG-1073.jpg](/api/files/608d3ed645fe6aba0d762648/snag-1073.jpeg)

![SNAG-1074.jpg](/api/files/608d3ed645fe6aba0d762649/snag-1074.jpeg)


-----------------------------

## What About That "Trinket Problem"?

As mentioned at the of this page, this custom titlebar journey bagan with a problem happening here on Trinket.  Because there was no titlebar, ***always***, it meant our nice, simple window:

```python
import PySimpleGUI as sg

sg.theme('dark red')

layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN-')],
            [sg.Button('Go'), sg.Button('Exit')]  ]

sg.Window('Window Title', layout).read(close=True)

```

Always appeared like this on Trinket:

![SNAG-1076.jpg](/api/files/608d417d45fe6aba0d763193/snag-1076.jpeg "SNAG-1076.jpg")

That's not at all what Windows and Linux user experience.  Not only was this a confusing situation, it was problematic should you want to move the window.  There's no titlebar to grab and move the window.

It's enough to drive a PySimpleGUI user crazy!

![frust_112.png](/api/files/608d423245fe6aba0d763460/frust_112.png "frust_112.png")


## Custom Titlebar to the Rescue

2021 was kicked off with release 4.33.0 on Jan 2, 2021.  This is when the Custom Titlebar was released as part of PySimpleGUI. When PySimpleGUI detects that the program is running on Trinket, then a custom titlebar is added on your behalf, no additional code needed!

Now your program above, the simple one, results in this window:

![SNAG-1077.jpg](/api/files/608d436e45fe6aba0d7639f6/snag-1077.jpeg "SNAG-1077.jpg")

![love_112.png](/api/files/608d438e45fe6aba0d763aa6/love_112.png "love_112.png")

Don't believe it?  Let's give it a go and see how things work.  Go ahead... poke the run button.  

<iframe src='https://trinket.io/embed/pygame/8f5b7fb5b4?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>

You can modify this Trinket and you'll find that the Titlebar colors match your theme's colors (of course....).

-------------------------------

## Custom Menubars to Match

Custom Menubars are now part of PySimpleGUI.  You can get the effect of a Menubar that is styled in a way that matches your theme, by using using the MenubarCustom element. 

Like Custom Titlebars, it was initially released as a Demo Program.  You can run this demo on Trinket here:


<iframe src='https://trinket.io/embed/pygame/6fa4a60b7e?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>



