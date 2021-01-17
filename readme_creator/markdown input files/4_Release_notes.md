## Versions
|Version | Description |
|--|--|
| 1.0.9   | July 10, 2018 - Initial Release |
| 1.0.21 | July 13, 2018 - Readme updates  |
| 2.0.0 | July 16, 2018 - ALL optional parameters renamed from CamelCase to all_lower_case
| 2.1.1 | July 18, 2018 - Global settings exposed, fixes
| 2.2.0| July 20, 2018 - Image Elements, Print output
| 2.3.0 | July 23, 2018 - Changed form.Read return codes, Slider Elements, Listbox element. Renamed some methods but left legacy calls in place for now.
| 2.4.0 | July 24, 2018 - Button images. Fixes so can run on Raspberry Pi
| 2.5.0 | July 26, 2018 - Colors. Listbox scrollbar. tkinter Progress Bar instead of homegrown.
| 2.6.0 | July 27, 2018 - auto_size_button setting.  License changed to LGPL 3+
| 2.7.0 | July 30, 2018 - realtime buttons, window_location default setting
| 2.8.0 | Aug 9, 2018 - New None default option for Checkbox element, text color option for all elements, return values as a dictionary, setting focus, binding return key
| 2.9.0 | Aug 16,2018 - Screen flash fix, `do_not_clear` input field option, `autosize_text` defaults to `True` now, return values as ordered dict, removed text target from progress bar, rework of return values and initial return values, removed legacy Form.Refresh() method (replaced by Form.ReadNonBlockingForm()), COLUMN elements!!, colored text defaults
| 2.10.0 | Aug 25, 2018 - Keyboard & Mouse features (Return individual keys as if buttons, return mouse scroll-wheel as button, bind return-key to button, control over keyboard focus), SaveAs Button, Update & Get methods for InputText, Update for Listbox, Update & Get for Checkbox, Get for Multiline, Color options for Text Element Update, Progress bar Update can change max value, Update for Button to change text & colors, Update for Image Element, Update for Slider, Form level text justification, Turn off default focus, scroll bar for Listboxes, Images can be from filename or from in-RAM, Update for Image).  Fixes - text wrapping in buttons, msg box, removed slider borders entirely and others
| 2.11.0 | Aug 29, 2018 - Lots of little changes that are needed for the demo programs to work. Buttons have their own default element size, fix for Mac default button color, padding support for all elements, option to immediately return if list box gets selected, FilesBrowse button, Canvas Element, Frame Element, Slider resolution option, Form.Refresh method, better text wrapping, 'SystemDefault' look and feel setting
| 2.20.0 | Sept 4, 2018 - Some sizable features this time around of interest to advanced users.  Renaming of the MsgBox functions to Popup. Renaming GetFile, etc, to PopupGetFile. High-level windowing capabilities start with Popup, PopupNoWait/PopupNonblocking, PopupNoButtons, default icon, change_submits option for Listbox/Combobox/Slider/Spin/, New OptionMenu element, updating elements after shown, system default color option for progress bars, new button type (Dummy Button) that only closes a window, SCROLLABLE Columns!! (yea, playing in the Big League now), LayoutAndShow function removed, form.Fill - bulk updates to forms, FindElement - find element based on key value (ALL elements have keys now), no longer use grid packing for row elements (a potentially huge change), scrolled text box sizing changed, new look and feel themes (Dark, Dark2, Black, Tan, TanBlue, DarkTanBlue, DarkAmber, DarkBlue, Reds, Green)
| 2.30.0 | Sept 6, 2018 - Calendar Chooser (button), borderless windows, load/save form to disk
| 3.0.0 | Sept 7, 2018 - The "fix for poor choice of 2.x numbers" release. Color Chooser (button), "grab anywhere" windows are on by default, disable combo boxes, Input Element text justification (last part needed for 'tables'), Image Element changes to support OpenCV?, PopupGetFile and PopupGetFolder have better no_window option
| 3.01.01 | Sept 10, 2018 - Menus! (sort of a big deal)
| 3.01.02 | Step 11, 2018 - All Element.Update functions have a `disabled` parameter so they can be disabled.  Renamed some parameters in Update function (sorry if I broke your code), fix for bug in Image.Update. Wasn't setting size correctly, changed grab_anywhere logic again,added grab anywhere option to PupupGetText (assumes disabled)
| 3.02.00 | Sept 14, 2018 - New Table Element (Beta release), MsgBox removed entirely, font setting for InputText Element, **packing change** risky change that allows some Elements to be resized,removed command parameter from Menu Element, new function names for ReadNonBlocking (Finalize, PreRead), change to text element autosizing and wrapping (yet again), lots of parameter additions to Popup functions (colors, etc).
| 3.03.00 | New feature - One Line Progress Meters, new display_row_numbers for Table Element, fixed bug in EasyProgresssMeters (function will soon go away), OneLine and Easy progress meters set to grab anywhere but can be turned off.
| 03,04.00 | Sept 18, 2018 - New features - Graph Element, Frame Element, more settings exposed to Popup calls.  See notes below for more.
| 03.04.01 | Sept 18, 2018 - See release notes
| 03.05.00 | Sept 20, 2018 - See release notes
| 03.05.01 | Sept 22, 2018 - See release notes
| 03.05.02 | Sept 23, 2018 - See release notes
| 03.06.00 | Sept 23, 2018 - Goodbye FlexForm, hello Window
| 03.08.00 | Sept 25, 2018 - Tab and TabGroup Elements\
| 01.00.00 for 2.7 | Sept 25, 2018 - First release for 2.7
| 03.08.04 | Sept 30, 2018 - See release notes
| 03.09.00 | Oct 1, 2018 |
| 2.7 01.01.00 | Oct 1, 2018
| 2.7 01.01.02 | Oct 8, 2018
| 03.09.01 | Oct 8, 2018
| 3.9.3 & 1.1.3 | Oct 11, 2018
| 3.9.4 & 1.1.4 | Oct 16, 2018
| 3.10.1 & 1.2.1 | Oct 20, 2018
| 3.10.3 & 1.2.3 | Oct 23, 2018
| 3.11.0 & 1.11.0 | Oct 28, 2018
| 3.12.0 & 1.12.0 | Oct 28, 2018
| 3.13.0 & 1.13.0 | Oct 29, 2018
| 3.14.0 & 1.14.0 | Nov 2, 2018
| 3.15.0 & 1.15.0 | Nov 20, 2018
| 3.16.0 & 1.16.0 | Nov 26, 2018
| 3.17.0 & 1.17.0 | Dec 1, 2018

## Release Notes
2.3 - Sliders, Listbox's and Image elements (oh my!)

If using Progress Meters, avoid cancelling them when you have another window open.  It could lead to future windows being blank. It's being worked on.

New debug printing capability.  `sg.Print`

2.5 Discovered issue with scroll bar on `Output` elements.  The bar will match size of ROW not the size of the element.  Normally you never notice this due to where on a form the `Output` element goes.

Listboxes are still without scrollwheels. The mouse can drag to see more items.  The mouse scrollwheel will also scroll the list and will `page up` and `page down` keys.

2.7 Is the "feature complete" release. Pretty much all features are done and in the code

2.8 More text color controls.  The caller has more control over things like the focus and what buttons should be clicked when enter key is pressed. Return values as a dictionary! (NICE addition)

2.9 COLUMNS!  This is the biggest feature and had the biggest impact on the code base.  It was a difficult feature to add, but it was worth it.  Can now make even more layouts. Almost any layout is possible with this addition.

.................. insert releases 2.9 to 2.30 .................

3.0 We've come a long way baby!  Time for a major revision bump.  One reason is that the numbers started to confuse people  the latest release was 2.30, but some people read it as 2.3 and thought it went backwards.  I kinda messed up the 2.x series of numbers, so why not start with a clean slate.  A lot has happened anyway so it's well earned.

One change that will set PySimpleGUI apart is the parlor trick of being able to move the window by clicking on it anywhere.  This is turned on by default.  It's not a common way to interact with windows.  Normally you have to move using the titlebar.  Not so with PySimpleGUI.  Now you can drag using any part of the window.  You will want to turn off for windows with sliders.  This feature is enabled in the Window call.

Related to the Grab Anywhere feature is the no_titlebar option, again found in the call to Window.  Your window will be a spiffy, borderless window.  It's a really interesting effect.  Slight problem is that you do not have an icon on the taskbar with these types of windows, so if you don't supply a button to close the window, there's no way to close it other than task manager.

3.0.2 Still making changes to Update methods with many more ahead in the future.  Continue to mess with grab anywhere option.  Needed to disable in more places such as the PopupGetText function.  Any time these is text input on a form, you generally want to turn off the grab anywhere feature.

#### 3.2.0
 Biggest change was the addition of the Table Element.  Trying to make changes so that form resizing is a possibility but unknown if will work in the long run.  Removed all MsgBox, Get* functions and replaced with Popup functions.  Popups had multiple new parameters added to change the look and feel of a popup.

#### 3.3.0
OneLineProgressMeter function added which gives you not only a one-line solution to progress meters, but it also gives you the ability to have more than 1 running at the same time, something not possible with the EasyProgressMeterCall

#### 3.4.0

* Frame - New Element - a labelled frame for grouping elements. Similar
   to Column
