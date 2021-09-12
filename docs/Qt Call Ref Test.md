# head1

## head2

## head3

1. list item1
	* sub list item2.1
	* sub list item2.2
	* sub list item2.3
1. list item2
1. list item3
1. list item4
1. list item5

## Function Reference

These are the functions available for you to call

### 1Line ProgressMeter

```
one_line_progress_meter(title,
    current_value,
    max_value,
    key = "OK for 1 meter",
    args=*<1 or N object>,
    orientation = "v",
    bar_color = (None, None),
    button_color = None,
    size = (200, 20),
    border_width = None,
    grab_anywhere = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `      str      ` |  orientation  | 'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical' / 'v') |
| `Tuple(str, str)` |   bar_color   | color of a bar line |
| `Tuple[str, str]` | button_color  | button color (foreground, background) |
| `Tuple[int, int]` |     size      | (w,h) w=characters-wide, h=rows-high (Default value = DEFAULT_PROGRESS_BAR_SIZE) |
| `      int      ` | border_width  | width of border around element |
| `     bool      ` | grab_anywhere | If True, than can grab anywhere to move the window (Default = False) |
| `     bool      ` |  no_titlebar  | If True no titlebar will be shown |

-----

```
one_line_progress_meter_cancel(key = "OK for 1 meter")
```

-----

### Button Related

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

-----

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

-----

```
FileBrowse(button_text = "Browse",
    target = (555666777, -1),
    file_types = (('ALL Files', '*'),),
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

-----

```
FilesBrowse(button_text = "Browse",
    target = (555666777, -1),
    file_types = (('ALL Files', '*'),),
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

-----

```
FileSaveAs(button_text = "Save As...",
    target = (555666777, -1),
    file_types = (('ALL Files', '*'),),
    initial_folder = None,
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

-----

```
SaveAs(button_text = "Save As...",
    target = (555666777, -1),
    file_types = (('ALL Files', '*'),),
    initial_folder = None,
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

-----

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

-----

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

-----

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

-----

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

-----

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

-----

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

-----

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

-----

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

-----

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

-----

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

-----

```
SimpleButton(button_text,
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

-----

```
close_button(button_text,
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

-----

```
read_button(button_text,
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
|:---:|:---:|:---:|
| `                                  str                                   ` |   button_text    | text in the button |
| `                                  str                                   ` |  image_filename  | image filename if there is a button image. GIFs and PNGs only. |
| `                              bytes or str                              ` |    image_data    | Raw or Base64 representation of the image to put on button. Choose either filename or data |
| `                            Tuple[int, int]                             ` |    image_size    | Size of the image in pixels (width, height) |
| `                                  int                                   ` | image_subsample  | amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
| `                                  int                                   ` |   border_width   | width of border around element |
| `                                  str                                   ` |     tooltip      | text, that will appear when mouse hovers over the element |
| `                            Tuple[int, int]                             ` |       size       | (w,h) w=characters-wide, h=rows-high |
| `                                  bool                                  ` | auto_size_button | True if button size is determined by button text |
| `                            Tuple[str, str]                             ` |   button_color   | button color (foreground, background) |
| `                         str or Tuple[str, int]                         ` |       font       | specifies the font family, size, etc |
| `                                  bool                                  ` | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
| `                                  bool                                  ` |     disabled     | set disable state for element (Default = False) |
| `                             idk_yetReally                              ` |      focus       | if focus should be set to this |
| `(int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int)` |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
| `                     str or int or tuple or object                      ` |       key        | key for uniquely identify this element (for window.FindElement) |
| `                     str or int or tuple or object                      ` |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| `                                  Any                                   ` |     metadata     | Anything you want to store along with this button |

-----

```
realtime_button(button_text,
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
|:---:|:---:|:---:|
| `                                  str                                   ` |   button_text    | text in the button |
| `                                  str                                   ` |  image_filename  | image filename if there is a button image. GIFs and PNGs only. |
| `                              bytes or str                              ` |    image_data    | Raw or Base64 representation of the image to put on button. Choose either filename or data |
| `                            Tuple[int, int]                             ` |    image_size    | Size of the image in pixels (width, height) |
| `                                  int                                   ` | image_subsample  | amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
| `                                  int                                   ` |   border_width   | width of border around element |
| `                                  str                                   ` |     tooltip      | text, that will appear when mouse hovers over the element |
| `                            Tuple[int, int]                             ` |       size       | (w,h) w=characters-wide, h=rows-high |
| `                                  bool                                  ` | auto_size_button | True if button size is determined by button text |
| `                            Tuple[str, str]                             ` |   button_color   | button color (foreground, background) |
| `                         str or Tuple[str, int]                         ` |       font       | specifies the font family, size, etc |
| `                                  bool                                  ` |     disabled     | set disable state for element (Default = False) |
| `                                  bool                                  ` | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
| `                                  bool                                  ` |      focus       | if focus should be set to this |
| `(int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int)` |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
| `                     str or int or tuple or object                      ` |       key        | key for uniquely identify this element (for window.FindElement) |
| `                     str or int or tuple or object                      ` |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| `                                  Any                                   ` |     metadata     | Anything you want to store along with this button |

-----

```
dummy_button(button_text,
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
|:---:|:---:|:---:|
| `                                  str                                   ` |   button_text    | text in the button |
| `                                  str                                   ` |  image_filename  | image filename if there is a button image. GIFs and PNGs only. |
| `                              bytes or str                              ` |    image_data    | Raw or Base64 representation of the image to put on button. Choose either filename or data |
| `                            Tuple[int, int]                             ` |    image_size    | Size of the image in pixels (width, height) |
| `                                  int                                   ` | image_subsample  | amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
| `                                  int                                   ` |   border_width   | width of border around element |
| `                                  str                                   ` |     tooltip      | text, that will appear when mouse hovers over the element |
| `                            Tuple[int, int]                             ` |       size       | (w,h) w=characters-wide, h=rows-high |
| `                                  bool                                  ` | auto_size_button | True if button size is determined by button text |
| `                            Tuple[str, str]                             ` |   button_color   | button color (foreground, background) |
| `                         str or Tuple[str, int]                         ` |       font       | specifies the font family, size, etc |
| `                                  bool                                  ` |     disabled     | set disable state for element (Default = False) |
| `                                  bool                                  ` | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
| `                                  bool                                  ` |      focus       | if focus should be set to this |
| `(int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int)` |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
| `                     str or int or tuple or object                      ` |       key        | key for uniquely identify this element (for window.FindElement) |
| `                     str or int or tuple or object                      ` |        k         | Same as the Key. You can use either k or key. Which ever is set will be used. |
| `                                  Any                                   ` |     metadata     | Anything you want to store along with this button |

-----

```
calendar_button(button_text,
    target = (None, None),
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
    key = None,
    k = None,
    metadata = None)
```

-----

```
color_chooser_button(button_text,
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
|:---:|:---:|:---:|
| `                                  str                                   ` |   button_text    | text in the button |
| `                         str or Tuple[int, int]                         ` |      target      | key or (row,col) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button |
| `                                  str                                   ` |  image_filename  | image filename if there is a button image. GIFs and PNGs only. |
| `                              bytes or str                              ` |    image_data    | Raw or Base64 representation of the image to put on button. Choose either filename or data |
| `                            Tuple[int, int]                             ` |    image_size    | Size of the image in pixels (width, height) |
| `                                  int                                   ` | image_subsample  | amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc |
| `                                  str                                   ` |     tooltip      | text, that will appear when mouse hovers over the element |
| `                                  int                                   ` |   border_width   | width of border around element |
| `                            Tuple[int, int]                             ` |       size       | (w,h) w=characters-wide, h=rows-high |
| `                                  bool                                  ` | auto_size_button | True if button size is determined by button text |
| `                            Tuple[str, str]                             ` |   button_color   | button color (foreground, background) |
| `                                  bool                                  ` |     disabled     | set disable state for element (Default = False) |
| `                         str or Tuple[str, int]                         ` |       font       | specifies the font family, size, etc |
| `                                  bool                                  ` | bind_return_key  | (Default = False) If True, then the return key will cause a the Listbox to generate an event |
| `                                  bool                                  ` |      focus       | if focus should be set to this |
| `(int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int)` |       pad        | Amount of padding to put around element in pixels (left/right, top/bottom) |
| `                                  Any                                   ` |     metadata     | Anything you want to store along with this button |

-----

### Color Printing

Sets up the color print (cprint) output destination

```
cprint_set_output_destination(window, multiline_key)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `Window` |    window     | The window that the cprint call will route the output to |
| ` Any  ` | multiline_key | Key for the Multiline Element where output will be sent |
| None | **RETURN** | None

-----

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
    key = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `          Any          ` |      *args       | stuff to output |
| `          str          ` |    text_color    | Color of the text |
| `          str          ` | background_color | The background color of the line |
| `str) or Tuple[str, str]` |      colors      | Either a tuple or a string that has both the text and background colors |
| `          str          ` |        t         | Color of the text |
| `          str          ` |        b         | The background color of the line |
| `str) or Tuple[str, str]` |        c         | Either a tuple or a string that has both the text and background colors |
| `          str          ` |       end        | end character |
| `          str          ` |       sep        | separator character |
| `          Any          ` |       key        | key of multiline to output to (if you want to override the one previously set) |
| `        Window         ` |      window      | Window containing the multiline to output to (if you want to override the one previously set) |
| None | **RETURN** | None

-----

### Debug Window Output

Works like a "print" statement but with windowing options.  Routes output to the "Debug Window"

In addition to the normal text and background colors, you can use a "colors" tuple/string
The "colors" or "c" parameter defines both the text and background in a single parm.
It can be a tuple or a single single. Both text and background colors need to be specified
colors -(str, str) or str.  A combined text/background color definition in a single parameter
c - Tuple[str, str] - Colors tuple has format (foreground, backgrouned)
c - str - can also be a string of the format "foreground on background"  ("white on red")

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
    background_color = None,
    colors = None,
    c = None,
    erase_all = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `          Any          ` |         *args         | stuff to output |
| `      (int, int)       ` |         size          | (w,h) w=characters-wide, h=rows-high |
| `          str          ` |          end          | end character |
| `          str          ` |          sep          | separator character |
| `    Tuple[int, int]    ` |       location        | Location of upper left corner of the window |
| `str or Tuple[str, int] ` |         font          | specifies the font family, size, etc |
| `         bool          ` |      no_titlebar      | If True no titlebar will be shown |
| `         bool          ` |       no_button       | don't show button |
| `         bool          ` |     grab_anywhere     | If True: can grab anywhere to move the window (Default = False) |
| `          str          ` |   background_color    | color of background |
| `          str          ` |      text_color       | color of the text |
| `         bool          ` |      keep_on_top      | If True the window will remain above all current windows |
| `    Tuple[int, int]    ` |       location        | Location of upper left corner of the window |
| `         bool          ` | do_not_reroute_stdout | do not reroute stdout |
| `str) or Tuple[str, str]` |        colors         | Either a tuple or a string that has both the text and background colors |
| `str) or Tuple[str, str]` |           c           | Either a tuple or a string that has both the text and background colors |
| `         bool          ` |       erase_all       | If True when erase the output before printing |

-----

```
easy_print_close()
```

-----

### Element-Function

"Pushes" out the size of whatever it is placed inside of.
This includes Columns, Frames, Tabs and Windows.
Kind of like a pad in layouts

```
sizer(h_pixels = 0, v_pixels = 0)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `int` | h_pixels | number of horizontal pixels |
| `int` | v_pixels | number of vertical pixels |
| (Column) | **RETURN** | (Column) A column element that has a pad setting set according to parameters

-----

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
|:---:|:---:|:---:|
| `  Element  ` |        elem        | the element to put into the layout |
| `str or None` | vertical_alignment | Aligns elements vertically. 'top', 'center', 'bottom'. Can be shortened to 't', 'c', 'b' |
| `   bool    ` |       shrink       | If True, then the space will shrink down to a single pixel when hidden. False leaves the area large and blank |
| `   bool    ` |      expand_x      | If True/False the value will be passed to the Column Elements used to make this feature |
| `   bool    ` |      expand_y      | If True/False the value will be passed to the Column Elements used to make this feature |
| Column | **RETURN** | A column element containing the provided element

-----

Align an element or a row of elements to the top of the row that contains it

```
vtop(elem_or_row)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `Element or List[Element] or Tuple[Element]` | elem_or_row | the element or row of elements |
| `                   bool                   ` |  expand_x   | If True/False the value will be passed to the Column Elements used to make this feature |
| `                   bool                   ` |  expand_y   | If True/False the value will be passed to the Column Elements used to make this feature |
| Column or List[Column] | **RETURN** | A column element containing the provided element aligned to the top or list of elements (a row)

-----

Align an element or a row of elements to the center of the row that contains it

```
vcenter(elem_or_row)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `Element or List[Element] or Tuple[Element]` | elem_or_row | the element or row of elements |
| `                   bool                   ` |  expand_x   | If True/False the value will be passed to the Column Elements used to make this feature |
| `                   bool                   ` |  expand_y   | If True/False the value will be passed to the Column Elements used to make this feature |
| Column or List[Column] | **RETURN** | A column element containing the provided element aligned to the center or list of elements (a row)

-----

Align an element or a row of elements to the bottom of the row that contains it

```
vbottom(elem_or_row)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `Element or List[Element] or Tuple[Element]` | elem_or_row | the element or row of elements |
| `                   bool                   ` |  expand_x   | If True/False the value will be passed to the Column Elements used to make this feature |
| `                   bool                   ` |  expand_y   | If True/False the value will be passed to the Column Elements used to make this feature |
| Column or List[Column] | **RETURN** | A column element containing the provided element aligned to the bottom or list of elements (a row)

-----

```
ross(args=*<1 or N object>, kw)
```

-----

### General usage

Main demo(Test Harness)

```
main_DEMO()
```

-----

demo program for testing keyboard

```
main3()
```

-----

### Popups

Popup - Display a popup box with as many parms as you wish to include

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
    icon = ...,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    any_key_closes = False,
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `         str          ` |        title        | Optional title for the window. If none provided, the first arg will be used instead. |
| `   Tuple[str, str]    ` |    button_color     | Color of the buttons shown (text color, button color) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         int          ` |     button_type     | NOT USER SET! Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). There are many Popup functions and they call Popup, changing this parameter to get the desired effect. |
| `         bool         ` |     auto_close      | If True the window will automatically close |
| `         int          ` | auto_close_duration | time in seconds to keep window open before closing it automatically |
| `Tuple[str, str] or str` |     custom_text     | A string or pair of strings that contain the text to display on the buttons |
| `         bool         ` |    non_blocking     | If True then will immediately return from the function without waiting for the user's input. |
| `     str or bytes     ` |        icon         | icon to display on the window. Same format as a Window call |
| `         int          ` |     line_width      | Width of lines in characters. Defaults to MESSAGE_BOX_LINE_WIDTH |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |      location       | Location on screen to display the top left corner of window. Defaults to window centered on screen |
| `         bool         ` |   any_key_closes    | If True then will turn on return_keyboard_events for the window which will cause window to close as soon as any key is pressed. Normally the return key only will close the window. Default is false. |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |
| str or None | **RETURN** | Returns text of the button that was pressed.  None will be returned if user closed window with X

-----

```
popup_scrolled(args=*<1 or N object>,
    button_color = None,
    yes_no = False,
    auto_close = False,
    auto_close_duration = None,
    size = (None, None),
    location = (None, None),
    title = None,
    non_blocking = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `      List[Any]       ` |        args         | The arguments to display |
| `         str          ` |        title        | Title to display in the window. |
| `   Tuple[str, str]    ` |    button_color     | button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |       yes_no        | If True, displays Yes and No buttons instead of Ok |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `   Tuple[int, int]    ` |        size         | (w,h) w=characters-wide, h=rows-high |
| `   Tuple[int, int]    ` |      location       | Location on the screen to place the upper left corner of the window |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |

-----

Show a Popup but without any buttons

```
popup_no_buttons(args=*<1 or N object>,
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
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `   Tuple[str, str]    ` |    button_color     | button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `     bytes or str     ` |        icon         | filename or base64 string to be used for the window's icon |
| `         int          ` |     line_width      | Width of lines in characters |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |
| `   Tuple[int, int]    ` |      location       | Location of upper left corner of the window |

-----

Show Popup box and immediately return (does not block)

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
    icon = ...,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `         str          ` |        title        | Title to display in the window. |
| `   Tuple[str, str]    ` |     button_type     | :param button_color: button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `     bytes or str     ` |        icon         | filename or base64 string to be used for the window's icon |
| `         int          ` |     line_width      | Width of lines in characters |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |
| `   Tuple[int, int]    ` |      location       | Location of upper left corner of the window |

-----

Popup (NonBlocking, Self-closing)

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
    icon = ...,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `         str          ` |        title        | Title to display in the window. |
| `         int          ` |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| `   Tuple[str, str]    ` |    button_color     | button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `     bytes or str     ` |        icon         | filename or base64 string to be used for the window's icon |
| `         int          ` |     line_width      | Width of lines in characters |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |      location       | Location of upper left corner of the window |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |

-----

Same as popup_quick + no titlebar and no buttons

```
popup_quick_message(args=*<1 or N object>,
    title = None,
    button_type = 5,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = True,
    auto_close_duration = 3,
    non_blocking = True,
    icon = ...,
    line_width = None,
    font = None,
    no_titlebar = True,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `         str          ` |        title        | Title to display in the window. |
| `         int          ` |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| `   Tuple[str, str]    ` |    button_color     | button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `     bytes or str     ` |        icon         | filename or base64 string to be used for the window's icon |
| `         int          ` |     line_width      | Width of lines in characters |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |      location       | Location of upper left corner of the window |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |

-----

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
    icon = ...,
    line_width = None,
    font = None,
    grab_anywhere = True,
    keep_on_top = False,
    location = (None, None),
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `         str          ` |        title        | Title to display in the window. |
| `         int          ` |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| `   Tuple[str, str]    ` |    button_color     | button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `     bytes or str     ` |        icon         | filename or base64 string to be used for the window's icon |
| `         int          ` |     line_width      | Width of lines in characters |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |      location       | Location of upper left corner of the window |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |

-----

Popup that closes itself after some time period

```
popup_auto_close(args=*<1 or N object>,
    title = None,
    button_type = 0,
    button_color = None,
    background_color = None,
    text_color = None,
    auto_close = True,
    auto_close_duration = 3,
    non_blocking = False,
    icon = ...,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `         str          ` |        title        | Title to display in the window. |
| `         int          ` |     button_type     | Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). |
| `   Tuple[str, str]    ` |    button_color     | button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `     bytes or str     ` |        icon         | filename or base64 string to be used for the window's icon |
| `         int          ` |     line_width      | Width of lines in characters |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |      location       | Location of upper left corner of the window |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |

-----

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
    icon = ...,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `         str          ` |        title        | Title to display in the window. |
| `   Tuple[str, str]    ` |    button_color     | button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `     bytes or str     ` |        icon         | filename or base64 string to be used for the window's icon |
| `         int          ` |     line_width      | Width of lines in characters |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |      location       | Location of upper left corner of the window |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |

-----

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
    icon = ...,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `         str          ` |        title        | Title to display in the window. |
| `   Tuple[str, str]    ` |    button_color     | button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `     bytes or str     ` |        icon         | filename or base64 string to be used for the window's icon |
| `         int          ` |     line_width      | Width of lines in characters |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |      location       | Location of upper left corner of the window |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |

-----

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
    icon = ...,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `   Tuple[str, str]    ` |    button_color     | button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `     bytes or str     ` |        icon         | filename or base64 string to be used for the window's icon |
| `         int          ` |     line_width      | Width of lines in characters |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |      location       | Location of upper left corner of the window |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |

-----

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
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `   Tuple[str, str]    ` |    button_color     | button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `     bytes or str     ` |        icon         | filename or base64 string to be used for the window's icon |
| `         int          ` |     line_width      | Width of lines in characters |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |      location       | Location of upper left corner of the window |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |
| str or None | **RETURN** | OK, Cancel or None

-----

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
    icon = ...,
    line_width = None,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         Any          ` |        *args        | Variable number of your arguments. Load up the call with stuff to see! |
| `   Tuple[str, str]    ` |    button_color     | button color (foreground, background) |
| `         str          ` |  background_color   | color of background |
| `         str          ` |     text_color      | color of the text |
| `         bool         ` |     auto_close      | if True window will close itself |
| `     int or float     ` | auto_close_duration | Older versions only accept int. Time in seconds until window will close |
| `         bool         ` |    non_blocking     | if True the call will immediately return rather than waiting on user input |
| `     bytes or str     ` |        icon         | filename or base64 string to be used for the window's icon |
| `         int          ` |     line_width      | Width of lines in characters |
| `str or Tuple[str, int]` |        font         | specifies the font family, size, etc |
| `         bool         ` |     no_titlebar     | If True no titlebar will be shown |
| `         bool         ` |    grab_anywhere    | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |     keep_on_top     | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |      location       | Location of upper left corner of the window |
| `     str or bytes     ` |        image        | Image to include at the top of the popup window |
| str or None | **RETURN** | Yes, No or None

-----

Display popup with text entry field and browse button. Browse for folder

```
popup_get_folder(message,
    title = None,
    default_path = "",
    no_window = False,
    size = (None, None),
    button_color = None,
    background_color = None,
    text_color = None,
    icon = ...,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    initial_folder = None,
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         str          ` |     message      | message displayed to user |
| `         str          ` |      title       | Window title |
| `         str          ` |   default_path   | path to display to user as starting point (filled into the input field) |
| `         bool         ` |    no_window     | if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown |
| `   Tuple[int, int]    ` |       size       | (width, height) of the InputText Element |
| `   Tuple[str, str]    ` |   button_color   | button color (foreground, background) |
| `         str          ` | background_color | color of background |
| `         str          ` |    text_color    | color of the text |
| `     bytes or str     ` |       icon       | filename or base64 string to be used for the window's icon |
| `str or Tuple[str, int]` |       font       | specifies the font family, size, etc |
| `         bool         ` |   no_titlebar    | If True no titlebar will be shown |
| `         bool         ` |  grab_anywhere   | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |   keep_on_top    | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |     location     | Location of upper left corner of the window |
| `         str          ` |  initial_folder  | location in filesystem to begin browsing |
| `     str or bytes     ` |      image       | Image to include at the top of the popup window |
| str or None | **RETURN** | Contents of text field. None if closed using X or cancelled

-----

Display popup with text entry field and browse button. Browse for file

```
popup_get_file(message,
    title = None,
    default_path = "",
    default_extension = "",
    save_as = False,
    file_types = (('ALL Files', '*'),),
    no_window = False,
    size = (None, None),
    button_color = None,
    background_color = None,
    text_color = None,
    icon = ...,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    initial_folder = None,
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         str          ` |      message      | message displayed to user |
| `         str          ` |       title       | Window title |
| `         str          ` |   default_path    | path to display to user as starting point (filled into the input field) |
| `         str          ` | default_extension | If no extension entered by user, add this to filename (only used in saveas dialogs) |
| `         bool         ` |      save_as      | if True, the "save as" dialog is shown which will verify before overwriting |
| `         bool         ` |  multiple_files   | if True, then allows multiple files to be selected that are returned with ';' between each filename |
| `Tuple[Tuple[str,str]] ` |    file_types     | List of extensions to show using wildcards. All files (the default) = (("ALL Files", "*.*"),) |
| `         bool         ` |     no_window     | if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown |
| `   Tuple[int, int]    ` |       size        | (width, height) of the InputText Element |
| `   Tuple[str, str]    ` |   button_color    | Color of the button (text, background) |
| `         str          ` | background_color  | color of background |
| `         str          ` |    text_color     | color of the text |
| `     bytes or str     ` |       icon        | filename or base64 string to be used for the window's icon |
| `str or Tuple[str, int]` |       font        | specifies the font family, size, etc |
| `         bool         ` |    no_titlebar    | If True no titlebar will be shown |
| `         bool         ` |   grab_anywhere   | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |    keep_on_top    | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |     location      | Location of upper left corner of the window |
| `         str          ` |  initial_folder   | location in filesystem to begin browsing |
| `     str or bytes     ` |       image       | Image to include at the top of the popup window |
| str or None | **RETURN** | string representing the path chosen, None if cancelled or window closed with X

-----

Display Popup with text entry field

```
popup_get_text(message,
    title = None,
    default_text = "",
    password_char = "",
    size = (None, None),
    button_color = None,
    background_color = None,
    text_color = None,
    icon = ...,
    font = None,
    no_titlebar = False,
    grab_anywhere = False,
    keep_on_top = False,
    location = (None, None),
    image = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `         str          ` |     message      | message displayed to user |
| `         str          ` |      title       | Window title |
| `         str          ` |   default_text   | default value to put into input area |
| `         str          ` |  password_char   | character to be shown instead of actually typed characters |
| `   Tuple[int, int]    ` |       size       | (width, height) of the InputText Element |
| `   Tuple[str, str]    ` |   button_color   | Color of the button (text, background) |
| `         str          ` | background_color | color of background |
| `         str          ` |    text_color    | color of the text |
| `     bytes or str     ` |       icon       | filename or base64 string to be used for the window's icon |
| `str or Tuple[str, int]` |       font       | specifies the font family, size, etc |
| `         bool         ` |   no_titlebar    | If True no titlebar will be shown |
| `         bool         ` |  grab_anywhere   | If True, than can grab anywhere to move the window (Default = False) |
| `         bool         ` |   keep_on_top    | If True the window will remain above all current windows |
| `   Tuple[int, int]    ` |     location     | (x,y) Location on screen to display the upper left corner of window |
| `     str or bytes     ` |      image       | Image to include at the top of the popup window |
| str or None | **RETURN** | Text entered or None if window was closed

-----

### Themes

Sets / Gets the current Theme.  If none is specified then returns the current theme.
This call replaces the ChangeLookAndFeel / change_look_and_feel call which only sets the theme.

```
theme(new_theme = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the background color currently in use
Used for Windows and containers (Column, Frame, Tab) and tables

```
theme_background_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the background color currently in use for all elements except containers

```
theme_element_background_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the text color currently in use

```
theme_text_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the input element background color currently in use

```
theme_input_background_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the input element entry color (not the text but the thing that's displaying the text)

```
theme_input_text_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the button color currently in use

```
theme_button_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the progress bar colors by the current color theme

```
theme_progress_bar_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the slider color (used for sliders)

```
theme_slider_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the border width currently in use
Used by non ttk elements at the moment

```
theme_border_width(border_width = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the slider border width currently in use

```
theme_slider_border_width(border_width = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the progress meter border width currently in use

```
theme_progress_bar_border_width(border_width = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Sets/Returns the text color used by elements that have text as part of their display (Tables, Trees and Sliders)

```
theme_element_text_color(color = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Returns a sorted list of the currently available color themes

```
theme_list()
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

-----

Add a new theme to the dictionary of themes

```
theme_add_new(new_theme_name, new_theme_dict)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `str ` | new_theme_name | text to display in element |
| `dict` | new_theme_dict | text to display in element |

-----

Show a window with all of the color themes - takes a while so be patient

```
theme_previewer(columns = 12)
```

-----

### Util

Dumps an Object's values as a formatted string.  Very nicely done. Great way to display an object's member variables in human form
Returns only the top-most object's variables instead of drilling down to dispolay more

# object to str
# Great for dumping debug data

```
obj_to_single_str_obj(obj)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `Any` | obj | The object to display |
| (str) | **RETURN** | Formatted output of the object's values

-----

Dumps an Object's values as a formatted string.  Very nicely done. Great way to display an object's member variables in human form

```
obj_to_string(obj, extra = "    ")
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `Any` |  obj  | The object to display |
| `str` | extra | extra stuff (Default value = ' ') |
| (str) | **RETURN** | Formatted output of the object's values

-----

```
genUUID()
```

-----

SS == 2 Stretch on ends in row

[row] >input>(SS)-output> [Stretch, row,  Stretch]

```
SS(row)
```

-----

```
frameit(layout)
```

-----

```
convert_args_to_single_string(args=*<1 or N object>)
```

-----

Determines the OS is Linux by using sys.platform

Returns True if Linux

```
running_linux()
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| (bool) | **RETURN** | True if sys.platform indicates running Linux

-----

Determines the OS is Mac by using sys.platform

Returns True if Mac

```
running_mac()
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| (bool) | **RETURN** | True if sys.platform indicates running Mac

-----

Determines the OS is Windows by using sys.platform

Returns True if Windows

```
running_windows()
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| (bool) | **RETURN** | True if sys.platform indicates running Windows

-----

A special case for Trinket.  Checks both the OS and the number of environment variables
Currently, Trinket only has ONE environment variable.  This fact is used to figure out if Trinket is being used.

Returns True if "Trinket" (in theory)

```
running_trinket()
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| (bool) | **RETURN** | True if sys.platform indicates Linux and the number of environment variables is 1

-----

```
is_psg_element(x)
```

-----

```
is_psg_element_row(x)
```

-----

### Version Info

Returns a human-readable string of version numbers for:
- Python version
- PySimpleGUI version
- PySimpleGUI Port-specific name
- PySimpleGUI Port-specific version
- The location of the PySimpleGUI file

```
get_versions()
```

-----

Returns a human-readable dict of version numbers for:
- Python version
- PySimpleGUI version
- PySimpleGUI Port-specific name
- PySimpleGUI Port-specific version
- The location of the PySimpleGUI file

```
get_versions_dict()
```

-----

### miniDemo as a function

```
keyboard_input_testing_DEMO()
```

-----

 -----------

## Version Info

1 Work with TABS/SPACES

2 Tree_Node is class for
	parsing menudef
	as multiline text
	with indented format for nested nodes

3 Usage:
	result_menudef_for__sg_Menu_class = Tree_Node.multiline_str2PySimgpleGUIMenu_Def("...<multiline text>...")
```
menubar_Tree_Node(indented_line)
```

```python
as_dict()
```

---

```
make_psg_list(tree, lvl = 0)
```

---

```
multiline_str2PySimgpleGUIMenu_Def(x)
```

---

```
gen_menubar(version = 0)
```

---

---
### non-pep8 methods for menubar_Tree_Node Element

---

## Class for wrapping your data in Tree element

Data holder in Tree element

```python
TreeData()
```

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
|:---:|:---:|:---:|
| `str(yes, string, and not Node object)` | parent | the parent Node |
| `    str or int or tuple or object    ` |  key   | Used to uniquely identify this node |
| `                 str                 ` |  text  | The text that is displayed at this node's location |
| `              List[Any]              ` | values | The list of values that are displayed at this node |
| `            str or bytes             ` |  icon  | icon |

---

---
### non-pep8 methods for TreeData Element

```
Node(parent,
    key,
    text,
    values,
    icon = None)
```

---

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
|:---:|:---:|:---:|
| `str(yes, string, and not Node object)` | parent | the parent Node |
| `    str or int or tuple or object    ` |  key   | Used to uniquely identify this node |
| `                 str                 ` |  text  | The text that is displayed at this node's location |
| `              List[Any]              ` | values | The list of values that are displayed at this node |
| `            str or bytes             ` |  icon  | icon |

---

---

## SystemTray for controlling icons at statusbar(line in on of the sides (usually bottom) of your screen)

SystemTray - create an icon in the system tray

```
SystemTray(menu = None,
    data = None,
    data_base64 = None,
    filename = None,
    metadata = None,
    tooltip = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `List[List[List[str] or str]]` |    menu     | Menu definition. Example - ['UNUSED', ['My', 'Simple', '---', 'Menu', 'Exit']] |
| `            str             ` |  filename   | filename for icon |
| `           bytes            ` |    data     | in-ram image for icon (same as data_base64 parm) |
| `           bytes            ` | data_base64 | base-64 data for icon |
| `            str             ` |   tooltip   | tooltip string |
| `            Any             ` |  metadata   | User metadata that can be set to ANYTHING |

Reads the context menu

```
read(timeout = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

---

```python
hide()
```

---

```python
un_hide()
```

---

Shows a balloon above icon in system tray

```
show_message(title,
    message,
    filename = None,
    data = None,
    data_base64 = None,
    messageicon = None,
    time = 10000)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

---

```python
close()
```

---

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
|:---:|:---:|:---:|

---

---
### non-pep8 methods for SystemTray Element

```python
close()
```

---

```python
hide()
```

---

Reads the context menu

```
read(timeout = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

---

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
|:---:|:---:|:---:|

---

```python
un_hide()
```

---

Shows a balloon above icon in system tray

```
show_message(title,
    message,
    filename = None,
    data = None,
    data_base64 = None,
    messageicon = None,
    time = 10000)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

---

---

## Window - holds all layout and starts gui loop

Represents a single Window
```
Window(title,
    layout = None,
    alpha_channel = 1,
    auto_close = False,
    auto_close_duration = 3,
    auto_size_buttons = None,
    auto_size_text = None,
    background_color = None,
    background_image = None,
    border_depth = None,
    button_color = None,
    default_button_element_size = (None, None),
    default_element_size = (250, 22),
    disable_close = False,
    disable_minimize = False,
    element_justification = "float",
    element_padding = None,
    finalize = False,
    font = None,
    force_toplevel = False,
    grab_anywhere = False,
    icon = ...,
    keep_on_top = False,
    location = (None, None),
    margins = (None, None),
    metadata = None,
    no_titlebar = False,
    progress_bar_color = (None, None),
    resizable = True,
    return_keyboard_events = False,
    size = (None, None),
    text_justification = None,
    use_default_focus = True,
    return_keyboard_events_as_namedtuple = False,
    is_verbose_css_update = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `                     str                     ` |                title                 | The title that will be displayed in the Titlebar and on the Taskbar |
| `            List[List[Elements]]             ` |                layout                | The layout for the window. Can also be specified in the Layout method |
| `      Tuple[int, int] - (width, height)      ` |         default_element_size         | size in characters (wide) and rows (high) for all elements in this window |
| `               Tuple[int, int]               ` |     default_button_element_size      | (width, height) size in characters (wide) and rows (high) for all Button elements in this window |
| `                    bool                     ` |            auto_size_text            | True if Elements in Window should be sized to exactly fir the length of text |
| `                    bool                     ` |          auto_size_buttons           | True if Buttons in this Window should be sized to exactly fit the text on this. |
| `               Tuple[int, int]               ` |               location               | (x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen. |
| `                    bool                     ` | return_keyboard_events_as_namedtuple | if True, then pressed keys will return special sg.KeyKnife object, not string (as default behaviour) |
| `               Tuple[int, int]               ` |                 size                 | (width, height) size in pixels for this window. Normally the window is autosized to fit contents, not set to an absolute size by the user |
| `  Tuple[int, int] or ((int, int),(int,int))  ` |           element_padding            | Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom)) |
| `               Tuple[int, int]               ` |               margins                | (left/right, top/bottom) Not yet implemented! Parameter here for potability purposes. |
| `Tuple[str, str] == (text color, button color)` |             button_color             | Default button colors for all buttons in the window |
| `           str or Tuple[str, int]            ` |                 font                 | specifies the font family, size, etc |
| `               Tuple[str, str]               ` |          progress_bar_color          | (bar color, background color) Sets the default colors for all progress bars in the window |
| `                     str                     ` |           background_color           | color of background |
| `                     int                     ` |             border_depth             | Default border depth (width) for all elements in the window |
| `                    bool                     ` |              auto_close              | If True, the window will automatically close itself |
| `                     int                     ` |         auto_close_duration          | Number of seconds to wait before closing the window |
| `                 str or str                  ` |                 icon                 | Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO |
| `                    bool                     ` |            force_toplevel            | If True will cause this window to skip the normal use of a hidden master window |
| `                    float                    ` |            alpha_channel             | Sets the opacity of the window. 0 = invisible 1 = completely visible. Values bewteen 0 & 1 will produce semi-transparent windows in SOME environments (The Raspberry Pi always has this value at 1 and cannot change. |
| `                    bool                     ` |        return_keyboard_events        | if True key presses on the keyboard will be returned as Events from Read calls |
| `                    bool                     ` |          use_default_focus           | If True will use the default focus algorithm to set the focus to the "Correct" element |
| `        'left' or 'right' or 'center'        ` |          text_justification          | Default text justification for all Text Elements in window |
| `                     str                     ` |        element_justification         | All elements in the Window itself will have this justification 'left', 'right', 'center' are valid values |
| `                    bool                     ` |             no_titlebar              | If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar |
| `                    bool                     ` |            grab_anywhere             | If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems |
| `                    bool                     ` |             keep_on_top              | If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm |
| `                    bool                     ` |              resizable               | If True, allows the user to resize the window. Note the not all Elements will change size or location when resizing. |
| `                    bool                     ` |            disable_close             | If True, the X button in the top right corner of the window will no work. Use with caution and always give a way out toyour users |
| `                    bool                     ` |           disable_minimize           | if True the user won't be able to minimize window. Good for taking over entire screen and staying that way. |
| `                     ???                     ` |           background_image           | ??? |
| `                    bool                     ` |               finalize               | If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code |
| `                     Any                     ` |               metadata               | User metadata that can be set to ANYTHING |
| `                     Any                     ` |        is_verbose_css_update         | if True -> then will output debug info to stdout |

```python
refresh_css()
```

---

```python
setup_qt_for_qmainwindow()
```

---

```
update_css(dont_update = False, css_props)
```

---

get all radio buttons within "radio_group_id"

```
groupip2btns(radio_group_id)
```

---

get selected radio buttons in "radio radio_group_id"

```
groupid2sel_radio(radio_group_id)
```

---

```python
clear_msg()
```

---

```
show_msg(msg, delay = 0)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `str` |  msg  | message to show |
| `int` | delay | show message after delay ms |

---

```
show(non_blocking = False)
```

---

```
increment_open_count()
```

---

```
decrement_open_count()
```

---

Parms are a variable number of Elements

```
add_row(args=*<1 or N object>)
```

---

```
add_rows(rows)
```

---

```
layout(rows)
```

---

```
layout_and_read(rows, non_blocking = False)
```

---

```
layout_and_show(rows)
```

---

```
set_icon(icon = None, pngbase64 = None)
```

---

THE biggest deal method in the Window class! This is how you get all of your data from your Window.
	Pass in a timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key
	if no other GUI events happen first.
Use the close parameter to close the window after reading

```
read(timeout = None,
    timeout_key = "__TIMEOUT__",
    close = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `int ` |   timeout   | Milliseconds to wait until the Read will return IF no other GUI events happen first |
| `Any ` | timeout_key | The value that will be returned from the call if the timer expired |
| `bool` |    close    | if True the window will be closed prior to returning |
| Tuple[(Any), Dict[Any:Any] or List[Any] or None] | **RETURN** | (event, values)

---

```python
finalize()
```

---

```python
refresh()
```

---

```python
visibility_changed()
```

---

```
fill(values_dict)
```

---

```
find_element(key, silent_on_error = False)
```

---

```python
find_element_with_focus()
```

---

```
save_to_disk(filename)
```

---

```
load_from_disk(filename)
```

---

```python
get_screen_dimensions()
```

---

```
move(x, y)
```

---

```python
minimize()
```

---

```python
maximize()
```

---

```
start_move(event)
```

---

```
stop_move(event)
```

---

```
on_motion(event)
```

---

```python
close()
```

---

```python
adjust()
```

---

```python
disable()
```

---

```python
enable()
```

---

```python
hide()
```

---

```python
un_hide()
```

---

```python
disappear()
```

---

```python
reappear()
```

---

Change the window's transparency

```
set_alpha(alpha)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

---

```python
bring_to_front()
```

---

```python
current_location()
```

---

Change the title of the window

```
set_title(title)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `str` | title | The string to set the title to |

---

---
### non-pep8 methods for Window Element

Parms are a variable number of Elements

```
add_row(args=*<1 or N object>)
```

---

```
add_rows(rows)
```

---

```python
bring_to_front()
```

---

```python
close()
```

---

```python
current_location()
```

---

```
decrement_open_count()
```

---

```python
disable()
```

---

```python
disappear()
```

---

```python
enable()
```

---

```
fill(values_dict)
```

---

```python
finalize()
```

---

```
find_element(key, silent_on_error = False)
```

---

```
find_element(key, silent_on_error = False)
```

---

```python
find_element_with_focus()
```

---

```python
get_screen_dimensions()
```

---

```python
hide()
```

---

```
increment_open_count()
```

---

```
layout(rows)
```

---

```
layout_and_read(rows, non_blocking = False)
```

---

```
layout_and_show(rows)
```

---

```
load_from_disk(filename)
```

---

```python
maximize()
```

---

```python
minimize()
```

---

```
move(x, y)
```

---

```
on_motion(event)
```

---

THE biggest deal method in the Window class! This is how you get all of your data from your Window.
	Pass in a timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key
	if no other GUI events happen first.
Use the close parameter to close the window after reading

```
read(timeout = None,
    timeout_key = "__TIMEOUT__",
    close = False)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `int ` |   timeout   | Milliseconds to wait until the Read will return IF no other GUI events happen first |
| `Any ` | timeout_key | The value that will be returned from the call if the timer expired |
| `bool` |    close    | if True the window will be closed prior to returning |
| Tuple[(Any), Dict[Any:Any] or List[Any] or None] | **RETURN** | (event, values)

---

```python
reappear()
```

---

```python
refresh()
```

---

```
save_to_disk(filename)
```

---

Change the window's transparency

```
set_alpha(alpha)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|

---

```
set_icon(icon = None, pngbase64 = None)
```

---

```
show(non_blocking = False)
```

---

```
start_move(event)
```

---

```
stop_move(event)
```

---

```python
un_hide()
```

---

```python
visibility_changed()
```

---

```python
close()
```

---

```python
close()
```

---

---

## QtStyle class for elemnts css attrbites

Easy to use:

1. Make a QtStyle object: `test1 = QtStyle(...)`
2. fill properties with `test1['key'] = val`:
```
test1['margin'] = 5
test1['margin'] = (10, 20)
```
3. build css
```
css = test1.build_css_string()
print(css)
...
```

API

```
# step 1 - make a style
ss = QtStyle(QLabel, widget__object_name)
ss = QtStyle('QGroupBox', a_objectname, ':title', psg_element=element)

# step 2 - add fields
ss['font'] = create_style_from_font()
ss['background-color'] = (color, color_default)
ss['color'] = (color, color_default)
# step 2.1 - add additions
ss.append_css_to_end.append(" QScrollBar:vertical { ... some css here ...  } ")
# step 2.2 - add anchor
ss.my_subelement_anchor = '::chunk'

# step 3 - build result
css_str = ss.build_css_string()
qt_widget.setStyleSheet(css_str)

====== Special fields
- font
- margin
Why they are special? Because of the formatting.

```

<!-- made by nngogol -->
```
QtStyle(widget_Typename = "",
    widget__object_name = None,
    my_subelement_anchor = None,
    psg_element = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `  str  ` |   widget_Typename    | 'QPushButton', 'QGroupBox', 'QCheckbox' etc |
| `  str  ` | widget__object_name  | 'objectName1' |
| `  str  ` | my_subelement_anchor | ':title' |
| `Element` |     psg_element      | Button, Frame element |

Check if a given property EXISTS in qt Spec

```
is_valid_css_prop(a_css_prop)
```

---

```
build_css_string(style = None)
```

---

---
### non-pep8 methods for QtStyle Element

---

## QuickMeter

```
QuickMeter(title,
    current_value,
    max_value,
    key,
    args=*<1 or N object>,
    orientation = "v",
    bar_color = (None, None),
    button_color = (None, None),
    size = (200, 20),
    border_width = None,
    grab_anywhere = False)
```

---
### non-pep8 methods for QuickMeter Element

```
BuildWindow(args=*<1 or N object>)
```

---

```
UpdateMeter(current_value,
    max_value,
    args=*<1 or N object>)
```

---

```python
ComputeProgressStats()
```

---

---

Button Element - Defines all possible buttons. The shortcuts such as Submit, FileBrowse, ... each create a Button

InputText - shows 1line input text.

## Combo Element

Combo - same as listbox, but has drop-down menu.
User can type in their own value or choose from list.

Input Combo Box Element (also called Dropdown box)

```
Combo(values,
    auto_complete = True,
    right_click_menu = None,
    auto_size_text = None,
    background_color = None,
    change_submits = False,
    default_value = None,
    vertical_alignment = None,
    horizontal_alignment = None,
    disabled = False,
    enable_events = False,
    font = None,
    k = None,
    key = None,
    metadata = None,
    pad = None,
    readonly = False,
    size = (None, None),
    size_px = (None, None),
    text_color = None,
    tooltip = None,
    visible = True,
    visible_items = 10)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `                        List[Any] or Tuple[Any]                         ` |        values        | values to choose. While displayed as text, the items returned are what the caller supplied, not text |
| `                                  Any                                   ` |    default_value     | Choice to be displayed as initial value. Must match one of values variable contents |
| `                    Tuple[int, int] (width, height)                     ` |         size         | width = characters-wide, height = rows-high |
| `                                  bool                                  ` |    auto_size_text    | True if element should be the same size as the contents |
| `                                  str                                   ` |   background_color   | Color for Element. Text or RGB Hex |
| `                                  str                                   ` |      text_color      | color of the text |
| `                                  bool                                  ` |    change_submits    | DEPRICATED DO NOT USE. Use `enable_events` instead |
| `                                  bool                                  ` |    enable_events     | Turns on the element specific events. Combo event is when a choice is made |
| `                   List[List[Tuple[str, List[str]]]]                    ` |   right_click_menu   | a menu definition (in menu definition format) |
| `                                  bool                                  ` |       disabled       | set disable state for element |
| `                                  str                                   ` |  vertical_alignment  | Place it at the 'top', 'vcenter', 'bottom', 'baseline' of the row (can also use 't','cv' or 'c','b', 'bs' or 'bl'). Defaults to no setting (it automatically decides) |
| `                                  str                                   ` | horizontal_alignment | Place it at the 'left', 'hcenter', 'right', 'justify' of the row (can also use 'l','ch' or 'cc','r', 'j'). Defaults to no setting (it automatically decides) |
| `                                  Any                                   ` |         key          | Used with window.FindElement and with return values to uniquely identify this element |
| `                     str or int or tuple or object                      ` |          k           | Same as the Key. You can use either k or key. Which ever is set will be used. |
| `(int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int)` |         pad          | Amount of padding to put around element in pixels (left/right, top/bottom) |
| `                                  str                                   ` |       tooltip        | text that will appear when mouse hovers over this element |
| `                                  bool                                  ` |       readonly       | make element readonly (user can't change). True means user cannot change |
| `                                  ???                                   ` |    visible_items     | ??? |
| `                         str or Tuple[str, int]                         ` |         font         | specifies the font family, size, etc |
| `                                  ???                                   ` |    auto_complete     | ??? |
| `                                  bool                                  ` |       visible        | set visibility state of the element |
| `                    Tupple[int, int] (width, height)                    ` |       size_px        | size in pixels (width, height). Will override the size parameter |
| `                                  Any                                   ` |       metadata       | User metadata that can be set to ANYTHING |

```
update(value = None,
    values = None,
    set_to_index = None,
    readonly = None,
    disabled = None,
    visible = None,
    font = None,
    background_color = None,
    text_color = None,
    padding = None,
    margin = None,
    elem_size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `    Element    ` |      value       | object to select in combo |
| ` List[Element] ` |      values      | set new list of elements |
| `      int      ` |   set_to_index   | int index to select in combo |
| `     bool      ` |     readonly     | makes a combo readonly |
| `Tuple[int,int] ` |    elem_size     | size of element in pixels |
| `      str      ` |       font       | your font in string format |
| `      int      ` |   border_width   | border width of element |
| `      str      ` | background_color | color in string format |
| `      str      ` |    text_color    | text color in string format |
| `     bool      ` |     disabled     | BOOL enable or disable state |
| `     bool      ` |     visible      | BOOL visible of hidden state |
| `Union[list,int]` |     padding      | padding (from box-model) |
| `Union[list,int]` |       pad        | same as padding |
| `Union[list,int]` |      margin      | margin (from box-model) |

---

```
update(value = None,
    values = None,
    set_to_index = None,
    readonly = None,
    disabled = None,
    visible = None,
    font = None,
    background_color = None,
    text_color = None,
    padding = None,
    margin = None,
    elem_size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `    Element    ` |      value       | object to select in combo |
| ` List[Element] ` |      values      | set new list of elements |
| `      int      ` |   set_to_index   | int index to select in combo |
| `     bool      ` |     readonly     | makes a combo readonly |
| `Tuple[int,int] ` |    elem_size     | size of element in pixels |
| `      str      ` |       font       | your font in string format |
| `      int      ` |   border_width   | border width of element |
| `      str      ` | background_color | color in string format |
| `      str      ` |    text_color    | text color in string format |
| `     bool      ` |     disabled     | BOOL enable or disable state |
| `     bool      ` |     visible      | BOOL visible of hidden state |
| `Union[list,int]` |     padding      | padding (from box-model) |
| `Union[list,int]` |       pad        | same as padding |
| `Union[list,int]` |      margin      | margin (from box-model) |

---

## OptionMenu Element

Available ONLY in PySimpleGUI(tkinter port)

```
OptionMenu(args=*<1 or N object>, kw)
```

```
update(args=*<1 or N object>, kw)
```

---

```
update(args=*<1 or N object>, kw)
```

---

## Listbox Element

List Box - select 1 or N values.
Returns a list of selected rows in the window.read() call

```
Listbox(values,
    auto_size_text = None,
    background_color = None,
    bind_return_key = False,
    no_scrollbar = None,
    change_submits = False,
    right_click_menu = None,
    vertical_alignment = None,
    horizontal_alignment = None,
    default_values = None,
    disabled = False,
    enable_events = False,
    font = None,
    k = None,
    key = None,
    metadata = None,
    pad = None,
    select_mode = None,
    size = (None, None),
    size_px = (None, None),
    text_color = None,
    tooltip = None,
    visible = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `                        List[Any] or Tuple[Any]                         ` |        values        | list of values to display. Can be any type including mixed types as long as they have __str__ method |
| `                               List[Any]                                ` |    default_values    | which values should be initially selected |
| `                                 [enum]                                 ` |     select_mode      | Select modes are used to determine if only 1 item can be selected or multiple and how they can be selected. Valid choices begin with "LISTBOX_SELECT_MODE_" and include: LISTBOX_SELECT_MODE_SINGLE LISTBOX_SELECT_MODE_MULTIPLE LISTBOX_SELECT_MODE_BROWSE LISTBOX_SELECT_MODE_EXTENDED |
| `                                  bool                                  ` |    change_submits    | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
| `                                  bool                                  ` |    enable_events     | Turns on the element specific events. Listbox generates events when an item is clicked |
| `                                  bool                                  ` |   bind_return_key    | If True, then the return key will cause a the Listbox to generate an event |
| `                                  bool                                  ` |     no_scrollbar     | If True, then no scrollbar will be shown |
| `                    Tuple(int, int) (width, height)                     ` |         size         | width = characters-wide, height = rows-high |
| `                                  bool                                  ` |       disabled       | set disable state for element |
| `                                  str                                   ` |  vertical_alignment  | Place it at the 'top', 'vcenter', 'bottom', 'baseline' of the row (can also use 't','cv' or 'c','b', 'bs' or 'bl'). Defaults to no setting (it automatically decides) |
| `                                  str                                   ` | horizontal_alignment | Place it at the 'left', 'hcenter', 'right', 'justify' of the row (can also use 'l','ch' or 'cc','r', 'j'). Defaults to no setting (it automatically decides) |
| `                   List[List[Tuple[str, List[str]]]]                    ` |   right_click_menu   | a menu definition (in menu definition format) |
| `                                  bool                                  ` |    auto_size_text    | True if element should be the same size as the contents |
| `                         str or Tuple[str, int]                         ` |         font         | specifies the font family, size, etc |
| `                                  str                                   ` |   background_color   | color of background |
| `                                  str                                   ` |      text_color      | color of the text |
| `                                  Any                                   ` |         key          | Used with window.FindElement and with return values to uniquely identify this element |
| `                     str or int or tuple or object                      ` |          k           | Same as the Key. You can use either k or key. Which ever is set will be used. |
| `(int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int)` |         pad          | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| `                                  str                                   ` |       tooltip        | text, that will appear when mouse hovers over the element |
| `                                  bool                                  ` |       visible        | set visibility state of the element |
| `                    Tuple[int, int] (width, height)                     ` |       size_px        | size in pixels (width, height). Will override the size parameter |
| `                                  Any                                   ` |       metadata       | User metadata that can be set to ANYTHING |

```
update(value = None,
    values = None,
    set_to_index = None,
    select_this_value = None,
    disabled = None,
    visible = None,
    font = None,
    background_color = None,
    text_color = None,
    padding = None,
    margin = None,
    elem_size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `      str      ` |     tooltip      | tooltip to show |
| `     bool      ` |     disabled     | BOOL enable or disable state |
| `     bool      ` |     visible      | BOOL visible of hidden state |
| `Tuple[int,int] ` |    elem_size     | size of element in pixels |
| `      str      ` |       font       | your font in string format |
| `      int      ` |   border_width   | border width of element |
| `      str      ` | background_color | color in string format |
| `Union[list,int]` |     padding      | padding (from box-model) |
| `Union[list,int]` |       pad        | same as padding |
| `Union[list,int]` |      margin      | margin (from box-model) |

---

Gets the current value of the Element as it would be represented in the results dictionary.
Normally you would NOT be using this method, but instead using the return values dictionary
that is returned from reading your window

`get()`

|Type|Name|Meaning|
|:---:|:---:|:---:|
|<type>| **return** |  |

---

```
set_value(values)
```

---

```python
get_list_values()
```

---

```
set_value(values)
```

---

```python
get_list_values()
```

---

```
update(value = None,
    values = None,
    set_to_index = None,
    select_this_value = None,
    disabled = None,
    visible = None,
    font = None,
    background_color = None,
    text_color = None,
    padding = None,
    margin = None,
    elem_size = (None, None))
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `      str      ` |     tooltip      | tooltip to show |
| `     bool      ` |     disabled     | BOOL enable or disable state |
| `     bool      ` |     visible      | BOOL visible of hidden state |
| `Tuple[int,int] ` |    elem_size     | size of element in pixels |
| `      str      ` |       font       | your font in string format |
| `      int      ` |   border_width   | border width of element |
| `      str      ` | background_color | color in string format |
| `Union[list,int]` |     padding      | padding (from box-model) |
| `Union[list,int]` |       pad        | same as padding |
| `Union[list,int]` |      margin      | margin (from box-model) |

---

## Radio Element

Radio - select 1 choice from button group of radios

```
Radio(text,
    group_id,
    default = False,
    disabled = False,
    auto_size_text = None,
    background_color = None,
    change_submits = False,
    vertical_alignment = None,
    horizontal_alignment = None,
    enable_events = False,
    font = None,
    k = None,
    key = None,
    metadata = None,
    pad = None,
    size = (None, None),
    size_px = (None, None),
    text_color = None,
    tooltip = None,
    visible = True)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `                                  str                                   ` |         text         | Text to display next to button |
| `                                  Any                                   ` |       group_id       | Groups together multiple Radio Buttons. Any type works |
| `                                  bool                                  ` |       default        | Set to True for the one element of the group you want initially selected |
| `                                  bool                                  ` |       disabled       | set disable state |
| `                            Tuple[int, int]                             ` |         size         | (width, height) width = characters-wide, height = rows-high |
| `                                  bool                                  ` |    auto_size_text    | if True will size the element to match the length of the text |
| `                                  str                                   ` |  vertical_alignment  | Place it at the 'top', 'vcenter', 'bottom', 'baseline' of the row (can also use 't','cv' or 'c','b', 'bs' or 'bl'). Defaults to no setting (it automatically decides) |
| `                                  str                                   ` | horizontal_alignment | Place it at the 'left', 'hcenter', 'right', 'justify' of the row (can also use 'l','ch' or 'cc','r', 'j'). Defaults to no setting (it automatically decides) |
| `                                  str                                   ` |   background_color   | color of background |
| `                                  str                                   ` |      text_color      | color of the text |
| `                         str or Tuple[str, int]                         ` |         font         | specifies the font family, size, etc |
| `                                  Any                                   ` |         key          | Used with window.FindElement and with return values to uniquely identify this element |
| `                     str or int or tuple or object                      ` |          k           | Same as the Key. You can use either k or key. Which ever is set will be used. |
| `(int, int or (int, int),(int,int) or int,(int,int)) or  ((int, int),int)` |         pad          | Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom)) |
| `                                  str                                   ` |       tooltip        | text, that will appear when mouse hovers over the element |
| `                                  bool                                  ` |    change_submits    | DO NOT USE. Only listed for backwards compat - Use enable_events instead |
| `                                  bool                                  ` |    enable_events     | Turns on the element specific events. Radio Button events happen when an item is selected |
| `                                  bool                                  ` |       visible        | set visibility state of the element |
| `                    Tupple[int, int] (width, height)                    ` |       size_px        | size in pixels (width, height). Will override the size parameter |
| `                                  Any                                   ` |       metadata       | User metadata that can be set to ANYTHING |

```
update(value = None,
    disabled = None,
    visible = None,
    font = None,
    background_color = None,
    text_color = None,
    padding = None,
    margin = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `            bool             ` |      value       | checked or unchecked state for element |
| `            bool             ` |     disabled     | state of element |
| `            bool             ` |     visible      | visibility of element |
| `             str             ` |       font       | (css property) font name and font size. Example: "Mono 20", "Helvetica 30" |
| `             str             ` | background_color | (css property) bg color |
| `             str             ` |    text_color    | (css property) fg color |
| `int or (int[,int], int[,int])` |     padding      | (css property) padding in box-model. Box model explained in psgQt readme.md |
| `int or (int[,int], int[,int])` |      margin      | (css property) margin in box-model. Box model explained in psgQt readme.md |

---

What does this method does?

```python
reset_group()
```

---

```python
get()
```

---

```
update(value = None,
    disabled = None,
    visible = None,
    font = None,
    background_color = None,
    text_color = None,
    padding = None,
    margin = None)
```

Parameter Descriptions:

|Type|Name|Meaning|
|:---:|:---:|:---:|
| `            bool             ` |      value       | checked or unchecked state for element |
| `            bool             ` |     disabled     | state of element |
| `            bool             ` |     visible      | visibility of element |
| `             str             ` |       font       | (css property) font name and font size. Example: "Mono 20", "Helvetica 30" |
| `             str             ` | background_color | (css property) bg color |
| `             str             ` |    text_color    | (css property) fg color |
| `int or (int[,int], int[,int])` |     padding      | (css property) padding in box-model. Box model explained in psgQt readme.md |
| `int or (int[,int], int[,int])` |      margin      | (css property) margin in box-model. Box model explained in psgQt readme.md |

---

1. line11
	* ds1
	* s1
2. line1

