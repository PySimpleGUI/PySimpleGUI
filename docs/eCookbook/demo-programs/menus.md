## Menubar and Titlebar With Trinkets

## Menus - MenubarCustom instead of Menu

There's a tricky issue with Trinket.  Trinket doesn't supply a titlebar by default.  You may notice that many of the older examples here lack a titlebar.  That's because it's only been in 2021 that a custom titlebar was developed and automatically added when the runtime enironment is Trinket.

There's one issue with these Custom Titlebars.... you need a custom Menubar to go with them. -sigh-

You'll find MenubarCustom is an element that works much like a normal Menu element.  

## Info from original Trinket made in 2019, but code updated in 2021:

This demo shows you how you can add a menu bar to your program.
You will receive events that are the menu item's text or the menu
item's key.

The main purpose of this demo is to teach you the layout of a menu definition.
It is a basic Python list with listings inside that respresent the cascading
of menus.  You can go as deep as you with.

Notice that the `ButtonMenu` Element is a little different. The MenuBar and right click menus both return the menu item chosen as the event.  For the `ButtonMenu` Element the key of the button is returned.  The menu item chosen is in the values variable.  It's a 2-step process to get the menu item chosen for `ButtonMenu` elements.


<iframe src="https://trinket.io/embed/pygame/b96cfa2f55" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>