* Graph (like a Canvas element except uses the caller's
   coordinate system rather than tkinter's).
* initial_folder - sets starting folder for browsing type buttons (browse for file/folder).
* Buttons return  key value rather than button text **If** a `key` is specified,
*
   OneLineProgressMeter!  Replaced EasyProgressMeter (sorry folks that's
   the way progress works sometimes)
 * Popup - changed ALL of the Popup calls to   provide many more customization settings
    * Popup
    * PopupGetFolder
    * PopupGetFile
    * PopupGetText
    * Popup
    * PopupNoButtons
    * PopupNonBlocking
    * PopupNoTitlebar
    * PopupAutoClose
    * PopupCancel
    * PopupOK
    * PopupOKCancel
    * PopupYesNo

#### 3.4.1
* Button.GetText - Button class method.  Returns the current text being shown on a button.
* Menu - Tearoff option. Determines if menus should allow them to be torn off
* Help - Shorcut button. Like Submit, cancel, etc
* ReadButton - shortcut for ReadFormButton

#### 3.5.0
* Tool Tips for all elements
* Clickable text
* Text Element relief setting
* Keys as targets for buttons
* New names for buttons:
   * Button = SimpleButton
   * RButton = ReadButton = ReadFormButton
* Double clickable list entries
* Auto sizing table widths works now
* Feature DELETED - Scaling. Removed from all elements

#### 3.5.1
* Bug fix for broken PySimpleGUI if Python version < 3.6 (sorry!)
* LOTS of Readme changes

#### 3.5.2
* Made `Finalize()` in a way that it can be chained
* Fixed bug in return values from Frame Element contents

#### 3.6.0
* Renamed FlexForm to Window
* Removed LookAndFeel capability from Mac platform.

#### 3.8.0
* Tab and TabGroup Elements - awesome new capabilities

#### 1.0.0 Python 2.7
It's official.  There is a 2.7 version of PySimpleGUI!

#### 3.8.2
* Exposed `TKOut` in Output Element
* `DrawText` added to Graph Elements
* Removed `Window.UpdateElements`
* `Window.grab_anywere` defaults to False

#### 3.8.3
* Listbox, Slider, Combobox, Checkbox,  Spin, Tab Group - if change_submits is set, will return the Element's key rather than ''
* Added change_submits capability to Checkbox, Tab Group
* Combobox - Can set value to an Index into the Values table rather than the Value itself
* Warnings added to Drawing routines for Graph element (rather than crashing)
* Window - can "force top level" window to be used rather than a normal window.  Means that instead of calling Tk to get a window, will call TopLevel to get the window
* Window Disable / Enable - Disables events (button clicks, etc) for a Window.  Use this when you open a second window and want to disable the first window from doing anything. This will simulate a 'dialog box'
* Tab Group returns a value with Window is Read.  Return value is the string of the selected tab
* Turned off grab_anywhere for Popups
* New parameter, default_extension, for PopupGetFile
* Keyboard shortcuts for menu items. Can hold ALT key to select items in men
* Removed old-style Tabs - Risky change because it hit fundamental window packing and creation. Will also break any old code using this style tab (sorry folks this is how progress happens)

#### 3.8.6

* Fix for Menus.
* Fixed table colors. Now they work
* Fixed returning keys for tabs
* Window Hide / UnHide methods
* Changed all Popups to remove context manager
* Error checking for Graphing objects and for Element Updates

### 3.9.0 & 1.1.0
* The FIRST UNIFIED version of the code!
* Python 2.7 got a TON of features . Look back to 1.0 release for the list
* Tab locations - Can place Tabs on top, bottom, left, right now instead of only the top

### 3.9.1 & 1.1.2
* Tab features
   * Themes
   * Enable / Disable
   * Tab text colors
   * Selected tab color
* New GetListValues method for Listbox
* Can now have multiple progress bars in 1 window
* Fix for closing debug-output window with other windows open
* Topanga Look and Feel setting
* User can create new look and feel settings / can access the look and feel table
* New PopupQuick call. Shows a non-blocking popup window with auto-close
* Tree Element partially done (don't use despite it showing up)

### 3.9.3 & 1.1.3

* Disabled setting when creating element for:
   * Input
  * Combo
  * Option Menu
  * Listbox
  * Radio
  * Checkbox
  * Spinner
  * Multiline
  * Buttons
  * Slider
* Doc strings on all Elements updated
* Buttons can take image data as well as image files
* Button Update can change images
* Images can have background color
* Table element new num_rows parameter
* Table Element new alternating_row_color parameter
* Tree Element
* Window Disappear / Reappear methods
* Popup buttons resized to same size
* Exposed look and feel table

###  3.9.4 & 1.1.4

* Parameter order change for Button.Update so that new button ext is at front
* New Graph.DrawArc method
* Slider tick interval parameter for labeling sliders
* Menu tearoff now disabled by default
* Tree Data printing simplified and made prettier
* Window resizable parameter.  Defaults to not resizable
* Button images can have text over them now
* BUG fix in listbox double-click.  First bug fix in months
* New Look And Feel capability.  List predefined settings using ListOfLookAndFeelValues

### 3.10.1 & 1.2.1
* Combobox new readonly parameter in init and Update
* Better default sizes for Slider
* Read of Tables now returns which rows are selected (big damned deal feature)
* PARTIAL support of Table.Update with new values (use at your own peril)
* Alpha channel setting for Windows
* Timeout setting for Window.Read (big damned deal feature)
* Icon can be base64 image now in SetIcon call
* Window.FindElementWithFocus call
* Window.Move allows moving window anywhere on screen
* Window.Minimize will minimize to taskbar
* Button background color can be set to system default (i.e. not changed)

### 3.10.2 & 1.2.2
Emergency patch release... going out same day as previous release
* The timeout timer for the new Read with timer wasn't being properly shut down
* The Image.Update method appears to not have been written correctly.  It didn't handle base64 images like the other elements that deal with images (buttons)


### 3.10.3 & 1.2.3

* New element - Vertical Separator
* New parameter for InputText - change_submits. If True will cause Read to return when a button fills in the InputText element
* Read with timeout = 0 is same as read non blocking and is the new preferred method
  * Will return event == None if window closed
* New Close method will close all window types
* Scrollbars for Tables automatically added (no need for a Column Element)
* Table Update method complete
* Turned off expand when packing row frame... was accidentally turned on (primary reason for this release)
* Try added to Image Update so won't crash if bad image passed in

### 3.11.0 & 1.11.0
* Syncing up the second digit of the releases so that they stay in sync better.  the 2.7 release is built literally from the 3.x code so they really are the same
* Reworked Read call... significantly.
* Realtime buttons work with timeouts or blocking read
* Removed default value parm on Buttons and Button Updates
* New Tree Element parm show_expanded. Causes Tree to be shown as fully expanded
* Tree Element now returns which rows are selected when Read
* New Window method BringToFront
* Shortcut buttons no longer close windows!
* Added CloseButton, CButton that closes the windows

### 3.12.0 & 1.12.0
* Changed Button to be the same as ReadButton which means it will no longer close the window
* All shortcut buttons no longer close the window
* Updating a table clears selected rows information in return values
* Progress meter uses new CloseButton
* Popups use new CloseButton

### 3.13.0 & 1.13.0
* Improved multiple window handling of Popups when the X is used to close
* Change submits added for:
  * Multiline
  * Input Text
  * Table
  * Tree
 * Option to close calendar chooser when date selected
 * Update for Tree Element
 * Scroll bars for Trees


### 3.14.0 & 1.14.0
* More windowing changes...
    * using a hidden root windowing (Tk())
    * all children are Toplevel() windows
* Read only setting for:
    * Input Text
    * Multiline
* Font setting for InputCombo, Multiline
* change_submits setting for Radio Element
* SetFocus for multiline, input elements
* Default mon, day, year for calendar chooser button
* Tree element update, added ability to change a single key
* Message parm removed from ReadNonBlocking
* Fix for closing windows using X
* CurrentLocation method for Windows
* Debug Window options
    * location
    * font
    * no_button
    * no_titlebar
    * grab_anywhere
    * keep_on_top
* New Print / EasyPrint options
    * location
    * font
    * no_button
    * no_titlebar
    * grab_anywhere
    * keep_on_top
* New popup, PopupQuickMessage
* PopupGetFolder, PopupGetFile new initial_folder parm


### 3.15.0 & 1.15.0

* Error checking for InputText.Get method
* Text color, background color added to multiline element.Update
* Update method for Output Element - gives ability to clear the output
* Graph Element - Read returns values if new flages set
    * Change submits, drag submits
    *   Returns x,y coordinates
* Column element new parm vertical_scroll_only
* Table element new parm - bind return key - returns if return or double click
* New Window parms - size, disable_close
* "Better" multiwindow capabilities
* Window.Size property
* Popups - new title parm, custom_text
    * title sets the window title
    * custom_text - single string or tuple string sets text on button(s)

### 3.16.0 & 1.16.0
* Bug fix in PopupScrolled
* New `Element` shortcut function for `FindElement`
* Dummy Stretch Element made for backwards compatibility with Qt
* Timer function prints in milliseconds now, was seconds

### 3.17.0 &1.17.0 2-Dec-2018
3.17.0 2-Dec-2017
* Tooltip offset now programmable.  Set variable DEFAULT_TOOLTIP_OFFSET.  Defaults to (20,-20)
* Tooltips are always on top now
* Disable menu items
* Menu items can have keys
* StatusBar Element (preparing for a real status bar in Qt)
* enable_events parameter added to ALL Elements capable of generating events
* InputText.Update select parameter will select the input text
* Listbox.Update - set_to_index parameter will select a single items
* Menus can be updated!
* Menus have an entry in the return values
* LayoutAndRead depricated
* Multi-window support continues (X detection)
* PopupScrolled now has a location parameter
* row_height parameter to Table Element
* Stretch Element (DUMMY) so that can be source code compatible with Qt
* ButtonMenu Element (DUMMY) so can be source code compat with Qt.  Will implement eventually

## 3.18.0  11-Dec-2018

 NOTE - **Menus are broken** on version 2.7.  Don't know how long they've been this way.  Please get off legacy Python if that's what you're running.

* Default progress bar length changed to shorter
* Master window and tracking of num open windows moved from global to Window class variable
* Element visibility setting (when created and when Updating element)
* Input text visiblity
* Combo visiblity
* Combo replaces InputCombo as the primary class name
* Option menu visibility
* Listbox visiblity
* Listbox new SetFocus method
* Radio visibility
* Checkbox visibility
* Spin visiblity
* Spin new Get method returns current value
* Multiline visiblity
* Text visibility
* StatusBar visiblity
* Output visibility
* Button visibility
* Button SetFocus
* ProgressBar - New Update method (used only for visibility)
* Image - clickable images!  enable_events parameter
* Image visibility
* Canvas visibility
* Graph visibility
* Graph - new DrawImage capability (finally)
* Frame visibility
* Tab visibility (may not be fully functional)
* TabGroup visibility
* Slider visibility
* Slider - new disable_number_display parameter
* Column visibilty
* Menu visibility - Not functional
* Table visibility
* Table - new num_rows parm for Update - changes number of visible rows
* Tree visiblity
* Window - New element_padding parameter will get padding for entire window
* OneLineProgressMeter - Completely REPLACED the implementation
* OneLineProgressMeter - can get reason for the cancellation (cancel button versus X)
* EasyProgressMeter - completely removed. Use OneLineProgressMeter instead
* Debug window, EasyPrint, Print - debug window will re-open if printed to after being closed
* SetOptions - can change the error button color
* Much bigger window created when running PySimpleGUI.py by itself.  Meant to help with regression testing

## 3.19.2  13-Dec-2018

* Warning for Mac's when trying to change button color
* New parms for Button.Update - image_size and image_subsample
* Buttons - remove highlight when border depth == 0
* OneLineProgressMeter - better layout implementation

## 3.20.0 & 1.20.0 18-Dec-2018

* New Pane Element
* Graph.DeleteFigure method
* disable_minimize - New parameter for Window
* Fix for 2.7 menus
* Debug Window no longer re-routes stdout by default
* Can re-route by specifying in Print / EasyPrint call
* New non-blocking for PopupScrolled
* Can set title for PopupScrolled window


## 3.21.0 & 1.21.0 28-Dec-2018

* ButtonMenu Element
* Embedded base64 default icon
* Input Text Right click menu
* Disabled Input Text are now 'readonly' instead of disabled
* Listbox right click menu
* Multiline right click menu
* Text right click menu
* Output right click menu
* Image right click menu
* Canvas right click menu
* Graph right click menu
* Frame right click menu
* Tab, tabgroup right click menu (unsure if works correctly)
* Column right click menu
* Table right click menu
* Tree right click menu
* Window level right click menu
* Window icon can be filename or bytes (Base64 string)
* Window.Maximize method
* Attempted to use Styles better with Combobox
* Fixed bug blocking setting bar colors in OneLineProgressMeter

# 3.22.0 PySimpleGUI / 1.22.0 PySimpleGUI27

* Added type hints to some portions of the code
* Output element can be made invisible
* Image sizing and subsample for Button images
* Invisibility for ButtonMenusup
* Attempt at specifying size of Column elements (limited success)
* Table Element
  * New row_colors parameter
  * New vertical_scroll_only parameter - NOTE - will have to disable to get horizontal scrollbars
* Tree Element
  * New row_height parameter
  * New feature - Icons for tree entries using filename or Base64 images
* Fix for bug sending back continuous mouse events
* New parameter silence_on_error for FindElement / Element calls
* Slider returns float now
* Fix for Menus when using Python 2.7
* Combobox Styling (again)


# 3.2.0 PySimpleGUI /  1.23.0 PySimpleGUI27 16-Jan-2019

* Animated GIFs!
* Calendar Chooser stays on top of other windows
* Fixed bug of no column headings for Tables
* Tables now use the font parameter

# 3.24.0 1.24.0 16-Jan-2019

* PopupAnimated - A popup call for showing "loading" type of windows

# 3.25 & 1.25 20-Feb-2019

* Comments :-)
* Convert Text to string right away
* Caught exceptions when main program shut down with X
* Caught exceptions in all of the graphics primitives
* Added parameter exportselection=False to Listbox so can use multiple listboxes
* OneLineProgressMeter - Can now change the text on every call if desired


## 3.27.0 PySimpleGUI  31-Mar-2019

Mixup.... 3.26 changes don't appear to have been correctly released so releasing in 3.27 now

* do_not_clear now defaults to TRUE!!!
  * Input Element
  * Multiline Element
* Enable Radio Buttons to be in different containers
* Ability to modify Autoscroll setting in Multiline.Update call
* PopupGetFolder, PopupGetFile, PopupGetText - title defaults to message if none provided
* PopupAnimated - image_source can be a filename or bytes (base64)
* Option Menu can now have values updated

## 3.28.0 11-Apr-2019 PySimpleGUI

* NEW Window Parameter - layout - second parameter. Can pass in layout directly now!
* New shortcuts
    * I = InputText
    * B = Btn = Butt = Button
* Convert button text to string when creating buttons
* Buttons are returned now as well as input fields when searching for element with focus

## 3.29 22-Apr-2019

* New method for `Graph` - `RelocateFigure`
* Output Element no longer accepts focus

## 3.32.0 PySimpleGUI 24-May-2019

* Rework of ALLL Tooltips. Was always displaying at uttuper left part of element. Not displays closer to where mouse entered or edited
* New Element.Widget base class variable. Brings tkinter into the newer architecture of user accessibility to underlying GUI Frameworks' widgets
* New SetTooltip Element method. Means all Elements gain this method. Can set the tooltip on the fly now for all elements
* Include scroll bar when making visible / invisible Listbox Elements
* New Radio Element method - `Radio.ResetGroup()` sets all elements in the Radio Group to False* Added borderwidth to Multiline Element
* `Button.Click()` - new method - Generates a button click even as if a user clicked a button (at the tkinter level)
* Made a Graph.Images dictionary to keep track of images being used in a graph.  When graph is deleted, all of the accociated images should be deleted too.'
* Added `Graph.SetFocus()` to give a Graph Element the focus just as you can input elements
* Table new parameter - `hide_vertical_scroll` if True will hide the table's vertical bars
* Window - new parameter - `transparent_color`. Causes a single color to become completely transparent such that you see through the window, you can click through the window. Its like tineows never was there.
* The new `Window.AllKeysDict = {}` has been adopted by all PySimpleGUI ports.  It's a new method of automatically creating missing keys, storing and retrieving keys in general for a window.
* Changed how `window.Maximize` is implemented previously used the '-fullscreen' attribute.  Now uses the 'zoomed' state
* Window gets a new `Normal()` method to return from Maximize state.  Sets root.state('normal')
* Window.Close() now closes the special `Window.hidden_master_root` window when the "last" window is closed
* `Window.SetTransparentColor` method added.  Same effect as if window was created with parameter set
* An Element's Widget stored in `.Widget` attribute
* Making ComboBox's ID unique by using it's Key
* Changed Multiline to be sunken and have a border depth setting now
* Removed a second canvas that was being used for Graph element.
* Changed how no titlebar is implemented running on Linux versus Windows. -type splash now used for Linux
* PopupScrolled - Added back using CloseButton to close the window
* Fixed PopupGetFolder to use correct PySimpleGUI program constructs (keys)
* PopupGetText populated values carrectly using the value variable, used keys
* PopupAnimated finally gets a completely transparent background


## 3.33.0 and 1.33 PySimpleGUI 25-May-2019

* Emergency fix due to debugger.  Old bug was that Image Element was not testing for COLOR_SYSTEM_DEFAULT correctly.


## 3.34.0 PySimpleGUI & 1.34.0 PySimpleGUI27 25-May-2019

  pip rhw  w cenf
* Fixed Window.Maximize and Window.Normal - needed special code for Linux
* Check for DEFAULT_SCROLLBAR_COLOR not being the COLOR_SYSTEM_DEFAULT (crashed)


## 3.35 PySimpleGUI & 1.35 PySimpleGUI27 27-May-2019

* Bug fix - when setting default for Checkbox it was also disabling the element!


## 3.36 PySimpleGUI & 1.36 PySimpleGUI27 29-May-2019

A combination of user requests, and needs of new `imwatchingyou` debugger

* New Debugger Icon for future built-in debugger
* Fixed bug in FindBoundReturnKey - needed to also check Panes
* NEW Window functions to turn on/off the Grab Anywhere feature
    * `Window.GrabAnyWhereOn()`
    * `Window.GrabAnyWhereOff()`
* New "Debugger" button that's built-in like other buttons.  It's a TINY button with a logo. For future use when a debugger is built into PySimpleGUI itself (SOON!)
* Change Text Element Wrap Length calculation.  Went fromn +40 pixels to +10 pixels in formula
* PopupGetFile has new parameter - `multiple_files`. If True then allows selection of multiple files


## 3.37 PySimpleGUI & 1.37 PySimpleGUI27 1-June-2019

* The built-in debugger is HERE - might not WORK exactly yet, but a lot of code went into te PySimpleGUI.py file for this.  At the moment, the `imwatchingyou` package is THE way to use a PySimpleGUI debugger. But soon enough you won't need that project in order to debug your program.
* Some strange code reformatting snuck in.  There are 351 differences between this and previous release.  I'm not sure what happened but am looking at every change by hand.
* New Calendar Button features
    * locale, format - new parameters to TKCalendar call
    * Use custom icon for window if one has been set
    * New parameters to CalendarButton - `locale`, `format`
* The bulk of the built-in PySimpleGUI debugger has been added but is not yet "officially supported".  Try pressing "break" or "ctrl+break" on your keyboard.
    * New bindings for break / pause button and debugger
    * New Debug button will launch debugger.
    * New parameter `debugger_enabled` added to Window call.  Default is __enabled__.
    * Your progam's call to Read is all that's needed to refresh debugger
    * New `Window` methods to control debugger access
        * `EnableDebugger` - turns on HOTKEYS to debugger
        * `DisableDebugger` - turns off HOTKEYS to debugger
* Restored wrap len for Text elements back from +10 to +40 pixels
* `PopupGetFolder`, `PopupGetFile` - fixed so that the "hidden" master window stays hidden (a Linux problem)
* Added support for Multiple Files to `PopupGetFiles` when no_window option has been set.


## 3.38 PySimpleGUI, 1.38 PySimpleGUI27

* Multiline - now has a "read only" state if created as "Disabled"
* Multiline - If window is created as resizable, then Multiline Elements will now expand when the window is enlarged, a feature long asked for.
* Output Element expands in the Y Direction
* "Expandable Rows" option added to PackFormIntoFrame allowing future elements to also expand
* Error Element - silence_on_error option
* Text Element wrapping - FINALLY got it right?  No more "Fudge factor" added
* PopupScrolled - Windows are now resizable
* Option to "launch built-in debugger" from the test harness
* Rememeber that the Debugger is still in this code!  It may or may not be operational as it's one version back from the latest release of the `imwatchingyou` debugger code. This code needs to be integrated back in

## 3.39 PySimpleGUI & 1.39 PySimpleGUI27 13-June-2019

* Ported the imwatchingyou debugger code into PySimpleGUI code
    * Replaced old debugger built-in code with the newer imwatchingyou version
    * Required removing all of the 'sg.' before PySimpleGUI calls since not importing
    * Dynamically create the debugger object when first call to `refresh` or `show` is made
* Started the procecss of renaming Class Methods that are private to start with _
* Needed for the automatic documentation generation that's being worked on
* Fixed crash when clicking the Debug button
* Fixed bug in DeleteFigure. Needed to delete image separately
* Added more type hints
* New `TabGroup` method `SelectTab(index)` selects a `Tab` within a `TabGroup`
* New `Table.Update` parameter - `select_rows`. List of rows to select (0 is first)
* Error checking in `Window.Layout` provides error "hints" to the user
    * Looks for badly placed ']'
    * Looks for functions missing '()'
    * Pops up a window warning user instead of crashing
    * May have to revisit if the popups start getting in the way
* New implementations of `Window.Disable()` and `Window.Enable()`
    * Previously did not work correctly at all
    * Now using the "-disabled" attribute
* Allow Comboboxes to have empty starting values
    * Was crashing
    * Enables application to fill these in later

# 4.0.0 PySimpleGUI & 2.0.0 PySimpleGUI27   19-June-2019

* DOC STRINGS DOCS STRINGS DOC STRINGS!
	* Your IDE is about to become very happy
	* All Elements have actual documentation in the call signature
	* The Readme and ReadTheDocs will be generated going forward using the CODE
	* HUGE Thanks for @nngogol for both copying & adding all those strings, but also for making an entire document creation system.
* New __version__ string for PySimpleGUI.py
* New parameter to ALL `SetFocus` calls. 	
	* def SetFocus(self, force=False)
	* If force is True, then a call to `focus_force` is made instead of `focus_set`
* Get - New Radio Button Method.  Returns True is the Radio Button is set
* Rename of Debugger class to _Debugger so IDEs don't get confused
* User read access to last Button Color set now available via property `Button.ButtonColor`
* Rename of a number of callback handlers to start with _
* Fix for memory leak in Read call. Every call to read lost a little memory due to root.protocol calls
* Listbox.Update - New parameter - scroll_to_index - scroll view so that index is shown at the top
* First PyPI release to use new documentation!


## PySimpleGUI 4.1 Anniversary Release!  4-Aug-2019

NEVER has there been this long of a lag, sorry to all users!
Long time coming.  Docstrings continue to be a focus.

* Version can be found using PySimpleGUI.version
* New bit of licensing info at the top of the file
* Types used in the doc strings. Also type hints in some comments. Because also running on 2.7 can't use full typing
* Added using of Warnings. Just getting started using this mechanism. May be great, maybe not. We'll see with this change
* Added TOOLTIP_BACKGROUND_COLOR which can be changed (it's tkinter only setting however so undertand this!)
* Graph.DrawText.  Ability to set `text_location` when drawing text onto a Graph Element.  Determines what part of the text will be located at the point you provide when you draw the text.   Choices are:
	* TEXT_LOCATION_TOP
	* TEXT_LOCATION_BOTTOM
	* TEXT_LOCATION_LEFT
	* TEXT_LOCATION_RIGHT
	* TEXT_LOCATION_TOP_LEFT
	* TEXT_LOCATION_TOP_RIGHT
	* TEXT_LOCATION_BOTTOM_LEFT
	* TEXT_LOCATION_BOTTOM_RIGT
	* TEXT_LOCATION_CENTER
* Flag ENABLE_TK_WINDOWS = False.  If True, all windows will be made using only tk.Tk()
* SetFocus available for all elements now due to it being added to base class. May NOT work on all elements however
* Added Combo.GetSElectedItemsIndexes() - returns a list of all currently selected items
* Fixed Listbox.Update - set_to_index changed to be an int, list or tuple
* Added parent parameter to call to tkinter's askopenfilename, directory, filenames.  Not sure why the root wasn't passed in before
* Button.Update - also sets the activebackground to the button's background color
* Graph - New parameter when creating. `float_values`.  If True, then you're indicating that your coordinate system is float not int based
* Graph.Update - made background color optional parm so that visible only can be set
* Frame.Layout returns self now for chaining
* TabGroup.Layout returns self now for chaining
* Column.Layout returns self now for chaining
* Menu.Update menu_definition is now optional to allow for changing visibility only
* Added inivisiblity support for menu bars
* Table.Update supports setting alternating row color and row_colors (list of rows and the color to set)
* Set window.TimeoutKey to TIMEOUT_KEY initially
* Window - check for types for title (should be string) and layout (should be list) and warns user if not correct
* Window - renamed some methods by adding _ in front (like Show) as they are NOT user callable
* Another shortcut! Elem = Element = FindElement
* SaveToDisk - will not write buttons to file.  Fixed problems due to buttons having keys
* Remapped Windowl.CloseNonBlockingForm, Window.CloseNonBlocking to be Window.CloseNonBlocking
* Fix for returning values from a combo list. Wasn't handling current value not in list of provided values
* Spin - Returns an actual value from list provided when Spin was created or updated
* Chaneged FillFormWithValues to use the new internal AllKeysDict dictionary
* Added try when creating combo. Problem happens when window is created twice.  Prior window had already created the style
* Added list of table (tree) ids to the Table element
* Enabled autoclose to use fractions of a second
* Added a try around one of the destroys because it could fail if user aborted
* Popup - Icon is no longer set to default by default
* Fix for debugger trying to execute a REPL comand.  The exec is only avilable in Python 3
* main() will display the version number in big letters when program is running

### 4.2 PySimpleGUI  2.2 for PySimpleGUI27  18 - Aug 2019

The cool lookup release!  No more need for FindElement. You can continue to use FindElement.
However, your code will look weird and ancient.  ;-)  (i.e. readable)
MORE Docstring and main doc updates!

* Finally 2.7 gets an upgrade and with it doc strings.  It however doesn't get a full-version bump like main PySimpleGUI as this may be its last release.
* New `window[key] == window.FindElement(key)`
* New Update calling method. Can directly call an Element and it will call its Update method
	* `window[key](value=new_value)    ==     window.FindElement(key).Update(value=new_value)`
* Made Tearoff part of element so anything can be a menu in theory
* Removed a bunch of `__del__` calls. Hoping it doesn't bite me in memory leaks
* Combo.Get method added
* Combo.GetSelectedItemsIndexes removed
* New Graph methods SendFigureToBack, BringFigureToFront
* Butten release changed for better Graph Dragging
	* Now returns key+"Up" for the event
	* Also returns the x,y coords in the values
* Tab.Select method added
* TabGroup.Get method added - returns key of currently selected Tab
* Window finalize parameter added - Will call finalize if a layout is also included.  No more need for Finalize!!
* Quiet, steady change to PEP8 user interface started
	* Now available are Window methods - read, layout, finalize, find_element, element, close
	* Should provide 100% PEP with these alone for most PySimpleGUI programs
* Added finding focus across ALL elements by using the .Widget member variable
* Fixed sizing Columns!  NOW they will finally be the size specified
* Fixed not using the initialdir paramter in PopupGetFile if the no_window option is set

## 4.3 PySimpleGUI Release 22-Aug-2019

PEP8 PEP8 PEP8
Layout controls!  Can finally center stuff
Some rather impactful changes this time
Let's hope it doesn't all blow up in our faces!

* PEP8 interfaces added for Class methods & functions
	* Finally a PEP8 compliant interface for PySimpleGUI!!
	* The "old CamelCase" are still in place and will be for quite some time
	* Can mix and match at will if you want, but suggest picking one and sticking with it
	* All docs and demo programs will need to be changed
* Internally saving parent row frame for layout checks
* Warnings on all Update calls - checks if Window.Read or Window.Finalize has been called
* Warning if a layout is attempted to be used twice
	* Shows an "Error Popup" to get the user's attention for sure
* Removed all element-specific SetFocus methods and made it available to ALL elements
* Listbox - no_scrollbar parameter added. If True then no scrollbar will be shown
* NEW finalize bool parameter added to Window. Removes need to "chain" .Finalize() call.
* NEW element_justification parameter for Column, Frame, Tab Elements and Window
	* Valid values are 'left', 'right', 'center'. Only first letter checked so can use 'l', 'c','r'
	* Default = 'left'
	* Result is that all Elements INSIDE of this container will be justified as specified
	* Works well with new Sizer Elements
* NEW justification parameter for Column elements.  
	* Justifies Column AND the row it's on to this setting (left, right, center)
	* Enables individual rows to be justified in addition to the entire window
* NEW Sizer Element
	* Has width and height parameters.  Can set one or both
	* Causes the element it is contained within to expand according to width and height of Sizer Element
	* Helps greatly with centering.  Frames will shrink to fit the contents for example. Use Sizer to pad out to right size
* Added Window.visibility_changed to match the PySimpleGUIQt call
* Fixed Debugger so that popout window shows any newly added locals


## 4.4 PySimpleGUI Release 5-Sep-2019

* window() - "Calling" your Window object will perform a Read call
* InputText - move cursor to end following Update
* Shortcuts - trying to get a manageable and stable set of Normal, Short, Super-short
	* DD - DropDown (Combo)
	* LB, LBox - Listbox
	* R, Rad - Radio
	* ML, MLine - Multiline
	* BMenu - ButtonMenu
	* PBar, Prog - ProgressBar
	* Col - Column
* Listbox - new method GetIndexes returns currently selected items as a list of indexes
* Output - new method Get returns the contents of the output element
* Button - For Macs don't don't allow setting button color. Previously only warned
* ButtonMenu - new Click method will click the button just like a normal Button's Click method
* Column scrolling finally works correctly with mousewheel. Shift+Mouse Scroll will scroll horizontally
* Table - Get method is a dummy version a Get because Qt port got a real Get method
* Table - Will add numerical column headers if Column Headsing is set to None when creating Table Element
* Table - FIXED the columns crazily resizing themselves bug!!
* Table - Can resize individual columns now
* Tree - was not returning Keys but instead the string representation of the key
* SetIcon will set to default base64 icon if there's an error loading icon
* Fix for duplicate key error. Was attempting to add a "unique key counter" onto end of keys if duplicate, but needed to turn into string first
* Columns
	* No longer expand nor fill
	* Sizing works for both scrolled and normal
* Setting focus - fixed bug when have tabs, columns, frames that have elements that can get the focus. Setting focus on top-level window
* InputText elements will now cause rows to expand due to X direction expansion
* Frame - Trying to set the size but doesn't seem to be setting it correctly
* Tabs will now expand & fill now (I hope this is OK!!!)

## 4.5 PySimpleGUI Release 04-Nov-2019

* Metadata!
	* All elements have a NEW metadata parameter that you can set to anything and access with Element.metadata
	* Windows can have metadata too
* Window.finalize() - changed internally to do a fully window.read with timeout=1 so that it will complete all initializations correctly
* Removed typing import
* ButtonReboundCallback - Used with tkinter's Widget.bind method. Use this as a "target" for your bind and you'll get the event back via window.read()
* NEW Element methods that will work on a variety of elements:
	* set_size - sets width, height. Can set one or both
	* get_size - returns width, heigh of Element (underlying Widget), usually in PIXELS
	* hide_row - hides the entire row that an element occupies
	* unhide_row - makes visible the entire row that an element occupies
	* expand - causes element to expand to fill available space in X or Y or both directions
* InputText Element - Update got new parameters: text_color=None, background_color=None, move_cursor_to='end'
* RadioButton - fix in Update. Was causing problems with loading a window from disk
* Text Element - new border width parameter that is used when there's a relief set for the text element
* Output Element - special expand method like the one for all other elements
* Frame element - Can change the text for the frame using Update method
* Slider element - can change range. Previously had to change value to change the range
* Scrollable frame / column - change to how mousewheel scrolls.  Was causing all things to scroll when scrolling a single column
	* NOTE - may have a bad side effect for scrolling tables with a mouse wheel
* Fix for icon setting when creating window.  Wasn't defaulting to correct icon
* Window.get_screen_size() returns the screen width and height.  Does not have to be a window that's created already as this is a class method
* Window.GetScreenDimensions - will return size even if the window has been destroyed by using get_screen_size
* Now deleting window read timers every time done with them
* Combo no longer defaults to first entry
* New Material1 and Material2 look and feel color schemes
* change_look_and_feel has new "force" parameter.  Set to True to force colors when using a Mac
* Fix in popup_get_files when 0 length of filename
* Fix in Window.SetIcon - properly sets icon using file with Linux now. Was always defaulting

## 4.6 PySimpleGUI 16-Nov-2019

* Themes!!!
* Added a LOT of Look and Feel themes. Total < 100 now
* Doctring comments for some missing functions
* PEP8 bindings for button_rebound_collback, set_tooltip, set_focus
* Spin Element Update - shortened code
* Allow tk.PhotoImage objeft to be passed into Image.update as the data
* DrawRectangle - added line_width parameter. Defaults to 1
* Fix for Slider - was only setting the trough color if the background color was being set_focus
* Added a deiconify call to Window.Normal so it can be used to restore a window that has been minimized.  Not working on Linux
* Combo - Fix for not allowing a "0" to be specified as the default
* Table - Saving the Frame that contains a table in the member variable table_frame.  This will enable the frame to be changed to expandable in the future so that the table can be resized as a window expands.
* LOTS AND LOTS of Look and Feel themes!!!!
* Added SystemDefaultForReal to look and feel that will prodce 100% not styled windows
* Changed the "gray" strings in look and feel table into RGB strtings (e.g. gray25 = #404040). No all graphics subsystems
* Removed Mac restriction from Look and Feel setting changes.  All color settings are changed EXCEPT for the button color now on a Mac
* "Fuzzy Logic" Look and Feel Theme Selection - No longer have to memorize every character and get the case right. Now can get "close enough" and it'll working
* New function - preview_all_look_and_feel_themes.  Causes a window to be shown that shows all of the currently available look and feel themes
* Removed use of CloseButton in popup get file, folder, text.  Was causing problems where input fields stopped working.  See bug on GitHub

## 4.7.0 PySimpleGUI 26-Nov-2019

TTK WIDGETS!  Welcome back Mac Users!

* Significant progress on using ttk widgets properly
* Added ttk buttons - MACS can use colored buttons again!!  (Big damned deal)
* The existing ttk based Elements are now correctly being colored and styled
* Ability to set the ttk theme for individual windows or system-wide, but no longer on a single Element basis
* Ability to use ttk buttons on a selective basis for non-Mac systems
* port variable == 'PySimpleGUI' so that your code can determine which PySimpleGUI is running
* InputText new parameter - use_readonly_for_dsiable defaults to True enables user to switch between a true disable and readonly setting when disabling
* Rework of progress bar's ttk style name
* Button - new parameter use_ttk_buttons - True = force use, False = force not used, None = let PySimpleGUI determine use
* Macs are forced to use ttk buttons EXCEPT when an image is added to the button
* TabGroup - can no longer set ttk theme directly
* Window new parameters
	* ttk_theme - sets the theme for the entire window
	* use_ttk_buttons - sets ttk button use policy for the entire window
* More Window layout error checking - checks that rows are iterables (a list). If not, an error popup is shown to help user find error
* Fixed progessbars not getting a key auto assigned to theme
* New Window method - send_to_back (SendToBack) - sends the window to the bottom of stack of all windows
* Fixed normal tk button text - was left justifying instead of centering
* Fixed table colors - wasn't setting correctly due to bad ttk styling
* Fixed tree ccolors - wasn't setting correctly due to bad ttk styling
* TabGroups now function correction with colors including currently selected tab color and background color of non-tab area (next to the tabs)
* New set_options parameters
	* use_ttk_buttons - sets system-wide policy for using ttk buttons. Needed for things like popups to work with ttk buttons
	* ttk_theme - sets system-wide tth theme
	* progress_meter_style parameter no longer used and generates a warning
* list_of_look_and_feel_values now sorts the list prior to returning
* Removed Mac restriction on Button colors from look and feel calls. Now can set button colors to anything!
* popup_scrolled new parameters - all popups need more parameters but these are for sure needed for the scrolled popup
	* background_color
	* text_color
	* no_titlebar
	* grab_anywhere
	* keep_on_top
	* font
* Test harness changes to help test new ttk stuff (want to shrink this window in the future so will fit on Trinket, Pi, etc	


## 4.8.0 PySimpleGUI 4-Dec-2019

Multicolored multiline text!  Often asked for feature going way back
ttk Buttons can have images
Print in color!

* Multiline Element got 2 new parameters to the update method
	* text_color_for_value - color for the newly added text
	* background_color_for_value - background color of the newly added text
* New Print/EasyPrint parameters and capability
	* text_color, background_color - control the text's color and background color when printing to "Debug Window"
	* Must be done only when used in mode where stdout is not re-routed (the default)
	* Wouldn't it be really nice if normal print calls had this parameter?
	* Print(event, text_color='green', background_color='white',  end='')
* ttk Buttons
	* can have images. No longer forces Buttons with images to be the old tk Butons. Now you can choose either	
	* can update the button color
	* can update the button image
* Set warning filter so that warnings are repeated
* New global variables:
	* CURRENT_LOOK_AND_FEEL - The current look and feel setting in use. Starts out as "Default"
	* BROWSE_FILES_DELIMITER - Defaults to ";"  It is the string placed between entries returned from a FilesBrowse button
	* TRANSPARENT_BUTTON - Depricated - was being used incorrectly as it was a relic from the early days. It's value was a color of gray
* Window - gentle reminder if you don't choose a look and feel for your window. It's easy to stop them. Add a change_look_and_feel line
* Test harness uses a debug window so don't be shocked when 2 windows appear when running PySimpleGUI by itself
	* Prints the "Event" in Green on White text
	* Prints the "values" normally

## 4.9.0 PySimpleGUI 7-Dec-2019

The "Finally Nailed Tabs" release

* Colors for Tabs!
	* When creating TabGroup can now specify
	* Text & Background color of all tabs
	* Text & Background color of selected tab
	* If nothing is specified then the Look and Feel theme will be used (which turned out GREAT)
* Tab visibility - Can finally control individual tab's visibility using update and when creating
* More "Look and Feel" Themes!  There's no excuse to be grey again. There are now 126 themes to choose from.  Here are the 32 new themes"
	DefaultNoMoreNagging
	DarkBlack1
	DarkBlue12
	DarkBlue13
	DarkBlue14
	DarkBlue15
	DarkBlue16
	DarkBlue17
	DarkBrown5
	DarkBrown6
	DarkGreen2
	DarkGreen3
	DarkGreen4
	DarkGreen5
	DarkGreen6
	DarkGrey4
	DarkGrey5
	DarkGrey6
	DarkGrey7
	DarkPurple6
	DarkRed2
	DarkTeal10
	DarkTeal11
	DarkTeal12
	DarkTeal9
	LightBlue6
	LightBlue7
	LightBrown12
	LightBrown13
	LightGray1
	LightGreen10
	LightGreen9
	LightGrey6
* preview_all_look_and_feel_themes now has a columns parameter to control number of entries per rows
	* also made each theme display smaller due to large number of themes


## 4.10.0 PySimpleGUI 9-Dec-2019

"Oh crap the debugger is broken!" + "Pretty Progress Bars" release

* Fix for built-in debugger not working
	* Important due to upcoming educational usage
	* Has been broken since 4.5.0 when a change to Finalize was made
* ProgessBar element colors set using Look and Feel colors
	* Combination of button color, input element, and input element text are used


## 4.11.0 PySimpleGUI 10-Dec-2019

The Element & Window bindings release

* Element.bind - New method of all Elements
	* Enables tkinter bindings to be added to any element
	* Will get an event returned from window.read() if the tkinter event happens
* Window.bind - New method for Windows, just like Elements
	* Enables tkinter bindings to be added to Windows
	* Will get an event returned from window.read() if the tkinter event happens
* TabGroup fonts - can now set the font and font size for Tab text



## 4.12.0 PySimpleGUI 14-Dec-2019

Finally no more outlines around TK Elements on Linux

* Fixed a long-term problem of the mysterious white border around (almost) all TK Elements on Linux
* Ability to set the disabled button colors
	* New Button and Button.update parameter - disabled_button_color
	* Specified as (Text Color, Background Color) just like button colors
	* For Normal / TK Buttons - can set button text color only
	* For TTK Buttons - can set both a disabled button and text color
	* Either parameter can be None to use current setting
* Removed use of CloseButton from Popups (still have a bug in the CloseButton code but not in popups now)
* Combobox - removed requirement of setting disabled if want to set to readonly using update method
* Fix for cancelling out of file/folder browse on Linux caused target to be cleared instead of just cancelling
* Removed try block around setting button colors - if user sets a bad color, well don't do that
* Now deleting windows after closing them for popup


## 4.13.0 PySimpleGUI 18-Dec-2019

Table and Tree header colors, expanded Graph methods

* Element.expand new parameter - expand_row. If true then row will expand along with the widgets. Provides better resizing control
* Using math.floor now instead of an int cast in Graph Element's unit conversions
* Graph.draw_point - now using caller's graph units for specifying point size
* Graph.draw_circle - converted radius size from user's graph units.
* Graph.draw_circle - added line_width parameter
* Graph.draw_oval - added line_width parameter
* Graph.get_figures_at_location - new method for getting a list of figures at a particular point
* Graph.get_bounding_box - returns bounding box for a previously drawn figure
* Table and Tree Elements
	* 3 new element creation parameters
		* header_text_color - color of the text for the column headings
		* header_background_color - color of the background of column headings
		* header_font - font family, style , size for the column headings
	* Defaults to using the current look and feel setting
		* Uses similar algorithm as Tabs - Input Text background and text colors are used
* Spin element - fixed bug that showed "None" if default value is "None"
* Test Harness sets incorrect look and feel on purpose so a random one is chosen


## 4.14.0 PySimpleGUI 23-Dec-2019

THEMES!

* theme is replacing change_look_and_feel. The old calls will still be usable however
* LOTS of new theme functions.  Search for "theme_" to find them in this documentation.  There's a section discussing themes too
* "Dark Blue 3" is the default theme now.  All windows will be colored using this theme unless the user sets another one
* Removed the code that forced Macs to use gray
* New element.set_cursor - can now set a cursor for any of the elements.  Pass in a cursor string and cursor will appear when mouse over widget
* Combo - enable setting to any value, not just those in the list
* Combo - changed how initial value is set
* Can change the font on tabs by setting font parameter in TabGroup
* Table heading font now defaults correctly
* Tree heading font now defaults correctly
* Renamed DebugWin to _DebugWin to discourage use


## 4.15.0 PySimpleGUI 08-Jan-2020

Dynamic Window Layouts!  Extend your layouts with `Window.extend_layout`
Lots of fixes

* Window.extend_layout
* Graph.change_coordinates - realtime change of coordinate systems for the Graph element
* theme_text_element_background_color - new function to expose this setting
* Radio & Checkbox colors changed to be ligher/darker than background
* Progress bar - allow updates of value > max value
* Output element does deletes now so that cleanup works. Can use in multiple windows as a result
* DrawArc (draw_arc) - New width / line width parameter
* RGB does more error checking, converts types
* More descriptive errors for find element	
* popup_error used interally now sets keep on top
* Element Re-use wording changed so that it's clear the element is the problem not the layout when re-use detected
* Window.Close (Window.close) - fix for not immediately seeing the window disappear on Linux when clicking "X"
* Window.BringToFront (bring_to_front) - on Windows needed to use topmost to bring window to front insteade of lift
* Multiline Scrollbar - removed the scrollbar color. It doesn't work on Windows so keeping consistent
* Changed how Debug Windows are created.  Uses finalize now instead of the read non-blocking
* Fix for Debug Window being closed by X causing main window to also close
* Changed all "black" and "white" in the Look and Feel table to #000000 and #FFFFFF
* Added new color processing functions for internal use (hsl and hsv related)
* popup - extended the automatic wrapping capabilities to messages containing \n
* Test harness uses a nicer colors for event, value print outs.
* _timeit decorator for timing functions



## 4.15.1 PySimpleGUI 09-Jan-2020

Quick patch to remove change to popup

## 4.15.2 PySimpleGUI 15-Jan-2020

Quick patch to remove f-string for 3.5 compat.


## 4.16.0 PySimpleGUI 20-Feb-2020

The "LONG time coming" release.  System Tray, Read with close + loads more changes
Note - there is a known problem with the built-in debugger created when the new read with close was added

* System Tray - Simulates the System Tray feature currently in PySimpleGUIWx and PySimpleGUIQt. All calls are the same. The icon is located just above the system tray (bottom right corner)
* Window.read - NEW close parameter will close the window for you after the read completes. Can make a single line window using this
* Window.element_list - Returns a list of all elements in the window
* Element.unbind - can remove a previously created binding
* Element.set_size - retries using "length" if "height" setting fails
* Listbox.update - select_mode parameter added
* Listbox.update - no longer selects the first entry when all values are changed
* Listbox.get - new. use to get the current values.  Will be the same as the read return dictionary
* Checkbox.update - added ability to change background and text colors.  Uses the same combuted checkbox background color (may remove)
* Multiline.update - fix for when no value is specified
* Multiline - Check for None when creating. Ignores None rather than converting to string
* Text.update - added changing value to string. Assumed caller was passing in string previously.
* Text Element - justification can be specified with a single character. l=left, r=right, c=center. Previously had to fully spell out
* Input Element - justification can be specified with a single character. l=left, r=right, c=center. Previously had to fully spell out
* StatusBar Element - justification can be specified with a single character. l=left, r=right, c=center. Previously had to fully spell out
* Image Element - can specify no image when creating.  Previously gave a warning and required filename = '' to indicate nothing set
* Table Element - justification can be specified as an "l" or "r" instead of full word left/right
* Tree Element - justification can be specified as an "l" or "r" instead of full word left/right
* Graph.draw_point - changed to using 1/2 the size rather than size. Set width = 0 so no outline will be drawn
* Graph.draw_polygon - new drawing method!  Can now draw polygons that fill
* Layout error checking and reporting added for - Frame, Tab, TabGroup, Column, Window
* Menu - Ability to set the font for the menu items
* Debug window - fix for problem closing using the "Quit" button
* print_to_element - print-like call that can be used to output to a Multiline element as if it is an Output element


## 4.17.0 PySimpleGUI 24-Mar-2020

The "it's been a minute" release
Improved DocStrings and documentation!
Upgrade utility
"Printing" directly to Multiline

* New upgrade utility to upgrade your installed package using GitHub version
    * Can invoke from command line. Run      `python -m PySimpleGUI.PySimpleGUI upgrade`
	* The test harness GUI has an upgrade button
* Multiline.print - Add multiline element to the front of any print statement.  Also supports color output
* Debug informmation like path and version displayed in test harness GUI
* Added back the TRANSPARENT_BUTTON variable until can find a better way to deprecate
* All elements were losing padding when made invisible. Fixed
* Image.update - fixed crash due to not checking for type before getting size
* Image.update_animation_no_buffering - playback GIF animations of any length
* Graph element - Fixed divide by zero error in convert function
* TabGroup will now autonumber keys if none specified
* Measuring strings more accurately during layout
	* Using specific font for measurement
	* Used to compute TTK button height
	* Used to compute Slider length
	* Used to compute header widths in Tables, Trees
	* Used to compute column widths in Tables, Trees
	* Used to compute row heights in Tables
* Removed padx from row frames.  Was using window's margins. Now padx & pady = 0. Was causing too every Column element to have extra padding
* Added no_titlebar to one line progress meter
* popup_notify - Creates a "notification window" that is like the System Tray Message window
* shell_with_animation - launch a shell command that runs while an animated GIF is shown
* Fixed problem with debugger not working after the recent close parameter addition to Window.read


## 4.18.0 PySimpleGUI 26-Mar-2020

An "Oh F**k" Release - Table column sizes were bad

* Fixed bug in Table Element's column size computation
* popup_animated has new title parameter
* Checkbox - update can change the text


## 4.18.1 PySimpleGUI 12-Apr-2020

Emergency patch - f-string managed to get into the code resulting crashes on 3.5 systems (Pi's for example) 

## 4.18.2 PySimpleGUI 12-Apr-2020

The Epic Fail release.... import error on 3.5 for subprocess.

## 4.19.0 PySimpleGUI 5-May-2020

New Date Chooser
Scrollable columns with mousewheel!! (oh please work right!)
WINDOW_CLOSE & WIN_CLOSE events
Long list of stuff!

* Imported from typing again to get correct docstrings
* Print and MLine.Print fixed sep char handling 
* New parameter to Muliline.print(autoscroll parameter)
* New autoscroll parameter added to _print_to_element
* popup_get_date 
* Complete reworking on Calendar Chooser Button
	* Has a LOT more paramteter
	* Can set location!
* icon parm popup_animated 
* popup button size (6,1) for all popups
* NEW CALENDAR chooser integrated 
* Graph.draw_lines - new method to allow for multiline lines that may not be a full polygon
* System Tray fixed the docstrings
* color chooser set parent window (needed for icon?)
* scrollable column scrollwheel fixed 
* fixed TabGroup border width (wasn't getting set properly at all)
* EXPERIMENTAL Scrollable Columns 
* Fixed Debug Printing to work like a normal "print"
* Fixed _print_to_element to work like a normal "print"
* Fixed light green 1 theme definition - Text color wasn't being set
* fix for install from GitHub 
* fix for Column scrolling with comboboxes 
* Added Text.get 
* Spin.update fix 
* import typing again 
* fixes for Pi 
* test for valid ttk_theme names 
* fix for Text.get docstring 
* added tuples to some docstrings 
* added code for better tag handling for Multiline elements (fixes a potential memory leak... thanks Ruud)
* WIN_CLOSE & WINDOW_CLOSED constants added.  Both are None
* EVENT_TIMEOUT and TIMEOUT_EVENT constants added to both be the same as TIMEOUT_KEY
* Some changes in test harness that tested recent changes (may still need shortening for trinket or others)
* Changed the misleading TRANSPARENT_BUTTON constant with an attempt using themes calls


## 4.20.0 PySimpleGUI 6-Jun-2020

Fixes and new features... broad range

* Fix for Typing import for Pi (3.4) users.  Now "tries" to import typing
* Tooltip fonts - can change the font for tooltips
* Fixed tearoff for Menus.  Had stoppped working
* Radio - If element is updated to False, the entire group of radio buttons will be set to false tooltips
* Multiline - fix for colors. Only set tags for output that has specific colors
* Multiline - keeping track of disabled with Disabled mumber variable
* Progress bar
	* Added class variable "uniqueness counter" so that every bar will have its own settings
	* Needed in case the same key is used in another window
* Fix for stdout being reset if someone sets flush on their call to print
* Mac special case added to tkfiledialog.askdirectory just like on askopenfilename
* Tab - can "update" the title
* Menu update - was not applying font when updating the menu
* Window.set_title - allows you to change the title for a window
* Added searching through Panes when looking for element with focus
* Removed Python 2 Add Menu Item code
* Added font to buttonmenu.
* Added font to the combobox drop-down list (wow what a pain)
* Table now uses the element's padding rather than 0,0
* Tree now uses the element's padding rather than 0,0
* set_options - added ability to set the tooltip font
* Fixed a couple of docstrings
* Reworked main() test harness to display DETAILED tkinter info and use better colors


## 4.21.0 PySimpleGUI 27-Jun-2020

Horizontal Separator, cprint, docstrings

* New color printing function cprint - enables easy color printing to an element
* Tons of docstring fixups (300+ changes)
* Removed old Python2 checks
* Added Element.set_vscroll_position - scroll to a particular % of the way into a scrollable widget
* Input Text - new parameters
	* border_width
	* read_only (for tkinter will have to be disabled OR readonly.  Cannot be both)
	* disabled_readonly_background_color
	* disabled_readonly_text_color
* Radio - Backed out the change that cleared all buttons in group because already have that ability using reset_group
* Graph drag mouse up events returned as either a string + "+UP" (as before) or as a tuple with "+UP" being added onto a tuple key
* Vertical separator - added key and color - color defaults to text color
* Horizontal separator!  (FINALLY). Color defaults to text color
* Fix for Table and Tree elements not automatically getting a key generated if one wasn't supplied
* Made key parameter for one_line_progress_meter have a default value so don't have to specify it when you have only 1 running
* theme_add_new - adds a new theme entry given a theme name and a dictionary entry. This way you don't have to directly modify the theme dictionary
* Added initial_folder to popup_get_folder when there is no window
* Added default_path to popup_get_file when there is no window
* Fix for removing too many PySimpleGUI installs when using the GitHub upgrade tooltip


## 4.22.0 PySimpleGUI 28-Jun-2020

More cprint stuff

* Additional window and key parameter to cprint
	* May seem like a small change, but the results are powerful
	* Can now easily "print" to anywhere, in color!
	

## 4.23.0 PySimpleGUI 3-Jul-2020

Table Colors Fix - workaround for problems with tables and tree colors in Python 3.7.2 to 3.9+
Mac crash fixed - tkinter.TclError: expected boolean value but got "" (hopefully)
New shortcut "k" parameter for all elements that is the same as "key" - may be experimental / temporary if not well received
More error checks
popup extensions


* Fix for missing Table and Tree colors created in tk 8.6.9
	* This is a problem in all versions of  Python 3.7.2 - 3.9.0 with no target fix date published
	* As a result of no fixes in sight, added a fix in PySimpleGUI if the tk version is 8.6.9
* New Element creation parameter "k" - exact same thing as "key" but shorter. Helps with complex layouts
* New error reporting on all element.update calls - checks to see if element has been fully created
* set_options - new option to supress popup_errors coming from PySimpleGUI.py
* Mac specific crash fix - if on a Mac, no longer calling wm_overrideredirect as it crashes the Mac now
* Additional error checking (shows error instead of asserting:
	* Check for Widget creation before widget operations like bind, unbind, expand
	* Check for window finalize / read before some window operations like maximize, hide, etc
* docstrings - more added.  Fixed up a number of missing / erroneous ones
* Tree element - caches images so that will not create new ones if previously used on another Tree item
* popup - two new options
	* any_key_closes - bool.  If True, any key pressed will close the window
	* image - can be a bytes (base64) or string (filename). Image will be shown at top of the popup
* all popups - new image parameter (base64 or string)
* a few new built-in icons
	

## 4.24.0 PySimpleGUI 3-Jul-2020

Selective control over tk 8.6.9 treeview color patch

* Disabled the code that patched the problem with background colors for Tree and Table elements
* Can enable the patched code by calling set_options
	* To enable set parameter enable_treeview_869_patch = True (defaults to false)



## 4.25.0 PySimpleGUI 17-Jul-2020

Biggest / most impactful set of changes in a while (fingers crossed)
Modal windows
Multithreaded Window.write_event_value method
stdout re-route to any Multiline
table/tree highlights
k element parameter

* New "k" parameter for all elements. 
	* Same as "key"
	* Created so layouts can be even more compact if desired
	* New docstring for keys (basically anything except a list)
* Popups
	* New text wrap behavior. Will wrap text between \n in user's string
	* All popups are now "modal" unless they are non-blocking (can be turned off using new parameter)
* New button color and table/tree highlight color format
	* Colors can still be tuple (text, background)
	* Can also be a single string with format "text on background" (e.g. "white on red")
* Multiline
	* Automatically refresh window when updating multiline or output elements
	* For cprint use Multiline's autoscroll setting
	* New autoscroll parameter in Multiline.print
	* New parameters to make the print and cprint stuff much easier
		* write_only=False (so that it's not returned when read)
		* auto_refresh=False
		* reroute_stdout=False
		* reroute_stderr=False
		* reroute_cprint=False (removes need to call the cprint cprint_set_output_destination function)
* Table / Tree Elements
	* Re-enabled the tk 8.6.9 background color fix again
	* selected_row_colors=(None, None) - tuple or string
	* Automatically sets the selected row color based on the theme colors! (uses the button color)
	* Can use 2 other constants for colors
		* OLD_TABLE_TREE_SELECTED_ROW_COLORS - ('#FFFFFF', '#4A6984') the old blueish color
		* ALTERNATE_TABLE_AND_TREE_SELECTED_ROW_COLORS - (SystemHighlightText, SystemHighlight)
	* Tree image caching happens at the element level now
* Window	
	* make_modal - new method to turn a window into a modal window
	* modal parameter when window is created.  Default is False
	* write_event_value - new method that can be called by threads!  This will "queue" an event and a value for the next window.read()
	* Display an error popup if read a closed window 100+ times (stops you from eating 100% of the CPU time)
	* was_closed method added - returns True if a window has been closed
* Combo - don't select first entry if updated with a new set of values
* Tooltip - fix for stuck-on tooltips
* New theme_previewer with scrollbars. 3 new parameters	
* cprint - now has all parameters shown in docstring versus using *args **kwargs	
* New global variable __tclversion_detailed__ - string with full tkinter version (3 numbers instead of 2)
* Warning is displayed if tcl version is found to be 8.5.


## 4.26.0 PySimpleGUI 18-Jul-2020

* Multi-threaded tkvar initialization location changed so that thread doesn't intialize it now
* Removed thread key - no longer needed
* Window.write_event_values - now requires both parms
* Upgrade button typo


## 4.27.4 PySimpleGUI 3-Aug-2020

Multi-window support done right!
New capabilities for printing, Multiline
Main app additions
Theme searching

* read_all_windows - function that reads all currently open windows.
	* Finally the efficient multi-window solution
	* No longer need to do round-robin type scheduling
	* Easily convert existing programs from single to multi-windows
	* Demo programs with multi-window design patterns all updated
	* Ideal for "floating palette / toolbar" window adds-ons
	* Can read with timeout including timeout=0
* theme_previewer
	* search option
	* button in main app
	* reset to previous theme following preview
* Sponsor button in main app
* Theme previewer in main app
* Progress bar 
	* colors can use the single string "foreground on background" color format
	* update_bar combined with update for a single update interface
* Better element key error handling
	* 3 options to control how lookup errors are handled
	* popup now shows
		* file, function, line #, actual line of code with error
		* erroneous key provided
		* best matching key
	* will automatically try to continue with best matching key
	* can assert with key error if desired (true by default)
* fix for get item
* Up/down arrow bindings for spinner if enabling events
* Multiline 
	* new justification parameter on creation and update
	* print - justification parameter added
* cprint - justification parameter added - note tricky to set color of single word but possible	
* Added mousewheel for Linux return_keyboard_events enabled
* Added get_globals function for extending easier
* Refactored callbacks
* Image element - can clear image by not setting any parameters when calling update
* Column Element's Widget member variable now being set
* Window's starting window location saved
* Early experimental "Move all windows in sync" when using grab_anywhere (coming soon)
* Fix for 3.4 (can't use f-strings)


## 4.28.0 PySimpleGUI 3-Aug-2020

Element pinning for invisibility!

* Better visible/invisible handling
	* pin - new function to place an element in a layout that will hold its position
	* border_width added to Canvas and Graph (so that they will default to 0)
* Combobox
	* button color will match theme's button color
	* background color set correctly when readonly indicated
* Spin element
	* spin button color set to background color of spinner
	* spin arrow color automatically set to text color
* Bad element key popup - fix for displaying correct line info in some situations


## 4.29.0 PySimpleGUI 25-Aug-2020

Custom titlebar capabilities (several new features required)
Better Alignment
Calendar button works again

* Window.visiblity_changed now refreshes the window 
* Added Column.contents_changed which will update the scrollbar so corrently match the contents
* Separators expand only in 1 direction now
* Added 8 SYMBOLS:
	SYMBOL_SQUARE = '█'
	SYMBOL_CIRCLE = '⚫'
	SYMBOL_CIRCLE_OUTLINE = '◯'
	SYMBOL_UP =    '▲'
	SYMBOL_RIGHT = '►'
	SYMBOL_LEFT =  '◄'
	SYMBOL_DOWN =  '▼'
	SYMBOL_X = '❎'
* New dark themes - dark grey 8, dark grey 9, dark green 9, dark purple 7
* When closing window no longer deletes the tkroot variable and rows but instead set to None
* Changd no-titlebar code to use try/except. Previously removed for Mac due to tk 8.6.10 errors calling wm_overrideredirect
* Fix for Column/window element justification
* New vertical_alignment parm for Column, Frame, pin
* New layout helper functions - vtop/vcenter/vbottom - Can pass an element or a row of elements
* Fixed statusbar expansion
* Added disabled button to theme previewer
* Fixed grab anywhere stop motion bug - was setting position to None and causing error changed to event.x
* Expanded main to include popup tests, theme tests, ability to hide tabs
* Grab parameter for Text Element, Column Element
* Added tclversion_detailed to get the detailed tkinter version
* All themes changed the progress bar definition that had a "DEFAULT" indicator. New constant DEFAULT_PROGRESS_BAR_COMPUTE indicates the other theme colors should be used to create the progess bar colors.
* Added expand_x and expand_y parameters to Columns
* Fix for Calendar Button.  Still needs to be fixed for read_all_windows
* Force focus when no-titlebar window. Needed for Raspberry Pi
* Added Window.force_focus
* No longer closes the hidden master window. Closing it caused a memory leak within tkinter
* Disable close on one_line_progress_meter. There is a cancel button that will close the window
* Changed back toplevel to no parent - was causing problems with timeout=0 windows


## 4.30.0 PySimpleGUI 14-Oct-2020

User Settings APIs, lots more themes, theme swatch previewer, test harness additions

* Added shrink parameter to pin, 
* added variable Window.maximized, 
* added main_sdk_help_window function, 
* New themes - DarkGrey10,DarkGrey11 DarkGrey12 DarkGrey13 DarkGrey14, Python, DarkBrown7
* Highlight Thickness for Button, Radio, Input elements
	* Set to 1 now instead of 0 so that focus can be seen
	* Color is automatically set for buttons, checkboxes, radio buttons
	* Color can be manually set for Buttons using `highlight_colors` parameter
	* Only used by Linux
* user_settings APIs
	* Whole new set of API calls for handling "user settings"
	* Settings are saved to json file
	* For more info, see the documentation
* Radio.update - added text, background & text colors parameters
* Multiline & Output Elements:
	* added parameter echo_stdout_stderr
	* if True then stdout & stderr will go to the console AND to the Multiline
* "ver" is shortened version string
* modal docstring fix in some popups
* image parameter implemented in popup_scrolled
* Graph.draw_image - removed color, font, angle parameters
* fixed blank entry with main program's theme previewer
* added Window.set_min_size
* error message function for soft errors
* focus indicator for Button Checkbox Radio using highlights
* added main_sdk_help Window
* added theme_previewer_swatches function
* added "Buy Me A Coffee" button
* updated `pin` layout helper function - added `shrink` parameter
* Main debugger window set to keep on top



## 4.31.0 PySimpleGUI 13-Nov-2020

User Settings class, write_event_value fixes, Menus get colors, Mac no_titlebar patch

* InputText element - Now treating None as '' for default
* Combo - handling update calls with both disabled and readonly set
* Spin - readonly 
	* Added parameter added when creating
	* Added parameter to update
* Spin.get() now returns value rather than string version of value
* Multiline print now autoscrolls by default
* FileSaveAs and SaveAs now has  default_extension parameter like the popup_get_file has
* Button Menu - Color and font changes
	* New create parameters - background color, text color, disabled text color, item font
	* Fixed problem with button always being flat
* Menu (Menubar) - Color changes
	* New create paramters - text color, disabled text color.
	* Hooked up background color parameter that was already there but not functional
* write_event_value - fixed race conditions
	* Window.read() and read_all_windows() now checks the thread queue for events before starting tkinter's mainloop in case events are queued
* Window.set_cursor added so that window's cursor can be set just like can be set for individual elements
* Icon is now set when no_window option used on popup_get_file or popup_get_folder
* Reformatted the theme definitions to save a LOT of lines of code
* UserSettings class
	* Added a class interface for User Settings
	* Can still use the function interface if desired
	* One advantage of class is that [ ] can be used to get and set entries
	* Looks and acts much like a "persistent global dictionary"
	* The User Settings function interfaces now use the class
* main_get_debug_data() 
	* Function added that will display a popup and add to the clipboard data needed for GitHub Issues
	* Added button to Test Harness to display the popup with version data
* Mac - Added parm enable_mac_notitlebar_patch to set_options to enable apply a "patch" if the Window has no_titlebar set.


## 4.32.0 PySimpleGUI 17-Nov-2020

Menu colors and font, fixes

* Menu, ButtonMenu, and right click menu now default to theme colors and Window font
	* The background color for menus is the InputText background color
	* The text color for menus is the InputText text color
	* The font defaults to the Window font
	* These theme colors have worked well in the past as they are the settings used for Table and Tree headers
	* All settings can be changed
* Added ability to set the right click menu colors and font
	* New parameters added to Window to control right click look
* Fixed problem with Button.update. 
	* Was crashing if button color changed to COLOR_SYSTEM_DEFAULT
* Fixed problem with right click menus introduced in the previous release
* Auto-close windows can now be finalized (previously could not do this)
* Window.read with timeout is faster



## 4.32.1 PySimpleGUI 17-Nov-2020

* Bug in finalize code


## 4.33.0 PySimpleGUI 2-Jan-2021 (Happy New Year!)

The let's kickoff 2021 release!

Custom Titlebars, Fix for Docstrings so PyCharm 2020 works correctly, New shortcuts, Window Close Attempted

* Custom Titlebar - new element
	* Initial reason was Trinket, but great feature overall
	* Allows windows to be styled to match the colors of the window
	* Automatically uses theme for colors
	* Automatically used when running on Trinket
	* Can specify using them by using set_options, a Titlebar element, or parameters in Window creation
	* Documentation is coming soonish
	* Demo exists showing how to use (it's enough that you won't need a Cookbook / detailed docs to add it to your own program)
	* Changes include adding a 16x16 pixel version of the PySimpleGUI icon
	* popups - If custom titlebar is set using set_options (and is thus globally applied) then popups will use the custom titlebar
* MASSIVE number of changes to docstrings so that PyCharm again works correctly.  All Unions had to be changed to use "|" instead
* Internal functions added to check what OS is being used rather than having os.platform checks all over thee place
* Element.Visible removed. Element.visible property returns current visibility state for element
	* This is a read-only property
* Added dummy Element.update method so that PyCharm doesn't complain about a missing method
* InputElement class changed to Input.  Both will work as InputElement is now an alias
* Fix in Spin.update.  Was using an illegal state value of "enable" rather than "normal"
* New Shortcuts for Elements
	* Sp = Spin
	* SBar = StatusBar
	* BM = ButtonMenu
	* Progress = ProgressBar
	* Im = Image
	* G = Graph
	* Fr = Frame
	* Sl = Slider
* Button - Allow button color background to be specified as None. This will cause the theme's color to be auto chosen as background
* Image.DrawArc - fill_color parameter added
* Column - update now uses the expand information so that a column will re-pack correctly when made invisible to visible. Added fill parm to pack call
* New Window parameters:
	* enable_close_attempted_event=False
    * titlebar_background_color=None
	* titlebar_text_color=None
	* titlebar_font=None
	* titlebar_icon=None
    * use_custom_titlebar=None
* Removed "Faking Timeout" print because the state that triggered it can be reached using a normal auto-closing window
* Can now intercept window close attempts when the user clicks X
	* If you don't want "X" to close the window, set enable_close_attempted_event to True when creating window
	* When enabled a WINDOW_CLOSE_ATTEMPTED_EVENT will be returned from read instead of WIN_CLOSED
	* Multiple aliases for the key: WINDOW_CLOSE_ATTEMPTED_EVENT, WIN_X_EVENT, WIN_CLOSE_ATTEMPTED_EVENT
* New Window property - key_dict
	* Returns the "All keys dictionary" which has keys and elements for all elements that have keys specified
* pin helper function got 2 new parameters - expand_x=None, expand_y=None.  Was needed for the Titlebar element
* no_titlebar implementation changed on Linux. Not using "splash" and instead using "dock". Was needed to get the minimize/restore to work
* New set_options parameters in support of custom Titlebar element
	* use_custom_titlebar=None
	* titlebar_background_color=None
	* titlebar_text_color=None
	* titlebar_font=None
	* titlebar_icon=None
* get_globals removed - not required for normal PySimpleGUI.  Was only used by patched packages which will need to fork PySimpleGUI for this feature.
* popup - support for custom titlebar!
* Changed from pathlib to os.path



## Upcoming

The future for PySimpleGUI looks bright!  

The overall roadmap is a simple one:
* Continue to build-out the tkinter port
* Continue to bring features forward from the tkinter port to the other ports (Qt, WxPython, Remi)
* Add mobile applications (native built applications instead of PyDriod3 that's used today)



## Code Condition

    Make it run
    Make it right
    Make it fast

It's a recipe for success if done right.  PySimpleGUI has completed the "Make it run" phase.  It's far from "right" in many ways.  These are being worked on.  The module has historically been particularly poor for PEP8 compliance.  It was a learning exercise that turned into a somewhat complete GUI solution for lightweight problems.

While the internals to PySimpleGUI are a tad sketchy, the public interfaces into the SDK are more strictly defined and comply with PEP8 naming conventions.  A set of "PEP8 Bindings" was released in summer of 2019 to ensure the externally facing interfaces all adhere to PEP8 names.

Please log bugs and suggestions **only on the PySimpleGUI GitHub**!  It will only make the code stronger and better in the end, a good thing for us all, right?  Logging them elsewhere doesn't enable the core developer and other PySimpleGUI users to help.  To make matters worse, you may get bad advice from other sites because there are simply not many PySimpleGUI experts, yet.

## Design

A moment about the design-spirit of `PySimpleGUI`.  From the beginning, this package was meant to take advantage of Python's capabilities with the goal of programming ease.

**Single File**
While not the best programming practice, the implementation resulted in a single file solution.  Only one file is needed, PySimpleGUI.py.  You can post this file, email it, and easily import it using one statement.

**Functions as objects**
In Python, functions behave just like object. When you're placing a Text Element into your form, you may be sometimes calling a function and other times declaring an object.  If you use the word Text, then you're getting an object.  If you're using `Txt`, then you're calling a function that returns a `Text` object.

**Lists**
It seemed quite natural to use Python's powerful list constructs when possible.  The form is specified as a series of lists.  Each "row" of the GUI is represented as a list of Elements. 

**Dictionaries**
Want to view your form's results as a dictionary instead of a list... no problem, just use the `key` keyword on your elements.  For complex forms with a lot of values that need to be changed frequently, this is by far the best way of consuming the results.

You can also look up elements using their keys.  This is an excellent way to update elements in reaction to another element.  Call `form.FindElement(key)` to get the Element.

**Named / Optional Parameters**
This is a language feature that is featured **heavily**  in all of the API calls, both functions and classes.  Elements are configured, in-place, by setting one or more optional parameters.  For example, a Text element's color is chosen by setting the optional `text_color` parameter.

**tkinter**
tkinter is the "official" GUI that Python supports.  It runs on Windows, Linux, and Mac.  It was chosen as the first target GUI framework due to its ***ubiquity***.  Nearly all Python installations, with the exception of Ubuntu Linux, come pre-loaded with tkinter.   It is the "simplest" of the GUI frameworks to get up an running (among Qt, WxPython, Kivy, etc).

From the start of the PSG project, tkinter was not meant to be the only underlying GUI framework for PySimpleGUI.  It is merely a starting point.  All journeys begin with one step forward and choosing tkinter was the first of many steps for PySimpleGUI.  Now there are 4 ports up and running - tkinter, WxPython, Qt and Remi (web support)


# Author & Owner

Written and owned by The PySimpleGUI Organization

This documentation as well as all PySimpleGUI documentation and  code is Copyright 2018, 2019, 2020 by PySimpleGUI.org

Send correspondence to PySimpleGUI@PySimpleGUI.com

## License

GNU Lesser General Public License (LGPL 3) +

## Acknowledgments

There are a number of people that have been key contributors to this project both directly and indirectly.  Paid professional help has been deployed a number of critical times in the project's history.  This happens in the life of software development from time to time.

If you've helped, I sure hope that you feel like you've been properly thanked.  That you have been recognized.  If not, then say something.... drop an email to comments@PySimpleGUI.org. 

## Support

In response to a number of email contacts from individuals and corporations that are using PySimpleGUI that wanted to financially support the project a "Support" Button was added to the GitHub site.  This support button is connected with a PayPal account.  If you wish to help support this currently freely supplied software and free technical support, then follow this link: www.paypal.me/psgui . 

To be clear, this is not a solicitation for your money.  No one is being directly asked to support / contribute.  The project is self-funded and there are ongoing costs just to offer the software (URLs, ReadTheDocs, etc). If you're a corporate user and find that PySimpleGUI is helping you financially, that's awesome.  If you want to help ensure PySimpleGUI has a future, you now have that option to help.  It's likely that at some point the costs will become too high for the project to continue to be free, but until then we'll all enjoy the successes we're having.
