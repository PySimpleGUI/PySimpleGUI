![pysimplegui_logo](https://user-images.githubusercontent.com/13696193/43165867-fe02e3b2-8f62-11e8-9fd0-cc7c86b11772.png)  

# ELEMENT AND FUNCTION CALL REFERENCE

Here you will find the details for all Elements, Objects, and Functions that are available to you.  If you want to use a complex element and don't understand the parameters, then this is the right place to come.  For every element you're shown the parameters used to create it as well as all methods available to call.

## Currently PySimpleGUI (tkinter) only

This documentation is created using the PySimpleGUI.py file which means it's based on the tkinter code. Some of the calls are different, might not exist at all, or there may be more methods/functions for the other PySimpleGUI ports (Qt, Wx, Web).  

Work is underway to get the PySimpleGUIQt docstrings completed and corrected.

## Caution - Some functions / methods may be internal only yet exposed in this documentation

This section of the documentation is generated directly from the source code.  As a result, sometimes internal only functions or methods that you are not supposed to be calling are accidently shown in this documentation.  Hopefully these accidents don't happen often.

Here are all of the Elements, the Window & SystemTray classes, and all functions

## Button Element 

    Button Element - Defines all possible buttons. The shortcuts such as Submit, FileBrowse, ... each create a Button

```
Button(button_text = "",
    button_type = 7,
    target = (None, None),
    tooltip = None,
    file_types = (('ALL Files', '*.*'),),
    initial_folder = None,
    default_extension = "",
    disabled = False,
    change_submits = False,
    enable_events = False,
    image_filename = None,
    image_data = None,
    image_size = (None, None),
    image_subsample = None,
    border_width = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled_button_color = None,
    highlight_colors = None,
    use_ttk_buttons = None,
    font = None,
    bind_return_key = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |      button_text      | Text to be displayed on the button |
|                                   int                                    |      button_type      | You should NOT be setting this directly. ONLY the shortcut functions set this |
|                          str or Tuple[int, int]                          |        target         | key or (row,col) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button |
|                                   str                                    |        tooltip        | text, that will appear when mouse hovers over the element |
|                       Tuple[Tuple[str, str], ...]                        |      file_types       | the filetypes that will be used to match files. To indicate all files: (("ALL Files", "*.*"),). Note - NOT SUPPORTED ON MAC |
|                                   str                                    |    initial_folder     | starting path for folders and files |
|                                   str                                    |   default_extension   | If no extension entered by user, add this to filename (only used in saveas dialogs) |
|                                   bool                                   |       disabled        | If True button will be created disabled |
|                                   bool                                   |    change_submits     | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
|                                   bool                                   |     enable_events     | Turns on the element specific events. If this button is a target, should it generate an event when filled in |
|                                   str                                    |    image_filename     | image filename if there is a button image. GIFs and PNGs only. |
|                               bytes or str                               |      image_data       | Raw or Base64 representation of the image to put on button. Choose either filename or data |
|                                (int, int)                                |      image_size       | Size of the image in pixels (width, height) |
|                                   int                                    |    image_subsample    | amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
|                                   int                                    |     border_width      | width of border around button in pixels |
|                                (int, int)                                |         size          | (width, height) of the button in characters wide, rows high |
|                                   bool                                   |   auto_size_button    | if True the button size is sized to fit the text |
|                      Tuple[str, str] or str or None                      |     button_color      | Color of button. Easy to remember which is which if you say "ON" between colors. "red" on "green". Normally a tuple, but can be a simplified-button-color-string "foreground on background" |
|                             Tuple[str, str]                              | disabled_button_color | colors to use when button is disabled (text, background). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color |
|                             Tuple[str, str]                              |   highlight_colors    | colors to use when button has focus (highlight, background). None will use computed colors. Only used by Linux and only for non-TTK button |
|                                   bool                                   |    use_ttk_buttons    | True = use ttk buttons. False = do not use ttk buttons. None (Default) = use ttk buttons only if on a Mac and not with button images |
|                          str or Tuple[str, int]                          |         font          | specifies the font family, size, etc |
|                                   bool                                   |    bind_return_key    | If True the return key will cause this button to be pressed |
|                                   bool                                   |         focus         | if True, initial focus will be put on this button |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |          pad          | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                      str or int or tuple or object                       |          key          | Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
|                      str or int or tuple or object                       |           k           | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   bool                                   |        visible        | set visibility state of the element |
|                                   Any                                    |       metadata        | User metadata that can be set to ANYTHING |

### Click

Generates a click of the button as if the user clicked the button
        Calls the tkinter invoke method for the button

```python
Click()
```

### GetText

Returns the current text shown on a button

`GetText()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The text currently displayed on the button         |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Button Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(text = None,
    button_color = (None, None),
    disabled = None,
    image_data = None,
    image_filename = None,
    visible = None,
    image_subsample = None,
    disabled_button_color = (None, None),
    image_size = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|           str            |         text          | sets button text |
| Tuple[str, str] or (str) |     button_color      | of button. Easy to remember which is which if you say "ON" between colors. "red" on "green" |
|           bool           |       disabled        | disable or enable state of the element |
|       bytes or str       |      image_data       | Raw or Base64 representation of the image to put on button. Choose either filename or data |
|           str            |    image_filename     | image filename if there is a button image. GIFs and PNGs only. |
|     Tuple[str, str]      | disabled_button_color | colors to use when button is disabled (text, background). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color |
|           bool           |        visible        | control visibility of element |
|           int            |    image_subsample    | amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
|        (int, int)        |      image_size       | Size of the image in pixels (width, height) |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### click

Generates a click of the button as if the user clicked the button
        Calls the tkinter invoke method for the button

```python
click()
```

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### get_text

Returns the current text shown on a button

`get_text()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The text currently displayed on the button         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### set_vscroll_position

Attempts to set the vertical scroll postition for an element's Widget

```
set_vscroll_position(percent_from_top)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | percent_from_top | From 0 to 1.0, the percentage from the top to move scrollbar to |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Button Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(text = None,
    button_color = (None, None),
    disabled = None,
    image_data = None,
    image_filename = None,
    visible = None,
    image_subsample = None,
    disabled_button_color = (None, None),
    image_size = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|           str            |         text          | sets button text |
| Tuple[str, str] or (str) |     button_color      | of button. Easy to remember which is which if you say "ON" between colors. "red" on "green" |
|           bool           |       disabled        | disable or enable state of the element |
|       bytes or str       |      image_data       | Raw or Base64 representation of the image to put on button. Choose either filename or data |
|           str            |    image_filename     | image filename if there is a button image. GIFs and PNGs only. |
|     Tuple[str, str]      | disabled_button_color | colors to use when button is disabled (text, background). Use None for a color if don't want to change. Only ttk buttons support both text and background colors. tk buttons only support changing text color |
|           bool           |        visible        | control visibility of element |
|           int            |    image_subsample    | amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
|        (int, int)        |      image_size       | Size of the image in pixels (width, height) |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## ButtonMenu Element 

    The Button Menu Element.  Creates a button that when clicked will show a menu similar to right click menu

```
ButtonMenu(button_text,
    menu_def,
    tooltip = None,
    disabled = False,
    image_filename = None,
    image_data = None,
    image_size = (None, None),
    image_subsample = None,
    border_width = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    text_color = None,
    background_color = None,
    disabled_text_color = None,
    font = None,
    item_font = None,
    pad = None,
    key = None,
    k = None,
    tearoff = False,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |     button_text     | Text to be displayed on the button |
|                             List[List[str]]                              |      menu_def       | A list of lists of Menu items to show when this element is clicked. See docs for format as they are the same for all menu types |
|                                   str                                    |       tooltip       | text, that will appear when mouse hovers over the element |
|                                   bool                                   |      disabled       | If True button will be created disabled |
|                                   str                                    |   image_filename    | image filename if there is a button image. GIFs and PNGs only. |
|                               bytes or str                               |     image_data      | Raw or Base64 representation of the image to put on button. Choose either filename or data |
|                                (int, int)                                |     image_size      | Size of the image in pixels (width, height) |
|                                   int                                    |   image_subsample   | amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
|                                   int                                    |    border_width     | width of border around button in pixels |
|                                (int, int)                                |        size         | (width, height) of the button in characters wide, rows high |
|                                   bool                                   |  auto_size_button   | if True the button size is sized to fit the text |
|                          Tuple[str, str] or str                          |    button_color     | of button. Easy to remember which is which if you say "ON" between colors. "red" on "green" |
|                                   str                                    |  background_color   | color of the background |
|                                   str                                    |     text_color      | element's text color. Can be in #RRGGBB format or a color name "black" |
|                                   str                                    | disabled_text_color | color to use for text when item is disabled. Can be in #RRGGBB format or a color name "black" |
|                          str or Tuple[str, int]                          |        font         | specifies the font family, size, etc |
|                          str or Tuple[str, int]                          |      item_font      | specifies the font family, size, etc, for the menu items |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |         pad         | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                      str or int or tuple or object                       |         key         | Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
|                      str or int or tuple or object                       |          k          | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   bool                                   |       tearoff       | Determines if menus should allow them to be torn off |
|                                   bool                                   |       visible       | set visibility state of the element |
|                                   Any                                    |      metadata       | User metadata that can be set to ANYTHING |

### Click

Generates a click of the button as if the user clicked the button
        Calls the tkinter invoke method for the button

```python
Click()
```

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the ButtonMenu Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(menu_definition, visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List] | menu_definition | (New menu definition (in menu definition format) |
|    bool    |     visible     | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### set_vscroll_position

Attempts to set the vertical scroll postition for an element's Widget

```
set_vscroll_position(percent_from_top)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | percent_from_top | From 0 to 1.0, the percentage from the top to move scrollbar to |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the ButtonMenu Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(menu_definition, visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List] | menu_definition | (New menu definition (in menu definition format) |
|    bool    |     visible     | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Canvas Element 

```
Canvas(canvas = None,
    background_color = None,
    size = (None, None),
    pad = None,
    key = None,
    k = None,
    tooltip = None,
    right_click_menu = None,
    visible = True,
    border_width = 0,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                               (tk.Canvas)                                |      canvas      | Your own tk.Canvas if you already created it. Leave blank to create a Canvas |
|                                   str                                    | background_color | color of background |
|                              Tuple[int,int]                              |       size       | (width in char, height in rows) size in pixels to make canvas |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element |
|                      str or int or tuple or object                       |       key        | Used with window.FindElement and with return values to uniquely identify this element |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                      List[List[ List[str] or str ]]                      | right_click_menu | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |     visible      | set visibility state of the element |
|                                   int                                    |   border_width   | width of border around element in pixels. Not normally used with Canvas element |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### TKCanvas

#### property: TKCanvas

Returns the underlying tkiner Canvas widget

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | The tkinter canvas widget         |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### tk_canvas

#### property: tk_canvas

Returns the underlying tkiner Canvas widget

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The tkinter canvas widget         |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Visibility state for element         |

## Checkbox Element 

    Checkbox Element - Displays a checkbox and text next to it

```
Checkbox(text,
    default = False,
    size = (None, None),
    auto_size_text = None,
    font = None,
    background_color = None,
    text_color = None,
    change_submits = False,
    enable_events = False,
    disabled = False,
    key = None,
    k = None,
    pad = None,
    tooltip = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |       text       | Text to display next to checkbox |
|                                   bool                                   |     default      | Set to True if you want this checkbox initially checked |
|                                (int, int)                                |       size       | (width, height) width = characters-wide, height = rows-high |
|                                   bool                                   |  auto_size_text  | if True will size the element to match the length of the text |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   str                                    | background_color | color of background |
|                                   str                                    |    text_color    | color of the text |
|                                   bool                                   |  change_submits  | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
|                                   bool                                   |  enable_events   | Turns on the element specific events. Checkbox events happen when an item changes |
|                                   bool                                   |     disabled     | set disable state |
|                      str or int or tuple or object                       |       key        | Used with window.FindElement and with return values to uniquely identify this element |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                   bool                                   |     visible      | set visibility state of the element |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |

### Get

Return the current state of this checkbox

`Get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Current state of checkbox         |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Checkbox Element. Must call `Window.Read` or `Window.Finalize` prior.
Note that changing visibility may cause element to change locations when made visible after invisible

```
Update(value = None,
    text = None,
    background_color = None,
    text_color = None,
    disabled = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |      value       | if True checks the checkbox, False clears it |
| str  |       text       | Text to display next to checkbox |
| str  | background_color | color of background |
| str  |    text_color    | color of the text. Note this also changes the color of the checkmark |
| bool |     disabled     | disable or enable element |
| bool |     visible      | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get

Return the current state of this checkbox

`get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Current state of checkbox         |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Checkbox Element. Must call `Window.Read` or `Window.Finalize` prior.
Note that changing visibility may cause element to change locations when made visible after invisible

```
update(value = None,
    text = None,
    background_color = None,
    text_color = None,
    disabled = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |      value       | if True checks the checkbox, False clears it |
| str  |       text       | Text to display next to checkbox |
| str  | background_color | color of background |
| str  |    text_color    | color of the text. Note this also changes the color of the checkmark |
| bool |     disabled     | disable or enable element |
| bool |     visible      | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Visibility state for element         |

## Column Element 

    A container element that is used to create a layout within your window's layout

```
Column(layout,
    background_color = None,
    size = (None, None),
    pad = None,
    scrollable = False,
    vertical_scroll_only = False,
    right_click_menu = None,
    key = None,
    k = None,
    visible = True,
    justification = None,
    element_justification = None,
    vertical_alignment = None,
    grab = None,
    expand_x = None,
    expand_y = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                           List[List[Element]]                            |        layout         | Layout that will be shown in the Column container |
|                                   str                                    |   background_color    | color of background of entire Column |
|                                (int, int)                                |         size          | (width, height) size in pixels (doesn't work quite right, sometimes only 1 dimension is set by tkinter |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |          pad          | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   bool                                   |      scrollable       | if True then scrollbars will be added to the column |
|                                   bool                                   | vertical_scroll_only  | if Truen then no horizontal scrollbar will be shown |
|                      List[List[ List[str] or str ]]                      |   right_click_menu    | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                      str or int or tuple or object                       |          key          | Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
|                      str or int or tuple or object                       |           k           | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   bool                                   |        visible        | set visibility state of the element |
|                                   str                                    |     justification     | set justification for the Column itself. Note entire row containing the Column will be affected |
|                                   str                                    | element_justification | All elements inside the Column will have this justification 'left', 'right', 'center' are valid values |
|                                   str                                    |  vertical_alignment   | Place the column at the 'top', 'center', 'bottom' of the row (can also use t,c,r). Defaults to no setting (tkinter decides) |
|                                   bool                                   |         grab          | If True can grab this element and move the window around. Default is False |
|                                   bool                                   |       expand_x        | If True the column will automatically expand in the X direction to fill available space |
|                                   bool                                   |       expand_y        | If True the column will automatically expand in the Y direction to fill available space |
|                                   Any                                    |       metadata        | User metadata that can be set to ANYTHING |

### AddRow

Not recommended user call.  Used to add rows of Elements to the Column Element.

```
AddRow(args=*<1 or N object>)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[Element] | *args | The list of elements for this row |

### Layout

Can use like the Window.Layout method, but it's better to use the layout parameter when creating

```
Layout(rows)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Element]] | rows | The rows of Elements |
| (Column) | **RETURN** | Used for chaining

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Column Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | visible | control visibility of element |

### add_row

Not recommended user call.  Used to add rows of Elements to the Column Element.

```
add_row(args=*<1 or N object>)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[Element] | *args | The list of elements for this row |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### layout

Can use like the Window.Layout method, but it's better to use the layout parameter when creating

```
layout(rows)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Element]] | rows | The rows of Elements |
| (Column) | **RETURN** | Used for chaining

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### set_vscroll_position

Attempts to set the vertical scroll postition for an element's Widget

```
set_vscroll_position(percent_from_top)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | percent_from_top | From 0 to 1.0, the percentage from the top to move scrollbar to |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Column Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | visible | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Visibility state for element         |

## Combo Element 

    ComboBox Element - A combination of a single-line input and a drop-down menu. User can type in their own value or choose from list.

```
Combo(values,
    default_value = None,
    size = (None, None),
    auto_size_text = None,
    background_color = None,
    text_color = None,
    change_submits = False,
    enable_events = False,
    disabled = False,
    key = None,
    k = None,
    pad = None,
    tooltip = None,
    readonly = False,
    font = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                         List[Any] or Tuple[Any]                          |      values      | values to choose. While displayed as text, the items returned are what the caller supplied, not text |
|                                   Any                                    |  default_value   | Choice to be displayed as initial value. Must match one of values variable contents |
|                        (int, int) (width, height)                        |       size       | width = characters-wide, height = rows-high |
|                                   bool                                   |  auto_size_text  | True if element should be the same size as the contents |
|                                   str                                    | background_color | color of background |
|                                   str                                    |    text_color    | color of the text |
|                                   bool                                   |  change_submits  | DEPRICATED DO NOT USE. Use `enable_events` instead |
|                                   bool                                   |  enable_events   | Turns on the element specific events. Combo event is when a choice is made |
|                                   bool                                   |     disabled     | set disable state for element |
|                      str or int or tuple or object                       |       key        | Used with window.FindElement and with return values to uniquely identify this element |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   str                                    |     tooltip      | text that will appear when mouse hovers over this element |
|                                   bool                                   |     readonly     | make element readonly (user can't change). True means user cannot change |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   |     visible      | set visibility state of the element |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |

### Get

Returns the current (right now) value of the Combo.  DO NOT USE THIS AS THE NORMAL WAY OF READING A COMBO!
You should be using values from your call to window.Read instead.  Know what you're doing if you use it.

`Get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Returns the value of what is currently chosen         |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Combo Element. Must call `Window.Read` or `Window.Finalize` prior.
Note that the state can be in 3 states only.... enabled, disabled, readonly even
though more combinations are available. The easy way to remember is that if you
change the readonly parameter then you are enabling the element.

```
Update(value = None,
    values = None,
    set_to_index = None,
    disabled = None,
    readonly = None,
    font = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any          |    value     | change which value is current selected based on new list of previous list of choices |
|       List[Any]       |    values    | change list of choices |
|          int          | set_to_index | change selection to a particular choice starting with index = 0 |
|         bool          |   disabled   | disable or enable state of the element |
|         bool          |   readonly   | if True make element readonly (user cannot change any choices). Enables the element if either choice are made. |
| str or Tuple[str, int] |     font     | specifies the font family, size, etc |
|         bool          |   visible    | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get

Returns the current (right now) value of the Combo.  DO NOT USE THIS AS THE NORMAL WAY OF READING A COMBO!
You should be using values from your call to window.Read instead.  Know what you're doing if you use it.

`get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Returns the value of what is currently chosen         |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Combo Element. Must call `Window.Read` or `Window.Finalize` prior.
Note that the state can be in 3 states only.... enabled, disabled, readonly even
though more combinations are available. The easy way to remember is that if you
change the readonly parameter then you are enabling the element.

```
update(value = None,
    values = None,
    set_to_index = None,
    disabled = None,
    readonly = None,
    font = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any          |    value     | change which value is current selected based on new list of previous list of choices |
|       List[Any]       |    values    | change list of choices |
|          int          | set_to_index | change selection to a particular choice starting with index = 0 |
|         bool          |   disabled   | disable or enable state of the element |
|         bool          |   readonly   | if True make element readonly (user cannot change any choices). Enables the element if either choice are made. |
| str or Tuple[str, int] |     font     | specifies the font family, size, etc |
|         bool          |   visible    | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Visibility state for element         |

## Frame Element 

    A Frame Element that contains other Elements. Encloses with a line around elements and a text label.

```
Frame(title,
    layout,
    title_color = None,
    background_color = None,
    title_location = None,
    relief = "groove",
    size = (None, None),
    font = None,
    pad = None,
    border_width = None,
    key = None,
    k = None,
    tooltip = None,
    right_click_menu = None,
    visible = True,
    element_justification = "left",
    vertical_alignment = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |         title         | text that is displayed as the Frame's "label" or title |
|                           List[List[Elements]]                           |        layout         | The layout to put inside the Frame |
|                                   str                                    |      title_color      | color of the title text |
|                                   str                                    |   background_color    | background color of the Frame |
|                                   enum                                   |    title_location     | location to place the text title. Choices include: TITLE_LOCATION_TOP TITLE_LOCATION_BOTTOM TITLE_LOCATION_LEFT TITLE_LOCATION_RIGHT TITLE_LOCATION_TOP_LEFT TITLE_LOCATION_TOP_RIGHT TITLE_LOCATION_BOTTOM_LEFT TITLE_LOCATION_BOTTOM_RIGHT |
|                                   enum                                   |        relief         | relief style. Values are same as other elements with reliefs. Choices include RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID |
|                                (int, int)                                |         size          | (width, height) (note this parameter may not always work) |
|                          str or Tuple[str, int]                          |         font          | specifies the font family, size, etc |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |          pad          | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   int                                    |     border_width      | width of border around element in pixels |
|                      str or int or tuple or object                       |          key          | Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
|                      str or int or tuple or object                       |           k           | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   str                                    |        tooltip        | text, that will appear when mouse hovers over the element |
|                      List[List[ List[str] or str ]]                      |   right_click_menu    | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |        visible        | set visibility state of the element |
|                                   str                                    | element_justification | All elements inside the Frame will have this justification 'left', 'right', 'center' are valid values |
|                                   str                                    |  vertical_alignment   | Place the column at the 'top', 'center', 'bottom' of the row (can also use t,c,r). Defaults to no setting (tkinter decides) |
|                                   Any                                    |       metadata        | User metadata that can be set to ANYTHING |

### AddRow

Not recommended user call.  Used to add rows of Elements to the Frame Element.

```
AddRow(args=*<1 or N object>)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[Element] | *args | The list of elements for this row |

### Layout

Can use like the Window.Layout method, but it's better to use the layout parameter when creating

```
Layout(rows)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Element]] | rows | The rows of Elements |
| (Frame) | **RETURN** | Used for chaining

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Frame Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(value = None, visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any  |  value  | New text value to show on frame |
| bool | visible | control visibility of element |

### add_row

Not recommended user call.  Used to add rows of Elements to the Frame Element.

```
add_row(args=*<1 or N object>)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[Element] | *args | The list of elements for this row |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### layout

Can use like the Window.Layout method, but it's better to use the layout parameter when creating

```
layout(rows)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Element]] | rows | The rows of Elements |
| (Frame) | **RETURN** | Used for chaining

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Frame Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(value = None, visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any  |  value  | New text value to show on frame |
| bool | visible | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Visibility state for element         |

## Graph Element 

    Creates an area for you to draw on.  The MAGICAL property this Element has is that you interact
    with the element using your own coordinate system.  This is an important point!!  YOU define where the location
    is for (0,0).  Want (0,0) to be in the middle of the graph like a math 4-quadrant graph?  No problem!  Set your
    lower left corner to be (-100,-100) and your upper right to be (100,100) and you've got yourself a graph with
    (0,0) at the center.
    One of THE coolest of the Elements.
    You can also use float values. To do so, be sure and set the float_values parameter.
    Mouse click and drag events are possible and return the (x,y) coordinates of the mouse
    Drawing primitives return an "id" that is referenced when you want to operation on that item (e.g. to erase it)

```
Graph(canvas_size,
    graph_bottom_left,
    graph_top_right,
    background_color = None,
    pad = None,
    change_submits = False,
    drag_submits = False,
    enable_events = False,
    key = None,
    k = None,
    tooltip = None,
    right_click_menu = None,
    visible = True,
    float_values = False,
    border_width = 0,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                             Tuple[int, int]                              |    canvas_size    | size of the canvas area in pixels |
|                             Tuple[int, int]                              | graph_bottom_left | (x,y) The bottoms left corner of your coordinate system |
|                             Tuple[int, int]                              |  graph_top_right  | (x,y) The top right corner of your coordinate system |
|                                   str                                    | background_color  | background color of the drawing area |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |        pad        | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   bool                                   |  change_submits   | * DEPRICATED DO NOT USE. Use `enable_events` instead |
|                                   bool                                   |   drag_submits    | if True and Events are enabled for the Graph, will report Events any time the mouse moves while button down |
|                                   bool                                   |   enable_events   | If True then clicks on the Graph are immediately reported as an event. Use this instead of change_submits |
|                      str or int or tuple or object                       |        key        | Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
|                      str or int or tuple or object                       |         k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   str                                    |      tooltip      | text, that will appear when mouse hovers over the element |
|                      List[List[ List[str] or str ]]                      | right_click_menu  | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |      visible      | set visibility state of the element (Default = True) |
|                                   bool                                   |   float_values    | If True x,y coordinates are returned as floats, not ints |
|                                   int                                    |   border_width    | width of border around element in pixels. Not normally used for Graph Elements |
|                                   Any                                    |     metadata      | User metadata that can be set to ANYTHING |

### BringFigureToFront

Changes Z-order of figures on the Graph.  Brings the indicated figure to the front of all other drawn figures

```
BringFigureToFront(figure)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int | figure | value returned by tkinter when creating the figure / drawing |

### DeleteFigure

Remove from the Graph the figure represented by id. The id is given to you anytime you call a drawing primitive

```
DeleteFigure(id)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int | id | the id returned to you when calling one of the drawing methods |

### DrawArc

Draws different types of arcs.  Uses a "bounding box" to define location

```
DrawArc(top_left,
    bottom_right,
    extent,
    start_angle,
    style = None,
    arc_color = "black",
    line_width = 1,
    fill_color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] |   top_left   | the top left point of bounding rectangle |
| Tuple[int, int] or Tuple[float, float] | bottom_right | the bottom right point of bounding rectangle |
|                 float                 |    extent    | Andle to end drawing. Used in conjunction with start_angle |
|                 float                 | start_angle  | Angle to begin drawing. Used in conjunction with extent |
|                  str                  |    style     | Valid choices are One of these Style strings- 'pieslice', 'chord', 'arc', 'first', 'last', 'butt', 'projecting', 'round', 'bevel', 'miter' |
|                  str                  |  arc_color   | color to draw arc with |
|                  str                  |  fill_color  | color to fill the area |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the arc

### DrawCircle

Draws a circle, cenetered at the location provided.  Can set the fill and outline colors

```
DrawCircle(center_location,
    radius,
    fill_color = None,
    line_color = "black",
    line_width = 1)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] | center_location | Center location using USER'S coordinate system |
|             int or float              |     radius      | Radius in user's coordinate values. |
|                  str                  |   fill_color    | color of the point to draw |
|                  str                  |   line_color    | color of the outer line that goes around the circle (sorry, can't set thickness) |
|                  int                  |   line_width    | width of the line around the circle, the outline, in pixels |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the circle

### DrawImage

Places an image onto your canvas.  It's a really important method for this element as it enables so much

```
DrawImage(filename = None,
    data = None,
    location = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                  str                  | filename | if image is in a file, path and filename for the image. (GIF and PNG only!) |
|             str or bytes              |   data   | if image is in Base64 format or raw? format then use instead of filename |
| Tuple[int, int] or Tuple[float, float] | location | the (x,y) location to place image's top left corner |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the image

### DrawLine

Draws a line from one point to another point using USER'S coordinates. Can set the color and width of line

```
DrawLine(point_from,
    point_to,
    color = "black",
    width = 1)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] | point_from | Starting point for line |
| Tuple[int, int] or Tuple[float, float] |  point_to  | Ending point for line |
|                  str                  |   color    | Color of the line |
|                  int                  |   width    | width of line in pixels |
| int or None | **RETURN** | id returned from tktiner or None if user closed the window. id is used when you

### DrawOval

Draws an oval based on coordinates in user coordinate system. Provide the location of a "bounding rectangle"

```
DrawOval(top_left,
    bottom_right,
    fill_color = None,
    line_color = None,
    line_width = 1)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] |   top_left   | the top left point of bounding rectangle |
| Tuple[int, int] or Tuple[float, float] | bottom_right | the bottom right point of bounding rectangle |
|                  str                  |  fill_color  | color of the interrior |
|                  str                  |  line_color  | color of outline of oval |
|                  int                  |  line_width  | width of the line around the oval, the outline, in pixels |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the oval

### DrawPoint

Draws a "dot" at the point you specify using the USER'S coordinate system

```
DrawPoint(point,
    size = 2,
    color = "black")
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] | point | Center location using USER'S coordinate system |
|             int or float              | size  | Radius? (Or is it the diameter?) in user's coordinate values. |
|                  str                  | color | color of the point to draw |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the point

### DrawPolygon

Draw a polygon given list of points

```
DrawPolygon(points,
    fill_color = None,
    line_color = None,
    line_width = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[Tuple[int, int] or Tuple[float, float]] |   points   | list of points that define the polygon |
|                     str                     | fill_color | color of the interior |
|                     str                     | line_color | color of outline |
|                     int                     | line_width | width of the line in pixels |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the rectangle

### DrawRectangle

Draw a rectangle given 2 points. Can control the line and fill colors

```
DrawRectangle(top_left,
    bottom_right,
    fill_color = None,
    line_color = None,
    line_width = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] |   top_left   | the top left point of rectangle |
| Tuple[int, int] or Tuple[float, float] | bottom_right | the bottom right point of rectangle |
|                  str                  |  fill_color  | color of the interior |
|                  str                  |  line_color  | color of outline |
|                  int                  |  line_width  | width of the line in pixels |
| int or None | **RETURN** | int | None id returned from tkinter that you'll need if you want to manipulate the rectangle

### DrawText

Draw some text on your graph.  This is how you label graph number lines for example

```
DrawText(text,
    location,
    color = "black",
    font = None,
    angle = 0,
    text_location = "center")
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                  str                  |     text      | text to display |
| Tuple[int, int] or Tuple[float, float] |   location    | location to place first letter |
|                  str                  |     color     | text color |
|        str or Tuple[str, int]         |     font      | specifies the font family, size, etc |
|                 float                 |     angle     | Angle 0 to 360 to draw the text. Zero represents horizontal text |
|                 enum                  | text_location | "anchor" location for the text. Values start with TEXT_LOCATION_ |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the text

### Erase

Erase the Graph - Removes all figures previously "drawn" using the Graph methods (e.g. DrawText)

```python
Erase()
```

### GetBoundingBox

Given a figure, returns the upper left and lower right bounding box coordinates

```
GetBoundingBox(figure)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| object | figure | a previously drawing figure |
| Tuple[int, int, int, int] or Tuple[float, float, float, float] | **RETURN** | upper left x, upper left y, lower right x, lower right y

### GetFiguresAtLocation

Returns a list of figures located at a particular x,y location within the Graph

```
GetFiguresAtLocation(location)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] | location | point to check |
| List[int] | **RETURN** | a list of previously drawn "Figures" (returned from the drawing primitives)

### Move

Moves the entire drawing area (the canvas) by some delta from the current position.  Units are indicated in your coordinate system indicated number of ticks in your coordinate system

```
Move(x_direction, y_direction)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int or float | x_direction | how far to move in the "X" direction in your coordinates |
| int or float | y_direction | how far to move in the "Y" direction in your coordinates |

### MoveFigure

Moves a previously drawn figure using a "delta" from current position

```
MoveFigure(figure,
    x_direction,
    y_direction)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|     id      |   figure    | Previously obtained figure-id. These are returned from all Draw methods |
| int or float | x_direction | delta to apply to position in the X direction |
| int or float | y_direction | delta to apply to position in the Y direction |

### RelocateFigure

Move a previously made figure to an arbitrary (x,y) location. This differs from the Move methods because it
uses absolute coordinates versus relative for Move

```
RelocateFigure(figure,
    x,
    y)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|     id      | figure | Previously obtained figure-id. These are returned from all Draw methods |
| int or float |   x    | location on X axis (in user coords) to move the upper left corner of the figure |
| int or float |   y    | location on Y axis (in user coords) to move the upper left corner of the figure |

### SendFigureToBack

Changes Z-order of figures on the Graph.  Sends the indicated figure to the back of all other drawn figures

```
SendFigureToBack(figure)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int | figure | value returned by tkinter when creating the figure / drawing |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### TKCanvas

#### property: TKCanvas

Returns the underlying tkiner Canvas widget

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The tkinter canvas widget         |

### Update

Changes some of the settings for the Graph Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(background_color = None, visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| ???  | background_color | color of background |
| bool |     visible      | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### bring_figure_to_front

Changes Z-order of figures on the Graph.  Brings the indicated figure to the front of all other drawn figures

```
bring_figure_to_front(figure)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int | figure | value returned by tkinter when creating the figure / drawing |

### change_coordinates

Changes the corrdinate system to a new one.  The same 2 points in space are used to define the coorinate
system - the bottom left and the top right values of your graph.

```
change_coordinates(graph_bottom_left, graph_top_right)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] (x,y)  | graph_bottom_left | The bottoms left corner of your coordinate system |
| Tuple[int, int]  (x,y) |  graph_top_right  | The top right corner of your coordinate system |

### delete_figure

Remove from the Graph the figure represented by id. The id is given to you anytime you call a drawing primitive

```
delete_figure(id)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int | id | the id returned to you when calling one of the drawing methods |

### draw_arc

Draws different types of arcs.  Uses a "bounding box" to define location

```
draw_arc(top_left,
    bottom_right,
    extent,
    start_angle,
    style = None,
    arc_color = "black",
    line_width = 1,
    fill_color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] |   top_left   | the top left point of bounding rectangle |
| Tuple[int, int] or Tuple[float, float] | bottom_right | the bottom right point of bounding rectangle |
|                 float                 |    extent    | Andle to end drawing. Used in conjunction with start_angle |
|                 float                 | start_angle  | Angle to begin drawing. Used in conjunction with extent |
|                  str                  |    style     | Valid choices are One of these Style strings- 'pieslice', 'chord', 'arc', 'first', 'last', 'butt', 'projecting', 'round', 'bevel', 'miter' |
|                  str                  |  arc_color   | color to draw arc with |
|                  str                  |  fill_color  | color to fill the area |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the arc

### draw_circle

Draws a circle, cenetered at the location provided.  Can set the fill and outline colors

```
draw_circle(center_location,
    radius,
    fill_color = None,
    line_color = "black",
    line_width = 1)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] | center_location | Center location using USER'S coordinate system |
|             int or float              |     radius      | Radius in user's coordinate values. |
|                  str                  |   fill_color    | color of the point to draw |
|                  str                  |   line_color    | color of the outer line that goes around the circle (sorry, can't set thickness) |
|                  int                  |   line_width    | width of the line around the circle, the outline, in pixels |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the circle

### draw_image

Places an image onto your canvas.  It's a really important method for this element as it enables so much

```
draw_image(filename = None,
    data = None,
    location = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                  str                  | filename | if image is in a file, path and filename for the image. (GIF and PNG only!) |
|             str or bytes              |   data   | if image is in Base64 format or raw? format then use instead of filename |
| Tuple[int, int] or Tuple[float, float] | location | the (x,y) location to place image's top left corner |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the image

### draw_line

Draws a line from one point to another point using USER'S coordinates. Can set the color and width of line

```
draw_line(point_from,
    point_to,
    color = "black",
    width = 1)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] | point_from | Starting point for line |
| Tuple[int, int] or Tuple[float, float] |  point_to  | Ending point for line |
|                  str                  |   color    | Color of the line |
|                  int                  |   width    | width of line in pixels |
| int or None | **RETURN** | id returned from tktiner or None if user closed the window. id is used when you

### draw_oval

Draws an oval based on coordinates in user coordinate system. Provide the location of a "bounding rectangle"

```
draw_oval(top_left,
    bottom_right,
    fill_color = None,
    line_color = None,
    line_width = 1)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] |   top_left   | the top left point of bounding rectangle |
| Tuple[int, int] or Tuple[float, float] | bottom_right | the bottom right point of bounding rectangle |
|                  str                  |  fill_color  | color of the interrior |
|                  str                  |  line_color  | color of outline of oval |
|                  int                  |  line_width  | width of the line around the oval, the outline, in pixels |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the oval

### draw_point

Draws a "dot" at the point you specify using the USER'S coordinate system

```
draw_point(point,
    size = 2,
    color = "black")
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] | point | Center location using USER'S coordinate system |
|             int or float              | size  | Radius? (Or is it the diameter?) in user's coordinate values. |
|                  str                  | color | color of the point to draw |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the point

### draw_polygon

Draw a polygon given list of points

```
draw_polygon(points,
    fill_color = None,
    line_color = None,
    line_width = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[Tuple[int, int] or Tuple[float, float]] |   points   | list of points that define the polygon |
|                     str                     | fill_color | color of the interior |
|                     str                     | line_color | color of outline |
|                     int                     | line_width | width of the line in pixels |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the rectangle

### draw_rectangle

Draw a rectangle given 2 points. Can control the line and fill colors

```
draw_rectangle(top_left,
    bottom_right,
    fill_color = None,
    line_color = None,
    line_width = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] |   top_left   | the top left point of rectangle |
| Tuple[int, int] or Tuple[float, float] | bottom_right | the bottom right point of rectangle |
|                  str                  |  fill_color  | color of the interior |
|                  str                  |  line_color  | color of outline |
|                  int                  |  line_width  | width of the line in pixels |
| int or None | **RETURN** | int | None id returned from tkinter that you'll need if you want to manipulate the rectangle

### draw_text

Draw some text on your graph.  This is how you label graph number lines for example

```
draw_text(text,
    location,
    color = "black",
    font = None,
    angle = 0,
    text_location = "center")
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                  str                  |     text      | text to display |
| Tuple[int, int] or Tuple[float, float] |   location    | location to place first letter |
|                  str                  |     color     | text color |
|        str or Tuple[str, int]         |     font      | specifies the font family, size, etc |
|                 float                 |     angle     | Angle 0 to 360 to draw the text. Zero represents horizontal text |
|                 enum                  | text_location | "anchor" location for the text. Values start with TEXT_LOCATION_ |
| int or None | **RETURN** | id returned from tkinter that you'll need if you want to manipulate the text

### erase

Erase the Graph - Removes all figures previously "drawn" using the Graph methods (e.g. DrawText)

```python
erase()
```

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_bounding_box

Given a figure, returns the upper left and lower right bounding box coordinates

```
get_bounding_box(figure)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| object | figure | a previously drawing figure |
| Tuple[int, int, int, int] or Tuple[float, float, float, float] | **RETURN** | upper left x, upper left y, lower right x, lower right y

### get_figures_at_location

Returns a list of figures located at a particular x,y location within the Graph

```
get_figures_at_location(location)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] or Tuple[float, float] | location | point to check |
| List[int] | **RETURN** | a list of previously drawn "Figures" (returned from the drawing primitives)

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### move

Moves the entire drawing area (the canvas) by some delta from the current position.  Units are indicated in your coordinate system indicated number of ticks in your coordinate system

```
move(x_direction, y_direction)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int or float | x_direction | how far to move in the "X" direction in your coordinates |
| int or float | y_direction | how far to move in the "Y" direction in your coordinates |

### move_figure

Moves a previously drawn figure using a "delta" from current position

```
move_figure(figure,
    x_direction,
    y_direction)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|     id      |   figure    | Previously obtained figure-id. These are returned from all Draw methods |
| int or float | x_direction | delta to apply to position in the X direction |
| int or float | y_direction | delta to apply to position in the Y direction |

### relocate_figure

Move a previously made figure to an arbitrary (x,y) location. This differs from the Move methods because it
uses absolute coordinates versus relative for Move

```
relocate_figure(figure,
    x,
    y)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|     id      | figure | Previously obtained figure-id. These are returned from all Draw methods |
| int or float |   x    | location on X axis (in user coords) to move the upper left corner of the figure |
| int or float |   y    | location on Y axis (in user coords) to move the upper left corner of the figure |

### send_figure_to_back

Changes Z-order of figures on the Graph.  Sends the indicated figure to the back of all other drawn figures

```
send_figure_to_back(figure)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int | figure | value returned by tkinter when creating the figure / drawing |

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### tk_canvas

#### property: tk_canvas

Returns the underlying tkiner Canvas widget

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The tkinter canvas widget         |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Graph Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(background_color = None, visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| ???  | background_color | color of background |
| bool |     visible      | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Visibility state for element         |

## HorizontalSeparator Element 

    Horizontal Separator Element draws a Horizontal line at the given location.

```
HorizontalSeparator(color = None,
    pad = None,
    key = None,
    k = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    | color | Color of the line. Defaults to theme's text color. Can be name or #RRGGBB format |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |  pad  | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                      str or int or tuple or object                       |  key  | Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
|                      str or int or tuple or object                       |   k   | Same as the Key. You can use either k or key. Which ever is set will be used. |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Image Element 

    Image Element - show an image in the window. Should be a GIF or a PNG only

```
Image(filename = None,
    data = None,
    background_color = None,
    size = (None, None),
    pad = None,
    key = None,
    k = None,
    tooltip = None,
    right_click_menu = None,
    visible = True,
    enable_events = False,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                               str or None                                |     filename     | image filename if there is a button image. GIFs and PNGs only. |
|                           bytes or str or None                           |       data       | Raw or Base64 representation of the image to put on button. Choose either filename or data |
|                                                                          | background_color | color of background |
|                                (int, int)                                |       size       | (width, height) size of image in pixels |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                      str or int or tuple or object                       |       key        | Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                      List[List[ List[str] or str ]]                      | right_click_menu | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |     visible      | set visibility state of the element |
|                                   bool                                   |  enable_events   | Turns on the element specific events. For an Image element, the event is "image clicked" |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Image Element. Must call `Window.Read` or `Window.Finalize` prior.
To clear an image that's been displayed, call with NONE of the options set.  A blank update call will
delete the previously shown image.

```
Update(filename = None,
    data = None,
    size = (None, None),
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|        str         | filename | filename to the new image to display. |
| str or tkPhotoImage |   data   | Base64 encoded string OR a tk.PhotoImage object |
|   Tuple[int,int]   |   size   | size of a image (w,h) w=characters-wide, h=rows-high |
|        bool        | visible  | control visibility of element |

### UpdateAnimation

Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next frame and will automatically advance to the next frame at the right time.
NOTE - does NOT perform a sleep call to delay

```
UpdateAnimation(source, time_between_frames = 0)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or bytes |       source        | Filename or Base64 encoded string containing Animated GIF |
|     int     | time_between_frames | Number of milliseconds to wait between showing frames |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Image Element. Must call `Window.Read` or `Window.Finalize` prior.
To clear an image that's been displayed, call with NONE of the options set.  A blank update call will
delete the previously shown image.

```
update(filename = None,
    data = None,
    size = (None, None),
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|        str         | filename | filename to the new image to display. |
| str or tkPhotoImage |   data   | Base64 encoded string OR a tk.PhotoImage object |
|   Tuple[int,int]   |   size   | size of a image (w,h) w=characters-wide, h=rows-high |
|        bool        | visible  | control visibility of element |

### update_animation

Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next frame and will automatically advance to the next frame at the right time.
NOTE - does NOT perform a sleep call to delay

```
update_animation(source, time_between_frames = 0)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or bytes |       source        | Filename or Base64 encoded string containing Animated GIF |
|     int     | time_between_frames | Number of milliseconds to wait between showing frames |

### update_animation_no_buffering

Show an Animated GIF. Call the function as often as you like. The function will determine when to show the next frame and will automatically advance to the next frame at the right time.
NOTE - does NOT perform a sleep call to delay

```
update_animation_no_buffering(source, time_between_frames = 0)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or bytes |       source        | Filename or Base64 encoded string containing Animated GIF |
|     int     | time_between_frames | Number of milliseconds to wait between showing frames |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Input Element 

    Display a single text input field.  Based on the tkinter Widget `Entry`

```
Input(default_text = "",
    size = (None, None),
    disabled = False,
    password_char = "",
    justification = None,
    background_color = None,
    text_color = None,
    font = None,
    tooltip = None,
    border_width = None,
    change_submits = False,
    enable_events = False,
    do_not_clear = True,
    key = None,
    k = None,
    focus = False,
    pad = None,
    use_readonly_for_disable = True,
    readonly = False,
    disabled_readonly_background_color = None,
    disabled_readonly_text_color = None,
    right_click_menu = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   Any                                    |            default_text            | Text initially shown in the input box as a default value(Default value = ''). Will automatically be converted to string |
|                       (int, int)  (width, height)                        |                size                | w=characters-wide, h=rows-high |
|                                   bool                                   |              disabled              | set disable state for element (Default = False) |
|                                   char                                   |           password_char            | Password character if this is a password field (Default value = '') |
|                                   str                                    |           justification            | justification for data display. Valid choices - left, right, center |
|                                   str                                    |          background_color          | color of background in one of the color formats |
|                                   str                                    |             text_color             | color of the text |
|                          str or Tuple[str, int]                          |                font                | specifies the font family, size, etc |
|                                   str                                    |              tooltip               | text, that will appear when mouse hovers over the element |
|                                   int                                    |            border_width            | width of border around element in pixels |
|                                   bool                                   |           change_submits           | * DEPRICATED DO NOT USE. Use `enable_events` instead |
|                                   bool                                   |           enable_events            | If True then changes to this element are immediately reported as an event. Use this instead of change_submits (Default = False) |
|                                   bool                                   |            do_not_clear            | If False then the field will be set to blank after ANY event (button, any event) (Default = True) |
|                      str or int or tuple or object                       |                key                 | Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
|                      str or int or tuple or object                       |                 k                  | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   bool                                   |               focus                | Determines if initial focus should go to this element. |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |                pad                 | Amount of padding to put around element. Normally (horizontal pixels, vertical pixels) but can be split apart further into ((horizontal left, horizontal right), (vertical above, vertical below)) |
|                                   bool                                   |      use_readonly_for_disable      | If True (the default) tkinter state set to 'readonly'. Otherwise state set to 'disabled' |
|                                   bool                                   |              readonly              | If True tkinter state set to 'readonly'. Use this in place of use_readonly_for_disable as another way of achieving readonly. Note cannot set BOTH readonly and disabled as tkinter only supplies a single flag |
|                                   str                                    | disabled_readonly_background_color | If state is set to readonly or disabled, the color to use for the background |
|                                   str                                    |    disabled_readonly_text_color    | If state is set to readonly or disabled, the color to use for the text |
|                      List[List[ List[str] or str ]]                      |          right_click_menu          | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |              visible               | set visibility state of the element (Default = True) |
|                                   Any                                    |              metadata              | User metadata that can be set to ANYTHING |

### Get

Read and return the current value of the input element. Must call `Window.Read` or `Window.Finalize` prior

`Get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | current value of Input field or '' if error encountered         |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Input Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(value = None,
    disabled = None,
    select = None,
    visible = None,
    text_color = None,
    background_color = None,
    move_cursor_to = "end")
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|    str    |      value       | new text to display as default text in Input field |
|   bool    |     disabled     | disable or enable state of the element (sets Entry Widget to readonly or normal) |
|   bool    |      select      | if True, then the text will be selected |
|   bool    |     visible      | change visibility of element |
|    str    |    text_color    | change color of text being typed |
|    str    | background_color | change color of the background |
| int or str |  move_cursor_to  | Moves the cursor to a particular offset. Defaults to 'end' |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get

Read and return the current value of the input element. Must call `Window.Read` or `Window.Finalize` prior

`get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | current value of Input field or '' if error encountered         |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### set_vscroll_position

Attempts to set the vertical scroll postition for an element's Widget

```
set_vscroll_position(percent_from_top)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | percent_from_top | From 0 to 1.0, the percentage from the top to move scrollbar to |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Input Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(value = None,
    disabled = None,
    select = None,
    visible = None,
    text_color = None,
    background_color = None,
    move_cursor_to = "end")
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|    str    |      value       | new text to display as default text in Input field |
|   bool    |     disabled     | disable or enable state of the element (sets Entry Widget to readonly or normal) |
|   bool    |      select      | if True, then the text will be selected |
|   bool    |     visible      | change visibility of element |
|    str    |    text_color    | change color of text being typed |
|    str    | background_color | change color of the background |
| int or str |  move_cursor_to  | Moves the cursor to a particular offset. Defaults to 'end' |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Listbox Element 

    A List Box.  Provide a list of values for the user to choose one or more of.   Returns a list of selected rows
    when a window.Read() is executed.

```
Listbox(values,
    default_values = None,
    select_mode = None,
    change_submits = False,
    enable_events = False,
    bind_return_key = False,
    size = (None, None),
    disabled = False,
    auto_size_text = None,
    font = None,
    no_scrollbar = False,
    background_color = None,
    text_color = None,
    key = None,
    k = None,
    pad = None,
    tooltip = None,
    right_click_menu = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                         List[Any] or Tuple[Any]                          |      values      | list of values to display. Can be any type including mixed types as long as they have __str__ method |
|                                List[Any]                                 |  default_values  | which values should be initially selected |
|                                  [enum]                                  |   select_mode    | Select modes are used to determine if only 1 item can be selected or multiple and how they can be selected. Valid choices begin with "LISTBOX_SELECT_MODE_" and include: LISTBOX_SELECT_MODE_SINGLE LISTBOX_SELECT_MODE_MULTIPLE LISTBOX_SELECT_MODE_BROWSE LISTBOX_SELECT_MODE_EXTENDED |
|                                   bool                                   |  change_submits  | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
|                                   bool                                   |  enable_events   | Turns on the element specific events. Listbox generates events when an item is clicked |
|                                   bool                                   | bind_return_key  | If True, then the return key will cause a the Listbox to generate an event |
|                     Tuple(int, int) (width, height)                      |       size       | width = characters-wide, height = rows-high |
|                                   bool                                   |     disabled     | set disable state for element |
|                                   bool                                   |  auto_size_text  | True if element should be the same size as the contents |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                ??? (bool)                                |       font       | specifies the font family, size, etc :param no_scrollbar: ??? |
|                                   str                                    | background_color | color of background |
|                                   str                                    |    text_color    | color of the text |
|                      str or int or tuple or object                       |       key        | Used with window.FindElement and with return values to uniquely identify this element |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                      List[List[ List[str] or str ]]                      | right_click_menu | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |     visible      | set visibility state of the element |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |

### GetIndexes

Returns the items currently selected as a list of indexes

`GetIndexes()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | A list of offsets into values that is currently selected         |

### GetListValues

Returns list of Values provided by the user in the user's format

`GetListValues()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | List of values. Can be any / mixed types -> []         |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### SetValue

Set listbox highlighted choices

```
SetValue(values)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[Any] | values | new values to choose based on previously set values |

### Update

Changes some of the settings for the Listbox Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(values = None,
    disabled = None,
    set_to_index = None,
    scroll_to_index = None,
    select_mode = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|     List[Any]      |     values      | new list of choices to be shown to user |
|        bool        |    disabled     | disable or enable state of the element |
| int or list or tuple |  set_to_index   | highlights the item(s) indicated. If parm is an int one entry will be set. If is a list, then each entry in list is highlighted |
|        int         | scroll_to_index | scroll the listbox so that this index is the first shown |
|        str         |      mode       | changes the select mode according to tkinter's listbox widget |
|        bool        |     visible     | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get

Returns the list of items currently selected in this listbox.  It should be identical
to the value you would receive when performing a window.read() call.

`get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The list of currently selected items. The actual items are returned, not the indexes         |

### get_indexes

Returns the items currently selected as a list of indexes

`get_indexes()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | A list of offsets into values that is currently selected         |

### get_list_values

Returns list of Values provided by the user in the user's format

`get_list_values()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | List of values. Can be any / mixed types -> []         |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### set_value

Set listbox highlighted choices

```
set_value(values)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[Any] | values | new values to choose based on previously set values |

### set_vscroll_position

Attempts to set the vertical scroll postition for an element's Widget

```
set_vscroll_position(percent_from_top)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | percent_from_top | From 0 to 1.0, the percentage from the top to move scrollbar to |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Listbox Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(values = None,
    disabled = None,
    set_to_index = None,
    scroll_to_index = None,
    select_mode = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|     List[Any]      |     values      | new list of choices to be shown to user |
|        bool        |    disabled     | disable or enable state of the element |
| int or list or tuple |  set_to_index   | highlights the item(s) indicated. If parm is an int one entry will be set. If is a list, then each entry in list is highlighted |
|        int         | scroll_to_index | scroll the listbox so that this index is the first shown |
|        str         |      mode       | changes the select mode according to tkinter's listbox widget |
|        bool        |     visible     | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Menu Element 

    Menu Element is the Element that provides a Menu Bar that goes across the top of the window, just below titlebar.
    Here is an example layout.  The "&" are shortcut keys ALT+key.
    Is a List of -  "Item String" + List
    Where Item String is what will be displayed on the Menubar itself.
    The List that follows the item represents the items that are shown then Menu item is clicked
    Notice how an "entry" in a mennu can be a list which means it branches out and shows another menu, etc. (resursive)
    menu_def = [['&File', ['!&Open', '&Save::savekey', '---', '&Properties', 'E&xit']],
                ['!&Edit', ['!&Paste', ['Special', 'Normal', ], 'Undo'], ],
                ['&Debugger', ['Popout', 'Launch Debugger']],
                ['&Toolbar', ['Command &1', 'Command &2', 'Command &3', 'Command &4']],
                ['&Help', '&About...'], ]
    Finally, "keys" can be added to entries so make them unique.  The "Save" entry has a key associated with it. You
    can see it has a "::" which signifies the beginning of a key.  The user will not see the key portion when the
    menu is shown.  The key portion is returned as part of the event.

```
Menu(menu_definition,
    background_color = None,
    text_color = None,
    disabled_text_color = None,
    size = (None, None),
    tearoff = False,
    font = None,
    pad = None,
    key = None,
    k = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                     List[List[Tuple[str, List[str]]]                     |   menu_definition   | The Menu definition specified using lists (docs explain the format) |
|                                   str                                    |  background_color   | color of the background |
|                                   str                                    |     text_color      | element's text color. Can be in #RRGGBB format or a color name "black" |
|                                   str                                    | disabled_text_color | color to use for text when item is disabled. Can be in #RRGGBB format or a color name "black" |
|                                (int, int)                                |        size         | Not used in the tkinter port |
|                                   bool                                   |       tearoff       | if True, then can tear the menu off from the window ans use as a floating window. Very cool effect |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |         pad         | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                          str or Tuple[str, int]                          |        font         | specifies the font family, size, etc |
|                      str or int or tuple or object                       |         key         | Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
|                      str or int or tuple or object                       |          k          | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   bool                                   |       visible       | set visibility state of the element |
|                                   Any                                    |      metadata       | User metadata that can be set to ANYTHING |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Update a menubar - can change the menu definition and visibility.  The entire menu has to be specified

```
Update(menu_definition = None, visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Tuple[str, List[str]]] | menu_definition | ??? |
|               bool               |     visible     | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Update a menubar - can change the menu definition and visibility.  The entire menu has to be specified

```
update(menu_definition = None, visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Tuple[str, List[str]]] | menu_definition | ??? |
|               bool               |     visible     | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Multiline Element 

    Multiline Element - Display and/or read multiple lines of text.  This is both an input and output element.
    Other PySimpleGUI ports have a separate MultilineInput and MultilineOutput elements.  May want to split this
    one up in the future too.

```
Multiline(default_text = "",
    enter_submits = False,
    disabled = False,
    autoscroll = False,
    border_width = None,
    size = (None, None),
    auto_size_text = None,
    background_color = None,
    text_color = None,
    change_submits = False,
    enable_events = False,
    do_not_clear = True,
    key = None,
    k = None,
    write_only = False,
    auto_refresh = False,
    reroute_stdout = False,
    reroute_stderr = False,
    reroute_cprint = False,
    echo_stdout_stderr = False,
    focus = False,
    font = None,
    pad = None,
    tooltip = None,
    justification = None,
    right_click_menu = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |    default_text    | Initial text to show |
|                                   bool                                   |   enter_submits    | if True, the Window.Read call will return is enter key is pressed in this element |
|                                   bool                                   |      disabled      | set disable state |
|                                   bool                                   |     autoscroll     | If True the contents of the element will automatically scroll as more data added to the end |
|                                   int                                    |    border_width    | width of border around element in pixels |
|                                (int, int)                                |        size        | (width, height) width = characters-wide, height = rows-high |
|                                   bool                                   |   auto_size_text   | if True will size the element to match the length of the text |
|                                   str                                    |  background_color  | color of background |
|                                   str                                    |     text_color     | color of the text |
|                                   bool                                   |   change_submits   | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
|                                   bool                                   |   enable_events    | Turns on the element specific events. Spin events happen when an item changes |
|                                   bool                                   |    do_not_clear    | if False the element will be cleared any time the Window.Read call returns |
|                      str or int or tuple or object                       |        key         | Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
|                      str or int or tuple or object                       |         k          | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   bool                                   |     write_only     | If True then no entry will be added to the values dictionary when the window is read |
|                                   bool                                   |    auto_refresh    | If True then anytime the element is updated, the window will be refreshed so that the change is immediately displayed |
|                                   bool                                   |   reroute_stdout   | If True then all output to stdout will be output to this element |
|                                   bool                                   |   reroute_stderr   | If True then all output to stderr will be output to this element |
|                                   bool                                   |   reroute_cprint   | If True your cprint calls will output to this element. It's the same as you calling cprint_set_output_destination |
|                                   bool                                   | echo_stdout_stderr | If True then output to stdout and stderr will be output to this element AND also to the normal console location |
|                                   bool                                   |       focus        | if True initial focus will go to this element |
|                          str or Tuple[str, int]                          |        font        | specifies the font family, size, etc |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |        pad         | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   str                                    |      tooltip       | text, that will appear when mouse hovers over the element |
|                                   str                                    |   justification    | text justification. left, right, center. Can use single characters l, r, c. |
|                      List[List[ List[str] or str ]]                      |  right_click_menu  | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |      visible       | set visibility state of the element |
|                                   Any                                    |      metadata      | User metadata that can be set to ANYTHING |

### Get

Return current contents of the Multiline Element

`Get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | current contents of the Multiline Element (used as an input type of Multiline         |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Multiline Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(value = None,
    disabled = None,
    append = False,
    font = None,
    text_color = None,
    background_color = None,
    text_color_for_value = None,
    background_color_for_value = None,
    visible = None,
    autoscroll = None,
    justification = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str          |           value            | new text to display |
|         bool          |          disabled          | disable or enable state of the element |
|         bool          |           append           | if True then new value will be added onto the end of the current value. if False then contents will be replaced. |
| str or Tuple[str, int] |            font            | specifies the font family, size, etc |
|          str          |         text_color         | color of the text |
|          str          |      background_color      | color of background |
|          str          |    text_color_for_value    | color of the new text being added (the value paramter) |
|          str          | background_color_for_value | color of the new background of the text being added (the value paramter) |
|         bool          |          visible           | set visibility state of the element |
|         bool          |         autoscroll         | if True then contents of element are scrolled down when new text is added to the end |
|          str          |       justification        | text justification. left, right, center. Can use single characters l, r, c. Sets only for this value, not entire element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get

Return current contents of the Multiline Element

`get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | current contents of the Multiline Element (used as an input type of Multiline         |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### print

Print like Python normally prints except route the output to a multline element and also add colors if desired

```
print(args=*<1 or N object>,
    end = None,
    sep = None,
    text_color = None,
    background_color = None,
    justification = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any |       args       | The arguments to print |
| str |       end        | The end char to use just like print uses |
| str |       sep        | The separation character like print uses |
| str |    text_color    | The color of the text |
| str | background_color | The background color of the line |
| str |  justification   | text justification. left, right, center. Can use single characters l, r, c. Sets only for this value, not entire element |

### reroute_stderr_to_here

Sends stderr to this element

```python
reroute_stderr_to_here()
```

### reroute_stdout_to_here

Sends stdout (prints) to this element

```python
reroute_stdout_to_here()
```

### restore_stderr

Restore a previously re-reouted stderr back to the original destination

```python
restore_stderr()
```

### restore_stdout

Restore a previously re-reouted stdout back to the original destination

```python
restore_stdout()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### set_vscroll_position

Attempts to set the vertical scroll postition for an element's Widget

```
set_vscroll_position(percent_from_top)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | percent_from_top | From 0 to 1.0, the percentage from the top to move scrollbar to |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Multiline Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(value = None,
    disabled = None,
    append = False,
    font = None,
    text_color = None,
    background_color = None,
    text_color_for_value = None,
    background_color_for_value = None,
    visible = None,
    autoscroll = None,
    justification = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str          |           value            | new text to display |
|         bool          |          disabled          | disable or enable state of the element |
|         bool          |           append           | if True then new value will be added onto the end of the current value. if False then contents will be replaced. |
| str or Tuple[str, int] |            font            | specifies the font family, size, etc |
|          str          |         text_color         | color of the text |
|          str          |      background_color      | color of background |
|          str          |    text_color_for_value    | color of the new text being added (the value paramter) |
|          str          | background_color_for_value | color of the new background of the text being added (the value paramter) |
|         bool          |          visible           | set visibility state of the element |
|         bool          |         autoscroll         | if True then contents of element are scrolled down when new text is added to the end |
|          str          |       justification        | text justification. left, right, center. Can use single characters l, r, c. Sets only for this value, not entire element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## OptionMenu Element 

    Option Menu is an Element available ONLY on the tkinter port of PySimpleGUI.  It's is a widget that is unique
    to tkinter.  However, it looks much like a ComboBox.  Instead of an arrow to click to pull down the list of
    choices, another little graphic is shown on the widget to indicate where you click.  After clicking to activate,
    it looks like a Combo Box that you scroll to select a choice.

```
OptionMenu(values,
    default_value = None,
    size = (None, None),
    disabled = False,
    auto_size_text = None,
    background_color = None,
    text_color = None,
    key = None,
    k = None,
    pad = None,
    tooltip = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                         List[Any] or Tuple[Any]                          |      values      | Values to be displayed |
|                                   Any                                    |  default_value   | the value to choose by default |
|                        (int, int) (width, height)                        |       size       | size in characters (wide) and rows (high) |
|                                   bool                                   |     disabled     | control enabled / disabled |
|                                   bool                                   |  auto_size_text  | True if size of Element should match the contents of the items |
|                                   str                                    | background_color | color of background |
|                                   str                                    |    text_color    | color of the text |
|                      str or int or tuple or object                       |       key        | Used with window.FindElement and with return values to uniquely identify this element |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   str                                    |     tooltip      | text that will appear when mouse hovers over this element |
|                                   bool                                   |     visible      | set visibility state of the element |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the OptionMenu Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(value = None,
    values = None,
    disabled = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|    Any    |  value   | the value to choose by default |
| List[Any] |  values  | Values to be displayed |
|   bool    | disabled | disable or enable state of the element |
|   bool    | visible  | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### set_vscroll_position

Attempts to set the vertical scroll postition for an element's Widget

```
set_vscroll_position(percent_from_top)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | percent_from_top | From 0 to 1.0, the percentage from the top to move scrollbar to |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the OptionMenu Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(value = None,
    values = None,
    disabled = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|    Any    |  value   | the value to choose by default |
| List[Any] |  values  | Values to be displayed |
|   bool    | disabled | disable or enable state of the element |
|   bool    | visible  | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Output Element 

    Output Element - a multi-lined text area where stdout and stderr are re-routed to.

```
Output(size = (None, None),
    background_color = None,
    text_color = None,
    pad = None,
    echo_stdout_stderr = False,
    font = None,
    tooltip = None,
    key = None,
    k = None,
    right_click_menu = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                (int, int)                                |        size        | (width, height) w=characters-wide, h=rows-high |
|                                   str                                    |  background_color  | color of background |
|                                   str                                    |     text_color     | color of the text |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |        pad         | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   bool                                   | echo_stdout_stderr | If True then output to stdout will be output to this element AND also to the normal console location |
|                          str or Tuple[str, int]                          |        font        | specifies the font family, size, etc |
|                                   str                                    |      tooltip       | text, that will appear when mouse hovers over the element |
|                      str or int or tuple or object                       |        key         | Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
|                      str or int or tuple or object                       |         k          | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                      List[List[ List[str] or str ]]                      |  right_click_menu  | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |      visible       | set visibility state of the element |
|                                   Any                                    |      metadata      | User metadata that can be set to ANYTHING |

### Get

Returns the current contents of the output.  Similar to Get method other Elements

`Get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | the current value of the output         |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### TKOut

#### property: TKOut

Returns the TKOutput object used to create the element

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The TKOutput object         |

### Update

Changes some of the settings for the Output Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(value = None, visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str  |  value  | string that will replace current contents of the output area |
| bool | visible | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | expand_x | If True Element will expand in the Horizontal directions |
| bool | expand_y | If True Element will expand in the Vertical directions |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### tk_out

#### property: tk_out

Returns the TKOutput object used to create the element

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The TKOutput object         |

### set_vscroll_position

Attempts to set the vertical scroll postition for an element's Widget

```
set_vscroll_position(percent_from_top)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | percent_from_top | From 0 to 1.0, the percentage from the top to move scrollbar to |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Output Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(value = None, visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str  |  value  | string that will replace current contents of the output area |
| bool | visible | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Pane Element 

    A sliding Pane that is unique to tkinter.  Uses Columns to create individual panes

```
Pane(pane_list,
    background_color = None,
    size = (None, None),
    pad = None,
    orientation = "vertical",
    show_handle = True,
    relief = "raised",
    handle_size = None,
    border_width = None,
    key = None,
    k = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                               List[Column]                               |    pane_list     | Must be a list of Column Elements. Each Column supplied becomes one pane that's shown |
|                                   str                                    | background_color | color of background |
|                                (int, int)                                |       size       | (width, height) w=characters-wide, h=rows-high How much room to reserve for the Pane |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   str                                    |   orientation    | 'horizontal' or 'vertical' or ('h' or 'v'). Direction the Pane should slide |
|                                   bool                                   |   show_handle    | if True, the handle is drawn that makes it easier to grab and slide |
|                                   enum                                   |      relief      | relief style. Values are same as other elements that use relief values. RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID |
|                                   int                                    |   handle_size    | Size of the handle in pixels |
|                                   int                                    |   border_width   | width of border around element in pixels |
|                      str or int or tuple or object                       |       key        | Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   bool                                   |     visible      | set visibility state of the element |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Pane Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | visible | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Pane Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | visible | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## ProgressBar Element 

    Progress Bar Element - Displays a colored bar that is shaded as progress of some operation is made

```
ProgressBar(max_value,
    orientation = None,
    size = (None, None),
    auto_size_text = None,
    bar_color = None,
    style = None,
    border_width = None,
    relief = None,
    key = None,
    k = None,
    pad = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   int                                    |   max_value    | max value of progressbar |
|                                   str                                    |  orientation   | 'horizontal' or 'vertical' |
|                                (int, int)                                |      size      | Size of the bar. If horizontal (chars wide, pixels high), vert (pixels wide, rows high) |
|                                   bool                                   | auto_size_text | Not sure why this is here |
|                          Tuple[str, str] or str                          |   bar_color    | The 2 colors that make up a progress bar. Easy to remember which is which if you say "ON" between colors. "red" on "green". |
|                                   str                                    |     style      | Progress bar style defined as one of these 'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative' |
|                                   int                                    |  border_width  | The amount of pixels that go around the outside of the bar |
|                                   str                                    |     relief     | relief style. Values are same as progress meter relief values. Can be a constant or a string: `RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID` (Default value = DEFAULT_PROGRESS_BAR_RELIEF) |
|                      str or int or tuple or object                       |      key       | Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
|                      str or int or tuple or object                       |       k        | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |      pad       | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   bool                                   |    visible     | set visibility state of the element |
|                                   Any                                    |    metadata    | User metadata that can be set to ANYTHING |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the ProgressBar Element. Must call `Window.Read` or `Window.Finalize` prior
Now has the ability to modify the count so that the update_bar method is not longer needed separately

```
Update(current_count,
    max = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int  | current_count | sets the current value |
| int  |      max      | changes the max value |
| bool |    visible    | control visibility of element |
| (bool) | **RETURN** | Returns True if update was OK.  False means something wrong with window or it was closed

### UpdateBar

DEPRECATED BUT STILL USABLE - has been combined with the normal ProgressBar.update method.
Change what the bar shows by changing the current count and optionally the max count

```
UpdateBar(current_count, max = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int | current_count | sets the current value |
| int |      max      | changes the max value |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the ProgressBar Element. Must call `Window.Read` or `Window.Finalize` prior
Now has the ability to modify the count so that the update_bar method is not longer needed separately

```
update(current_count,
    max = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int  | current_count | sets the current value |
| int  |      max      | changes the max value |
| bool |    visible    | control visibility of element |
| (bool) | **RETURN** | Returns True if update was OK.  False means something wrong with window or it was closed

### update_bar

DEPRECATED BUT STILL USABLE - has been combined with the normal ProgressBar.update method.
Change what the bar shows by changing the current count and optionally the max count

```
update_bar(current_count, max = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int | current_count | sets the current value |
| int |      max      | changes the max value |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Radio Element 

    Radio Button Element - Used in a group of other Radio Elements to provide user with ability to select only
    1 choice in a list of choices.

```
Radio(text,
    group_id,
    default = False,
    disabled = False,
    size = (None, None),
    auto_size_text = None,
    background_color = None,
    text_color = None,
    font = None,
    key = None,
    k = None,
    pad = None,
    tooltip = None,
    change_submits = False,
    enable_events = False,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |       text       | Text to display next to button |
|                                   Any                                    |     group_id     | Groups together multiple Radio Buttons. Any type works |
|                                   bool                                   |     default      | Set to True for the one element of the group you want initially selected |
|                                   bool                                   |     disabled     | set disable state |
|                                (int, int)                                |       size       | (width, height) width = characters-wide, height = rows-high |
|                                   bool                                   |  auto_size_text  | if True will size the element to match the length of the text |
|                                   str                                    | background_color | color of background |
|                                   str                                    |    text_color    | color of the text |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                      str or int or tuple or object                       |       key        | Used with window.FindElement and with return values to uniquely identify this element |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                   bool                                   |  change_submits  | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
|                                   bool                                   |  enable_events   | Turns on the element specific events. Radio Button events happen when an item is selected |
|                                   bool                                   |     visible      | set visibility state of the element |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |

### Get

A snapshot of the value of Radio Button -> (bool)

`Get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | True if this radio button is selected         |

### ResetGroup

Sets all Radio Buttons in the group to not selected

```python
ResetGroup()
```

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Radio Button Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(value = None,
    text = None,
    background_color = None,
    text_color = None,
    disabled = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |      value       | if True change to selected and set others in group to unselected |
| str  |       text       | Text to display next to radio button |
| str  | background_color | color of background |
| str  |    text_color    | color of the text. Note this also changes the color of the selection dot |
| bool |     disabled     | disable or enable state of the element |
| bool |     visible      | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get

A snapshot of the value of Radio Button -> (bool)

`get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | True if this radio button is selected         |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### reset_group

Sets all Radio Buttons in the group to not selected

```python
reset_group()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Radio Button Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(value = None,
    text = None,
    background_color = None,
    text_color = None,
    disabled = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |      value       | if True change to selected and set others in group to unselected |
| str  |       text       | Text to display next to radio button |
| str  | background_color | color of background |
| str  |    text_color    | color of the text. Note this also changes the color of the selection dot |
| bool |     disabled     | disable or enable state of the element |
| bool |     visible      | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Slider Element 

    A slider, horizontal or vertical

```
Slider(range = (None, None),
    default_value = None,
    resolution = None,
    tick_interval = None,
    orientation = None,
    disable_number_display = False,
    border_width = None,
    relief = None,
    change_submits = False,
    enable_events = False,
    disabled = False,
    size = (None, None),
    font = None,
    background_color = None,
    text_color = None,
    key = None,
    k = None,
    pad = None,
    tooltip = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                  Tuple[int, int] or Tuple[float, float]                  |         range          | slider's range (min value, max value) |
|                               int or float                               |     default_value      | starting value for the slider |
|                               int or float                               |       resolution       | the smallest amount the slider can be moved |
|                               int or float                               |     tick_interval      | how often a visible tick should be shown next to slider |
|                                   str                                    |      orientation       | 'horizontal' or 'vertical' ('h' or 'v' also work) |
|                                   bool                                   | disable_number_display | if True no number will be displayed by the Slider Element |
|                                   int                                    |      border_width      | width of border around element in pixels |
|                                   enum                                   |         relief         | relief style. RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID |
|                                   bool                                   |     change_submits     | * DEPRICATED DO NOT USE. Use `enable_events` instead |
|                                   bool                                   |     enable_events      | If True then moving the slider will generate an Event |
|                                   bool                                   |        disabled        | set disable state for element |
|                                (int, int)                                |          size          | (w=characters-wide, h=rows-high) |
|                          str or Tuple[str, int]                          |          font          | specifies the font family, size, etc |
|                                   str                                    |    background_color    | color of slider's background |
|                                   str                                    |       text_color       | color of the slider's text |
|                      str or int or tuple or object                       |          key           | Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
|                      str or int or tuple or object                       |           k            | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |          pad           | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   str                                    |        tooltip         | text, that will appear when mouse hovers over the element |
|                                   bool                                   |        visible         | set visibility state of the element |
|                                   Any                                    |        metadata        | User metadata that can be set to ANYTHING |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Slider Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(value = None,
    range = (None, None),
    disabled = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|             int or float             |  value   | sets current slider value |
| Tuple[int, int] or Tuple[float, float |  range   | Sets a new range for slider |
|                 bool                 | disabled | disable or enable state of the element |
|                 bool                 | visible  | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Slider Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(value = None,
    range = (None, None),
    disabled = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|             int or float             |  value   | sets current slider value |
| Tuple[int, int] or Tuple[float, float |  range   | Sets a new range for slider |
|                 bool                 | disabled | disable or enable state of the element |
|                 bool                 | visible  | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Spin Element 

    A spinner with up/down buttons and a single line of text. Choose 1 values from list

```
Spin(values,
    initial_value = None,
    disabled = False,
    change_submits = False,
    enable_events = False,
    readonly = False,
    size = (None, None),
    auto_size_text = None,
    font = None,
    background_color = None,
    text_color = None,
    key = None,
    k = None,
    pad = None,
    tooltip = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                         Tuple[Any] or List[Any]                          |      values      | List of valid values |
|                                   Any                                    |  initial_value   | Initial item to show in window. Choose from list of values supplied |
|                                   bool                                   |     disabled     | set disable state |
|                                   bool                                   |  change_submits  | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
|                                   bool                                   |  enable_events   | Turns on the element specific events. Spin events happen when an item changes |
|                                   bool                                   |     readonly     | Turns on the element specific events. Spin events happen when an item changes |
|                                (int, int)                                |       size       | (width, height) width = characters-wide, height = rows-high |
|                                   bool                                   |  auto_size_text  | if True will size the element to match the length of the text |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   str                                    | background_color | color of background |
|                                   str                                    |    text_color    | color of the text |
|                      str or int or tuple or object                       |       key        | Used with window.FindElement and with return values to uniquely identify this element |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                   bool                                   |     visible      | set visibility state of the element |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |

### Get

Return the current chosen value showing in spinbox.
This value will be the same as what was provided as list of choices.  If list items are ints, then the
item returned will be an int (not a string)

`Get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The currently visible entry         |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Spin Element. Must call `Window.Read` or `Window.Finalize` prior
Note that the state can be in 3 states only.... enabled, disabled, readonly even
though more combinations are available. The easy way to remember is that if you
change the readonly parameter then you are enabling the element.

```
Update(value = None,
    values = None,
    disabled = None,
    readonly = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|    Any    |  value   | set the current value from list of choices |
| List[Any] |  values  | set available choices |
|   bool    | disabled | disable. Note disabled and readonly cannot be mixed. It must be one OR the other |
|   bool    | readonly | make element readonly. Note disabled and readonly cannot be mixed. It must be one OR the other |
|   bool    | visible  | control visibility of element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get

Return the current chosen value showing in spinbox.
This value will be the same as what was provided as list of choices.  If list items are ints, then the
item returned will be an int (not a string)

`get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The currently visible entry         |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Spin Element. Must call `Window.Read` or `Window.Finalize` prior
Note that the state can be in 3 states only.... enabled, disabled, readonly even
though more combinations are available. The easy way to remember is that if you
change the readonly parameter then you are enabling the element.

```
update(value = None,
    values = None,
    disabled = None,
    readonly = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|    Any    |  value   | set the current value from list of choices |
| List[Any] |  values  | set available choices |
|   bool    | disabled | disable. Note disabled and readonly cannot be mixed. It must be one OR the other |
|   bool    | readonly | make element readonly. Note disabled and readonly cannot be mixed. It must be one OR the other |
|   bool    | visible  | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## StatusBar Element 

    A StatusBar Element creates the sunken text-filled strip at the bottom. Many Windows programs have this line

```
StatusBar(text,
    size = (None, None),
    auto_size_text = None,
    click_submits = None,
    enable_events = False,
    relief = "sunken",
    font = None,
    text_color = None,
    background_color = None,
    justification = None,
    pad = None,
    key = None,
    k = None,
    right_click_menu = None,
    tooltip = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |       text       | Text that is to be displayed in the widget |
|                           Tuple[(int), (int)]                            |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   |  auto_size_text  | True if size should fit the text length |
|                                   bool                                   |  click_submits   | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
|                                   bool                                   |  enable_events   | Turns on the element specific events. StatusBar events occur when the bar is clicked |
|                                   enum                                   |      relief      | relief style. Values are same as progress meter relief values. Can be a constant or a string: `RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID` |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   str                                    |    text_color    | color of the text |
|                                   str                                    | background_color | color of background |
|                                   str                                    |  justification   | how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center` |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                      str or int or tuple or object                       |       key        | Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                      List[List[ List[str] or str ]]                      | right_click_menu | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                   bool                                   |     visible      | set visibility state of the element |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Status Bar Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(value = None,
    background_color = None,
    text_color = None,
    font = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str          |      value       | new text to show |
|          str          | background_color | color of background |
|          str          |    text_color    | color of the text |
| str or Tuple[str, int] |       font       | specifies the font family, size, etc |
|         bool          |     visible      | set visibility state of the element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Status Bar Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(value = None,
    background_color = None,
    text_color = None,
    font = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str          |      value       | new text to show |
|          str          | background_color | color of background |
|          str          |    text_color    | color of the text |
| str or Tuple[str, int] |       font       | specifies the font family, size, etc |
|         bool          |     visible      | set visibility state of the element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Tab Element 

    Tab Element is another "Container" element that holds a layout and displays a tab with text. Used with TabGroup only
    Tabs are never placed directly into a layout.  They are always "Contained" in a TabGroup layout

```
Tab(title,
    layout,
    title_color = None,
    background_color = None,
    font = None,
    pad = None,
    disabled = False,
    border_width = None,
    key = None,
    k = None,
    tooltip = None,
    right_click_menu = None,
    visible = True,
    element_justification = "left",
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |         title         | text to show on the tab |
|                           List[List[Element]]                            |        layout         | The element layout that will be shown in the tab |
|                                   str                                    |      title_color      | color of the tab text (note not currently working on tkinter) |
|                                   str                                    |   background_color    | color of background of the entire layout |
|                          str or Tuple[str, int]                          |         font          | specifies the font family, size, etc |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |          pad          | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   bool                                   |       disabled        | If True button will be created disabled |
|                                   int                                    |     border_width      | width of border around element in pixels |
|                      str or int or tuple or object                       |          key          | Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
|                      str or int or tuple or object                       |           k           | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   str                                    |        tooltip        | text, that will appear when mouse hovers over the element |
|                      List[List[ List[str] or str ]]                      |   right_click_menu    | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |        visible        | set visibility state of the element |
|                                   str                                    | element_justification | All elements inside the Tab will have this justification 'left', 'right', 'center' are valid values |
|                                   Any                                    |       metadata        | User metadata that can be set to ANYTHING |

### AddRow

Not recommended use call.  Used to add rows of Elements to the Frame Element.

```
AddRow(args=*<1 or N object>)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[Element] | *args | The list of elements for this row |

### Layout

Not user callable.  Use layout parameter instead. Creates the layout using the supplied rows of Elements

```
Layout(rows)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Element]] | rows | List[List[Element]] The list of rows |

### Select

Create a tkinter event that mimics user clicking on a tab. Must have called window.Finalize / Read first!

```python
Select()
```

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Tab Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(title = None,
    disabled = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str  |  title   | tab title |
| bool | disabled | disable or enable state of the element |
| bool | visible  | control visibility of element |

### add_row

Not recommended use call.  Used to add rows of Elements to the Frame Element.

```
add_row(args=*<1 or N object>)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[Element] | *args | The list of elements for this row |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### layout

Not user callable.  Use layout parameter instead. Creates the layout using the supplied rows of Elements

```
layout(rows)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Element]] | rows | List[List[Element]] The list of rows |

### select

Create a tkinter event that mimics user clicking on a tab. Must have called window.Finalize / Read first!

```python
select()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Tab Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(title = None,
    disabled = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str  |  title   | tab title |
| bool | disabled | disable or enable state of the element |
| bool | visible  | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## TabGroup Element 

    TabGroup Element groups together your tabs into the group of tabs you see displayed in your window

```
TabGroup(layout,
    tab_location = None,
    title_color = None,
    tab_background_color = None,
    selected_title_color = None,
    selected_background_color = None,
    background_color = None,
    font = None,
    change_submits = False,
    enable_events = False,
    pad = None,
    border_width = None,
    theme = None,
    key = None,
    k = None,
    tooltip = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                             List[List[Tab]]                              |          layout           | Layout of Tabs. Different than normal layouts. ALL Tabs should be on first row |
|                                   str                                    |       tab_location        | location that tabs will be displayed. Choices are left, right, top, bottom, lefttop, leftbottom, righttop, rightbottom, bottomleft, bottomright, topleft, topright |
|                                   str                                    |        title_color        | color of text on tabs |
|                                   str                                    |   tab_background_color    | color of all tabs that are not selected |
|                                   str                                    |   selected_title_color    | color of tab text when it is selected |
|                                   str                                    | selected_background_color | color of tab when it is selected |
|                                   str                                    |     background_color      | color of background area that tabs are located on |
|                          str or Tuple[str, int]                          |           font            | specifies the font family, size, etc |
|                                   bool                                   |      change_submits       | * DEPRICATED DO NOT USE. Use `enable_events` instead |
|                                   bool                                   |       enable_events       | If True then switching tabs will generate an Event |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |            pad            | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                                   int                                    |       border_width        | width of border around element in pixels |
|                                   enum                                   |           theme           | DEPRICATED - You can only specify themes using set options or when window is created. It's not possible to do it on an element basis |
|                      str or int or tuple or object                       |            key            | Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
|                      str or int or tuple or object                       |             k             | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   str                                    |          tooltip          | text, that will appear when mouse hovers over the element |
|                                   bool                                   |          visible          | set visibility state of the element |
|                                   Any                                    |         metadata          | User metadata that can be set to ANYTHING |

### FindKeyFromTabName

Searches through the layout to find the key that matches the text on the tab. Implies names should be unique

```
FindKeyFromTabName(tab_name)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tab_name | name of a tab |
| key or None | **RETURN** | Returns the key or None if no key found

### Get

Returns the current value for the Tab Group, which will be the currently selected tab's KEY or the text on
the tab if no key is defined.  Returns None if an error occurs.
Note that this is exactly the same data that would be returned from a call to Window.Read. Are you sure you
are using this method correctly?

`Get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The key of the currently selected tab or the tab's text if it has no key         |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### find_key_from_tab_name

Searches through the layout to find the key that matches the text on the tab. Implies names should be unique

```
find_key_from_tab_name(tab_name)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tab_name | name of a tab |
| key or None | **RETURN** | Returns the key or None if no key found

### get

Returns the current value for the Tab Group, which will be the currently selected tab's KEY or the text on
the tab if no key is defined.  Returns None if an error occurs.
Note that this is exactly the same data that would be returned from a call to Window.Read. Are you sure you
are using this method correctly?

`get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The key of the currently selected tab or the tab's text if it has no key         |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### set_vscroll_position

Attempts to set the vertical scroll postition for an element's Widget

```
set_vscroll_position(percent_from_top)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | percent_from_top | From 0 to 1.0, the percentage from the top to move scrollbar to |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Table Element 

```
Table(values,
    headings = None,
    visible_column_map = None,
    col_widths = None,
    def_col_width = 10,
    auto_size_columns = True,
    max_col_width = 20,
    select_mode = None,
    display_row_numbers = False,
    num_rows = None,
    row_height = None,
    font = None,
    justification = "right",
    text_color = None,
    background_color = None,
    alternating_row_color = None,
    selected_row_colors = (None, None),
    header_text_color = None,
    header_background_color = None,
    header_font = None,
    row_colors = None,
    vertical_scroll_only = True,
    hide_vertical_scroll = False,
    size = (None, None),
    change_submits = False,
    enable_events = False,
    bind_return_key = False,
    pad = None,
    key = None,
    k = None,
    tooltip = None,
    right_click_menu = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                     List[List[str or int or float]]                      |         values          | ??? |
|                                List[str]                                 |        headings         | The headings to show on the top line |
|                                List[bool]                                |   visible_column_map    | One entry for each column. False indicates the column is not shown |
|                                List[int]                                 |       col_widths        | Number of characters that each column will occupy |
|                                   int                                    |      def_col_width      | Default column width in characters |
|                                   bool                                   |    auto_size_columns    | if True columns will be sized automatically |
|                                   int                                    |      max_col_width      | Maximum width for all columns in characters |
|                                   enum                                   |       select_mode       | Select Mode. Valid values start with "TABLE_SELECT_MODE_". Valid values are: TABLE_SELECT_MODE_NONE TABLE_SELECT_MODE_BROWSE TABLE_SELECT_MODE_EXTENDED |
|                                   bool                                   |   display_row_numbers   | if True, the first column of the table will be the row # |
|                                   int                                    |        num_rows         | The number of rows of the table to display at a time |
|                                   int                                    |       row_height        | height of a single row in pixels |
|                          str or Tuple[str, int]                          |          font           | specifies the font family, size, etc |
|                                   str                                    |      justification      | 'left', 'right', 'center' are valid choices |
|                                   str                                    |       text_color        | color of the text |
|                                   str                                    |    background_color     | color of background |
|                                   str                                    |  alternating_row_color  | if set then every other row will have this color in the background. |
|                          str or Tuple[str, str]                          |   selected_row_colors   | Sets the text color and background color for a selected row. Same format as button colors - tuple ('red', 'yellow') or string 'red on yellow'. Defaults to theme's button color |
|                                   str                                    |    header_text_color    | sets the text color for the header |
|                                   str                                    | header_background_color | sets the background color for the header |
|                          str or Tuple[str, int]                          |       header_font       | specifies the font family, size, etc |
|              List[Tuple[int, str] or Tuple[Int, str, str]]               |       row_colors        | list of tuples of (row, background color) OR (row, foreground color, background color). Sets the colors of listed rows to the color(s) provided (note the optional foreground color) |
|                                   bool                                   |  vertical_scroll_only   | if True only the vertical scrollbar will be visible |
|                                   bool                                   |  hide_vertical_scroll   | if True vertical scrollbar will be hidden |
|                                (int, int)                                |          size           | DO NOT USE! Use num_rows instead |
|                                   bool                                   |     change_submits      | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
|                                   bool                                   |      enable_events      | Turns on the element specific events. Table events happen when row is clicked |
|                                   bool                                   |     bind_return_key     | if True, pressing return key will cause event coming from Table, ALSO a left button double click will generate an event if this parameter is True |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |           pad           | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                      str or int or tuple or object                       |           key           | Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
|                      str or int or tuple or object                       |            k            | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   str                                    |         tooltip         | text, that will appear when mouse hovers over the element |
|                      List[List[ List[str] or str ]]                      |    right_click_menu     | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |         visible         | set visibility state of the element |
|                                   Any                                    |        metadata         | User metadata that can be set to ANYTHING |

### Get

Dummy function for tkinter port.  In the Qt port you can read back the values in the table in case they were
edited.  Don't know yet how to enable editing of a Tree in tkinter so just returning the values provided by
user when Table was created or Updated.

`Get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | the current table values (for now what was originally provided up updated)         |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Table Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(values = None,
    num_rows = None,
    visible = None,
    select_rows = None,
    alternating_row_color = None,
    row_colors = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|       List[List[str or int or float]]        |        values         | A new 2-dimensional table to show |
|                     int                      |       num_rows        | How many rows to display at a time |
|                     bool                     |        visible        | if True then will be visible |
|                  List[int]                   |      select_rows      | List of rows to select as if user did |
|                     str                      | alternating_row_color | the color to make every other row |
| List[Tuple[int, str] or Tuple[Int, str, str]] |      row_colors       | list of tuples of (row, background color) OR (row, foreground color, background color). Changes the colors of listed rows to the color(s) provided (note the optional foreground color) |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get

Dummy function for tkinter port.  In the Qt port you can read back the values in the table in case they were
edited.  Don't know yet how to enable editing of a Tree in tkinter so just returning the values provided by
user when Table was created or Updated.

`get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | the current table values (for now what was originally provided up updated)         |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Table Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(values = None,
    num_rows = None,
    visible = None,
    select_rows = None,
    alternating_row_color = None,
    row_colors = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|       List[List[str or int or float]]        |        values         | A new 2-dimensional table to show |
|                     int                      |       num_rows        | How many rows to display at a time |
|                     bool                     |        visible        | if True then will be visible |
|                  List[int]                   |      select_rows      | List of rows to select as if user did |
|                     str                      | alternating_row_color | the color to make every other row |
| List[Tuple[int, str] or Tuple[Int, str, str]] |      row_colors       | list of tuples of (row, background color) OR (row, foreground color, background color). Changes the colors of listed rows to the color(s) provided (note the optional foreground color) |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Text Element 

    Text - Display some text in the window.  Usually this means a single line of text.  However, the text can also be multiple lines.  If multi-lined there are no scroll bars.

```
Text(text = "",
    size = (None, None),
    auto_size_text = None,
    click_submits = False,
    enable_events = False,
    relief = None,
    font = None,
    text_color = None,
    background_color = None,
    border_width = None,
    justification = None,
    pad = None,
    key = None,
    k = None,
    right_click_menu = None,
    grab = None,
    tooltip = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   Any                                    |       text       | The text to display. Can include /n to achieve multiple lines. Will convert (optional) parameter into a string |
|                           (int, int or  None)                            |       size       | (width, height) width = characters-wide, height = rows-high |
|                                   bool                                   |  auto_size_text  | if True size of the Text Element will be sized to fit the string provided in 'text' parm |
|                                   bool                                   |  click_submits   | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
|                                   bool                                   |  enable_events   | Turns on the element specific events. Text events happen when the text is clicked |
|                                (str/enum)                                |      relief      | relief style around the text. Values are same as progress meter relief values. Should be a constant that is defined at starting with "RELIEF_" - `RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID` |
|                     (str or Tuple[str, int] or None)                     |       font       | specifies the font family, size, etc |
|                                   str                                    |    text_color    | color of the text |
|                                   str                                    | background_color | color of background |
|                                   int                                    |   border_width   | number of pixels for the border (if using a relief) |
|                                   str                                    |  justification   | how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center` |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                      str or int or tuple or object                       |       key        | Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                      List[List[ List[str] or str ]]                      | right_click_menu | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |       grab       | If True can grab this element and move the window around. Default is False |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                   bool                                   |     visible      | set visibility state of the element |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |

#### Get

Gets the current value of the displayed text

`Get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The current value         |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Text Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(value = None,
    background_color = None,
    text_color = None,
    font = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str          |      value       | new text to show |
|          str          | background_color | color of background |
|          str          |    text_color    | color of the text |
| str or Tuple[str, int] |       font       | specifies the font family, size, etc |
|         bool          |     visible      | set visibility state of the element |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

#### get

Gets the current value of the displayed text

`get()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The current value         |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Text Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(value = None,
    background_color = None,
    text_color = None,
    font = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str          |      value       | new text to show |
|          str          | background_color | color of background |
|          str          |    text_color    | color of the text |
| str or Tuple[str, int] |       font       | specifies the font family, size, etc |
|         bool          |     visible      | set visibility state of the element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## Titlebar Element

Note that while the Titlebar is an element, it is implemented using a function.
It is actually a "compound element" that consists of several elements combined into a single Column element.
See the Column element to get a list of method calls available.  The function returns a Column element.

A custom titlebar that replaces the OS provided titlebar, thus giving you control
the is not possible using the OS provided titlebar such as the color.

NOTE LINUX USERS - at the moment the minimize function is not yet working.  Windows users
should have no problem and it should function as a normal window would.

This titlebar is created from a row of elements that is then encapulated into a
single Column element which is what the Titlebar returns to you.

A custom titlebar removes the margins from your window.  Ify ou want the  remainder
of your Window to have margins, place the layout after the Titlebar into a Column and
set the pad of that Column to the dimensions you would like your margins to have.

The Titlebar is a COLUMN element.  You can thus call the update method for the column and
perform operations such as making the column visible/invisible

```
Titlebar(title = "",
    icon = None,
    text_color = None,
    background_color = None,
    font = None,
    key = None,
    k = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|       str or bytes or None        |       icon       | Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO |
|                str                |      title       | The "title" to show in the titlebar |
|            str or None            |    text_color    | Text color for titlebar |
|            str or None            | background_color | Background color for titlebar |
|            str or None            |       font       | Font to be used for the text and the symbols |
| str or int or tuple or object or None |       key        | Identifies an Element. Should be UNIQUE to this window. |
| str or int or tuple or object or None |        k         | Exactly the same as key. Choose one of them to use |
| List[Element] | **RETURN** | A list of elements (i.e. a "row" for a layout)
    :param key: Identifies an Element. Should be UNIQUE to this window.
    :type key: str | int | tuple | object | None
    :param k: Exactly the same as key.  Choose one of them to use
    :type k: str | int | tuple | object | None

## Tree Element 

    Tree Element - Presents data in a tree-like manner, much like a file/folder browser.  Uses the TreeData class
    to hold the user's data and pass to the element for display.

```
Tree(data = None,
    headings = None,
    visible_column_map = None,
    col_widths = None,
    col0_width = 10,
    def_col_width = 10,
    auto_size_columns = True,
    max_col_width = 20,
    select_mode = None,
    show_expanded = False,
    change_submits = False,
    enable_events = False,
    font = None,
    justification = "right",
    text_color = None,
    background_color = None,
    selected_row_colors = (None, None),
    header_text_color = None,
    header_background_color = None,
    header_font = None,
    num_rows = None,
    row_height = None,
    pad = None,
    key = None,
    k = None,
    tooltip = None,
    right_click_menu = None,
    visible = True,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                 TreeData                                 |          data           | The data represented using a PySimpleGUI provided TreeData class |
|                                List[str]                                 |        headings         | List of individual headings for each column |
|                                List[bool]                                |   visible_column_map    | Determines if a column should be visible. If left empty, all columns will be shown |
|                                List[int]                                 |       col_widths        | List of column widths so that individual column widths can be controlled |
|                                   int                                    |       col0_width        | Size of Column 0 which is where the row numbers will be optionally shown |
|                                   int                                    |      def_col_width      | default column width |
|                                   bool                                   |    auto_size_columns    | if True, the size of a column is determined using the contents of the column |
|                                   int                                    |      max_col_width      | the maximum size a column can be |
|                                   enum                                   |       select_mode       | Use same values as found on Table Element. Valid values include: TABLE_SELECT_MODE_NONE TABLE_SELECT_MODE_BROWSE TABLE_SELECT_MODE_EXTENDED |
|                                   bool                                   |      show_expanded      | if True then the tree will be initially shown with all nodes completely expanded |
|                                   bool                                   |     change_submits      | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
|                                   bool                                   |      enable_events      | Turns on the element specific events. Tree events happen when row is clicked |
|                          str or Tuple[str, int]                          |          font           | specifies the font family, size, etc |
|                                   str                                    |      justification      | 'left', 'right', 'center' are valid choices |
|                                   str                                    |       text_color        | color of the text |
|                                   str                                    |    background_color     | color of background |
|                          str or Tuple[str, str]                          |   selected_row_colors   | Sets the text color and background color for a selected row. Same format as button colors - tuple ('red', 'yellow') or string 'red on yellow'. Defaults to theme's button color |
|                                   str                                    |    header_text_color    | sets the text color for the header |
|                                   str                                    | header_background_color | sets the background color for the header |
|                          str or Tuple[str, int]                          |       header_font       | specifies the font family, size, etc |
|                                   int                                    |        num_rows         | The number of rows of the table to display at a time |
|                                   int                                    |       row_height        | height of a single row in pixels |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |           pad           | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                      str or int or tuple or object                       |           key           | Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element |
|                      str or int or tuple or object                       |            k            | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   str                                    |         tooltip         | text, that will appear when mouse hovers over the element |
|                         List[List[str] or str]]                          |    right_click_menu     | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                                   bool                                   |         visible         | set visibility state of the element |
|                                   Any                                    |        metadata         | User metadata that can be set to ANYTHING |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### Update

Changes some of the settings for the Tree Element. Must call `Window.Read` or `Window.Finalize` prior

```
Update(values = None,
    key = None,
    value = None,
    text = None,
    icon = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          TreeData          | values  | Representation of the tree |
| str or int or tuple or object |   key   | identifies a particular item in tree to update |
|            Any             |  value  | sets the node identified by key to a particular value |
|            str             |  text   | sets the node identified by ket to this string |
|        bytes or str        |  icon   | can be either a base64 icon or a filename for the icon |
|            bool            | visible | control visibility of element |

### add_treeview_data

Not a user function.  Recursive method that inserts tree data into the tkinter treeview widget.

```
add_treeview_data(node)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| TreeData | node | The node to insert. Will insert all nodes from starting point downward, recursively |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### set_vscroll_position

Attempts to set the vertical scroll postition for an element's Widget

```
set_vscroll_position(percent_from_top)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | percent_from_top | From 0 to 1.0, the percentage from the top to move scrollbar to |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### update

Changes some of the settings for the Tree Element. Must call `Window.Read` or `Window.Finalize` prior

```
update(values = None,
    key = None,
    value = None,
    text = None,
    icon = None,
    visible = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          TreeData          | values  | Representation of the tree |
| str or int or tuple or object |   key   | identifies a particular item in tree to update |
|            Any             |  value  | sets the node identified by key to a particular value |
|            str             |  text   | sets the node identified by ket to this string |
|        bytes or str        |  icon   | can be either a base64 icon or a filename for the icon |
|            bool            | visible | control visibility of element |

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## TreeData (for Tree Element) 

    Class that user fills in to represent their tree data. It's a very simple tree representation with a root "Node"
    with possibly one or more children "Nodes".  Each Node contains a key, text to display, list of values to display
    and an icon.  The entire tree is built using a single method, Insert.  Nothing else is required to make the tree.

Instantiate the object, initializes the Tree Data, creates a root node for you

```python
TreeData()
```

### Insert

Inserts a node into the tree. This is how user builds their tree, by Inserting Nodes
This is the ONLY user callable method in the TreeData class

```
Insert(parent,
    key,
    text,
    values,
    icon = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|            Node            | parent | the parent Node |
| str or int or tuple or object |  key   | Used to uniquely identify this node |
|            str             |  text  | The text that is displayed at this node's location |
|         List[Any]          | values | The list of values that are displayed at this node |
|        str or bytes        |  icon  | icon |

### Node

Contains information about the individual node in the tree

```
Node(parent,
    key,
    text,
    values,
    icon = None)
```

### insert

Inserts a node into the tree. This is how user builds their tree, by Inserting Nodes
This is the ONLY user callable method in the TreeData class

```
insert(parent,
    key,
    text,
    values,
    icon = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|            Node            | parent | the parent Node |
| str or int or tuple or object |  key   | Used to uniquely identify this node |
|            str             |  text  | The text that is displayed at this node's location |
|         List[Any]          | values | The list of values that are displayed at this node |
|        str or bytes        |  icon  | icon |

## VerticalSeparator Element 

    Vertical Separator Element draws a vertical line at the given location. It will span 1 "row". Usually paired with
    Column Element if extra height is needed

```
VerticalSeparator(color = None,
    pad = None,
    key = None,
    k = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    | color | Color of the line. Defaults to theme's text color. Can be name or #RRGGBB format |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |  pad  | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                      str or int or tuple or object                       |  key  | Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window |
|                      str or int or tuple or object                       |   k   | Same as the Key. You can use either k or key. Which ever is set will be used. |

### SetFocus

Sets the current focus to be on this element

```
SetFocus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### SetTooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
SetTooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### bind

Used to add tkinter events to an Element.
The tkinter specific data is in the Element's member variable user_bind_event

```
bind(bind_string, key_modifier)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string  | The string tkinter expected in its bind function |
| str | key_modifier | Additional data to be added to the element's key when event is returned |

### expand

Causes the Element to expand to fill available space in the X and Y directions.  Can specify which or both directions

```
expand(expand_x = False,
    expand_y = False,
    expand_row = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool |  expand_x  | If True Element will expand in the Horizontal directions |
| bool |  expand_y  | If True Element will expand in the Vertical directions |
| bool | expand_row | If True the row containing the element will also expand. Without this your element is "trapped" within the row |

### get_size

Return the size of an element in Pixels.  Care must be taken as some elements use characters to specify their size but will return pixels when calling this get_size method.

`get_size()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | width and height of the element         |

### hide_row

Hide the entire row an Element is located on.
        Use this if you must have all space removed when you are hiding an element, including the row container

```python
hide_row()
```

### set_cursor

Sets the cursor for the current Element.

```
set_cursor(cursor)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | cursor | The tkinter cursor name |

### set_focus

Sets the current focus to be on this element

```
set_focus(force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | force | if True will call focus_force otherwise calls focus_set |

### set_size

Changes the size of an element to a specific size.
It's possible to specify None for one of sizes so that only 1 of the element's dimensions are changed.

```
set_size(size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | size | The size in characters, rows typically. In some cases they are pixels |

### set_tooltip

Called by application to change the tooltip text for an Element.  Normally invoked using the Element Object such as: window.Element('key').SetToolTip('New tip').

```
set_tooltip(tooltip_text)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | tooltip_text | the text to show in tooltip. |

### unbind

Removes a previously bound tkinter event from an Element.

```
unbind(bind_string)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | bind_string | The string tkinter expected in its bind function |

### unhide_row

Unhides (makes visible again) the row container that the Element is located on.
        Note that it will re-appear at the bottom of the window / container, most likely.

```python
unhide_row()
```

### visible

#### property: visible

Returns visibility state for the element.  This is a READONLY property
To control visibility, use the element's update method

|Type|Name|Meaning|
|---|---|---|
| bool | **return** | Visibility state for element         |

## UserSettings (Class interface to User Settings APIs... can also use the function call interface) 

User Settings

```
UserSettings(filename = None,
    path = None,
    silent_on_error = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str or None) | filename | The name of the file to use. Can be a full path and filename or just filename |
| (str or None) |   path   | The folder that the settings file will be stored in. Do not include the filename. |

### delete_entry

Deletes an individual entry.  If no filename has been specified up to this point,
then a default filename will be used.
After value has been deleted, the settings file is written to disk.

```
delete_entry(key)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any | key | Setting to be deleted. Can be any valid dictionary key type (i.e. must be hashable) |

### delete_file

Deltes the filename and path for your settings file.  Either paramter can be optional.
If you don't choose a path, one is provided for you that is OS specific
Windows path default = users/name/AppData/Local/PySimpleGUI/settings.
If you don't choose a filename, your application's filename + '.json' will be used
Also sets your current dictionary to a blank one.

```
delete_file(filename = None, path = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str or None) | filename | The name of the file to use. Can be a full path and filename or just filename |
| (str or None) |   path   | The folder that the settings file will be stored in. Do not include the filename. |

### exists

Check if a particular settings file exists.  Returns True if file exists

```
exists(filename = None, path = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str or None) | filename | The name of the file to use. Can be a full path and filename or just filename |
| (str or None) |   path   | The folder that the settings file will be stored in. Do not include the filename. |

### get

Returns the value of a specified setting.  If the setting is not found in the settings dictionary, then
the user specified default value will be returned.  It no default is specified and nothing is found, then
the "default value" is returned.  This default can be specified in this call, or previously defined
by calling set_default. If nothing specified now or previously, then None is returned as default.

```
get(key, default = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any |   key   | Key used to lookup the setting in the settings dictionary |
| Any | default | Value to use should the key not be found in the dictionary |
| (Any) | **RETURN** | Value of specified settings

### get_dict

Returns the current settings dictionary.  If you've not setup the filename for the
settings, a default one will be used and then read.

Note that you can display the dictionary in text format by printing the object itself.

`get_dict()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The current settings dictionary         |

### get_filename

Sets the filename and path for your settings file.  Either paramter can be optional.

If you don't choose a path, one is provided for you that is OS specific
Windows path default = users/name/AppData/Local/PySimpleGUI/settings.

If you don't choose a filename, your application's filename + '.json' will be used.

Normally the filename and path are split in the user_settings calls. However for this call they
can be combined so that the filename contains both the path and filename.

```
get_filename(filename = None, path = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str or None) | filename | The name of the file to use. Can be a full path and filename or just filename |
| (str or None) |   path   | The folder that the settings file will be stored in. Do not include the filename. |
| (str) | **RETURN** | The full pathname of the settings file that has both the path and filename combined.

### load

Specifies the path and filename to use for the settings and reads the contents of the file.
The filename can be a full filename including a path, or the path can be specified separately.
If  no filename is specified, then the caller's filename will be used with the extension ".json"

```
load(filename = None, path = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str or None) | filename | Filename to load settings from (and save to in the future) |
| (str or None) |   path   | Path to the file. Defaults to a specific folder depending on the operating system |
| (dict) | **RETURN** | The settings dictionary (i.e. all settings)

### read

Reads settings file and returns the dictionary.

`read()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | settings dictionary         |

### save

Saves the current settings dictionary.  If a filename or path is specified in the call, then it will override any
previously specitfied filename to create a new settings file.  The settings dictionary is then saved to the newly defined file.

```
save(filename = None, path = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str or None) | filename | The fFilename to save to. Can specify a path or just the filename. If no filename specified, then the caller's filename will be used. |
| (str or None) |   path   | The (optional) path to use to save the file. |
| (str) | **RETURN** | The full path and filename used to save the settings

### set

Sets an individual setting to the specified value.  If no filename has been specified up to this point,
then a default filename will be used.
After value has been modified, the settings file is written to disk.

```
set(key, value)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any |  key  | Setting to be saved. Can be any valid dictionary key type |
| Any | value | Value to save as the setting's value. Can be anything |

### set_default_value

Set the value that will be returned if a requested setting is not found

```
set_default_value(default)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any | default | value to be returned if a setting is not found in the settings dictionary |

### set_location

Sets the location of the settings file

```
set_location(filename = None, path = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str or None) | filename | The name of the file to use. Can be a full path and filename or just filename |
| (str or None) |   path   | The folder that the settings file will be stored in. Do not include the filename. |

### write_new_dictionary

Writes a specified dictionary to the currently defined settings filename.

```
write_new_dictionary(settings_dict)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| dict | settings_dict | The dictionary to be written to the currently defined settings file |

## Window 

    Represents a single Window

```
Window(title,
    layout = None,
    default_element_size = (45, 1),
    default_button_element_size = (None, None),
    auto_size_text = None,
    auto_size_buttons = None,
    location = (None, None),
    size = (None, None),
    element_padding = None,
    margins = (None, None),
    button_color = None,
    font = None,
    progress_bar_color = (None, None),
    background_color = None,
    border_depth = None,
    auto_close = False,
    auto_close_duration = 3,
    icon = None,
    force_toplevel = False,
    alpha_channel = 1,
    return_keyboard_events = False,
    use_default_focus = True,
    text_justification = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    resizable = False,
    disable_close = False,
    disable_minimize = False,
    right_click_menu = None,
    transparent_color = None,
    debugger_enabled = True,
    right_click_menu_background_color = None,
    right_click_menu_text_color = None,
    right_click_menu_disabled_text_color = None,
    right_click_menu_font = None,
    finalize = False,
    element_justification = "left",
    ttk_theme = None,
    use_ttk_buttons = None,
    modal = False,
    enable_close_attempted_event = False,
    titlebar_background_color = None,
    titlebar_text_color = None,
    titlebar_font = None,
    titlebar_icon = None,
    use_custom_titlebar = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                    str                    |                title                 | The title that will be displayed in the Titlebar and on the Taskbar |
|           List[List[Elements]]            |                layout                | The layout for the window. Can also be specified in the Layout method |
|       (int, int) - (width, height)        |         default_element_size         | size in characters (wide) and rows (high) for all elements in this window |
|                (int, int)                 |     default_button_element_size      | (width, height) size in characters (wide) and rows (high) for all Button elements in this window |
|                   bool                    |            auto_size_text            | True if Elements in Window should be sized to exactly fir the length of text |
|                   bool                    |          auto_size_buttons           | True if Buttons in this Window should be sized to exactly fit the text on this. |
|              Tuple[int, int]              |               location               | (x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen. |
|                (int, int)                 |                 size                 | (width, height) size in pixels for this window. Normally the window is autosized to fit contents, not set to an absolute size by the user |
| Tuple[int, int] or ((int, int),(int,int)) |           element_padding            | Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom)) |
|              Tuple[int, int]              |               margins                | (left/right, top/bottom) Amount of pixels to leave inside the window's frame around the edges before your elements are shown. |
|          Tuple[str, str] or str           |             button_color             | Default button colors for all buttons in the window |
|      str or Tuple[str, int] or None       |                 font                 | specifies the font family, size, etc |
|              Tuple[str, str]              |          progress_bar_color          | (bar color, background color) Sets the default colors for all progress bars in the window |
|                    str                    |           background_color           | color of background |
|                    int                    |             border_depth             | Default border depth (width) for all elements in the window |
|                   bool                    |              auto_close              | If True, the window will automatically close itself |
|                    int                    |         auto_close_duration          | Number of seconds to wait before closing the window |
|                    str                    |                 icon                 | Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO |
|                   bool                    |            force_toplevel            | If True will cause this window to skip the normal use of a hidden master window |
|                   float                   |            alpha_channel             | Sets the opacity of the window. 0 = invisible 1 = completely visible. Values bewteen 0 & 1 will produce semi-transparent windows in SOME environments (The Raspberry Pi always has this value at 1 and cannot change. |
|                   bool                    |        return_keyboard_events        | if True key presses on the keyboard will be returned as Events from Read calls |
|                   bool                    |          use_default_focus           | If True will use the default focus algorithm to set the focus to the "Correct" element |
|       'left' or 'right' or 'center'       |          text_justification          | Default text justification for all Text Elements in window |
|                   bool                    |             no_titlebar              | If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar |
|                   bool                    |            grab_anywhere             | If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems |
|                   bool                    |             keep_on_top              | If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm |
|                   bool                    |              resizable               | If True, allows the user to resize the window. Note the not all Elements will change size or location when resizing. |
|                   bool                    |            disable_close             | If True, the X button in the top right corner of the window will no work. Use with caution and always give a way out toyour users |
|                   bool                    |           disable_minimize           | if True the user won't be able to minimize window. Good for taking over entire screen and staying that way. |
|      List[List[ List[str] or str ]]       |           right_click_menu           | A list of lists of Menu items to show when this element is right clicked. See user docs for exact format. |
|                    str                    |          transparent_color           | Any portion of the window that has this color will be completely transparent. You can even click through these spots to the window under this window. |
|                   bool                    |           debugger_enabled           | If True then the internal debugger will be enabled |
|                    str                    |  right_click_menu_background_color   | Background color for right click menus |
|                    str                    |     right_click_menu_text_color      | Text color for right click menus |
|                    str                    | right_click_menu_disabled_text_color | Text color for disabled right click menu items |
|          str or Tuple[str, int]           |        right_click_menu_font         | Font for right click menus |
|                   bool                    |               finalize               | If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code |
|                    str                    |        element_justification         | All elements in the Window itself will have this justification 'left', 'right', 'center' are valid values |
|                    str                    |              ttk_theme               | Set the tkinter ttk "theme" of the window. Default = DEFAULT_TTK_THEME. Sets all ttk widgets to this theme as their default |
|                   bool                    |           use_ttk_buttons            | Affects all buttons in window. True = use ttk buttons. False = do not use ttk buttons. None = use ttk buttons only if on a Mac |
|                   bool                    |                modal                 | If True then this window will be the only window a user can interact with until it is closed |
|                   bool                    |     enable_close_attempted_event     | If True then the window will not close when "X" clicked. Instead an event WINDOW_CLOSE_ATTEMPTED_EVENT if returned from window.read |
|               (str or None)               |      titlebar_background_color       | If custom titlebar indicated by use_custom_titlebar, then use this as background color |
|               (str or None)               |         titlebar_text_color          | If custom titlebar indicated by use_custom_titlebar, then use this as text color |
|     (str or Tuple[str, int] or None)      |            titlebar_font             | If custom titlebar indicated by use_custom_titlebar, then use this as title font |
|              (bytes or str)               |            titlebar_icon             | If custom titlebar indicated by use_custom_titlebar, then use this as the icon (file or base64 bytes) |
|                   bool                    |         use_custom_titlebar          | If True, then a custom titlebar will be used instead of the normal titlebar |
|                    Any                    |               metadata               | User metadata that can be set to ANYTHING |

### AddRow

Adds a single row of elements to a window's self.Rows variables.
Generally speaking this is NOT how users should be building Window layouts.
Users, create a single layout (a list of lists) and pass as a parameter to Window object, or call Window.Layout(layout)

```
AddRow(args=*<1 or N object>)
```

### AddRows

Loops through a list of lists of elements and adds each row, list, to the layout.
This is NOT the best way to go about creating a window.  Sending the entire layout at one time and passing
it as a parameter to the Window call is better.

```
AddRows(rows)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Elements]] | rows | A list of a list of elements |

### AlphaChannel

#### property: AlphaChannel

A property that changes the current alpha channel value (internal value)

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | (float) the current alpha channel setting according to self, not read directly from tkinter |

### BringToFront

Brings this window to the top of all other windows (perhaps may not be brought before a window made to "stay
        on top")

```python
BringToFront()
```

### Close

Closes window.  Users can safely call even if window has been destroyed.   Should always call when done with
        a window so that resources are properly freed up within your thread.

```python
Close()
```

### CurrentLocation

Get the current location of the window's top left corner

`CurrentLocation()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The x and y location in tuple form (x,y)         |

### Disable

Disables window from taking any input from the user

```python
Disable()
```

### DisableDebugger

Disable the internal debugger. By default the debugger is ENABLED

```python
DisableDebugger()
```

### Disappear

Causes a window to "disappear" from the screen, but remain on the taskbar. It does this by turning the alpha
        channel to 0.  NOTE that on some platforms alpha is not supported. The window will remain showing on these
        platforms.  The Raspberry Pi for example does not have an alpha setting

```python
Disappear()
```

### Elem

Find element object associated with the provided key.
THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement:
element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way"
window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these:
FindElement == Element == Find
Rememeber that this call will return None if no match is found which may cause your code to crash if not
checked for.

```
Elem(key, silent_on_error = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or int or tuple or object |       key       | Used with window.FindElement and with return values to uniquely identify this element |
|            bool            | silent_on_error | If True do not display popup nor print warning of key errors |
| Element or Error Element or None | **RETURN** | Return value can be: the Element that matches the supplied key if found; an Error Element if silent_on_error is False; None if silent_on_error True;

### Element

Find element object associated with the provided key.
THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement:
element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way"
window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these:
FindElement == Element == Find
Rememeber that this call will return None if no match is found which may cause your code to crash if not
checked for.

```
Element(key, silent_on_error = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or int or tuple or object |       key       | Used with window.FindElement and with return values to uniquely identify this element |
|            bool            | silent_on_error | If True do not display popup nor print warning of key errors |
| Element or Error Element or None | **RETURN** | Return value can be: the Element that matches the supplied key if found; an Error Element if silent_on_error is False; None if silent_on_error True;

### Enable

Re-enables window to take user input after having it be Disabled previously

```python
Enable()
```

### EnableDebugger

Enables the internal debugger. By default, the debugger IS enabled

```python
EnableDebugger()
```

### Fill

Fill in elements that are input fields with data based on a 'values dictionary'

```
Fill(values_dict)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (Dict[Any, Any]) - {Element_key : value} | values_dict | pairs |
| (Window) | **RETURN** | returns self so can be chained with other methods

### Finalize

Use this method to cause your layout to built into a real tkinter window.  In reality this method is like
Read(timeout=0).  It doesn't block and uses your layout to create tkinter widgets to represent the elements.
Lots of action!

`Finalize()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Returns 'self' so that method "Chaining" can happen (read up about it as it's very cool!)         |

### Find

Find element object associated with the provided key.
THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement:
element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way"
window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these:
FindElement == Element == Find
Rememeber that this call will return None if no match is found which may cause your code to crash if not
checked for.

```
Find(key, silent_on_error = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or int or tuple or object |       key       | Used with window.FindElement and with return values to uniquely identify this element |
|            bool            | silent_on_error | If True do not display popup nor print warning of key errors |
| Element or Error Element or None | **RETURN** | Return value can be: the Element that matches the supplied key if found; an Error Element if silent_on_error is False; None if silent_on_error True;

### FindElement

Find element object associated with the provided key.
THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement:
element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way"
window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these:
FindElement == Element == Find
Rememeber that this call will return None if no match is found which may cause your code to crash if not
checked for.

```
FindElement(key, silent_on_error = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or int or tuple or object |       key       | Used with window.FindElement and with return values to uniquely identify this element |
|            bool            | silent_on_error | If True do not display popup nor print warning of key errors |
| Element or Error Element or None | **RETURN** | Return value can be: the Element that matches the supplied key if found; an Error Element if silent_on_error is False; None if silent_on_error True;

### FindElementWithFocus

Returns the Element that currently has focus as reported by tkinter. If no element is found None is returned!

`FindElementWithFocus()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | An Element if one has been found with focus or None if no element found         |

### GetScreenDimensions

Get the screen dimensions.  NOTE - you must have a window already open for this to work (blame tkinter not me)

`GetScreenDimensions()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Tuple containing width and height of screen in pixels         |

### GrabAnyWhereOff

Turns off Grab Anywhere functionality AFTER a window has been created.  Don't try on a window that's not yet
        been Finalized or Read.

```python
GrabAnyWhereOff()
```

### GrabAnyWhereOn

Turns on Grab Anywhere functionality AFTER a window has been created.  Don't try on a window that's not yet
        been Finalized or Read.

```python
GrabAnyWhereOn()
```

### Hide

Hides the window from the screen and the task bar

```python
Hide()
```

### Layout

Second of two preferred ways of telling a Window what its layout is. The other way is to pass the layout as
a parameter to Window object.  The parameter method is the currently preferred method. This call to Layout
has been removed from examples contained in documents and in the Demo Programs. Trying to remove this call
from history and replace with sending as a parameter to Window.

```
Layout(rows)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Elements]] | rows | Your entire layout |
| (Window) | **RETURN** | self so that you can chain method calls

### LoadFromDisk

Restore values from a previous call to SaveToDisk which saves the returned values dictionary in Pickle format

```
LoadFromDisk(filename)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | filename | Pickle Filename to load |

### Maximize

Maximize the window. This is done differently on a windows system versus a linux or mac one.  For non-Windows
        the root attribute '-fullscreen' is set to True.  For Windows the "root" state is changed to "zoomed"
        The reason for the difference is the title bar is removed in some cases when using fullscreen option

```python
Maximize()
```

### Minimize

Minimize this window to the task bar

```python
Minimize()
```

### Move

Move the upper left corner of this window to the x,y coordinates provided

```
Move(x, y)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int | x | x coordinate in pixels |
| int | y | y coordinate in pixels |

### Normal

Restore a window to a non-maximized state.  Does different things depending on platform.  See Maximize for more.

```python
Normal()
```

### Read

THE biggest deal method in the Window class! This is how you get all of your data from your Window.
Pass in a timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key
if no other GUI events happen first.

```
Read(timeout = None,
    timeout_key = "__TIMEOUT__",
    close = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int  |   timeout   | Milliseconds to wait until the Read will return IF no other GUI events happen first |
| Any  | timeout_key | The value that will be returned from the call if the timer expired |
| bool |    close    | if True the window will be closed prior to returning |
| Tuple[(Any), Dict[Any, Any], List[Any], None] | **RETURN** | (event, values)

### Reappear

Causes a window previously made to "Disappear" (using that method). Does this by restoring the alpha channel

```python
Reappear()
```

### Refresh

Refreshes the window by calling tkroot.update().  Can sometimes get away with a refresh instead of a Read.
Use this call when you want something to appear in your Window immediately (as soon as this function is called).
Without this call your changes to a Window will not be visible to the user until the next Read call

`Refresh()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | `self` so that method calls can be easily "chained"         |

### SaveToDisk

Saves the values contained in each of the input areas of the form. Basically saves what would be returned from a call to Read.  It takes these results and saves them to disk using pickle.
 Note that every element in your layout that is to be saved must have a key assigned to it.

```
SaveToDisk(filename)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | filename | Filename to save the values to in pickled form |

### SendToBack

Pushes this window to the bottom of the stack of windows. It is the opposite of BringToFront

```python
SendToBack()
```

### SetAlpha

Sets the Alpha Channel for a window.  Values are between 0 and 1 where 0 is completely transparent

```
SetAlpha(alpha)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | alpha | 0 to 1. 0 is completely transparent. 1 is completely visible and solid (can't see through) |

### SetIcon

Changes the icon that is shown on the title bar and on the task bar.
NOTE - The file type is IMPORTANT and depends on the OS!
Can pass in:
* filename which must be a .ICO icon file for windows, PNG file for Linux
* bytes object
* BASE64 encoded file held in a variable

```
SetIcon(icon = None, pngbase64 = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str |   icon    | Filename or bytes object |
| str | pngbase64 | Base64 encoded image |

### SetTransparentColor

Set the color that will be transparent in your window. Areas with this color will be SEE THROUGH.

```
SetTransparentColor(color)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | color | Color string that defines the transparent color |

### Size

#### property: Size

Return the current size of the window in pixels

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | (width, height) of the window         |

### UnHide

Used to bring back a window that was previously hidden using the Hide method

```python
UnHide()
```

### VisibilityChanged

When making an element in a column or someplace that has a scrollbar, then you'll want to call this function
        prior to the column's contents_changed() method.

```python
VisibilityChanged()
```

### add_row

Adds a single row of elements to a window's self.Rows variables.
Generally speaking this is NOT how users should be building Window layouts.
Users, create a single layout (a list of lists) and pass as a parameter to Window object, or call Window.Layout(layout)

```
add_row(args=*<1 or N object>)
```

### add_rows

Loops through a list of lists of elements and adds each row, list, to the layout.
This is NOT the best way to go about creating a window.  Sending the entire layout at one time and passing
it as a parameter to the Window call is better.

```
add_rows(rows)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Elements]] | rows | A list of a list of elements |

### alpha_channel

#### property: alpha_channel

A property that changes the current alpha channel value (internal value)

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | (float) the current alpha channel setting according to self, not read directly from tkinter |

### bind

Used to add tkinter events to a Window.
The tkinter specific data is in the Window's member variable user_bind_event

```
bind(bind_string, key)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|            str             | bind_string | The string tkinter expected in its bind function |
| str or int or tuple or object |     key     | The event that will be generated when the tkinter event occurs |

### bring_to_front

Brings this window to the top of all other windows (perhaps may not be brought before a window made to "stay
        on top")

```python
bring_to_front()
```

### close

Closes window.  Users can safely call even if window has been destroyed.   Should always call when done with
        a window so that resources are properly freed up within your thread.

```python
close()
```

### current_location

Get the current location of the window's top left corner

`current_location()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | The x and y location in tuple form (x,y)         |

### disable

Disables window from taking any input from the user

```python
disable()
```

### disable_debugger

Disable the internal debugger. By default the debugger is ENABLED

```python
disable_debugger()
```

### disappear

Causes a window to "disappear" from the screen, but remain on the taskbar. It does this by turning the alpha
        channel to 0.  NOTE that on some platforms alpha is not supported. The window will remain showing on these
        platforms.  The Raspberry Pi for example does not have an alpha setting

```python
disappear()
```

### elem

Find element object associated with the provided key.
THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement:
element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way"
window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these:
FindElement == Element == Find
Rememeber that this call will return None if no match is found which may cause your code to crash if not
checked for.

```
elem(key, silent_on_error = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or int or tuple or object |       key       | Used with window.FindElement and with return values to uniquely identify this element |
|            bool            | silent_on_error | If True do not display popup nor print warning of key errors |
| Element or Error Element or None | **RETURN** | Return value can be: the Element that matches the supplied key if found; an Error Element if silent_on_error is False; None if silent_on_error True;

### element

Find element object associated with the provided key.
THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement:
element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way"
window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these:
FindElement == Element == Find
Rememeber that this call will return None if no match is found which may cause your code to crash if not
checked for.

```
element(key, silent_on_error = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or int or tuple or object |       key       | Used with window.FindElement and with return values to uniquely identify this element |
|            bool            | silent_on_error | If True do not display popup nor print warning of key errors |
| Element or Error Element or None | **RETURN** | Return value can be: the Element that matches the supplied key if found; an Error Element if silent_on_error is False; None if silent_on_error True;

### element_list

Returns a list of all elements in the window

`element_list()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | List of all elements in the window and container elements in the window         |

### enable

Re-enables window to take user input after having it be Disabled previously

```python
enable()
```

### enable_debugger

Enables the internal debugger. By default, the debugger IS enabled

```python
enable_debugger()
```

### extend_layout

Adds new rows to an existing container element inside of this window

```
extend_layout(container, rows)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Frame or Column or Tab | container | The container Element the layout will be placed inside of |
| (List[List[Element]]) |   rows    | The layout to be added |
| (Window) | **RETURN** | (Window) self so could be chained

### fill

Fill in elements that are input fields with data based on a 'values dictionary'

```
fill(values_dict)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (Dict[Any, Any]) - {Element_key : value} | values_dict | pairs |
| (Window) | **RETURN** | returns self so can be chained with other methods

### finalize

Use this method to cause your layout to built into a real tkinter window.  In reality this method is like
Read(timeout=0).  It doesn't block and uses your layout to create tkinter widgets to represent the elements.
Lots of action!

`finalize()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Returns 'self' so that method "Chaining" can happen (read up about it as it's very cool!)         |

### find

Find element object associated with the provided key.
THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement:
element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way"
window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these:
FindElement == Element == Find
Rememeber that this call will return None if no match is found which may cause your code to crash if not
checked for.

```
find(key, silent_on_error = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or int or tuple or object |       key       | Used with window.FindElement and with return values to uniquely identify this element |
|            bool            | silent_on_error | If True do not display popup nor print warning of key errors |
| Element or Error Element or None | **RETURN** | Return value can be: the Element that matches the supplied key if found; an Error Element if silent_on_error is False; None if silent_on_error True;

### find_element

Find element object associated with the provided key.
THIS METHOD IS NO LONGER NEEDED to be called by the user

You can perform the same operation by writing this statement:
element = window[key]

You can drop the entire "FindElement" function name and use [ ] instead.

Typically used in combination with a call to element's Update method (or any other element method!):
window[key].Update(new_value)

Versus the "old way"
window.FindElement(key).Update(new_value)

This call can be abbreviated to any of these:
FindElement == Element == Find
Rememeber that this call will return None if no match is found which may cause your code to crash if not
checked for.

```
find_element(key, silent_on_error = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or int or tuple or object |       key       | Used with window.FindElement and with return values to uniquely identify this element |
|            bool            | silent_on_error | If True do not display popup nor print warning of key errors |
| Element or Error Element or None | **RETURN** | Return value can be: the Element that matches the supplied key if found; an Error Element if silent_on_error is False; None if silent_on_error True;

### find_element_with_focus

Returns the Element that currently has focus as reported by tkinter. If no element is found None is returned!

`find_element_with_focus()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | An Element if one has been found with focus or None if no element found         |

### force_focus

Forces this window to take focus

```python
force_focus()
```

### get_screen_dimensions

Get the screen dimensions.  NOTE - you must have a window already open for this to work (blame tkinter not me)

`get_screen_dimensions()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | Tuple containing width and height of screen in pixels         |

### get_screen_size

This is a "Class Method" meaning you call it by writing: width, height = Window.get_screen_size()
Returns the size of the "screen" as determined by tkinter.  This can vary depending on your operating system and the number of monitors installed on your system.  For Windows, the primary monitor's size is returns. On some multi-monitored Linux systems, the monitors are combined and the total size is reported as if one screen.

```
get_screen_size()
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (int, int) | **RETURN** | Size of the screen in pixels as determined by tkinter

### grab_any_where_off

Turns off Grab Anywhere functionality AFTER a window has been created.  Don't try on a window that's not yet
        been Finalized or Read.

```python
grab_any_where_off()
```

### grab_any_where_on

Turns on Grab Anywhere functionality AFTER a window has been created.  Don't try on a window that's not yet
        been Finalized or Read.

```python
grab_any_where_on()
```

### hide

Hides the window from the screen and the task bar

```python
hide()
```

### layout

Second of two preferred ways of telling a Window what its layout is. The other way is to pass the layout as
a parameter to Window object.  The parameter method is the currently preferred method. This call to Layout
has been removed from examples contained in documents and in the Demo Programs. Trying to remove this call
from history and replace with sending as a parameter to Window.

```
layout(rows)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[Elements]] | rows | Your entire layout |
| (Window) | **RETURN** | self so that you can chain method calls

### load_from_disk

Restore values from a previous call to SaveToDisk which saves the returned values dictionary in Pickle format

```
load_from_disk(filename)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | filename | Pickle Filename to load |

### make_modal

Makes a window into a "Modal Window"
        This means user will not be able to interact with other windows until this one is closed

```python
make_modal()
```

### maximize

Maximize the window. This is done differently on a windows system versus a linux or mac one.  For non-Windows
        the root attribute '-fullscreen' is set to True.  For Windows the "root" state is changed to "zoomed"
        The reason for the difference is the title bar is removed in some cases when using fullscreen option

```python
maximize()
```

### minimize

Minimize this window to the task bar

```python
minimize()
```

### move

Move the upper left corner of this window to the x,y coordinates provided

```
move(x, y)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int | x | x coordinate in pixels |
| int | y | y coordinate in pixels |

### normal

Restore a window to a non-maximized state.  Does different things depending on platform.  See Maximize for more.

```python
normal()
```

### read

THE biggest deal method in the Window class! This is how you get all of your data from your Window.
Pass in a timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key
if no other GUI events happen first.

```
read(timeout = None,
    timeout_key = "__TIMEOUT__",
    close = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int  |   timeout   | Milliseconds to wait until the Read will return IF no other GUI events happen first |
| Any  | timeout_key | The value that will be returned from the call if the timer expired |
| bool |    close    | if True the window will be closed prior to returning |
| Tuple[(Any), Dict[Any, Any], List[Any], None] | **RETURN** | (event, values)

### reappear

Causes a window previously made to "Disappear" (using that method). Does this by restoring the alpha channel

```python
reappear()
```

### refresh

Refreshes the window by calling tkroot.update().  Can sometimes get away with a refresh instead of a Read.
Use this call when you want something to appear in your Window immediately (as soon as this function is called).
Without this call your changes to a Window will not be visible to the user until the next Read call

`refresh()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | `self` so that method calls can be easily "chained"         |

### save_to_disk

Saves the values contained in each of the input areas of the form. Basically saves what would be returned from a call to Read.  It takes these results and saves them to disk using pickle.
 Note that every element in your layout that is to be saved must have a key assigned to it.

```
save_to_disk(filename)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | filename | Filename to save the values to in pickled form |

### send_to_back

Pushes this window to the bottom of the stack of windows. It is the opposite of BringToFront

```python
send_to_back()
```

### set_alpha

Sets the Alpha Channel for a window.  Values are between 0 and 1 where 0 is completely transparent

```
set_alpha(alpha)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| float | alpha | 0 to 1. 0 is completely transparent. 1 is completely visible and solid (can't see through) |

### set_icon

Changes the icon that is shown on the title bar and on the task bar.
NOTE - The file type is IMPORTANT and depends on the OS!
Can pass in:
* filename which must be a .ICO icon file for windows, PNG file for Linux
* bytes object
* BASE64 encoded file held in a variable

```
set_icon(icon = None, pngbase64 = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str |   icon    | Filename or bytes object |
| str | pngbase64 | Base64 encoded image |

### set_min_size

Changes the minimum size of the window. Note Window must be read or finalized first.

```
set_min_size(size)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] | size | (width, height) tuple (int, int) of the desired window size in pixels |

### set_title

Change the title of the window

```
set_title(title)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | title | The string to set the title to |

### set_transparent_color

Set the color that will be transparent in your window. Areas with this color will be SEE THROUGH.

```
set_transparent_color(color)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | color | Color string that defines the transparent color |

### size

#### property: size

Return the current size of the window in pixels

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | (width, height) of the window         |

### un_hide

Used to bring back a window that was previously hidden using the Hide method

```python
un_hide()
```

### visibility_changed

When making an element in a column or someplace that has a scrollbar, then you'll want to call this function
        prior to the column's contents_changed() method.

```python
visibility_changed()
```

### was_closed

Returns True if the window was closed

`was_closed()`

|Type|Name|Meaning|
|---|---|---|
|<type>| **return** | True if the window is closed         |

### write_event_value

Adds a key & value tuple to the queue that is used by threads to communicate with the window

```
write_event_value(key, value)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any |  key  | The key that will be returned as the event when reading the window |
| Any | value | The value that will be in the values dictionary |

## SystemTray 

    A "Simulated System Tray" that duplicates the API calls available to PySimpleGUIWx and PySimpleGUIQt users.

    All of the functionality works. The icon is displayed ABOVE the system tray rather than inside of it.

SystemTray - create an icon in the system tray

```
SystemTray(menu = None,
    filename = None,
    data = None,
    data_base64 = None,
    tooltip = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[List[List[str] or str]] |    menu     | Menu definition. Example - ['UNUSED', ['My', 'Simple', '---', 'Menu', 'Exit']] |
|             str              |  filename   | filename for icon |
|            bytes             |    data     | in-ram image for icon (same as data_base64 parm) |
|            bytes             | data_base64 | base-64 data for icon |
|             str              |   tooltip   | tooltip string |
|             Any              |  metadata   | User metadata that can be set to ANYTHING |

### Close

Close the system tray window

```python
Close()
```

### Hide

Hides the icon

```python
Hide()
```

### Read

Reads the context menu

```
Read(timeout = None)
```

### ShowMessage

Shows a balloon above icon in system tray

```
ShowMessage(title,
    message,
    filename = None,
    data = None,
    data_base64 = None,
    messageicon = None,
    time = (1000, 3000))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str          |    title    | Title shown in balloon |
|          str          |   message   | Message to be displayed |
|          str          |  filename   | Optional icon filename |
|          b''          |    data     | Optional in-ram icon |
|          b''          | data_base64 | Optional base64 icon |
| int or Tuple[int, int] |    time     | Amount of time to display message in milliseconds. If tuple, first item is fade in/out duration |
| Any | **RETURN** | The event that happened during the display such as user clicked on message

### UnHide

Restores a previously hidden icon

```python
UnHide()
```

### Update

Updates the menu, tooltip or icon

```
Update(menu = None,
    tooltip = None,
    filename = None,
    data = None,
    data_base64 = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| ??? |    menu     | menu defintion |
| ??? |   tooltip   | string representing tooltip |
| ??? |  filename   | icon filename |
| ??? |    data     | icon raw image |
| ??? | data_base64 | icon base 64 image |

### close

Close the system tray window

```python
close()
```

### hide

Hides the icon

```python
hide()
```

### notify

Displays a "notification window", usually in the bottom right corner of your display.  Has an icon, a title, and a message
The window will slowly fade in and out if desired.  Clicking on the window will cause it to move through the end the current "phase". For example, if the window was fading in and it was clicked, then it would immediately stop fading in and instead be fully visible.  It's a way for the user to quickly dismiss the window.

```
notify(title,
    message,
    icon = ...,
    display_duration_in_ms = 3000,
    fade_in_duration = 1000,
    alpha = 0.9,
    location = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|       str       |         title          | Text to be shown at the top of the window in a larger font |
|       str       |        message         | Text message that makes up the majority of the window |
|  bytes or str   |          icon          | A base64 encoded PNG/GIF image or PNG/GIF filename that will be displayed in the window |
|       int       | display_duration_in_ms | Number of milliseconds to show the window |
|       int       |    fade_in_duration    | Number of milliseconds to fade window in and out |
|      float      |         alpha          | Alpha channel. 0 - invisible 1 - fully visible |
| Tuple[int, int] |        location        | Location on the screen to display the window |
| (int) | **RETURN** | (int) reason for returning

### read

Reads the context menu

```
read(timeout = None)
```

### show_message

Shows a balloon above icon in system tray

```
show_message(title,
    message,
    filename = None,
    data = None,
    data_base64 = None,
    messageicon = None,
    time = (1000, 3000))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str          |    title    | Title shown in balloon |
|          str          |   message   | Message to be displayed |
|          str          |  filename   | Optional icon filename |
|          b''          |    data     | Optional in-ram icon |
|          b''          | data_base64 | Optional base64 icon |
| int or Tuple[int, int] |    time     | Amount of time to display message in milliseconds. If tuple, first item is fade in/out duration |
| Any | **RETURN** | The event that happened during the display such as user clicked on message

### un_hide

Restores a previously hidden icon

```python
un_hide()
```

### update

Updates the menu, tooltip or icon

```
update(menu = None,
    tooltip = None,
    filename = None,
    data = None,
    data_base64 = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| ??? |    menu     | menu defintion |
| ??? |   tooltip   | string representing tooltip |
| ??? |  filename   | icon filename |
| ??? |    data     | icon raw image |
| ??? | data_base64 | icon base 64 image |

## Function Reference

These are the functions available for you to call

## Multi-window Interface

Reads a list of windows.  If any of the list returns a value then the window and its event and values
are returned.

```
read_all_windows(timeout = None, timeout_key = "__TIMEOUT__")
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| int |   timeout   | Time in milliseconds to delay before a returning a timeout event |
| Any | timeout_key | Key to return when a timeout happens. Defaults to the standard TIMEOUT_KEY |
| Tuple[Window, Any, (Dict or List)] | **RETURN** | A tuple with the  (Window, event, values dictionary/list)

## Button Related

Button that will show a calendar chooser window.  Fills in the target element with result

```
CalendarButton(button_text,
    target = (555666777, -1),
    close_when_date_chosen = True,
    default_date_m_d_y = (None, None, None),
    image_filename = None,
    image_data = None,
    image_size = (None, None),
    image_subsample = None,
    tooltip = None,
    border_width = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    font = None,
    bind_return_key = False,
    focus = False,
    pad = None,
    enable_events = None,
    key = None,
    k = None,
    locale = None,
    format = "%Y-%m-%d %H:%M:%S",
    begin_at_sunday_plus = 0,
    month_names = None,
    day_abbreviations = None,
    title = "Choose Date",
    no_titlebar = True,
    location = (None, None),
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |      button_text       | text in the button |
|                            (int, int) or Any                             |         target         | Key or "coordinate" (see docs) of target element |
|                                   bool                                   | close_when_date_chosen | (Default = True) |
|                         (int, int or None, int)                          |   default_date_m_d_y   | Beginning date to show |
|                image filename if there is a button image                 |     image_filename     | image filename if there is a button image |
|                  in-RAM image to be displayed on button                  |       image_data       | in-RAM image to be displayed on button |
|                            (Default = (None))                            |       image_size       | image size (O.K.) |
|                  amount to reduce the size of the image                  |    image_subsample     | amount to reduce the size of the image |
|                                   str                                    |        tooltip         | text, that will appear when mouse hovers over the element |
|                      width of border around element                      |      border_width      | width of border around element |
|                                (int, int)                                |          size          | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   |    auto_size_button    | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |      button_color      | button color (foreground, background) |
|                                   bool                                   |        disabled        | set disable state for element (Default = False) |
|                          str or Tuple[str, int]                          |          font          | specifies the font family, size, etc |
|                                   bool                                   |    bind_return_key     | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
|                                   bool                                   |         focus          | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |          pad           | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |          key           | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |           k            | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   str                                    |         locale         | defines the locale used to get day names |
|                                   str                                    |         format         | formats result using this strftime format |
|                                List[str]                                 |      month_names       | optional list of month names to use (should be 12 items) |
|                                List[str]                                 |   day_abbreviations    | optional list of abbreviations to display as the day of week |
|                                   str                                    |         title          | Title shown on the date chooser window |
|                                   bool                                   |      no_titlebar       | if True no titlebar will be shown on the date chooser window |
|                                (int, int)                                |        location        | Location on the screen (x,y) to show the calendar popup window |
|                                   Any                                    |        metadata        | Anything you want to store along with this button |
| (Button) | **RETURN** | returns a button

```
Cancel(button_text = "Cancel",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    tooltip = None,
    font = None,
    bind_return_key = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Cancel') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |      focus       | if focus should be set to this :param pad: Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
ColorChooserButton(button_text,
    target = (None, None),
    image_filename = None,
    image_data = None,
    image_size = (None, None),
    image_subsample = None,
    tooltip = None,
    border_width = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    font = None,
    bind_return_key = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button |
|                          str or Tuple[int, int]                          |      target      | key or (row,col) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button |
|                                   str                                    |  image_filename  | image filename if there is a button image. GIFs and PNGs only. |
|                               bytes or str                               |    image_data    | Raw or Base64 representation of the image to put on button. Choose either filename or data |
|                                (int, int)                                |    image_size    | Size of the image in pixels (width, height) |
|                                   int                                    | image_subsample  | amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                   int                                    |   border_width   | width of border around element |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   | bind_return_key  | If True, then the return key will cause a the Listbox to generate an event |
|                                   bool                                   |      focus       | Determines if initial focus should go to this element. |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   Any                                    |     metadata     | User metadata that can be set to ANYTHING |
| (Button) | **RETURN** | returns a button

```
Debug(button_text = "",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    font = None,
    tooltip = None,
    bind_return_key = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = '') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |      focus       | if focus should be set to this :param pad: Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   Any                                    |     metadata     | Anything you want to store along with this button |
| (Button) | **RETURN** | returns a button

```
DummyButton(button_text,
    image_filename = None,
    image_data = None,
    image_size = (None, None),
    image_subsample = None,
    border_width = None,
    tooltip = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    font = None,
    disabled = False,
    bind_return_key = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button |
|                image filename if there is a button image                 |  image_filename  | image filename if there is a button image |
|                  in-RAM image to be displayed on button                  |    image_data    | in-RAM image to be displayed on button |
|                            (Default = (None))                            |    image_size    | image size (O.K.) |
|                  amount to reduce the size of the image                  | image_subsample  | amount to reduce the size of the image |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
|                                   bool                                   |      focus       | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   Any                                    |     metadata     | Anything you want to store along with this button |
|                                   int                                    |   border_width   | width of border around element |
| (Button) | **RETURN** | returns a button

```
Exit(button_text = "Exit",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    tooltip = None,
    font = None,
    bind_return_key = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Exit') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |      focus       | if focus should be set to this :param pad: Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
FileBrowse(button_text = "Browse",
    target = (555666777, -1),
    file_types = (('ALL Files', '*.*'),),
    initial_folder = None,
    tooltip = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    change_submits = False,
    enable_events = False,
    font = None,
    disabled = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Browse') |
|                       Tuple[Tuple[str, str], ...]                        |      target      | key or (row,col) target for the button (Default value = (ThisRow, -1)) :param file_types: filter file types (Default value = (("ALL Files", "*.*"))) |
|                                   str                                    |  initial_folder  | starting path for folders and files :param tooltip: text, that will appear when mouse hovers over the element |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |  change_submits  | If True, pressing Enter key submits window (Default = False) |
|                                   bool                                   |  enable_events   | Turns on the element specific events.(Default = False) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
FileSaveAs(button_text = "Save As...",
    target = (555666777, -1),
    file_types = (('ALL Files', '*.*'),),
    initial_folder = None,
    default_extension = "",
    disabled = False,
    tooltip = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    change_submits = False,
    enable_events = False,
    font = None,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |    button_text    | text in the button (Default value = 'Save As...') |
|                       Tuple[Tuple[str, str], ...]                        |      target       | key or (row,col) target for the button (Default value = (ThisRow, -1)) :param file_types: (Default value = (("ALL Files", "*.*"))) |
|                                   str                                    | default_extension | If no extension entered by user, add this to filename (only used in saveas dialogs) |
|                                   str                                    |  initial_folder   | starting path for folders and files |
|                                   bool                                   |     disabled      | set disable state for element (Default = False) |
|                                   str                                    |      tooltip      | text, that will appear when mouse hovers over the element |
|                                (int, int)                                |       size        | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button  | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color    | button color (foreground, background) |
|                                   bool                                   |  change_submits   | If True, pressing Enter key submits window (Default = False) |
|                                   bool                                   |   enable_events   | Turns on the element specific events.(Default = False) |
|                          str or Tuple[str, int]                          |       font        | specifies the font family, size, etc |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |        pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |        key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |         k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

Allows browsing of multiple files. File list is returned as a single list with the delimeter defined using the variable
BROWSE_FILES_DELIMETER.  This defaults to ';' but is changable by the user

```
FilesBrowse(button_text = "Browse",
    target = (555666777, -1),
    file_types = (('ALL Files', '*.*'),),
    disabled = False,
    initial_folder = None,
    tooltip = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    change_submits = False,
    enable_events = False,
    font = None,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Browse') |
|                       Tuple[Tuple[str, str], ...]                        |      target      | key or (row,col) target for the button (Default value = (ThisRow, -1)) :param file_types: (Default value = (("ALL Files", "*.*"))) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   str                                    |  initial_folder  | starting path for folders and files |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |  change_submits  | If True, pressing Enter key submits window (Default = False) |
|                                   bool                                   |  enable_events   | Turns on the element specific events.(Default = False) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
FolderBrowse(button_text = "Browse",
    target = (555666777, -1),
    initial_folder = None,
    tooltip = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    change_submits = False,
    enable_events = False,
    font = None,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Browse') |
|                             key or (row,col)                             |      target      | target for the button (Default value = (ThisRow, -1)) |
|                                   str                                    |  initial_folder  | starting path for folders and files |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                                   bool                                   |   button_color   | button color (foreground, background) :param disabled: set disable state for element (Default = False) |
|                                   bool                                   |  change_submits  | If True, pressing Enter key submits window (Default = False) |
|                                   bool                                   |  enable_events   | Turns on the element specific events.(Default = False) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element |
|                      str or int or tuple or object                       |       key        | Used with window.FindElement and with return values to uniquely identify this element |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | The Button created

```
Help(button_text = "Help",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    font = None,
    tooltip = None,
    bind_return_key = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Help') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |      focus       | if focus should be set to this :param pad: Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
No(button_text = "No",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    tooltip = None,
    font = None,
    bind_return_key = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'No') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |      focus       | if focus should be set to this :param pad: Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
OK(button_text = "OK",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    bind_return_key = True,
    tooltip = None,
    font = None,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'OK') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   bool                                   | bind_return_key  | (Default = True) If True, then the return key will cause a the Listbox to generate an event |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                              idk_yetReally                               |      focus       | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

Dumps an Object's values as a formatted string.  Very nicely done. Great way to display an object's member variables in human form

```
ObjToString(obj, extra = "    ")
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any |  obj  | The object to display |
| str | extra | extra stuff (Default value = ' ') |
| (str) | **RETURN** | Formatted output of the object's values

Dumps an Object's values as a formatted string.  Very nicely done. Great way to display an object's member variables in human form
Returns only the top-most object's variables instead of drilling down to dispolay more

```
ObjToStringSingleObj(obj)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any | obj | The object to display |
| (str) | **RETURN** | Formatted output of the object's values

```
Ok(button_text = "Ok",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    bind_return_key = True,
    tooltip = None,
    font = None,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Ok') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   bool                                   | bind_return_key  | (Default = True) If True, then the return key will cause a the Listbox to generate an event |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                              idk_yetReally                               |      focus       | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
Open(button_text = "Open",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    bind_return_key = True,
    tooltip = None,
    font = None,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Open') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   bool                                   | bind_return_key  | (Default = True) If True, then the return key will cause a the Listbox to generate an event |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                              idk_yetReally                               |      focus       | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
Quit(button_text = "Quit",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    tooltip = None,
    font = None,
    bind_return_key = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Quit') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |      focus       | if focus should be set to this :param pad: Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
RealtimeButton(button_text,
    image_filename = None,
    image_data = None,
    image_size = (None, None),
    image_subsample = None,
    border_width = None,
    tooltip = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    font = None,
    disabled = False,
    bind_return_key = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button |
|                image filename if there is a button image                 |  image_filename  | image filename if there is a button image |
|                  in-RAM image to be displayed on button                  |    image_data    | in-RAM image to be displayed on button |
|                            (Default = (None))                            |    image_size    | image size (O.K.) |
|                  amount to reduce the size of the image                  | image_subsample  | amount to reduce the size of the image |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
|                                   bool                                   |      focus       | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   int                                    |   border_width   | width of border around element |
|                                   Any                                    |     metadata     | Anything you want to store along with this button |
| (Button) | **RETURN** | Button created

```
Save(button_text = "Save",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    bind_return_key = True,
    disabled = False,
    tooltip = None,
    font = None,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Save') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   | bind_return_key  | (Default = True) If True, then the return key will cause a the Listbox to generate an event |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                              idk_yetReally                               |      focus       | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
SaveAs(button_text = "Save As...",
    target = (555666777, -1),
    file_types = (('ALL Files', '*.*'),),
    initial_folder = None,
    default_extension = "",
    disabled = False,
    tooltip = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    change_submits = False,
    enable_events = False,
    font = None,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |    button_text    | text in the button (Default value = 'Save As...') |
|                       Tuple[Tuple[str, str], ...]                        |      target       | key or (row,col) target for the button (Default value = (ThisRow, -1)) :param file_types: (Default value = (("ALL Files", "*.*"))) |
|                                   str                                    | default_extension | If no extension entered by user, add this to filename (only used in saveas dialogs) |
|                                   str                                    |  initial_folder   | starting path for folders and files |
|                                   bool                                   |     disabled      | set disable state for element (Default = False) |
|                                   str                                    |      tooltip      | text, that will appear when mouse hovers over the element |
|                                (int, int)                                |       size        | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button  | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color    | button color (foreground, background) |
|                                   bool                                   |  change_submits   | If True, pressing Enter key submits window (Default = False) |
|                                   bool                                   |   enable_events   | Turns on the element specific events.(Default = False) |
|                          str or Tuple[str, int]                          |       font        | specifies the font family, size, etc |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |        pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |        key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |         k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
Submit(button_text = "Submit",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    bind_return_key = True,
    tooltip = None,
    font = None,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Submit') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   bool                                   | bind_return_key  | (Default = True) If True, then the return key will cause a the Listbox to generate an event |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                              idk_yetReally                               |      focus       | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
Yes(button_text = "Yes",
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    disabled = False,
    tooltip = None,
    font = None,
    bind_return_key = True,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button (Default value = 'Yes') |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   | bind_return_key  | (Default = True) If True, then the return key will cause a the Listbox to generate an event |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |      focus       | if focus should be set to this :param pad: Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

## Button No Longer To Be Used

Note - These are no longer recommended! 
They are shown here in case you run into them in some old code.

```
RButton(button_text,
    image_filename = None,
    image_data = None,
    image_size = (None, None),
    image_subsample = None,
    border_width = None,
    tooltip = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    font = None,
    bind_return_key = False,
    disabled = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button |
|                image filename if there is a button image                 |  image_filename  | image filename if there is a button image |
|                  in-RAM image to be displayed on button                  |    image_data    | in-RAM image to be displayed on button |
|                            (Default = (None))                            |    image_size    | image size (O.K.) |
|                  amount to reduce the size of the image                  | image_subsample  | amount to reduce the size of the image |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                              idk_yetReally                               |      focus       | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   int                                    |   border_width   | width of border around element |
|                                   Any                                    |     metadata     | Anything you want to store along with this button |
| (Button) | **RETURN** | Button created

```
ReadButton(button_text,
    image_filename = None,
    image_data = None,
    image_size = (None, None),
    image_subsample = None,
    border_width = None,
    tooltip = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    font = None,
    bind_return_key = False,
    disabled = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button |
|                image filename if there is a button image                 |  image_filename  | image filename if there is a button image |
|                  in-RAM image to be displayed on button                  |    image_data    | in-RAM image to be displayed on button |
|                            (Default = (None))                            |    image_size    | image size (O.K.) |
|                  amount to reduce the size of the image                  | image_subsample  | amount to reduce the size of the image |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                              idk_yetReally                               |      focus       | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
|                                   int                                    |   border_width   | width of border around element |
|                                   Any                                    |     metadata     | Anything you want to store along with this button |
| (Button) | **RETURN** | Button created

```
CButton(button_text,
    image_filename = None,
    image_data = None,
    image_size = (None, None),
    image_subsample = None,
    border_width = None,
    tooltip = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    font = None,
    bind_return_key = False,
    disabled = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button |
|                image filename if there is a button image                 |  image_filename  | image filename if there is a button image |
|                  in-RAM image to be displayed on button                  |    image_data    | in-RAM image to be displayed on button |
|                            (Default = (None))                            |    image_size    | image size (O.K.) |
|                  amount to reduce the size of the image                  | image_subsample  | amount to reduce the size of the image |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                              idk_yetReally                               |      focus       | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

```
CloseButton(button_text,
    image_filename = None,
    image_data = None,
    image_size = (None, None),
    image_subsample = None,
    border_width = None,
    tooltip = None,
    size = (None, None),
    auto_size_button = None,
    button_color = None,
    font = None,
    bind_return_key = False,
    disabled = False,
    focus = False,
    pad = None,
    key = None,
    k = None,
    metadata = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                                   str                                    |   button_text    | text in the button |
|                image filename if there is a button image                 |  image_filename  | image filename if there is a button image |
|                  in-RAM image to be displayed on button                  |    image_data    | in-RAM image to be displayed on button |
|                            (Default = (None))                            |    image_size    | image size (O.K.) |
|                  amount to reduce the size of the image                  | image_subsample  | amount to reduce the size of the image |
|                                   str                                    |     tooltip      | text, that will appear when mouse hovers over the element |
|                                (int, int)                                |       size       | (w,h) w=characters-wide, h=rows-high |
|                                   bool                                   | auto_size_button | True if button size is determined by button text |
|                          Tuple[str, str] or str                          |   button_color   | button color (foreground, background) |
|                          str or Tuple[str, int]                          |       font       | specifies the font family, size, etc |
|                                   bool                                   | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
|                                   bool                                   |     disabled     | set disable state for element (Default = False) |
|                              idk_yetReally                               |      focus       | if focus should be set to this |
| (int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int) |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
|                      str or int or tuple or object                       |       key        | key for uniquely identify this element (for window.FindElement) |
|                      str or int or tuple or object                       |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| (Button) | **RETURN** | returns a button

## Debug Window Output

Works like a "print" statement but with windowing options.  Routes output to the "Debug Window"

```
easy_print(args=*<1 or N object>,
    size = (None, None),
    end = None,
    sep = None,
    location = (None, None),
    font = None,
    no_titlebar = False,
    no_button = False,
    grab_anywhere = False,
    keep_on_top = False,
    do_not_reroute_stdout = True,
    text_color = None,
    background_color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any          |         *args         | stuff to output |
|      (int, int)       |         size          | (w,h) w=characters-wide, h=rows-high |
|          str          |          end          | end character |
|          str          |          sep          | separator character |
|    Tuple[int, int]    |       location        | Location of upper left corner of the window |
| str or Tuple[str, int] |         font          | specifies the font family, size, etc |
|         bool          |      no_titlebar      | If True no titlebar will be shown |
|         bool          |       no_button       | don't show button |
|         bool          |     grab_anywhere     | If True: can grab anywhere to move the window (Default = False) |
|          str          |   background_color    | color of background |
|          str          |      text_color       | color of the text |
|         bool          |      keep_on_top      | If True the window will remain above all current windows |
|    Tuple[int, int]    |       location        | Location of upper left corner of the window |
|         bool          | do_not_reroute_stdout | do not reroute stdout |

Close a previously opened EasyPrint window

```
easy_print_close()
```

Works like a "print" statement but with windowing options.  Routes output to the "Debug Window"

```
eprint(args=*<1 or N object>,
    size = (None, None),
    end = None,
    sep = None,
    location = (None, None),
    font = None,
    no_titlebar = False,
    no_button = False,
    grab_anywhere = False,
    keep_on_top = False,
    do_not_reroute_stdout = True,
    text_color = None,
    background_color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any          |         *args         | stuff to output |
|      (int, int)       |         size          | (w,h) w=characters-wide, h=rows-high |
|          str          |          end          | end character |
|          str          |          sep          | separator character |
|    Tuple[int, int]    |       location        | Location of upper left corner of the window |
| str or Tuple[str, int] |         font          | specifies the font family, size, etc |
|         bool          |      no_titlebar      | If True no titlebar will be shown |
|         bool          |       no_button       | don't show button |
|         bool          |     grab_anywhere     | If True: can grab anywhere to move the window (Default = False) |
|          str          |   background_color    | color of background |
|          str          |      text_color       | color of the text |
|         bool          |      keep_on_top      | If True the window will remain above all current windows |
|    Tuple[int, int]    |       location        | Location of upper left corner of the window |
|         bool          | do_not_reroute_stdout | do not reroute stdout |

Works like a "print" statement but with windowing options.  Routes output to the "Debug Window"

```
sgprint(args=*<1 or N object>,
    size = (None, None),
    end = None,
    sep = None,
    location = (None, None),
    font = None,
    no_titlebar = False,
    no_button = False,
    grab_anywhere = False,
    keep_on_top = False,
    do_not_reroute_stdout = True,
    text_color = None,
    background_color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any          |         *args         | stuff to output |
|      (int, int)       |         size          | (w,h) w=characters-wide, h=rows-high |
|          str          |          end          | end character |
|          str          |          sep          | separator character |
|    Tuple[int, int]    |       location        | Location of upper left corner of the window |
| str or Tuple[str, int] |         font          | specifies the font family, size, etc |
|         bool          |      no_titlebar      | If True no titlebar will be shown |
|         bool          |       no_button       | don't show button |
|         bool          |     grab_anywhere     | If True: can grab anywhere to move the window (Default = False) |
|          str          |   background_color    | color of background |
|          str          |      text_color       | color of the text |
|         bool          |      keep_on_top      | If True the window will remain above all current windows |
|    Tuple[int, int]    |       location        | Location of upper left corner of the window |
|         bool          | do_not_reroute_stdout | do not reroute stdout |

Close a previously opened EasyPrint window

```
sgprint_close()
```

Works like a "print" statement but with windowing options.  Routes output to the "Debug Window"

```
EasyPrint(args=*<1 or N object>,
    size = (None, None),
    end = None,
    sep = None,
    location = (None, None),
    font = None,
    no_titlebar = False,
    no_button = False,
    grab_anywhere = False,
    keep_on_top = False,
    do_not_reroute_stdout = True,
    text_color = None,
    background_color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any          |         *args         | stuff to output |
|      (int, int)       |         size          | (w,h) w=characters-wide, h=rows-high |
|          str          |          end          | end character |
|          str          |          sep          | separator character |
|    Tuple[int, int]    |       location        | Location of upper left corner of the window |
| str or Tuple[str, int] |         font          | specifies the font family, size, etc |
|         bool          |      no_titlebar      | If True no titlebar will be shown |
|         bool          |       no_button       | don't show button |
|         bool          |     grab_anywhere     | If True: can grab anywhere to move the window (Default = False) |
|          str          |   background_color    | color of background |
|          str          |      text_color       | color of the text |
|         bool          |      keep_on_top      | If True the window will remain above all current windows |
|    Tuple[int, int]    |       location        | Location of upper left corner of the window |
|         bool          | do_not_reroute_stdout | do not reroute stdout |

Close a previously opened EasyPrint window

```
EasyPrintClose()
```

Works like a "print" statement but with windowing options.  Routes output to the "Debug Window"

```
Print(args=*<1 or N object>,
    size = (None, None),
    end = None,
    sep = None,
    location = (None, None),
    font = None,
    no_titlebar = False,
    no_button = False,
    grab_anywhere = False,
    keep_on_top = False,
    do_not_reroute_stdout = True,
    text_color = None,
    background_color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any          |         *args         | stuff to output |
|      (int, int)       |         size          | (w,h) w=characters-wide, h=rows-high |
|          str          |          end          | end character |
|          str          |          sep          | separator character |
|    Tuple[int, int]    |       location        | Location of upper left corner of the window |
| str or Tuple[str, int] |         font          | specifies the font family, size, etc |
|         bool          |      no_titlebar      | If True no titlebar will be shown |
|         bool          |       no_button       | don't show button |
|         bool          |     grab_anywhere     | If True: can grab anywhere to move the window (Default = False) |
|          str          |   background_color    | color of background |
|          str          |      text_color       | color of the text |
|         bool          |      keep_on_top      | If True the window will remain above all current windows |
|    Tuple[int, int]    |       location        | Location of upper left corner of the window |
|         bool          | do_not_reroute_stdout | do not reroute stdout |

Close a previously opened EasyPrint window

```
PrintClose()
```

## Color Printing to Multiline Element of a Window

Color print to a multiline element in a window of your choice.
Must have EITHER called cprint_set_output_destination prior to making this call so that the
window and element key can be saved and used here to route the output, OR used the window
and key parameters to the cprint function to specicy these items.

args is a variable number of things you want to print.

end - The end char to use just like print uses
sep - The separation character like print uses
text_color - The color of the text
key - overrides the previously defined Multiline key
window - overrides the previously defined window to output to
background_color - The color of the background
colors -(str, str) or str.  A combined text/background color definition in a single parameter

There are also "aliases" for text_color, background_color and colors (t, b, c)
t - An alias for color of the text (makes for shorter calls)
b - An alias for the background_color parameter
c - Tuple[str, str] - "shorthand" way of specifying color. (foreground, backgrouned)
c - str - can also be a string of the format "foreground on background"  ("white on red")

With the aliases it's possible to write the same print but in more compact ways:
cprint('This will print white text on red background', c=('white', 'red'))
cprint('This will print white text on red background', c='white on red')
cprint('This will print white text on red background', text_color='white', background_color='red')
cprint('This will print white text on red background', t='white', b='red')

```
cprint(args=*<1 or N object>,
    end = None,
    sep = " ",
    text_color = None,
    t = None,
    background_color = None,
    b = None,
    colors = None,
    c = None,
    window = None,
    key = None,
    justification = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|           Any           |      *args       | stuff to output |
|           str           |    text_color    | Color of the text |
|           str           | background_color | The background color of the line |
| str) or Tuple[str, str] |      colors      | Either a tuple or a string that has both the text and background colors |
|           str           |        t         | Color of the text |
|           str           |        b         | The background color of the line |
| str) or Tuple[str, str] |        c         | Either a tuple or a string that has both the text and background colors |
|           str           |       end        | end character |
|           str           |       sep        | separator character |
|           Any           |       key        | key of multiline to output to (if you want to override the one previously set) |
|           str           |      window      | Window containing the multiline to output to (if you want to override the one previously set) :param justification: text justification. left, right, center. Can use single characters l, r, c. Sets only for this value, not entire element |
| None | **RETURN** | None

Sets up the color print (cprint) output destination

```
cprint_set_output_destination(window, multiline_key)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Window |    window     | The window that the cprint call will route the output to |
|  Any   | multiline_key | Key for the Multiline Element where output will be sent |
| None | **RETURN** | None

## OneLineProgressMeter

```
OneLineProgressMeter(title,
    current_value,
    max_value,
    key = "OK for 1 meter",
    args=*<1 or N object>,
    orientation = "v",
    bar_color = (None, None),
    button_color = None,
    size = (20, 20),
    border_width = None,
    grab_anywhere = False,
    no_titlebar = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|            str             |     title     | text to display in eleemnt |
|            int             | current_value | current value |
|            int             |   max_value   | max value of QuickMeter |
| str or int or tuple or object |      key      | Used to differentiate between mutliple meters. Used to cancel meter early. Now optional as there is a default value for single meters |
|            Any             |     *args     | stuff to output |
|            str             |  orientation  | 'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical' / 'v') |
|      Tuple(str, str)       |   bar_color   | color of a bar line |
|   Tuple[str, str] or str   | button_color  | button color (foreground, background) |
|         (int, int)         |     size      | (w,h) w=characters-wide, h=rows-high (Default value = DEFAULT_PROGRESS_BAR_SIZE) |
|            int             | border_width  | width of border around element |
|            bool            | grab_anywhere | If True: can grab anywhere to move the window (Default = False) |
|            bool            |  no_titlebar  | If True: no titlebar will be shown on the window |
| (bool) | **RETURN** | True if updated successfully. False if user closed the meter with the X or Cancel button

Cancels and closes a previously created One Line Progress Meter window

```
OneLineProgressMeterCancel(key = "OK for 1 meter")
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any | key | Key used when meter was created |
| None | **RETURN** | None

```
one_line_progress_meter(title,
    current_value,
    max_value,
    key = "OK for 1 meter",
    args=*<1 or N object>,
    orientation = "v",
    bar_color = (None, None),
    button_color = None,
    size = (20, 20),
    border_width = None,
    grab_anywhere = False,
    no_titlebar = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|            str             |     title     | text to display in eleemnt |
|            int             | current_value | current value |
|            int             |   max_value   | max value of QuickMeter |
| str or int or tuple or object |      key      | Used to differentiate between mutliple meters. Used to cancel meter early. Now optional as there is a default value for single meters |
|            Any             |     *args     | stuff to output |
|            str             |  orientation  | 'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical' / 'v') |
|      Tuple(str, str)       |   bar_color   | color of a bar line |
|   Tuple[str, str] or str   | button_color  | button color (foreground, background) |
|         (int, int)         |     size      | (w,h) w=characters-wide, h=rows-high (Default value = DEFAULT_PROGRESS_BAR_SIZE) |
|            int             | border_width  | width of border around element |
|            bool            | grab_anywhere | If True: can grab anywhere to move the window (Default = False) |
|            bool            |  no_titlebar  | If True: no titlebar will be shown on the window |
| (bool) | **RETURN** | True if updated successfully. False if user closed the meter with the X or Cancel button

Cancels and closes a previously created One Line Progress Meter window

```
one_line_progress_meter_cancel(key = "OK for 1 meter")
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any | key | Key used when meter was created |
| None | **RETURN** | None

## Popup Functions

Popup - Display a popup Window with as many parms as you wish to include.  This is the GUI equivalent of the
"print" statement.  It's also great for "pausing" your program's flow until the user can read some error messages.

```
Popup(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    button_type = 0,
    auto_close = False,
    auto_close_duration = None,
    custom_text = (None, None),
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    any_key_closes = False,
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                   Any                   |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
|                   str                   |        title        | Optional title for the window. If none provided, the first arg will be used instead. |
|         Tuple[str, str] or None         |    button_color     | Color of the buttons shown (text color, button color) |
|                   str                   |  background_color   | Window's background color |
|                   str                   |     text_color      | text color |
|                   int                   |     button_type     | NOT USER SET! Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). There are many Popup functions and they call Popup, changing this parameter to get the desired effect. |
|                  bool                   |     auto_close      | If True the window will automatically close |
|                   int                   | auto_close_duration | time in seconds to keep window open before closing it automatically |
|         Tuple[str, str] or str          |     custom_text     | A string or pair of strings that contain the text to display on the buttons |
|                  bool                   |    non_blocking     | If True then will immediately return from the function without waiting for the user's input. |
|              str or bytes               |        icon         | icon to display on the window. Same format as a Window call |
|                   int                   |     line_width      | Width of lines in characters. Defaults to MESSAGE_BOX_LINE_WIDTH |
| str or Tuple[font_name, size, modifiers] |        font         | specifies the font family, size, etc |
|                  bool                   |     no_titlebar     | If True will not show the frame around the window and the titlebar across the top |
|                  bool                   |    grab_anywhere    | If True can grab anywhere to move the window. If no_titlebar is True, grab_anywhere should likely be enabled too |
|             Tuple[int, int]             |      location       | Location on screen to display the top left corner of window. Defaults to window centered on screen |
|                  bool                   |     keep_on_top     | If True the window will remain above all current windows |
|                  bool                   |   any_key_closes    | If True then will turn on return_keyboard_events for the window which will cause window to close as soon as any key is pressed. Normally the return key only will close the window. Default is false. |
|              str or bytes               |        image        | Image to include at the top of the popup window |
|                  bool                   |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Show animation one frame at a time.  This function has its own internal clocking meaning you can call it at any frequency
 and the rate the frames of video is shown remains constant.  Maybe your frames update every 30 ms but your
 event loop is running every 10 ms.  You don't have to worry about delaying, just call it every time through the
 loop.

```
PopupAnimated(image_source,
    message = None,
    background_color = None,
    text_color = None,
    font = None,
    no_titlebar = True,
    grab_anywhere = True,
    keep_on_top = True,
    location = (None, None),
    alpha_channel = None,
    time_between_frames = 0,
    transparent_color = None,
    title = "",
    icon = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or bytes |    image_source     | Either a filename or a base64 string. |
|     str     |       message       | An optional message to be shown with the animation |
|     str     |  background_color   | color of background |
|     str     |     text_color      | color of the text |
| str or tuple |        font         | specifies the font family, size, etc |
|    bool     |     no_titlebar     | If True then the titlebar and window frame will not be shown |
|    bool     |    grab_anywhere    | If True then you can move the window just clicking anywhere on window, hold and drag |
|    bool     |     keep_on_top     | If True then Window will remain on top of all other windows currently shownn |
| (int, int)  |      location       | (x,y) location on the screen to place the top left corner of your window. Default is to center on screen |
|    float    |    alpha_channel    | Window transparency 0 = invisible 1 = completely visible. Values between are see through |
|     int     | time_between_frames | Amount of time in milliseconds between each frame |
|     str     |  transparent_color  | This color will be completely see-through in your window. Can even click through |
|     str     |        title        | Title that will be shown on the window |
|     str     |        icon         | Same as Window icon parameter. Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO |
| None | **RETURN** | No return value

Display a Popup without a titlebar.   Enables grab anywhere so you can move it

```
PopupAnnoying(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    grab_anywhere = True,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Popup that closes itself after some time period

```
PopupAutoClose(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = True,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display Popup with "cancelled" button text

```
PopupCancel(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Popup with colored button and 'Error' as button text

```
PopupError(args=*<1 or N object>,
    title = None,
    button_color = (None, None),
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display popup window with text entry field and browse button so that a file can be chosen by user.

```
PopupGetFile(message,
    title = None,
    default_path = "",
    default_extension = "",
    save_as = False,
    multiple_files = False,
    file_types = (('ALL Files', '*.*'),),
    no_window = False,
    size = (None, None),
    button_color = None,
    background_color = None,
    text_color = None,
    icon = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    initial_folder = None,
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str           |      message      | message displayed to user |
|          str           |       title       | Window title |
|          str           |   default_path    | path to display to user as starting point (filled into the input field) |
|          str           | default_extension | If no extension entered by user, add this to filename (only used in saveas dialogs) |
|          bool          |      save_as      | if True, the "save as" dialog is shown which will verify before overwriting |
|          bool          |  multiple_files   | if True, then allows multiple files to be selected that are returned with ';' between each filename |
| Tuple[Tuple[str,str]]  |    file_types     | List of extensions to show using wildcards. All files (the default) = (("ALL Files", "*.*"),) |
|          bool          |     no_window     | if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown |
|       (int, int)       |       size        | (width, height) of the InputText Element |
| Tuple[str, str] or str |   button_color    | Color of the button (text, background) |
|          str           | background_color  | background color of the entire window |
|          str           |    text_color     | color of the text |
|      bytes or str      |       icon        | filename or base64 string to be used for the window's icon |
| str or Tuple[str, int] |       font        | specifies the font family, size, etc |
|          bool          |    no_titlebar    | If True no titlebar will be shown |
|          bool          |   grab_anywhere   | If True: can grab anywhere to move the window (Default = False) |
|          bool          |    keep_on_top    | If True the window will remain above all current windows |
|    Tuple[int, int]     |     location      | Location of upper left corner of the window |
|          str           |  initial_folder   | location in filesystem to begin browsing |
|      str or bytes      |       image       | Image to include at the top of the popup window |
|          bool          |       modal       | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None | **RETURN** | string representing the file(s) chosen, None if cancelled or window closed with X

Display popup with text entry field and browse button so that a folder can be chosen.

```
PopupGetFolder(message,
    title = None,
    default_path = "",
    no_window = False,
    size = (None, None),
    button_color = None,
    background_color = None,
    text_color = None,
    icon = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    initial_folder = None,
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str           |     message      | message displayed to user |
|          str           |      title       | Window title |
|          str           |   default_path   | path to display to user as starting point (filled into the input field) |
|          bool          |    no_window     | if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown |
|       (int, int)       |       size       | (width, height) of the InputText Element |
| Tuple[str, str] or str |   button_color   | button color (foreground, background) |
|          str           | background_color | color of background |
|          str           |    text_color    | color of the text |
|      bytes or str      |       icon       | filename or base64 string to be used for the window's icon |
| str or Tuple[str, int] |       font       | specifies the font family, size, etc |
|          bool          |   no_titlebar    | If True no titlebar will be shown |
|          bool          |  grab_anywhere   | If True: can grab anywhere to move the window (Default = False) |
|          bool          |   keep_on_top    | If True the window will remain above all current windows |
|    Tuple[int, int]     |     location     | Location of upper left corner of the window |
|          str           |  initial_folder  | location in filesystem to begin browsing |
|      str or bytes      |      image       | Image to include at the top of the popup window |
|          bool          |      modal       | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None | **RETURN** | string representing the path chosen, None if cancelled or window closed with X

Display Popup with text entry field. Returns the text entered or None if closed / cancelled

```
PopupGetText(message,
    title = None,
    default_text = "",
    password_char = "",
    size = (None, None),
    button_color = None,
    background_color = None,
    text_color = None,
    icon = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str           |     message      | message displayed to user |
|          str           |      title       | Window title |
|          str           |   default_text   | default value to put into input area |
|          str           |  password_char   | character to be shown instead of actually typed characters |
|       (int, int)       |       size       | (width, height) of the InputText Element |
| Tuple[str, str] or str |   button_color   | Color of the button (text, background) |
|          str           | background_color | background color of the entire window |
|          str           |    text_color    | color of the message text |
|      bytes or str      |       icon       | filename or base64 string to be used for the window's icon |
| str or Tuple[str, int] |       font       | specifies the font family, size, etc |
|          bool          |   no_titlebar    | If True no titlebar will be shown |
|          bool          |  grab_anywhere   | If True can click and drag anywhere in the window to move the window |
|          bool          |   keep_on_top    | If True the window will remain above all current windows |
|    Tuple[int, int]     |     location     | (x,y) Location on screen to display the upper left corner of window |
|      str or bytes      |      image       | Image to include at the top of the popup window |
|          bool          |      modal       | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None | **RETURN** | Text entered or None if window was closed or cancel button clicked

Display a Popup without a titlebar.   Enables grab anywhere so you can move it

```
PopupNoBorder(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    grab_anywhere = True,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Show a Popup but without any buttons

```
PopupNoButtons(args=*<1 or N object>,
    title = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any          |        *args        | Variable number of items to display |
|          str          |        title        | Title to display in the window. |
|          str          |  background_color   | color of background |
|          str          |     text_color      | color of the text |
|         bool          |     auto_close      | if True window will close itself |
|     int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|         bool          |    non_blocking     | If True then will immediately return from the function without waiting for the user's input. (Default = False) |
|     bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int          |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|         bool          |     no_titlebar     | If True no titlebar will be shown |
|         bool          |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
|    Tuple[int, int]    |      location       | Location of upper left corner of the window |
|     str or bytes      |        image        | Image to include at the top of the popup window |
|         bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display a Popup without a titlebar.   Enables grab anywhere so you can move it

```
PopupNoFrame(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    grab_anywhere = True,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display a Popup without a titlebar.   Enables grab anywhere so you can move it

```
PopupNoTitlebar(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    grab_anywhere = True,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Show Popup window and immediately return (does not block)

```
PopupNoWait(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = True,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = False |
| str or None | **RETURN** | Reason for popup closing

Show Popup window and immediately return (does not block)

```
PopupNonBlocking(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = True,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = False |
| str or None | **RETURN** | Reason for popup closing

Display Popup with OK button only

```
PopupOK(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display popup with OK and Cancel buttons

```
PopupOKCancel(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = ...,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| "OK" or "Cancel" or None | **RETURN** | clicked button

Show Popup box that doesn't block and closes itself

```
PopupQuick(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = True,
    auto_close_duration = 2,
    non_blocking = True,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = False |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Show Popup window with no titlebar, doesn't block, and auto closes itself.

```
PopupQuickMessage(args=*<1 or N object>,
    title = None,
    button_type = 5,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = True,
    auto_close_duration = 2,
    non_blocking = True,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = True,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = False |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Show a scrolled Popup window containing the user's text that was supplied.  Use with as many items to print as you
want, just like a print statement.

```
PopupScrolled(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    yes_no = False,
    auto_close = False,
    auto_close_duration = None,
    size = (None, None),
    location = (None, None),
    non_blocking = False,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    font = None,
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          bool          |       yes_no        | If True, displays Yes and No buttons instead of Ok |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|       (int, int)       |        size         | (w,h) w=characters-wide, h=rows-high |
|    Tuple[int, int]     |      location       | Location on the screen to place the upper left corner of the window |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Popup that closes itself after some time period

```
PopupTimed(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = True,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display Popup with Yes and No buttons

```
PopupYesNo(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| "Yes" or "No" or None | **RETURN** | clicked button

## Popups PEP8 Versions

Popup - Display a popup Window with as many parms as you wish to include.  This is the GUI equivalent of the
"print" statement.  It's also great for "pausing" your program's flow until the user can read some error messages.

```
popup(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    button_type = 0,
    auto_close = False,
    auto_close_duration = None,
    custom_text = (None, None),
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    any_key_closes = False,
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                   Any                   |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
|                   str                   |        title        | Optional title for the window. If none provided, the first arg will be used instead. |
|         Tuple[str, str] or None         |    button_color     | Color of the buttons shown (text color, button color) |
|                   str                   |  background_color   | Window's background color |
|                   str                   |     text_color      | text color |
|                   int                   |     button_type     | NOT USER SET! Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). There are many Popup functions and they call Popup, changing this parameter to get the desired effect. |
|                  bool                   |     auto_close      | If True the window will automatically close |
|                   int                   | auto_close_duration | time in seconds to keep window open before closing it automatically |
|         Tuple[str, str] or str          |     custom_text     | A string or pair of strings that contain the text to display on the buttons |
|                  bool                   |    non_blocking     | If True then will immediately return from the function without waiting for the user's input. |
|              str or bytes               |        icon         | icon to display on the window. Same format as a Window call |
|                   int                   |     line_width      | Width of lines in characters. Defaults to MESSAGE_BOX_LINE_WIDTH |
| str or Tuple[font_name, size, modifiers] |        font         | specifies the font family, size, etc |
|                  bool                   |     no_titlebar     | If True will not show the frame around the window and the titlebar across the top |
|                  bool                   |    grab_anywhere    | If True can grab anywhere to move the window. If no_titlebar is True, grab_anywhere should likely be enabled too |
|             Tuple[int, int]             |      location       | Location on screen to display the top left corner of window. Defaults to window centered on screen |
|                  bool                   |     keep_on_top     | If True the window will remain above all current windows |
|                  bool                   |   any_key_closes    | If True then will turn on return_keyboard_events for the window which will cause window to close as soon as any key is pressed. Normally the return key only will close the window. Default is false. |
|              str or bytes               |        image        | Image to include at the top of the popup window |
|                  bool                   |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Show animation one frame at a time.  This function has its own internal clocking meaning you can call it at any frequency
 and the rate the frames of video is shown remains constant.  Maybe your frames update every 30 ms but your
 event loop is running every 10 ms.  You don't have to worry about delaying, just call it every time through the
 loop.

```
popup_animated(image_source,
    message = None,
    background_color = None,
    text_color = None,
    font = None,
    no_titlebar = True,
    grab_anywhere = True,
    keep_on_top = True,
    location = (None, None),
    alpha_channel = None,
    time_between_frames = 0,
    transparent_color = None,
    title = "",
    icon = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str or bytes |    image_source     | Either a filename or a base64 string. |
|     str     |       message       | An optional message to be shown with the animation |
|     str     |  background_color   | color of background |
|     str     |     text_color      | color of the text |
| str or tuple |        font         | specifies the font family, size, etc |
|    bool     |     no_titlebar     | If True then the titlebar and window frame will not be shown |
|    bool     |    grab_anywhere    | If True then you can move the window just clicking anywhere on window, hold and drag |
|    bool     |     keep_on_top     | If True then Window will remain on top of all other windows currently shownn |
| (int, int)  |      location       | (x,y) location on the screen to place the top left corner of your window. Default is to center on screen |
|    float    |    alpha_channel    | Window transparency 0 = invisible 1 = completely visible. Values between are see through |
|     int     | time_between_frames | Amount of time in milliseconds between each frame |
|     str     |  transparent_color  | This color will be completely see-through in your window. Can even click through |
|     str     |        title        | Title that will be shown on the window |
|     str     |        icon         | Same as Window icon parameter. Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO |
| None | **RETURN** | No return value

Display a Popup without a titlebar.   Enables grab anywhere so you can move it

```
popup_annoying(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    grab_anywhere = True,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Popup that closes itself after some time period

```
popup_auto_close(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = True,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display Popup with "cancelled" button text

```
popup_cancel(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Popup with colored button and 'Error' as button text

```
popup_error(args=*<1 or N object>,
    title = None,
    button_color = (None, None),
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display a calendar window, get the user's choice, return as a tuple (mon, day, year)

```
popup_get_date(start_mon = None,
    start_day = None,
    start_year = None,
    begin_at_sunday_plus = 0,
    no_titlebar = True,
    title = "Choose Date",
    keep_on_top = True,
    location = (None, None),
    close_when_chosen = False,
    icon = None,
    locale = None,
    month_names = None,
    day_abbreviations = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|    int     |      start_mon       | The starting month |
| int or None |      start_day       | The starting day - optional. Set to None or 0 if no date to be chosen at start |
|    int     |      start_year      | The starting year |
|    int     | begin_at_sunday_plus | Determines the left-most day in the display. 0=sunday, 1=monday, etc |
|    str     |         icon         | Same as Window icon parameter. Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO |
| (int, int) |       location       | (x,y) location on the screen to place the top left corner of your window. Default is to center on screen |
|    str     |        title         | Title that will be shown on the window |
|    bool    |  close_when_chosen   | MIKE_please_add_text_here |
|    str     |        locale        | locale used to get the day names |
|    bool    |     no_titlebar      | If True no titlebar will be shown |
|    bool    |     keep_on_top      | If True the window will remain above all current windows |
| List[str]  |     month_names      | optional list of month names to use (should be 12 items) |
| List[str]  |  day_abbreviations   | optional list of abbreviations to display as the day of week |
|    bool    |        modal         | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| None or (int, int, int) | **RETURN** | Tuple containing (month, day, year) of chosen date or None if was cancelled

Display popup window with text entry field and browse button so that a file can be chosen by user.

```
popup_get_file(message,
    title = None,
    default_path = "",
    default_extension = "",
    save_as = False,
    multiple_files = False,
    file_types = (('ALL Files', '*.*'),),
    no_window = False,
    size = (None, None),
    button_color = None,
    background_color = None,
    text_color = None,
    icon = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    initial_folder = None,
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str           |      message      | message displayed to user |
|          str           |       title       | Window title |
|          str           |   default_path    | path to display to user as starting point (filled into the input field) |
|          str           | default_extension | If no extension entered by user, add this to filename (only used in saveas dialogs) |
|          bool          |      save_as      | if True, the "save as" dialog is shown which will verify before overwriting |
|          bool          |  multiple_files   | if True, then allows multiple files to be selected that are returned with ';' between each filename |
| Tuple[Tuple[str,str]]  |    file_types     | List of extensions to show using wildcards. All files (the default) = (("ALL Files", "*.*"),) |
|          bool          |     no_window     | if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown |
|       (int, int)       |       size        | (width, height) of the InputText Element |
| Tuple[str, str] or str |   button_color    | Color of the button (text, background) |
|          str           | background_color  | background color of the entire window |
|          str           |    text_color     | color of the text |
|      bytes or str      |       icon        | filename or base64 string to be used for the window's icon |
| str or Tuple[str, int] |       font        | specifies the font family, size, etc |
|          bool          |    no_titlebar    | If True no titlebar will be shown |
|          bool          |   grab_anywhere   | If True: can grab anywhere to move the window (Default = False) |
|          bool          |    keep_on_top    | If True the window will remain above all current windows |
|    Tuple[int, int]     |     location      | Location of upper left corner of the window |
|          str           |  initial_folder   | location in filesystem to begin browsing |
|      str or bytes      |       image       | Image to include at the top of the popup window |
|          bool          |       modal       | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None | **RETURN** | string representing the file(s) chosen, None if cancelled or window closed with X

Display popup with text entry field and browse button so that a folder can be chosen.

```
popup_get_folder(message,
    title = None,
    default_path = "",
    no_window = False,
    size = (None, None),
    button_color = None,
    background_color = None,
    text_color = None,
    icon = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    initial_folder = None,
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str           |     message      | message displayed to user |
|          str           |      title       | Window title |
|          str           |   default_path   | path to display to user as starting point (filled into the input field) |
|          bool          |    no_window     | if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown |
|       (int, int)       |       size       | (width, height) of the InputText Element |
| Tuple[str, str] or str |   button_color   | button color (foreground, background) |
|          str           | background_color | color of background |
|          str           |    text_color    | color of the text |
|      bytes or str      |       icon       | filename or base64 string to be used for the window's icon |
| str or Tuple[str, int] |       font       | specifies the font family, size, etc |
|          bool          |   no_titlebar    | If True no titlebar will be shown |
|          bool          |  grab_anywhere   | If True: can grab anywhere to move the window (Default = False) |
|          bool          |   keep_on_top    | If True the window will remain above all current windows |
|    Tuple[int, int]     |     location     | Location of upper left corner of the window |
|          str           |  initial_folder  | location in filesystem to begin browsing |
|      str or bytes      |      image       | Image to include at the top of the popup window |
|          bool          |      modal       | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None | **RETURN** | string representing the path chosen, None if cancelled or window closed with X

Display Popup with text entry field. Returns the text entered or None if closed / cancelled

```
popup_get_text(message,
    title = None,
    default_text = "",
    password_char = "",
    size = (None, None),
    button_color = None,
    background_color = None,
    text_color = None,
    icon = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          str           |     message      | message displayed to user |
|          str           |      title       | Window title |
|          str           |   default_text   | default value to put into input area |
|          str           |  password_char   | character to be shown instead of actually typed characters |
|       (int, int)       |       size       | (width, height) of the InputText Element |
| Tuple[str, str] or str |   button_color   | Color of the button (text, background) |
|          str           | background_color | background color of the entire window |
|          str           |    text_color    | color of the message text |
|      bytes or str      |       icon       | filename or base64 string to be used for the window's icon |
| str or Tuple[str, int] |       font       | specifies the font family, size, etc |
|          bool          |   no_titlebar    | If True no titlebar will be shown |
|          bool          |  grab_anywhere   | If True can click and drag anywhere in the window to move the window |
|          bool          |   keep_on_top    | If True the window will remain above all current windows |
|    Tuple[int, int]     |     location     | (x,y) Location on screen to display the upper left corner of window |
|      str or bytes      |      image       | Image to include at the top of the popup window |
|          bool          |      modal       | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None | **RETURN** | Text entered or None if window was closed or cancel button clicked

Display a Popup without a titlebar.   Enables grab anywhere so you can move it

```
popup_no_border(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    grab_anywhere = True,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Show a Popup but without any buttons

```
popup_no_buttons(args=*<1 or N object>,
    title = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any          |        *args        | Variable number of items to display |
|          str          |        title        | Title to display in the window. |
|          str          |  background_color   | color of background |
|          str          |     text_color      | color of the text |
|         bool          |     auto_close      | if True window will close itself |
|     int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|         bool          |    non_blocking     | If True then will immediately return from the function without waiting for the user's input. (Default = False) |
|     bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int          |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|         bool          |     no_titlebar     | If True no titlebar will be shown |
|         bool          |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
|    Tuple[int, int]    |      location       | Location of upper left corner of the window |
|     str or bytes      |        image        | Image to include at the top of the popup window |
|         bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display a Popup without a titlebar.   Enables grab anywhere so you can move it

```
popup_no_frame(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    grab_anywhere = True,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display a Popup without a titlebar.   Enables grab anywhere so you can move it

```
popup_no_titlebar(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    grab_anywhere = True,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Show Popup window and immediately return (does not block)

```
popup_no_wait(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = True,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = False |
| str or None | **RETURN** | Reason for popup closing

Show Popup window and immediately return (does not block)

```
popup_non_blocking(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = True,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = False |
| str or None | **RETURN** | Reason for popup closing

Displays a "notification window", usually in the bottom right corner of your display.  Has an icon, a title, and a message.  It is more like a "toaster" window than the normal popups.

The window will slowly fade in and out if desired.  Clicking on the window will cause it to move through the end the current "phase". For example, if the window was fading in and it was clicked, then it would immediately stop fading in and instead be fully visible.  It's a way for the user to quickly dismiss the window.

The return code specifies why the call is returning (e.g. did the user click the message to dismiss it)

```
popup_notify(args=*<1 or N object>,
    title = "",
    icon = ...,
    display_duration_in_ms = 3000,
    fade_in_duration = 1000,
    alpha = 0.9,
    location = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|       str       |         title          | Text to be shown at the top of the window in a larger font |
|       str       |        message         | Text message that makes up the majority of the window |
|  bytes or str   |          icon          | A base64 encoded PNG/GIF image or PNG/GIF filename that will be displayed in the window |
|       int       | display_duration_in_ms | Number of milliseconds to show the window |
|       int       |    fade_in_duration    | Number of milliseconds to fade window in and out |
|      float      |         alpha          | Alpha channel. 0 - invisible 1 - fully visible |
| Tuple[int, int] |        location        | Location on the screen to display the window |
| (int) | **RETURN** | reason for returning

Display Popup with OK button only

```
popup_ok(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display popup with OK and Cancel buttons

```
popup_ok_cancel(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = ...,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| "OK" or "Cancel" or None | **RETURN** | clicked button

Show Popup box that doesn't block and closes itself

```
popup_quick(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = True,
    auto_close_duration = 2,
    non_blocking = True,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = False |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Show Popup window with no titlebar, doesn't block, and auto closes itself.

```
popup_quick_message(args=*<1 or N object>,
    title = None,
    button_type = 5,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = True,
    auto_close_duration = 2,
    non_blocking = True,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = True,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = False |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Show a scrolled Popup window containing the user's text that was supplied.  Use with as many items to print as you
want, just like a print statement.

```
popup_scrolled(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    yes_no = False,
    auto_close = False,
    auto_close_duration = None,
    size = (None, None),
    location = (None, None),
    non_blocking = False,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    font = None,
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          bool          |       yes_no        | If True, displays Yes and No buttons instead of Ok |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|       (int, int)       |        size         | (w,h) w=characters-wide, h=rows-high |
|    Tuple[int, int]     |      location       | Location on the screen to place the upper left corner of the window |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Popup that closes itself after some time period

```
popup_timed(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = True,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
|          int           |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Display Popup with Yes and No buttons

```
popup_yes_no(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = False,
    auto_close_duration = None,
    non_blocking = False,
    icon = None,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|      bytes or str      |        icon         | filename or base64 string to be used for the window's icon |
|          int           |     line_width      | Width of lines in characters |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True: can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
|    Tuple[int, int]     |      location       | Location of upper left corner of the window |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| "Yes" or "No" or None | **RETURN** | clicked button

Same as popup_scrolled

Show a scrolled Popup window containing the user's text that was supplied.  Use with as many items to print as you
want, just like a print statement.

```
sprint(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    yes_no = False,
    auto_close = False,
    auto_close_duration = None,
    size = (None, None),
    location = (None, None),
    non_blocking = False,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    font = None,
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          bool          |       yes_no        | If True, displays Yes and No buttons instead of Ok |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|       (int, int)       |        size         | (w,h) w=characters-wide, h=rows-high |
|    Tuple[int, int]     |      location       | Location on the screen to place the upper left corner of the window |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

Show a scrolled Popup window containing the user's text that was supplied.  Use with as many items to print as you
want, just like a print statement.

```
ScrolledTextBox(args=*<1 or N object>,
    title = None,
    button_color = None,
    background_color = None,
    text_color = None,
    yes_no = False,
    auto_close = False,
    auto_close_duration = None,
    size = (None, None),
    location = (None, None),
    non_blocking = False,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    font = None,
    image = None,
    modal = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|          Any           |        *args        | Variable number of items to display |
|          str           |        title        | Title to display in the window. |
| Tuple[str, str] or str |    button_color     | button color (foreground, background) |
|          bool          |       yes_no        | If True, displays Yes and No buttons instead of Ok |
|          bool          |     auto_close      | if True window will close itself |
|      int or float      | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
|       (int, int)       |        size         | (w,h) w=characters-wide, h=rows-high |
|    Tuple[int, int]     |      location       | Location on the screen to place the upper left corner of the window |
|          bool          |    non_blocking     | if True the call will immediately return rather than waiting on user input |
|          str           |  background_color   | color of background |
|          str           |     text_color      | color of the text |
|          bool          |     no_titlebar     | If True no titlebar will be shown |
|          bool          |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
|          bool          |     keep_on_top     | If True the window will remain above all current windows |
| str or Tuple[str, int] |        font         | specifies the font family, size, etc |
|      str or bytes      |        image        | Image to include at the top of the popup window |
|          bool          |        modal        | If True then makes the popup will behave like a Modal window... all other windows are non-operational until this one is closed. Default = True |
| str or None or TIMEOUT_KEY | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

## PEP8 Function Bindings

Dumps an Object's values as a formatted string.  Very nicely done. Great way to display an object's member variables in human form

```
obj_to_string(obj, extra = "    ")
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any |  obj  | The object to display |
| str | extra | extra stuff (Default value = ' ') |
| (str) | **RETURN** | Formatted output of the object's values

Dumps an Object's values as a formatted string.  Very nicely done. Great way to display an object's member variables in human form
Returns only the top-most object's variables instead of drilling down to dispolay more

```
obj_to_string_single_obj(obj)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any | obj | The object to display |
| (str) | **RETURN** | Formatted output of the object's values

### Non PEP8 version (same as PEP8 version)

Sets the icon which will be used any time a window is created if an icon is not provided when the
window is created.

```
SetGlobalIcon(icon)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bytes or str | icon | Either a Base64 byte string or a filename |
| None | **RETURN** | None

```
SetOptions(icon = None,
    button_color = None,
    element_size = (None, None),
    button_element_size = (None, None),
    margins = (None, None),
    element_padding = (None, None),
    auto_size_text = None,
    auto_size_buttons = None,
    font = None,
    border_width = None,
    slider_border_width = None,
    slider_relief = None,
    slider_orientation = None,
    autoclose_time = None,
    message_box_line_width = None,
    progress_meter_border_depth = None,
    progress_meter_style = None,
    progress_meter_relief = None,
    progress_meter_color = None,
    progress_meter_size = None,
    text_justification = None,
    background_color = None,
    element_background_color = None,
    text_element_background_color = None,
    input_elements_background_color = None,
    input_text_color = None,
    scrollbar_color = None,
    text_color = None,
    element_text_color = None,
    debug_win_size = (None, None),
    window_location = (None, None),
    error_button_color = (None, None),
    tooltip_time = None,
    tooltip_font = None,
    use_ttk_buttons = None,
    ttk_theme = None,
    suppress_error_popups = None,
    suppress_raise_key_errors = None,
    suppress_key_guessing = None,
    enable_treeview_869_patch = None,
    enable_mac_notitlebar_patch = None,
    use_custom_titlebar = None,
    titlebar_background_color = None,
    titlebar_text_color = None,
    titlebar_font = None,
    titlebar_icon = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                  bytes or str                  |              icon               | filename or base64 string to be used for the window's icon |
|             Tuple[str, str] or str             |          button_color           | Color of the button (text, background) |
|                   (int, int)                   |          element_size           | element size (width, height) in characters |
|                   (int, int)                   |       button_element_size       | Size of button |
|                Tuple[int, int]                 |             margins             | (left/right, top/bottom) tkinter margins around outsize. Amount of pixels to leave inside the window's frame around the edges before your elements are shown. |
|   Tuple[int, int] or ((int, int),(int,int))    |         element_padding         | Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                      bool                      |         auto_size_text          | True if the Widget should be shrunk to exactly fit the number of chars to show |
|                      bool                      |        auto_size_buttons        | True if Buttons in this Window should be sized to exactly fit the text on this. |
|             str or Tuple[str, int]             |              font               | specifies the font family, size, etc |
|                      int                       |          border_width           | width of border around element |
|                      ???                       |       slider_border_width       | ??? |
|                      ???                       |          slider_relief          | ??? |
|                      ???                       |       slider_orientation        | ??? |
|                      ???                       |         autoclose_time          | ??? |
|                      ???                       |     message_box_line_width      | ??? |
|                      ???                       |   progress_meter_border_depth   | ??? |
|                      ???                       |      progress_meter_style       | You can no longer set a progress bar style. All ttk styles must be the same for the window |
|                      ???                       |      progress_meter_relief      |  |
|                      ???                       |      progress_meter_color       | ??? |
|                      ???                       |       progress_meter_size       | ??? |
|         'left' or 'right' or 'center'          |       text_justification        | Default text justification for all Text Elements in window |
|                      str                       |        background_color         | color of background |
|                      str                       |    element_background_color     | element background color |
|                      str                       |  text_element_background_color  | text element background color |
|                 idk_yetReally                  | input_elements_background_color | ??? |
|                      ???                       |        input_text_color         | ??? |
|                      ???                       |         scrollbar_color         | ??? |
|                      str                       |           text_color            | color of the text |
|                      ???                       |       element_text_color        | ??? |
|                Tuple[int, int]                 |         debug_win_size          | window size |
|                      ???                       |         window_location         | (Default = (None)) |
|                      ???                       |       error_button_color        | (Default = (None)) |
|                      int                       |          tooltip_time           | time in milliseconds to wait before showing a tooltip. Default is 400ms |
| str or Tuple[str, int] or Tuple[str, int, str] |          tooltip_font           | font to use for all tooltips |
|                      bool                      |         use_ttk_buttons         | if True will cause all buttons to be ttk buttons |
|                      str                       |            ttk_theme            | Theme to use with ttk widgets. Choices (on Windows) include - 'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative' |
|                      bool                      |      suppress_error_popups      | If True then error popups will not be shown if generated internally to PySimpleGUI |
|                      bool                      |    suppress_raise_key_errors    | If True then key errors won't be raised (you'll still get popup error) |
|                      bool                      |      suppress_key_guessing      | If True then key errors won't try and find closest matches for you |
|                      bool                      |    enable_treeview_869_patch    | If True, then will use the treeview color patch for tk 8.6.9 |
|                      bool                      |   enable_mac_notitlebar_patch   | If True then Windows with no titlebar use an alternative technique when tkinter version < 8.6.10 |
|                      bool                      |       use_custom_titlebar       | If True then a custom titlebar is used instead of the normal system titlebar |
|                  str or None                   |    titlebar_background_color    | If custom titlebar indicated by use_custom_titlebar, then use this as background color |
|                  str or None                   |       titlebar_text_color       | If custom titlebar indicated by use_custom_titlebar, then use this as text color |
|         str or Tuple[str, int] or None         |          titlebar_font          | If custom titlebar indicated by use_custom_titlebar, then use this as title font |
|                  bytes or str                  |          titlebar_icon          | If custom titlebar indicated by use_custom_titlebar, then use this as the icon (file or base64 bytes) |
| None | **RETURN** | None

## The Test Harness

Used to test the installation, get information about the versions, upgrade from GitHub

The PySimpleGUI "Test Harness".  This is meant to be a super-quick test of the Elements.

```
main()
```

Display a window that will display the docstrings for each PySimpleGUI Element and the Window object

```
main_sdk_help()
```

The PySimpleGUI "Test Harness".  This is meant to be a super-quick test of the Elements.

```
test()
```

## Debugger

Shows the smaller "popout" window.  Default location is the upper right corner of your screen

```
show_debugger_popout_window(location = (None, None), args=*<1 or N object>)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] | location | Locations (x,y) on the screen to place upper left corner of the window |
| None | **RETURN** | None

Shows the large main debugger window

```
show_debugger_window(location = (None, None), args=*<1 or N object>)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Tuple[int, int] | location | Locations (x,y) on the screen to place upper left corner of the window |
| None | **RETURN** | None

## Themes

Sets / Gets the current Theme.  If none is specified then returns the current theme.
This call replaces the ChangeLookAndFeel / change_look_and_feel call which only sets the theme.

```
theme(new_theme = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | new_theme | the new theme name to use |
| (str) | **RETURN** | the currently selected theme

Add a new theme to the dictionary of themes

```
theme_add_new(new_theme_name, new_theme_dict)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str  | new_theme_name | text to display in element |
| dict | new_theme_dict | text to display in element |

Sets/Returns the background color currently in use
Used for Windows and containers (Column, Frame, Tab) and tables

```
theme_background_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | color | new background color to use (optional) |
| (str) | **RETURN** | color string of the background color currently in use

Sets/Returns the border width currently in use
Used by non ttk elements at the moment

```
theme_border_width(border_width = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | (int) - border width currently in use

Sets/Returns the button color currently in use

```
theme_button_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | Tuple[str, str] - TUPLE with color strings of the button color currently in use (button text color, button background color)

Sets/Returns the background color currently in use for all elements except containers

```
theme_element_background_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | (str) - color string of the element background color currently in use

Sets/Returns the text color used by elements that have text as part of their display (Tables, Trees and Sliders)

```
theme_element_text_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | (str) - color string currently in use

Sets/Returns the input element background color currently in use

```
theme_input_background_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | (str) - color string of the input element background color currently in use

Sets/Returns the input element entry color (not the text but the thing that's displaying the text)

```
theme_input_text_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | (str) - color string of the input element color currently in use

Returns a sorted list of the currently available color themes

```
theme_list()
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[str] | **RETURN** | List[str] - A sorted list of the currently available color themes

Displays a "Quick Reference Window" showing all of the different Look and Feel settings that are available.
They are sorted alphabetically.  The legacy color names are mixed in, but otherwise they are sorted into Dark and Light halves

```
theme_previewer(columns = 12,
    scrollable = False,
    scroll_area_size = (None, None),
    search_string = None,
    location = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|    int     |     columns      | The number of themes to display per row |
|    bool    |    scrollable    | If True then scrollbars will be added |
| (int, int) | scroll_area_size | Size of the scrollable area (The Column Element used to make scrollable) |
|    str     |  search_string   | If specified then only themes containing this string will be shown |
| (int, int) |     location     | Location on the screen to place the window. Defaults to the center like all windows |

Display themes in a window as color swatches.
Click on a color swatch to see the hex value printed on the console.
If you hover over a color or right click it you'll also see the hext value.

```
theme_previewer_swatches()
```

Sets/Returns the progress meter border width currently in use

```
theme_progress_bar_border_width(border_width = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | (int) - border width currently in use

Sets/Returns the progress bar colors by the current color theme

```
theme_progress_bar_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | Tuple[str, str] - TUPLE with color strings of the ProgressBar color currently in use(button text color, button background color)

Sets/Returns the slider border width currently in use

```
theme_slider_border_width(border_width = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | (int) - border width currently in use

Sets/Returns the slider color (used for sliders)

```
theme_slider_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | (str) - color string of the slider color currently in use

Sets/Returns the text color currently in use

```
theme_text_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | (str) - color string of the text color currently in use

Sets/Returns the background color for text elements

```
theme_text_element_background_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (str) | **RETURN** | (str) - color string of the text background color currently in use

## User Settings

Returns the current settings dictionary.  If you've not setup the filename for the
settings, a default one will be used and then read.

```
user_settings()
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| (dict) | **RETURN** | The current settings dictionary

Deletes an individual entry.  If no filename has been specified up to this point,
then a default filename will be used.
After value has been deleted, the settings file is written to disk.

```
user_settings_delete_entry(key)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any | key | Setting to be saved. Can be any valid dictionary key type (hashable) |

Deltes the filename and path for your settings file.  Either paramter can be optional.
If you don't choose a path, one is provided for you that is OS specific
Windows path default = users/name/AppData/Local/PySimpleGUI/settings.
If you don't choose a filename, your application's filename + '.json' will be used
Also sets your current dictionary to a blank one.

```
user_settings_delete_filename(filename = None, path = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | filename | The name of the file to use. Can be a full path and filename or just filename |
| str |   path   | The folder that the settings file will be stored in. Do not include the filename. |

Determines if a settings file exists.  If so a boolean True is returned.
If either a filename or a path is not included, then the appropriate default
will be used.

```
user_settings_file_exists(filename = None, path = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | filename | Filename to check |
| str |   path   | Path to the file. Defaults to a specific folder depending on the operating system |
| (bool) | **RETURN** | True if the file exists

Sets the filename and path for your settings file.  Either paramter can be optional.

If you don't choose a path, one is provided for you that is OS specific
Windows path default = users/name/AppData/Local/PySimpleGUI/settings.

If you don't choose a filename, your application's filename + '.json' will be used.

Normally the filename and path are split in the user_settings calls. However for this call they
can be combined so that the filename contains both the path and filename.

```
user_settings_filename(filename = None, path = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | filename | The name of the file to use. Can be a full path and filename or just filename |
| str |   path   | The folder that the settings file will be stored in. Do not include the filename. |
| (str) | **RETURN** | The full pathname of the settings file that has both the path and filename combined.

Returns the value of a specified setting.  If the setting is not found in the settings dictionary, then
the user specified default value will be returned.  It no default is specified and nothing is found, then
None is returned.  If the key isn't in the dictionary, then it will be added and the settings file saved.
If no filename has been specified up to this point, then a default filename will be assigned and used.
The settings are SAVED prior to returning.

```
user_settings_get_entry(key, default = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any |   key   | Key used to lookup the setting in the settings dictionary |
| Any | default | Value to use should the key not be found in the dictionary |
| (Any) | **RETURN** | Value of specified settings

Specifies the path and filename to use for the settings and reads the contents of the file.
The filename can be a full filename including a path, or the path can be specified separately.
If  no filename is specified, then the caller's filename will be used with the extension ".json"

```
user_settings_load(filename = None, path = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | filename | Filename to load settings from (and save to in the future) |
| str |   path   | Path to the file. Defaults to a specific folder depending on the operating system |
| (dict) | **RETURN** | The settings dictionary (i.e. all settings)

Saves the current settings dictionary.  If a filename or path is specified in the call, then it will override any
previously specitfied filename to create a new settings file.  The settings dictionary is then saved to the newly defined file.

```
user_settings_save(filename = None, path = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str | filename | The fFilename to save to. Can specify a path or just the filename. If no filename specified, then the caller's filename will be used. |
| str |   path   | The (optional) path to use to save the file. |
| (str) | **RETURN** | The full path and filename used to save the settings

Sets an individual setting to the specified value.  If no filename has been specified up to this point,
then a default filename will be used.
After value has been modified, the settings file is written to disk.

```
user_settings_set_entry(key, value)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Any |  key  | Setting to be saved. Can be any valid dictionary key type |
| Any | value | Value to save as the setting's value. Can be anything |

Used to control the display of error messages.  By default, error messages are displayed to stdout.

```
user_settings_silent_on_error(silent_on_error = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bool | silent_on_error | If True then all error messages are silenced (not displayed on the console) |

Writes a specified dictionary to the currently defined settings filename.

```
user_settings_write_new_dictionary(settings_dict)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| dict | settings_dict | The dictionary to be written to the currently defined settings file |

## Misc

Fills a window with values provided in a values dictionary { element_key : new_value }

```
FillFormWithValues(window, values_dict)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|      Window      |   window    | The window object to fill |
| (Dict[Any, Any]) | values_dict | A dictionary with element keys as key and value is values parm for Update call |
| None | **RETURN** | None

Fills a window with values provided in a values dictionary { element_key : new_value }

```
fill_form_with_values(window, values_dict)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|      Window      |   window    | The window object to fill |
| (Dict[Any, Any]) | values_dict | A dictionary with element keys as key and value is values parm for Update call |
| None | **RETURN** | None

## Layout Helper Funcs

Pin's an element provided into a layout so that when it's made invisible and visible again, it will
 be in the correct place.  Otherwise it will be placed at the end of its containing window/column.

```
pin(elem,
    vertical_alignment = None,
    shrink = True,
    expand_x = None,
    expand_y = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|  Element   |        elem        | the element to put into the layout |
| str or None | vertical_alignment | Aligns elements vertically. 'top', 'center', 'bottom'. Can be shortened to 't', 'c', 'b' |
|    bool    |       shrink       | If True, then the space will shrink down to a single pixel when hidden. False leaves the area large and blank |
| Column | **RETURN** | A column element containing the provided element

Align an element or a row of elements to the bottom of the row that contains it

```
vbottom(elem_or_row)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Element or List[Element] or Tuple[Element] | elem_or_row | the element or row of elements |
| Column or List[Column] | **RETURN** | A column element containing the provided element aligned to the bottom or list of elements (a row)

Align an element or a row of elements to the center of the row that contains it

```
vcenter(elem_or_row)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Element or List[Element] or Tuple[Element] | elem_or_row | the element or row of elements |
| Column or List[Column] | **RETURN** | A column element containing the provided element aligned to the center or list of elements (a row)

Align an element or a row of elements to the top of the row that contains it

```
vtop(elem_or_row)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| Element or List[Element] or Tuple[Element] | elem_or_row | the element or row of elements |
| Column or List[Column] | **RETURN** | A column element containing the provided element aligned to the top or list of elements (a row)

## Configuration / Settings / Extensions

Sets the icon which will be used any time a window is created if an icon is not provided when the
window is created.

```
set_global_icon(icon)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| bytes or str | icon | Either a Base64 byte string or a filename |
| None | **RETURN** | None

```
set_options(icon = None,
    button_color = None,
    element_size = (None, None),
    button_element_size = (None, None),
    margins = (None, None),
    element_padding = (None, None),
    auto_size_text = None,
    auto_size_buttons = None,
    font = None,
    border_width = None,
    slider_border_width = None,
    slider_relief = None,
    slider_orientation = None,
    autoclose_time = None,
    message_box_line_width = None,
    progress_meter_border_depth = None,
    progress_meter_style = None,
    progress_meter_relief = None,
    progress_meter_color = None,
    progress_meter_size = None,
    text_justification = None,
    background_color = None,
    element_background_color = None,
    text_element_background_color = None,
    input_elements_background_color = None,
    input_text_color = None,
    scrollbar_color = None,
    text_color = None,
    element_text_color = None,
    debug_win_size = (None, None),
    window_location = (None, None),
    error_button_color = (None, None),
    tooltip_time = None,
    tooltip_font = None,
    use_ttk_buttons = None,
    ttk_theme = None,
    suppress_error_popups = None,
    suppress_raise_key_errors = None,
    suppress_key_guessing = None,
    enable_treeview_869_patch = None,
    enable_mac_notitlebar_patch = None,
    use_custom_titlebar = None,
    titlebar_background_color = None,
    titlebar_text_color = None,
    titlebar_font = None,
    titlebar_icon = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|                  bytes or str                  |              icon               | filename or base64 string to be used for the window's icon |
|             Tuple[str, str] or str             |          button_color           | Color of the button (text, background) |
|                   (int, int)                   |          element_size           | element size (width, height) in characters |
|                   (int, int)                   |       button_element_size       | Size of button |
|                Tuple[int, int]                 |             margins             | (left/right, top/bottom) tkinter margins around outsize. Amount of pixels to leave inside the window's frame around the edges before your elements are shown. |
|   Tuple[int, int] or ((int, int),(int,int))    |         element_padding         | Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom)) |
|                      bool                      |         auto_size_text          | True if the Widget should be shrunk to exactly fit the number of chars to show |
|                      bool                      |        auto_size_buttons        | True if Buttons in this Window should be sized to exactly fit the text on this. |
|             str or Tuple[str, int]             |              font               | specifies the font family, size, etc |
|                      int                       |          border_width           | width of border around element |
|                      ???                       |       slider_border_width       | ??? |
|                      ???                       |          slider_relief          | ??? |
|                      ???                       |       slider_orientation        | ??? |
|                      ???                       |         autoclose_time          | ??? |
|                      ???                       |     message_box_line_width      | ??? |
|                      ???                       |   progress_meter_border_depth   | ??? |
|                      ???                       |      progress_meter_style       | You can no longer set a progress bar style. All ttk styles must be the same for the window |
|                      ???                       |      progress_meter_relief      |  |
|                      ???                       |      progress_meter_color       | ??? |
|                      ???                       |       progress_meter_size       | ??? |
|         'left' or 'right' or 'center'          |       text_justification        | Default text justification for all Text Elements in window |
|                      str                       |        background_color         | color of background |
|                      str                       |    element_background_color     | element background color |
|                      str                       |  text_element_background_color  | text element background color |
|                 idk_yetReally                  | input_elements_background_color | ??? |
|                      ???                       |        input_text_color         | ??? |
|                      ???                       |         scrollbar_color         | ??? |
|                      str                       |           text_color            | color of the text |
|                      ???                       |       element_text_color        | ??? |
|                Tuple[int, int]                 |         debug_win_size          | window size |
|                      ???                       |         window_location         | (Default = (None)) |
|                      ???                       |       error_button_color        | (Default = (None)) |
|                      int                       |          tooltip_time           | time in milliseconds to wait before showing a tooltip. Default is 400ms |
| str or Tuple[str, int] or Tuple[str, int, str] |          tooltip_font           | font to use for all tooltips |
|                      bool                      |         use_ttk_buttons         | if True will cause all buttons to be ttk buttons |
|                      str                       |            ttk_theme            | Theme to use with ttk widgets. Choices (on Windows) include - 'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative' |
|                      bool                      |      suppress_error_popups      | If True then error popups will not be shown if generated internally to PySimpleGUI |
|                      bool                      |    suppress_raise_key_errors    | If True then key errors won't be raised (you'll still get popup error) |
|                      bool                      |      suppress_key_guessing      | If True then key errors won't try and find closest matches for you |
|                      bool                      |    enable_treeview_869_patch    | If True, then will use the treeview color patch for tk 8.6.9 |
|                      bool                      |   enable_mac_notitlebar_patch   | If True then Windows with no titlebar use an alternative technique when tkinter version < 8.6.10 |
|                      bool                      |       use_custom_titlebar       | If True then a custom titlebar is used instead of the normal system titlebar |
|                  str or None                   |    titlebar_background_color    | If custom titlebar indicated by use_custom_titlebar, then use this as background color |
|                  str or None                   |       titlebar_text_color       | If custom titlebar indicated by use_custom_titlebar, then use this as text color |
|         str or Tuple[str, int] or None         |          titlebar_font          | If custom titlebar indicated by use_custom_titlebar, then use this as title font |
|                  bytes or str                  |          titlebar_icon          | If custom titlebar indicated by use_custom_titlebar, then use this as the icon (file or base64 bytes) |
| None | **RETURN** | None

## Old Themes (Look and Feel) - Replaced by theme()

Change the "color scheme" of all future PySimpleGUI Windows.
The scheme are string names that specify a group of colors. Background colors, text colors, button colors.
There are 13 different color settings that are changed at one time using a single call to ChangeLookAndFeel
The look and feel table itself has these indexes into the dictionary LOOK_AND_FEEL_TABLE.
The original list was (prior to a major rework and renaming)... these names still work...
In Nov 2019 a new Theme Formula was devised to make choosing a theme easier:
The "Formula" is:
["Dark" or "Light"] Color Number
Colors can be Blue Brown Grey Green Purple Red Teal Yellow Black
The number will vary for each pair. There are more DarkGrey entries than there are LightYellow for example.
Default = The default settings (only button color is different than system default)
Default1 = The full system default including the button (everything's gray... how sad... don't be all gray... please....)

```
ChangeLookAndFeel(index, force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str  | index | the name of the index into the Look and Feel table (does not have to be exact, can be "fuzzy") |
| bool | force | no longer used |
| None | **RETURN** | None

Get a list of the valid values to pass into your call to change_look_and_feel

```
ListOfLookAndFeelValues()
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[str] | **RETURN** | list of valid string values

Displays a "Quick Reference Window" showing all of the different Look and Feel settings that are available.
They are sorted alphabetically.  The legacy color names are mixed in, but otherwise they are sorted into Dark and Light halves

```
preview_all_look_and_feel_themes(columns = 12,
    scrollable = False,
    scroll_area_size = (None, None),
    search_string = None,
    location = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
|    int     |     columns      | The number of themes to display per row |
|    bool    |    scrollable    | If True then scrollbars will be added |
| (int, int) | scroll_area_size | Size of the scrollable area (The Column Element used to make scrollable) |
|    str     |  search_string   | If specified then only themes containing this string will be shown |
| (int, int) |     location     | Location on the screen to place the window. Defaults to the center like all windows |

Get a list of the valid values to pass into your call to change_look_and_feel

```
list_of_look_and_feel_values()
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| List[str] | **RETURN** | list of valid string values

Change the "color scheme" of all future PySimpleGUI Windows.
The scheme are string names that specify a group of colors. Background colors, text colors, button colors.
There are 13 different color settings that are changed at one time using a single call to ChangeLookAndFeel
The look and feel table itself has these indexes into the dictionary LOOK_AND_FEEL_TABLE.
The original list was (prior to a major rework and renaming)... these names still work...
In Nov 2019 a new Theme Formula was devised to make choosing a theme easier:
The "Formula" is:
["Dark" or "Light"] Color Number
Colors can be Blue Brown Grey Green Purple Red Teal Yellow Black
The number will vary for each pair. There are more DarkGrey entries than there are LightYellow for example.
Default = The default settings (only button color is different than system default)
Default1 = The full system default including the button (everything's gray... how sad... don't be all gray... please....)

```
change_look_and_feel(index, force = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|--|--|--|
| str  | index | the name of the index into the Look and Feel table (does not have to be exact, can be "fuzzy") |
| bool | force | no longer used |
| None | **RETURN** | None