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



## 4.34.0 PySimpleGUI 18-Jan-2021

Fix popup_scrolled, big swap of PEP8 names from alias to def statements

* Quick "Emergency" release since popup_scrolled crashes. BAD bad thing that has to be corrected ASAP
* Changed all of the functions and methods so that the definition is PEP8 compliant and and alias is not compliant
* Built-in SDK help
	* Added a "Summary mode"
	* Make window smaller to fit on more monitors
	* Added aliases to end of help for each element
* metadata
	* Changed into a class Property so that it shows up in the docs correctly
	* The Element, Window and SystemTray classes all got this same change
* Added all elements to the docstring for window[key] style lookups to make PyCharm happier
* Moved all PEP8 function aliases to a centralized spot at the end of the code
* sdk_help alias of main_sdk_help
* Several new demos including a demo browser



## 4.35.0 PySimpleGUI 3-Mar-2021

Emojis, Global settings, Exec APIs

* Emojis!  Help has arrived!
	* Official PySimpleGUI emojis now usable for your applications
	* Used in the error messages
	* Has the PSG super-hero logo on his/her chest
	* Number 1 PySimpleGUI Goal remains the same.... FUN!
	* EMOJI_BASE64_LIST is the list of all emojis. These are formed from the EMOJI_BASE64_SAD_LIST and EMOJI_BASE64_HAPPY_LIST
* "Take me to error"
	* It's been close to 2 years in the making, but finally it's here.
	* Suppress error popups are
* Mac loses Modal windows setting
	* Another Mac feature turned off. The modal setting is now ignored for the Mac. Will turn back on if fixed in tkinter.
* Built-in SDK Help
	* Expanded to include init and update parms summary
	* Function search capability
	* Mode to filter out non-PEP8 compliant functions
	* Function search
	* Link to external live documentation at bottom
	* Sorted list now
	* Summary checkbox immediately updates window when changed
* Global Settings & Global Settings Window
	* Can set defaults that all programs using PySimpleGUI package will use
	* sg.main() has a button "Global Settings"
		* Directly access the settings window by calling sg.main_global_pysimplegui_settings()
	* Main settings include:
		* Default theme
		* Editor to use
		* Specification of how to launch your editor to editor a specific file at a specific line #
		* Python interpreter to use when calling `execute_py_file()`
	* Theme (see themes section too)
* User Settings
	* Option added to set the default user settings path
		* user_settings_path: default path for user_settings API calls. Expanded with os.path.expanduser so can contain ~ to represent user
		* pysimplegui_settings_path: default path for the global PySimpleGUI user_settings
		* pysimplegui_settings_filename: default filename for the global PySimpleGUI user_settings
	* The initial values can be found with constants:  DEFAULT_USER_SETTINGS_
* Buttons
	* Button color string more robust, less crashes due to bad user formatting
	* If a single color specified, then only the button background will be set/modified
	* "Disabled means ignore"
		* The parameter "disabled" is a tertiary now instead of bool
		* disabled True/False still works as it always has
		* If disabled parameter is set to the value BUTTON_DISABLED_MEANS_IGNORE, then the button will stop returning events
		* Enables you to create your own disabled button colors / behavior. Especially important with buttons with images
		* There is a new toggle button demo that shows how to use this feature
	* TRANSPARENT_BUTTON is being updated now when the theme changes. It's not recommended for use, but just in case, it's being updated.
	* files_delimiter parameter added to BrowseFiles
* Themes
	* Spaces can now be used in the theme names
	* themes_global() - Gets and sets the theme globally
		* Easy and dangerous all in 1 call
		* Can also change this setting using the global settings window via sg.main() or main_global_pysimplegui_settings()
	* Swatch previewer copies colors onto clipboard correctly now
* Exec APIs - A new set of APIs for executing subprocesses
	* execute_command_subprocess
	* execute_py_file
	* execute_editor
	* execute_file_explorer
	* execute_get_results
* Debug button color fixed		
* popup_get_file
	* fixed files_delimiter not being passed correctly to button
	* files_delimiter parameter added
* Column - auto expands entire ROW if y-expand is set to True	
* popups
	* fixed problem when using custom buttons
* Print - easy_print or Debug Print
	* Addition of color / c parameter
	* erase_all parameter added
	* 100% use of Multiline element. Output Element no longer used for Print
	* Auto refreshes the multiline
	* Window.close needed a tkroot.update() added in order to close these windows
* Graph
	* Update coordinate	when user bound event happens
	* Update coordinate when right click menu item elected
* Checkbox
	* Box color parameter added. Normally computed. Now directly accessable to users
* Radio buttons
	* Circle color parameter added. Like Checkbox, this is a computed value but is now accessable
* Slider
	* Trough color is now settable on a per-element basis
* Input
	* update method now includes ability to change the password character
* Listbox
	* update values converts items to list
* OptionMenu
	* Does not set a default if none was specified
	* Use correct font and colors for the list
	* Added size parm to update
* Combo
	* Ausizes 1 additional character wide to account for arrow
	* fixed update bug when default was previously specified
	* Added size parm to update
 * Element.set_cursor
	* now has a color parameter to set the color of the BEAM for input and other elements like them


## 4.36.0 PySimpleGUI 14-Mar-2021

Happy Pi Day!  
Exec APIs 1.1, some others fixes too

* Exec APIs
    * Fixed the Popen problems found in 3.8+
	* Add quotes on all platforms now, not just Windows
* Added checks for COLOR_SYSTEM_DEFAULT to a number of the element .update mehtods
* Changed GreenTan theme to use black
* Fix for button update when cubsample used
* Changed image update anumiation to start & stop at correct frame
* Added return values for popup_animated
* Themes - gray or grey can be used to select the gray themes. Spelling doesn't matter now
* New scrollbar parm for Multiline Element - will use a Text Widget now if scrollbar is False
* New Text element class methods for measuring size of characters
* Debugger theme changed and red button removed


## 4.37.0 PySimpleGUI 15-Mar-2021

Happy "Pi with significant rounding error day"!
I'll eventually figure out this subprocess thing... honest...

* Exec APIs
	* More control needed over routing of STDOUT
	* Additional parm added pipe_output to execute_command_subprocess
	* execute_get_results has a timeout parm now
	* execute_subprocess_still_running added to check if a subprocess is still running
* Exposed the "running" functions so they can be used by Demos
	* Used internally to see if running on Windows, Linux, Mac, Trinket
	* Makes it one less import and the code already existed.  All that needed to happen is the _ removed from the front of function name
	

	
## 4.38.0 PySimpleGUI 21-Mar-2021

The "so much for no new releases for a while" release

