#!/usr/bin/python3
version = __version__ = "0.14.0 Released 17-Nov-2019"

import sys
import wx
import wx.adv
import wx.lib.inspection
from wx.lib.embeddedimage import PyEmbeddedImage
import wx.lib.scrolledpanel
import types
import datetime
import textwrap
import pickle
import os
import time
from random import randint

######           #####                                       #####   #     #  ###  #     #
#     #  #   #  #     #  #  #    #  #####   #       ######  #     #  #     #   #   #  #  #  #    #
#     #   # #   #        #  ##  ##  #    #  #       #       #        #     #   #   #  #  #   #  #
######     #     #####   #  # ## #  #    #  #       #####   #  ####  #     #   #   #  #  #    ##
#          #          #  #  #    #  #####   #       #       #     #  #     #   #   #  #  #    ##
#          #    #     #  #  #    #  #       #       #       #     #  #     #   #   #  #  #   #  #
#          #     #####   #  #    #  #       ######  ######   #####    #####   ###   ## ##   #    #

"""

    21-Dec-2018
    Welcome to the "core" PySimpleGUIWx port!

:::       ::: :::    ::: :::::::::  :::   ::: ::::::::::: :::    :::  ::::::::  ::::    ::: 
:+:       :+: :+:    :+: :+:    :+: :+:   :+:     :+:     :+:    :+: :+:    :+: :+:+:   :+: 
+:+       +:+  +:+  +:+  +:+    +:+  +:+ +:+      +:+     +:+    +:+ +:+    +:+ :+:+:+  +:+ 
+#+  +:+  +#+   +#++:+   +#++:++#+    +#++:       +#+     +#++:++#++ +#+    +:+ +#+ +:+ +#+ 
+#+ +#+#+ +#+  +#+  +#+  +#+           +#+        +#+     +#+    +#+ +#+    +#+ +#+  +#+#+# 
 #+#+# #+#+#  #+#    #+# #+#           #+#        #+#     #+#    #+# #+#    #+# #+#   #+#+# 
  ###   ###   ###    ### ###           ###        ###     ###    ###  ########  ###    #### 



    This marks the 3rd port of the PySimpleGUI GUI SDK.  Each port gets a little better than
    the previous, in theory.

    It will take a while for this Wx port to be completed, but should be running with a fully selection
    of widgets fairly quickly.  The Qt port required 1 week to get to "Alpha" condition

    Enjoy!
"""

g_time_start = 0
g_time_end = 0
g_time_delta = 0

RUN_INSPECTION_TOOL = False

# Because looks matter...
DEFAULT_BASE64_ICON = b'iVBORw0KGgoAAAANSUhEUgAAACEAAAAgCAMAAACrZuH4AAAABGdBTUEAALGPC/xhBQAAAwBQTFRFAAAAMGmYMGqZMWqaMmubMmycM22dNGuZNm2bNm6bNG2dN26cNG6dNG6eNW+fN3CfOHCeOXGfNXCgNnGhN3KiOHOjOXSjOHSkOnWmOnamOnanPHSiPXakPnalO3eoPnimO3ioPHioPHmpPHmqPXqqPnurPnusPnytP3yuQHimQnurQn2sQH2uQX6uQH6vR32qRn+sSXujSHynTH2mTn+nSX6pQH6wTIGsTYKuTYSvQoCxQoCyRIK0R4S1RYS2Roa4SIe4SIe6SIi7Soq7SYm8SYq8Sou+TY2/UYStUYWvVIWtUYeyVoewUIi0VIizUI6+Vo+8WImxXJG5YI2xZI+xZ5CzZJC0ZpG1b5a3apW4aZm/cZi4dJ2/eJ69fJ+9XZfEZZnCZJzHaZ/Jdp/AeKTI/tM8/9Q7/9Q8/9Q9/9Q+/tQ//9VA/9ZA/9ZB/9ZC/9dD/9ZE/tdJ/9dK/9hF/9hG/9hH/9hI/9hJ/9hK/9lL/9pK/9pL/thO/9pM/9pN/9tO/9tP/9xP/tpR/9xQ/9xR/9xS/9xT/91U/91V/t1W/95W/95X/95Y/95Z/99a/99b/txf/txh/txk/t5l/t1q/t5v/+Bb/+Bc/+Bd/+Be/+Bf/+Bg/+Fh/+Fi/+Jh/+Ji/uJk/uJl/+Jm/+Rm/uJo/+Ro/+Rr/+Zr/+Vs/+Vu/+Zs/+Zu/uF0/uVw/+dw/+dz/+d2/uB5/uB6/uJ9/uR7/uR+/uV//+hx/+hy/+h0/+h2/+l4/+l7/+h8gKXDg6vLgazOhKzMiqrEj6/KhK/Qka/Hk7HJlLHJlLPMmLTLmbbOkLXSmLvXn77XoLrPpr/Tn8DaocLdpcHYrcjdssfZus/g/uOC/uOH/uaB/uWE/uaF/uWK/+qA/uqH/uqI/uuN/uyM/ueS/ueW/ueY/umQ/uqQ/uuS/uuW/uyU/uyX/uqa/uue/uye/uyf/u6f/uyq/u+r/u+t/vCm/vCp/vCu/vCy/vC2/vK2/vO8/vO/wtTjwtXlzdrl/vTA/vPQAAAAiNpY5gAAAQB0Uk5T////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AFP3ByUAAAAJcEhZcwAAFw8AABcPASe7rwsAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjEuMWMqnEsAAAKUSURBVDhPhdB3WE1xHMdxt5JV0dANoUiyd8kqkey996xclUuTlEKidO3qVnTbhIyMW/bee5NskjJLmR/f3++cK/94vP76Ps/n/Zx7z6mE/6koJowcK154vvHOL/GsKCZXkUgkWlf4vWGWq5tsDz+JWIzSokAiqXGe7nWu3HxhEYof7fhOqp1GtptQuMruVhQdxZ05U5G47tYUHbQ4oah6Fg9Z4ubm7i57JhQjdHS0RSzUPoG17u6zZTKZh8c8XlytqW9YWUOH1LqFOZ6enl5ec+XybFb0rweM1tPTM6yuq6vLs0lYJJfLvb19fHwDWGF0jh5lYNAe4/QFemOwxtfXz8/fPyBgwVMqzAcCF4ybAZ2MRCexJGBhYGBQUHDw4u1UHDG1G2ZqB/Q1MTHmzAE+kpCwL1RghlTaBt/6SaXS2kx9YH1IaOjSZST8vfA9JtoDnSngGgL7wkg4WVkofA9mcF1Sx8zMzBK4v3wFiYiMVLxlEy9u21syFhYNmgN7IyJXEYViNZvEYoCVVWOmUVvgQVSUQqGIjolRFvOAFd8HWVs34VoA+6OjY2JjY5Vxm4BC1UuhGG5jY9OUaQXci1MqlfHx8YmqjyhOViW9ZsUN29akJRmPFwkJCZsTSXIpilJffXiTzorLXYgtcxRJKpUqKTklJQ0oSt9FP/EonxVdNY4jla1kK4q2ZB6mIr+AipvduzFUzMSOtLT09IyMzMxtJKug/F0u/6dTexAWDcXXLGEjapKjfsILOLKEuYiSnTQeYCt3UHhbwEHjGMrETfBJU5zq5dSTcXC8hLJccSWP2cgLXHPu7cQNAcpyxF1dyjehAKb0cSYUAOXCUw6V8OFPgevTXFymC+fPPLU677Nw/1X8A/AbfAKGulaqFlIAAAAASUVORK5CYII='


def TimerStart():
    global g_time_start

    g_time_start = time.time()


def TimerStop():
    global g_time_delta, g_time_end

    g_time_end = time.time()
    g_time_delta = g_time_end - g_time_start
    print(g_time_delta)


# ----====----====----==== Constants the user CAN safely change ====----====----====----#
DEFAULT_WINDOW_ICON = 'default_icon.ico'
DEFAULT_ELEMENT_SIZE = (250, 26)  # In pixels
DEFAULT_BUTTON_ELEMENT_SIZE = (10, 1)  # In CHARACTERS
DEFAULT_MARGINS = (10, 5)  # Margins for each LEFT/RIGHT margin is first term
DEFAULT_ELEMENT_PADDING = (3, 2)  # Padding between elements (row, col) in pixels
DEFAULT_AUTOSIZE_TEXT = True
DEFAULT_AUTOSIZE_BUTTONS = True
DEFAULT_FONT = ("Helvetica", 10)
DEFAULT_TEXT_JUSTIFICATION = 'left'
DEFAULT_BORDER_WIDTH = 1
DEFAULT_AUTOCLOSE_TIME = 3  # time in seconds to show an autoclose form
DEFAULT_DEBUG_WINDOW_SIZE = (80, 20)
DEFAULT_WINDOW_LOCATION = (None, None)
MAX_SCROLLED_TEXT_BOX_HEIGHT = 50
DEFAULT_TOOLTIP_TIME = 400
DEFAULT_PIXELS_TO_CHARS_SCALING = (10,26)      # 1 character represents x by y pixels
DEFAULT_PIXELS_TO_CHARS_SCALING_MULTILINE_TEXT = (10,20)      # 1 character represents x by y pixels
DEFAULT_PIXEL_TO_CHARS_CUTOFF = 20             # number of chars that triggers using pixels instead of chars
DEFAULT_PIXEL_TO_CHARS_CUTOFF_MULTILINE = 70             # number of chars that triggers using pixels instead of chars
MENU_DISABLED_CHARACTER = '!'
MENU_KEY_SEPARATOR = '::'

#################### COLOR STUFF ####################
BLUES = ("#082567", "#0A37A3", "#00345B")
PURPLES = ("#480656", "#4F2398", "#380474")
GREENS = ("#01826B", "#40A860", "#96D2AB", "#00A949", "#003532")
YELLOWS = ("#F3FB62", "#F0F595")
TANS = ("#FFF9D5", "#F4EFCF", "#DDD8BA")
NICE_BUTTON_COLORS = ((GREENS[3], TANS[0]),
                      ('#000000', '#FFFFFF'),
                      ('#FFFFFF', '#000000'),
                      (YELLOWS[0], PURPLES[1]),
                      (YELLOWS[0], GREENS[3]),
                      (YELLOWS[0], BLUES[2]))

COLOR_SYSTEM_DEFAULT = '1234567890'  # Colors should never be this long
if sys.platform == 'darwin':
    DEFAULT_BUTTON_COLOR = COLOR_SYSTEM_DEFAULT  # Foreground, Background (None, None) == System Default
    OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR = COLOR_SYSTEM_DEFAULT  # Colors should never be this long
else:
    DEFAULT_BUTTON_COLOR = ('white', BLUES[0])  # Foreground, Background (None, None) == System Default
    OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR = ('white', BLUES[0])  # Colors should never be this long

DEFAULT_ERROR_BUTTON_COLOR = ("#FFFFFF", "#FF0000")
DEFAULT_BACKGROUND_COLOR = None
DEFAULT_ELEMENT_BACKGROUND_COLOR = None
DEFAULT_ELEMENT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR = None
DEFAULT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_INPUT_ELEMENTS_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_INPUT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_SCROLLBAR_COLOR = None
# DEFAULT_BUTTON_COLOR = (YELLOWS[0], PURPLES[0])    # (Text, Background) or (Color "on", Color) as a way to remember
# DEFAULT_BUTTON_COLOR = (GREENS[3], TANS[0])    # Foreground, Background (None, None) == System Default
# DEFAULT_BUTTON_COLOR = (YELLOWS[0], GREENS[4])    # Foreground, Background (None, None) == System Default
# DEFAULT_BUTTON_COLOR = ('white', 'black')    # Foreground, Background (None, None) == System Default
# DEFAULT_BUTTON_COLOR = (YELLOWS[0], PURPLES[2])    # Foreground, Background (None, None) == System Default
# DEFAULT_PROGRESS_BAR_COLOR = (GREENS[2], GREENS[0])     # a nice green progress bar
# DEFAULT_PROGRESS_BAR_COLOR = (BLUES[1], BLUES[1])     # a nice green progress bar
# DEFAULT_PROGRESS_BAR_COLOR = (BLUES[0], BLUES[0])     # a nice green progress bar
# DEFAULT_PROGRESS_BAR_COLOR = (PURPLES[1],PURPLES[0])    # a nice purple progress bar

# A transparent button is simply one that matches the background
TRANSPARENT_BUTTON = ('#F0F0F0', '#F0F0F0')
# --------------------------------------------------------------------------------
# Progress Bar Relief Choices
RELIEF_RAISED = 'raised'
RELIEF_SUNKEN = 'sunken'
RELIEF_FLAT = 'flat'
RELIEF_RIDGE = 'ridge'
RELIEF_GROOVE = 'groove'
RELIEF_SOLID = 'solid'

DEFAULT_PROGRESS_BAR_COLOR = (GREENS[0], '#D0D0D0')  # a nice green progress bar
DEFAULT_PROGRESS_BAR_SIZE = (20, 20)  # Size of Progress Bar (characters for length, pixels for width)
DEFAULT_PROGRESS_BAR_BORDER_WIDTH = 1
DEFAULT_PROGRESS_BAR_RELIEF = RELIEF_GROOVE
PROGRESS_BAR_STYLES = ('default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative')
DEFAULT_PROGRESS_BAR_STYLE = 'default'
DEFAULT_METER_ORIENTATION = 'Horizontal'
DEFAULT_SLIDER_ORIENTATION = 'vertical'
DEFAULT_SLIDER_BORDER_WIDTH = 1
DEFAULT_SLIDER_RELIEF = 00000
DEFAULT_FRAME_RELIEF = 00000

DEFAULT_LISTBOX_SELECT_MODE = 00000
SELECT_MODE_MULTIPLE = 00000
LISTBOX_SELECT_MODE_MULTIPLE = 'multiple'
SELECT_MODE_BROWSE = 00000
LISTBOX_SELECT_MODE_BROWSE = 'browse'
SELECT_MODE_EXTENDED =00000
LISTBOX_SELECT_MODE_EXTENDED = 'extended'
SELECT_MODE_SINGLE = 00000
LISTBOX_SELECT_MODE_SINGLE = 'single'

TABLE_SELECT_MODE_NONE = 00000
TABLE_SELECT_MODE_BROWSE = 00000
TABLE_SELECT_MODE_EXTENDED = 00000
DEFAULT_TABLE_SECECT_MODE = TABLE_SELECT_MODE_EXTENDED

TITLE_LOCATION_TOP = 00000
TITLE_LOCATION_BOTTOM = 00000
TITLE_LOCATION_LEFT = 00000
TITLE_LOCATION_RIGHT = 00000
TITLE_LOCATION_TOP_LEFT = 00000
TITLE_LOCATION_TOP_RIGHT = 00000
TITLE_LOCATION_BOTTOM_LEFT = 00000
TITLE_LOCATION_BOTTOM_RIGHT = 00000

THEME_DEFAULT = 'default'
THEME_WINNATIVE = 'winnative'
THEME_CLAM = 'clam'
THEME_ALT = 'alt'
THEME_CLASSIC = 'classic'
THEME_VISTA = 'vista'
THEME_XPNATIVE = 'xpnative'

# DEFAULT_METER_ORIENTATION = 'Vertical'
# ----====----====----==== Constants the user should NOT f-with ====----====----====----#
ThisRow = 555666777  # magic number

# DEFAULT_WINDOW_ICON = ''
MESSAGE_BOX_LINE_WIDTH = 60

# "Special" Key Values.. reserved
# Key representing a Read timeout
TIMEOUT_KEY = '__TIMEOUT__'
# Key indicating should not create any return values for element
WRITE_ONLY_KEY = '__WRITE ONLY__'
EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED = '__DOUBLE_CLICKED__'
EVENT_SYSTEM_TRAY_ICON_ACTIVATED = '__ACTIVATED__'
EVENT_SYSTEM_TRAY_ICON_RIGHT_CLICK = '__RIGHT_CLICK__'
EVENT_SYSTEM_TRAY_MESSAGE_CLICKED = '__MESSAGE_CLICKED__'

# Icons for displaying system tray messages
SYSTEM_TRAY_MESSAGE_ICON_INFORMATION = wx.ICON_INFORMATION
SYSTEM_TRAY_MESSAGE_ICON_WARNING = wx.ICON_WARNING
SYSTEM_TRAY_MESSAGE_ICON_CRITICAL = wx.ICON_ERROR
SYSTEM_TRAY_MESSAGE_ICON_NOICON = None

ICON_SCREEN_DEPTH = -1

ICON_STOP = 512

# a shameful global variable. This represents the top-level window information. Needed because opening a second window is different than opening the first.
class MyWindows():
    def __init__(self):
        self.NumOpenWindows = 0
        self.user_defined_icon = None
        self.hidden_master_root = None

    def Decrement(self):
        self.NumOpenWindows -= 1 * (self.NumOpenWindows != 0)  # decrement if not 0
        # print('---- DECREMENTING Num Open Windows = {} ---'.format(self.NumOpenWindows))

    def Increment(self):
        self.NumOpenWindows += 1
        # print('++++ INCREMENTING Num Open Windows = {} ++++'.format(self.NumOpenWindows))


_my_windows = MyWindows()  # terrible hack using globals... means need a class for collecing windows


# ====================================================================== #
# One-liner functions that are handy as f_ck                             #
# ====================================================================== #
def RGB(red, green, blue): return '#%02x%02x%02x' % (red, green, blue)


# ====================================================================== #
# Enums for types                                                        #
# ====================================================================== #
# -------------------------  Button types  ------------------------- #
# todo Consider removing the Submit, Cancel types... they are just 'RETURN' type in reality
# uncomment this line and indent to go back to using Enums
# class ButtonType(Enum):
BUTTON_TYPE_BROWSE_FOLDER = 1
BUTTON_TYPE_BROWSE_FILE = 2
BUTTON_TYPE_BROWSE_FILES = 21
BUTTON_TYPE_SAVEAS_FILE = 3
BUTTON_TYPE_CLOSES_WIN = 5
BUTTON_TYPE_CLOSES_WIN_ONLY = 6
BUTTON_TYPE_READ_FORM = 7
BUTTON_TYPE_REALTIME = 9
BUTTON_TYPE_CALENDAR_CHOOSER = 30
BUTTON_TYPE_COLOR_CHOOSER = 40

# -------------------------  Element types  ------------------------- #
# class ElementType(Enum):
ELEM_TYPE_TEXT = 'text'
ELEM_TYPE_INPUT_TEXT = 'input'
ELEM_TYPE_INPUT_COMBO = 'combo'
ELEM_TYPE_INPUT_OPTION_MENU = 'option menu'
ELEM_TYPE_INPUT_RADIO = 'radio'
ELEM_TYPE_INPUT_MULTILINE = 'multiline'
ELEM_TYPE_MULTILINE_OUTPUT = 'multioutput'
ELEM_TYPE_INPUT_CHECKBOX = 'checkbox'
ELEM_TYPE_INPUT_SPIN = 'spin'
ELEM_TYPE_BUTTON = 'button'
ELEM_TYPE_BUTTONMENU = 'buttonmenu'
ELEM_TYPE_IMAGE = 'image'
ELEM_TYPE_CANVAS = 'canvas'
ELEM_TYPE_FRAME = 'frame'
ELEM_TYPE_GRAPH = 'graph'
ELEM_TYPE_TAB = 'tab'
ELEM_TYPE_TAB_GROUP = 'tabgroup'
ELEM_TYPE_INPUT_SLIDER = 'slider'
ELEM_TYPE_INPUT_LISTBOX = 'listbox'
ELEM_TYPE_OUTPUT = 'output'
ELEM_TYPE_COLUMN = 'column'
ELEM_TYPE_MENUBAR = 'menubar'
ELEM_TYPE_PROGRESS_BAR = 'progressbar'
ELEM_TYPE_BLANK = 'blank'
ELEM_TYPE_TABLE = 'table'
ELEM_TYPE_TREE = 'tree'
ELEM_TYPE_ERROR = 'error'
ELEM_TYPE_SEPARATOR = 'separator'

# -------------------------  Popup Buttons Types  ------------------------- #
POPUP_BUTTONS_YES_NO = 1
POPUP_BUTTONS_CANCELLED = 2
POPUP_BUTTONS_ERROR = 3
POPUP_BUTTONS_OK_CANCEL = 4
POPUP_BUTTONS_OK = 0
POPUP_BUTTONS_NO_BUTTONS = 5


# ---------------------------------------------------------------------- #
# Cascading structure.... Objects get larger                             #
#   Button                                                               #
#       Element                                                          #
#           Row                                                          #
#               Form                                                     #
# ---------------------------------------------------------------------- #
# ---------------------------------------------------------------------- #
#                       Element CLASS                                    #
# ---------------------------------------------------------------------- #
class Element():
    def __init__(self, elem_type, size=(None, None), auto_size_text=None, font=None, background_color=None, text_color=None,
                 key=None, pad=None, tooltip=None, visible=True, size_px=(None, None)):


        # if elem_type != ELEM_TYPE_GRAPH:
        #     self.Size = convert_tkinter_size_to_Wx(size)
        # else:
        #     self.Size = size
        self.Size = size_px
        if size_px == (None, None) and size != (None, None):
            if elem_type in (ELEM_TYPE_MULTILINE_OUTPUT, ELEM_TYPE_INPUT_MULTILINE, ELEM_TYPE_OUTPUT, ELEM_TYPE_TABLE, ELEM_TYPE_TREE, ELEM_TYPE_TAB, ELEM_TYPE_COLUMN):
                self.Size = _convert_tkinter_size_to_Wx(size, DEFAULT_PIXELS_TO_CHARS_SCALING_MULTILINE_TEXT, DEFAULT_PIXEL_TO_CHARS_CUTOFF_MULTILINE)
            else:
                self.Size = _convert_tkinter_size_to_Wx(size, DEFAULT_PIXELS_TO_CHARS_SCALING, DEFAULT_PIXEL_TO_CHARS_CUTOFF)
        self.Type = elem_type
        self.AutoSizeText = auto_size_text
        # self.Pad = DEFAULT_ELEMENT_PADDING if pad is None else pad
        self.Pad = pad
        if font is not None and type(font) is not str:
            self.Font = font
        elif font is not None:
            self.Font = font.split(' ')
        else:
            self.Font = font

        self.TKStringVar = None
        self.TKIntVar = None
        self.TKText = None
        self.TKEntry = None
        self.TKImage = None

        self.ParentForm = None      # type: Window
        self.ParentContainer = None  # will be a Form, Column, or Frame element
        self.TextInputDefault = None
        self.Position = (0, 0)  # Default position Row 0, Col 0
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_ELEMENT_BACKGROUND_COLOR
        self.TextColor = text_color if text_color is not None else DEFAULT_ELEMENT_TEXT_COLOR
        self.Key = key  # dictionary key for return values
        self.Tooltip = tooltip
        self.TooltipObject = None
        self.Visible = visible
        self.metadata = None                # type: Any



    def FindReturnKeyBoundButton(self, form):
        for row in form.Rows:
            for element in row:
                if element.Type == ELEM_TYPE_BUTTON:
                    if element.BindReturnKey:
                        return element
                if element.Type == ELEM_TYPE_COLUMN:
                    rc = self.FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
                if element.Type == ELEM_TYPE_FRAME:
                    rc = self.FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
                if element.Type == ELEM_TYPE_TAB_GROUP:
                    rc = self.FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
                if element.Type == ELEM_TYPE_TAB:
                    rc = self.FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
        return None

    def _TextClickedHandler(self, event):
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = self.DisplayText
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def _ReturnKeyHandler(self, event):
        MyForm = self.ParentForm
        button_element = self.FindReturnKeyBoundButton(MyForm)
        if button_element is not None:
            button_element.ButtonCallBack(event)

    def _ListboxSelectHandler(self, event):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def _ComboboxSelectHandler(self, event):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def _RadioHandler(self):
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()

    def _CheckboxHandler(self):
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()

    def _TabGroupSelectHandler(self, event):
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()


    def _KeyboardHandler(self, event):
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()


    def _WxCallbackKeyboard(self, value):
        element_callback_quit_mainloop(self)


    def Update(self, widget, background_color=None, text_color=None, font=None, visible=None, disabled=None, tooltip=None):
        if font:
            widget.SetFont(font_to_wx_font(font))
        if text_color not in (None, COLOR_SYSTEM_DEFAULT):
            widget.SetForegroundColour(text_color)
        if background_color not in (None, COLOR_SYSTEM_DEFAULT):
            widget.SetBackgroundColour(background_color)
        if visible is True:
            widget.Show()
            self.ParentForm.VisibilityChanged()
        elif visible is False:
            widget.Hide()
            self.ParentForm.VisibilityChanged()
        if disabled:
            widget.Enable(False)
        elif disabled is False:
            widget.Enable(True)
        if tooltip is not None:
            widget.SetToolTip(tooltip)

    def __call__(self, *args, **kwargs):
        """
        Makes it possible to "call" an already existing element.  When you do make the "call", it actually calls
        the Update method for the element.
        Example:    If this text element was in yoiur layout:
                    sg.Text('foo', key='T')
                    Then you can call the Update method for that element by writing:
                    window.FindElement('T')('new text value')

        :param args:
        :param kwargs:
        :return:
        """
        return self.Update(*args, **kwargs)

    update = Update

# ---------------------------------------------------------------------- #
#                           Input Class                                  #
# ---------------------------------------------------------------------- #
class InputText(Element):
    def __init__(self, default_text='', size=(None,None), disabled=False, password_char='',
                 justification=None, background_color=None, text_color=None, font=None, tooltip=None,
                 change_submits=False, enable_events=False,
                 do_not_clear=True, key=None, focus=False, pad=None, visible=True, size_px=(None,None)):
        '''
        Input a line of text Element
        :param default_text: Default value to display
        :param size: Size of field in characters
        :param password_char: If non-blank, will display this character for every character typed
        :param background_color: Color for Element. Text or RGB Hex
        '''
        self.DefaultText = str(default_text)
        self.PasswordCharacter = str(password_char)
        bg = background_color if background_color is not None else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Focus = focus
        self.do_not_clear = do_not_clear
        self.Justification = justification or 'left'
        self.Disabled = disabled
        self.ChangeSubmits = change_submits or enable_events
        self.QT_QLineEdit = None
        self.ValueWasChanged = False
        self.WxTextCtrl = None


        super().__init__(ELEM_TYPE_INPUT_TEXT,size=size, background_color=bg, text_color=fg, key=key, pad=pad,
                         font=font, tooltip=tooltip, visible=visible, size_px=size_px)


    def Update(self, value=None, disabled=None, select=None, background_color=None, text_color=None, font=None, visible=None):
        if disabled is True:
            self.WxTextCtrl.Enable(True)
        elif disabled is False:
            self.WxTextCtrl.Enable(False)
        if value is not None:
            self.WxTextCtrl.SetValue(str(value))
            self.DefaultText = value
        if select:
            self.WxTextCtrl.SelectAll()
        # if visible:
        #     self.WxTextCtrl.Show()
        #     self.ParentForm.VisibilityChanged()
        # elif visible is False:
        #     self.WxTextCtrl.Hide()
        super().Update(self.WxTextCtrl, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def Get(self):
        return self.WxTextCtrl.GetValue()

    def SetFocus(self):
        self.WxTextCtrl.SetFocus()

    get = Get
    set_focus = SetFocus
    update = Update


# -------------------------  INPUT TEXT Element lazy functions  ------------------------- #
In = InputText
Input = InputText
I = InputText

# ---------------------------------------------------------------------- #
#                           Combo                                        #
# ---------------------------------------------------------------------- #
class Combo(Element):
    def __init__(self, values, default_value=None, size=(None, None), auto_size_text=None, background_color=None,
                 text_color=None, change_submits=False, enable_events=False, disabled=False, key=None, pad=None, tooltip=None,
                 readonly=False, visible_items=10, font=None, auto_complete=True, visible=True, size_px=(None,None)):
        '''
        Input Combo Box Element (also called Dropdown box)
        :param values:
        :param size: Size of field in characters
        :param auto_size_text: True if should shrink field to fit the default text
        :param background_color: Color for Element. Text or RGB Hex
        '''
        self.Values = values
        self.DefaultValue = default_value
        self.ChangeSubmits = change_submits or enable_events
        # self.InitializeAsDisabled = disabled
        self.Disabled = disabled
        self.Readonly = readonly
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.VisibleItems = visible_items
        self.AutoComplete = auto_complete
        self.WxComboBox = None     # type: wx.ComboBox

        super().__init__(ELEM_TYPE_INPUT_COMBO, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, size_px=size_px)




    def Update(self, value=None, values=None, set_to_index=None, disabled=None, readonly=None,  background_color=None, text_color=None, font=None, visible=None):
        if values is not None:
            self.WxComboBox.Set(values)
        if value:
            self.WxComboBox.SetSelection(self.WxComboBox.FindString(value))
        if set_to_index is not None:
            self.WxComboBox.SetSelection(set_to_index)
        if disabled is True:
            self.WxComboBox.Enable(False)
        elif disabled is False:
            self.WxComboBox.Enable(True)
        if readonly is not None:
            self.WxComboBox.SetWindowStyle(wx.CB_READONLY)

        super().Update(self.WxComboBox, background_color=background_color, text_color=text_color, font=font, visible=visible)

    update = Update


# -------------------------  INPUT COMBO Element lazy functions  ------------------------- #
InputCombo = Combo
DropDown = InputCombo
Drop = InputCombo



# ---------------------------------------------------------------------- #
#                           Option Menu                                  #
# ---------------------------------------------------------------------- #
class OptionMenu(Element):
    def __init__(self, values, default_value=None, size=(None, None), disabled=False, auto_size_text=None,
                 background_color=None, text_color=None, key=None, pad=None, tooltip=None):
        '''
        InputOptionMenu
        :param values:
        :param default_value:
        :param size:
        :param disabled:
        :param auto_size_text:
        :param background_color:
        :param text_color:
        :param key:
        :param pad:
        :param tooltip:
        '''
        self.Values = values
        self.DefaultValue = default_value
        self.TKOptionMenu = None
        self.Disabled = disabled
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_OPTION_MENU, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip)

    def Update(self, value=None, values=None, disabled=None):
        if values is not None:
            self.Values = values
        if self.Values is not None:
            for index, v in enumerate(self.Values):
                if v == value:
                    try:
                        self.TKStringVar.set(value)
                    except:
                        pass
                    self.DefaultValue = value
                    break
        if disabled == True:
            self.TKOptionMenu['state'] = 'disabled'
        elif disabled == False:
            self.TKOptionMenu['state'] = 'normal'

    update = Update


# -------------------------  OPTION MENU Element lazy functions  ------------------------- #
InputOptionMenu = OptionMenu


# ---------------------------------------------------------------------- #
#                           Listbox                                      #
# ---------------------------------------------------------------------- #
class Listbox(Element):
    def __init__(self, values, default_values=None, select_mode=None, change_submits=False, bind_return_key=False,
                 size=(None, None), disabled=False, auto_size_text=None, font=None, background_color=None, size_px=(None, None),
                 text_color=None, key=None, pad=None, tooltip=None):
        '''
        Listbox Element
        :param values:
        :param default_values:
        :param select_mode:
        :param change_submits:
        :param bind_return_key:
        :param size:
        :param disabled:
        :param auto_size_text:
        :param font:
        :param background_color:
        :param text_color:
        :param key:
        :param pad:
        :param tooltip:
        '''
        self.Values = values
        self.DefaultValues = default_values
        self.TKListbox = None
        self.ChangeSubmits = change_submits
        self.BindReturnKey = bind_return_key
        self.Disabled = disabled
        if select_mode == LISTBOX_SELECT_MODE_BROWSE:
            self.SelectMode = SELECT_MODE_BROWSE
        elif select_mode == LISTBOX_SELECT_MODE_EXTENDED:
            self.SelectMode = SELECT_MODE_EXTENDED
        elif select_mode == LISTBOX_SELECT_MODE_MULTIPLE:
            self.SelectMode = SELECT_MODE_MULTIPLE
        elif select_mode == LISTBOX_SELECT_MODE_SINGLE:
            self.SelectMode = SELECT_MODE_SINGLE
        else:
            self.SelectMode = DEFAULT_LISTBOX_SELECT_MODE
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_LISTBOX, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=bg, text_color=fg, key=key, pad=pad, size_px=size_px, tooltip=tooltip)

    def Update(self, values=None, disabled=None):
        if disabled == True:
            self.TKListbox.configure(state='disabled')
        elif disabled == False:
            self.TKListbox.configure(state='normal')
        if values is not None:
            self.TKListbox.delete(0, 'end')
            for item in values:
                self.TKListbox.insert(tk.END, item)
            self.TKListbox.selection_set(0, 0)
            self.Values = values

    def SetValue(self, values):
        for index, item in enumerate(self.Values):
            try:
                if item in values:
                    self.TKListbox.selection_set(index)
                else:
                    self.TKListbox.selection_clear(index)
            except:
                pass
        self.DefaultValues = values

    def GetListValues(self):
        return self.Values

    get_list_values = GetListValues
    set_value = SetValue
    update = Update

# ---------------------------------------------------------------------- #
#                           Radio                                        #
# ---------------------------------------------------------------------- #
class Radio(Element):
    def __init__(self, text, group_id, default=False, disabled=False, size=(None, None), auto_size_text=None,
                 background_color=None, text_color=None, font=None, key=None, pad=None, tooltip=None,
                 change_submits=False, enable_events=False, visible=True, size_px=(None, None)):
        """

        :param text:
        :param group_id:
        :param default:
        :param disabled:
        :param size:
        :param auto_size_text:
        :param background_color:
        :param text_color:
        :param font:
        :param key:
        :param pad:
        :param tooltip:
        :param change_submits:
        :param enable_events:
        :param visible:
        :param size_px:
        """
        self.InitialState = default
        self.Text = text
        self.GroupID = group_id
        self.Value = None
        self.Disabled = disabled
        self.TextColor = text_color or DEFAULT_TEXT_COLOR
        self.ChangeSubmits = change_submits or enable_events
        self.WxRadioButton = None       # type: wx.RadioButton

        super().__init__(ELEM_TYPE_INPUT_RADIO, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip, visible=visible, size_px=size_px)


    def Update(self, value=None, disabled=None, background_color=None, text_color=None, font=None, visible=None):
        if value:
            self.WxRadioButton.SetValue(True)
        elif value is False:
            self.WxRadioButton.SetValue(False)
        super().Update(self.WxRadioButton, background_color=background_color, text_color=text_color, font=font, visible=visible)


    update = Update