* Changed name of the NEW parm in Multiline element from scrollbar to no_scrollbar
	* This matches the other elements that also have this same parameter (Listbox)
	* Wanted to get this release posted prior to users writing code that uses it (it's only been 1 week)
	* This is the actual purpose for the release... so that it doesn't linger to the point it breaks being backwards compatible
* Some additional debugger stuff... nothing to see here... keep moving.... will let you know when there's more
* Added icon parameter to popup_scrolled
* New Exec API call - execute_find_callers_filename
	* It basically looks backwards until PySimpleGUI isn't found
	* Hopefully will help in error messages to determine who is calling PySimpleGUI
* Made a constant variable for the & char used by Menus in PySimpleGUI for shortcuts
	* Also fixed a couple of places where they were being erroneously stripped from the normal menu text
* Better error reporting for duplicatea keys
	* Found a problem with using print for errors - rerouted stdout/stderr can cause MORE errors
	* Interestingly, popups work great for these errors as they do not have a cascading error effect


## 4.39.0 PySimpleGUI 11-Apr-2021

Window.write_event_value is solid release!
The s parm debut (alias for size... works like k does for key)
GitHub Issues GUI

* write_event_value fixed(THANK YOU daemon2021!)
* GitHub issue GUI added - access via sg.main() or sg.main_open_github_issue()
* s parm added to all elements
* Element.block_focus - blocks an element from getting focus when using keyboard
* Listbox 
	* Set the selected colors to be opposite of normal text/background colors
	* Added highlight parms to Listbox so that they can be directly set
	* The expand method now works for Listbox element
* Button on Mac can be tk Buttons
	* In the past the Mac could only use ttk buttons
	* Now setting use_ttk=False will cause the tk buttons to be used
* Right Click Menu
	* Window get new parameter right_click_menu_tearoff to enable tearoff feature for right click menus
	* Buttons and ButtonMenus can now use right click menus. Will automatically use the Window's right click menu
	* New constants
		* MENU_RIGHT_CLICK_EDITME_EXIT = ['_', ['Edit Me', 'Exit']] - a common menu for simple programs
		* MENU_RIGHT_CLICK_DISABLED = [[]]   to block an element from getting a window's right click menu
	* parameter right_click_entry_selected_colors added to Window - a simple dual color string or a tuple - used for right click menus and pop_menu
* Error windows - better line wrapping
* Show an error window if a bad Image specified in the Image element
* expand_x & expand_y parms for vtop vbottom vcenter, 
* Added framework_version
* RealtimeButton works again!
* New popup - popup_menu will show a torn off right click menu at the indicated location
* new comment figlets
* More permissive layouts - embedded layouts for PSG+ features
* Added more symbols for buttons - double L/R & arrowheads, 
* Moved theme tests into a tab" in sg.main


## 4.40.0 PySimpleGUI 25-Apr-2021

The "A4 Release" (440 Hz)
Buttons get a boost
Fix for Graph Dragging caused by last release
Gray Gray Gray should you wish to go colorless

* Right-click Menu constant - MENU_RIGHT_CLICK_EXIT - Has only "Exit"
    * Constant = ['', ['Exit']]
* Checkbox.get() now returns a bool instead of int
* Button colors
    * mouseover_colors - new parm to Button. Sets the color when mouse moves over the button
	    * When a TK Button this is Only visible on Linux systems when mouse is over button
		* On Windows, these colors appear when the button is clicked
		* Default is to swap the button's normal colors (text = background, background = text)
	* Close Window Only button type changed to work on all windows, not just non-blocking ones
	* ColorChooserButton - target now matches other choosers (target=(ThisRow, -1))
* TabGroup - new size parm that will set size in either or both directions
* Fix for TCL error when scrolling a column
* Themes
	* Fix for COLOR_SYSTEM_DEFAULT error when choosing "default1" Theme
	* New Theme - "Gray Gray Gray" - sets no colors. The window will likely be some shades of gray
	* Changed error messages to use "theme" instead of the old "change_look_and_feel"
	* 
* Debug window - problems was if set the erase_all parm and Debug window is then closed
* timer_start, timer_stop - stop now returns the milliseconds elapsed instead of printing them
* popup_menu - now uses the passed in title if provided
* GitHub Issues GUI
	* Made necessary changes to be 3.4 compatible. You can post Issues directly from your Pi running 3.4
	* Changed layout so that the window is smaller
	* New Help window uses tabs to make smaller
* Fix for extend_layout when adding to a scrollable column
* Added back functions accidently lost during a PEP8 rework
    * added back popup_annoying, popup_no_border, popup_no_frame, popup_no_wait, popup_timed, sgprint, sgprint_close



## 4.41.0 PySimpleGUI 12-May-2021

New Readme & Other PyPI info
Fixed Syntax error in Text.update

* 2 more menu definition constants (simply a shortcut way to add right click menu)
	* MENU_RIGHT_CLICK_EDITME_VER_EXIT = ['', ['Edit Me', 'Version', 'Exit']]
	* MENU_RIGHT_CLICK_EDITME_VER_SETTINGS_EXIT = ['', ['Edit Me', 'Settings', 'Version', 'Exit']]
* 3 new SYMBOL constants. Use code completion with SYMBOL_ to find some handy symbols
	* SYMBOL_CHECK = '✅'
	* SYMBOL_BALLOT_X ='☒'
	* SYMBOL_BALLOT_CHECK = '☑'
* Syntax error, and thus crash, if the check for widget was created is false
* Fix for scrollable Column (was able to scroll further than should have been possible)
* More docstrings to explain Column.contents_changed is needed when layout is extended
* Docstring addition for read_all_windows to explain which windows will be read and what's returned when a window is closed
* Titlebar docstring fix - return was misplaced.  rtype changed to Column
* Added execute_py_get_interpreter to return the current global setting
* get_versions() function added to aid in dubugging.  print(sg.get_versions())
	* Returns a human readable string with labels next to each version.
	* Python version x.x.x
	* Port (tkinter)
	* tkinter version
	* PySimpleGUI version
	* PySimpleGUI filename with full path


## 4.42.0 PySimpleGUI 23-May-2021

New Sizegrip Element
New MenubarCustom pseudo-Element
Grab Anywhere feature improved

* New Sizegrip element
	* Needed in order to resize windows that doesn't have a titlebar
	* Place as the last element on the last row of your layout
* New MenubarCustom Element
	* Needed when using a custom Titlebar
	* Provides the ability to have a window that is entirely themed
	* Without it, was not possible to have a custom Titlebar with a menubar
	* Works like the traditional Menu Element (the item chosen is returned as the event)
* Added new elements to the SDK Reference built into PySimpleGUI and in the call reference documentation online	
* Grab Anywhere
	* Finally got the appropriate elements and widgets excluded!  Yeah!
	* Now Multiline, Input, Slider, Pane, Sizegrip, active scrollbars will not move the window
	* Additionally, a new method Element.grab_anywhere_exclude() will exclude your element from being grabbed
		* Useful for Graph elements
		* Sometimes you'll have a window with graphs that you can to be able to move using Graph element
		* Other times, you are using your Graph element with drag option set. In this case, you will want to exclude it.
* Improved torn-off menu placement. Now places them at the window's location
* Combo element new bind_return_key parameter - if set, when return key is pressed and element is focused, then event will be generated. Works like the Listbox's bind_return_key
* Fix for changing the title of a Tab using 


## 4.43.0 PySimpleGUI 23-May-2021

Happy User Appreciate Day!
Multiline expand_x, expand_y parms
Window.ding() - because FUN is the #1 goal

* Added 2 new parms to Multiline Element
	* expand_x - if True, then the element will expand in the X direction
	* expand_y - if True, then the element will expand in the Y direction
	* replaces the need to perform:   window['-MULTILINE KEY-'].expand(True, True, True)
	* Defaults to FALSE to be backward compatible
* popup_scrolled
	* changed to be resizable by default and expands the multline too
	* if no_titlebar is set, then a Sizegrip will be added, unless no_sizerip parm = True
* easy_print(sg.Print)
	* changed to be resizable by default and exands the multiline too
	* if no_titlebar is set, then a Sizegrip will be added
* Window.ding() added - get your user's attention when errors happen or just for FUN
* Added Element.grab_anywhere_include - includes an element in grab_anywhere in case you have something like a Multiline element that you can to move the window using that element


## 4.44.0 PySimpleGUI 13-Jun-2021

popup with history
clipboard functions
fonts for printing

* Added clipboard_set and clipboard_get functions
	* Known tkinter problem requires application to remain running until pasted. Found a workaround for Windows.
* History feature added to popup_get_file and popup_get_folder
	* Set parameter history=True
	* Your users will love it! (promise)
* font parameter added for Multiline-type of outputs so font can be changed on a per char basis. Added to:
	* Multiline.print
	* cprint
	* Debug print - Print, easy_print
* Listbox visibility fix
* Tree, Table expansion fixed
* Combo size not changed unless the size parameter changes in the update call
* Canvas removed from return values
* Versions string returned from get_versions() is clearer
* cwd automatically set for folder of application being launched when execute_py_file is called with cwd=None
* Fix for Mac for popup_get_file
* Better button error handling when bad Unicode chars are used or bad colors provided
* Open GitHub Issue GUI improved. Added collapse button for top section
* See-through mode in test harness changed to be a toggle
* Several error messages changed to error popups with traceback
* Combo added to list of elements that initially get focus when default focus is used
* Sizegrip autoexpands row so that it anchors correctly to right hand side
* MENU_SEPARATOR_LINE constant
* Button highlightthickness set to 0 if padding on the button is 0 in either x or y
* `__version__` fix for pip installed versions
* Release dedicated to Lester Moore


## 4.45.0 PySimpleGUI 21-Jun-2021

Happy 1M installs and 3 year anniversary edition!

* Fix for no titlebar windows on Raspberry Pi
	* This appears to have fixed a problem on REPL.It
	* And also on the Mac!
	* Setting twice now - not sure if will cause a side effect
* Docstring updates for more clarity on Window.current_location
* Menu Element (recorded the Udemy lesson which generally results in finding some problems)
	* fix for update modifying the caller's data!
	* fix for color settings incorrectly in update
	* fixed docstring
	* fixed menu tearoff location after update
* Better string length handling in the error popups
* NEW popup - popup_error_with_traceback
	* Provides the same error window as used internally with PySimpleGUI
* Changed Output element's docstring to explain Multiline is now recommended instead
* Fix for combo and input element readonly state not being recalled when updating disabled value
* Moved *args to end in one_line_progress_meter


## 4.46.0 PySimpleGUI 10-Aug-2021

McRelease - Lots of Mac changes including new Mac patch control panel in global settings

expand_x, expand_y in the constructors

docstrings reformatted

Text Elements really autosize now

* Multiline.print & cprint 
	* Added autoscroll parameter - defaults to True (backward compatible)
	* will now take a single color and use as text color
* Text element - autosize with size of None, None creates an expanding Label widget with size and width of None and wraplen=0 (truely autosizing it appears!),
* ButtonMenu 
	* use font for button as menu font if none is supplied
	* fixed mutible problem - makes a copy of menu definition when making ButtonMenu
	* made menu definition optional so can change only some other settings
* Mac
	* New window added to control the patches and feature disables. Access by calling main_mac_feature_control or through the global settings window from main()
	* Disables grab anywhere if a titlebar is present
	* Right click menu bound to Button2 which is the right button on a Mac (Button3 for all other systems)
	* FINALLY found the no-titlebar problem - weird tkinter bug. Can't set alpha channel while making window if no titlebar on Mac (credit to Tanay for this find!!)
	* Allowed Modal windows again
	* Will not try to apply no titlebar patch if tkinter version >= 8.6.10 regardless of user settings
	* Disable the alpha chan to zero if the no titlebar patch is set on the Mac. Will see the window move to center of screen for these windows.
	* Added no-titlebar batch to toolore neetips
- Fixed problem with titles on some Linux systems set class_ for Toplevel windows
- Menu defintion bug fix when menu shortcut char in first pos and item is disabled !&Item
- Sizegrip fixed expansion problem
- Added kill application button to error popup
- one_line_progress_meter
	- keep_on_top parameter added
	- no_button parameter added so that no cancel button is shown
- Deprication warning added to FindElement as first step of moving out of non-PEP8 world,
- Added TabGroup.add_tab to add new tab to TabGroup at runtime
- execute_py_file
	* set cwd='.' if dir not found
	* check for file exists
- Right click menu	
	- added to Radio Checkbox Tabgroup Spin Slider
	- Elements that don't have a right_click_menu parm now pick up the default from the Window
	- Added a right click menu callback to cover portions of the window that don't have an element on them
	- Changed Button binding for Mac to Button2 (the right button rather than middle on the other systems)
	- Made right click menus based on button release (MUCH better)
- docstrings
	- Reformatted all docstrings to line up the desriptions for better readability
	- Added type and rtype to docstrings that were missing any entries
	- Updated all font entires in docstrings to include list as well as string
- Added stderr to Debug print if rerouting stdout
- expand_x and expand_y now in the constructor of all elements. No longer need to call Element.expand after finalizing window if using these.
- Added Window.perform_long_operation to automatically run users functions as threads
- Fixed Text.get() was returning not the latest value when set by another element
- Set cursor color to the same as the text color for Input Combo Spin Multiline Output
- Added echo_stdout to debug print so that stdout can be captured when run as a subprocess
- Addition of autosave parameter for UserSettings
- Test harness
	- Made progress meter shorter so that the test harness fit better on smaller screens (a constant battle)
	- Compacted Test Harness significantly so it's 690x670
- Added Sizegrip to Debug Window
- New Grab Anywhere move code
- Move all windows at the same timed if using grab_anywhere (experimental) (set Window._move_all_windows = True)
- Table element set the headers to stretch if expand_x is True
- Element.set_size if Graph element then also set the member variable CanvasSize
- added exception details when making window with 0 alpha
- Check for no color setting when setting the cursor color for inputs (must test for gray gray gray theme in the future regression tests)
- Added exception details if have a problem with the wm_overriderediect
- Addition of "project information" to the issue your opportunity to share something about what you're making


## 4.47.0 PySimpleGUI 30-Aug-2021

Stretch & VStretch - A new era of element alignment!   
Upgrade from GitHub - uses pip for real now   
Image element - Simpler to use   
`size` and `pad` parms can be ints in addition to tuples    to speed up coding   

- `rstrip` parm added to `Multiline` element
- `Combo.update` fixed bug added in 4.45.0 with disabled not working correctly when calling update   
- Changed font type in all docstrings to be (str or (str, int[, str]) or None) (thank you Jason!!)  
- Added code from Jason (slightly modified) for _fixed_map  
- Fix for default element size was incorrectly using as the default for parm in Window.  
    - Needed to set it in the init code rather than using the parm to set it.  
- `Window.location` gets a new parm `more_accurate` (defaults to `False`). If `True`, uses window's geometry   
- Added `Window.keep_on_top_set` and `Window.keep_on_top_clear`. Makes window behave like was set when creating Window   
- Image Element
	- Added new constant `BLANK_BASE64` that essentially erases an Image element if assigned to it. It's 1x1 pixel and Alpha=0
	- Image element New `source` parameter as the first parm. 
		- Can be a string or a bytestring. Backwards compatible because first was filename.
		- Works for both the init and the update. No need to specify any name at all... just pass in the thing you want to change to. Greatly shortens code.
		- Ths idea is to not have to specify the parameter name. `sg.Image('filename')` and `sg.Image(base64)` both work without using any parameter names.
	- Fix for `Image.update` docstring
- Element sizes, when being created, can be an **int**.  If `size=int`, then it represents a `size=(int, 1)`. GREATLY shortens layouts.
	- Sometimes this these things only become apparent later even though it seems obvious
- padding - Another tuple / int convenience change. 
	- Tired of typing `pad=(0,0)`?  Yea, me too. Now we can type `pad=0`.
	- If an int is specified instead of a tuple, then a tuple will be created to be same as the int.  `pad=0` is the same as `pad=(0,0)`
- Add NEW upgrade from GitHub code.  Thank you @israel-dryer!
- Change in ttk style naming to ensure more unique style names are used
- Cast key to string when making a ttk style
- Added `"___"` between unique counter and user's key when making a unique style string for ttk widgets. Fixed problem with elements from one window interfering with another window elements
- Changed Upgrade From GitHub Code
	- When upgrading, use the interpreter from the global settings for the upgrade!  This could get tricky, but trying to make it logical
	- Output of the pip command shown in an upgrade window using a `Multiline` element so errors can be copied from it.
	- Added printing of the value of `sys.executable` to the upgrade information
- `Stretch` and `VStretch` Elements - a promising solution to element justification!
	- Redefinition of the `Stretch` element.  No longer returns an Error Element.  It now returns a Text element that does the same kind of operation as the PySimpleGUIQt's `Stretch` element!  Very nice!
    - `VStretch` stretches vertically instead of horizontally
- UserSettings APIs
	- Changed the repr method of the user settings object to use the pretty printer to format the dictionary information into a nicer string


## 4.48.0 PySimpleGUI 25-Sept-2021
- Highlights:  
	- Table clicking   
	- Push element   
	- p = pad in layouts   

* Table Element - Feature expansion
    * enable_click_events - New parameter and associated events
	* If parm is True, then events will be generated that are tuples when a user clicks on the table and headers
	* The event format is a tuple: ('-TABLE KEY-', '+CICKED+', (3, 3))  3 items in the tuple:
            1. The Table's key
            2. "An additional event name" in this case I've called it "+CLICKED+"
            3. The (row, col) 
	* The (row, col) will match the user's data unless one of these is clicked:
		* A header (will return a row of -1)
		* A row number (these are artificially generated numbers) and has a column of -1
* set_options - new keep_on_top option. Makes all windows you create, including popups, have keep_on_top set to True
* User Settings APIs
    * user_settings_object() - returns the UserSettings object that is used by the function interface for the user_settings APIs
	* Improved print by returning the pprint formattted dictionary rather than just the string version
* Docstrings
    * set_clipboard takes str or bytes
	* ProgressBar - better size parm description
	* Fixed return type for Window.read_all_windows
* ProgressBar - new size_px parameter allows you to specify your meter directly in pixels	
* pad alias!  Lazy coders and those wanting ultra-compact layouts may like this one
	* You can use the parameter p just like the parameter pad
    * pad joins the parameters size (s) and key (k)
* Push Element
    * Alias for Stretch - they are the exact same thing
	* Stretch was a term used by Qt.
	* Push "feels" more like what it does.  It "pushes" other elements around
	* Alias is P - like many other Elements, it has a 1-letter alias that can be used to write more compact code
* Removed printing of Mac warnings about global settings at the startup
* Redefined the Debug button to be a simple button with a the graphic as before
* Added a right click menu to the SDK reference so the window can be closed if moved off the screen too far

## 4.49.0 PySimpleGUI 30-Sept-2021

- Highlights    
	- popup_get_file bug fix (primary reason for a quick release)   
	- VPush   
	- popup_get_file fix   

- VPush = VP = VStretch
	- Same concept as Push element except in the Vertical direction
- `Image.update_animation_no_buffering` bug fix wasn't checking timer between frames (DOH!)
- `one_line_progress_meter` no longer returns a not OK when max reached.  Makes the user if statements much easier to get only cancel as False
	- Note that this is a backward compatibility problem is you are relying on a False being returned when the counter reaches the maximum
- `popup_get_file` fixed bug when `show_hidden` is set. Added to docstring
- Added `popup_get_file`, get_folder, get_data to the test harness under the popups tab
- Changed docstring for Multiline default value to Any and added a cast to string
- Added more tests and information to the `sg.main()` test harness


## 4.50.0 PySimpleGUI 17-Oct-2021
UserSettings API - support for .INI files  
Listbox horizontal scrollbar  
Column Element allow None for 1 size direction

* UserSettings API
	* INI File Support
		* Read access:  `settings[section][key]`  
	    Modify existing section and key:  `settings[section][key] = new_value`  
	    Create a new key in an existing section:  `settings[section][new_key] = new_value`  
	    Create a new section and key:  `settings[new_section][new_key] = new_value`    
        Delete a section: `settings.delete_section(section)`  
        Save the INI file: `settings.save()`  
		* Available for UserSettings object only, not the function interface
		* Demo Program released specific to .ini features
		* Option to convert strings to Python values for True, False, None
	* Added checks for running on Trinket or Replit so path can be set to "." if on either
* Added `running_replit` function. Returns True if environment is repl.it
* New option in set_options - `warn_button_key_duplicates` will show a warning if duplicate keys found on buttons. Defaults to OFF (duplicate key attempts on Buttons are common and OK)
* Right Click Menus
	* New Element method `Element.set_right_click_menu`
		* Enables changing a right click menu after initial window is created
		* If none specified, uses the parent's menu
* Added `Window.get_size_accurate()` to get the window's size based on the geometry string from tkinter
* Removed moving of the theme color swatch preview window and allowed to center now
* Added check for bad value returned from tkinter when table clicked event happens
* Removed print when 8.6.9 ttk treeview code is patched
* Removed a debug print accidentally left in the bind code
* Listbox - added horizontal scrollbar option
* New `pin` layout helper function implementation (hopefully better, not worse)
* Column Element - Allow `None` to be used in any part of the `size`.
	* If None used on width, then Column will default to width required by contents.  
	* If None used on height, then Column will default to width required by contents divided by 2
	* These are same values as `(None, None)` today but can invidually control now.
* Made `Window.LayoutAndRead` deprication more user friendly with a popup
* Added * to the `file_types` default so that files without an extension are shown (only a problem on non-Windows systems). Default is now `(("ALL Files", "*.* *"),)`
	* Changed `popup_get_file`, the Browse buttons, etc
	* `FILE_TYPES_ALL_FILES` is a new constant with this value
* `popup_scrolled` added 1 line per argument to fit the contents better in some cases


## 4.51.0 PySimpleGUI 18-Oct-2021
`relative_location` parameter for `Window`   

* New parameter for `Window` - `relative_location`
	* Locates the window at an **offset** from the normal location
	* Very useful for multi-window applications
	* Also works when you've set a default window location using the `set_options` call.

## 4.51.2 - 4.51.7 

A series of dot releases to make the psg commands operational for upgrading, etc.  Was a bit of a mess for a week

## 4.52.0 - A deleted release that instead fell back to 4.51.* dot releases

## 4.53.0 PySimpleGUI 24-Oct-2021

The "Mike's really excited about this release!" release  

psg commands!  
psgmain  
psgupgrade  
psghelp  
psgver  
psgsettings  
Control Click window movement  
Frame Elements with `size` parameter  

I really like this release.  It pulls together a ***lot*** of work over the past week. It fixes some things that have bothered me for a long time and adds support for some things that have bothered users for a long time.... so here we go....


* Added Commands that you can type or make shortcuts to
	* psgmain - Runs the sg.main() test harness.  Your gateway to settings, version info, etc
	* psgupgrade - Upgrades PySimpleGUI to the latest version on ***GitHub***
	* psghelp - view the SDK help window
	* psgver - view the version numbers
	* psgsettings - access the settings window (usually done via the main window)
	* Don't forget to use `sudo` if you're upgrading on Linux!
* Control Key Dragging - move ***any*** PySimpleGUI window by holding down control key while holding the left mouse button down. Ignores the usual Grab Anywhere restrictions and allows dragging over Multiline elements for example
* A new, shorter, version of the 1x1 pixel BLANK_BASE64 image
* Image Element
	* New logic for the `Image.update()` (with no parms). This will delete an image and now will also shrink down to 1 pixel
	* Set border width to 0 so that takes up even less space when empty
* Frame Element
	* Can now use the `size` parameter to create a fixed size Frame
	* `element_justification` behaves properly - consider using a `Frame` with border width=0 and no text instead of a `Column` element if you need both a hard coded size and to justify the elements inside
* `set_options`
	* Added `dpi_awareness` setting to turn on DPI Awareness (currently only on Windows)
	* Added `scaling` parameter for system-wide Window scaling
* `Window`
	* Added `scaling` parameter - will scale the contents of the window. Takes a float value
	* If need scaling for **all windows** then set using the `set_options` call
* Better 3.4 compatibility
	* Previously has issues with subprocesses
	* Upgrade to GitHub version now works
	* The new psgcommands to work too so all you 3.4, 3.5 users out there aren't left behind!
	* The PySimpleGUI Tent was built to be big and has plans on staying that way
* Exec APIs - improved ability to modify interpreter to use in other programs so that your program will then pick up the latest changes
* Testing more thoroughly 3.4, 3.6, 3.7, 3.8, 3.9, 3.10 and tkinter 8.6.2 through 8.6.10
* Doc updates to the Call Reference doc - Added `Sizer` element and reorganizing a bit.
* Special thanks to Jason for providing amazing support to the PySimpleGUI users. If you think PySimpleGUI is great... if you really want to see something impressive, try logging an issue on the GitHub and watch Jason do his thing.

## 4.54.0 PySimpleGUI 6-Nov-2021

Tabs - Are even better now  
Right click menu better for Tabs, Frame, Columns  
relative_location proliferation  

* Tab & TabGroup
	* Added image_source parameter, enabling file-based and Base64 images to be added to your tabs
	* image_subample parm added so images and be reduced in size
	* TabGroup.add_tab also got the image support
	* tab_border_width parm added to TabGroup to control the border around the tab labels
	* Added constants for Tab Location for easier code completion. All begin with TAB_LOCATION_
	* focus_color added to TabGroup
	* Significant change to right-click menus for Tabs. Now the Tab determines the right click menu shown when right clicking a tab title. Enables a right-click to close feature.
* Frame Element
	* Better right click support in blank areas
	* Added grab parameter
	* Btter grab support in blank areas
* VerticalSeperator - Improvement in expansion
* VPush and Push - background_color parameter added
* grab_any_where_on - unreported bug fixed
* relative_location - a recent parameter to Window has been added to all popups and to Print
* New Base64 images
	* Hearts (TWO types), green checkmark, red X
		* HEART_3D_BASE64
		* HEART_FLAT_BASE64
		* GREEN_CHECK_BASE64
		* RED_X_BASE64
	* Each are 90 x 90 pixels
	* Use image_subsample to reduce size to 45, 30, etc
* bar_color added to ProgressMeter.update
* visible parm added to all pre-defined buttons (FileBrowse, FolderBrowse, Ok, Cancel, etc)
* Exec APIs stderr merge with stdout
	* merge_stderr_with_stdout added to execute_command_subprocess and execute_py_file
	* Default it TRUE
	* Stderr will be merged with stdout in 1 stream
* Right click menus propagate down the container elements (Column, Frame, Tab) to the elements inside
* Window.mouse_location() - returns tuple with mouse (x,y) location
* SDK Help window now resizble
* MENU_RIGHT_CLICK_DISABLED changed to match format of normal right click menus
* psgmain and psgupgrade - changed version of Python used to relaunch to be the same as the one calling the function to invoke PySimpleGUI. Also changed the upgrade from GitHub logic to use Python interpreter for pip as used to invoke.


## 4.55.0 PySimpleGUI 7-Nov-2021

Exec APIs - Use sys.executable as default  
FIXED the install from GitHub problem with psgmain/psgupgrade!  

* Exec APIs Changes
	* If no interpreter is set in the global settings, then the interpreter running currently (sys.executable) will be used as the default rather than the system-wide default. 
	* Use python NOT pythonw (if returned from sys.executable) for all upgrades from github. The pip command was running pythonw and that caused future psgmain, psgupgrade, etc, commands to fail  


## 4.55.1 PySimpleGUI 7-Nov-2021

* Exec API Fix
	* Fix for bug created in 4.55.0 that caused the Global Setting for Python interpreter to never be used
	* The sys.executable interpreter will be used for GitHub upgrades and if no interpreter is specified in the PySimpleGUI settings



## 4.56.0 PySimpleGUI 5-Jan-2022

The "It's been a minute" & "Welcome to 2022!" release  


* Addition of stdin parm to execute_command_subprocess. This is to fix problem when pyinstaller is used to make an EXE from a psg program that calls this function
* Changed getargspec call in the SDK Reference window to getfullargspec. In 3.11 getargspec is no longer supported and thus crashes
* Added try to SDK Reference event loop to catch any additional problems that may pop up in 3.11
* Added Window.move_to_center moves a window to the center of the screen. Good for when your window changes size or you want to recenter it
* Disable debugger when installing from github
* Better error reporting when a problem with the layout detected
* Removed import of site and now get the information from os.path.dirname(sys.executable).  I like simpler!
* Combo added parameters to control the colors on the button used to display the items. Parms are button_background_color and button_arrow_color
    * Default values continue to be the same the theme's button color if nothing is set.
* Fixed missing docstring item for Table value so that the new documentation will be accurate
* (Maybe temporarily) added print to the Text element. Was an easy addition, but is limited in how colors are controlled, scrolling, etc.  May be very short-lived addition.
* New Table Element parameter right_click_selects. Default is False. If True, then will select a row using the right mouse button, but only if
    * zero or one rows are selected. If multiple rows are already selected, then the right click will not change the selection. This feature enables
    * a right-click-menu to be combined with table selection for features such as "delete row" using a right click menu.
* Fixed bug in Column element was incorrectly checking background color for None or COLOR_SYSTEM_DEFAULT 
* Changed docstring for Table.get_last_clicked_postition to indicate what's returned now. Was not useful for tkinter port until recently when cell clicks added.
* Better auto-sizing of Columns for Tables.
    * Better sizing of the row number column using the font for the header in the calculation
    * Use the column heading font to help determine if the header will be what determines the width instead of the data in the column
* Don't print the error message about wm_overrideredirect while hiding the master root if running on a Mac. 
* Fix for Tree Element not setting the row height if none is specified. Needed to set to value based on the font used.
* Tree Element
    * Always left justify the first column. This is how it's always worked. tkinter 8.6.12 changed the behavior of the first col. This changes it back
    * Better auto-size column. Uses the data as well as the Column header to determine size of column
* Table Element fix case when tables have too many headers, thus not matching the data columns
* Tree element addition of a heading for the Column 0 (the main column shown in the Tree). Default is '' which is what's shown today.
* Graph Element Experimental addition of parm motion_events If True then mouse motion over the Graph returns event of key '+MOVE' or (key, '+MOVE')
* ButtonMenu Element
    * New init parm image_source Use instead of the filename and data parms. This parm is a unified one and is how several other elements work now too.
    * New update parms image_source, image_size, image_subsample enables the initial image to be changed to a new one
* Fix in sdk_help crashed if asked for summary view of Titlebar or MenubarCustom because they're not classes            
* Fix in open github issue the python experience and overall experience values were swapped.
* UserSettings delete_entry will show popup error now with traceback like almost all PySimpleGUI errors (can be silenced)
* TTK Button wraplen fix, height padding fix? (thank you Jason for another fix!)
* Button fix for wraplen on non-TTK buttons. 
* Layout reuse error message
* Fix for set_options checking for "not None" instead of "True" for the dpi_awareness setting.  Note that once turned on, there is no option to turn off.
* Docstring changes for all Element.update methods to indicate that the change will not be visible until Window.refresh or Window.read is called
* Enabled the Text class methods that measure strings and characters to be called prior to any windows being created. Method list:
    * string_width_in_pixels, char_height_in_pixels, char_width_in_pixels
    * Replaced the error messages that were being printed with a poper error popup
* Removed destruction of hidden master root from popup_get_file and popup_get_folder



## 4.57.0 PySimpleGUI 13-Feb 2022
  
A little of this, a little of that  
New Emojis for 2022... collect them all!  


- set_options added disable_modal_windows option to provide a single call to disable the modal feature globally (including popups)
- Added OptionMenu to the list of tkinter widgets that are ignored when the grab anywhere feature is used
- Slider update the range FIRST and then the value in the update method (thank you Jason for the fix)
- Updated docstrings for all Element.update methods to indicate that the helper function "pin" need to be used to keep an element in place if visibility changes
- Replaced sponsor tab with a tab about the udemy course as well as the buy me a coffee link
- Fixed event generation for Spin element.  Also changed to use the "command" parameter to get the event. NOTE still need to handle manual entry
- New Emojis for 2022! 
- New base64 image PYTHON_COLORED_HEARTS_BASE64 (yes, more hearts... apologies to the heart-haters)
- Changed +CICKEDto +CLICKED(typo) in the table header
- Added constant TABLE_CLICKED_INDICATOR that is the value '+CLICKED+' so that it can be referenced instead of user's hard cording a string
- Added class method Text.fonts_installed_list returns list of fonts as reported by tkinter
- Horizontal scrollbar for Multiline element (long awaited).  New parameter added to control just this one scrollbar. The no_scrollbar existing parm refers to the vertical scrollbar
- Fix for font parameter only being applied to Text portion of popup_get_text. Should have been to the entire window.
- Updated the internal keys to use the -KEY- coding convention. Was using the really old _KEY_ coding convention.
- Added check for bad Image filename in Image.update. Will show an error popup now like the initial Image element creation error popup
- Addition of parameter paste (bool) to Input.update.  Inserts as if the value was pasted rather than replacing entirely
- Fix for Listbox scrollbar not behaving correctly when making element invisible / visible
- Docstring update for Window.perform_long_operation warns users that Thread are used and thus no PySimpleGUI calls are allowed. Also added description of exactly what happens when the user's function completes. 

## 4.58.0 PySimpleGUI 3-Apr-2022

A little of this and that release  
More focus on focus  
`bind` methods improved with `propagate` parm  
Visibility losing settings fix

- `execute_get_results` Added checking for timeout error to  instead of showing an error popup as it's not truly an error in this case
- `Checkbox` Added cast to bool of default parm in case user passes in an incorrect type
- `ButtonMenu.update` addition of button_text parameter. Enables changing text displayed on the ButtonMenu. Should have been an original feature.
- Open GitHub Issue GUI Tabs use 2 lines now. Added tab asking where found PSG.
- New symbols `SYMBOL_CHECKMARK_SMALL` & `SYMBOL_X_SMALL`
- `ButtonMenu.Click` - Added click PEP8 alias `ButtonMenu.click`
- Automatically add timeouts to user reads if a debugger window is opened. Debugger for multi-window applications still needs to be added
- `Window.start_thread` a simple alias for `Window.perform_long_operation`.  It's clearer what's happening with this alias.
- `bind_return_key` parm added to Spin element.  If element has focus and the return key is pressed, then an event is generated.
- Event generation for disabled elements
	- If an element is disabled, then don't generate events (fixed specifically for Input element). However, if a Browse button fills in a disabled element, then an event should still be generated
	- Don't generate events if no files / folders selected using File or Folder Browse buttons. If cancel is clicked then no longer generates an event. 
- Fix docstring for image in the Titlebar element. Incorrectly said an ICO file can be used. Must be PNG or GIF
- Windows-specific code that enables the PySimpleGUI supplied icon to be shown rather than the python.exe logo
- Removed all temporary Tk() window creation calls
	- Instead create the hidden master root. 
	- These were required for operations like getting the list of fonts from tkinter, the screensize, character width and height. This way one and only one Tk window will ever be creeated
	- The reason for the change is that the Mac crashes if multiple Tk() objects are created, even if only 1 at a time is active.
- `image_source` parm added to `Button`
	- It can be either a filename or a base64 string. 
	- This is like the Image elements parms
- Graph element doc string improvement. Describes the mouse up event.
- Improved support for focus
	- `Element.get_next_focus` added. Returns the element that should get the focus after the indicated element
	- `Element.get_previous_focus` added. Returns the element that should get the focus after the indicated element
	- Better exception error reporting for the Element focus methods.  Uses popups with tracebacks now instead of prints
- `Window.widget_to_element` returns the element that a tkinter widget is used to implement (it's a reverse lookup)
- `Element.widget` added.  It's a PEP8 compliant property  that returns `Element.Widget`
- `Element.key` added. It's a PEP8 compliant property that returns `Element.Key`
- Simplified Radio, Checkbox, Slider creation. Moved the command parm outside the creation and instead made a config call.
- Visibility fix
	- Expand and other settings were being lost when element is made invisible and visible again.
- `propagate` parameter to the bind methods.  Used to tell tkinter whether or not to propagate the event to the element / or window
- `Canvas.update` method added so that a `Canvas` can be made visible/invisible
- Removed the need for `tk.scrolledtext.ScrolledText` by adding a vertical scrollbar to a Text widget.  Getting ready for addition of ttk scrollbars!  
- `tooltip_offset` parm added to `set_options` as a way to set tooltip location (a hack to get around an 8.6.12 bug)
- `Table` and `Tree` elements new parameters
	- `border_width` -  the border width for the element
	- `header_border_width` - the width of the border for the header
	- `header_relief` - the type of header relief to use
- `Table` and `Tree` elements are now excluded from grab-anywhere so that headers can be resized without moving the window

## 4.59.0 PySimpleGUI 4-Apr-2022

An oh sh*t release due to yesterday's bug
New force modal Windows option
Test harness forces all windows to be modal and is no longer keep-on-top

- Removed ttk theme from the test harness. Forgot that I had changed it for testing.
- Fixed bug where disabled state was not correctly saved in update methods, causing events to not be generated (Thank you Jason, again!)
	- Changed numerous elements, not just the `Input` element that demonstrated the problem
- New `force_modal_windows` parm added to `set_options`
	- Forces all windows to be modal
	- Overrides the `disable_modal_windows` option
	- Used in the `main()` test harness to ensure all windows are modal so no window is accidentally lost 
- Test Harness changes
	- Set `keep_on_top=True` for all popups and windows created by test harness
	- Set the main window `keep_on_top=False`. Ensures that all windows created by it should never be hidden.  This is a somewhat experimental change.  Let's hope for the best!
	- Forced all windows except for 1 non-modal popup to be modal. This also should ensure no windows are "lost" behind the main window


## 4.60.0 PySimpleGUI 8-May-2022

TTK Scrollbars... the carpet now matches the drapes  
Debug Window improvements  
Built-in Screen-capture Initial Release  
Test Harness and Settings Windows fit on small screens better  

* Debug Window
	* Added the `wait` and `blocking` parameters (they are identical)
		* Setting to `True` will make the `Print` call wait for a user to press a `Click To Continue...` button
		* Example use - if you want to print right before exiting your program
	* Added `Pause` button
		* If clicked, the `Print` will not return until user presses `Resume`
		* Good for programs that are outputting information quickly and you want to pause execution so you can read the output
* TTK
	* TTK Theme added to the PySimpleGUI Global Settings Window
	* Theme list is retrieved from tkinter now rather than hard coded
	* TTK Scrollbars
		* All Scrollbars have been replaced with TTK Scrollbars
		* Scrollbars now match the PySimpleGUI theme colors
		* Can indicate default settings in the PySimpleGUI Global Settings Window
		* Can preview the settings in the Global Settings Window
		* Scrollbars settings are defined in this priority order:
			* The Element's creation in your layout
			* The Window's creation
			* Calling `set_options`
			* The defaults in the PySimpleGUI Global Settings
		* The TTK Theme can change the appearance of scrollbars as well
		* Impacted Elements:
			* `Multiline`
			* `Listbox`
			* `Table`
			* `Tree`
			* `Output`
 * Tree Element gets horizontal scrollbar setting
 * `sg.main()` Test Harness
 	* Restructured the `main()` Test Harness to be more compact. Now fits Pi screens better.
 	* Made not modal so can interact with the Debug Window
 	* Turned off Grab Anywhere (note you can always use Control+Drag to move any PySimpleGUI window)
 	* Freed up graph lines as they scroll off the screen for better memory management
 	* Made the upgrade from GitHub status window smaller to fit small screens better
 * Global Settings
 	* Restructured the Global Settings window to be tabbed
 	* Added ability to control Custom Titlebar. Set here and all of your applications will use this setting for the Titlebar and Menubar
 	* TTK Theme can be specified in the global settings (already mentioned above)
 	* New section for the Screenshot feature
 * Exception handling added to `bind` methods
 * Screenshots
	 * First / early release of a built-in screenshot feature
	 * Requires that PIL be installed on your system
	 * New `Window` method `save_window_screenshot_to_disk`
	 * Global Settings allows definition of a hotkey that triggers a save
	 * Popup is shown when hotkeys are used
	 * **To be clear** - PIL does not need to be installed in order to use PySimpleGUI.  ONLY when a capture is attempted does PySimpleGUI try to import PIL
	 * It's the first step of building the larger "Gallery" feature
	 * The alignment is not perfect and  the whole thing needs more work
	 * The auto-numbering freature is not yet implemented.  Only 1 file is used and is overwritten if exists
* `user_settings_delete_filename` got a new parm `report_error` (off by default).  The `UserSettings` object also got this parm to help control error reporting
* Themes (PySimpleGUI Themes)
	* `theme_global` - added error checking and reporting should non-strandard theme names be attempted with this call
	* New theme `Dark Grey 15`.  Give it a try!
	* New theme `Python Plus` - a more saturated blue and yellow colors. Give it a try!
	* New function - `theme_button_color_background` - read-only call that returns the button background color. Previously only available as a tuple using `theme_button_color`.
	* New function - `theme_button_color_text` - read-only call that returns the button text color. Previously only available as a tuple using `theme_button_color`.
	* New function - `theme_use_custom_titlebar` returns `True` if Global Settings indicate custom titlebars should will be used
* `Output` Element - implementation changed to use the Multiline Element.  No one should be impacted unless you were using some internal object details that was not published.  I still suggest using the `Multiline` element instead so that you can access much more functionality.
* Tab errors now use the popup errors with traceback
* `Column` Element
	* Fixed scrollwheel not working correctly when expand paramters used. Scrolls the canvas now not the frame.
	* New `size_subsample_width` & `size_subsample_height` parameteres
		* Gives much more control over the sizing of SCROLLABLE columns.  Previously the size was set to 1/2 the required height and the full required width. 
		* The defaults are backward compatible (size_subsample_width=1, size_subsample_height=2)
		* Setting both to 1 will make the Column fit the contents exactly. One use is when you expect your Column to grow or shrink over time.  Or maybe you didn't like the 1/2 size that PySimpleGUI has always used before.
* Made Select Colors match the theme colors
	* `Input`, `Multiline`, `Combo` elements now use matching colors for selections of characters (big-time thanks to Jason who also provided the magic code to make the combo drop-down match the theme)
* `popup_get_file` - Removed the file_types parameter use if on a Mac
	* Missed catching this problem when added the no_window option
	* Need to revisit this file types on the Mac topic in next release.
	* Particularly bad problem because cannot catch the exception.  Your code simply crashes.  And the behavior isn't the same across all Macs.
	* I'm really sorry Mac users that we keep running into these kinds of issues!
* Auto-correct file_types problems for Browse buttons.  Automatically change the formatting from (str, str) to ((str, str),) and warns the user
* Docstring typo fixes for file_types parm

## 4.60.1 PySimpleGUI 22-May-2022

* A patch-release that fixes crash if `horizontal_scrollbar=True` when making a `Listbox` element


## 4.60.2 PySimpleGUI 26-Jul-2022

* Emergency Patch Release for Mac OS 12.3 and greater
	* Adds a PySimpleGUI Mac Control Panel Controlled patch that sets the Alpha channel to 0.99 by default for these users
	* Is a workaround for a bug that was introduced into Mac OS 12.3

## 4.60.3 PySimpleGUI 27-Jul-2022

* Emergency Patch Release for Mac OS 12.3 and greater
	* Fixed bug in Mac OS version check in yesterday's 4.60.2 release

## 4.60.4 PySimpleGUI 10-Oct-2022

* Dot release to quickly fix the Trinket detection which stopped working recently


## 4.60.5 PySimpleGUI 21-May-2023

* Mac fixes
	* Fix for Input Element not working in no-titlebar windows on MacOs 13.2.1
	* Change to the 0.99 Alpha fix made in 4.60.2. Now only applies patch when running on 8.6.12, regardless of Mac Control Panel setting in PySimpleGUI Global Settings. Removes the need for users to disable when upgrading tkinter.
* Added Intelligent Upgrade Service -  inform users when there are releases of PySimpleGUI that fix a problem that may be unique to their combination of components
* Change to GitHub Issue GUI
	* Added checkbox for checking if running latest PyPI version
	* Recommended using Demo Browser to search Demo Programs
	* Use platform module to fill in the OS information field
* SDK Help Window - changed all readthedocs links to use the PySimpleGUI.org hostname for better portability




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

Written and owned by PySimpleGUI.

This documentation as well as all PySimpleGUI documentation and  code is Copyright 2018, 2019, 2020, 2021, 2022 by PySimpleGUI

Send business correspondence to PySimpleGUI@PySimpleGUI.com

## License

GNU Lesser General Public License (LGPL 3) +

Please note that this license does **not** allow you to break copyright laws.  You are licensing the software.

## Acknowledgments

There are a number of people that have been key contributors to this project both directly and indirectly.  Paid professional help has been deployed a number of critical times in the project's history.  This happens in the life of software development from time to time.

If you've helped, I sure hope that you feel like you've been properly thanked.  That you have been recognized.  If not, then say something.... drop an email to comments@PySimpleGUI.org. 
Please see the readme file for usage of other Python packages by this project.

## Support

In response to a number of email contacts from individuals and corporations that are using PySimpleGUI that wanted to financially support the project a "Support" Button was added to the GitHub site.  This support button is connected with a PayPal account.  If you wish to help support this currently freely supplied software and free technical support, then follow this link: https://www.paypal.me/pythongui.  You'll find all the ways you can help support PySimpleGUI in the readme. 

The project is self-funded and there are ongoing costs just to offer the software (URLs, ReadTheDocs, etc). If you're a corporate user and find that PySimpleGUI is helping you financially, that's awesome.  If you want to help ensure PySimpleGUI has a future, you now have that option to help.  It's likely that at some point the costs will become too high for the project to continue to be free or perhaps continue at all, but until then we'll all enjoy the successes we're having.

## Legal

All documentation in this file and in the PySimpleGUI GitHub account are copyright 2018-2022 by PySimpleGUI Tech LLC.  The PySimpleGUI code, the demo programs and other source code in the PySimpleGUI account also have are copyright owned by PySimpleGUI

The name "PySimpleGUI" and the PySimpleGUI logo are Trademarked

When in doubt, ask.