# ---------------------------------------------------------------------- #
#                           Checkbox                                     #
# ---------------------------------------------------------------------- #
class Checkbox(Element):
    def __init__(self, text, default=False, size=(None, None), auto_size_text=None, font=None, background_color=None,
                 text_color=None, change_submits=False, enable_events=False, disabled=False, key=None, pad=None, tooltip=None, visible=True, size_px=(None,None)):
        '''
        Checkbox Element
        :param text:
        :param default:
        :param size:
        :param auto_size_text:
        :param font:
        :param background_color:
        :param text_color:
        :param change_submits:
        :param disabled:
        :param key:
        :param pad:
        :param tooltip:
        '''
        self.Text = text
        self.InitialState = default
        self.WxCheckbox = None      # type:wx.CheckBox
        self.Disabled = disabled
        self.TextColor = text_color if text_color else DEFAULT_TEXT_COLOR
        self.ChangeSubmits = change_submits or enable_events


        super().__init__(ELEM_TYPE_INPUT_CHECKBOX, size=size,  auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip, visible=visible, size_px=size_px)

    def Get(self):
        return self.WxCheckbox.GetValue()

    def Update(self, value=None, disabled=None):
        if value is not None:
            try:
                self.WxCheckbox.SetValue(value)
                self.InitialState = value
            except:
                pass
        if disabled == True:
            self.WxCheckbox.Disable()
        elif disabled == False:
            self.WxCheckbox.Enable()

    get = Get
    update = Update


# -------------------------  CHECKBOX Element lazy functions  ------------------------- #
CB = Checkbox
CBox = Checkbox
Check = Checkbox


# ---------------------------------------------------------------------- #
#                           Spin                                         #
# ---------------------------------------------------------------------- #

class Spin(Element):
    # Values = None
    # TKSpinBox = None
    def __init__(self, values, initial_value=None, disabled=False, change_submits=False,  enable_events=False, size=(None, None), readonly=True, auto_size_text=None, font=None, background_color=None, text_color=None, key=None, pad=None, tooltip=None, visible=True, size_px=(None,None)):
        '''
        Spinner Element
        :param values:
        :param initial_value:
        :param disabled:
        :param change_submits:
        :param size:
        :param auto_size_text:
        :param font:
        :param background_color:
        :param text_color:
        :param key:
        :param pad:
        :param tooltip:
        '''
        self.Values = values
        self.DefaultValue = initial_value or values[0]
        self.ChangeSubmits = change_submits or enable_events
        self.Disabled = disabled
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.WxSpinCtrl : wx.SpinCtrl = None
        self.WxTextCtrl = None  # type : wx.TextCtrl
        self.CurrentValue = self.DefaultValue
        self.ReadOnly = readonly


        super().__init__(ELEM_TYPE_INPUT_SPIN, size=size, auto_size_text=auto_size_text, font=font, background_color=bg, text_color=fg,
                         key=key, pad=pad, tooltip=tooltip, visible=visible, size_px=size_px)
        return


    def _WxSpinCallback(self, event):
        event = event       # type:wx.SpinEvent
        print(f'spin event {event.GetInt()} {self.WxSpinCtrl.GetValue()}')
        offset = event.GetInt()
        self.WxTextCtrl.SetValue(self.Values[offset])
        self.CurrentValue = self.Values[offset]
        if self.ChangeSubmits:
            element_callback_quit_mainloop(self)

    def Update(self, value=None, values=None, disabled=None, background_color=None, text_color=None, font=None, visible=None):
        if values != None:
            self.Values = values
            self.QT_Spinner.setStrings(values)
            # self.QT_Spinner.setRange(self.Values[0], self.Values[1])
        if value is not None:
            # self.QT_Spinner.setValue(value)
            try:
                self.QT_Spinner.setValue(self.QT_Spinner.valueFromText(value))
                self.DefaultValue = value
            except:
                pass
        if disabled == True:
            self.QT_Spinner.setDisabled(True)
        elif disabled == False:
            self.QT_Spinner.setDisabled(False)
        super().Update(self.QT_Spinner, background_color=background_color, text_color=text_color, font=font, visible=visible)

    def Get(self):
        return self.WxSpinCtrl.GetValue()

    get = Get
    update = Update



# ---------------------------------------------------------------------- #
#                           Multiline                                    #
# ---------------------------------------------------------------------- #
class Multiline(Element):
    def __init__(self, default_text='', enter_submits=False, disabled=False, autoscroll=False, size=(None, None),
                 auto_size_text=None, background_color=None, text_color=None, change_submits=False, enable_events=False, do_not_clear=True,
                 key=None, focus=False, font=None, pad=None, tooltip=None, visible=True, size_px=(None,None)):
        '''
        Multiline Element
        :param default_text:
        :param enter_submits:
        :param disabled:
        :param autoscroll:
        :param size:
        :param auto_size_text:
        :param background_color:
        :param text_color:
        :param do_not_clear:
        :param key:
        :param focus:
        :param pad:
        :param tooltip:
        :param font:
        '''
        self.DefaultText = default_text
        self.EnterSubmits = enter_submits
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        self.Focus = focus
        self.do_not_clear = do_not_clear
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Autoscroll = autoscroll
        self.Disabled = disabled
        self.ChangeSubmits = change_submits or enable_events

        self.Widget = self.WxTextCtrl = None

        super().__init__(ELEM_TYPE_INPUT_MULTILINE, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, size_px=size_px)
        return


    def Update(self, value=None, disabled=None, append=False, background_color=None, text_color=None, font=None, visible=None):
            try:        # added in case the widget has already been deleted for some readon.
                if value is not None and not append:
                    self.WxTextCtrl.SetLabel(value)
                elif value is not None and append:
                    self.WxTextCtrl.AppendText(value)
                if background_color is not None:
                    self.WxTextCtrl.SetBackgroundColour(background_color)
                if text_color is not None:
                    self.WxTextCtrl.SetForegroundColour(text_color)
                if font is not None:
                    self.WxTextCtrl.SetFont(font)
                if disabled:
                    self.WxTextCtrl.Enable(True)
                elif disabled is False:
                    self.WxTextCtrl.Enable(False)
            except:
                pass

            super().Update(self.WxTextCtrl, background_color=background_color, text_color=text_color, font=font, visible=visible)

    #
    # def Update(self, value=None, disabled=None, append=False, background_color=None, text_color=None, font=None, visible=None):
    #     if value is not None and not append:
    #         self.DefaultText = value
    #         self.QT_TextEdit.setText(str(value))
    #     elif value is not None and append:
    #         self.DefaultText = value
    #         self.QT_TextEdit.setText(self.QT_TextEdit.toPlainText() + str(value))
    #     if disabled == True:
    #         self.QT_TextEdit.setDisabled(True)
    #     elif disabled == False:
    #         self.QT_TextEdit.setDisabled(False)
    #     super().Update(self.QT_TextEdit, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def Get(self):
        self.WxTextCtrl.GetValue()

    def SetFocus(self):
        self.WxTextCtrl.SetFocus()

    get = Get
    set_focus = SetFocus
    update = Update



# ---------------------------------------------------------------------- #
#                           Multiline Output                             #
# ---------------------------------------------------------------------- #
class MultilineOutput(Element):
    def __init__(self, default_text='', enter_submits=False, disabled=False, autoscroll=False, size=(None, None), auto_size_text=None, background_color=None, text_color=None, change_submits=False, enable_events=False, do_not_clear=True, key=None, focus=False, font=None, pad=None, tooltip=None, visible=True, size_px=(None,None)):
        '''
        Multiline Element
        :param default_text:
        :param enter_submits:
        :param disabled:
        :param autoscroll:
        :param size:
        :param auto_size_text:
        :param background_color:
        :param text_color:
        :param do_not_clear:
        :param key:
        :param focus:
        :param pad:
        :param tooltip:
        :param font:
        '''
        self.DefaultText = default_text
        self.EnterSubmits = enter_submits
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        self.Focus = focus
        self.do_not_clear = do_not_clear
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Autoscroll = autoscroll
        self.Disabled = disabled
        self.ChangeSubmits = change_submits or enable_events

        self.WxTextCtrl = None

        super().__init__(ELEM_TYPE_MULTILINE_OUTPUT, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, size_px=size_px)
        return


    def Update(self, value=None, disabled=None, append=False, background_color=None, text_color=None, font=None, visible=None):
            if value is not None and not append:
                self.WxTextCtrl.SetLabel(value)
            elif value is not None and append:
                self.WxTextCtrl.AppendText(value)
            if background_color is not None:
                self.WxTextCtrl.SetBackgroundColour(background_color)
            if text_color is not None:
                self.WxTextCtrl.SetForegroundColour(text_color)
            if font is not None:
                self.WxTextCtrl.SetFont(font)
            if disabled:
                self.WxTextCtrl.Enable(True)
            elif disabled is False:
                self.WxTextCtrl.Enable(False)
            super().Update(self.WxTextCtrl, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def Get(self):
        self.WxTextCtrl.GetValue()

    def SetFocus(self):
        self.WxTextCtrl.SetFocus()

    get = Get
    set_focus = SetFocus
    update = Update

# ---------------------------------------------------------------------- #
#                                       Text                             #
# ---------------------------------------------------------------------- #
class Text(Element):
    def __init__(self, text='', size=(None, None),  auto_size_text=None, click_submits=None, enable_events=False, relief=None, border_width=None, font=None, text_color=None, background_color=None, justification=None, pad=None, margins=None, key=None, tooltip=None, visible=True, size_px=(None,None)):
        """
        Text
        :param text:
        :param size:
        :param auto_size_text:
        :param click_submits:
        :param enable_events:
        :param relief:
        :param font:
        :param text_color:
        :param background_color:
        :param justification:
        :param pad:
        :param margins:
        :param key:
        :param tooltip:
        :param visible:
        :param size_px:
        """
        self.DisplayText = str(text)
        self.TextColor = text_color if text_color else DEFAULT_TEXT_COLOR
        self.Justification = justification
        self.Relief = relief
        self.ClickSubmits = click_submits or enable_events
        self.Margins = margins
        self.size_px = size_px
        if background_color is None:
            bg = DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR
        else:
            bg = background_color
        pixelsize = size
        if size[1] is not None and size[1] < 10:
            pixelsize = size[0]*10, size[1]*20
        self.WxStaticText = None   # type: wx.StaticText  # wx.StaticText(form.MasterPanel, -1, element.DisplayText)
        self.BorderWidth = border_width if border_width is not None else DEFAULT_BORDER_WIDTH

        super().__init__(ELEM_TYPE_TEXT, pixelsize, auto_size_text, background_color=bg, font=font if font else DEFAULT_FONT,
                         text_color=self.TextColor, pad=pad, key=key, tooltip=tooltip, size_px=size_px, visible=visible)
        return

    def Update(self, value=None, background_color=None, text_color=None, font=None, visible=None):
        if self.ParentForm.TKrootDestroyed:
            return
        if value is not None:
            self.WxStaticText.SetLabel(str(value))
            self.DisplayText = str(value)
        if background_color is not None:
            self.WxStaticText.SetBackgroundColour(background_color)
        if text_color is not None:
            self.WxStaticText.SetForegroundColour(text_color)
        if font is not None:
            self.WxStaticText.SetFont(font)
        super().Update(self.WxStaticText, background_color=background_color, text_color=text_color, font=font, visible=visible)


    update = Update


# -------------------------  Text Element lazy functions  ------------------------- #
Txt = Text
T = Text


class RedirectText(object):
    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self, string):
        self.out.AppendText(string)

    def flush(self):
        return

# ---------------------------------------------------------------------- #
#                           Output                                       #
#  Routes stdout, stderr to a scrolled window                            #
# ---------------------------------------------------------------------- #
class Output(Element):
    def __init__(self, size=(None, None), background_color=None, text_color=None, pad=None, font=None, tooltip=None,
                 key=None, visible=True, size_px=(None,None), disabled=False):
        '''
        Output Element
        :param size:
        :param background_color:
        :param text_color:
        :param pad:
        :param font:
        :param tooltip:
        :param key:
        '''
        self._TKOut = None
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.WxTextCtrl = None # type: wx.TextCtrl
        self.redir = None
        self.output = None
        self.Disabled = disabled

        super().__init__(ELEM_TYPE_OUTPUT, size=size, background_color=bg, text_color=fg, pad=pad, font=font,
                         tooltip=tooltip, key=key, visible=visible, size_px=size_px)

    def _reroute_stdout(self):
        self.my_stdout = sys.stdout
        self.my_stderr = sys.stderr
        self.redir = RedirectText(self.WxTextCtrl)
        sys.stdout = self.redir
        sys.stderr = self.redir
        Window.stdout_is_rerouted = True
        Window.stdout_location = self.redir

    def _reroute_again(self):
        sys.stdout = self.redir

    def Update(self,value=None, background_color=None, text_color=None, font=None, visible=None):
        if value is not None:
            self.WxTextCtrl.AppendText(value)
        super().Update(self.WxTextCtrl, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def __del__(self):
        try:
            sys.stdout = self.my_stdout
            sys.stderr = self.my_stderr
        except: pass
        # super().__del__()



    update = Update

# ---------------------------------------------------------------------- #
#                           Button Class                                 #
# ---------------------------------------------------------------------- #
class Button(Element):
    def __init__(self, button_text='', button_type=BUTTON_TYPE_READ_FORM, target=(None, None), tooltip=None,
                 file_types=(("ALL Files", "*"),), initial_folder=None, disabled=False, change_submits=False, enable_events=False,
                 image_filename=None, image_data=None, image_size=(None, None), image_subsample=None, border_width=None,
                 size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False,
                 focus=False, pad=None, key=None, visible=True, size_px=(None,None)):
        '''
        Button Element
        :param button_text:
        :param button_type:
        :param target:
        :param tooltip:
        :param file_types:
        :param initial_folder:
        :param disabled:
        :param image_filename:
        :param image_size:
        :param image_subsample:
        :param border_width:
        :param size:
        :param auto_size_button:
        :param button_color:
        :param default_value:
        :param font:
        :param bind_return_key:
        :param focus:
        :param pad:
        :param key:
        '''
        self.AutoSizeButton = auto_size_button
        self.BType = button_type
        self.FileTypes = file_types
        self.TKButton = None
        self.Target = target
        self.ButtonText = str(button_text)
        self.ButtonColor = button_color if button_color else DEFAULT_BUTTON_COLOR
        self.TextColor = self.ButtonColor[0]
        self.BackgroundColor = self.ButtonColor[1]
        self.ImageFilename = image_filename
        self.ImageData = image_data
        self.ImageSize = image_size
        self.ImageSubsample = image_subsample
        self.UserData = None
        self.BorderWidth = border_width if border_width is not None else DEFAULT_BORDER_WIDTH
        self.BindReturnKey = bind_return_key
        self.Focus = focus
        self.TKCal = None
        self.CalendarCloseWhenChosen = None
        self.DefaultDate_M_D_Y = (None, None, None)
        self.InitialFolder = initial_folder
        self.Disabled = disabled
        self.ChangeSubmits = change_submits or enable_events
        self.QT_QPushButton = None
        self.ColorChosen = None
        self.Relief = None
        self.WxButton = None        # type: wx.Button
        # self.temp_size = size if size != (NONE, NONE) else

        super().__init__(ELEM_TYPE_BUTTON, size=size, font=font, pad=pad, key=key, tooltip=tooltip, text_color=self.TextColor, background_color=self.BackgroundColor, visible=visible, size_px=size_px)
        return

    # Realtime button release callback
    def ButtonReleaseCallBack(self, parm):
        self.LastButtonClickedWasRealtime = False
        self.ParentForm.LastButtonClicked = None

    # Realtime button callback
    def ButtonPressCallBack(self, parm):
        self.ParentForm.LastButtonClickedWasRealtime = True
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = self.ButtonText
        if self.ParentForm.CurrentlyRunningMainloop:
            pass  # kick out of loop if read was called

    # -------  Button Callback  ------- #
    def ButtonCallBack(self, event):

        # print('Button callback')

        # print(f'Parent = {self.ParentForm}   Position = {self.Position}')
        # Buttons modify targets or return from the form
        # If modifying target, get the element object at the target and modify its StrVar
        target = self.Target
        target_element = None
        if target[0] == ThisRow:
            target = [self.Position[0], target[1]]
            if target[1] < 0:
                target[1] = self.Position[1] + target[1]
        strvar = None
        should_submit_window = False
        if target == (None, None):
            strvar = self.TKStringVar
        else:
            if not isinstance(target, str):
                if target[0] < 0:
                    target = [self.Position[0] + target[0], target[1]]
                target_element = self.ParentContainer._GetElementAtLocation(target)
            else:
                target_element = self.ParentForm.FindElement(target)
            try:
                strvar = target_element.TKStringVar
            except:
                pass
            try:
                if target_element.ChangeSubmits:
                    should_submit_window = True
            except:
                pass
        filetypes = (("ALL Files", "*"),) if self.FileTypes is None else self.FileTypes
        if self.BType == BUTTON_TYPE_BROWSE_FOLDER:                     # Browse Folder
            wx_types = convert_tkinter_filetypes_to_wx(self.FileTypes)
            if self.InitialFolder:
                dialog = wx.DirDialog(self.ParentForm.MasterFrame, style=wx.FD_OPEN)
            else:
                dialog = wx.DirDialog(self.ParentForm.MasterFrame)
            folder_name = ''
            if dialog.ShowModal() == wx.ID_OK:
                folder_name = dialog.GetPath()
            if folder_name != '':
                if target_element.Type == ELEM_TYPE_BUTTON:
                    target_element.FileOrFolderName = folder_name
                else:
                    target_element.Update(folder_name)
        elif self.BType == BUTTON_TYPE_BROWSE_FILE:                     # Browse File
            qt_types = convert_tkinter_filetypes_to_wx(self.FileTypes)
            if self.InitialFolder:
                dialog = wx.FileDialog(self.ParentForm.MasterFrame,defaultDir=self.InitialFolder, wildcard=qt_types, style=wx.FD_OPEN)
            else:
                dialog = wx.FileDialog(self.ParentForm.MasterFrame, wildcard=qt_types, style=wx.FD_OPEN)
            file_name = ''
            if dialog.ShowModal() == wx.ID_OK:
                file_name = dialog.GetPath()
            else:
                file_name = ''
            if file_name != '':
                if target_element.Type == ELEM_TYPE_BUTTON:
                    target_element.FileOrFolderName = file_name
                else:
                    target_element.Update(file_name)
        elif self.BType == BUTTON_TYPE_BROWSE_FILES:                    # Browse Files
            qt_types = convert_tkinter_filetypes_to_wx(self.FileTypes)
            if self.InitialFolder:
                dialog = wx.FileDialog(self.ParentForm.MasterFrame,defaultDir=self.InitialFolder, wildcard=qt_types, style=wx.FD_MULTIPLE)
            else:
                dialog = wx.FileDialog(self.ParentForm.MasterFrame, wildcard=qt_types, style=wx.FD_MULTIPLE)
            file_names = ''
            if dialog.ShowModal() == wx.ID_OK:
                file_names = dialog.GetPaths()
            else:
                file_names = ''
            if file_names != '':
                file_names = ';'.join(file_names)
                if target_element.Type == ELEM_TYPE_BUTTON:
                    target_element.FileOrFolderName = file_names
                else:
                    target_element.Update(file_names)
        elif self.BType == BUTTON_TYPE_SAVEAS_FILE:                     # Save As File
            qt_types = convert_tkinter_filetypes_to_wx(self.FileTypes)
            if self.InitialFolder:
                dialog = wx.FileDialog(self.ParentForm.MasterFrame,defaultDir=self.InitialFolder, wildcard=qt_types, style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
            else:
                dialog = wx.FileDialog(self.ParentForm.MasterFrame, wildcard=qt_types, style=wx.FD_SAVE|wx.FD_OVERWRITE_PROMPT)
            file_name = ''
            if dialog.ShowModal() == wx.ID_OK:
                file_name = dialog.GetPath()
            else:
                file_name = ''
            if file_name != '':
                if target_element.Type == ELEM_TYPE_BUTTON:
                    target_element.FileOrFolderName = file_name
                else:
                    target_element.Update(file_name)
        elif self.BType == BUTTON_TYPE_COLOR_CHOOSER:                   # Color Chooser
            qcolor = QColorDialog.getColor()
            rgb_color = qcolor.getRgb()
            color= '#' + ''.join('%02x'% i for i in rgb_color[:3])
            if self.Target == (None, None):
                self.FileOrFolderName = color
            else:
                target_element.Update(color)
        elif self.BType == BUTTON_TYPE_CLOSES_WIN:                      # Closes Window
            # first, get the results table built
            # modify the Results table in the parent FlexForm object
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = self.ButtonText
            self.ParentForm.FormRemainedOpen = False
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.App.ExitMainLoop()
            self.ParentForm.IgnoreClose = True
            self.ParentForm.MasterFrame.Close()
            if self.ParentForm.NonBlocking:
                Window.DecrementOpenCount()
            self.ParentForm._Close()
        elif self.BType == BUTTON_TYPE_READ_FORM:                       # Read Button
            # first, get the results table built
            # modify the Results table in the parent FlexForm object
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = self.ButtonText
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:  # if this window is running the mainloop, kick out
                self.ParentForm.App.ExitMainLoop()
        elif self.BType == BUTTON_TYPE_CLOSES_WIN_ONLY:  # special kind of button that does not exit main loop
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = self.ButtonText
            if self.ParentForm.CurrentlyRunningMainloop:  # if this window is running the mainloop, kick out
                self.ParentForm.App.ExitMainLoop()
            self.ParentForm.IgnoreClose = True
            self.ParentForm.MasterFrame.Close()
            self.ParentForm._Close()
            Window.DecrementOpenCount()
        elif self.BType == BUTTON_TYPE_CALENDAR_CHOOSER:  # this is a return type button so GET RESULTS and destroy window
            should_submit_window = False

        if should_submit_window:
            self.ParentForm.LastButtonClicked = target_element.Key
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.App.ExitMainLoop()
        return

    def Update(self, text=None, button_color=(None, None), disabled=None, image_data=None, image_filename=None, font=None, visible=None):
        if text is not None:
            self.WxButton.SetLabelText(text)
            self.ButtonText = text
        fg = bg = None
        if button_color != (None, None):
            self.ButtonColor = button_color
            fg, bg = button_color
        super().Update(self.WxButton, background_color=bg, text_color=fg, font=font, visible=visible, disabled=disabled)


    def GetText(self):
        return self.ButtonText

    def SetFocus(self):
        self.QT_QPushButton.setFocus()

    get_text = GetText
    set_focus = SetFocus
    update = Update



def convert_tkinter_filetypes_to_wx(filetypes):
    wx_filetypes = ''
    for item in filetypes:
        filetype = item[0] + ' (' + item[1] + ')|'+ item[1]
        wx_filetypes += filetype
    return wx_filetypes


# -------------------------  Button lazy functions  ------------------------- #
B = Button
Btn = Button


# ---------------------------------------------------------------------- #
#                           ProgreessBar                                 #
# ---------------------------------------------------------------------- #
class ProgressBar(Element):
    def __init__(self, max_value, orientation=None, size=(None, None),start_value=0,  auto_size_text=None, bar_color=(None, None),
                 style=None, border_width=None, relief=None, key=None, pad=None, disabled=False, visible=True, size_px=(None,None)):
        '''
        ProgressBar Element
        :param max_value:
        :param orientation:
        :param size:
        :param auto_size_text:
        :param bar_color:
        :param style:
        :param border_width:
        :param relief:
        :param key:
        :param pad:
        '''
        self.MaxValue = max_value
        self.TKProgressBar = None
        self.Cancelled = False
        self.NotRunning = True
        self.Orientation = orientation if orientation else DEFAULT_METER_ORIENTATION
        self.BarColor = bar_color if bar_color != (None, None) else DEFAULT_PROGRESS_BAR_COLOR
        self.BarStyle = style if style else DEFAULT_PROGRESS_BAR_STYLE
        self.BorderWidth = border_width if border_width is not None else DEFAULT_PROGRESS_BAR_BORDER_WIDTH
        self.Relief = relief if relief else DEFAULT_PROGRESS_BAR_RELIEF
        self.BarExpired = False
        self.StartValue = start_value
        self.Disabled = disabled
        tsize = size
        if size[0] is not None and size[0] < 100:
            # tsize = size[0] * DEFAULT_PIXELS_TO_CHARS_SCALING[0], size[1] * DEFAULT_PIXELS_TO_CHARS_SCALING[1]
            tsize = size[0]*10, size[1]
        self.WxGauge = None # type: wx.Gauge

        super().__init__(ELEM_TYPE_PROGRESS_BAR, size=tsize, auto_size_text=auto_size_text, key=key, pad=pad, visible=visible, size_px=size_px)

    # returns False if update failed
    def UpdateBar(self, current_count, max=None):
        try:    # Could havae been destroyed by user
            if max is not None:
                self.WxGauge.SetRange(max)
            self.WxGauge.SetValue(current_count)
        except: pass
        return True


    def Update(self, visible=None):
        super().Update(self.WxGauge, visible=visible)

    update = Update
    update_bar = UpdateBar


# ---------------------------------------------------------------------- #
#                           Image                                        #
# ---------------------------------------------------------------------- #
class Image(Element):
    def __init__(self, filename=None, data=None, background_color=None, size=(None, None), pad=None, key=None,
                 tooltip=None):
        '''
        Image Element
        :param filename:
        :param data:
        :param background_color:
        :param size:
        :param pad:
        :param key:
        :param tooltip:
        '''
        self.Filename = filename
        self.Data = data
        self.tktext_label = None
        self.BackgroundColor = background_color
        if data is None and filename is None:
            print('* Warning... no image specified in Image Element! *')
        super().__init__(ELEM_TYPE_IMAGE, size=size, background_color=background_color, pad=pad, key=key,
                         tooltip=tooltip, size_px=size)
        return

    def Update(self, filename=None, data=None, size=(None, None)):
        if filename is not None:
            image = tk.PhotoImage(file=filename)
        elif data is not None:
            # if type(data) is bytes:
            try:
                image = tk.PhotoImage(data=data)
            except:
                return  # an error likely means the window has closed so exit
            # else:
            # image = data
        else:
            return
        width, height = size[0] or image.width(), size[1] or image.height()
        self.tktext_label.configure(image=image, width=width, height=height)
        self.tktext_label.image = image


    update = Update


# ---------------------------------------------------------------------- #
#                           Canvas                                       #
# ---------------------------------------------------------------------- #
class Canvas(Element):
    def __init__(self, canvas=None, background_color=None, size=(None, None), pad=None, key=None, tooltip=None):
        '''
        Canvas Element
        :param canvas:
        :param background_color:
        :param size:
        :param pad:
        :param key:
        :param tooltip:
        '''
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self._TKCanvas = canvas

        super().__init__(ELEM_TYPE_CANVAS, background_color=background_color, size=size, pad=pad, key=key,
                         tooltip=tooltip)
        return

    @property
    def TKCanvas(self):
        if self._TKCanvas is None:
            print('*** Did you forget to call Finalize()? Your code should look something like: ***')
            print('*** form = sg.Window("My Form").Layout(layout).Finalize() ***')
        return self._TKCanvas




# ---------------------------------------------------------------------- #
#                           Graph                                        #
# ---------------------------------------------------------------------- #
class Graph(Element):
    def __init__(self, canvas_size, graph_bottom_left, graph_top_right, background_color=None, pad=None,
                 change_submits=False, drag_submits=False, key=None, tooltip=None):
        '''
        Graph Element
        :param canvas_size:
        :param graph_bottom_left:
        :param graph_top_right:
        :param background_color:
        :param pad:
        :param key:
        :param tooltip:
        '''
        self.CanvasSize = canvas_size
        self.BottomLeft = graph_bottom_left
        self.TopRight = graph_top_right
        self._TKCanvas = None
        self._TKCanvas2 = None
        self.ChangeSubmits = change_submits
        self.DragSubmits = drag_submits
        self.ClickPosition = (None, None)
        self.MouseButtonDown = False
        super().__init__(ELEM_TYPE_GRAPH, background_color=background_color, size_px=canvas_size, pad=pad, key=key,
                         tooltip=tooltip)
        return

    def _convert_xy_to_canvas_xy(self, x_in, y_in):
        if None in (x_in, y_in):
            return None, None
        scale_x = (self.CanvasSize[0] - 0) / (self.TopRight[0] - self.BottomLeft[0])
        scale_y = (0 - self.CanvasSize[1]) / (self.TopRight[1] - self.BottomLeft[1])
        new_x = 0 + scale_x * (x_in - self.BottomLeft[0])
        new_y = self.CanvasSize[1] + scale_y * (y_in - self.BottomLeft[1])
        return new_x, new_y

    def _convert_canvas_xy_to_xy(self, x_in, y_in):
        if None in (x_in, y_in):
            return None, None
        scale_x = (self.CanvasSize[0] - 0) / (self.TopRight[0] - self.BottomLeft[0])
        scale_y = (0 - self.CanvasSize[1]) / (self.TopRight[1] - self.BottomLeft[1])

        new_x = x_in / scale_x + self.BottomLeft[0]
        new_y = (y_in - self.CanvasSize[1]) / scale_y + self.BottomLeft[1]
        return int(new_x), int(new_y)

    def DrawLine(self, point_from, point_to, color='black', width=1):
        if point_from == (None, None):
            return
        converted_point_from = self._convert_xy_to_canvas_xy(point_from[0], point_from[1])
        converted_point_to = self._convert_xy_to_canvas_xy(point_to[0], point_to[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return self._TKCanvas2.create_line(converted_point_from, converted_point_to, width=width, fill=color)

    def DrawPoint(self, point, size=2, color='black'):
        if point == (None, None):
            return
        converted_point = self._convert_xy_to_canvas_xy(point[0], point[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return self._TKCanvas2.create_oval(converted_point[0] - size, converted_point[1] - size,
                                           converted_point[0] + size, converted_point[1] + size, fill=color,
                                           outline=color)

    def DrawCircle(self, center_location, radius, fill_color=None, line_color='black'):
        if center_location == (None, None):
            return
        converted_point = self._convert_xy_to_canvas_xy(center_location[0], center_location[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return self._TKCanvas2.create_oval(converted_point[0] - radius, converted_point[1] - radius,
                                           converted_point[0] + radius, converted_point[1] + radius, fill=fill_color,
                                           outline=line_color)

    def DrawOval(self, top_left, bottom_right, fill_color=None, line_color=None):
        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return self._TKCanvas2.create_oval(converted_top_left[0], converted_top_left[1], converted_bottom_right[0],
                                           converted_bottom_right[1], fill=fill_color, outline=line_color)

    def DrawArc(self, top_left, bottom_right, extent, start_angle, style=None, arc_color='black'):
        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        tkstyle = tk.PIESLICE if style is None else style
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return self._TKCanvas2.create_arc(converted_top_left[0], converted_top_left[1], converted_bottom_right[0],
                                          converted_bottom_right[1], extent=extent, start=start_angle, style=tkstyle,
                                          outline=arc_color)

    def DrawRectangle(self, top_left, bottom_right, fill_color=None, line_color=None):
        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return self._TKCanvas2.create_rectangle(converted_top_left[0], converted_top_left[1], converted_bottom_right[0],
                                                converted_bottom_right[1], fill=fill_color, outline=line_color)

    def DrawText(self, text, location, color='black', font=None, angle=0):
        if location == (None, None):
            return
        converted_point = self._convert_xy_to_canvas_xy(location[0], location[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        text_id = self._TKCanvas2.create_text(converted_point[0], converted_point[1], text=text, font=font, fill=color,
                                              angle=angle)
        return text_id

    def Erase(self):
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        self._TKCanvas2.delete('all')

    def Update(self, background_color):
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        self._TKCanvas2.configure(background=background_color)

    def Move(self, x_direction, y_direction):
        zero_converted = self._convert_xy_to_canvas_xy(0, 0)
        shift_converted = self._convert_xy_to_canvas_xy(x_direction, y_direction)
        shift_amount = (shift_converted[0] - zero_converted[0], shift_converted[1] - zero_converted[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        self._TKCanvas2.move('all', shift_amount[0], shift_amount[1])

    def MoveFigure(self, figure, x_direction, y_direction):
        zero_converted = self._convert_xy_to_canvas_xy(0, 0)
        shift_converted = self._convert_xy_to_canvas_xy(x_direction, y_direction)
        shift_amount = (shift_converted[0] - zero_converted[0], shift_converted[1] - zero_converted[1])
        if figure is None:
            print('*** WARNING - Your figure is None. It most likely means your did not Finalize your Window ***')
            print('Call Window.Finalize() prior to all graph operations')
            return None
        self._TKCanvas2.move(figure, shift_amount[0], shift_amount[1])

    @property
    def TKCanvas(self):
        if self._TKCanvas2 is None:
            print('*** Did you forget to call Finalize()? Your code should look something like: ***')
            print('*** form = sg.Window("My Form").Layout(layout).Finalize() ***')
        return self._TKCanvas2

    # Realtime button release callback
    def ButtonReleaseCallBack(self, event):
        self.ClickPosition = (None, None)
        self.LastButtonClickedWasRealtime = not self.DragSubmits
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = '__GRAPH__'  # need to put something rather than None
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()
        if self.DragSubmits:
            self.ParentForm.LastButtonClicked = None
        self.MouseButtonDown = False

    # Realtime button callback
    def ButtonPressCallBack(self, event):
        self.ClickPosition = self._convert_canvas_xy_to_xy(event.x, event.y)
        self.ParentForm.LastButtonClickedWasRealtime = self.DragSubmits
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = '__GRAPH__'  # need to put something rather than None
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick out of loop if read was called
        self.MouseButtonDown = True

    # Realtime button callback
    def MotionCallBack(self, event):
        if not self.MouseButtonDown:
            return
        self.ClickPosition = self._convert_canvas_xy_to_xy(event.x, event.y)
        self.ParentForm.LastButtonClickedWasRealtime = self.DragSubmits
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = '__GRAPH__'  # need to put something rather than None
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick out of loop if read was called

# ---------------------------------------------------------------------- #
#                           Frame                                        #
# ---------------------------------------------------------------------- #
class Frame(Element):
    def __init__(self, title, layout, title_color=None, background_color=None, title_location=None,
                 relief=DEFAULT_FRAME_RELIEF, size=(None, None), size_px=(None,None), font=None, pad=None, border_width=None, key=None,
                 tooltip=None):
        '''
        Frame Element
        :param title:
        :param layout:
        :param title_color:
        :param background_color:
        :param title_location:
        :param relief:
        :param size:
        :param font:
        :param pad:
        :param border_width:
        :param key:
        :param tooltip:
        '''
        self.UseDictionary = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.ParentWindow = None
        self.Rows = []
        # self.ParentForm = None
        self.TKFrame = None
        self.Title = title
        self.Relief = relief
        self.TitleLocation = title_location
        self.BorderWidth = border_width
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR

        self._Layout(layout)

        super().__init__(ELEM_TYPE_FRAME, background_color=background_color, text_color=title_color, size=size,
                         font=font, pad=pad, key=key, tooltip=tooltip, size_px=size_px)
        return

    def _AddRow(self, *args):
        ''' Parms are a variable number of Elements '''
        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            CurrentRow.append(element)
            if element.Key is not None:
                self.UseDictionary = True
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    def _Layout(self, rows):
        for row in rows:
            self._AddRow(*row)

    def _GetElementAtLocation(self, location):
        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element




# ---------------------------------------------------------------------- #
#                           Separator                                    #
#  Routes stdout, stderr to a scrolled window                            #
# ---------------------------------------------------------------------- #
class VerticalSeparator(Element):
    def __init__(self, size=(None, None), size_px=None, pad=None):
        '''
        VerticalSeperator - A separator that spans only 1 row in a vertical fashion
        :param pad:
        '''
        self.Orientation = 'vertical'  # for now only vertical works
        self.Disabled = None
        self.WxStaticLine = None        # type: wx.StaticLine
        super().__init__(ELEM_TYPE_SEPARATOR, pad=pad, size=size, size_px=size_px)



VSeperator = VerticalSeparator
VSep = VerticalSeparator



# ---------------------------------------------------------------------- #
#                           Separator                                    #
# ---------------------------------------------------------------------- #
class HorizontalSeparator(Element):
    def __init__(self, pad=None, size=(None, None), size_px=(None,None)):
        '''
        VerticalSeperator - A separator that spans only 1 row in a vertical fashion
        :param pad:
        '''
        self.Orientation = 'horizontal'  # for now only vertical works
        self.Disabled = None
        self.WxStaticLine = None        # type: wx.StaticLine

        super().__init__(ELEM_TYPE_SEPARATOR, pad=pad, size=size, size_px=size_px)



HSeperator = HorizontalSeparator
HSep = HorizontalSeparator




# ---------------------------------------------------------------------- #
#                           Tab                                          #
# ---------------------------------------------------------------------- #
class Tab(Element):
    def __init__(self, title, layout, title_color=None, background_color=None, font=None, pad=None, disabled=False,
                 border_width=None, key=None, tooltip=None):
        '''
        Tab Element
        :param title:
        :param layout:
        :param title_color:
        :param background_color:
        :param font:
        :param pad:
        :param disabled:
        :param border_width:
        :param key:
        :param tooltip:
        '''
        self.UseDictionary = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.ParentWindow = None
        self.Rows = []
        self.TKFrame = None
        self.Title = title
        self.BorderWidth = border_width
        self.Disabled = disabled
        self.ParentNotebook = None
        self.TabID = None
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR

        self._Layout(layout)

        super().__init__(ELEM_TYPE_TAB, background_color=background_color, text_color=title_color, font=font, pad=pad,
                         key=key, tooltip=tooltip)
        return

    def _AddRow(self, *args):
        ''' Parms are a variable number of Elements '''
        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            CurrentRow.append(element)
            if element.Key is not None:
                self.UseDictionary = True
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    def _Layout(self, rows):
        for row in rows:
            self._AddRow(*row)
        return self

    def Update(self, disabled=None):  # TODO Disable / enable of tabs is not complete
        if disabled is None:
            return
        self.Disabled = disabled
        state = 'disabled' if disabled is True else 'normal'
        self.ParentNotebook.tab(self.TabID, state=state)
        return self

    def _GetElementAtLocation(self, location):
        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element

    update = Update


# ---------------------------------------------------------------------- #
#                           TabGroup                                     #
# ---------------------------------------------------------------------- #
class TabGroup(Element):
    def __init__(self, layout, tab_location=None, title_color=None, selected_title_color=None, background_color=None,
                 font=None, change_submits=False, pad=None, border_width=None, theme=None, key=None, tooltip=None):
        '''
        TabGroup Element
        :param layout:
        :param tab_location:
        :param title_color:
        :param selected_title_color:
        :param background_color:
        :param font:
        :param change_submits:
        :param pad:
        :param border_width:
        :param theme:
        :param key:
        :param tooltip:
        '''
        self.UseDictionary = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.ParentWindow = None
        self.SelectedTitleColor = selected_title_color
        self.Rows = []
        self.TKNotebook = None
        self.TabCount = 0
        self.BorderWidth = border_width
        self.Theme = theme
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.ChangeSubmits = change_submits
        self.TabLocation = tab_location

        self._Layout(layout)

        super().__init__(ELEM_TYPE_TAB_GROUP, background_color=background_color, text_color=title_color, font=font,
                         pad=pad, key=key, tooltip=tooltip)
        return

    def _AddRow(self, *args):
        ''' Parms are a variable number of Elements '''
        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            CurrentRow.append(element)
            if element.Key is not None:
                self.UseDictionary = True
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    def _Layout(self, rows):
        for row in rows:
            self._AddRow(*row)

    def _GetElementAtLocation(self, location):
        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element

    def FindKeyFromTabName(self, tab_name):
        for row in self.Rows:
            for element in row:
                if element.Title == tab_name:
                    return element.Key
        return None

    find_key_from_tab_name = FindKeyFromTabName


# ---------------------------------------------------------------------- #
#                           Slider                                       #
# ---------------------------------------------------------------------- #
class Slider(Element):
    def __init__(self, range=(None, None), default_value=None, resolution=None, tick_interval=None, orientation=None,
                 border_width=None, relief=None, change_submits=False, disabled=False, size=(None, None), size_px=(None,None), font=None,
                 background_color=None, text_color=None, key=None, pad=None, tooltip=None):
        '''
        Slider Element
        :param range:
        :param default_value:
        :param resolution:
        :param orientation:
        :param border_width:
        :param relief:
        :param change_submits:
        :param disabled:
        :param size:
        :param font:
        :param background_color:
        :param text_color:
        :param key:
        :param pad:
        :param tooltip:
        '''
        self.TKScale = None
        self.Range = (1, 10) if range == (None, None) else range
        self.DefaultValue = self.Range[0] if default_value is None else default_value
        self.Orientation = orientation if orientation else DEFAULT_SLIDER_ORIENTATION
        self.BorderWidth = border_width if border_width else DEFAULT_SLIDER_BORDER_WIDTH
        self.Relief = relief if relief else DEFAULT_SLIDER_RELIEF
        self.Resolution = 1 if resolution is None else resolution
        self.ChangeSubmits = change_submits
        self.Disabled = disabled
        self.TickInterval = tick_interval
        temp_size = size
        if temp_size == (None, None):
            temp_size = (20, 20) if orientation.startswith('h') else (8, 20)

        super().__init__(ELEM_TYPE_INPUT_SLIDER, size=temp_size, font=font, background_color=background_color,
                         text_color=text_color, key=key, pad=pad, tooltip=tooltip, size_px=size_px)
        return

    def Update(self, value=None, range=(None, None), disabled=None):
        if value is not None:
            try:
                self.TKIntVar.set(value)
                if range != (None, None):
                    self.TKScale.config(from_=range[0], to_=range[1])
            except:
                pass
            self.DefaultValue = value
        if disabled == True:
            self.TKScale['state'] = 'disabled'
        elif disabled == False:
            self.TKScale['state'] = 'normal'


    update = Update



#
# ---------------------------------------------------------------------- #
#                           Column                                       #
# ---------------------------------------------------------------------- #
class Column(Element):
    def __init__(self, layout, background_color=None, size=(None, None), size_px=(None, None), pad=None, scrollable=False, vertical_scroll_only=False, right_click_menu=None, key=None, visible=True):
        '''
        Column Element
        :param layout:
        :param background_color:
        :param size:
        :param pad:
        :param scrollable:
        :param key:
        '''
        self.UseDictionary = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.ParentWindow = None
        self.Rows = []
        self.Scrollable = scrollable
        self.VerticalScrollOnly = vertical_scroll_only
        self.RightClickMenu = right_click_menu
        bg = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.WxBoxSizer = None      # type: wx.BoxSizer
        self.WxHSizer = None        # type: wx.BoxSizer
        self._Layout(layout)
        tsize = size_px if size_px != (None, None) else size

        super().__init__(ELEM_TYPE_COLUMN, background_color=background_color, size_px=tsize, pad=pad, key=key, visible=visible)
        return

    def _AddRow(self, *args):
        ''' Parms are a variable number of Elements '''
        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            CurrentRow.append(element)
            if element.Key is not None:
                self.UseDictionary = True
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    def _Layout(self, rows):
        for row in rows:
            self._AddRow(*row)

    def _GetElementAtLocation(self, location):
        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element


    def Update(self, visible=None):
        if visible:
            self.WxHSizer.Show(self.WxBoxSizer, recursive=True)
            self.ParentForm.VisibilityChanged()
        elif visible is False:
            self.WxHSizer.Hide(self.WxBoxSizer, recursive=True)
            self.ParentForm.VisibilityChanged()

    update = Update


# ---------------------------------------------------------------------- #
#                           Menu                                       #
# ---------------------------------------------------------------------- #
class Menu(Element):
    def __init__(self, menu_definition, background_color=None, size=(None, None), tearoff=False, pad=None, key=None):
        '''
        Menu Element
        :param menu_definition:
        :param background_color:
        :param size:
        :param tearoff:
        :param pad:
        :param key:
        '''
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.MenuDefinition = menu_definition
        self.TKMenu = None
        self.Tearoff = tearoff

        super().__init__(ELEM_TYPE_MENUBAR, background_color=background_color, size=size, pad=pad, key=key)
        return

    def _MenuItemChosenCallback(self, item_chosen):
        # print('IN MENU ITEM CALLBACK', item_chosen)
        self.ParentForm.LastButtonClicked = item_chosen
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop



# ---------------------------------------------------------------------- #
#                           Table                                        #
# ---------------------------------------------------------------------- #
class Table(Element):
    def __init__(self, values, headings=None, visible_column_map=None, col_widths=None, def_col_width=10,
                 auto_size_columns=True, max_col_width=20, select_mode=None, display_row_numbers=False, num_rows=None,
                 font=None, justification='right', text_color=None, background_color=None, alternating_row_color=None,
                 size=(None, None), change_submits=False, bind_return_key=False, pad=None, key=None, tooltip=None):
        '''
        Table Element
        :param values:
        :param headings:
        :param visible_column_map:
        :param col_widths:
        :param def_col_width:
        :param auto_size_columns:
        :param max_col_width:
        :param select_mode:
        :param display_row_numbers:
        :param font:
        :param justification:
        :param text_color:
        :param background_color:
        :param size:
        :param pad:
        :param key:
        :param tooltip:
        '''
        self.Values = values
        self.ColumnHeadings = headings
        self.ColumnsToDisplay = visible_column_map
        self.ColumnWidths = col_widths
        self.MaxColumnWidth = max_col_width
        self.DefaultColumnWidth = def_col_width
        self.AutoSizeColumns = auto_size_columns
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.TextColor = text_color
        self.Justification = justification
        self.InitialState = None
        self.SelectMode = select_mode
        self.DisplayRowNumbers = display_row_numbers
        self.NumRows = num_rows if num_rows is not None else size[1]
        self.TKTreeview = None
        self.AlternatingRowColor = alternating_row_color
        self.SelectedRows = []
        self.ChangeSubmits = change_submits
        self.BindReturnKey = bind_return_key
        self.StartingRowNumber = 0  # When displaying row numbers, where to start
        self.RowHeaderText = 'Row'
        super().__init__(ELEM_TYPE_TABLE, text_color=text_color, background_color=background_color, font=font,
                         size=size, pad=pad, key=key, tooltip=tooltip)
        return

    def Update(self, values=None):
        if values is not None:
            children = self.TKTreeview.get_children()
            for i in children:
                self.TKTreeview.detach(i)
                self.TKTreeview.delete(i)
            children = self.TKTreeview.get_children()
            # self.TKTreeview.delete(*self.TKTreeview.get_children())
            for i, value in enumerate(values):
                if self.DisplayRowNumbers:
                    value = [i + self.StartingRowNumber] + value
                id = self.TKTreeview.insert('', 'end', text=i, iid=i + 1, values=value, tag=i % 2)
            if self.AlternatingRowColor is not None:
                self.TKTreeview.tag_configure(1, background=self.AlternatingRowColor)
            self.Values = values
            self.SelectedRows = []

    update = Update


# ---------------------------------------------------------------------- #
#                           Tree                                         #
# ---------------------------------------------------------------------- #
class Tree(Element):
    def __init__(self, data=None, headings=None, visible_column_map=None, col_widths=None, col0_width=10,
                 def_col_width=10, auto_size_columns=True, max_col_width=20, select_mode=None, show_expanded=False,
                 change_submits=False, font=None, justification='right', text_color=None, background_color=None, num_rows=None, pad=None, key=None,
                 tooltip=None):
        '''
        Tree Element
        :param headings:
        :param visible_column_map:
        :param col_widths:
        :param def_col_width:
        :param auto_size_columns:
        :param max_col_width:
        :param select_mode:
        :param font:
        :param justification:
        :param text_color:
        :param background_color:
        :param num_rows:
        :param pad:
        :param key:
        :param tooltip:
        '''
        self.TreeData = data
        self.ColumnHeadings = headings
        self.ColumnsToDisplay = visible_column_map
        self.ColumnWidths = col_widths
        self.MaxColumnWidth = max_col_width
        self.DefaultColumnWidth = def_col_width
        self.AutoSizeColumns = auto_size_columns
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.TextColor = text_color
        self.Justification = justification
        self.InitialState = None
        self.SelectMode = select_mode
        self.ShowExpanded = show_expanded
        self.NumRows = num_rows
        self.Col0Width = col0_width
        self.TKTreeview = None
        self.SelectedRows = []
        self.ChangeSubmits = change_submits

        super().__init__(ELEM_TYPE_TREE, text_color=text_color, background_color=background_color, font=font, pad=pad,
                         key=key, tooltip=tooltip)
        return

    def add_treeview_data(self, node):
        # print(f'Inserting {node.key} under parent {node.parent}')
        if node.key != '':
            self.TKTreeview.insert(node.parent, 'end', node.key, text=node.text, values=node.values,
                                   open=self.ShowExpanded)
        for node in node.children:
            self.add_treeview_data(node)

    def Update(self, values=None, key=None, value=None, text=None):
        if values is not None:
            children = self.TKTreeview.get_children()
            for i in children:
                self.TKTreeview.detach(i)
                self.TKTreeview.delete(i)
            children = self.TKTreeview.get_children()
            self.TreeData = values
            self.add_treeview_data(self.TreeData.root_node)
            self.SelectedRows = []
        if key is not None:
            item = self.TKTreeview.item(key)
            if value is not None:
                self.TKTreeview.item(key, values=value)
            if text is not None:
                self.TKTreeview.item(key, text=text)
            item = self.TKTreeview.item(key)
        return self

    update = Update


class TreeData(object):
    class Node(object):
        def __init__(self, parent, key, text, values):
            self.parent = parent
            self.children = []
            self.key = key
            self.text = text
            self.values = values

        def _Add(self, node):
            self.children.append(node)

    def __init__(self):
        self.tree_dict = {}
        self.root_node = self.Node("", "", 'root', [])
        self.tree_dict[""] = self.root_node

    def _AddNode(self, key, node):
        self.tree_dict[key] = node

    def Insert(self, parent, key, text, values):
        node = self.Node(parent, key, text, values)
        self.tree_dict[key] = node
        parent_node = self.tree_dict[parent]
        parent_node._Add(node)

    def __repr__(self):
        return self._NodeStr(self.root_node, 1)

    def _NodeStr(self, node, level):
        return '\n'.join(
            [str(node.key) + ' : ' + str(node.text)] +
            [' ' * 4 * level + self._NodeStr(child, level + 1) for child in node.children])


# ---------------------------------------------------------------------- #
#                           Error Element                                #
# ---------------------------------------------------------------------- #
class ErrorElement(Element):
    def __init__(self, key=None):
        '''
        Error Element
        :param key:
        '''
        self.Key = key

        super().__init__(ELEM_TYPE_ERROR, key=key)
        return

    def Update(self, *args, **kwargs):
        PopupError('Keyword error in Update',
                   'You need to stop this madness and check your spelling',
                   'Bad key = {}'.format(self.Key),
                   'Your bad line of code may resemble this:',
                   'window.FindElement("{}")'.format(self.Key))
        return self

    def Get(self):
        return 'This is NOT a valid Element!\nSTOP trying to do things with it or I will have to crash at some point!'

    update = Update
    get = Get

Stretch = ErrorElement


# ------------------------------------------------------------------------- #
#                       Tray CLASS                                      #
# ------------------------------------------------------------------------- #
class SystemTray:
    def __init__(self, menu=None, filename=None, data=None, data_base64=None, tooltip=None):
        '''
        SystemTray - create an icon in the system tray
        :param menu: Menu definition
        :param filename: filename for icon
        :param data: in-ram image for icon
        :param data_base64: basee-64 data for icon
        :param tooltip: tooltip string
        '''
        self.Menu = menu
        self.TrayIcon = None
        self.Shown = False
        self.MenuItemChosen = TIMEOUT_KEY
        self.LastMessage = None
        self.LastTitle = None
        self.App = None
        self.Filename = filename
        self.timer = None
        self.DataBase64 = data_base64
        if Window.highest_level_app is None:
            self.App = Window.highest_level_app =  wx.App(False)
            # This could be a very dangerous thing to add!
            # It was needed in order for an application to run the Tray in a Thread
            self.App.SetAssertMode(wx.APP_ASSERT_SUPPRESS)
        else:
            self.App = Window.highest_level_app
        self.Tooltip = tooltip

        frame = wx.Frame(None, title='Tray icon frame')
        if filename:
            self.icon = wx.Icon(filename, wx.BITMAP_TYPE_ANY)
        elif data_base64:
            self.icon = PyEmbeddedImage(data_base64).GetIcon()
        else:
            self.icon = PyEmbeddedImage(DEFAULT_BASE64_ICON).GetIcon()
        self.TaskBarIcon = self.CustomTaskBarIcon(frame, self.App, self.Menu, self.icon, tooltip=tooltip)

        # self.App.MainLoop()


    class CustomTaskBarIcon(wx.adv.TaskBarIcon):
        def __init__(self, frame, app, menu, icon, tooltip=None):
            wx.adv.TaskBarIcon.__init__(self)
            self.frame = frame
            self.app = app
            self.menu_item_chosen = None
            self.menu = menu
            self.id_to_text = {}
            self.tooltip = tooltip or wx.EmptyString


            self.SetIcon(icon, tooltip=self.tooltip)
            self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
            self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDoubleClick)
            self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, self.OnTaskBarRightClick)
            self.Bind(wx.adv.EVT_TASKBAR_BALLOON_CLICK, self.OnTaskBarMessageClick)
            self.Bind(wx.EVT_MENU, self.OnMenu)

        def OnTaskBarActivate(self, evt):
            pass

        def OnTaskBarClose(self, evt):
            self.frame.Close()

        def OnTaskBarLeftClick(self, evt):
            # print('Got a LEFT click!')
            self.menu_item_chosen = EVENT_SYSTEM_TRAY_ICON_ACTIVATED
            self.app.ExitMainLoop()

        def OnTaskBarMessageClick(self, evt):
            # print('Got a LEFT click!')
            self.menu_item_chosen = EVENT_SYSTEM_TRAY_MESSAGE_CLICKED
            self.app.ExitMainLoop()

        def OnTaskBarLeftDoubleClick(self, evt):
            # print('Got a double click!')
            self.menu_item_chosen = EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED
            self.app.ExitMainLoop()

        def CreatePopupMenu(self):
            # print(f'Popup menu = {self.menu}')
            menu = wx.Menu()
            AddMenuItem(menu, self.menu[1], self)
            return menu

        def OnTaskBarRightClick(self, evt):
            # print('Got a right click!')
            self.menu_item_chosen = EVENT_SYSTEM_TRAY_ICON_RIGHT_CLICK
            # self.app.ExitMainLoop()

        def OnMenu(self, event):
            # print(f'On Menu {event}')
            menu = event.EventObject
            text=''
            item = menu.FindItemById(event.Id)
            # for item in menu.MenuItems:
            #     if item.Id == event.Id:
            #         print('** FOUND MENU ENTRY! **')
            # print(f'item = {item}')
            text = self.id_to_text[item]
            # text = self.id_to_text[item.Id]
            self.menu_item_chosen = text
            self.app.ExitMainLoop()



    def Read(self, timeout=None):
        '''
        Reads the context menu
        :param timeout: Optional.  Any value other than None indicates a non-blocking read
        :return:
        '''
        # if not self.Shown:
        #     self.Shown = True
        #     self.TrayIcon.show()
        timeout1 = timeout
        # if timeout1 == 0:
        #     timeout1 = 1
            # if wx.GetApp():
            #     wx.GetApp().ProcessPendingEvents()
            # self.App.ProcessPendingEvents()
            # self.App.ProcessIdle()
            # return self.MenuItemChosen
        if timeout1 is not None:
            try:
                self.timer = wx.Timer(self.TaskBarIcon)
                self.TaskBarIcon.Bind(wx.EVT_TIMER, self.timer_timeout)
                self.timer.Start(milliseconds=timeout1, oneShot=wx.TIMER_ONE_SHOT)
            except:
                print('*** Got error in Read ***')
        self.RunningMainLoop = True
        self.App.MainLoop()
        self.RunningMainLoop = False
        if self.timer:
            self.timer.Stop()
            self.TaskBarIcon.Unbind(wx.EVT_TIMER)
            del(self.timer)
            self.timer = None
        self.MenuItemChosen = self.TaskBarIcon.menu_item_chosen
        return self.MenuItemChosen

    def timer_timeout(self, event):
        self.TaskBarIcon.Unbind(wx.EVT_TIMER)
        del (self.timer)
        self.timer = None
        self.TaskBarIcon.menu_item_chosen = TIMEOUT_KEY
        self.App.ExitMainLoop()


    def Hide(self):
        self.TaskBarIcon.RemoveIcon()


    def UnHide(self):
        self.TaskBarIcon.SetIcon(icon=self.TaskBarIcon.icon, tooltip=self.TaskBarIcon.tooltip)


    def ShowMessage(self, title, message, filename=None, data=None, data_base64=None, messageicon=None, time=10000):
        '''
        Shows a balloon above icon in system tray
        :param title:  Title shown in balloon
        :param message: Message to be displayed
        :param filename: Optional icon filename
        :param data: Optional in-ram icon
        :param data_base64: Optional base64 icon
        :param time: How long to display message in milliseconds
        :return:
        '''
        if messageicon is None:
            self.TaskBarIcon.ShowBalloon(title, message, msec=time)
        else:
            self.TaskBarIcon.ShowBalloon(title, message, msec=time, flags=messageicon)

        return self

    def Close(self):
        '''

        :return:
        '''
        self.Hide()
        # Don't close app because windows could be depending on it
        # self.App.quit()

    def _DisableAsserts(self):
        wx.DisableAsserts()


    def Update(self, menu=None, tooltip=None,filename=None, data=None, data_base64=None,):
        '''
        Updates the menu, tooltip or icon
        :param menu: menu defintion
        :param tooltip: string representing tooltip
        :param filename:  icon filename
        :param data:  icon raw image
        :param data_base64: icon base 64 image
        :return:
        '''
        # Menu
        if menu is not None:
            self.TaskBarIcon.menu = menu
        if filename:
            self.icon = wx.Icon(filename, wx.BITMAP_TYPE_ANY)
        elif data_base64:
            self.icon = PyEmbeddedImage(data_base64).GetIcon()
        elif not self.icon:
            self.icon = PyEmbeddedImage(DEFAULT_BASE64_ICON).GetIcon()
        if self.icon:
            self.Tooltip = tooltip or self.Tooltip or self.TaskBarIcon.tooltip or wx.EmptyString
            self.TaskBarIcon.SetIcon(self.icon, tooltip=self.Tooltip)
        # Tooltip
        # if tooltip is not None:
        #     self.TrayIcon.setToolTip(str(tooltip))
        # Icon
        # qicon = None
        # if filename is not None:
        #     icon = wx.Icon(filename, wx.BITMAP_TYPE_ICO)
        #     self.TaskBarIcon.SetIcon(icon, tooltip=tooltip)
        # elif data is not None:
        #     ba = QtCore.QByteArray.fromRawData(data)
        #     pixmap = QtGui.QPixmap()
        #     pixmap.loadFromData(ba)
        #     qicon = QIcon(pixmap)
        # elif data_base64 is not None:
        #     ico1 = base64.b64decode(data_base64)
        #     fout = open("zzztemp_icon.ico", "wb")
        #     fout.write(ico1)
        #     fout.close()
        #     icon = wx.Icon('zzztemp_icon.ico', wx.BITMAP_TYPE_ICO)
        #     self.TrayIcon.SetIcon(icon, tooltip=tooltip)
        #     os.remove("zzztemp_icon.ico")
        # if qicon is not None:
        #     self.TrayIcon.setIcon(qicon)

    close = Close
    hide = Hide
    read = Read
    show_message = ShowMessage
    un_hide = UnHide
    update = Update


class DragFrame(wx.Frame):
    def __init__(self, title=''):
        wx.Frame.__init__(self, None, title=title)

    def on_mouse(self, event):
        '''
        implement dragging
        '''
        # print('on_mouse')
        if not event.Dragging():
            self._dragPos = None
            return
        # self.CaptureMouse()
        if not self._dragPos:
            self._dragPos = event.GetPosition()
        else:
            pos = event.GetPosition()
            displacement = self._dragPos - pos
            self.SetPosition( self.GetPosition() - displacement )


# ------------------------------------------------------------------------- #
#                       Window CLASS                                      #
# ------------------------------------------------------------------------- #
class Window:

    NumOpenWindows = 0
    user_defined_icon = None
    hidden_master_root = None
    QTApplication = None
    active_popups = {}
    highest_level_app = None
    stdout_is_rerouted = False
    stdout_location = None

    def __init__(self, title, layout=None, default_element_size=DEFAULT_ELEMENT_SIZE, default_button_element_size=(None, None),
                 auto_size_text=None, auto_size_buttons=None, location=(None, None), size=(None, None), element_padding=None, button_color=None, font=None,
                 progress_bar_color=(None, None), background_color=None, border_depth=None, auto_close=False,
                 auto_close_duration=None, icon=DEFAULT_BASE64_ICON, force_toplevel=False,
                 alpha_channel=1, return_keyboard_events=False, use_default_focus=True, text_justification=None,
                 no_titlebar=False, grab_anywhere=False, keep_on_top=False, resizable=True, disable_close=False, disable_minimize=False, background_image=None, finalize=False):
        '''

        :param title:
        :param default_element_size:
        :param default_button_element_size:
        :param auto_size_text:
        :param auto_size_buttons:
        :param location:
        :param size:
        :param element_padding:
        :param button_color:
        :param font:
        :param progress_bar_color:
        :param background_color:
        :param border_depth:
        :param auto_close:
        :param auto_close_duration:
        :param icon:
        :param force_toplevel:
        :param alpha_channel:
        :param return_keyboard_events:
        :param use_default_focus:
        :param text_justification:
        :param no_titlebar:
        :param grab_anywhere:
        :param keep_on_top:
        :param resizable:
        :param disable_close:
        :param background_image:
        '''
        self.AutoSizeText = auto_size_text if auto_size_text is not None else DEFAULT_AUTOSIZE_TEXT
        self.AutoSizeButtons = auto_size_buttons if auto_size_buttons is not None else DEFAULT_AUTOSIZE_BUTTONS
        self.Title = title
        self.Rows = []  # a list of ELEMENTS for this row
        self.DefaultElementSize = _convert_tkinter_size_to_Wx(default_element_size)
        self.DefaultButtonElementSize = _convert_tkinter_size_to_Wx(default_button_element_size) if default_button_element_size != (
            None, None) else _convert_tkinter_size_to_Wx(DEFAULT_BUTTON_ELEMENT_SIZE)
        self.Location = location
        self.ButtonColor = button_color if button_color else DEFAULT_BUTTON_COLOR
        self.BackgroundColor = background_color if background_color else DEFAULT_BACKGROUND_COLOR
        self.ParentWindow = None
        self.Font = font if font else DEFAULT_FONT
        self.RadioDict = {}
        self.BorderDepth = border_depth
        self.WindowIcon = Window.user_defined_icon if Window.user_defined_icon is not None else icon if icon is not None else DEFAULT_WINDOW_ICON
        self.AutoClose = auto_close
        self.NonBlocking = False
        self.TKroot = None
        self.TKrootDestroyed = False
        self.CurrentlyRunningMainloop = False
        self.FormRemainedOpen = False
        self.TKAfterID = None
        self.ProgressBarColor = progress_bar_color
        self.AutoCloseDuration = auto_close_duration
        self.RootNeedsDestroying = False
        self.Shown = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.LastButtonClicked = None
        self.LastButtonClickedWasRealtime = False
        self.UseDictionary = False
        self.UseDefaultFocus = use_default_focus
        self.ReturnKeyboardEvents = return_keyboard_events
        self.LastKeyboardEvent = None
        self.TextJustification = text_justification
        self.NoTitleBar = no_titlebar
        self.GrabAnywhere = grab_anywhere
        self.KeepOnTop = keep_on_top
        self.ForcefTopLevel = force_toplevel
        self.Resizable = resizable
        self._AlphaChannel = alpha_channel
        self.Timeout = None
        self.TimeoutKey = TIMEOUT_KEY
        self.TimerCancelled = False
        self.DisableClose = disable_close
        self._Hidden = False
        # self.QTApplication = None
        # self.QT_QMainWindow = None
        self._Size=size
        self.ElementPadding = element_padding or DEFAULT_ELEMENT_PADDING
        self.FocusElement = None
        self.BackgroundImage = background_image
        self.XFound = False
        self.DisableMinimize = disable_minimize
        self.App = None             # type: wx.App
        self.MasterFrame =  None    # type: wx.Frame
        self.MasterPanel = None     # type: wx.Panel
        self.IgnoreClose = False
        self.UniqueKeyCounter = 0
        self.AllKeysDict = {}       # dictionary containing all the keys and elements in this window

        if layout is not None:
            self.Layout(layout)
            if finalize:
                self.Finalize()

    @classmethod
    def IncrementOpenCount(self):
        self.NumOpenWindows += 1
        # print('+++++ INCREMENTING Num Open Windows = {} ---'.format(Window.NumOpenWindows))

    @classmethod
    def DecrementOpenCount(self):
        self.NumOpenWindows -= 1 * (self.NumOpenWindows != 0)  # decrement if not 0
        # print('----- DECREMENTING Num Open Windows = {} ---'.format(Window.NumOpenWindows))


    # ------------------------- Add ONE Row to Form ------------------------- #
    def AddRow(self, *args):
        ''' Parms are a variable number of Elements '''
        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            CurrentRow.append(element)
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    # ------------------------- Add Multiple Rows to Form ------------------------- #
    def AddRows(self, rows):
        for row in rows:
            self.AddRow(*row)

    def Layout(self, rows):
        self.AddRows(rows)
        self.BuildKeyDict()
        return self

    def LayoutAndRead(self, rows, non_blocking=False):
        raise DeprecationWarning('LayoutAndRead is no longer supported... change your call to window.Layout(layout).Read()')
        # self.AddRows(rows)
        # self.Show(non_blocking=non_blocking)
        # return self.ReturnValues

    def LayoutAndShow(self, rows):
        raise DeprecationWarning('LayoutAndShow is no longer supported... change your call to LayoutAndRead')

    # ------------------------- ShowForm   THIS IS IT! ------------------------- #
    def Show(self, non_blocking=False):
        self.Shown = True
        # Compute num rows & num cols (it'll come in handy debugging)
        self.NumRows = len(self.Rows)
        self.NumCols = max(len(row) for row in self.Rows)
        self.NonBlocking = non_blocking

        # Search through entire form to see if any elements set the focus
        # if not, then will set the focus to the first input element
        found_focus = False
        for row in self.Rows:
            for element in row:
                try:
                    if element.Focus:
                        found_focus = True
                except:
                    pass
                try:
                    if element.Key is not None:
                        self.UseDictionary = True
                except:
                    pass

        if not found_focus and self.UseDefaultFocus:
            self.UseDefaultFocus = True
        else:
            self.UseDefaultFocus = False
        # -=-=-=-=-=-=-=-=- RUN the GUI -=-=-=-=-=-=-=-=- ##
        StartupTK(self)
        # If a button or keyboard event happened but no results have been built, build the results
        if self.LastKeyboardEvent is not None or self.LastButtonClicked is not None:
            return BuildResults(self, False, self)

        return self.ReturnValues

    # ------------------------- SetIcon - set the window's fav icon ------------------------- #
    def SetIcon(self, icon=None, pngbase64=None):
            pass

    def _GetElementAtLocation(self, location):
        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element

    def _GetDefaultElementSize(self):
        return self.DefaultElementSize

    def _AutoCloseAlarmCallback(self):
        try:
            window = self
            if window:
                if window.NonBlocking:
                    self.CloseNonBlockingForm()
                else:
                    window._Close()
                    if self.CurrentlyRunningMainloop:
                        self.QTApplication.exit()  # kick the users out of the mainloop
                    self.RootNeedsDestroying = True
                    self.QT_QMainWindow.close()

        except:
            pass

    def timer_timeout(self, event):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        # print('timer timeout')
        if self.TimerCancelled:
            return
        self.LastButtonClicked = self.TimeoutKey
        self.FormRemainedOpen = True
        if self.CurrentlyRunningMainloop:
            self.App.ExitMainLoop()


    def non_block_timer_timeout(self, event):
        # print('non-blocking timer timeout')
        self.App.ExitMainLoop()


    def autoclose_timer_callback(self, frame):
        # print('*** AUTOCLOSE TIMEOUT CALLBACK ***', frame)
        try:
            frame.Close()
        except:
            pass        # if user has already closed the frame will get an error
        # TODO Sept - does this need adding back?
        # if self.CurrentlyRunningMainloop:
        #     self.App.ExitMainLoop()

    def callback_keyboard_char(self, event):
        event = event       # type:wx.KeyEvent
        self.LastButtonClicked = None
        self.FormRemainedOpen = True
        if event.ClassName == 'wxMouseEvent':
            if event.WheelRotation < 0:
                self.LastKeyboardEvent = 'MouseWheel:Down'
            else:
                self.LastKeyboardEvent = 'MouseWheel:Up'
        else:
            self.LastKeyboardEvent = event.GetKeyCode()
        if not self.NonBlocking:
            BuildResults(self, False, self)
        if self.CurrentlyRunningMainloop:  # quit if this is the current mainloop, otherwise don't quit!
            self.App.ExitMainLoop()  # kick the users out of the mainloop
        if event.ClassName != 'wxMouseEvent':
            event.DoAllowNextEvent()

    def Read(self, timeout=None, timeout_key=TIMEOUT_KEY):
        if timeout == 0:  # timeout of zero runs the old readnonblocking
            event, values = self._ReadNonBlocking()
            if event is None:
                event = timeout_key
            if values is None:
                event = None
            return event, values  # make event None if values was None and return
        # Read with a timeout
        self.Timeout = timeout
        self.TimeoutKey = timeout_key
        self.NonBlocking = False
        if not self.Shown:
            self.Show()
        else:
            # if already have a button waiting, the return previously built results
            if self.LastButtonClicked is not None and not self.LastButtonClickedWasRealtime:
                # print(f'*** Found previous clicked saved {self.LastButtonClicked}')
                results = BuildResults(self, False, self)
                self.LastButtonClicked = None
                return results
            InitializeResults(self)
            # if the last button clicked was realtime, emulate a read non-blocking
            # the idea is to quickly return realtime buttons without any blocks until released
            if self.LastButtonClickedWasRealtime:
                # print(f'RTime down {self.LastButtonClicked}' )
                try:
                    rc = self.TKroot.update()
                except:
                    self.TKrootDestroyed = True
                    Window.DecrementOpenCount()
                results = BuildResults(self, False, self)
                if results[0] != None and results[0] != timeout_key:
                    return results
                else:
                    pass

                # else:
                #     print("** REALTIME PROBLEM FOUND **", results)

            # normal read blocking code....
            if timeout != None:
                self.TimerCancelled = False
                timer = wx.Timer(self.App)
                self.App.Bind(wx.EVT_TIMER, self.timer_timeout)
                timer.Start(milliseconds=timeout, oneShot=wx.TIMER_ONE_SHOT)
            else:
                timer = None
            self.CurrentlyRunningMainloop = True
            # print(f'In main {self.Title}')
            ################################# CALL GUWxTextCtrlI MAINLOOP ############################
            self.App.MainLoop()
            self.CurrentlyRunningMainloop = False
            self.TimerCancelled = True
            if timer:
                timer.Stop()
            if Window.stdout_is_rerouted:
                sys.stdout = Window.stdout_location
            if self.RootNeedsDestroying:
                # self.LastButtonClicked = None
                # self.App.Close()
                try:
                    self.MasterFrame.Close()
                except: pass
                Window.DecrementOpenCount()
            # if form was closed with X
            if self.LastButtonClicked is None and self.LastKeyboardEvent is None and self.ReturnValues[0] is None:
                Window.DecrementOpenCount()
        # Determine return values
        if self.LastKeyboardEvent is not None or self.LastButtonClicked is not None:
            results = BuildResults(self, False, self)
            if not self.LastButtonClickedWasRealtime:
                self.LastButtonClicked = None
            return results
        else:
            if not self.XFound and self.Timeout != 0 and self.Timeout is not None and self.ReturnValues[0] is None:       # Special Qt case because returning for no reason so fake timeout
                self.ReturnValues = self.TimeoutKey, self.ReturnValues[1]   # fake a timeout
            elif not self.XFound and self.ReturnValues[0] is None:                   # TODO HIGHLY EXPERIMENTAL... added due to tray icon interaction
                # print("*** Faking timeout ***")
                self.ReturnValues = self.TimeoutKey, self.ReturnValues[1]   # fake a timeout
            return self.ReturnValues

    def _ReadNonBlocking(self):
        if self.TKrootDestroyed:
            return None, None
        if not self.Shown:
            self.Show(non_blocking=True)
        else:
            # event = wx.Event()
            # self.App.QueueEvent(event)
            timer = wx.Timer(self.App)
            self.App.Bind(wx.EVT_TIMER, self.timer_timeout)
            timer.Start(milliseconds=0, oneShot=wx.TIMER_ONE_SHOT)
            self.CurrentlyRunningMainloop = True
            # print(f'In main {self.Title}')
            ################################# CALL GUWxTextCtrlI MAINLOOP ############################

            self.App.MainLoop()
            if Window.stdout_is_rerouted:
                sys.stdout = Window.stdout_location
            # self.LastButtonClicked = 'TEST'
            self.CurrentlyRunningMainloop = False
            timer.Stop()
            # while self.App.HasPendingEvents():
            #     self.App.ProcessPendingEvents()
        return BuildResults(self, False, self)


    def Finalize(self):
        if self.TKrootDestroyed:
            return self
        if not self.Shown:
            self.Show(non_blocking=True)
        # else:
        #     try:
        #         self.QTApplication.processEvents()              # refresh the window
        #     except:
        #         print('* ERROR FINALIZING *')
        #         self.TKrootDestroyed = True
        #         Window.DecrementOpenCount()
        return self


    def Refresh(self):
        # self.QTApplication.processEvents()              # refresh the window
        return self

    def VisibilityChanged(self):
        self.SizeChanged()
        return self

    def Fill(self, values_dict):
        FillFormWithValues(self, values_dict)
        return self

    def FindElement(self, key, silent_on_error=False):
        try:
            element = self.AllKeysDict[key]
        except KeyError:
            element = None
        # element = _FindElementFromKeyInSubForm(self, key)
        if element is None:
            if not silent_on_error:
                print('*** WARNING = FindElement did not find the key. Please check your key\'s spelling ***')
                PopupError('Keyword error in FindElement Call',
                           'Bad key = {}'.format(key),
                           'Your bad line of code may resemble this:',
                           'window.FindElement("{}")'.format(key))
                return ErrorElement(key=key)
            else:
                return False
        return element

    Element = FindElement       # shortcut function definition


    def BuildKeyDict(self):
        dict = {}
        self.AllKeysDict = self._BuildKeyDictForWindow(self,self, dict)
        # print(f'keys built = {self.AllKeysDict}')

    def _BuildKeyDictForWindow(self, top_window, window, key_dict):
        for row_num, row in enumerate(window.Rows):
            for col_num, element in enumerate(row):
                if element.Type == ELEM_TYPE_COLUMN:
                    key_dict = self._BuildKeyDictForWindow(top_window, element, key_dict)
                if element.Type == ELEM_TYPE_FRAME:
                    key_dict = self._BuildKeyDictForWindow(top_window, element, key_dict)
                if element.Type == ELEM_TYPE_TAB_GROUP:
                    key_dict = self._BuildKeyDictForWindow(top_window, element, key_dict)
                if element.Type == ELEM_TYPE_TAB:
                    key_dict = self._BuildKeyDictForWindow(top_window, element, key_dict)
                if element.Key is None:   # if no key has been assigned.... create one for input elements
                    if element.Type == ELEM_TYPE_BUTTON:
                        element.Key = element.ButtonText
                    if element.Type in (ELEM_TYPE_MENUBAR, ELEM_TYPE_BUTTONMENU, ELEM_TYPE_CANVAS,
                                        ELEM_TYPE_INPUT_SLIDER, ELEM_TYPE_GRAPH, ELEM_TYPE_IMAGE,
                                        ELEM_TYPE_INPUT_CHECKBOX, ELEM_TYPE_INPUT_LISTBOX, ELEM_TYPE_INPUT_COMBO,
                                        ELEM_TYPE_INPUT_MULTILINE, ELEM_TYPE_INPUT_OPTION_MENU, ELEM_TYPE_INPUT_SPIN,
                                        ELEM_TYPE_INPUT_TEXT):
                        element.Key = top_window.DictionaryKeyCounter
                        top_window.DictionaryKeyCounter += 1
                if element.Key is not None:
                    if element.Key in key_dict.keys():
                        print('*** Duplicate key found in your layout {} ***'.format(element.Key)) if element.Type != ELEM_TYPE_BUTTON else None
                        element.Key = element.Key + str(self.UniqueKeyCounter)
                        self.UniqueKeyCounter += 1
                        print('*** Replaced new key with {} ***'.format(element.Key)) if element.Type != ELEM_TYPE_BUTTON else None
                    key_dict[element.Key] = element
        return key_dict

    def FindElementWithFocus(self):
        return self.FocusElement
        # element = _FindElementWithFocusInSubForm(self)
        # return element

    def SaveToDisk(self, filename):
        try:
            results = BuildResults(self, False, self)
            with open(filename, 'wb') as sf:
                pickle.dump(results[1], sf)
        except:
            print('*** Error saving form to disk ***')

    def LoadFromDisk(self, filename):
        try:
            with open(filename, 'rb') as df:
                self.Fill(pickle.load(df))
        except:
            print('*** Error loading form to disk ***')

    def GetScreenDimensions(self):
        size = wx.GetDisplaySize()
        return size

    def Move(self, x, y):
        self.MasterFrame.SetPosition((x,y))

    def Minimize(self):
        self.MasterFrame.Iconize()


    def Maximize(self):
        self.MasterFrame.Maximize()


    def _Close(self):
        try:
            self.TKroot.update()
        except:
            pass
        if not self.NonBlocking:
            BuildResults(self, False, self)
        if self.TKrootDestroyed:
            return None
        self.TKrootDestroyed = True
        self.RootNeedsDestroying = True
        # self.__del__()
        return None

    def Close(self):
        if self.TKrootDestroyed:
            return
        try:
            self.MasterFrame.Close()
        except:
            print('error closing window')

    CloseNonBlockingForm = Close
    CloseNonBlocking = Close

    def Disable(self):
        self.MasterFrame.Enable(False)

    def Enable(self):
        self.MasterFrame.Enable(True)

    def Hide(self):
        self._Hidden = True
        self.MasterFrame.Hide()
        return

    def UnHide(self):
        if self._Hidden:
            self.MasterFrame.Show()
            self._Hidden = False

    def Disappear(self):
        self.MasterFrame.SetTransparent(0)

    def Reappear(self):
        self.MasterFrame.SetTransparent(255)

    def SetAlpha(self, alpha):
        '''
        Change the window's transparency
        :param alpha: From 0 to 1 with 0 being completely transparent
        :return:
        '''
        self._AlphaChannel = alpha * 255
        if self._AlphaChannel is not None:
            self.MasterFrame.SetTransparent(self._AlphaChannel)

    @property
    def AlphaChannel(self):
        return self._AlphaChannel

    @AlphaChannel.setter
    def AlphaChannel(self, alpha):
        self.SetAlpha(alpha)

    def BringToFront(self):
        self.MasterFrame.ToggleWindowStyle(wx.STAY_ON_TOP)


    def CurrentLocation(self):
        location = self.MasterFrame.GetPosition()
        return location

    def OnClose(self, event):
        # print(f'CLOSE EVENT! event = {event}')
        if self.DisableClose:
            return
        # print('GOT A CLOSE EVENT!', event, self.Window.Title)
        if not self.IgnoreClose:
            self.LastButtonClicked = None
            self.XFound = True
        if not self.CurrentlyRunningMainloop:  # quit if this is the current mainloop, otherwise don't quit!
            self.RootNeedsDestroying = True
        else:
            self.RootNeedsDestroying = True
            self.App.ExitMainLoop()  # kick the users out of the mainloop
            # print('exiting mainloop')

        self.MasterFrame.Destroy()
        # TODO - Sept - This is all new from prior release... comment out?
        """
        timer = wx.Timer(self.App)
        self.App.Bind(wx.EVT_TIMER, self.timer_timeout)
        timer.Start(milliseconds=100, oneShot=wx.TIMER_ONE_SHOT)
        # self.CurrentlyRunningMainloop = True
        # print(f'In main {self.Title}')
        ################################# CALL GUWxTextCtrlI MAINLOOP ############################

        self.App.MainLoop()
        # self.CurrentlyRunningMainloop = False
        timer.Stop()
        print('after mainloop in close')
        # TODO end
        """

        self.TKrootDestroyed = True
        self.RootNeedsDestroying = True


    @property
    def Size(self):
        size = self.MasterFrame.GetSize()
        return size

    @Size.setter
    def Size(self, size):
        self.MasterFrame.SetSize(size[0], size[1])

    def SizeChanged(self):
        size = self.Size
        self.Size = size[0] + 1, size[1] + 1
        self.Size = size
        self.MasterFrame.SetSizer(self.OuterSizer)
        self.OuterSizer.Fit(self.MasterFrame)

    def __getitem__(self, key):
        """
        Returns Element that matches the passed in key.
        This is "called" by writing code as thus:
        window['element key'].Update

        :param key: (Any) The key to find
        :return: Union[Element, None] The element found or None if no element was found
        """
        try:
            return self.Element(key)
        except Exception as e:
            print('The key you passed in is no good. Key = {}*'.format(key))
            return None


    def __call__(self, *args, **kwargs):
        """
        Call window.Read but without having to type it out.
        window() == window.Read()
        window(timeout=50) == window.Read(timeout=50)

        :param args:
        :param kwargs:
        :return: Tuple[Any, Dict[Any:Any]] The famous event, values that Read returns.
        """
        return self.Read(*args, **kwargs)

    add_row = AddRow
    add_rows = AddRows
    alpha_channel = AlphaChannel
    bring_to_front = BringToFront
    close = Close
    current_location = CurrentLocation
    disable = Disable
    disappear = Disappear
    element = Element
    enable = Enable
    fill = Fill
    finalize = Finalize
    find_element = FindElement
    find_element_with_focus = FindElementWithFocus
    get_screen_dimensions = GetScreenDimensions
    hide = Hide
    layout = Layout
    load_from_disk = LoadFromDisk
    maximize = Maximize
    minimize = Minimize
    move = Move
    read = Read
    reappear = Reappear
    refresh = Refresh
    save_to_disk = SaveToDisk
    set_alpha = SetAlpha
    set_icon = SetIcon
    size = Size
    size_changed = SizeChanged
    un_hide = UnHide
    visibility_changed = VisibilityChanged

FlexForm = Window

# =========================================================================== #
# Stops the mainloop and sets the event information                           #
# =========================================================================== #

def element_callback_quit_mainloop(element):
    if element.Key is not None:
        element.ParentForm.LastButtonClicked = element.Key
    else:
        element.ParentForm.LastButtonClicked = ''
    element.ParentForm.FormRemainedOpen = True
    if element.ParentForm.CurrentlyRunningMainloop:
        element.ParentForm.App.ExitMainLoop() # kick the users out of the mainloop


def quit_mainloop(window):
    window.App.ExitMainLoop()


# =========================================================================== #
# Convert from characters to pixels                                           #
# =========================================================================== #
# def convert_tkinter_size_to_Wx(size):
#     """
#     Converts size in characters to size in pixels
#     :param size:  size in characters, rows
#     :return: size in pixels, pixels
#     """
#     qtsize = size
#     if size[1] is not None and size[1] < DEFAULT_PIXEL_TO_CHARS_CUTOFF:        # change from character based size to pixels (roughly)
#         qtsize = size[0]*DEFAULT_PIXELS_TO_CHARS_SCALING[0], size[1]*DEFAULT_PIXELS_TO_CHARS_SCALING[1]
#     return qtsize


# =========================================================================== #
# Convert from characters to pixels                                           #
# =========================================================================== #
def _convert_tkinter_size_to_Wx(size, scaling=DEFAULT_PIXELS_TO_CHARS_SCALING, height_cutoff=DEFAULT_PIXEL_TO_CHARS_CUTOFF):
    """
    Converts size in characters to size in pixels
    :param size:  size in characters, rows
    :return: size in pixels, pixels
    """
    qtsize = size
    if size[1] is not None and size[1] < height_cutoff:        # change from character based size to pixels (roughly)
        qtsize = size[0]*scaling[0], size[1]*scaling[1]
    return qtsize



def font_to_wx_font(font):
    """
    Convert from font string/tyuple into a Qt style sheet string
    :param font: "Arial 10 Bold" or ('Arial', 10, 'Bold)
    :return: style string that can be combined with other style strings
    """

    if font is None:
        return ''

    if type(font) is str:
        _font = font.split(' ')
    else:
        _font = font
    name = _font[0]
    family = _font[0]
    point_size = int(_font[1])

    # style = _font[2]

    underline =  'underline' in _font[2:]
    bold =  'bold' in _font

    wxfont = wx.Font(point_size,
                     wx.FONTFAMILY_DEFAULT,
                     wx.FONTSTYLE_NORMAL,
                     wx.FONTWEIGHT_BOLD if bold else wx.FONTWEIGHT_NORMAL,
                     underline,
                     faceName=family)

    return wxfont



def preprocess_radio_elements(top_window, window):
    for row in window.Rows:
        for element in row:
            if element.Type == ELEM_TYPE_INPUT_RADIO:
                if element.WxRadioButton is None:
                    element.WxRadioButton = wx.RadioButton(top_window.MasterPanel, id=wx.ID_ANY, label=element.Text, style=wx.RB_GROUP)
                    create_wx_radio_buttons(top_window, top_window, element.GroupID)
            if element.Type in (ELEM_TYPE_COLUMN, ELEM_TYPE_FRAME,ELEM_TYPE_TAB_GROUP, ELEM_TYPE_TAB) :
                preprocess_radio_elements(top_window, element)


def create_wx_radio_buttons(top_window, window, group_id):
    for row in window.Rows:
        for element in row:
            if element.Type == ELEM_TYPE_INPUT_RADIO:
                if element.GroupID == group_id and element.WxRadioButton is None:
                    element.WxRadioButton = wx.RadioButton(top_window.MasterPanel, id=wx.ID_ANY, label=element.Text )
            if element.Type in (ELEM_TYPE_COLUMN, ELEM_TYPE_FRAME,ELEM_TYPE_TAB_GROUP, ELEM_TYPE_TAB) :
                create_wx_radio_buttons(top_window, element, group_id)


# ################################################################################
# ################################################################################
#  END OF ELEMENT DEFINITIONS
# ################################################################################
# ################################################################################


# =========================================================================== #
# Button Lazy Functions so the caller doesn't have to define a bunch of stuff #
# =========================================================================== #


# -------------------------  FOLDER BROWSE Element lazy function  ------------------------- #
def FolderBrowse(button_text='Browse', target=(ThisRow, -1), initial_folder=None, tooltip=None, size=(None, None),
                 auto_size_button=None, button_color=None, disabled=False, change_submits=False, font=None, pad=None,
                 key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FOLDER, target=target,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  disabled=disabled, button_color=button_color, change_submits=change_submits, font=font, pad=pad,
                  key=key)


# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileBrowse(button_text='Browse', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), initial_folder=None,
               tooltip=None, size=(None, None), auto_size_button=None, button_color=None, change_submits=False,
               font=None, disabled=False,
               pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  change_submits=change_submits, disabled=disabled, button_color=button_color, font=font, pad=pad,
                  key=key)


# -------------------------  FILES BROWSE Element (Multiple file selection) lazy function  ------------------------- #
def FilesBrowse(button_text='Browse', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), disabled=False,
                initial_folder=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                change_submits=False,
                font=None, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FILES, target=target, file_types=file_types,
                  initial_folder=initial_folder, change_submits=change_submits, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button,
                  disabled=disabled, button_color=button_color, font=font, pad=pad, key=key)


# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileSaveAs(button_text='Save As...', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), initial_folder=None,
               disabled=False, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
               change_submits=False, font=None,
               pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_SAVEAS_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, change_submits=change_submits,
                  font=font, pad=pad, key=key)


# -------------------------  SAVE AS Element lazy function  ------------------------- #
def SaveAs(button_text='Save As...', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), initial_folder=None,
           disabled=False, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
           change_submits=False, font=None,
           pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_SAVEAS_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, change_submits=change_submits,
                  font=font, pad=pad, key=key)


# -------------------------  SAVE BUTTON  lazy function  ------------------------- #
def Save(button_text='Save', size=(None, None), auto_size_button=None, button_color=None, bind_return_key=True,
         disabled=False, tooltip=None, font=None, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  SUBMIT BUTTON lazy function  ------------------------- #
def Submit(button_text='Submit', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
           bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  OPEN BUTTON lazy function  ------------------------- #
def Open(button_text='Open', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
         bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  OK BUTTON lazy function  ------------------------- #
def OK(button_text='OK', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
       bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  YES BUTTON lazy function  ------------------------- #
def Ok(button_text='Ok', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
       bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  CANCEL BUTTON lazy function  ------------------------- #
def Cancel(button_text='Cancel', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
           tooltip=None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  QUIT BUTTON lazy function  ------------------------- #
def Quit(button_text='Quit', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
         font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  Exit BUTTON lazy function  ------------------------- #
def Exit(button_text='Exit', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
         font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  YES BUTTON lazy function  ------------------------- #
def Yes(button_text='Yes', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
        font=None, bind_return_key=True, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  NO BUTTON lazy function  ------------------------- #
def No(button_text='No', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
       font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  NO BUTTON lazy function  ------------------------- #
def Help(button_text='Help', size=(None, None), auto_size_button=None, button_color=None, disabled=False, font=None,
         tooltip=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  GENERIC BUTTON lazy function  ------------------------- #
def SimpleButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                 border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                 font=None, bind_return_key=False, disabled=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  CLOSE BUTTON lazy function  ------------------------- #
def CloseButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
                bind_return_key=False, disabled=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


CButton = CloseButton


# -------------------------  GENERIC BUTTON lazy function  ------------------------- #
def ReadButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
               border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
               bind_return_key=False, disabled=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


ReadFormButton = ReadButton
RButton = ReadFormButton


# -------------------------  Realtime BUTTON lazy function  ------------------------- #
def RealtimeButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                   border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                   font=None, disabled=False, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_REALTIME, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  Dummy BUTTON lazy function  ------------------------- #
def DummyButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
                disabled=False, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN_ONLY, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  button_color=button_color, font=font, disabled=disabled, bind_return_key=bind_return_key, focus=focus,
                  pad=pad, key=key)


# -------------------------  Calendar Chooser Button lazy function  ------------------------- #
def CalendarButton(button_text, target=(None, None), close_when_date_chosen=True, default_date_m_d_y=(None, None, None),
                   image_filename=None, image_data=None, image_size=(None, None),
                   image_subsample=None, tooltip=None, border_width=None, size=(None, None), auto_size_button=None,
                   button_color=None, disabled=False, font=None, bind_return_key=False, focus=False, pad=None,
                   key=None):
    button = Button(button_text=button_text, button_type=BUTTON_TYPE_CALENDAR_CHOOSER, target=target,
                    image_filename=image_filename, image_data=image_data, image_size=image_size,
                    image_subsample=image_subsample, border_width=border_width, tooltip=tooltip, size=size,
                    auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                    bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)
    button.CalendarCloseWhenChosen = close_when_date_chosen
    button.DefaultDate_M_D_Y = default_date_m_d_y
    return button


# -------------------------  Calendar Chooser Button lazy function  ------------------------- #
def ColorChooserButton(button_text, target=(None, None), image_filename=None, image_data=None, image_size=(None, None),
                       image_subsample=None, tooltip=None, border_width=None, size=(None, None), auto_size_button=None,
                       button_color=None, disabled=False, font=None, bind_return_key=False, focus=False, pad=None,
                       key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_COLOR_CHOOSER, target=target,
                  image_filename=image_filename, image_data=image_data, image_size=image_size,
                  image_subsample=image_subsample, border_width=border_width, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


#####################################  -----  RESULTS   ------ ##################################################

def AddToReturnDictionary(form, element, value):
    form.ReturnValuesDictionary[element.Key] = value
    return
    if element.Key is None:
        form.ReturnValuesDictionary[form.DictionaryKeyCounter] = value
        element.Key = form.DictionaryKeyCounter
        form.DictionaryKeyCounter += 1
    else:
        form.ReturnValuesDictionary[element.Key] = value


def AddToReturnList(form, value):
    form.ReturnValuesList.append(value)


# ----------------------------------------------------------------------------#
# -------  FUNCTION InitializeResults.  Sets up form results matrix  --------#
def InitializeResults(form):
    BuildResults(form, True, form)
    return


# =====  Radio Button RadVar encoding and decoding =====#
# =====  The value is simply the row * 1000 + col  =====#
def DecodeRadioRowCol(RadValue):
    row = RadValue // 1000
    col = RadValue % 1000
    return row, col


def EncodeRadioRowCol(row, col):
    RadValue = row * 1000 + col
    return RadValue


# -------  FUNCTION BuildResults.  Form exiting so build the results to pass back  ------- #
# format of return values is
# (Button Pressed, input_values)
def BuildResults(form, initialize_only, top_level_form):
    # Results for elements are:
    #   TEXT - Nothing
    #   INPUT - Read value from TK
    #   Button - Button Text and position as a Tuple

    # Get the initialized results so we don't have to rebuild
    form.DictionaryKeyCounter = 0
    form.ReturnValuesDictionary = {}
    form.ReturnValuesList = []
    BuildResultsForSubform(form, initialize_only, top_level_form)
    # try:
    #     BuildResultsForSubform(form, initialize_only, top_level_form)
    # except:
    #     print('Error building return values')
    if not top_level_form.LastButtonClickedWasRealtime:
        top_level_form.LastButtonClicked = None
    return form.ReturnValues


def BuildResultsForSubform(form, initialize_only, top_level_form):
    button_pressed_text = top_level_form.LastButtonClicked
    for row_num, row in enumerate(form.Rows):
        for col_num, element in enumerate(row):
            if element.Key is not None and WRITE_ONLY_KEY in str(element.Key):
                continue
            value = None
            if element.Type == ELEM_TYPE_COLUMN:
                element.DictionaryKeyCounter = top_level_form.DictionaryKeyCounter
                element.ReturnValuesList = []
                element.ReturnValuesDictionary = {}
                BuildResultsForSubform(element, initialize_only, top_level_form)
                for item in element.ReturnValuesList:
                    AddToReturnList(top_level_form, item)
                if element.UseDictionary:
                    top_level_form.UseDictionary = True
                if element.ReturnValues[0] is not None:  # if a button was clicked
                    button_pressed_text = element.ReturnValues[0]

            if element.Type == ELEM_TYPE_FRAME:
                element.DictionaryKeyCounter = top_level_form.DictionaryKeyCounter
                element.ReturnValuesList = []
                element.ReturnValuesDictionary = {}
                BuildResultsForSubform(element, initialize_only, top_level_form)
                for item in element.ReturnValuesList:
                    AddToReturnList(top_level_form, item)
                if element.UseDictionary:
                    top_level_form.UseDictionary = True
                if element.ReturnValues[0] is not None:  # if a button was clicked
                    button_pressed_text = element.ReturnValues[0]

            if element.Type == ELEM_TYPE_TAB_GROUP:
                element.DictionaryKeyCounter = top_level_form.DictionaryKeyCounter
                element.ReturnValuesList = []
                element.ReturnValuesDictionary = {}
                BuildResultsForSubform(element, initialize_only, top_level_form)
                for item in element.ReturnValuesList:
                    AddToReturnList(top_level_form, item)
                if element.UseDictionary:
                    top_level_form.UseDictionary = True
                if element.ReturnValues[0] is not None:  # if a button was clicked
                    button_pressed_text = element.ReturnValues[0]

            if element.Type == ELEM_TYPE_TAB:
                element.DictionaryKeyCounter = top_level_form.DictionaryKeyCounter
                element.ReturnValuesList = []
                element.ReturnValuesDictionary = {}
                BuildResultsForSubform(element, initialize_only, top_level_form)
                for item in element.ReturnValuesList:
                    AddToReturnList(top_level_form, item)
                if element.UseDictionary:
                    top_level_form.UseDictionary = True
                if element.ReturnValues[0] is not None:  # if a button was clicked
                    button_pressed_text = element.ReturnValues[0]

            if not initialize_only:
                if element.Type == ELEM_TYPE_INPUT_TEXT:
                    value = element.WxTextCtrl.GetValue()
                    if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                        element.WxTextCtrl.SetValue('')
                elif element.Type == ELEM_TYPE_INPUT_CHECKBOX:
                    value = element.WxCheckbox.GetValue()
                    value = (value != 0)
                elif element.Type == ELEM_TYPE_INPUT_RADIO:
                    value = element.WxRadioButton.GetValue()
                elif element.Type == ELEM_TYPE_BUTTON:
                    if top_level_form.LastButtonClicked == element.ButtonText:
                        button_pressed_text = top_level_form.LastButtonClicked
                        if element.BType != BUTTON_TYPE_REALTIME:  # Do not clear realtime buttons
                            top_level_form.LastButtonClicked = None
                    if element.BType == BUTTON_TYPE_CALENDAR_CHOOSER:
                        try:
                            value = element.TKCal.selection
                        except:
                            value = None
                    else:
                        try:
                            value = element.TKStringVar.get()
                        except:
                            value = None
                elif element.Type == ELEM_TYPE_INPUT_COMBO:
                    value = element.WxComboBox.GetValue()
                elif element.Type == ELEM_TYPE_INPUT_OPTION_MENU:
                    value = element.TKStringVar.get()
                elif element.Type == ELEM_TYPE_INPUT_LISTBOX:
                    try:
                        items = element.TKListbox.curselection()
                        value = [element.Values[int(item)] for item in items]
                    except:
                        value = ''
                elif element.Type == ELEM_TYPE_INPUT_SPIN:
                    value = element.WxTextCtrl.GetValue()
                    # value = element.CurrentValue
                elif element.Type == ELEM_TYPE_INPUT_SLIDER:
                    try:
                        value = element.TKIntVar.get()
                    except:
                        value = 0
                elif element.Type == ELEM_TYPE_INPUT_MULTILINE:
                    try:
                        value = element.WxTextCtrl.GetValue()
                    except:
                        pass

                    if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                        element.WxTextCtrl.SetValue('')
                elif element.Type == ELEM_TYPE_TAB_GROUP:
                    try:
                        value = element.TKNotebook.tab(element.TKNotebook.index('current'))['text']
                        tab_key = element.FindKeyFromTabName(value)
                        if tab_key is not None:
                            value = tab_key
                    except:
                        value = None
                elif element.Type == ELEM_TYPE_TABLE:
                    value = element.SelectedRows
                elif element.Type == ELEM_TYPE_TREE:
                    value = element.SelectedRows
                elif element.Type == ELEM_TYPE_GRAPH:
                    value = element.ClickPosition
            else:
                value = None

            # if an input type element, update the results
            if element.Type != ELEM_TYPE_BUTTON and \
                    element.Type != ELEM_TYPE_TEXT and \
                    element.Type != ELEM_TYPE_IMAGE and \
                    element.Type != ELEM_TYPE_OUTPUT and \
                    element.Type != ELEM_TYPE_PROGRESS_BAR and \
                    element.Type != ELEM_TYPE_COLUMN and \
                    element.Type != ELEM_TYPE_FRAME \
                    and element.Type != ELEM_TYPE_TAB:
                AddToReturnList(form, value)
                AddToReturnDictionary(top_level_form, element, value)
            elif (element.Type == ELEM_TYPE_BUTTON and
                  element.BType == BUTTON_TYPE_CALENDAR_CHOOSER and
                  element.Target == (None, None)) or \
                    (element.Type == ELEM_TYPE_BUTTON and
                     element.BType == BUTTON_TYPE_COLOR_CHOOSER and
                     element.Target == (None, None)) or \
                    (element.Type == ELEM_TYPE_BUTTON
                     and element.Key is not None and
                     (element.BType in (BUTTON_TYPE_SAVEAS_FILE, BUTTON_TYPE_BROWSE_FILE, BUTTON_TYPE_BROWSE_FILES,
                                        BUTTON_TYPE_BROWSE_FOLDER))):
                AddToReturnList(form, value)
                AddToReturnDictionary(top_level_form, element, value)

    # if this is a column, then will fail so need to wrap with tr
    try:
        if form.ReturnKeyboardEvents and form.LastKeyboardEvent is not None:
            button_pressed_text = form.LastKeyboardEvent
            form.LastKeyboardEvent = None
    except:
        pass

    try:
        form.ReturnValuesDictionary.pop(None, None)  # clean up dictionary include None was included
    except:
        pass

    if not form.UseDictionary:
        form.ReturnValues = button_pressed_text, form.ReturnValuesList
    else:
        form.ReturnValues = button_pressed_text, form.ReturnValuesDictionary

    return form.ReturnValues


def FillFormWithValues(form, values_dict):
    FillSubformWithValues(form, values_dict)


def FillSubformWithValues(form, values_dict):
    for row_num, row in enumerate(form.Rows):
        for col_num, element in enumerate(row):
            value = None
            if element.Type == ELEM_TYPE_COLUMN:
                FillSubformWithValues(element, values_dict)
            if element.Type == ELEM_TYPE_FRAME:
                FillSubformWithValues(element, values_dict)
            if element.Type == ELEM_TYPE_TAB_GROUP:
                FillSubformWithValues(element, values_dict)
            if element.Type == ELEM_TYPE_TAB:
                FillSubformWithValues(element, values_dict)
            try:
                value = values_dict[element.Key]
            except:
                continue
            if element.Type == ELEM_TYPE_INPUT_TEXT:
                element.Update(value)
            elif element.Type == ELEM_TYPE_INPUT_CHECKBOX:
                element.Update(value)
            elif element.Type == ELEM_TYPE_INPUT_RADIO:
                element.Update(value)
            elif element.Type == ELEM_TYPE_INPUT_COMBO:
                element.Update(value)
            elif element.Type == ELEM_TYPE_INPUT_OPTION_MENU:
                element.Update(value)
            elif element.Type == ELEM_TYPE_INPUT_LISTBOX:
                element.SetValue(value)
            elif element.Type == ELEM_TYPE_INPUT_SLIDER:
                element.Update(value)
            elif element.Type == ELEM_TYPE_INPUT_MULTILINE:
                element.Update(value)
            elif element.Type == ELEM_TYPE_INPUT_SPIN:
                element.Update(value)
            elif element.Type == ELEM_TYPE_BUTTON:
                element.Update(value)


def _FindElementFromKeyInSubForm(form, key):
    for row_num, row in enumerate(form.Rows):
        for col_num, element in enumerate(row):
            if element.Type == ELEM_TYPE_COLUMN:
                matching_elem = _FindElementFromKeyInSubForm(element, key)
                if matching_elem is not None:
                    return matching_elem
            if element.Type == ELEM_TYPE_FRAME:
                matching_elem = _FindElementFromKeyInSubForm(element, key)
                if matching_elem is not None:
                    return matching_elem
            if element.Type == ELEM_TYPE_TAB_GROUP:
                matching_elem = _FindElementFromKeyInSubForm(element, key)
                if matching_elem is not None:
                    return matching_elem
            if element.Type == ELEM_TYPE_TAB:
                matching_elem = _FindElementFromKeyInSubForm(element, key)
                if matching_elem is not None:
                    return matching_elem
            if element.Key == key:
                return element


def _FindElementWithFocusInSubForm(form):
    for row_num, row in enumerate(form.Rows):
        for col_num, element in enumerate(row):
            if element.Type == ELEM_TYPE_COLUMN:
                matching_elem = _FindElementWithFocusInSubForm(element)
                if matching_elem is not None:
                    return matching_elem
            if element.Type == ELEM_TYPE_FRAME:
                matching_elem = _FindElementWithFocusInSubForm(element)
                if matching_elem is not None:
                    return matching_elem
            if element.Type == ELEM_TYPE_TAB_GROUP:
                matching_elem = _FindElementWithFocusInSubForm(element)
                if matching_elem is not None:
                    return matching_elem
            if element.Type == ELEM_TYPE_TAB:
                matching_elem = _FindElementWithFocusInSubForm(element)
                if matching_elem is not None:
                    return matching_elem
            if element.Type == ELEM_TYPE_INPUT_TEXT:
                if element.TKEntry is not None:
                    if element.TKEntry is element.TKEntry.focus_get():
                        return element
            if element.Type == ELEM_TYPE_INPUT_MULTILINE:
                if element.TKText is not None:
                    if element.TKText is element.TKText.focus_get():
                        return element


if sys.version_info[0] >= 3:
    def AddMenuItem(top_menu, sub_menu_info, element, is_sub_menu=False, skip=False):
        return_val = None
        if type(sub_menu_info) is str:
            if not is_sub_menu and not skip:
                # print(f'Adding command {sub_menu_info}')
                pos = sub_menu_info.find('&')
                if pos != -1:
                    if pos == 0 or sub_menu_info[pos - 1] != "\\":
                        sub_menu_info = sub_menu_info[:pos] + sub_menu_info[pos + 1:]
                if sub_menu_info == '---':
                    top_menu.Append(wx.ID_SEPARATOR)
                else:
                    try:
                        item_without_key = sub_menu_info[:sub_menu_info.index(MENU_KEY_SEPARATOR)]
                    except:
                        item_without_key = sub_menu_info

                    if item_without_key[0] == MENU_DISABLED_CHARACTER:
                        id = top_menu.Append(wx.ID_ANY, item_without_key[len(MENU_DISABLED_CHARACTER):])
                        element.id_to_text[id] = sub_menu_info[1:]
                        top_menu.Enable(id.Id, False)
                    else:
                        id = top_menu.Append(wx.ID_ANY, item_without_key)
                        element.id_to_text[id] = sub_menu_info

        else:
            i = 0
            while i < (len(sub_menu_info)):
                item = sub_menu_info[i]
                if i != len(sub_menu_info) - 1:
                    if type(sub_menu_info[i + 1]) == list:
                        new_menu = wx.Menu()
                        return_val = new_menu
                        pos = sub_menu_info[i].find('&')
                        if pos != -1:
                            if pos == 0 or sub_menu_info[i][pos - 1] != "\\":
                                sub_menu_info[i] = sub_menu_info[i][:pos] + sub_menu_info[i][pos + 1:]
                        if sub_menu_info[i][0] == MENU_DISABLED_CHARACTER:
                            id = top_menu.AppendSubMenu(new_menu, sub_menu_info[i][len(MENU_DISABLED_CHARACTER):])
                            top_menu.Enable(id.Id, False)
                        else:
                            top_menu.AppendSubMenu(new_menu, sub_menu_info[i])
                        AddMenuItem(new_menu, sub_menu_info[i + 1], element, is_sub_menu=True)
                        i += 1  # skip the next one
                    else:
                        AddMenuItem(top_menu, item, element)
                else:
                    AddMenuItem(top_menu, item, element)
                i += 1
        return return_val

if sys.version_info[0] >= 3:
    def AddMenuItem2(top_menu, sub_menu_info, element, is_sub_menu=False, skip=False):
        if type(sub_menu_info) is str:
            if not is_sub_menu and not skip:
                # print(f'Adding command {sub_menu_info}')
                pos = sub_menu_info.find('&')
                if pos != -1:
                    if pos == 0 or sub_menu_info[pos - 1] != "\\":
                        sub_menu_info = sub_menu_info[:pos] + sub_menu_info[pos + 1:]
                if sub_menu_info == '---':
                    top_menu.Append(wx.ID_SEPARATOR)
                else:
                    top_menu.Append(wx.ID_ANY, sub_menu_info)
        else:
            i = 0
            while i < (len(sub_menu_info)):
                item = sub_menu_info[i]
                if i != len(sub_menu_info) - 1:
                    if type(sub_menu_info[i + 1]) == list:
                        new_menu = wx.Menu()
                        pos = sub_menu_info[i].find('&')
                        if pos != -1:
                            if pos == 0 or sub_menu_info[i][pos - 1] != "\\":
                                sub_menu_info[i] = sub_menu_info[i][:pos] + sub_menu_info[i][pos + 1:]
                        top_menu.AppendSubMenu(new_menu, sub_menu_info[i])
                        AddMenuItem(new_menu, sub_menu_info[i + 1], element, is_sub_menu=True)
                        i += 1  # skip the next one
                    else:
                        AddMenuItem(top_menu, item, element)
                else:
                    AddMenuItem(top_menu, item, element)
                i += 1
else:
    def AddMenuItem(top_menu, sub_menu_info, element, is_sub_menu=False, skip=False):
        if isinstance(sub_menu_info, types.StringType):
            if not is_sub_menu and not skip:
                # print(f'Adding command {sub_menu_info}')
                pos = sub_menu_info.find('&')
                if pos != -1:
                    if pos == 0 or sub_menu_info[pos - 1] != "\\":
                        sub_menu_info = sub_menu_info[:pos] + sub_menu_info[pos + 1:]
                if sub_menu_info == '---':
                    top_menu.add('separator')
                else:
                    top_menu.add_command(label=sub_menu_info, underline=pos,
                                         command=lambda: Menu._MenuItemChosenCallback(element, sub_menu_info))
        else:
            i = 0
            while i < (len(sub_menu_info)):
                item = sub_menu_info[i]
                if i != len(sub_menu_info) - 1:
                    if not isinstance(sub_menu_info[i + 1], types.StringType):
                        new_menu = tk.Menu(top_menu, tearoff=element.Tearoff)
                        pos = sub_menu_info[i].find('&')
                        if pos != -1:
                            if pos == 0 or sub_menu_info[i][pos - 1] != "\\":
                                sub_menu_info[i] = sub_menu_info[i][:pos] + sub_menu_info[i][pos + 1:]
                        top_menu.add_cascade(label=sub_menu_info[i], menu=new_menu, underline=pos)
                        AddMenuItem(new_menu, sub_menu_info[i + 1], element, is_sub_menu=True)
                        i += 1  # skip the next one
                    else:
                        AddMenuItem(top_menu, item, element)
                else:
                    AddMenuItem(top_menu, item, element)
                i += 1



 #     #        ######
 #  #  # #    # #     # #   # ##### #    #  ####  #    #
 #  #  #  #  #  #     #  # #    #   #    # #    # ##   #
 #  #  #   ##   ######    #     #   ###### #    # # #  #
 #  #  #   ##   #         #     #   #    # #    # #  # #
 #  #  #  #  #  #         #     #   #    # #    # #   ##
  ## ##  #    # #         #     #   #    #  ####  #    #

# My crappy WxPython code

# ░░░░░░░░░░░█▀▀░░█░░░░░░
# ░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░
# ░░░░░░█░█░░░░░░░░░░▐░░░
# ░░░░░░▐▐░░░░░░░░░▄░▐░░░
# ░░░░░░█░░░░░░░░▄▀▀░▐░░░
# ░░░░▄▀░░░░░░░░▐░▄▄▀░░░░
# ░░▄▀░░░▐░░░░░█▄▀░▐░░░░░
# ░░█░░░▐░░░░░░░░▄░█░░░░░
# ░░░█▄░░▀▄░░░░▄▀▐░█░░░░░
# ░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░
# ░░▐█▐▄░░▀░░░░░░▐░█▄▄░░░
# ░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░
# ░░░░░░░░░░░░░░░░░░░░░░░



# ------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #
# =====================================   WxPython CODE STARTS HERE ================================================ #
# ------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #

def PackFormIntoFrame(form, containing_frame, toplevel_form):
    def pad_widget(widget):
        lrsizer = wx.BoxSizer(wx.HORIZONTAL)
        if full_element_pad[1] == full_element_pad[3]:  # if right = left
            lrsizer.Add(widget, 0, wx.LEFT | wx.RIGHT, border=full_element_pad[1])
        else:
            sizer = wx.BoxSizer(wx.HORIZONTAL)
            sizer.Add(widget, 0, wx.LEFT, border=full_element_pad[3])
            lrsizer.Add(sizer, 0, wx.RIGHT, border=full_element_pad[1])

        top_bottom_sizer = wx.BoxSizer(wx.HORIZONTAL)
        if full_element_pad[0] == full_element_pad[2]:  # if top = bottom
            top_bottom_sizer.Add(lrsizer, 0, wx.TOP | wx.BOTTOM, border=full_element_pad[0])
        else:
            sizer = wx.BoxSizer(wx.HORIZONTAL)
            sizer.Add(lrsizer, 0, wx.TOP, border=full_element_pad[0])
            top_bottom_sizer.Add(sizer, 0, wx.BOTTOM, border=full_element_pad[2])
        return top_bottom_sizer

    #
    # font, text color, background color, size, disabled, visible, tooltip
    #
    def do_font_and_color(widget):
        if font:
            widget.SetFont(font_to_wx_font(font))
        if element.TextColor not in (None, COLOR_SYSTEM_DEFAULT):
            widget.SetForegroundColour(element.TextColor)
        if element.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
            widget.SetBackgroundColour(element.BackgroundColor)
        widget.SetMinSize(element_size)
        if element.Disabled:
            widget.Enable(False)
        if not element.Visible:
            widget.Hide()
        if element.Tooltip:
            widget.SetToolTip(element.Tooltip)

    def CharWidthInPixels():
        return tkinter.font.Font().measure('A')  # single character width

    border_depth = toplevel_form.BorderDepth if toplevel_form.BorderDepth is not None else DEFAULT_BORDER_WIDTH
    # --------------------------------------------------------------------------- #
    # ****************  Use FlexForm to build the tkinter window ********** ----- #
    # Building is done row by row.                                                #
    # --------------------------------------------------------------------------- #
    focus_set = False
    ######################### LOOP THROUGH ROWS #########################
    # *********** -------  Loop through ROWS  ------- ***********#
    for row_num, flex_row in enumerate(form.Rows):
        ######################### LOOP THROUGH ELEMENTS ON ROW #########################
        # *********** -------  Loop through ELEMENTS  ------- ***********#
        # *********** Make TK Row                             ***********#
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        for col_num, element in enumerate(flex_row):
            element.ParentForm = toplevel_form  # save the button's parent form object
            if toplevel_form.Font and (element.Font == DEFAULT_FONT or not element.Font):
                font = toplevel_form.Font
                element.Font = font
            elif element.Font is not None:
                font = element.Font
            else:
                font = DEFAULT_FONT
                # -------  Determine Auto-Size setting on a cascading basis ------- #
            if element.AutoSizeText is not None:  # if element overide
                auto_size_text = element.AutoSizeText
            elif toplevel_form.AutoSizeText is not None:  # if form override
                auto_size_text = toplevel_form.AutoSizeText
            else:
                auto_size_text = DEFAULT_AUTOSIZE_TEXT
            element_type = element.Type
            # Set foreground color
            text_color = element.TextColor
            # Determine Element size
            element_size = element.Size
            if (element_size == (None, None) and element_type not in (ELEM_TYPE_BUTTON, ELEM_TYPE_BUTTONMENU)):  # user did not specify a size
                element_size = toplevel_form.DefaultElementSize
            elif (element_size == (None, None) and element_type in (ELEM_TYPE_BUTTON, ELEM_TYPE_BUTTONMENU)):
                element_size = toplevel_form.DefaultButtonElementSize
            else:
                auto_size_text = False  # if user has specified a size then it shouldn't autosize
            full_element_pad = [0, 0, 0, 0]  # Top, Right, Bottom, Left
            elementpad = element.Pad if element.Pad is not None else toplevel_form.ElementPadding
            if type(elementpad[0]) != tuple:  # left and right
                full_element_pad[1] = full_element_pad[3] = elementpad[0]
            else:
                full_element_pad[3], full_element_pad[1] = elementpad[0]
            if type(elementpad[1]) != tuple:  # top and bottom
                full_element_pad[0] = full_element_pad[2] = elementpad[1]
            else:
                full_element_pad[0], full_element_pad[2] = elementpad[1]

            border_depth = toplevel_form.BorderDepth if toplevel_form.BorderDepth is not None else DEFAULT_BORDER_WIDTH
            try:
                if element.BorderWidth is not None:
                    border_depth = element.BorderWidth
            except:
                pass

            # -------------------------  COLUMN element  ------------------------- #
            if element_type == ELEM_TYPE_COLUMN:
                element = element   # type: Column
                element.WxBoxSizer = vsizer = wx.BoxSizer(wx.VERTICAL)
                element.WxHSizer = hsizer
                # element.WxScrollBar = wx.ScrollBar(toplevel_form.MasterFrame, id=wx.ID_ANY, style=wx.SB_VERTICAL)
                # vsizer.Add(element.WxScrollBar)
                PackFormIntoFrame(element, vsizer, toplevel_form)

                hsizer.Add(pad_widget(vsizer), 0)
                if not element.Visible:
                    hsizer.Hide(vsizer, recursive=True)

            # # column_widget = QWidget()
            # column_widget = QGroupBox()
            # element.QT_QGroupBox = column_widget
            # # column_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
            # style = create_style_from_font(font)
            # if element.BackgroundColor is not None:
            #     style = style_entry(background_color=element.BackgroundColor)
            #     style += 'background-color: %s;' % element.BackgroundColor
            # style += style_entry(border='0px solid gray')
            # # style += 'border: 0px solid gray; '
            # style = style_generate('QGroupBox', style)
            # column_widget.setStyleSheet(style)
            #
            # column_layout = QFormLayout()
            # column_vbox = QVBoxLayout()
            #
            # PackFormIntoFrame(element, column_layout, toplevel_win)
            #
            # column_vbox.addLayout(column_layout)
            # column_widget.setLayout(column_vbox)
            #
            # # column_widget.setStyleSheet(style)
            # if not element.Visible:
            #     column_widget.setVisible(False)
            #
            # qt_row_layout.addWidget(column_widget)


            #     if element.Scrollable:
            #         col_frame = TkScrollableFrame(tk_row_frame,
            #                                       element.VerticalScrollOnly)  # do not use yet!  not working
            #         PackFormIntoFrame(element, col_frame.TKFrame, toplevel_form)
            #         col_frame.TKFrame.update()
            #         if element.Size == (None, None):  # if no size specified, use column width x column height/2
            #             col_frame.canvas.config(width=col_frame.TKFrame.winfo_reqwidth(),
            #                                     height=col_frame.TKFrame.winfo_reqheight() / 2)
            #         else:
            #             col_frame.canvas.config(width=element.Size[0], height=element.Size[1])
            #
            #         if not element.BackgroundColor in (None, COLOR_SYSTEM_DEFAULT):
            #             col_frame.canvas.config(background=element.BackgroundColor)
            #             col_frame.TKFrame.config(background=element.BackgroundColor, borderwidth=0,
            #                                      highlightthickness=0)
            #             col_frame.config(background=element.BackgroundColor, borderwidth=0, highlightthickness=0)
            #     else:
            #         col_frame = tk.Frame(tk_row_frame)
            #         PackFormIntoFrame(element, col_frame, toplevel_form)
            #
            #     col_frame.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1], expand=True, fill='both')
            #     if element.BackgroundColor != COLOR_SYSTEM_DEFAULT and element.BackgroundColor is not None:
            #         col_frame.configure(background=element.BackgroundColor, highlightbackground=element.BackgroundColor,
            #                             highlightcolor=element.BackgroundColor)
            # -------------------------  TEXT element  ------------------------- #
            elif element_type == ELEM_TYPE_TEXT:
                element = element       # type: Text
                if element.Justification is not None:
                    justification = element.Justification
                elif toplevel_form.TextJustification is not None:
                    justification = toplevel_form.TextJustification
                else:
                    justification = DEFAULT_TEXT_JUSTIFICATION
                style = wx.ALIGN_LEFT if justification.startswith('l') else wx.ALIGN_CENTER if justification.startswith('c') else wx.ALIGN_RIGHT
                # print(border_depth, element.BorderWidth)
                if border_depth:
                    if element.Relief:
                        if element.Relief in (RELIEF_SOLID, RELIEF_FLAT):
                            style |= wx.SIMPLE_BORDER
                        elif element.Relief == RELIEF_SUNKEN:
                            style |= wx.SUNKEN_BORDER
                        elif element.Relief in(RELIEF_RAISED, RELIEF_RIDGE):
                            style |= wx.RAISED_BORDER
                        elif element.Relief in (RELIEF_SUNKEN, RELIEF_SUNKEN):
                            style |= wx.SUNKEN_BORDER
                statictext = element.WxStaticText = wx.StaticText(toplevel_form.MasterPanel, -1, element.DisplayText, style=style)
                if font:
                    statictext.SetFont(font_to_wx_font(font))
                if element.TextColor not in (None, COLOR_SYSTEM_DEFAULT):
                    statictext.SetForegroundColour(element.TextColor)
                if element.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
                    statictext.SetBackgroundColour(element.BackgroundColor)
                display_text = element.DisplayText      # text to display
                if auto_size_text is False:
                    width, height = element_size
                else:
                    lines = display_text.split('\n')
                    max_line_len = max([len(l) for l in lines])
                    num_lines = len(lines)
                    if max_line_len > element_size[0]:  # if text exceeds element size, the will have to wrap
                        width = element_size[0]
                    else:
                        width = max_line_len
                    height = num_lines

                if element.ClickSubmits:                # bind events
                    statictext.Bind(wx.EVT_LEFT_UP, element._WxCallbackKeyboard)

                hsizer.Add(pad_widget(element.WxStaticText), 0)

                if not auto_size_text:
                    statictext.SetMinSize((width,height))

                if element.Tooltip:
                    statictext.SetToolTip(element.Tooltip)
                if not element.Visible:
                    statictext.Hide()


                # Set wrap-length for text (in PIXELS) == PAIN IN THE ASS
                # wraplen = tktext_label.winfo_reqwidth() + 40  # width of widget in Pixels
                # if not auto_size_text and height == 1:
                #     wraplen = 0
            # -------------------------  BUTTON element  ------------------------- #
            elif element_type == ELEM_TYPE_BUTTON:
                element = element        # type: Button
                element.WxButton = button = wx.Button(toplevel_form.MasterPanel, style=wx.NO_BORDER)
                button.SetLabelText(element.ButtonText)
                if font:
                    button.SetFont(font_to_wx_font(font))
                button.Bind(wx.EVT_BUTTON, element.ButtonCallBack)

                element.Location = (row_num, col_num)
                if element.AutoSizeButton is not None:
                    auto_size = element.AutoSizeButton
                else:
                    auto_size = toplevel_form.AutoSizeButtons
                if auto_size is False or element.Size[0] is not None:
                    width, height = element_size
                else:
                    width = 0
                    height = toplevel_form.DefaultButtonElementSize[1]

                if auto_size:
                    element.WxButton.SetWindowStyleFlag(element.WxButton.GetWindowStyleFlag() | wx.BU_EXACTFIT)
                else:
                    element.WxButton.SetMinSize(_convert_tkinter_size_to_Wx((width,height), DEFAULT_PIXEL_TO_CHARS_CUTOFF))
                if element.ButtonColor != (None, None) and element.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = element.ButtonColor
                elif toplevel_form.ButtonColor != (None, None) and toplevel_form.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = toplevel_form.ButtonColor
                else:
                    bc = DEFAULT_BUTTON_COLOR

                button.SetBackgroundColour(bc[1])
                button.SetForegroundColour(bc[0])

                sizer = pad_widget(button)
                hsizer.Add(sizer, 0)

                if not element.Visible:
                    button.Hide()
                if element.Tooltip:
                    button.SetToolTip(element.Tooltip)


            #     if btype != BUTTON_TYPE_REALTIME:
            #         tkbutton = tk.Button(tk_row_frame, text=btext, width=width, height=height,
            #                              command=element.ButtonCallBack, justify=tk.LEFT, bd=border_depth, font=font)
            #     else:
            #         tkbutton = tk.Button(tk_row_frame, text=btext, width=width, height=height, justify=tk.LEFT,
            #                              bd=border_depth, font=font)
            #         tkbutton.bind('<ButtonRelease-1>', element.ButtonReleaseCallBack)
            #         tkbutton.bind('<ButtonPress-1>', element.ButtonPressCallBack)
            #     if element.ImageFilename:  # if button has an image on it
            #         tkbutton.config(highlightthickness=0)
            #         photo = tk.PhotoImage(file=element.ImageFilename)
            #         if element.ImageSize != (None, None):
            #             width, height = element.ImageSize
            #             if element.ImageSubsample:
            #                 photo = photo.subsample(element.ImageSubsample)
            #         else:
            #             width, height = photo.width(), photo.height()
            #         tkbutton.config(image=photo, compound=tk.CENTER, width=width, height=height)
            #         tkbutton.image = photo
            #     if element.ImageData:  # if button has an image on it
            #         tkbutton.config(highlightthickness=0)
            #         photo = tk.PhotoImage(data=element.ImageData)
            #         if element.ImageSize != (None, None):
            #             width, height = element.ImageSize
            #             if element.ImageSubsample:
            #                 photo = photo.subsample(element.ImageSubsample)
            #         else:
            #             width, height = photo.width(), photo.height()
            #         tkbutton.config(image=photo, compound=tk.CENTER, width=width, height=height)
            #         tkbutton.image = photo
            #     if width != 0:
            #         tkbutton.configure(wraplength=wraplen + 10)  # set wrap to width of widget
            #     tkbutton.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
            #     if element.BindReturnKey:
            #         element.TKButton.bind('<Return>', element._ReturnKeyHandler)
            #     if element.Focus is True or (toplevel_form.UseDefaultFocus and not focus_set):
            #         focus_set = True
            #         element.TKButton.bind('<Return>', element._ReturnKeyHandler)
            #         element.TKButton.focus_set()
            #         toplevel_form.TKroot.focus_force()
            #     if element.Disabled == True:
            #         element.TKButton['state'] = 'disabled'
            #     if element.Tooltip is not None:
            #         element.TooltipObject = ToolTip(element.TKButton, text=element.Tooltip,
            #                                         timeout=DEFAULT_TOOLTIP_TIME)

            # # -------------------------  INPUT element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_TEXT:
                element = element       # type: InputText
                if element.Justification is not None:
                    justification = element.Justification
                elif toplevel_form.TextJustification is not None:
                    justification = toplevel_form.TextJustification
                else:
                    justification = DEFAULT_TEXT_JUSTIFICATION
                justify = wx.ALIGN_LEFT if justification.startswith('l') else wx.ALIGN_CENTER_HORIZONTAL if justification.startswith('c') else wx.ALIGN_RIGHT
                if element.PasswordCharacter:
                    justify |= wx.TE_PASSWORD

                element.WxTextCtrl = text_ctrl = wx.TextCtrl(toplevel_form.MasterPanel, style=justify)

                if element.DefaultText:
                    text_ctrl.SetValue(element.DefaultText)
                if font:
                    text_ctrl.SetFont(font_to_wx_font(font))
                if element.TextColor not in (None, COLOR_SYSTEM_DEFAULT):
                    text_ctrl.SetForegroundColour(element.TextColor)
                if element.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
                    text_ctrl.SetBackgroundColour(element.BackgroundColor)
                text_ctrl.SetMinSize(element_size)
                if element.Disabled:
                    text_ctrl.Enable(False)
                if element.ChangeSubmits:
                    text_ctrl.Bind(wx.EVT_KEY_UP, element._WxCallbackKeyboard)
                    text_ctrl.Bind(wx.EVT_TEXT_ENTER, element._ReturnKeyHandler)

                sizer = pad_widget(text_ctrl)

                hsizer.Add(sizer, 0)

                if not element.Visible:
                    text_ctrl.Hide()
                if element.Tooltip:
                    text_ctrl.SetToolTip(element.Tooltip)

                if element.Focus is True or (toplevel_form.UseDefaultFocus and not focus_set):
                    focus_set = True
                    element.SetFocus()

            # -------------------------  COMBO BOX (Drop Down) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_COMBO:
                element = element       # type: Combo
                if element.Readonly:
                    element.WxComboBox = wx.Choice(toplevel_form.MasterPanel,
                                                              id=wx.ID_ANY,
                                                              choices=element.Values)
                else:
                    element.WxComboBox = wx.ComboBox(toplevel_form.MasterPanel,
                                                            id=wx.ID_ANY,
                                                            choices=element.Values)
                if element.DefaultValue:
                    element.WxComboBox.SetSelection(element.WxComboBox.FindString(element.DefaultValue))
                if element.Readonly:
                    element.WxComboBox.SetWindowStyle(wx.CB_READONLY)

                do_font_and_color(element.WxComboBox)
                sizer = pad_widget(element.WxComboBox)

                if element.ChangeSubmits:
                    element.WxComboBox.Bind(wx.EVT_COMBOBOX, element._WxCallbackKeyboard)

                hsizer.Add(sizer, 0)

                # max_line_len = max([len(str(l)) for l in element.Values])
                # if auto_size_text is False:
                #     width = element_size[0]
                # else:
                #     width = max_line_len
                # element.TKStringVar = tk.StringVar()
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     combostyle = ttk.Style()
                #     try:
                #         combostyle.theme_create('combostyle',
                #                                 settings={'TCombobox':
                #                                               {'configure':
                #                                                    {'selectbackground': element.BackgroundColor,
                #                                                     'fieldbackground': element.BackgroundColor,
                #                                                     'foreground': text_color,
                #                                                     'background': element.BackgroundColor}
                #                                                }})
                #     except:
                #         try:
                #             combostyle.theme_settings('combostyle',
                #                                       settings={'TCombobox':
                #                                                     {'configure':
                #                                                          {'selectbackground': element.BackgroundColor,
                #                                                           'fieldbackground': element.BackgroundColor,
                #                                                           'foreground': text_color,
                #                                                           'background': element.BackgroundColor}
                #                                                      }})
                #         except:
                #             pass
                #     # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
                #     combostyle.theme_use('combostyle')
                # element.TKCombo = ttk.Combobox(tk_row_frame, width=width, textvariable=element.TKStringVar, font=font)
                # if element.Size[1] != 1 and element.Size[1] is not None:
                #     element.TKCombo.configure(height=element.Size[1])
                # # element.TKCombo['state']='readonly'
                # element.TKCombo['values'] = element.Values
                #
                # # if element.InitializeAsDisabled:
                # #     element.TKCombo['state'] = 'disabled'
                # # if element.BackgroundColor is not None:
                # #     element.TKCombo.configure(background=element.BackgroundColor)
                # element.TKCombo.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # if element.DefaultValue:
                #     for i, v in enumerate(element.Values):
                #         if v == element.DefaultValue:
                #             element.TKCombo.current(i)
                #             break
                # else:
                #     element.TKCombo.current(0)
                # if element.ChangeSubmits:
                #     element.TKCombo.bind('<<ComboboxSelected>>', element.ComboboxSelectHandler)
                # if element.Readonly:
                #     element.TKCombo['state'] = 'readonly'
                # if element.Disabled is True:  # note overrides readonly if disabled
                #     element.TKCombo['state'] = 'disabled'
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element.TKCombo, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
            # # -------------------------  LISTBOX element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_LISTBOX:
                pass
            #     max_line_len = max([len(str(l)) for l in element.Values]) if len(element.Values) != 0 else 0
            #     if auto_size_text is False:
            #         width = element_size[0]
            #     else:
            #         width = max_line_len
            #     listbox_frame = tk.Frame(tk_row_frame)
            #     element.TKStringVar = tk.StringVar()
            #     element.TKListbox = tk.Listbox(listbox_frame, height=element_size[1], width=width,
            #                                    selectmode=element.SelectMode, font=font)
            #     for index, item in enumerate(element.Values):
            #         element.TKListbox.insert(tk.END, item)
            #         if element.DefaultValues is not None and item in element.DefaultValues:
            #             element.TKListbox.selection_set(index)
            #     if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
            #         element.TKListbox.configure(background=element.BackgroundColor)
            #     if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
            #         element.TKListbox.configure(fg=text_color)
            #     if element.ChangeSubmits:
            #         element.TKListbox.bind('<<ListboxSelect>>', element.ListboxSelectHandler)
            #     vsb = tk.Scrollbar(listbox_frame, orient="vertical", command=element.TKListbox.yview)
            #     element.TKListbox.configure(yscrollcommand=vsb.set)
            #     element.TKListbox.pack(side=tk.LEFT)
            #     vsb.pack(side=tk.LEFT, fill='y')
            #     listbox_frame.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
            #     if element.BindReturnKey:
            #         element.TKListbox.bind('<Return>', element.ListboxSelectHandler)
            #         element.TKListbox.bind('<Double-Button-1>', element.ListboxSelectHandler)
            #     if element.Disabled == True:
            #         element.TKListbox['state'] = 'disabled'
            #     if element.Tooltip is not None:
            #         element.TooltipObject = ToolTip(element.TKListbox, text=element.Tooltip,
            #                                         timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  INPUT MULTILINE element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_MULTILINE:
                element = element   # type: Multiline
                justify = 0
                if element.EnterSubmits:
                    justify |= wx.TE_PROCESS_ENTER
                justify |= wx.TE_MULTILINE
                element.WxTextCtrl = text_ctrl = wx.TextCtrl(toplevel_form.MasterPanel, style=justify)

                if element.DefaultText:
                    text_ctrl.SetValue(element.DefaultText)
                if font:
                    text_ctrl.SetFont(font_to_wx_font(font))
                if element.TextColor not in (None, COLOR_SYSTEM_DEFAULT):
                    text_ctrl.SetForegroundColour(element.TextColor)
                if element.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
                    text_ctrl.SetBackgroundColour(element.BackgroundColor)
                text_ctrl.SetMinSize(element_size)
                if element.Disabled:
                    text_ctrl.Enable(False)
                if element.ChangeSubmits:
                    text_ctrl.Bind(wx.EVT_KEY_UP, element._WxCallbackKeyboard)
                if element.EnterSubmits:
                    text_ctrl.Bind(wx.EVT_TEXT_ENTER, element._ReturnKeyHandler)

                sizer = pad_widget(text_ctrl)
                hsizer.Add(sizer, 0)

                if not element.Visible:
                    text_ctrl.Hide()
                if element.Tooltip:
                    text_ctrl.SetToolTip(element.Tooltip)

                if element.Focus is True or (toplevel_form.UseDefaultFocus and not focus_set):
                    focus_set = True
                    element.SetFocus()
            # ------------------------- OUTPUT MULTILINE element  ------------------------- #
            elif element_type == ELEM_TYPE_MULTILINE_OUTPUT:
                element = element                   # type: MultilineOutput
                style = 0
                if element.EnterSubmits:
                    style |= wx.TE_PROCESS_ENTER
                style |= wx.TE_MULTILINE | wx.TE_READONLY
                element.WxTextCtrl = text_ctrl = wx.TextCtrl(toplevel_form.MasterPanel, style=style)
                if element.DefaultText:
                    text_ctrl.SetValue(element.DefaultText)

                do_font_and_color(element.WxTextCtrl)
                
                if element.ChangeSubmits:
                    text_ctrl.Bind(wx.EVT_KEY_UP, element._WxCallbackKeyboard)
                if element.EnterSubmits:
                    text_ctrl.Bind(wx.EVT_TEXT_ENTER, element._ReturnKeyHandler)

                sizer = pad_widget(text_ctrl)

                hsizer.Add(sizer, 0)


                if element.Focus is True or (toplevel_form.UseDefaultFocus and not focus_set):
                    focus_set = True
                    element.SetFocus()
                # -------------------------  OUTPUT element  -----------------fd-------- #
            elif element_type == ELEM_TYPE_OUTPUT:
                element = element                   # type: Output
                style = 0
                style |= wx.TE_MULTILINE | wx.TE_READONLY
                style = wx.TE_MULTILINE | wx.TE_READONLY | wx.HSCROLL
                element.WxTextCtrl = text_ctrl = wx.TextCtrl(toplevel_form.MasterPanel, style=style)

                do_font_and_color(element.WxTextCtrl)

                sizer = pad_widget(text_ctrl)

                hsizer.Add(sizer, 0)

                element._reroute_stdout()
            # -------------------------  INPUT CHECKBOX element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_CHECKBOX:
                element = element                   # type:Checkbox
                element.WxCheckbox = widget = wx.CheckBox(toplevel_form.MasterPanel)
                if element.Text:
                    widget.SetLabel(element.Text)
                do_font_and_color(element.WxCheckbox)
                sizer = pad_widget(widget)

                if element.ChangeSubmits:
                    widget.Bind(wx.EVT_CHECKBOX, element._WxCallbackKeyboard)

                hsizer.Add(sizer, 0)

                if element.InitialState:
                    widget.SetValue(True)
                element.WxCheckbox = widget

            # # -------------------------  PROGRESS BAR element  ------------------------- #
            elif element_type == ELEM_TYPE_PROGRESS_BAR:
                element = element                   # type: ProgressBar
                style = wx.GA_HORIZONTAL if element.Orientation.startswith('h') else wx.GA_VERTICAL
                element_size = element_size[::-1] if element.Orientation.startswith('v') else element_size
                element_size = wx.Size((element_size[0], element_size[1]))
                element.WxGauge = gauge = wx.Gauge(toplevel_form.MasterPanel, wx.ID_ANY, range=element.MaxValue, style=style, size=element_size)
                if element.StartValue is not None:
                    gauge.SetValue(element.StartValue)
                do_font_and_color(element.WxGauge)
                sizer = pad_widget(gauge)
                hsizer.Add(sizer, 0)
                # -------------------------  INPUT RADIO BUTTON element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_RADIO:
                element = element                   # type: Radio
                widget = element.WxRadioButton      # type: wx.RadioButton
                do_font_and_color(element.WxRadioButton)
                sizer = pad_widget(widget)
                if element.ChangeSubmits:
                    widget.Bind(wx.EVT_RADIOBUTTON, element._WxCallbackKeyboard)
                hsizer.Add(sizer, 0)
                if element.InitialState:
                    widget.SetValue(True)

                # -------------------------  INPUT SPINNER element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SPIN:
                element = element                   # type:Spin
                ######## First make an Input widget that will be used to display the text ########
                style = wx.ALIGN_RIGHT
                if element.ReadOnly:
                    style |= wx.TE_READONLY
                element.WxTextCtrl = text_ctrl = wx.TextCtrl(toplevel_form.MasterPanel, style=style)
                do_font_and_color(element.WxTextCtrl)
                if element.ChangeSubmits:
                    text_ctrl.Bind(wx.EVT_KEY_UP, element._WxCallbackKeyboard)
                    text_ctrl.Bind(wx.EVT_TEXT_ENTER, element._ReturnKeyHandler)
                if element.DefaultValue:
                    text_ctrl.SetValue(str(element.DefaultValue))
                    element.CurrentValue = element.DefaultValue
                saved_pad = full_element_pad
                full_element_pad[3] = 0             # set right padding to 0
                hsizer.Add(pad_widget(text_ctrl), 0)

                full_element_pad = saved_pad
                ######## Now make a "Spin Button" that has the arrows ########
                # element.WxSpinCtrl = widget = wx.SpinCtrl(toplevel_form.MasterPanel, style=wx.SP_WRAP|wx.SP_ARROW_KEYS)
                element.WxSpinCtrl = widget = wx.SpinButton(toplevel_form.MasterPanel, style=wx.SP_WRAP|wx.SP_ARROW_KEYS)
                do_font_and_color(element.WxSpinCtrl)
                element.WxSpinCtrl.SetRange(0, len(element.Values)-1)
                if element.DefaultValue:
                    element.WxSpinCtrl.SetValue(element.Values.index(element.DefaultValue))
                widget.SetMinSize((25,25))

                widget.Bind(wx.EVT_SPIN, element._WxSpinCallback)
                saved_pad = full_element_pad
                full_element_pad[1] = 0             # trying to set left pad to 0 but doesn't seem to work
                hsizer.Add(pad_widget(widget), 0)
                full_element_pad = saved_pad

            # -------------------------  IMAGE element  ------------------------- #
            elif element_type == ELEM_TYPE_IMAGE:
                pass
                # if element.Filename is not None:
                #     photo = tk.PhotoImage(file=element.Filename)
                # elif element.Data is not None:
                #     photo = tk.PhotoImage(data=element.Data)
                # else:
                #     photo = None
                #     print('*ERROR laying out form.... Image Element has no image specified*')
                #
                # if photo is not None:
                #     if element_size == (
                #             None, None) or element_size == None or element_size == toplevel_form.DefaultElementSize:
                #         width, height = photo.width(), photo.height()
                #     else:
                #         width, height = element_size
                #     if photo is not None:
                #         element.tktext_label = tk.Label(tk_row_frame, image=photo, width=width, height=height,
                #                                         bd=border_depth)
                #     else:
                #         element.tktext_label = tk.Label(tk_row_frame, width=width, height=height, bd=border_depth)
                #     if element.BackgroundColor is not None:
                #         element.tktext_label.config(background=element.BackgroundColor);
                #
                #     element.tktext_label.image = photo
                #     # tktext_label.configure(anchor=tk.NW, image=photo)
                #     element.tktext_label.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                #     if element.Tooltip is not None:
                #         element.TooltipObject = ToolTip(element.tktext_label, text=element.Tooltip,
                #                                         timeout=DEFAULT_TOOLTIP_TIME)
                # -------------------------  Canvas element  ------------------------- #
            elif element_type == ELEM_TYPE_CANVAS:
                pass
                # width, height = element_size
                # if element._TKCanvas is None:
                #     element._TKCanvas = tk.Canvas(tk_row_frame, width=width, height=height, bd=border_depth)
                # else:
                #     element._TKCanvas.master = tk_row_frame
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     element._TKCanvas.configure(background=element.BackgroundColor, highlightthickness=0)
                # element._TKCanvas.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element._TKCanvas, text=element.Tooltip,
                #                                     timeout=DEFAULT_TOOLTIP_TIME)

                # -------------------------  Graph element  ------------------------- #
            elif element_type == ELEM_TYPE_GRAPH:
                pass
                # width, height = element_size
                # if element._TKCanvas is None:
                #     element._TKCanvas = tk.Canvas(tk_row_frame, width=width, height=height, bd=border_depth)
                # else:
                #     element._TKCanvas.master = tk_row_frame
                # element._TKCanvas2 = tk.Canvas(element._TKCanvas, width=width, height=height, bd=border_depth)
                # element._TKCanvas2.pack(side=tk.LEFT)
                # element._TKCanvas2.addtag_all('mytag')
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     element._TKCanvas2.configure(background=element.BackgroundColor, highlightthickness=0)
                #     element._TKCanvas.configure(background=element.BackgroundColor, highlightthickness=0)
                # element._TKCanvas.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element._TKCanvas, text=element.Tooltip,
                #                                     timeout=DEFAULT_TOOLTIP_TIME)
                # if element.ChangeSubmits:
                #     element._TKCanvas2.bind('<ButtonRelease-1>', element.ButtonReleaseCallBack)
                #     element._TKCanvas2.bind('<ButtonPress-1>', element.ButtonPressCallBack)
                # if element.DragSubmits:
                #     element._TKCanvas2.bind('<Motion>', element.MotionCallBack)
            # -------------------------  MENUBAR element  ------------------------- #
            elif element_type == ELEM_TYPE_MENUBAR:
                pass
                # menu_def = element.MenuDefinition
                # element.TKMenu = tk.Menu(toplevel_form.TKroot, tearoff=element.Tearoff)  # create the menubar
                # menubar = element.TKMenu
                # for menu_entry in menu_def:
                #     # print(f'Adding a Menubar ENTRY {menu_entry}')
                #     baritem = tk.Menu(menubar, tearoff=element.Tearoff)
                #     pos = menu_entry[0].find('&')
                #     # print(pos)
                #     if pos != -1:
                #         if pos == 0 or menu_entry[0][pos - 1] != "\\":
                #             menu_entry[0] = menu_entry[0][:pos] + menu_entry[0][pos + 1:]
                #     menubar.add_cascade(label=menu_entry[0], menu=baritem, underline=pos)
                #     if len(menu_entry) > 1:
                #         AddMenuItem(baritem, menu_entry[1], element)
                # toplevel_form.TKroot.configure(menu=element.TKMenu)
            # -------------------------  Frame element  ------------------------- #
            elif element_type == ELEM_TYPE_FRAME:
                pass
                # labeled_frame = tk.LabelFrame(tk_row_frame, text=element.Title, relief=element.Relief)
                # PackFormIntoFrame(element, labeled_frame, toplevel_form)
                # labeled_frame.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # if element.BackgroundColor != COLOR_SYSTEM_DEFAULT and element.BackgroundColor is not None:
                #     labeled_frame.configure(background=element.BackgroundColor,
                #                             highlightbackground=element.BackgroundColor,
                #                             highlightcolor=element.BackgroundColor)
                # if element.TextColor != COLOR_SYSTEM_DEFAULT and element.TextColor is not None:
                #     labeled_frame.configure(foreground=element.TextColor)
                # if font is not None:
                #     labeled_frame.configure(font=font)
                # if element.TitleLocation is not None:
                #     labeled_frame.configure(labelanchor=element.TitleLocation)
                # if element.BorderWidth is not None:
                #     labeled_frame.configure(borderwidth=element.BorderWidth)
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(labeled_frame, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  Tab element  ------------------------- #
            elif element_type == ELEM_TYPE_TAB:
                pass
                # element.TKFrame = tk.Frame(form.TKNotebook)
                # PackFormIntoFrame(element, element.TKFrame, toplevel_form)
                # if element.Disabled:
                #     form.TKNotebook.add(element.TKFrame, text=element.Title, state='disabled')
                # else:
                #     form.TKNotebook.add(element.TKFrame, text=element.Title)
                # form.TKNotebook.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # element.ParentNotebook = form.TKNotebook
                # element.TabID = form.TabCount
                # form.TabCount += 1
                # if element.BackgroundColor != COLOR_SYSTEM_DEFAULT and element.BackgroundColor is not None:
                #     element.TKFrame.configure(background=element.BackgroundColor,
                #                               highlightbackground=element.BackgroundColor,
                #                               highlightcolor=element.BackgroundColor)
                # # if element.TextColor != COLOR_SYSTEM_DEFAULT and element.TextColor is not None:
                # #     element.TKFrame.configure(foreground=element.TextColor)
                #
                # # ttk.Style().configure("TNotebook", background='red')
                # # ttk.Style().map("TNotebook.Tab", background=[("selected", 'orange')],
                # #             foreground=[("selected", 'green')])
                # # ttk.Style().configure("TNotebook.Tab", background='blue', foreground='yellow')
                #
                # if element.BorderWidth is not None:
                #     element.TKFrame.configure(borderwidth=element.BorderWidth)
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element.TKFrame, text=element.Tooltip,
                #                                     timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  TabGroup element  ------------------------- #
            elif element_type == ELEM_TYPE_TAB_GROUP:
                pass

                # custom_style = str(element.Key) + 'customtab.TNotebook'
                # style = ttk.Style(tk_row_frame)
                # if element.Theme is not None:
                #     style.theme_use(element.Theme)
                # if element.TabLocation is not None:
                #     position_dict = {'left': 'w', 'right': 'e', 'top': 'n', 'bottom': 's', 'lefttop': 'wn',
                #                      'leftbottom': 'ws', 'righttop': 'en', 'rightbottom': 'es', 'bottomleft': 'sw',
                #                      'bottomright': 'se', 'topleft': 'nw', 'topright': 'ne'}
                #     try:
                #         tab_position = position_dict[element.TabLocation]
                #     except:
                #         tab_position = position_dict['top']
                #     style.configure(custom_style, tabposition=tab_position)
                #
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     style.configure(custom_style, background=element.BackgroundColor, foreground='purple')
                #
                # # style.theme_create("yummy", parent="alt", settings={
                # #     "TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}},
                # #     "TNotebook.Tab": {
                # #         "configure": {"padding": [5, 1], "background": mygreen},
                # #         "map": {"background": [("selected", myred)],
                # #                 "expand": [("selected", [1, 1, 1, 0])]}}})
                #
                # # style.configure(custom_style+'.Tab', background='red')
                # if element.SelectedTitleColor != None:
                #     style.map(custom_style + '.Tab', foreground=[("selected", element.SelectedTitleColor)])
                # if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                #     style.configure(custom_style + '.Tab', foreground=element.TextColor)
                # # style.configure(custom_style, background='blue', foreground='yellow')
                #
                # element.TKNotebook = ttk.Notebook(tk_row_frame, style=custom_style)
                #
                # PackFormIntoFrame(element, toplevel_form.TKroot, toplevel_form)
                #
                # if element.ChangeSubmits:
                #     element.TKNotebook.bind('<<NotebookTabChanged>>', element.TabGroupSelectHandler)
                # if element.BorderWidth is not None:
                #     element.TKNotebook.configure(borderwidth=element.BorderWidth)
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element.TKNotebook, text=element.Tooltip,
                #                                     timeout=DEFAULT_TOOLTIP_TIME)
                # -------------------------  SLIDER Box element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SLIDER:
                pass
                # slider_length = element_size[0] * CharWidthInPixels()
                # slider_width = element_size[1]
                # element.TKIntVar = tk.IntVar()
                # element.TKIntVar.set(element.DefaultValue)
                # if element.Orientation[0] == 'v':
                #     range_from = element.Range[1]
                #     range_to = element.Range[0]
                #     slider_length += DEFAULT_MARGINS[1] * (element_size[0] * 2)  # add in the padding
                # else:
                #     range_from = element.Range[0]
                #     range_to = element.Range[1]
                # if element.ChangeSubmits:
                #     tkscale = tk.Scale(tk_row_frame, orient=element.Orientation, variable=element.TKIntVar,
                #                        from_=range_from, to_=range_to, resolution=element.Resolution,
                #                        length=slider_length, width=slider_width, bd=element.BorderWidth,
                #                        relief=element.Relief, font=font, tickinterval=element.TickInterval,
                #                        command=element.SliderChangedHandler)
                # else:
                #     tkscale = tk.Scale(tk_row_frame, orient=element.Orientation, variable=element.TKIntVar,
                #                        from_=range_from, to_=range_to, resolution=element.Resolution,
                #                        length=slider_length, width=slider_width, bd=element.BorderWidth,
                #                        relief=element.Relief, font=font, tickinterval=element.TickInterval)
                # tkscale.config(highlightthickness=0)
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     tkscale.configure(background=element.BackgroundColor)
                #     if DEFAULT_SCROLLBAR_COLOR != COLOR_SYSTEM_DEFAULT:
                #         tkscale.config(troughcolor=DEFAULT_SCROLLBAR_COLOR)
                # if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                #     tkscale.configure(fg=text_color)
                # tkscale.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # element.TKScale = tkscale
                # if element.Disabled == True:
                #     element.TKScale['state'] = 'disabled'
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element.TKScale, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  TABLE element  ------------------------- #
            elif element_type == ELEM_TYPE_TABLE:
                pass
                # frame = tk.Frame(tk_row_frame)
                #
                # height = element.NumRows
                # if element.Justification == 'left':
                #     anchor = tk.W
                # elif element.Justification == 'right':
                #     anchor = tk.E
                # else:
                #     anchor = tk.CENTER
                # column_widths = {}
                # for row in element.Values:
                #     for i, col in enumerate(row):
                #         col_width = min(len(str(col)), element.MaxColumnWidth)
                #         try:
                #             if col_width > column_widths[i]:
                #                 column_widths[i] = col_width
                #         except:
                #             column_widths[i] = col_width
                # if element.ColumnsToDisplay is None:
                #     displaycolumns = element.ColumnHeadings
                # else:
                #     displaycolumns = []
                #     for i, should_display in enumerate(element.ColumnsToDisplay):
                #         if should_display:
                #             displaycolumns.append(element.ColumnHeadings[i])
                # column_headings = element.ColumnHeadings
                # if element.DisplayRowNumbers:  # if display row number, tack on the numbers to front of columns
                #     displaycolumns = [element.RowHeaderText, ] + displaycolumns
                #     column_headings = [element.RowHeaderText, ] + element.ColumnHeadings
                # element.TKTreeview = ttk.Treeview(frame, columns=column_headings,
                #                                   displaycolumns=displaycolumns, show='headings', height=height,
                #                                   selectmode=element.SelectMode)
                # treeview = element.TKTreeview
                # if element.DisplayRowNumbers:
                #     treeview.heading(element.RowHeaderText, text=element.RowHeaderText)  # make a dummy heading
                #     treeview.column(element.RowHeaderText, width=50, anchor=anchor)
                # for i, heading in enumerate(element.ColumnHeadings):
                #     treeview.heading(heading, text=heading)
                #     if element.AutoSizeColumns:
                #         width = max(column_widths[i], len(heading))
                #     else:
                #         try:
                #             width = element.ColumnWidths[i]
                #         except:
                #             width = element.DefaultColumnWidth
                #
                #     treeview.column(heading, width=width * CharWidthInPixels(), anchor=anchor)
                # # Insert values into the tree
                # for i, value in enumerate(element.Values):
                #     if element.DisplayRowNumbers:
                #         value = [i + element.StartingRowNumber] + value
                #     id = treeview.insert('', 'end', text=value, iid=i + 1, values=value, tag=i % 2)
                # if element.AlternatingRowColor is not None:
                #     treeview.tag_configure(1, background=element.AlternatingRowColor)
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     ttk.Style().configure("Treeview", background=element.BackgroundColor,
                #                           fieldbackground=element.BackgroundColor)
                # if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                #     ttk.Style().configure("Treeview", foreground=element.TextColor)
                # # scrollable_frame.pack(side=tk.LEFT,  padx=element.Pad[0], pady=element.Pad[1], expand=True, fill='both')
                # treeview.bind("<<TreeviewSelect>>", element.treeview_selected)
                # if element.BindReturnKey:
                #     treeview.bind('<Return>', element.treeview_double_click)
                #     treeview.bind('<Double-Button-1>', element.treeview_double_click)
                # scrollbar = tk.Scrollbar(frame)
                # scrollbar.pack(side=tk.RIGHT, fill='y')
                # scrollbar.config(command=treeview.yview)
                # treeview.configure(yscrollcommand=scrollbar.set)
                #
                # element.TKTreeview.pack(side=tk.LEFT, expand=True, padx=0, pady=0, fill='both')
                # frame.pack(side=tk.LEFT, expand=True, padx=0, pady=0)
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element.TKTreeview, text=element.Tooltip,
                #                                     timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  Tree element  ------------------------- #
            elif element_type == ELEM_TYPE_TREE:
                pass
                # frame = tk.Frame(tk_row_frame)
                #
                # height = element.NumRows
                # if element.Justification == 'left':  # justification
                #     anchor = tk.W
                # elif element.Justification == 'right':
                #     anchor = tk.E
                # else:
                #     anchor = tk.CENTER
                #
                # if element.ColumnsToDisplay is None:  # Which cols to display
                #     displaycolumns = element.ColumnHeadings
                # else:
                #     displaycolumns = []
                #     for i, should_display in enumerate(element.ColumnsToDisplay):
                #         if should_display:
                #             displaycolumns.append(element.ColumnHeadings[i])
                # column_headings = element.ColumnHeadings
                # # ------------- GET THE TREEVIEW WIDGET -------------
                # element.TKTreeview = ttk.Treeview(frame, columns=column_headings,
                #                                   displaycolumns=displaycolumns, show='tree headings', height=height,
                #                                   selectmode=element.SelectMode, )
                # treeview = element.TKTreeview
                # for i, heading in enumerate(element.ColumnHeadings):  # Configure cols + headings
                #     treeview.heading(heading, text=heading)
                #     if element.AutoSizeColumns:
                #         width = min(element.MaxColumnWidth, len(heading) + 1)
                #     else:
                #         try:
                #             width = element.ColumnWidths[i]
                #         except:
                #             width = element.DefaultColumnWidth
                #     treeview.column(heading, width=width * CharWidthInPixels(), anchor=anchor)
                #
                # def add_treeview_data(node):
                #     # print(f'Inserting {node.key} under parent {node.parent}')
                #     if node.key != '':
                #         treeview.insert(node.parent, 'end', node.key, text=node.text, values=node.values,
                #                         open=element.ShowExpanded)
                #     for node in node.children:
                #         add_treeview_data(node)
                #
                # add_treeview_data(element.TreeData.root_node)
                # treeview.column('#0', width=element.Col0Width * CharWidthInPixels(), anchor=anchor)
                # # ----- configure colors -----
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     ttk.Style().configure("Treeview", background=element.BackgroundColor,
                #                           fieldbackground=element.BackgroundColor)
                # if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                #     ttk.Style().configure("Treeview", foreground=element.TextColor)
                #
                # scrollbar = tk.Scrollbar(frame)
                # scrollbar.pack(side=tk.RIGHT, fill='y')
                # scrollbar.config(command=treeview.yview)
                # treeview.configure(yscrollcommand=scrollbar.set)
                # element.TKTreeview.pack(side=tk.LEFT, expand=True, padx=0, pady=0, fill='both')
                # frame.pack(side=tk.LEFT, expand=True, padx=0, pady=0)
                # treeview.bind("<<TreeviewSelect>>", element.treeview_selected)
                # if element.Tooltip is not None:  # tooltip
                #     element.TooltipObject = ToolTip(element.TKTreeview, text=element.Tooltip,
                #                                     timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  Separator element  ------------------------- #
            elif element_type == ELEM_TYPE_SEPARATOR:
                element = element       # type: VerticalSeparator
                if element.Orientation.lower().startswith('v'):
                    element.WxStaticLine = static_line = wx.StaticLine(toplevel_form.MasterPanel, style=wx.LI_VERTICAL)
                else:
                    element.WxStaticLine = static_line = wx.StaticLine(toplevel_form.MasterPanel, style=wx.LI_HORIZONTAL)

                do_font_and_color(element.WxStaticLine)

                sizer = pad_widget(static_line)

                hsizer.Add(sizer, 0)
        #         separator = ttk.Separator(tk_row_frame, orient=element.Orientation, )
        #         separator.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1], fill='both', expand=True)
        #
        # # ............................DONE WITH ROW pack the row of widgets ..........................#
        # done with row, pack the row of widgets
        containing_frame.Add(hsizer,0, wx.TOP|wx.BOTTOM, border=0)
        # tk_row_frame.grid(row=row_num+2, sticky=tk.NW, padx=DEFAULT_MARGINS[0])
        # tk_row_frame.pack(side=tk.TOP, anchor='nw', padx=DEFAULT_MARGINS[0], expand=False)
        # if form.BackgroundColor is not None and form.BackgroundColor != COLOR_SYSTEM_DEFAULT:
        #     tk_row_frame.configure(background=form.BackgroundColor)
        # toplevel_form.TKroot.configure(padx=DEFAULT_MARGINS[0], pady=DEFAULT_MARGINS[1])
    return


# ----====----====----====----====----==== STARTUP TK ====----====----====----====----====----#
def StartupTK(window:Window):

    ow = Window.NumOpenWindows
    if Window.highest_level_app is None:
        app = Window.highest_level_app = wx.App(False)
    else:
        app = Window.highest_level_app
    Window.IncrementOpenCount()

    # -------- grab anywhere --------
    if window.GrabAnywhere:
        frame = DragFrame(title=window.Title)
    else:
        frame = wx.Frame(None, title=window.Title)

    panel = wx.Panel(frame, -1,  style=wx.TRANSPARENT_WINDOW)
    # panel.SetTransparent(.5)
    if window.GrabAnywhere:
        panel.Bind(wx.EVT_MOTION, frame.on_mouse)

    window.App = app
    window.MasterFrame =  frame
    window.MasterPanel = panel
    window.MasterFrame.panel = panel
    frame.Bind(wx.EVT_CLOSE, window.OnClose)

    # ----------------------------- Icon -----------------------------
    if window.WindowIcon:
        if type(window.WindowIcon) is bytes:
            icon = PyEmbeddedImage(window.WindowIcon).GetIcon()
        else:
            if os.path.exists(window.WindowIcon):
                icon = wx.Icon(window.WindowIcon, wx.BITMAP_TYPE_ANY)
            else:
                icon = PyEmbeddedImage(DEFAULT_BASE64_ICON).GetIcon()
        if icon:
            frame.SetIcon(icon)

    # ----------------------------- Background -----------------------------
    if window.BackgroundColor is not None and window.BackgroundColor != COLOR_SYSTEM_DEFAULT:
        panel.SetBackgroundColour(window.BackgroundColor)

    if window.BackgroundImage:
        if type(window.BackgroundImage) is bytes:
            pic = PyEmbeddedImage(window.BackgroundImage).GetBitmap()
        else:
            if os.path.exists(window.BackgroundImage):
                pic = wx.Image(window.BackgroundImage, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            else:
                pic = PyEmbeddedImage(DEFAULT_BASE64_ICON).GetBitmap()
        window.bitmap1 = wx.StaticBitmap(window.MasterPanel, -1, pic, (0, 0))



    InitializeResults(window)

    # -----------------------------  -----------------------------
    # -----------------------------  -----------------------------
    # ----------------------------- handle settings using Style Flags -----------------------------
    style = 0
    if window.NoTitleBar:
        style |= wx.BORDER_NONE
    else:
        style |= wx.BORDER_DEFAULT
    if window.KeepOnTop:
        style |= wx.STAY_ON_TOP
    if style:
        window.MasterFrame.SetWindowStyleFlag(style)

    if window.ReturnKeyboardEvents:
        # style |= wx.WANTS_CHARS
        window.App.Bind(wx.EVT_CHAR_HOOK, window.callback_keyboard_char)
        window.App.Bind(wx.EVT_MOUSEWHEEL, window.callback_keyboard_char)

    # ----------------------------- Sizer creation and PACK FORM -----------------------------
    vsizer = wx.BoxSizer(wx.VERTICAL)

    preprocess_radio_elements(window, window)

    # ----------------------------- Do the packing of the elements -----------------------------

    PackFormIntoFrame(window, vsizer, window)

    # ----------------------------- Sizers to create margins -----------------------------
    outersizer = wx.BoxSizer(wx.VERTICAL)
    outersizer.Fit(window.MasterFrame)
    outersizer.Add(vsizer, 1, wx.TOP|wx.BOTTOM|wx.EXPAND, border=DEFAULT_MARGINS[1])

    window.OuterSizer = wx.BoxSizer(wx.VERTICAL)
    window.OuterSizer.Fit(window.MasterFrame)
    window.OuterSizer.Add(outersizer, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, border=DEFAULT_MARGINS[0])

    window.MasterPanel.SetSizer(window.OuterSizer)

    window.OuterSizer.Fit(window.MasterFrame)

    # ----------------------------- window location, size and alpha -----------------------------
    if window.Location != (None, None):
        window.MasterFrame.Move(window.Location[0], window.Location[1])
    else:
        window.MasterFrame.Center(wx.BOTH)

    if window._Size != (None, None):
        window.MasterFrame.SetSize(window._Size[0], window._Size[1])

    if window._AlphaChannel is not None:
        window.SetAlpha(window._AlphaChannel)

    # ----------------------------- DISPLAY the window -----------------------------
    window.MasterFrame.Show()

    # ....................................... DONE creating and laying out window ..........................#
    if RUN_INSPECTION_TOOL:
        wx.lib.inspection.InspectionTool().Show()
    window.CurrentlyRunningMainloop = True

    if window.Timeout:
        timer = wx.Timer(window.App)
        window.App.Bind(wx.EVT_TIMER, window.timer_timeout)
        timer.Start(milliseconds=window.Timeout, oneShot=wx.TIMER_ONE_SHOT)
    else:
        timer = None

    if window.AutoClose:
        window.timer = wx.Timer(window.App, id=Window.NumOpenWindows)
        window.App.Bind(wx.EVT_TIMER, lambda frame: window.autoclose_timer_callback(window.MasterFrame), id=Window.NumOpenWindows)
        window.timer.Start(milliseconds=window.AutoCloseDuration*1000, oneShot=wx.TIMER_ONE_SHOT)
    # ------------------------------------ MAINLOOP ------------------------------------
    if not window.NonBlocking:
        window.App.MainLoop()
    else:
        window.non_block_timer = wx.Timer(window.App, id=5678)
        window.App.Bind(wx.EVT_TIMER, window.non_block_timer_timeout, id=5678)
        window.non_block_timer.Start(milliseconds=0, oneShot=wx.TIMER_ONE_SHOT)
        window.App.MainLoop()

    if Window.stdout_is_rerouted:
        sys.stdout = Window.stdout_location
    window.CurrentlyRunningMainloop = False
    if timer:
        timer.Stop()

        # if not window.FormRemainedOpen:
        #     _my_windows.Decrement()
        # if window.RootNeedsDestroying:
        #     window.TKroot.destroy()
        #     window.RootNeedsDestroying = False
    return


# ==============================_GetNumLinesNeeded ==#
# Helper function for determining how to wrap text   #
# ===================================================#
def _GetNumLinesNeeded(text, max_line_width):
    if max_line_width == 0:
        return 1
    lines = text.split('\n')
    num_lines = len(lines)  # number of original lines of text
    max_line_len = max([len(l) for l in lines])  # longest line
    lines_used = []
    for L in lines:
        lines_used.append(len(L) // max_line_width + (len(L) % max_line_width > 0))  # fancy math to round up
    total_lines_needed = sum(lines_used)
    return total_lines_needed


# ==============================  PROGRESS METER ========================================== #

def ConvertArgsToSingleString(*args):
    max_line_total, width_used, total_lines, = 0, 0, 0
    single_line_message = ''
    # loop through args and built a SINGLE string from them
    for message in args:
        # fancy code to check if string and convert if not is not need. Just always convert to string :-)
        # if not isinstance(message, str): message = str(message)
        message = str(message)
        longest_line_len = max([len(l) for l in message.split('\n')])
        width_used = max(longest_line_len, width_used)
        max_line_total = max(max_line_total, width_used)
        lines_needed = _GetNumLinesNeeded(message, width_used)
        total_lines += lines_needed
        single_line_message += message + '\n'
    return single_line_message, width_used, total_lines


METER_REASON_CANCELLED = 'cancelled'
METER_REASON_CLOSED = 'closed'
METER_REASON_REACHED_MAX = 'finished'
METER_OK = True
METER_STOPPED = False

class QuickMeter(object):
    active_meters = {}
    exit_reasons = {}

    def __init__(self, title, current_value, max_value, key, *args, orientation='v', bar_color=(None, None),
                         button_color=(None, None), size=DEFAULT_PROGRESS_BAR_SIZE, border_width=None, grab_anywhere=False):
        self.start_time = datetime.datetime.utcnow()
        self.key = key
        self.orientation = orientation
        self.bar_color = bar_color
        self.size = size
        self.grab_anywhere = grab_anywhere
        self.button_color = button_color
        self.border_width = border_width
        self.title = title
        self.current_value = current_value
        self.max_value = max_value
        self.close_reason = None
        self.window = self.BuildWindow(*args)

    def BuildWindow(self, *args):
        layout = []
        if self.orientation.lower().startswith('h'):
            col = []
            col += [[T(''.join(map(lambda x: str(x)+'\n',args)),key='_OPTMSG_')]] ### convert all *args into one string that can be updated
            col += [[T('', size=(25,8), key='_STATS_')],
                    [ProgressBar(max_value=self.max_value, orientation='h', key='_PROG_', size=self.size)],
                    [Cancel(button_color=self.button_color), Stretch()]]
            layout = [Column(col)]
        else:
            col = [[ProgressBar(max_value=self.max_value, orientation='v', key='_PROG_', size=self.size)]]
            col2 = []
            col2 += [[T(''.join(map(lambda x: str(x)+'\n',args)),key='_OPTMSG_')]] ### convert all *args into one string that can be updated
            col2 += [[T('', size=(25,8), key='_STATS_')],
                     [Cancel(button_color=self.button_color), Stretch()]]
            layout = [Column(col), Column(col2)]
        self.window = Window(self.title, grab_anywhere=self.grab_anywhere, border_depth=self.border_width)
        self.window.Layout([layout]).Finalize()

        return self.window

    def UpdateMeter(self, current_value, max_value, *args):
        self.current_value = current_value
        self.max_value = max_value
        self.window.Element('_PROG_').UpdateBar(self.current_value, self.max_value)
        self.window.Element('_STATS_').Update('\n'.join(self.ComputeProgressStats()))
        self.window.Element('_OPTMSG_').Update(value=''.join(map(lambda x: str(x)+'\n',args))) ###  update the string with the args
        event, values = self.window.Read(timeout=0)
        if event in('Cancel', None) or current_value >= max_value:
            self.window.Close()
            del(QuickMeter.active_meters[self.key])
            QuickMeter.exit_reasons[self.key] = METER_REASON_CANCELLED if event == 'Cancel' else METER_REASON_CLOSED if event is None else METER_REASON_REACHED_MAX
            return QuickMeter.exit_reasons[self.key]
        return METER_OK


    def ComputeProgressStats(self):
        utc = datetime.datetime.utcnow()
        time_delta = utc - self.start_time
        total_seconds = time_delta.total_seconds()
        if not total_seconds:
            total_seconds = 1
        try:
            time_per_item = total_seconds / self.current_value
        except:
            time_per_item = 1
        seconds_remaining = (self.max_value - self.current_value) * time_per_item
        time_remaining = str(datetime.timedelta(seconds=seconds_remaining))
        time_remaining_short = (time_remaining).split(".")[0]
        time_delta_short = str(time_delta).split(".")[0]
        total_time = time_delta + datetime.timedelta(seconds=seconds_remaining)
        total_time_short = str(total_time).split(".")[0]
        self.stat_messages = [
            '{} of {}'.format(self.current_value, self.max_value),
            '{} %'.format(100 * self.current_value // self.max_value),
            '',
            ' {:6.2f} Iterations per Second'.format(self.current_value / total_seconds),
            ' {:6.2f} Seconds per Iteration'.format(total_seconds / (self.current_value if self.current_value else 1)),
            '',
            '{} Elapsed Time'.format(time_delta_short),
            '{} Time Remaining'.format(time_remaining_short),
            '{} Estimated Total Time'.format(total_time_short)]
        return self.stat_messages


def OneLineProgressMeter(title, current_value, max_value, key, *args, orientation='v', bar_color=(None, None),
                         button_color=None, size=DEFAULT_PROGRESS_BAR_SIZE, border_width=None, grab_anywhere=False):
    if key not in QuickMeter.active_meters:
        meter = QuickMeter(title, current_value, max_value, key, *args, orientation=orientation, bar_color=bar_color,
                           button_color=button_color, size=size, border_width=border_width, grab_anywhere=grab_anywhere)
        QuickMeter.active_meters[key] = meter
    else:
        meter = QuickMeter.active_meters[key]

    rc = meter.UpdateMeter(current_value, max_value, *args)
    OneLineProgressMeter.exit_reasons = getattr(OneLineProgressMeter,'exit_reasons', QuickMeter.exit_reasons)
    return rc == METER_OK

def OneLineProgressMeterCancel(key):
    try:
        meter = QuickMeter.active_meters[key]
        meter.window.Close()
        del(QuickMeter.active_meters[key])
        QuickMeter.exit_reasons[key] = METER_REASON_CANCELLED
    except:  # meter is already deleted
        return



# input is #RRGGBB
# output is #RRGGBB
def GetComplimentaryHex(color):
    # strip the # from the beginning
    color = color[1:]
    # convert the string into hex
    color = int(color, 16)
    # invert the three bytes
    # as good as substracting each of RGB component by 255(FF)
    comp_color = 0xFFFFFF ^ color
    # convert the color back to hex by prefixing a #
    comp_color = "#%06X" % comp_color
    return comp_color


# ========================  EasyPrint           =====#
# ===================================================#

class DebugWin():
    debug_window = None

    def __init__(self, size=(None, None), location=(None, None), font=None, no_titlebar=False, no_button=False,
                 grab_anywhere=False, keep_on_top=False, title=None, do_not_reroute_stdout=False):
        # Show a form that's a running counter
        self.size = size
        self.location = location
        self.font = font
        self.no_titlebar = no_titlebar
        self.no_button = no_button
        self.grab_anywhere = grab_anywhere
        self.keep_on_top = keep_on_top
        self.do_not_reroute_stdout = do_not_reroute_stdout

        win_size = size if size != (None, None) else DEFAULT_DEBUG_WINDOW_SIZE
        self.window = Window(title=title or 'Debug Window', no_titlebar=no_titlebar, auto_size_text=True, location=location,
                             font=font or ('Courier New', 10), grab_anywhere=grab_anywhere, keep_on_top=keep_on_top)
        self.output_element = MultilineOutput(size=win_size,  key='_MULTILINE_') if do_not_reroute_stdout else Output(size=win_size)

        if no_button:
            self.layout = [[self.output_element]]
        else:
            self.layout = [
                [self.output_element],
                [DummyButton('Quit'), Stretch()]
            ]
        self.window.AddRows(self.layout)
        self.window.Read(timeout=0)  # Show a non-blocking form, returns immediately
        Window.active_popups[self.window] = 'debug window'
        return

    def Print(self, *args, end=None, sep=None):
        sepchar = sep if sep is not None else ' '
        endchar = end if end is not None else '\n'

        if self.window is None:  # if window was destroyed already, just print
            self.__init__(size=self.size, location=self.location, font=self.font, no_titlebar=self.no_titlebar, no_button=self.no_button, grab_anywhere=self.grab_anywhere, keep_on_top=self.keep_on_top, do_not_reroute_stdout=self.do_not_reroute_stdout)
        event, values = self.window.Read(timeout=0)
        if event == 'Quit' or event is None:
            self.Close()
            self.__init__(size=self.size, location=self.location, font=self.font, no_titlebar=self.no_titlebar, no_button=self.no_button, grab_anywhere=self.grab_anywhere, keep_on_top=self.keep_on_top, do_not_reroute_stdout=self.do_not_reroute_stdout)
        if self.do_not_reroute_stdout:
            outstring = ''
            for arg in args:
                outstring += str(arg) + sepchar
            outstring += endchar
            self.output_element.Update(outstring, append=True)
        else:
            print(*args, sep=sepchar, end=endchar)


    def Close(self):
        self.window.Close()
        self.window = None


def PrintClose():
    EasyPrintClose()


def EasyPrint(*args, size=(None, None), end=None, sep=None, location=(None, None), font=None, no_titlebar=False,
              no_button=False, grab_anywhere=False, keep_on_top=False, do_not_reroute_stdout=True):


    if DebugWin.debug_window is None:
        DebugWin.debug_window = DebugWin(size=size, location=location, font=font, no_titlebar=no_titlebar,
                                    no_button=no_button, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, do_not_reroute_stdout=do_not_reroute_stdout)
    DebugWin.debug_window.Print(*args, end=end, sep=sep)


Print = EasyPrint
eprint = EasyPrint


def EasyPrintClose():
    if DebugWin.debug_window is not None:
        DebugWin.debug_window.Close()
        DebugWin.debug_window = None


# ========================  Scrolled Text Box   =====#
# ===================================================#
def PopupScrolled(*args, button_color=None, yes_no=False, auto_close=False, auto_close_duration=None,
                  size=(None, None)):
    if not args: return
    width, height = size
    width = width if width else MESSAGE_BOX_LINE_WIDTH
    form = Window(args[0], auto_size_text=True, button_color=button_color, auto_close=auto_close,
                  auto_close_duration=auto_close_duration)
    max_line_total, max_line_width, total_lines, height_computed = 0, 0, 0, 0
    complete_output = ''
    for message in args:
        # fancy code to check if string and convert if not is not need. Just always convert to string :-)
        # if not isinstance(message, str): message = str(message)
        message = str(message)
        longest_line_len = max([len(l) for l in message.split('\n')])
        width_used = min(longest_line_len, width)
        max_line_total = max(max_line_total, width_used)
        max_line_width = width
        lines_needed = _GetNumLinesNeeded(message, width_used)
        height_computed += lines_needed
        complete_output += message + '\n'
        total_lines += lines_needed
    height_computed = MAX_SCROLLED_TEXT_BOX_HEIGHT if height_computed > MAX_SCROLLED_TEXT_BOX_HEIGHT else height_computed
    if height:
        height_computed = height
    form.AddRow(Multiline(complete_output, size=(max_line_width, height_computed)))
    pad = max_line_total - 15 if max_line_total > 15 else 1
    # show either an OK or Yes/No depending on paramater
    if yes_no:
        form.AddRow(Text('', size=(pad, 1), auto_size_text=False), Yes(), No())
        button, values = form.Read()
        return button
    else:
        form.AddRow(Text('', size=(pad, 1), auto_size_text=False), Button('OK', size=(5, 1), button_color=button_color))
    button, values = form.Read()
    return button


ScrolledTextBox = PopupScrolled


# ============================== SetGlobalIcon ======#
# Sets the icon to be used by default                #
# ===================================================#
def SetGlobalIcon(icon):
    if icon is not None:
        Window.user_defined_icon = icon
    return True


# ============================== SetOptions =========#
# Sets the icon to be used by default                #
# ===================================================#
def SetOptions(icon=None, button_color=None, element_size=(None, None), button_element_size=(None, None),
               margins=(None, None),
               element_padding=(None, None), auto_size_text=None, auto_size_buttons=None, font=None, border_width=None,
               slider_border_width=None, slider_relief=None, slider_orientation=None,
               autoclose_time=None, message_box_line_width=None,
               progress_meter_border_depth=None, progress_meter_style=None,
               progress_meter_relief=None, progress_meter_color=None, progress_meter_size=None,
               text_justification=None, background_color=None, element_background_color=None,
               text_element_background_color=None, input_elements_background_color=None, input_text_color=None,
               scrollbar_color=None, text_color=None, element_text_color=None, debug_win_size=(None, None),
               window_location=(None, None),
               tooltip_time=None):
    global DEFAULT_ELEMENT_SIZE
    global DEFAULT_BUTTON_ELEMENT_SIZE
    global DEFAULT_MARGINS  # Margins for each LEFT/RIGHT margin is first term
    global DEFAULT_ELEMENT_PADDING  # Padding between elements (row, col) in pixels
    global DEFAULT_AUTOSIZE_TEXT
    global DEFAULT_AUTOSIZE_BUTTONS
    global DEFAULT_FONT
    global DEFAULT_BORDER_WIDTH
    global DEFAULT_AUTOCLOSE_TIME
    global DEFAULT_BUTTON_COLOR
    global MESSAGE_BOX_LINE_WIDTH
    global DEFAULT_PROGRESS_BAR_BORDER_WIDTH
    global DEFAULT_PROGRESS_BAR_STYLE
    global DEFAULT_PROGRESS_BAR_RELIEF
    global DEFAULT_PROGRESS_BAR_COLOR
    global DEFAULT_PROGRESS_BAR_SIZE
    global DEFAULT_TEXT_JUSTIFICATION
    global DEFAULT_DEBUG_WINDOW_SIZE
    global DEFAULT_SLIDER_BORDER_WIDTH
    global DEFAULT_SLIDER_RELIEF
    global DEFAULT_SLIDER_ORIENTATION
    global DEFAULT_BACKGROUND_COLOR
    global DEFAULT_INPUT_ELEMENTS_COLOR
    global DEFAULT_ELEMENT_BACKGROUND_COLOR
    global DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR
    global DEFAULT_SCROLLBAR_COLOR
    global DEFAULT_TEXT_COLOR
    global DEFAULT_WINDOW_LOCATION
    global DEFAULT_ELEMENT_TEXT_COLOR
    global DEFAULT_INPUT_TEXT_COLOR
    global DEFAULT_TOOLTIP_TIME

    if icon is not None:
        Window.user_defined_icon = icon

    if button_color != None:
        DEFAULT_BUTTON_COLOR = button_color

    if element_size != (None, None):
        DEFAULT_ELEMENT_SIZE = element_size

    if button_element_size != (None, None):
        DEFAULT_BUTTON_ELEMENT_SIZE = button_element_size

    if margins != (None, None):
        DEFAULT_MARGINS = margins

    if element_padding != (None, None):
        DEFAULT_ELEMENT_PADDING = element_padding

    if auto_size_text != None:
        DEFAULT_AUTOSIZE_TEXT = auto_size_text

    if auto_size_buttons != None:
        DEFAULT_AUTOSIZE_BUTTONS = auto_size_buttons

    if font != None:
        DEFAULT_FONT = font

    if border_width != None:
        DEFAULT_BORDER_WIDTH = border_width

    if autoclose_time != None:
        DEFAULT_AUTOCLOSE_TIME = autoclose_time

    if message_box_line_width != None:
        MESSAGE_BOX_LINE_WIDTH = message_box_line_width

    if progress_meter_border_depth != None:
        DEFAULT_PROGRESS_BAR_BORDER_WIDTH = progress_meter_border_depth

    if progress_meter_style != None:
        DEFAULT_PROGRESS_BAR_STYLE = progress_meter_style

    if progress_meter_relief != None:
        DEFAULT_PROGRESS_BAR_RELIEF = progress_meter_relief

    if progress_meter_color != None:
        DEFAULT_PROGRESS_BAR_COLOR = progress_meter_color

    if progress_meter_size != None:
        DEFAULT_PROGRESS_BAR_SIZE = progress_meter_size

    if slider_border_width != None:
        DEFAULT_SLIDER_BORDER_WIDTH = slider_border_width

    if slider_orientation != None:
        DEFAULT_SLIDER_ORIENTATION = slider_orientation

    if slider_relief != None:
        DEFAULT_SLIDER_RELIEF = slider_relief

    if text_justification != None:
        DEFAULT_TEXT_JUSTIFICATION = text_justification

    if background_color != None:
        DEFAULT_BACKGROUND_COLOR = background_color

    if text_element_background_color != None:
        DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR = text_element_background_color

    if input_elements_background_color != None:
        DEFAULT_INPUT_ELEMENTS_COLOR = input_elements_background_color

    if element_background_color != None:
        DEFAULT_ELEMENT_BACKGROUND_COLOR = element_background_color

    if window_location != (None, None):
        DEFAULT_WINDOW_LOCATION = window_location

    if debug_win_size != (None, None):
        DEFAULT_DEBUG_WINDOW_SIZE = debug_win_size

    if text_color != None:
        DEFAULT_TEXT_COLOR = text_color

    if scrollbar_color != None:
        DEFAULT_SCROLLBAR_COLOR = scrollbar_color

    if element_text_color != None:
        DEFAULT_ELEMENT_TEXT_COLOR = element_text_color

    if input_text_color is not None:
        DEFAULT_INPUT_TEXT_COLOR = input_text_color

    if tooltip_time is not None:
        DEFAULT_TOOLTIP_TIME = tooltip_time

    return True


#################### ChangeLookAndFeel #######################
# Predefined settings that will change the colors and styles #
# of the elements.                                           #
##############################################################
LOOK_AND_FEEL_TABLE = { 'SystemDefault':
     {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
      'TEXT': COLOR_SYSTEM_DEFAULT,
      'INPUT': COLOR_SYSTEM_DEFAULT,
      'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
      'SCROLL': COLOR_SYSTEM_DEFAULT,
      'BUTTON': OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR,
      'PROGRESS': COLOR_SYSTEM_DEFAULT,
      'BORDER': 1, 'SLIDER_DEPTH': 1,
      'PROGRESS_DEPTH': 0},

 'SystemDefaultForReal':
     {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
      'TEXT': COLOR_SYSTEM_DEFAULT,
      'INPUT': COLOR_SYSTEM_DEFAULT,
      'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
      'SCROLL': COLOR_SYSTEM_DEFAULT,
      'BUTTON': COLOR_SYSTEM_DEFAULT,
      'PROGRESS': COLOR_SYSTEM_DEFAULT,
      'BORDER': 1, 'SLIDER_DEPTH': 1,
      'PROGRESS_DEPTH': 0},

 'Material1': {'BACKGROUND': '#E3F2FD',
               'TEXT': '#000000',
               'INPUT': '#86A8FF',
               'TEXT_INPUT': '#000000',
               'SCROLL': '#86A8FF',
               'BUTTON': ('#FFFFFF', '#5079D3'),
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 0, 'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0,
               'ACCENT1': '#FF0266',
               'ACCENT2': '#FF5C93',
               'ACCENT3': '#C5003C'},

 'Material2': {'BACKGROUND': '#FAFAFA',
               'TEXT': '#000000',
               'INPUT': '#004EA1',
               'TEXT_INPUT': '#FFFFFF',
               'SCROLL': '#5EA7FF',
               'BUTTON': ('#FFFFFF', '#0079D3'),  # based on Reddit color
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 0, 'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0,
               'ACCENT1': '#FF0266',
               'ACCENT2': '#FF5C93',
               'ACCENT3': '#C5003C'},

 'Reddit': {'BACKGROUND': '#ffffff',
            'TEXT': '#1a1a1b',
            'INPUT': '#dae0e6',
            'TEXT_INPUT': '#222222',
            'SCROLL': '#a5a4a4',
            'BUTTON': ('white', '#0079d3'),
            'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
            'BORDER': 1,
            'SLIDER_DEPTH': 0,
            'PROGRESS_DEPTH': 0,
            'ACCENT1': '#ff5414',
            'ACCENT2': '#33a8ff',
            'ACCENT3': '#dbf0ff'},

 'Topanga': {'BACKGROUND': '#282923',
             'TEXT': '#E7DB74',
             'INPUT': '#393a32',
             'TEXT_INPUT': '#E7C855',
             'SCROLL': '#E7C855',
             'BUTTON': ('#E7C855', '#284B5A'),
             'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
             'BORDER': 1,
             'SLIDER_DEPTH': 0,
             'PROGRESS_DEPTH': 0,
             'ACCENT1': '#c15226',
             'ACCENT2': '#7a4d5f',
             'ACCENT3': '#889743'},

 'GreenTan': {'BACKGROUND': '#9FB8AD',
              'TEXT': COLOR_SYSTEM_DEFAULT,
              'INPUT': '#F7F3EC', 'TEXT_INPUT': 'black',
              'SCROLL': '#F7F3EC',
              'BUTTON': ('white', '#475841'),
              'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
              'BORDER': 1, 'SLIDER_DEPTH': 0,
              'PROGRESS_DEPTH': 0},

 'Dark': {'BACKGROUND': '#404040',
          'TEXT': 'white',
          'INPUT': '#4D4D4D',
          'TEXT_INPUT': 'white',
          'SCROLL': '#707070',
          'BUTTON': ('white', '#004F00'),
          'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
          'BORDER': 1,
          'SLIDER_DEPTH': 0,
          'PROGRESS_DEPTH': 0},

 'LightGreen': {'BACKGROUND': '#B7CECE',
                'TEXT': 'black',
                'INPUT': '#FDFFF7',
                'TEXT_INPUT': 'black',
                'SCROLL': '#FDFFF7',
                'BUTTON': ('white', '#658268'),
                'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'ACCENT1': '#76506d',
                'ACCENT2': '#5148f1',
                'ACCENT3': '#0a1c84',
                'PROGRESS_DEPTH': 0},

 'Dark2': {'BACKGROUND': '#404040',
           'TEXT': 'white',
           'INPUT': 'white',
           'TEXT_INPUT': 'black',
           'SCROLL': '#707070',
           'BUTTON': ('white', '#004F00'),
           'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
           'BORDER': 1,
           'SLIDER_DEPTH': 0,
           'PROGRESS_DEPTH': 0},

 'Black': {'BACKGROUND': 'black',
           'TEXT': 'white',
           'INPUT': '#4D4D4D',
           'TEXT_INPUT': 'white',
           'SCROLL': '#707070',
           'BUTTON': ('black', 'white'),
           'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
           'BORDER': 1,
           'SLIDER_DEPTH': 0,
           'PROGRESS_DEPTH': 0},

 'Tan': {'BACKGROUND': '#fdf6e3',
         'TEXT': '#268bd1',
         'INPUT': '#eee8d5',
         'TEXT_INPUT': '#6c71c3',
         'SCROLL': '#eee8d5',
         'BUTTON': ('white', '#063542'),
         'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
         'BORDER': 1,
         'SLIDER_DEPTH': 0,
         'PROGRESS_DEPTH': 0},

 'TanBlue': {'BACKGROUND': '#e5dece',
             'TEXT': '#063289',
             'INPUT': '#f9f8f4',
             'TEXT_INPUT': '#242834',
             'SCROLL': '#eee8d5',
             'BUTTON': ('white', '#063289'),
             'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
             'BORDER': 1,
             'SLIDER_DEPTH': 0,
             'PROGRESS_DEPTH': 0},

 'DarkTanBlue': {'BACKGROUND': '#242834',
                 'TEXT': '#dfe6f8',
                 'INPUT': '#97755c',
                 'TEXT_INPUT': 'white',
                 'SCROLL': '#a9afbb',
                 'BUTTON': ('white', '#063289'),
                 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                 'BORDER': 1,
                 'SLIDER_DEPTH': 0,
                 'PROGRESS_DEPTH': 0},

 'DarkAmber': {'BACKGROUND': '#2c2825',
               'TEXT': '#fdcb52',
               'INPUT': '#705e52',
               'TEXT_INPUT': '#fdcb52',
               'SCROLL': '#705e52',
               'BUTTON': ('black', '#fdcb52'),
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 1,
               'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0},

 'DarkBlue': {'BACKGROUND': '#1a2835',
              'TEXT': '#d1ecff',
              'INPUT': '#335267',
              'TEXT_INPUT': '#acc2d0',
              'SCROLL': '#1b6497',
              'BUTTON': ('black', '#fafaf8'),
              'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
              'BORDER': 1, 'SLIDER_DEPTH': 0,
              'PROGRESS_DEPTH': 0},

 'Reds': {'BACKGROUND': '#280001',
          'TEXT': 'white',
          'INPUT': '#d8d584',
          'TEXT_INPUT': 'black',
          'SCROLL': '#763e00',
          'BUTTON': ('black', '#daad28'),
          'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
          'BORDER': 1,
          'SLIDER_DEPTH': 0,
          'PROGRESS_DEPTH': 0},

 'Green': {'BACKGROUND': '#82a459',
           'TEXT': 'black',
           'INPUT': '#d8d584',
           'TEXT_INPUT': 'black',
           'SCROLL': '#e3ecf3',
           'BUTTON': ('white', '#517239'),
           'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
           'BORDER': 1,
           'SLIDER_DEPTH': 0,
           'PROGRESS_DEPTH': 0},

 'BluePurple': {'BACKGROUND': '#A5CADD',
                'TEXT': '#6E266E',
                'INPUT': '#E0F5FF',
                'TEXT_INPUT': 'black',
                'SCROLL': '#E0F5FF',
                'BUTTON': ('white', '#303952'),
                'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0},

 'Purple': {'BACKGROUND': '#B0AAC2',
            'TEXT': 'black',
            'INPUT': '#F2EFE8',
            'SCROLL': '#F2EFE8',
            'TEXT_INPUT': 'black',
            'BUTTON': ('black', '#C2D4D8'),
            'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
            'BORDER': 1,
            'SLIDER_DEPTH': 0,
            'PROGRESS_DEPTH': 0},

 'BlueMono': {'BACKGROUND': '#AAB6D3',
              'TEXT': 'black',
              'INPUT': '#F1F4FC',
              'SCROLL': '#F1F4FC',
              'TEXT_INPUT': 'black',
              'BUTTON': ('white', '#7186C7'),
              'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
              'BORDER': 1,
              'SLIDER_DEPTH': 0,
              'PROGRESS_DEPTH': 0},

 'GreenMono': {'BACKGROUND': '#A8C1B4',
               'TEXT': 'black',
               'INPUT': '#DDE0DE',
               'SCROLL': '#E3E3E3',
               'TEXT_INPUT': 'black',
               'BUTTON': ('white', '#6D9F85'),
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 1,
               'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0},

 'BrownBlue': {'BACKGROUND': '#64778d',
               'TEXT': 'white',
               'INPUT': '#f0f3f7',
               'SCROLL': '#A6B2BE',
               'TEXT_INPUT': 'black',
               'BUTTON': ('white', '#283b5b'),
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 1,
               'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0},

 'BrightColors': {'BACKGROUND': '#b4ffb4',
                  'TEXT': 'black',
                  'INPUT': '#ffff64',
                  'SCROLL': '#ffb482',
                  'TEXT_INPUT': 'black',
                  'BUTTON': ('black', '#ffa0dc'),
                  'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                  'BORDER': 1,
                  'SLIDER_DEPTH': 0,
                  'PROGRESS_DEPTH': 0},

 'NeutralBlue': {'BACKGROUND': '#92aa9d',
                 'TEXT': 'black',
                 'INPUT': '#fcfff6',
                 'SCROLL': '#fcfff6',
                 'TEXT_INPUT': 'black',
                 'BUTTON': ('black', '#d0dbbd'),
                 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                 'BORDER': 1,
                 'SLIDER_DEPTH': 0,
                 'PROGRESS_DEPTH': 0},

 'Kayak': {'BACKGROUND': '#a7ad7f',
           'TEXT': 'black',
           'INPUT': '#e6d3a8',
           'SCROLL': '#e6d3a8',
           'TEXT_INPUT': 'black',
           'BUTTON': ('white', '#5d907d'),
           'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
           'BORDER': 1,
           'SLIDER_DEPTH': 0,
           'PROGRESS_DEPTH': 0},

 'SandyBeach': {'BACKGROUND': '#efeccb',
                'TEXT': '#012f2f',
                'INPUT': '#e6d3a8',
                'SCROLL': '#e6d3a8',
                'TEXT_INPUT': '#012f2f',
                'BUTTON': ('white', '#046380'),
                'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                'BORDER': 1, 'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0},

 'TealMono': {'BACKGROUND': '#a8cfdd',
              'TEXT': 'black',
              'INPUT': '#dfedf2',
              'SCROLL': '#dfedf2',
              'TEXT_INPUT': 'black',
              'BUTTON': ('white', '#183440'),
              'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
              'BORDER': 1,
              'SLIDER_DEPTH': 0,
              'PROGRESS_DEPTH': 0},
################################## Renamed Original Themes ##################################
'Default':
     {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
      'TEXT': COLOR_SYSTEM_DEFAULT,
      'INPUT': COLOR_SYSTEM_DEFAULT,
      'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
      'SCROLL': COLOR_SYSTEM_DEFAULT,
      'BUTTON': OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR,
      'PROGRESS': COLOR_SYSTEM_DEFAULT,
      'BORDER': 1, 'SLIDER_DEPTH': 1,
      'PROGRESS_DEPTH': 0},

 'Default1':
     {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
      'TEXT': COLOR_SYSTEM_DEFAULT,
      'INPUT': COLOR_SYSTEM_DEFAULT,
      'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
      'SCROLL': COLOR_SYSTEM_DEFAULT,
      'BUTTON': COLOR_SYSTEM_DEFAULT,
      'PROGRESS': COLOR_SYSTEM_DEFAULT,
      'BORDER': 1, 'SLIDER_DEPTH': 1,
      'PROGRESS_DEPTH': 0},

 'LightBlue': {'BACKGROUND': '#E3F2FD',
               'TEXT': '#000000',
               'INPUT': '#86A8FF',
               'TEXT_INPUT': '#000000',
               'SCROLL': '#86A8FF',
               'BUTTON': ('#FFFFFF', '#5079D3'),
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 0, 'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0,
               'ACCENT1': '#FF0266',
               'ACCENT2': '#FF5C93',
               'ACCENT3': '#C5003C'},

 'LightGrey': {'BACKGROUND': '#FAFAFA',
               'TEXT': '#000000',
               'INPUT': '#004EA1',
               'TEXT_INPUT': '#FFFFFF',
               'SCROLL': '#5EA7FF',
               'BUTTON': ('#FFFFFF', '#0079D3'),  # based on Reddit color
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 0, 'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0,
               'ACCENT1': '#FF0266',
               'ACCENT2': '#FF5C93',
               'ACCENT3': '#C5003C'},

 'LightGrey1': {'BACKGROUND': '#ffffff',
            'TEXT': '#1a1a1b',
            'INPUT': '#dae0e6',
            'TEXT_INPUT': '#222222',
            'SCROLL': '#a5a4a4',
            'BUTTON': ('white', '#0079d3'),
            'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
            'BORDER': 1,
            'SLIDER_DEPTH': 0,
            'PROGRESS_DEPTH': 0,
            'ACCENT1': '#ff5414',
            'ACCENT2': '#33a8ff',
            'ACCENT3': '#dbf0ff'},

 'DarkBrown': {'BACKGROUND': '#282923',
             'TEXT': '#E7DB74',
             'INPUT': '#393a32',
             'TEXT_INPUT': '#E7C855',
             'SCROLL': '#E7C855',
             'BUTTON': ('#E7C855', '#284B5A'),
             'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
             'BORDER': 1,
             'SLIDER_DEPTH': 0,
             'PROGRESS_DEPTH': 0,
             'ACCENT1': '#c15226',
             'ACCENT2': '#7a4d5f',
             'ACCENT3': '#889743'},

 'LightGreen1': {'BACKGROUND': '#9FB8AD',
              'TEXT': COLOR_SYSTEM_DEFAULT,
              'INPUT': '#F7F3EC', 'TEXT_INPUT': 'black',
              'SCROLL': '#F7F3EC',
              'BUTTON': ('white', '#475841'),
              'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
              'BORDER': 1, 'SLIDER_DEPTH': 0,
              'PROGRESS_DEPTH': 0},

 'DarkGrey': {'BACKGROUND': '#404040',
          'TEXT': 'white',
          'INPUT': '#4D4D4D',
          'TEXT_INPUT': 'white',
          'SCROLL': '#707070',
          'BUTTON': ('white', '#004F00'),
          'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
          'BORDER': 1,
          'SLIDER_DEPTH': 0,
          'PROGRESS_DEPTH': 0},

 'LightGreen2': {'BACKGROUND': '#B7CECE',
                'TEXT': 'black',
                'INPUT': '#FDFFF7',
                'TEXT_INPUT': 'black',
                'SCROLL': '#FDFFF7',
                'BUTTON': ('white', '#658268'),
                'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'ACCENT1': '#76506d',
                'ACCENT2': '#5148f1',
                'ACCENT3': '#0a1c84',
                'PROGRESS_DEPTH': 0},

 'DarkGrey1': {'BACKGROUND': '#404040',
           'TEXT': 'white',
           'INPUT': 'white',
           'TEXT_INPUT': 'black',
           'SCROLL': '#707070',
           'BUTTON': ('white', '#004F00'),
           'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
           'BORDER': 1,
           'SLIDER_DEPTH': 0,
           'PROGRESS_DEPTH': 0},

 'DarkBlack': {'BACKGROUND': 'black',
           'TEXT': 'white',
           'INPUT': '#4D4D4D',
           'TEXT_INPUT': 'white',
           'SCROLL': '#707070',
           'BUTTON': ('black', 'white'),
           'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
           'BORDER': 1,
           'SLIDER_DEPTH': 0,
           'PROGRESS_DEPTH': 0},

 'LightBrown': {'BACKGROUND': '#fdf6e3',
         'TEXT': '#268bd1',
         'INPUT': '#eee8d5',
         'TEXT_INPUT': '#6c71c3',
         'SCROLL': '#eee8d5',
         'BUTTON': ('white', '#063542'),
         'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
         'BORDER': 1,
         'SLIDER_DEPTH': 0,
         'PROGRESS_DEPTH': 0},

 'LightBrown1': {'BACKGROUND': '#e5dece',
             'TEXT': '#063289',
             'INPUT': '#f9f8f4',
             'TEXT_INPUT': '#242834',
             'SCROLL': '#eee8d5',
             'BUTTON': ('white', '#063289'),
             'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
             'BORDER': 1,
             'SLIDER_DEPTH': 0,
             'PROGRESS_DEPTH': 0},

 'DarkBlue1': {'BACKGROUND': '#242834',
                 'TEXT': '#dfe6f8',
                 'INPUT': '#97755c',
                 'TEXT_INPUT': 'white',
                 'SCROLL': '#a9afbb',
                 'BUTTON': ('white', '#063289'),
                 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                 'BORDER': 1,
                 'SLIDER_DEPTH': 0,
                 'PROGRESS_DEPTH': 0},

 'DarkBrown1': {'BACKGROUND': '#2c2825',
               'TEXT': '#fdcb52',
               'INPUT': '#705e52',
               'TEXT_INPUT': '#fdcb52',
               'SCROLL': '#705e52',
               'BUTTON': ('black', '#fdcb52'),
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 1,
               'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0},

 'DarkBlue2': {'BACKGROUND': '#1a2835',
              'TEXT': '#d1ecff',
              'INPUT': '#335267',
              'TEXT_INPUT': '#acc2d0',
              'SCROLL': '#1b6497',
              'BUTTON': ('black', '#fafaf8'),
              'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
              'BORDER': 1, 'SLIDER_DEPTH': 0,
              'PROGRESS_DEPTH': 0},

 'DarkBrown2': {'BACKGROUND': '#280001',
          'TEXT': 'white',
          'INPUT': '#d8d584',
          'TEXT_INPUT': 'black',
          'SCROLL': '#763e00',
          'BUTTON': ('black', '#daad28'),
          'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
          'BORDER': 1,
          'SLIDER_DEPTH': 0,
          'PROGRESS_DEPTH': 0},

 'DarkGreen': {'BACKGROUND': '#82a459',
           'TEXT': 'black',
           'INPUT': '#d8d584',
           'TEXT_INPUT': 'black',
           'SCROLL': '#e3ecf3',
           'BUTTON': ('white', '#517239'),
           'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
           'BORDER': 1,
           'SLIDER_DEPTH': 0,
           'PROGRESS_DEPTH': 0},

 'LightBlue1': {'BACKGROUND': '#A5CADD',
                'TEXT': '#6E266E',
                'INPUT': '#E0F5FF',
                'TEXT_INPUT': 'black',
                'SCROLL': '#E0F5FF',
                'BUTTON': ('white', '#303952'),
                'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                'BORDER': 1,
                'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0},

 'LightPurple': {'BACKGROUND': '#B0AAC2',
            'TEXT': 'black',
            'INPUT': '#F2EFE8',
            'SCROLL': '#F2EFE8',
            'TEXT_INPUT': 'black',
            'BUTTON': ('black', '#C2D4D8'),
            'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
            'BORDER': 1,
            'SLIDER_DEPTH': 0,
            'PROGRESS_DEPTH': 0},

 'LightBlue2': {'BACKGROUND': '#AAB6D3',
              'TEXT': 'black',
              'INPUT': '#F1F4FC',
              'SCROLL': '#F1F4FC',
              'TEXT_INPUT': 'black',
              'BUTTON': ('white', '#7186C7'),
              'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
              'BORDER': 1,
              'SLIDER_DEPTH': 0,
              'PROGRESS_DEPTH': 0},

 'LightGreen3': {'BACKGROUND': '#A8C1B4',
               'TEXT': 'black',
               'INPUT': '#DDE0DE',
               'SCROLL': '#E3E3E3',
               'TEXT_INPUT': 'black',
               'BUTTON': ('white', '#6D9F85'),
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 1,
               'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0},

 'DarkBlue3': {'BACKGROUND': '#64778d',
               'TEXT': 'white',
               'INPUT': '#f0f3f7',
               'SCROLL': '#A6B2BE',
               'TEXT_INPUT': 'black',
               'BUTTON': ('white', '#283b5b'),
               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
               'BORDER': 1,
               'SLIDER_DEPTH': 0,
               'PROGRESS_DEPTH': 0},

 'LightGreen4': {'BACKGROUND': '#b4ffb4',
                  'TEXT': 'black',
                  'INPUT': '#ffff64',
                  'SCROLL': '#ffb482',
                  'TEXT_INPUT': 'black',
                  'BUTTON': ('black', '#ffa0dc'),
                  'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                  'BORDER': 1,
                  'SLIDER_DEPTH': 0,
                  'PROGRESS_DEPTH': 0},

 'LightGreen5': {'BACKGROUND': '#92aa9d',
                 'TEXT': 'black',
                 'INPUT': '#fcfff6',
                 'SCROLL': '#fcfff6',
                 'TEXT_INPUT': 'black',
                 'BUTTON': ('black', '#d0dbbd'),
                 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                 'BORDER': 1,
                 'SLIDER_DEPTH': 0,
                 'PROGRESS_DEPTH': 0},

 'LightBrown2': {'BACKGROUND': '#a7ad7f',
           'TEXT': 'black',
           'INPUT': '#e6d3a8',
           'SCROLL': '#e6d3a8',
           'TEXT_INPUT': 'black',
           'BUTTON': ('white', '#5d907d'),
           'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
           'BORDER': 1,
           'SLIDER_DEPTH': 0,
           'PROGRESS_DEPTH': 0},

 'LightBrown3': {'BACKGROUND': '#efeccb',
                'TEXT': '#012f2f',
                'INPUT': '#e6d3a8',
                'SCROLL': '#e6d3a8',
                'TEXT_INPUT': '#012f2f',
                'BUTTON': ('white', '#046380'),
                'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                'BORDER': 1, 'SLIDER_DEPTH': 0,
                'PROGRESS_DEPTH': 0},

 'LightBlue3': {'BACKGROUND': '#a8cfdd',
              'TEXT': 'black',
              'INPUT': '#dfedf2',
              'SCROLL': '#dfedf2',
              'TEXT_INPUT': 'black',
              'BUTTON': ('white', '#183440'),
              'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
              'BORDER': 1,
              'SLIDER_DEPTH': 0,
              'PROGRESS_DEPTH': 0},


################################## End Renamed Original Themes ##################################


#
 'LightBrown4': {'BACKGROUND': '#d7c79e', 'TEXT': '#a35638', 'INPUT': '#9dab86', 'TEXT_INPUT': '#000000', 'SCROLL': '#a35638', 'BUTTON': ('white', '#a35638'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#a35638', '#9dab86', '#e08f62', '#d7c79e'], },
 'DarkTeal': {'BACKGROUND': '#003f5c', 'TEXT': '#fb5b5a', 'INPUT': '#bc4873', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#bc4873', 'BUTTON': ('white', '#fb5b5a'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#003f5c', '#472b62', '#bc4873', '#fb5b5a'], },
 'DarkPurple': {'BACKGROUND': '#472b62', 'TEXT': '#fb5b5a', 'INPUT': '#bc4873', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#bc4873', 'BUTTON': ('#FFFFFF', '#472b62'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#003f5c', '#472b62', '#bc4873', '#fb5b5a'], },
 'LightGreen6': {'BACKGROUND': '#eafbea', 'TEXT': '#1f6650', 'INPUT': '#6f9a8d', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#1f6650', 'BUTTON': ('white', '#1f6650'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#1f6650', '#6f9a8d', '#ea5e5e', '#eafbea'], },
 'DarkGrey2': {'BACKGROUND': '#2b2b28', 'TEXT': '#f8f8f8', 'INPUT': '#f1d6ab', 'TEXT_INPUT': '#000000', 'SCROLL': '#f1d6ab', 'BUTTON': ('#2b2b28', '#e3b04b'),
              'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
              'COLOR_LIST': ['#2b2b28', '#e3b04b', '#f1d6ab', '#f8f8f8'], },
 'LightBrown6': {'BACKGROUND': '#f9b282', 'TEXT': '#8f4426', 'INPUT': '#de6b35', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#8f4426', 'BUTTON': ('white', '#8f4426'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#8f4426', '#de6b35', '#64ccda', '#f9b282'], },
 'DarkTeal1': {'BACKGROUND': '#396362', 'TEXT': '#ffe7d1', 'INPUT': '#f6c89f', 'TEXT_INPUT': '#000000', 'SCROLL': '#f6c89f',
                   'BUTTON': ('#ffe7d1', '#4b8e8d'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                   'COLOR_LIST': ['#396362', '#4b8e8d', '#f6c89f', '#ffe7d1'],},
 'LightBrown7': {'BACKGROUND': '#f6c89f', 'TEXT': '#396362', 'INPUT': '#4b8e8d', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#396362',
                    'BUTTON': ('white', '#396362'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                    'COLOR_LIST': ['#396362', '#4b8e8d', '#f6c89f', '#ffe7d1'],},
 'DarkPurple1': {'BACKGROUND': '#0c093c', 'TEXT': '#fad6d6', 'INPUT': '#eea5f6', 'TEXT_INPUT': '#000000', 'SCROLL': '#eea5f6', 'BUTTON': ('#FFFFFF', '#df42d1'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#0c093c', '#df42d1', '#eea5f6', '#fad6d6'], },
 'DarkGrey3': {'BACKGROUND': '#211717', 'TEXT': '#dfddc7', 'INPUT': '#f58b54', 'TEXT_INPUT': '#000000', 'SCROLL': '#f58b54', 'BUTTON': ('#dfddc7', '#a34a28'),
               'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
               'COLOR_LIST': ['#211717', '#a34a28', '#f58b54', '#dfddc7'], },
 'LightBrown8': {'BACKGROUND': '#dfddc7', 'TEXT': '#211717', 'INPUT': '#a34a28', 'TEXT_INPUT': '#dfddc7', 'SCROLL': '#211717', 'BUTTON': ('#dfddc7', '#a34a28'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#211717', '#a34a28', '#f58b54', '#dfddc7'], },
 'DarkBlue4': {'BACKGROUND': '#494ca2', 'TEXT': '#e3e7f1', 'INPUT': '#c6cbef', 'TEXT_INPUT': '#000000', 'SCROLL': '#c6cbef', 'BUTTON': ('#FFFFFF', '#8186d5'),
              'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
              'COLOR_LIST': ['#494ca2', '#8186d5', '#c6cbef', '#e3e7f1'],},
 'LightBlue4': {'BACKGROUND': '#5c94bd', 'TEXT': '#470938', 'INPUT': '#1a3e59', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#470938', 'BUTTON': ('white', '#470938'),
               'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
               'COLOR_LIST': ['#470938', '#1a3e59', '#5c94bd', '#f2d6eb'],},
 'DarkTeal2': {'BACKGROUND': '#394a6d', 'TEXT': '#c0ffb3', 'INPUT': '#52de97', 'TEXT_INPUT': '#000000', 'SCROLL': '#52de97',
                    'BUTTON': ('#c0ffb3', '#394a6d'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                    'COLOR_LIST': ['#394a6d', '#3c9d9b', '#52de97', '#c0ffb3'],},
 'DarkTeal3': {'BACKGROUND': '#3c9d9b', 'TEXT': '#c0ffb3', 'INPUT': '#52de97', 'TEXT_INPUT': '#000000', 'SCROLL': '#52de97',
                    'BUTTON': ('#c0ffb3', '#394a6d'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                    'COLOR_LIST': ['#394a6d', '#3c9d9b', '#52de97', '#c0ffb3'], },
 'DarkPurple5': {'BACKGROUND': '#730068', 'TEXT': '#f6f078', 'INPUT': '#01d28e', 'TEXT_INPUT': '#000000', 'SCROLL': '#01d28e', 'BUTTON': ('#f6f078', '#730068'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#730068', '#434982', '#01d28e', '#f6f078'],},
 'DarkPurple2': {'BACKGROUND': '#202060', 'TEXT': '#b030b0', 'INPUT': '#602080', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#602080', 'BUTTON': ('white', '#202040'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#202040', '#202060', '#602080', '#b030b0'], },
 'DarkBlue5': {'BACKGROUND': '#000272', 'TEXT': '#ff6363', 'INPUT': '#a32f80', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#a32f80', 'BUTTON': ('#FFFFFF', '#341677'),
               'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
               'COLOR_LIST': ['#000272', '#341677', '#a32f80', '#ff6363'], },
 'LightGrey2': {'BACKGROUND': '#f6f6f6', 'TEXT': '#420000', 'INPUT': '#d4d7dd', 'TEXT_INPUT': '#420000', 'SCROLL': '#420000', 'BUTTON': ('#420000', '#d4d7dd'),
               'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
               'COLOR_LIST': ['#420000', '#d4d7dd', '#eae9e9', '#f6f6f6'],},
 'LightGrey3': {'BACKGROUND': '#eae9e9', 'TEXT': '#420000', 'INPUT': '#d4d7dd', 'TEXT_INPUT': '#420000', 'SCROLL': '#420000', 'BUTTON': ('#420000', '#d4d7dd'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#420000', '#d4d7dd', '#eae9e9', '#f6f6f6'], },
 'DarkBlue6': {'BACKGROUND': '#01024e', 'TEXT': '#ff6464', 'INPUT': '#8b4367', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#8b4367', 'BUTTON': ('#FFFFFF', '#543864'),
              'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
              'COLOR_LIST': ['#01024e', '#543864', '#8b4367', '#ff6464'],},
 'DarkBlue7': {'BACKGROUND': '#241663', 'TEXT': '#eae7af', 'INPUT': '#a72693', 'TEXT_INPUT': '#eae7af', 'SCROLL': '#a72693', 'BUTTON': ('#eae7af', '#160f30'),
               'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
               'COLOR_LIST': ['#160f30', '#241663', '#a72693', '#eae7af'], },
 'LightBrown9': {'BACKGROUND': '#f6d365', 'TEXT': '#3a1f5d', 'INPUT': '#c83660', 'TEXT_INPUT': '#f6d365', 'SCROLL': '#3a1f5d', 'BUTTON': ('#f6d365', '#c83660'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#3a1f5d', '#c83660', '#e15249', '#f6d365'], },
 'DarkPurple3': {'BACKGROUND': '#6e2142', 'TEXT': '#ffd692', 'INPUT': '#e16363', 'TEXT_INPUT': '#ffd692', 'SCROLL': '#e16363', 'BUTTON': ('#ffd692', '#943855'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#6e2142', '#943855', '#e16363', '#ffd692'], },
 'LightBrown10': {'BACKGROUND': '#ffd692', 'TEXT': '#6e2142', 'INPUT': '#943855', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#6e2142', 'BUTTON': ('white', '#6e2142'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#6e2142', '#943855', '#e16363', '#ffd692'],},
 'DarkPurple4': {'BACKGROUND': '#200f21', 'TEXT': '#f638dc', 'INPUT': '#5a3d5c', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#5a3d5c', 'BUTTON': ('#FFFFFF', '#382039'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#200f21', '#382039', '#5a3d5c', '#f638dc'],},
 'LightBlue5': {'BACKGROUND': '#b2fcff', 'TEXT': '#3e64ff', 'INPUT': '#5edfff', 'TEXT_INPUT': '#000000', 'SCROLL': '#3e64ff', 'BUTTON': ('white', '#3e64ff'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#3e64ff', '#5edfff', '#b2fcff', '#ecfcff'], },
 'DarkTeal4': {'BACKGROUND': '#464159', 'TEXT': '#c7f0db', 'INPUT': '#8bbabb', 'TEXT_INPUT': '#000000', 'SCROLL': '#8bbabb',
                   'BUTTON': ('#FFFFFF', '#6c7b95'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                   'COLOR_LIST': ['#464159', '#6c7b95', '#8bbabb', '#c7f0db'], },
 'LightTeal': {'BACKGROUND': '#c7f0db', 'TEXT': '#464159', 'INPUT': '#6c7b95', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#464159',
                     'BUTTON': ('white', '#464159'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                     'COLOR_LIST': ['#464159', '#6c7b95', '#8bbabb', '#c7f0db'],},
 'DarkTeal5': {'BACKGROUND': '#8bbabb', 'TEXT': '#464159', 'INPUT': '#6c7b95', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#464159',
                     'BUTTON': ('#c7f0db', '#6c7b95'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                     'COLOR_LIST': ['#464159', '#6c7b95', '#8bbabb', '#c7f0db'], },
 'LightGrey4': {'BACKGROUND': '#faf5ef', 'TEXT': '#672f2f', 'INPUT': '#99b19c', 'TEXT_INPUT': '#672f2f', 'SCROLL': '#672f2f', 'BUTTON': ('#672f2f', '#99b19c'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#672f2f', '#99b19c', '#d7d1c9', '#faf5ef'], },
 'LightGreen7': {'BACKGROUND': '#99b19c', 'TEXT': '#faf5ef', 'INPUT': '#d7d1c9', 'TEXT_INPUT': '#000000', 'SCROLL': '#d7d1c9', 'BUTTON': ('#FFFFFF', '#99b19c'),
               'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
               'COLOR_LIST': ['#672f2f', '#99b19c', '#d7d1c9', '#faf5ef'],},
 'LightGrey5': {'BACKGROUND': '#d7d1c9', 'TEXT': '#672f2f', 'INPUT': '#99b19c', 'TEXT_INPUT': '#672f2f', 'SCROLL': '#672f2f', 'BUTTON': ('white', '#672f2f'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#672f2f', '#99b19c', '#d7d1c9', '#faf5ef'], },
 'DarkBrown3': {'BACKGROUND': '#a0855b', 'TEXT': '#f9f6f2', 'INPUT': '#f1d6ab', 'TEXT_INPUT': '#000000', 'SCROLL': '#f1d6ab', 'BUTTON': ('white', '#38470b'),
               'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
               'COLOR_LIST': ['#38470b', '#a0855b', '#f1d6ab', '#f9f6f2'], },
 'LightBrown11': {'BACKGROUND': '#f1d6ab', 'TEXT': '#38470b', 'INPUT': '#a0855b', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#38470b', 'BUTTON': ('#f9f6f2', '#a0855b'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#38470b', '#a0855b', '#f1d6ab', '#f9f6f2'],},
 'DarkRed': {'BACKGROUND': '#83142c', 'TEXT': '#f9d276', 'INPUT': '#ad1d45', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#ad1d45', 'BUTTON': ('#f9d276', '#ad1d45'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#44000d', '#83142c', '#ad1d45', '#f9d276'], },
 'DarkTeal6': {'BACKGROUND': '#204969', 'TEXT': '#fff7f7', 'INPUT': '#dadada', 'TEXT_INPUT': '#000000', 'SCROLL': '#dadada',
                    'BUTTON': ('black', '#fff7f7'), 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                    'COLOR_LIST': ['#204969', '#08ffc8', '#dadada', '#fff7f7'],},
 'DarkBrown4': {'BACKGROUND': '#252525', 'TEXT': '#ff0000', 'INPUT': '#af0404', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#af0404', 'BUTTON': ('white', '#252525'),
             'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
             'COLOR_LIST': ['#252525', '#414141', '#af0404', '#ff0000'], },
 'LightYellow': {'BACKGROUND': '#f4ff61', 'TEXT': '#27aa80', 'INPUT': '#32ff6a', 'TEXT_INPUT': '#000000', 'SCROLL': '#27aa80', 'BUTTON': ('#f4ff61', '#27aa80'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#27aa80', '#32ff6a', '#a8ff3e', '#f4ff61'],},
 'DarkGreen1': {'BACKGROUND': '#2b580c', 'TEXT': '#fdef96', 'INPUT': '#f7b71d', 'TEXT_INPUT': '#000000', 'SCROLL': '#f7b71d', 'BUTTON': ('#fdef96', '#2b580c'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#2b580c', '#afa939', '#f7b71d', '#fdef96'], },
 'LightGreen8': {'BACKGROUND': '#c8dad3', 'TEXT': '#63707e', 'INPUT': '#93b5b3', 'TEXT_INPUT': '#000000', 'SCROLL': '#63707e', 'BUTTON': ('white', '#63707e'),
                'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                'COLOR_LIST': ['#63707e', '#93b5b3', '#c8dad3', '#f2f6f5'], },
 'DarkTeal7': {'BACKGROUND': '#248ea9', 'TEXT': '#fafdcb', 'INPUT': '#aee7e8', 'TEXT_INPUT': '#000000', 'SCROLL': '#aee7e8', 'BUTTON': ('black', '#fafdcb'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#248ea9', '#28c3d4', '#aee7e8', '#fafdcb'],},
'DarkBlue8': {'BACKGROUND': '#454d66', 'TEXT': '#d9d872', 'INPUT': '#58b368', 'TEXT_INPUT': '#000000', 'SCROLL': '#58b368',
              'BUTTON': ('black', '#009975'),
              'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#009975', '#454d66', '#58b368', '#d9d872'], },
 'DarkBlue9': {'BACKGROUND': '#263859', 'TEXT': '#ff6768', 'INPUT': '#6b778d', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#6b778d', 'BUTTON': ('#ff6768', '#263859'),
               'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
               'COLOR_LIST': ['#17223b', '#263859', '#6b778d', '#ff6768'], },
 'DarkBlue10': {'BACKGROUND': '#0028ff', 'TEXT': '#f1f4df', 'INPUT': '#10eaf0', 'TEXT_INPUT': '#000000', 'SCROLL': '#10eaf0', 'BUTTON': ('#f1f4df', '#24009c'),
               'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
               'COLOR_LIST': ['#24009c', '#0028ff', '#10eaf0', '#f1f4df'],},
 'DarkBlue11': {'BACKGROUND': '#6384b3', 'TEXT': '#e6f0b6', 'INPUT': '#b8e9c0', 'TEXT_INPUT': '#000000', 'SCROLL': '#b8e9c0', 'BUTTON': ('#e6f0b6', '#684949'),
               'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
               'COLOR_LIST': ['#684949', '#6384b3', '#b8e9c0', '#e6f0b6'], },

 'DarkTeal8': {'BACKGROUND': '#71a0a5', 'TEXT': '#212121', 'INPUT': '#665c84', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#212121', 'BUTTON': ('#fab95b', '#665c84'),
                 'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                 'COLOR_LIST': ['#212121', '#665c84', '#71a0a5', '#fab95b']},
 'DarkRed1': {'BACKGROUND': '#c10000', 'TEXT': '#eeeeee', 'INPUT': '#dedede', 'TEXT_INPUT': '#000000', 'SCROLL': '#dedede', 'BUTTON': ('#c10000', '#eeeeee'),
               'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
               'COLOR_LIST': ['#c10000', '#ff4949', '#dedede', '#eeeeee'],},
 'LightBrown5': {'BACKGROUND': '#fff591', 'TEXT': '#e41749', 'INPUT': '#f5587b', 'TEXT_INPUT': '#000000', 'SCROLL': '#e41749', 'BUTTON': ('#fff591', '#e41749'),
              'PROGRESS': ('#01826B', '#D0D0D0'), 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
              'COLOR_LIST': ['#e41749', '#f5587b', '#ff8a5c', '#fff591']}
                 }

def ListOfLookAndFeelValues():
    """
    Get a list of the valid values to pass into your call to change_look_and_feel
    :return: List[str] - list of valid string values
    """
    return list(LOOK_AND_FEEL_TABLE.keys())


def ChangeLookAndFeel(index, force=False):
    """
    Change the "color scheme" of all future PySimpleGUI Windows.
    The scheme are string names that specify a group of colors. Background colors, text colors, button colors.
    There are 13 different color settings that are changed at one time using a single call to ChangeLookAndFeel
    The look and feel table itself has these indexes into the dictionary LOOK_AND_FEEL_TABLE.
    The original list was (prior to a major rework and renaming)... these names still work...
        SystemDefault
        SystemDefaultForRead
        Material1
        Material2
        Reddit
        Topanga
        GreenTan
        Dark
        LightGreen
        Dark2
        Black
        Tan
        TanBlue
        DarkTanBlue
        DarkAmber
        DarkBlue
        Reds
        Green
        BluePurple
        Purple
        BlueMono
        GreenMono
        BrownBlue
        BrightColors
        NeutralBlue
        Kayak
        SandyBeach
        TealMono

    In Nov 2019 a new Theme Formula was devised to make choosing a theme easier:
    The "Formula" is:
    ["Dark" or "Light"] Color Number
    Colors can be Blue Brown Grey Green Purple Red Teal Yellow Black
    The number will vary for each pair. There are more DarkGrey entries than there are LightYellow for example.
    Default = The default settings (only button color is different than system default)
    Default1 = The full system default including the button (everything's gray... how sad... don't be all gray... please....)
    :param index: (str) the name of the index into the Look and Feel table
    :param force: (bool) if True allows Macs to use the look and feel feature. Otherwise Macs are blocked due to problems with button colors
    """

    # if sys.platform.startswith('darwin') and not force:
    #     print('*** Changing look and feel is not supported on Mac platform ***')
    #     return

    theme = index
    # normalize available l&f values
    lf_values = [item.lower() for item in list_of_look_and_feel_values()]

    # option 1
    opt1 = theme.replace(' ', '').lower()

    # option 2 (reverse lookup)
    optx = theme.lower().split(' ')
    optx.reverse()
    opt2 = ''.join(optx)

    # search for valid l&f name
    if opt1 in lf_values:
        ix = lf_values.index(opt1)
    elif opt2 in lf_values:
        ix = lf_values.index(opt2)
    else:
        ix = randint(0,len(lf_values))
        print('** Warning - {} Look and Feel value not valid. Change your ChangeLookAndFeel call. **'.format(index))
        print('valid values are', list_of_look_and_feel_values())
        print('Instead, please enjoy a random Theme named {}'.format(list_of_look_and_feel_values()[ix]))

    selection = list_of_look_and_feel_values()[ix]

    try:
        colors = LOOK_AND_FEEL_TABLE[selection]

        SetOptions(background_color=colors['BACKGROUND'],
                   text_element_background_color=colors['BACKGROUND'],
                   element_background_color=colors['BACKGROUND'],
                   text_color=colors['TEXT'],
                   input_elements_background_color=colors['INPUT'],
                   button_color=colors['BUTTON'],
                   progress_meter_color=colors['PROGRESS'],
                   border_width=colors['BORDER'],
                   slider_border_width=colors['SLIDER_DEPTH'],
                   progress_meter_border_depth=colors['PROGRESS_DEPTH'],
                   scrollbar_color=(colors['SCROLL']),
                   element_text_color=colors['TEXT'],
                   input_text_color=colors['TEXT_INPUT'])
    except:  # most likely an index out of range
        print('** Warning - Look and Feel value not valid. Change your ChangeLookAndFeel call. **')
        print('valid values are', list_of_look_and_feel_values())


def preview_all_look_and_feel_themes():
    """
    Displays a "Quick Reference Window" showing all of the different Look and Feel settings that are available.
    They are sorted alphabetically.  The legacy color names are mixed in, but otherwise they are sorted into Dark and Light halves
    """
    web=False

    WINDOW_BACKGROUND = 'lightblue'

    def sample_layout():
        return [[Text('Text element'), InputText('Input data here', size=(15, 1))],
                [Button('Ok'), Button('Cancel'), Slider((1, 10), orientation='h', size=(10, 15))]]

    layout = [[Text('Here is a complete list of themes', font='Default 18', background_color=WINDOW_BACKGROUND)]]

    names = list_of_look_and_feel_values()
    names.sort()
    row = []
    for count, theme in enumerate(names):
        change_look_and_feel(theme)
        if not count % 9:
            layout += [row]
            row = []
        row += [Frame(theme, sample_layout() if not web else [[T(theme)]] + sample_layout())]
    if row:
        layout += [row]

    window = Window('Preview of all Look and Feel choices', layout, background_color=WINDOW_BACKGROUND)
    window.read()
    window.close()
    del window



# ============================== sprint ======#
# Is identical to the Scrolled Text Box       #
# Provides a crude 'print' mechanism but in a #
# GUI environment                             #
# ============================================#
sprint = ScrolledTextBox


# Converts an object's contents into a nice printable string.  Great for dumping debug data
def ObjToStringSingleObj(obj):
    if obj is None:
        return 'None'
    return str(obj.__class__) + '\n' + '\n'.join(
        (repr(item) + ' = ' + repr(obj.__dict__[item]) for item in sorted(obj.__dict__)))


def ObjToString(obj, extra='    '):
    if obj is None:
        return 'None'
    return str(obj.__class__) + '\n' + '\n'.join(
        (extra + (str(item) + ' = ' +
                  (ObjToString(obj.__dict__[item], extra + '    ') if hasattr(obj.__dict__[item], '__dict__') else str(
                      obj.__dict__[item])))
         for item in sorted(obj.__dict__)))


# ------------------------------------------------------------------------------------------------------------------ #
# =====================================   Upper PySimpleGUI ======================================================== #
#   Pre-built dialog boxes for all your needs    These are the "high level API calls                                 #
# ------------------------------------------------------------------------------------------------------------------ #

######
#     #   ####   #####   #    #  #####    ####
#     #  #    #  #    #  #    #  #    #  #
######   #    #  #    #  #    #  #    #   ####
#        #    #  #####   #    #  #####        #
#        #    #  #       #    #  #       #    #
#         ####   #        ####   #        ####



# ----------------------------------- The mighty Popup! ------------------------------------------------------------ #


def Popup(*args, title=None, button_color=None, background_color=None, text_color=None, button_type=POPUP_BUTTONS_OK,
          auto_close=False, auto_close_duration=None, custom_text=(None, None), non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None,
          font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Popup - Display a popup box with as many parms as you wish to include
    :param args:
    :param button_color:
    :param background_color:
    :param text_color:
    :param button_type:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return:
    """
    if not args:
        args_to_print = ['']
    else:
        args_to_print = args
    if line_width != None:
        local_line_width = line_width
    else:
        local_line_width = MESSAGE_BOX_LINE_WIDTH
    _title =  title if title is not None else args_to_print[0]
    window = Window(_title, auto_size_text=True, background_color=background_color, button_color=button_color,
                    auto_close=auto_close, auto_close_duration=auto_close_duration, icon=icon, font=font,
                    no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)
    max_line_total, total_lines = 0, 0
    for message in args_to_print:
        # fancy code to check if string and convert if not is not need. Just always convert to string :-)
        # if not isinstance(message, str): message = str(message)
        message = str(message)
        if message.count('\n'):
            message_wrapped = message
        else:
            message_wrapped = textwrap.fill(message, local_line_width)
        message_wrapped_lines = message_wrapped.count('\n') + 1
        longest_line_len = max([len(l) for l in message.split('\n')])
        width_used = min(longest_line_len, local_line_width)
        max_line_total = max(max_line_total, width_used)
        # height = _GetNumLinesNeeded(message, width_used)
        height = message_wrapped_lines
        window.AddRow(
            Text(message_wrapped, auto_size_text=True, text_color=text_color, background_color=background_color))
        total_lines += height

    if non_blocking:
        PopupButton = DummyButton  # important to use or else button will close other windows too!
    else:
        PopupButton = Button
    # show either an OK or Yes/No depending on paramater
    if custom_text != (None, None):
        if type(custom_text) is not tuple:
            window.AddRow(PopupButton(custom_text,size=(len(custom_text),1), button_color=button_color, focus=True, bind_return_key=True))
        elif custom_text[1] is None:
            window.AddRow(PopupButton(custom_text[0],size=(len(custom_text[0]),1), button_color=button_color, focus=True, bind_return_key=True))
        else:
            window.AddRow(PopupButton(custom_text[0], button_color=button_color, focus=True, bind_return_key=True, size=(len(custom_text[0]), 1)),
                          PopupButton(custom_text[1], button_color=button_color, size=(len(custom_text[0]), 1)))
    elif button_type is POPUP_BUTTONS_YES_NO:
        window.AddRow(PopupButton('Yes', button_color=button_color, focus=True, bind_return_key=True, pad=((20, 5), 3),
                                  size=(5, 1)), PopupButton('No', button_color=button_color, size=(5, 1)))
    elif button_type is POPUP_BUTTONS_CANCELLED:
        window.AddRow(
            PopupButton('Cancelled', button_color=button_color, focus=True, bind_return_key=True, pad=((20, 0), 3)))
    elif button_type is POPUP_BUTTONS_ERROR:
        window.AddRow(PopupButton('Error', size=(6, 1), button_color=button_color, focus=True, bind_return_key=True,
                                  pad=((20, 0), 3)))
    elif button_type is POPUP_BUTTONS_OK_CANCEL:
        window.AddRow(PopupButton('OK', size=(6, 1), button_color=button_color, focus=True, bind_return_key=True),
                      PopupButton('Cancel', size=(6, 1), button_color=button_color))
    elif button_type is POPUP_BUTTONS_NO_BUTTONS:
        pass
    else:
        window.AddRow(PopupButton('OK', size=(5, 1), button_color=button_color, focus=True, bind_return_key=True,
                                  pad=((20, 0), 3)))

    if non_blocking:
        button, values = window.Read(timeout=0)
        return button, window
    else:
        button, values = window.Read()
        window.Close()
        return button


# ==============================  MsgBox============#
# Lazy function. Same as calling Popup with parms   #
# This function WILL Disappear perhaps today        #
# ==================================================#
# MsgBox is the legacy call and should not be used any longer
def MsgBox(*args):
    raise DeprecationWarning('MsgBox is no longer supported... change your call to Popup')


# --------------------------- PopupNoButtons ---------------------------
def PopupNoButtons(*args, button_color=None, background_color=None, text_color=None, auto_close=False,
                   auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
                   no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Show a Popup but without any buttons
    :param args:
    :param button_color:
    :param background_color:
    :param text_color:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return:
    """
    Popup(*args, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=POPUP_BUTTONS_NO_BUTTONS,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupNonBlocking ---------------------------
def PopupNonBlocking(*args, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
                     auto_close=False, auto_close_duration=None, non_blocking=True, icon=DEFAULT_WINDOW_ICON,
                     line_width=None, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False,
                     location=(None, None)):
    """
    Show Popup box and immediately return (does not block)
    :param args:
    :param button_type:
    :param button_color:
    :param background_color:
    :param text_color:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return:
    """
    return Popup(*args, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


PopupNoWait = PopupNonBlocking


# --------------------------- PopupQuick - a NonBlocking, Self-closing Popup  ---------------------------
def PopupQuick(*args, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
               auto_close=True, auto_close_duration=2, non_blocking=True, icon=DEFAULT_WINDOW_ICON, line_width=None,
               font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Show Popup box that doesn't block and closes itself
    :param args:
    :param button_type:
    :param button_color:
    :param background_color:
    :param text_color:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return:
    """
    Popup(*args, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupQuick - a NonBlocking, Self-closing Popup with no titlebar and no buttons ---------------------------
def PopupQuickMessage(*args, button_type=POPUP_BUTTONS_NO_BUTTONS, button_color=None, background_color=None,
                      text_color=None,
                      auto_close=True, auto_close_duration=2, non_blocking=True, icon=DEFAULT_WINDOW_ICON,
                      line_width=None,
                      font=None, no_titlebar=True, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Show Popup box that doesn't block and closes itself
    :param args:
    :param button_type:
    :param button_color:
    :param background_color:
    :param text_color:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return:
    """
    Popup(*args, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupNoTitlebar ---------------------------
def PopupNoTitlebar(*args, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
                    auto_close=False, auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON,
                    line_width=None, font=None, grab_anywhere=True, keep_on_top=False, location=(None, None)):
    """
    Display a Popup without a titlebar.   Enables grab anywhere so you can move it
    :param args:
    :param button_type:
    :param button_color:
    :param background_color:
    :param text_color:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return:
    """
    Popup(*args, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=True, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


PopupNoFrame = PopupNoTitlebar
PopupNoBorder = PopupNoTitlebar
PopupAnnoying = PopupNoTitlebar


# --------------------------- PopupAutoClose ---------------------------
def PopupAutoClose(*args, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
                   auto_close=True, auto_close_duration=DEFAULT_AUTOCLOSE_TIME, non_blocking=False, icon=DEFAULT_WINDOW_ICON,
                   line_width=None, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False,
                   location=(None, None)):
    """
    Popup that closes itself after some time period
    :param args:
    :param button_type:
    :param button_color:
    :param background_color:
    :param text_color:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return:
    """
    Popup(*args, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


PopupTimed = PopupAutoClose


# --------------------------- PopupError ---------------------------
def PopupError(*args, button_color=DEFAULT_ERROR_BUTTON_COLOR, background_color=None, text_color=None, auto_close=False,
               auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
               no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Popup with colored button and 'Error' as button text
    :param args:
    :param button_color:
    :param background_color:
    :param text_color:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return:
    """
    Popup(*args, button_type=POPUP_BUTTONS_ERROR, background_color=background_color, text_color=text_color,
          non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color, auto_close=auto_close,
          auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
          keep_on_top=keep_on_top, location=location)


# --------------------------- PopupCancel ---------------------------
def PopupCancel(*args, button_color=None, background_color=None, text_color=None, auto_close=False,
                auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
                no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Display Popup with "cancelled" button text
    :param args:
    :param button_color:
    :param background_color:
    :param text_color:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return:
    """
    Popup(*args, button_type=POPUP_BUTTONS_CANCELLED, background_color=background_color, text_color=text_color,
          non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color, auto_close=auto_close,
          auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
          keep_on_top=keep_on_top, location=location)


# --------------------------- PopupOK ---------------------------
def PopupOK(*args, button_color=None, background_color=None, text_color=None, auto_close=False,
            auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
            no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Display Popup with OK button only
    :param args:
    :param button_color:
    :param background_color:
    :param text_color:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return:
    """
    Popup(*args, button_type=POPUP_BUTTONS_OK, background_color=background_color, text_color=text_color,
          non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color, auto_close=auto_close,
          auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
          keep_on_top=keep_on_top, location=location)


# --------------------------- PopupOKCancel ---------------------------
def PopupOKCancel(*args, button_color=None, background_color=None, text_color=None, auto_close=False,
                  auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
                  no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Display popup with OK and Cancel buttons
    :param args:
    :param button_color:
    :param background_color:
    :param text_color:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return: OK, Cancel or None
    """
    return Popup(*args, button_type=POPUP_BUTTONS_OK_CANCEL, background_color=background_color, text_color=text_color,
                 non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color,
                 auto_close=auto_close, auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar,
                 grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupYesNo ---------------------------
def PopupYesNo(*args, button_color=None, background_color=None, text_color=None, auto_close=False,
               auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
               no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Display Popup with Yes and No buttons
    :param args:
    :param button_color:
    :param background_color:
    :param text_color:
    :param auto_close:
    :param auto_close_duration:
    :param non_blocking:
    :param icon:
    :param line_width:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return: Yes, No or None
    """
    return Popup(*args, button_type=POPUP_BUTTONS_YES_NO, background_color=background_color, text_color=text_color,
                 non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color,
                 auto_close=auto_close, auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar,
                 grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


##############################################################################
#   The PopupGet_____ functions - Will return user input                     #
##############################################################################


# --------------------------- PopupGetFolder ---------------------------


def PopupGetFolder(message, title=None, default_path='', no_window=False, size=(None, None), button_color=None,
                   background_color=None, text_color=None, icon=DEFAULT_WINDOW_ICON, font=None, no_titlebar=False,
                   grab_anywhere=False, keep_on_top=False, location=(None, None), initial_folder=None):
    """
    Display popup with text entry field and browse button. Browse for folder
    :param message:
    :param default_path:
    :param no_window:
    :param size:
    :param button_color:
    :param background_color:
    :param text_color:
    :param icon:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return: Contents of text field. None if closed using X or cancelled
    """


    if no_window:
        app = wx.App(False)
        frame = wx.Frame()

        if initial_folder:
            dialog = wx.DirDialog(frame, style=wx.FD_OPEN)
        else:
            dialog = wx.DirDialog(frame)
        folder_name = ''
        if dialog.ShowModal() == wx.ID_OK:
            folder_name = dialog.GetPath()
        return folder_name



    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=size, key='_INPUT_'), FolderBrowse(initial_folder=initial_folder)],
              [Button('Ok', size=(60, 20), bind_return_key=True), Button('Cancel', size=(60, 20))]]

    _title = title if title is not None else message
    window = Window(title=_title, layout=layout, icon=icon, auto_size_text=True, button_color=button_color,
                    background_color=background_color,
                    font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    button, values = window.Read()
    window.Close()
    if button != 'Ok':
        return None
    else:
        path = values['_INPUT_']
        return path




# --------------------------- PopupGetFile ---------------------------

def PopupGetFile(message, title=None, default_path='', default_extension='', save_as=False, file_types=(("ALL Files", "*"),),
                 no_window=False, size=(None, None), button_color=None, background_color=None, text_color=None,
                 icon=DEFAULT_WINDOW_ICON, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False,
                 location=(None, None), initial_folder=None):
    """
        Display popup with text entry field and browse button. Browse for file
    :param message:
    :param default_path:
    :param default_extension:
    :param save_as:
    :param file_types:
    :param no_window:
    :param size:
    :param button_color:
    :param background_color:
    :param text_color:
    :param icon:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return:  string representing the path chosen, None if cancelled or window closed with X
    """

    if no_window:
        app = wx.App(False)
        frame = wx.Frame()

        qt_types = convert_tkinter_filetypes_to_wx(file_types)
        style = wx.FD_SAVE if save_as else wx.FD_OPEN
        if initial_folder:
            dialog = wx.FileDialog(frame, defaultDir=initial_folder, wildcard=qt_types,
                                   style=style)
        else:
            dialog = wx.FileDialog(frame, wildcard=qt_types, style=style)
        if dialog.ShowModal() == wx.ID_OK:
            file_name = dialog.GetPath()
        else:
            file_name = ''
        return file_name

    browse_button = SaveAs(file_types=file_types, initial_folder=initial_folder) if save_as else FileBrowse(
        file_types=file_types, initial_folder=initial_folder)

    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=(30,1), key='_INPUT_'), browse_button],
              [Button('Ok', size=(60, 20), bind_return_key=True), Button('Cancel', size=(60, 20))]]

    _title = title if title is not None else message

    window = Window(title=_title, layout=layout, icon=icon, auto_size_text=True, button_color=button_color, font=font,
                    background_color=background_color,
                    no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)

    button, values = window.Read()
    window.Close()
    if button != 'Ok':
        return None
    else:
        path = values['_INPUT_']
        return path




# --------------------------- PopupGetText ---------------------------

def PopupGetText(message, title=None, default_text='', password_char='', size=(None, None), button_color=None,
                 background_color=None, text_color=None, icon=DEFAULT_WINDOW_ICON, font=None, no_titlebar=False,
                 grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Display Popup with text entry field
    :param message:
    :param default_text:
    :param password_char:
    :param size:
    :param button_color:
    :param background_color:
    :param text_color:
    :param icon:
    :param font:
    :param no_titlebar:
    :param grab_anywhere:
    :param keep_on_top:
    :param location:
    :return: Text entered or None if window was closed
    """

    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color, font=font)],
              [InputText(default_text=default_text, size=size, key='_INPUT_', password_char=password_char)],
              [CloseButton('Ok', size=(60, 20), bind_return_key=True), CloseButton('Cancel', size=(60, 20))]]

    _title = title if title is not None else message

    window = Window(title=_title, layout=layout, icon=icon, auto_size_text=True, button_color=button_color, no_titlebar=no_titlebar,
                    background_color=background_color, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    button, values = window.Read()
    window.Close()
    if button != 'Ok':
        return None
    else:
        path = values['_INPUT_']
        return path




# ------------------------ PEP8-ify The SDK ------------------------#
change_look_and_feel = ChangeLookAndFeel
easy_print = EasyPrint
easy_print_close = EasyPrintClose
fill_form_with_values = FillFormWithValues
get_complimentary_hex = GetComplimentaryHex
list_of_look_and_feel_values = ListOfLookAndFeelValues
obj_to_string = ObjToString
obj_to_string_single_obj = ObjToStringSingleObj
one_line_progress_meter = OneLineProgressMeter
one_line_progress_meter_cancel = OneLineProgressMeterCancel
popup = Popup
popup_annoying = PopupAnnoying
popup_auto_close = PopupAutoClose
popup_cancel = PopupCancel
popup_error = PopupError
popup_get_file = PopupGetFile
popup_get_folder = PopupGetFolder
popup_get_text = PopupGetText
popup_no_border = PopupNoBorder
popup_no_buttons = PopupNoButtons
popup_no_frame = PopupNoFrame
popup_no_titlebar = PopupNoTitlebar
popup_no_wait = PopupNoWait
popup_non_blocking = PopupNonBlocking
popup_ok = PopupOK
popup_ok_cancel = PopupOKCancel
popup_quick = PopupQuick
popup_quick_message = PopupQuickMessage
popup_scrolled = PopupScrolled
popup_timed = PopupTimed
popup_yes_no = PopupYesNo
print_close = PrintClose
scrolled_text_box = ScrolledTextBox
set_global_icon = SetGlobalIcon
set_options = SetOptions
timer_start = TimerStart
timer_stop = TimerStop





"""
                       d8b          
                       Y8P          

88888b.d88b.   8888b.  888 88888b.  
888 "888 "88b     "88b 888 888 "88b 
888  888  888 .d888888 888 888  888 
888  888  888 888  888 888 888  888 
888  888  888 "Y888888 888 888  888 

"""


def main():
    ChangeLookAndFeel('Light Brown 11')

    layout = [
              [Text('Welcome to PySimpleGUI!', font='Arial 15', text_color='red')],
              [Text('You are running version {}'.format(version), font='Arial 20', text_color='red')],
              [Text('You should be importing this module rather than running it', justification='l', size=(50, 1))],
              [Text('Here is your sample input window....')],
              [InputText('Source', focus=True, size_px=(200,80)), FileBrowse()],
              [InputText('Dest'), FolderBrowse()],
              [Checkbox('Checkbox 1', size=(15,1)), Checkbox('Checkbox 2')],
              [Radio('Radio 1', 'group', size=(15,1)), Radio('Radio 2', 'group')],
              [Multiline('Multiline Input', do_not_clear=True, size=(40,4), enable_events=True)],

              [MultilineOutput('Multiline Output', size=(40,5), text_color='blue')],
              [Combo(values=['Combo 1', 'Combo 2', 'Combo 3'], default_value='Combo 2', key='_COMBO_',
                        enable_events=True, readonly=False, tooltip='Combo box', disabled=False, font='Courier 18',
                        size=(12, 1))],
              [Spin(values=['Spin a', 'Spin b', 'Spin c'], font='ANY 15', key='_SPIN_', size=(10, 1), enable_events=True)],
              [Button('Ok'), Button('Exit')]]

    window = Window('Demo window..', layout,
                    # default_element_size=(35,1),
                    auto_size_text=True,
                    auto_size_buttons=True,
                    no_titlebar=False,
                    disable_close=False,
                    disable_minimize=True,
                    grab_anywhere=True,
                    )

    while True:
        event, values = window.Read()
        print(event, values)

        if event in (None, 'Exit'):
            break
    window.Close()


if __name__ == '__main__':
    main()
    sys.exit(69)
