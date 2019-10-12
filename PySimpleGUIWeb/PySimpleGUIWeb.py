#usr/bin/python3

version = __version__ = "0.31.0.8 Unreleased No flicker, fixed multiline not in values"

import sys
import datetime
import textwrap
import pickle
import calendar
import threading
from queue import Queue
import remi
import logging
import traceback
import os
import base64, binascii
import mimetypes

from typing import List, Any, Union, Tuple, Dict    # For doing types in comments


try:
    from io import StringIO
except:
    from cStringIO import StringIO

g_time_start = 0
g_time_end = 0
g_time_delta = 0

import time


def TimerStart():
    global g_time_start

    g_time_start = time.time()


def TimerStop():
    global g_time_delta, g_time_end

    g_time_end = time.time()
    g_time_delta = g_time_end - g_time_start
    print(g_time_delta*1000)

######           #####                                       #####   #     #  ###  #     #
#     #  #   #  #     #  #  #    #  #####   #       ######  #     #  #     #   #   #  #  #  ######  #####
#     #   # #   #        #  ##  ##  #    #  #       #       #        #     #   #   #  #  #  #       #    #
######     #     #####   #  # ## #  #    #  #       #####   #  ####  #     #   #   #  #  #  #####   #####
#          #          #  #  #    #  #####   #       #       #     #  #     #   #   #  #  #  #       #    #
#          #    #     #  #  #    #  #       #       #       #     #  #     #   #   #  #  #  #       #    #
#          #     #####   #  #    #  #       ######  ######   #####    #####   ###   ## ##   ######  #####

"""
    Welcome to the "core" PySimpleGUIWeb code....
    
    This special port of the PySimpleGUI SDK to the browser is made possible by the magic of Remi 
    
    https://github.com/dddomodossola/remi 
    
    To be clear, PySimpleGUI would not be able to run in a web browser without this important GUI Framework
    It may not be as widely known at tkinter or Qt, but it should be.  Just as those are the best of the desktop
    GUI frameworks, Remi is THE framework for doing Web Page GUIs in Python.  Nothing else like it exists.                                       
    
          :::::::::       ::::::::::         :::   :::       ::::::::::: 
         :+:    :+:      :+:               :+:+: :+:+:          :+:      
        +:+    +:+      +:+              +:+ +:+:+ +:+         +:+       
       +#++:++#:       +#++:++#         +#+  +:+  +#+         +#+        
      +#+    +#+      +#+              +#+       +#+         +#+         
     #+#    #+#      #+#              #+#       #+#         #+#          
    ###    ###      ##########       ###       ###     ###########       

"""

# Because looks matter...
DEFAULT_BASE64_ICON = b'iVBORw0KGgoAAAANSUhEUgAAACEAAAAgCAMAAACrZuH4AAAABGdBTUEAALGPC/xhBQAAAwBQTFRFAAAAMGmYMGqZMWqaMmubMmycM22dNGuZNm2bNm6bNG2dN26cNG6dNG6eNW+fN3CfOHCeOXGfNXCgNnGhN3KiOHOjOXSjOHSkOnWmOnamOnanPHSiPXakPnalO3eoPnimO3ioPHioPHmpPHmqPXqqPnurPnusPnytP3yuQHimQnurQn2sQH2uQX6uQH6vR32qRn+sSXujSHynTH2mTn+nSX6pQH6wTIGsTYKuTYSvQoCxQoCyRIK0R4S1RYS2Roa4SIe4SIe6SIi7Soq7SYm8SYq8Sou+TY2/UYStUYWvVIWtUYeyVoewUIi0VIizUI6+Vo+8WImxXJG5YI2xZI+xZ5CzZJC0ZpG1b5a3apW4aZm/cZi4dJ2/eJ69fJ+9XZfEZZnCZJzHaZ/Jdp/AeKTI/tM8/9Q7/9Q8/9Q9/9Q+/tQ//9VA/9ZA/9ZB/9ZC/9dD/9ZE/tdJ/9dK/9hF/9hG/9hH/9hI/9hJ/9hK/9lL/9pK/9pL/thO/9pM/9pN/9tO/9tP/9xP/tpR/9xQ/9xR/9xS/9xT/91U/91V/t1W/95W/95X/95Y/95Z/99a/99b/txf/txh/txk/t5l/t1q/t5v/+Bb/+Bc/+Bd/+Be/+Bf/+Bg/+Fh/+Fi/+Jh/+Ji/uJk/uJl/+Jm/+Rm/uJo/+Ro/+Rr/+Zr/+Vs/+Vu/+Zs/+Zu/uF0/uVw/+dw/+dz/+d2/uB5/uB6/uJ9/uR7/uR+/uV//+hx/+hy/+h0/+h2/+l4/+l7/+h8gKXDg6vLgazOhKzMiqrEj6/KhK/Qka/Hk7HJlLHJlLPMmLTLmbbOkLXSmLvXn77XoLrPpr/Tn8DaocLdpcHYrcjdssfZus/g/uOC/uOH/uaB/uWE/uaF/uWK/+qA/uqH/uqI/uuN/uyM/ueS/ueW/ueY/umQ/uqQ/uuS/uuW/uyU/uyX/uqa/uue/uye/uyf/u6f/uyq/u+r/u+t/vCm/vCp/vCu/vCy/vC2/vK2/vO8/vO/wtTjwtXlzdrl/vTA/vPQAAAAiNpY5gAAAQB0Uk5T////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////AFP3ByUAAAAJcEhZcwAAFw8AABcPASe7rwsAAAAYdEVYdFNvZnR3YXJlAHBhaW50Lm5ldCA0LjEuMWMqnEsAAAKUSURBVDhPhdB3WE1xHMdxt5JV0dANoUiyd8kqkey996xclUuTlEKidO3qVnTbhIyMW/bee5NskjJLmR/f3++cK/94vP76Ps/n/Zx7z6mE/6koJowcK154vvHOL/GsKCZXkUgkWlf4vWGWq5tsDz+JWIzSokAiqXGe7nWu3HxhEYof7fhOqp1GtptQuMruVhQdxZ05U5G47tYUHbQ4oah6Fg9Z4ubm7i57JhQjdHS0RSzUPoG17u6zZTKZh8c8XlytqW9YWUOH1LqFOZ6enl5ec+XybFb0rweM1tPTM6yuq6vLs0lYJJfLvb19fHwDWGF0jh5lYNAe4/QFemOwxtfXz8/fPyBgwVMqzAcCF4ybAZ2MRCexJGBhYGBQUHDw4u1UHDG1G2ZqB/Q1MTHmzAE+kpCwL1RghlTaBt/6SaXS2kx9YH1IaOjSZST8vfA9JtoDnSngGgL7wkg4WVkofA9mcF1Sx8zMzBK4v3wFiYiMVLxlEy9u21syFhYNmgN7IyJXEYViNZvEYoCVVWOmUVvgQVSUQqGIjolRFvOAFd8HWVs34VoA+6OjY2JjY5Vxm4BC1UuhGG5jY9OUaQXci1MqlfHx8YmqjyhOViW9ZsUN29akJRmPFwkJCZsTSXIpilJffXiTzorLXYgtcxRJKpUqKTklJQ0oSt9FP/EonxVdNY4jla1kK4q2ZB6mIr+AipvduzFUzMSOtLT09IyMzMxtJKug/F0u/6dTexAWDcXXLGEjapKjfsILOLKEuYiSnTQeYCt3UHhbwEHjGMrETfBJU5zq5dSTcXC8hLJccSWP2cgLXHPu7cQNAcpyxF1dyjehAKb0cSYUAOXCUw6V8OFPgevTXFymC+fPPLU677Nw/1X8A/AbfAKGulaqFlIAAAAASUVORK5CYII='



# ----====----====----==== Constants the user CAN safely change ====----====----====----#
DEFAULT_WINDOW_ICON = 'default_icon.ico'
DEFAULT_ELEMENT_SIZE = (250, 26)  # In pixels
DEFAULT_BUTTON_ELEMENT_SIZE = (10, 1)  # In CHARACTERS
DEFAULT_MARGINS = (10, 5)  # Margins for each LEFT/RIGHT margin is first term
DEFAULT_ELEMENT_PADDING = (5, 3)  # Padding between elements (row, col) in pixels
DEFAULT_AUTOSIZE_TEXT = True
DEFAULT_AUTOSIZE_BUTTONS = True
DEFAULT_FONT = ("Helvetica", 15)
DEFAULT_TEXT_JUSTIFICATION = 'left'
DEFAULT_BORDER_WIDTH = 1
DEFAULT_AUTOCLOSE_TIME = 3  # time in seconds to show an autoclose form
DEFAULT_DEBUG_WINDOW_SIZE = (80, 20)
DEFAULT_OUTPUT_ELEMENT_SIZE = (40, 10)
DEFAULT_WINDOW_LOCATION = (None, None)
MAX_SCROLLED_TEXT_BOX_HEIGHT = 50
DEFAULT_TOOLTIP_TIME = 400

DEFAULT_PIXELS_TO_CHARS_SCALING = (10,26)      # 1 character represents x by y pixels
DEFAULT_PIXEL_TO_CHARS_CUTOFF = 20             # number of chars that triggers using pixels instead of chars

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
DEFAULT_PROGRESS_BAR_SIZE = (25, 20)  # Size of Progress Bar (characters for length, pixels for width)
DEFAULT_PROGRESS_BAR_BORDER_WIDTH = 1
DEFAULT_PROGRESS_BAR_RELIEF = RELIEF_GROOVE
PROGRESS_BAR_STYLES = ('default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative')
DEFAULT_PROGRESS_BAR_STYLE = 'default'
DEFAULT_METER_ORIENTATION = 'horizontal'
DEFAULT_SLIDER_ORIENTATION = 'vertical'
DEFAULT_SLIDER_BORDER_WIDTH = 1
DEFAULT_SLIDER_RELIEF = 00000
DEFAULT_FRAME_RELIEF = 00000


DEFAULT_LISTBOX_SELECT_MODE = 'extended'
SELECT_MODE_MULTIPLE = 'multiple'
LISTBOX_SELECT_MODE_MULTIPLE = 'multiple'
SELECT_MODE_BROWSE = 'browse'
LISTBOX_SELECT_MODE_BROWSE = 'browse'
SELECT_MODE_EXTENDED = 'extended'
LISTBOX_SELECT_MODE_EXTENDED = 'extended'
SELECT_MODE_SINGLE = 'single'
LISTBOX_SELECT_MODE_SINGLE = 'single'
SELECT_MODE_CONTIGUOUS = 'contiguous'
LISTBOX_SELECT_MODE_CONTIGUOUS = 'contiguous'

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

# MENU Constants, can be changed by user if desired
MENU_DISABLED_CHARACTER = '!'
MENU_KEY_SEPARATOR = '::'




# a shameful global variable. This represents the top-level window information. Needed because opening a second window is different than opening the first.
class MyWindows():
    def __init__(self):
        self._NumOpenWindows = 0
        self.user_defined_icon = None
        self.hidden_master_root = None

    def Decrement(self):
        self._NumOpenWindows -= 1 * (self._NumOpenWindows != 0)  # decrement if not 0
        # print('---- DECREMENTING Num Open Windows = {} ---'.format(self._NumOpenWindows))

    def Increment(self):
        self._NumOpenWindows += 1
        # print('++++ INCREMENTING Num Open Windows = {} ++++'.format(self._NumOpenWindows))


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
# Was enum previously ButtonType(Enum):
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
# These used to be enums ElementType(Enum):
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
# ------------------------------------------------------------------------- #
#                       Element CLASS                                       #
# ------------------------------------------------------------------------- #
class Element():
    def __init__(self, elem_type, size=(None, None), auto_size_text=None, font=None, background_color=None, text_color=None,
                 key=None, pad=None, tooltip=None, visible=True, size_px=(None, None)):

        if elem_type != ELEM_TYPE_GRAPH:
            self.Size = convert_tkinter_size_to_Wx(size)
        else:
            self.Size = size
        if size_px != (None, None):
            self.Size = size_px
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


    # -------------------------  REMI CHANGED CALLBACK -----------------------
    # called when a widget has changed and the element has events enabled
    def _ChangedCallback(self, widget, *args):
        # type: (Element, remi.Widget, Any) -> None
        # print(f'Callback {args}')
        self.ParentForm.LastButtonClicked = self.Key if self.Key is not None else ''
        self.ParentForm.MessageQueue.put(self.ParentForm.LastButtonClicked)

    def Update(self, widget, background_color=None, text_color=None, font=None, visible=None, disabled=None, tooltip=None):
        if font is not None:
            font_info = font_parse_string(font)  # family, point size, other
            widget.style['font-family'] = font_info[0]
            widget.style['font-size'] = '{}px'.format(font_info[1])

        if background_color not in (None, COLOR_SYSTEM_DEFAULT):
            widget.style['background-color'] = background_color
        if text_color not in (None, COLOR_SYSTEM_DEFAULT):
            widget.style['color'] = text_color

        if disabled:
            widget.set_enabled(False)
        elif disabled is False:
            widget.set_enabled(True)
        if visible is False:
            widget.attributes['hidden'] = 'true'
        elif visible is True:
            del(widget.attributes['hidden'])
        if tooltip is not None:
            widget.attributes['title'] = tooltip


        # if font:
        #     widget.SetFont(font_to_wx_font(font))
        # if text_color not in (None, COLOR_SYSTEM_DEFAULT):
        #     widget.SetForegroundColour(text_color)
        # if background_color not in (None, COLOR_SYSTEM_DEFAULT):
        #     widget.SetBackgroundColour(background_color)
        # if visible is True:
        #     widget.Show()
        #     self.ParentForm.VisibilityChanged()
        # elif visible is False:
        #     widget.Hide()
        #     self.ParentForm.VisibilityChanged()
        # if disabled:
        #     widget.Enable(False)
        # elif disabled is False:
        #     widget.Enable(True)
        # if tooltip is not None:
        #     widget.SetToolTip(tooltip)
        if visible is False:
            widget.attributes['hidden'] = 'true'
        elif visible is True:
            del(widget.attributes['hidden'])


    def __call__(self, *args, **kwargs):
        """
        Makes it possible to "call" an already existing element.  When you do make the "call", it actually calls
        the Update method for the element.
        Example:    If this text element was in your layout:
                    sg.Text('foo', key='T')
                    Then you can call the Update method for that element by writing:
                    window.FindElement('T')('new text value')

        :param args:
        :param kwargs:
        :return:
        """
        return self.Update(*args, **kwargs)


# ---------------------------------------------------------------------- #
#                           Input Class                                  #
# ---------------------------------------------------------------------- #
class InputText(Element):
    def __init__(self, default_text='', size=(None, None), disabled=False, password_char='',
                 justification=None, background_color=None, text_color=None, font=None, tooltip=None,
                 change_submits=False, enable_events=False,
                 do_not_clear=True, key=None, focus=False, pad=None, visible=True, size_px=(None, None)):
        '''
        Input a line of text Element
        :param default_text: Default value to display
        :param size: Size of field in characters
        :param password_char: If non-blank, will display this character for every character typed
        :param background_color: Color for Element. Text or RGB Hex
        '''
        self.DefaultText = default_text
        self.PasswordCharacter = password_char
        bg = background_color if background_color is not None else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Focus = focus
        self.do_not_clear = do_not_clear
        self.Justification = justification or 'left'
        self.Disabled = disabled
        self.ChangeSubmits = change_submits or enable_events
        self.QT_QLineEdit = None
        self.ValueWasChanged = False
        self.Widget = None  # type: remi.gui.TextInput
        super().__init__(ELEM_TYPE_INPUT_TEXT, size=size, background_color=bg, text_color=fg, key=key, pad=pad,
                         font=font, tooltip=tooltip, visible=visible, size_px=size_px)

    def _InputTextCallback(self,widget, key, keycode, ctrl, shift, alt):
        # print(f'text widget value = {widget.get_value()}')
        # widget.set_value('')
        # widget.set_value(value)
        self.ParentForm.LastButtonClicked = key
        self.ParentForm.MessageQueue.put(self.ParentForm.LastButtonClicked)
        widget.set_value(widget.get_value()+key)
        return (key, keycode, ctrl, shift, alt)

    def Update(self, value=None, disabled=None, select=None, background_color=None, text_color=None, font=None, visible=None):
        if value is not None:
            self.Widget.set_value(str(value))
        if disabled is True:
            self.Widget.set_enabled(False)
        elif disabled is False:
            self.Widget.set_enabled(True)

    def Get(self):
        return self.Widget.get_value()


    get = Get
    update = Update

    class TextInput_raw_onkeyup(remi.gui.TextInput):
        @remi.gui.decorate_set_on_listener("(self, emitter, key, keycode, ctrl, shift, alt)")
        @remi.gui.decorate_event_js("""var params={};params['key']=event.key;
                params['keycode']=(event.which||event.keyCode);
                params['ctrl']=event.ctrlKey;
                params['shift']=event.shiftKey;
                params['alt']=event.altKey;
                sendCallbackParam('%(emitter_identifier)s','%(event_name)s',params);
                event.stopPropagation();event.preventDefault();return false;""")
        def onkeyup(self, key, keycode, ctrl, shift, alt):
            return (key, keycode, ctrl, shift, alt)

        @remi.gui.decorate_set_on_listener("(self, emitter, key, keycode, ctrl, shift, alt)")
        @remi.gui.decorate_event_js("""var params={};params['key']=event.key;
                params['keycode']=(event.which||event.keyCode);
                params['ctrl']=event.ctrlKey;
                params['shift']=event.shiftKey;
                params['alt']=event.altKey;
                sendCallbackParam('%(emitter_identifier)s','%(event_name)s',params);
                event.stopPropagation();event.preventDefault();return false;""")
        def onkeydown(self, key, keycode, ctrl, shift, alt):
            return (key, keycode, ctrl, shift, alt)


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
        self.Values = [str(v) for v in values]
        self.DefaultValue = default_value
        self.ChangeSubmits = change_submits or enable_events
        # self.InitializeAsDisabled = disabled
        self.Disabled = disabled
        self.Readonly = readonly
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.VisibleItems = visible_items
        self.AutoComplete = auto_complete
        self.Widget = None          # type: remi.gui.DropDown
        super().__init__(ELEM_TYPE_INPUT_COMBO, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, size_px=size_px)



    def Update(self, value=None, values=None, set_to_index=None, disabled=None, readonly=None,  background_color=None, text_color=None, font=None, visible=None):
        if values is not None:
            self.Widget.empty()
            for i, item in enumerate(values):
                self.Widget.append(value=item, key=str(i))
        if value:
            self.Widget.select_by_value(value)
        if set_to_index is not None:
            try:            # just in case a bad index is passed in
                self.Widget.select_by_key(str(set_to_index))
            except:
                pass

        super().Update(self.Widget, background_color=background_color, text_color=text_color, font=font, visible=visible, disabled=disabled)

    update = Update


# -------------------------  INPUT COMBO Element lazy functions  ------------------------- #
InputCombo = Combo
DropDown = Combo
Drop = Combo


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



# -------------------------  OPTION MENU Element lazy functions  ------------------------- #
InputOptionMenu = OptionMenu



# ---------------------------------------------------------------------- #
#                           Listbox                                      #
# ---------------------------------------------------------------------- #
class Listbox(Element):
    def __init__(self, values, default_values=None, select_mode=None, change_submits=False, enable_events=False, bind_return_key=False, size=(None, None), disabled=False, auto_size_text=None, font=None, background_color=None, text_color=None, key=None, pad=None, tooltip=None, visible=True, size_px=(None,None)):
        """

        :param values:
        :param default_values:
        :param select_mode:
        :param change_submits:
        :param enable_events:
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
        :param visible:
        :param size_px:
        """
        self.Values = values
        self.DefaultValues = default_values
        self.TKListbox = None
        self.ChangeSubmits = change_submits or enable_events
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
        elif select_mode == LISTBOX_SELECT_MODE_CONTIGUOUS:
            self.SelectMode = SELECT_MODE_CONTIGUOUS
        else:
            self.SelectMode = DEFAULT_LISTBOX_SELECT_MODE
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Widget = None          # type: remi.gui.ListView
        tsize = size                # convert tkinter size to pixels
        if size[0] is not None and size[0] < 100:
            tsize = size[0]*DEFAULT_PIXELS_TO_CHARS_SCALING[0], size[1]*DEFAULT_PIXELS_TO_CHARS_SCALING[1]

        super().__init__(ELEM_TYPE_INPUT_LISTBOX, size=tsize, auto_size_text=auto_size_text, font=font,
                         background_color=bg, text_color=fg, key=key, pad=pad, tooltip=tooltip, visible=visible, size_px=size_px)

    def Update(self, values=None, disabled=None, set_to_index=None,background_color=None, text_color=None, font=None, visible=None):
        if values is not None:
            self.Values = values
            self.Widget.empty()
            for item in values:
                self.Widget.append(remi.gui.ListItem(item))
        # if disabled == True:
        #     self.QT_ListWidget.setDisabled(True)
        # elif disabled == False:
        #     self.QT_ListWidget.setDisabled(False)
        # if set_to_index is not None:
        #     self.QT_ListWidget.setCurrentRow(set_to_index)
        super().Update(self.Widget, background_color=background_color, text_color=text_color, font=font, visible=visible, disabled=disabled)

        return

    # def SetValue(self, values):
    #     # for index, item in enumerate(self.Values):
    #     for index, value in enumerate(self.Values):
    #         item = self.QT_ListWidget.item(index)
    #         if value in values:
    #             self.QT_ListWidget.setItemSelected(item, True)


    def GetListValues(self):
        return self.Values

    get_list_values = GetListValues
    update = Update


# ---------------------------------------------------------------------- #
#                           Radio                                        #
# ---------------------------------------------------------------------- #
class Radio(Element):
    def __init__(self, text, group_id, default=False, disabled=False, size=(None, None), auto_size_text=None,
                 background_color=None, text_color=None, font=None, key=None, pad=None, tooltip=None,
                 change_submits=False):
        '''
        Radio Button Element
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
        '''
        self.InitialState = default
        self.Text = text
        self.TKRadio = None
        self.GroupID = group_id
        self.Value = None
        self.Disabled = disabled
        self.TextColor = text_color or DEFAULT_TEXT_COLOR
        self.ChangeSubmits = change_submits

        print('*** WARNING - Radio Buttons are not yet available on PySimpleGUIWeb ***')

        super().__init__(ELEM_TYPE_INPUT_RADIO, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip)

    def Update(self, value=None, disabled=None):
        print('*** NOT IMPLEMENTED ***')
        location = EncodeRadioRowCol(self.Position[0], self.Position[1])
        if value is not None:
            try:
                self.TKIntVar.set(location)
            except:
                pass
            self.InitialState = value
        if disabled == True:
            self.TKRadio['state'] = 'disabled'
        elif disabled == False:
            self.TKRadio['state'] = 'normal'

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
        self.Disabled = disabled
        self.TextColor = text_color if text_color else DEFAULT_TEXT_COLOR
        self.ChangeSubmits = change_submits or enable_events
        self.Widget = None      # type: remi.gui.CheckBox

        super().__init__(ELEM_TYPE_INPUT_CHECKBOX, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip, visible=visible, size_px=size_px)

    def _ChangedCallback(self, widget, value):
        # type: (remi.Widget, Any) -> None
        # print(f'text widget value = {widget.get_value()}')
        self.ParentForm.LastButtonClicked = self.Key
        self.ParentForm.MessageQueue.put(self.ParentForm.LastButtonClicked)


    def Get(self):
        return self.Widget.get_value()

    def Update(self, value=None, disabled=None):
        if value is not None:
            self.Widget.set_value(value)
        if disabled == True:
            self.Widget.set_enabled(False)
        elif disabled == False:
            self.Widget.set_enabled(True)

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
    def __init__(self, values, initial_value=None, disabled=False, change_submits=False,  enable_events=False, size=(None, None), readonly=True, auto_size_text=None, font=None, background_color=None, text_color=None, key=None, pad=None,
                 tooltip=None, visible=True, size_px=(None,None)):
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
        self.CurrentValue = self.DefaultValue
        self.ReadOnly = readonly
        self.Widget = None      # type: remi.gui.SpinBox
        super().__init__(ELEM_TYPE_INPUT_SPIN, size, auto_size_text, font=font, background_color=bg, text_color=fg,
                         key=key, pad=pad, tooltip=tooltip, visible=visible, size_px=size_px)
        return


    def Update(self, value=None, values=None, disabled=None, background_color=None, text_color=None, font=None, visible=None):
        if value is not None:
            self.Widget.set_value(value)
        super().Update(self.Widget, background_color=background_color, text_color=text_color, font=font,visible=visible)

    def Get(self):
        return self.Widget.get_value()

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
        if size[0] is not None and size[0] < 100:
            size = size[0]*DEFAULT_PIXELS_TO_CHARS_SCALING[0], size[1]*DEFAULT_PIXELS_TO_CHARS_SCALING[1]
        self.Widget = None      # type: remi.gui.TextInput

        super().__init__(ELEM_TYPE_INPUT_MULTILINE, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, size_px=size_px)
        return

    def _InputTextCallback(self, widget:remi.Widget, value, keycode):
        # print(f'text widget value = {widget.get_value()}')
        self.ParentForm.LastButtonClicked = chr(int(keycode))
        self.ParentForm.MessageQueue.put(self.ParentForm.LastButtonClicked)

    def Update(self, value=None, disabled=None, append=False, background_color=None, text_color=None, font=None, visible=None):
            if value is not None and not append:
                self.Widget.set_value(value)
            elif value is not None and append:
                text = self.Widget.get_value() + str(value)
                self.Widget.set_value(text)
            # if background_color is not None:
            #     self.WxTextCtrl.SetBackgroundColour(background_color)
            # if text_color is not None:
            #     self.WxTextCtrl.SetForegroundColour(text_color)
            # if font is not None:
            #     self.WxTextCtrl.SetFont(font)
            # if disabled:
            #     self.WxTextCtrl.Enable(True)
            # elif disabled is False:
            #     self.WxTextCtrl.Enable(False)
            super().Update(self.Widget, background_color=background_color, text_color=text_color, font=font, visible=visible)


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
        tsize = size                # convert tkinter size to pixels
        if size[0] is not None and size[0] < 100:
            tsize = size[0]*DEFAULT_PIXELS_TO_CHARS_SCALING[0], size[1]*DEFAULT_PIXELS_TO_CHARS_SCALING[1]
        self.Widget = None      # type: remi.gui.TextInput
        self.CurrentValue = ''

        super().__init__(ELEM_TYPE_MULTILINE_OUTPUT, size=tsize, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, size_px=size_px)
        return


    def Update(self, value=None, disabled=None, append=False, background_color=None, text_color=None, font=None, visible=None):
        if value is not None and not append:
            self.Widget.set_value(str(value))
        elif value is not None and append:
            self.CurrentValue = self.CurrentValue + '\n' + str(value)
            self.Widget.set_value(self.CurrentValue)
        if self.Autoscroll:
            app = self.ParentForm.App
            if hasattr(app, "websockets"):
                app.execute_javascript("document.getElementById('%s').scrollTop=%s;" % (
                    self.Widget.identifier, 9999))  # 9999 number of pixel to scroll

        super().Update(self.Widget, background_color=background_color, text_color=text_color, font=font, visible=visible)


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
        self.BorderWidth = border_width if border_width is not None else DEFAULT_BORDER_WIDTH
        self.Disabled = False
        self.Widget = None      #type: remi.gui.Label

        super().__init__(ELEM_TYPE_TEXT, pixelsize, auto_size_text, background_color=bg, font=font if font else DEFAULT_FONT,
                         text_color=self.TextColor, pad=pad, key=key, tooltip=tooltip, size_px=size_px, visible=visible)
        return

    def Update(self, value=None, background_color=None, text_color=None, font=None, visible=None):
        if value is not None:
            self.Widget.set_text(str(value))
        super().Update(self.Widget, background_color=background_color, text_color=text_color, font=font, visible=visible)

    update = Update

# -------------------------  Text Element lazy functions  ------------------------- #
Txt = Text
T = Text



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
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        # fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        fg = text_color if text_color is not None else 'black' if DEFAULT_INPUT_TEXT_COLOR == COLOR_SYSTEM_DEFAULT else DEFAULT_INPUT_TEXT_COLOR
        self.Disabled = disabled
        self.Widget = None      # type: remi.gui.TextInput
        if size_px == (None, None) and size == (None, None):
            size = DEFAULT_OUTPUT_ELEMENT_SIZE
        if size[0] is not None and size[0] < 100:
            size = size[0]*DEFAULT_PIXELS_TO_CHARS_SCALING[0], size[1]*DEFAULT_PIXELS_TO_CHARS_SCALING[1]
        super().__init__(ELEM_TYPE_OUTPUT, size=size, size_px=size_px, visible=visible, background_color=bg, text_color=fg, pad=pad, font=font, tooltip=tooltip, key=key)


    def Update(self, value=None, disabled=None, append=False, background_color=None, text_color=None, font=None, visible=None):
        if value is not None and not append:
            self.Widget.set_value(str(value))
            self.CurrentValue = str(value)
        elif value is not None and append:
            self.CurrentValue = self.CurrentValue + '\n' + str(value)
            self.Widget.set_value(self.CurrentValue)
        # do autoscroll
        app = self.ParentForm.App
        if hasattr(app, "websockets"):
            app.execute_javascript("document.getElementById('%s').scrollTop=%s;" % (
                self.Widget.identifier, 9999))  # 9999 number of pixel to scroll

        super().Update(self.Widget, background_color=background_color, text_color=text_color, font=font, visible=visible)

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
        # self.temp_size = size if size != (NONE, NONE) else
        self.Widget = None          # type: remi.gui.Button
        super().__init__(ELEM_TYPE_BUTTON, size=size, font=font, pad=pad, key=key, tooltip=tooltip, text_color=self.TextColor, background_color=self.BackgroundColor, visible=visible, size_px=size_px)
        return



    # -------  Button Callback  ------- #
    def _ButtonCallBack(self, event):

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
                Window._DecrementOpenCount()
            self.ParentForm._Close()
        elif self.BType == BUTTON_TYPE_READ_FORM:                       # Read Button
            # first, get the results table built
            # modify the Results table in the parent FlexForm object
            # if self.Key is not None:
            #     self.ParentForm.LastButtonClicked = self.Key
            # else:
            #     self.ParentForm.LastButtonClicked = self.ButtonText
            self.ParentForm.FormRemainedOpen = True
            element_callback_quit_mainloop(self)
        elif self.BType == BUTTON_TYPE_CLOSES_WIN_ONLY:  # special kind of button that does not exit main loop
            element_callback_quit_mainloop(self)
            self.ParentForm._Close()
            Window._DecrementOpenCount()
        elif self.BType == BUTTON_TYPE_CALENDAR_CHOOSER:  # this is a return type button so GET RESULTS and destroy window
            should_submit_window = False

        if should_submit_window:
            self.ParentForm.LastButtonClicked = target_element.Key
            self.ParentForm.FormRemainedOpen = True
            self.ParentForm.MessageQueue.put(self.ParentForm.LastButtonClicked)
        return


    def Update(self, text=None, button_color=(None, None), disabled=None, image_data=None, image_filename=None, font=None, visible=None, image_subsample=None, image_size=(None,None)):
        if text is not None:
            self.Widget.set_text(str(text))
        fg, bg = button_color
        if image_data:
            self.Widget.empty()
            simage = SuperImage(image_data)
            if image_size is not (None, None):
                simage.set_size(image_size[0], image_size[1])
            self.Widget.append(simage)
        if image_filename:
            self.Widget.empty()
            simage = SuperImage(image_filename)
            if image_size is not (None, None):
                simage.set_size(image_size[0], image_size[1])
            self.Widget.append(simage)

        super().Update(self.Widget, background_color=bg, text_color=fg, disabled=disabled, font=font, visible=visible)


    def GetText(self):
        return self.Widget.get_text()

    get_text = GetText
    update = Update

# -------------------------  Button lazy functions  ------------------------- #
B = Button
Btn = Button
Butt = Button


def convert_tkinter_filetypes_to_wx(filetypes):
    wx_filetypes = ''
    for item in filetypes:
        filetype = item[0] + ' (' + item[1] + ')|'+ item[1]
        wx_filetypes += filetype
    return wx_filetypes





# ---------------------------------------------------------------------- #
#                           ProgreessBar                                 #
# ---------------------------------------------------------------------- #
class ProgressBar(Element):
    def __init__(self, max_value, orientation=None, size=(None, None), auto_size_text=None, bar_color=(None, None),
                 style=None, border_width=None, relief=None, key=None, pad=None):
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
        self.BarColor = bar_color
        self.BarStyle = style if style else DEFAULT_PROGRESS_BAR_STYLE
        self.BorderWidth = border_width if border_width else DEFAULT_PROGRESS_BAR_BORDER_WIDTH
        self.Relief = relief if relief else DEFAULT_PROGRESS_BAR_RELIEF
        self.BarExpired = False
        super().__init__(ELEM_TYPE_PROGRESS_BAR, size=size, auto_size_text=auto_size_text, key=key, pad=pad)

    # returns False if update failed
    def UpdateBar(self, current_count, max=None):
        print('*** NOT IMPLEMENTED ***')
        return
        if self.ParentForm.TKrootDestroyed:
            return False
        self.TKProgressBar.Update(current_count, max=max)
        try:
            self.ParentForm.TKroot.update()
        except:
            _my_windows.Decrement()
            return False
        return True

    update_bar = UpdateBar

# ---------------------------------------------------------------------- #
#                           Image                                        #
# ---------------------------------------------------------------------- #
class Image(Element):
    def __init__(self, filename=None, data=None, background_color=None, size=(None, None), pad=None, key=None,
                 tooltip=None, right_click_menu=None, visible=True, enable_events=False):
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
        self.Filename = filename if filename else None # note that Remi expects a / at the front of resource files
        self.Data = data
        self.tktext_label = None
        self.BackgroundColor = background_color
        self.Disabled = False
        self.EnableEvents = enable_events
        sz = (0,0) if size == (None, None) else size
        self.Widget = None          #type: SuperImage
        if data is None and filename is None:
            print('* Warning... no image specified in Image Element! *')
        super().__init__(ELEM_TYPE_IMAGE, size=sz, background_color=background_color, pad=pad, key=key,
                         tooltip=tooltip, visible=visible)
        return

    def Update(self, filename=None, data=None, size=(None,None), visible=None):
        if data is not None:
            self.Widget.load(data)
            # decoded = base64.b64decode(data)
            # with open(r'.\decoded.out', 'wb') as f:
            #     f.write(decoded)
            # filename = r'.\decoded.out'
        if filename is not None:
            self.Widget.load(filename)
            # self.Widget.set_image(filename=filename)
        # if size != (None, None):
        #     self.Widget.style['height'] = '{}px'.format(size[1])
        #     self.Widget.style['width'] = '{}px'.format(size[0])
        super().Update(self.Widget,  visible=visible)

    update = Update



# class SuperImageOld(remi.gui.Image):
#     def __init__(self, file_path_name=None, **kwargs):
#         image = file_path_name
#         super(SuperImage, self).__init__(image, **kwargs)
#
#         self.imagedata = None
#         self.mimetype = None
#         self.encoding = None
#         if image is None:
#             return
#         self.load(image)
#
#     def load(self, file_path_name):
#         if type(file_path_name) is bytes or len(file_path_name) > 200:
#             try:
#                 self.imagedata = base64.b64decode(file_path_name, validate=True)
#             except binascii.Error:
#                 self.imagedata = file_path_name
#         else:
#             self.mimetype, self.encoding = mimetypes.guess_type(file_path_name)
#             with open(file_path_name, 'rb') as f:
#                 self.imagedata = f.read()
#         self.refresh()
#
#     def refresh(self):
#         i = int(time.time() * 1e6)
#         self.attributes['src'] = "/%s/get_image_data?update_index=%d" % (id(self), i)
#
#     def get_image_data(self, update_index):
#         headers = {'Content-type': self.mimetype if self.mimetype else 'application/octet-stream'}
#         return [self.imagedata, headers]

class SuperImage(remi.gui.Image):
    def __init__(self, file_path_name=None, **kwargs):
        """
        This new app_instance variable is causing lots of problems.  I do not know the value of the App
        when I create this image.
        :param app_instance:
        :param file_path_name:
        :param kwargs:
        """
        # self.app_instance = app_instance
        image = file_path_name
        super(SuperImage, self).__init__(image, **kwargs)

        self.imagedata = None
        self.mimetype = None
        self.encoding = None
        if not image: return
        self.load(image)

    def load(self, file_path_name):
        if type(file_path_name) is bytes or len(file_path_name) > 200:
            print("image data")
            # self.mimetype = 'image/png'
            self.imagedata = file_path_name #base64.b64decode(file_path_name)
            # self.imagedata = base64.b64decode(file_path_name, validate=True)
        else:
            self.mimetype, self.encoding = mimetypes.guess_type(file_path_name)
            with open(file_path_name, 'rb') as f:
                self.imagedata = f.read()
        self.refresh()

    def refresh(self):
        # print("refresh")
        i = int(time.time() * 1e6)
        # self.app_instance.execute_javascript("""
        if Window.App is not None:
            Window.App.execute_javascript("""
                var url = '/%(id)s/get_image_data?update_index=%(frame_index)s';
                var xhr = new XMLHttpRequest();
                xhr.open('GET', url, true);
                xhr.responseType = 'blob'
                xhr.onload = function(e){
                    var urlCreator = window.URL || window.webkitURL;
                    var imageUrl = urlCreator.createObjectURL(this.response);
                    document.getElementById('%(id)s').src = imageUrl;
                }
                xhr.send();
                """ % {'id': id(self), 'frame_index':i})

    def get_image_data(self, update_index):
        # print("get image data")
        headers = {'Content-type': self.mimetype if self.mimetype else 'application/octet-stream'}
        return [self.imagedata, headers]

# ---------------------------------------------------------------------- #
#                           Graph                                        #
# ---------------------------------------------------------------------- #
class Graph(Element):
    def __init__(self, canvas_size, graph_bottom_left, graph_top_right, background_color=None, pad=None,
                 change_submits=False, drag_submits=False, size_px=(None,None), enable_events=False, key=None, visible=True, disabled=False, tooltip=None):
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
        self.ChangeSubmits = change_submits or enable_events
        self.DragSubmits = drag_submits
        self.ClickPosition = (None, None)
        self.MouseButtonDown = False
        self.Disabled = disabled
        self.Widget = None                  # type: remi.gui.Svg
        self.SvgGroup = None                # type: remi.gui.SvgGroup
        super().__init__(ELEM_TYPE_GRAPH, size=canvas_size, size_px=size_px, visible=visible, background_color=background_color, pad=pad,  tooltip=tooltip, key=key)
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
        x_in, y_in = int(x_in), int(y_in)
        scale_x = (self.CanvasSize[0] - 0) / (self.TopRight[0] - self.BottomLeft[0])
        scale_y = (0 - self.CanvasSize[1]) / (self.TopRight[1] - self.BottomLeft[1])
        new_x = x_in / scale_x + self.BottomLeft[0]
        new_y = (y_in - self.CanvasSize[1]) / scale_y + self.BottomLeft[1]
        return int(new_x), int(new_y)

    def DrawLine(self, point_from, point_to, color='black', width=1):
        if point_from == (None, None) or color is None:
            return
        converted_point_from = self._convert_xy_to_canvas_xy(point_from[0], point_from[1])
        converted_point_to = self._convert_xy_to_canvas_xy(point_to[0], point_to[1])
        if self.Widget is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        line = remi.gui.SvgLine(converted_point_from[0], converted_point_from[1], converted_point_to[0], converted_point_to[1])
        line.set_stroke(width, color)
        self.SvgGroup.append([line,])
        return line

    def DrawPoint(self, point, size=2, color='black'):
        if point == (None, None):
            return
        converted_point = self._convert_xy_to_canvas_xy(point[0], point[1])
        if self.Widget is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        rpoint = remi.gui.SvgCircle(converted_point[0], converted_point[1], size)
        rpoint.set_stroke(size, color)
        rpoint.set_fill(color)
        self.SvgGroup.append([rpoint,])
        return rpoint


    def DrawCircle(self, center_location, radius, fill_color=None, line_color='black'):
        if center_location == (None, None):
            return
        converted_point = self._convert_xy_to_canvas_xy(center_location[0], center_location[1])
        if self.Widget is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        rpoint = remi.gui.SvgCircle(converted_point[0], converted_point[1], radius=radius)
        rpoint.set_fill(fill_color)
        rpoint.set_stroke(color=line_color)
        self.SvgGroup.append([rpoint,])
        return rpoint


    def DrawOval(self, top_left, bottom_right, fill_color=None, line_color=None):
        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        if self.Widget is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return


    # def DrawArc(self, top_left, bottom_right, extent, start_angle, style=None, arc_color='black'):
    #     converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
    #     converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
    #     tkstyle = tk.PIESLICE if style is None else style
    #     if self._TKCanvas2 is None:
    #         print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
    #         print('Call Window.Finalize() prior to this operation')
    #         return None
    #     return

    def DrawRectangle(self, top_left, bottom_right, fill_color=None, line_color='black'):
        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        if self.Widget is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None

        rpoint = remi.gui.SvgRectangle(converted_top_left[0], converted_top_left[1], abs(converted_bottom_right[0]-converted_top_left[0]), abs(converted_top_left[1] - converted_bottom_right[1]))
        rpoint.set_stroke(width=1, color=line_color)
        if fill_color is not None:
            rpoint.set_fill(fill_color)
        else:
            rpoint.set_fill('transparent')
        self.SvgGroup.append([rpoint,])
        return rpoint



    def DrawText(self, text, location, color='black', font=None, angle=0):
        if location == (None, None):
            return
        converted_point = self._convert_xy_to_canvas_xy(location[0], location[1])
        if self.Widget is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None

        rpoint = remi.gui.SvgText(converted_point[0], converted_point[1], text)
        self.SvgGroup.append([rpoint,])
        # self.SvgGroup.redraw()
        return rpoint


    def DrawImage(self, data=None, image_source=None, location=(None, None), size=(100, 100)):
        if location == (None, None):
            return
        if data is not None:
            image_source = data.decode('utf-8') if type(data) is bytes else data
        converted_point = self._convert_xy_to_canvas_xy(location[0], location[1])
        if self.Widget is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None

        rpoint = remi.gui.SvgImage('', converted_point[0], converted_point[0], size[0], size[1])

        if type(image_source) is bytes or len(image_source) > 200:
            rpoint.set_image("data:image/svg;base64,%s"%image_source)
        else:
            mimetype, encoding = mimetypes.guess_type(image_source)
            with open(image_source, 'rb') as f:
                data = f.read()
            b64 = base64.b64encode(data)
            b64_str = b64.decode("utf-8")
            image_string = "data:image/svg;base64,%s"%b64_str
            rpoint.set_image(image_string)
        self.SvgGroup.append([rpoint,])
        rpoint.redraw()
        self.SvgGroup.redraw()
        return rpoint

    def Erase(self):
        if self.Widget is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        self.Widget.empty()
        self.SvgGroup = remi.gui.SvgGroup(self.Size[1],0)
        self.Widget.append(self.SvgGroup)

    def Update(self, background_color):
        if self.Widget is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        if self.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
            self.Widget.style['background-color'] = self.BackgroundColor

    def Move(self, x_direction, y_direction):
        # TODO - IT's still not working yet!  I'm trying!!

        self.MoveFigure(self.SvgGroup, x_direction,y_direction)
        return
        zero_converted = self._convert_xy_to_canvas_xy(0, 0)
        shift_converted = self._convert_xy_to_canvas_xy(x_direction, y_direction)
        shift_amount = (shift_converted[0] - zero_converted[0], shift_converted[1] - zero_converted[1])
        if self.Widget is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        cur_x = float(self.SvgGroup.attributes['cx'])
        cur_y = float(self.SvgGroup.attributes['cy'])
        self.SvgGroup.set_position(cur_x - x_direction,cur_y - y_direction)
        self.SvgGroup.redraw()


    def Relocate(self, x, y):
        shift_converted = self._convert_xy_to_canvas_xy(x, y)
        if self.Widget is None:
            print('*** WARNING - Your figure is None. It most likely means your did not Finalize your Window ***')
            print('Call Window.Finalize() prior to all graph operations')
            return None
        # figure.empty()
        self.SvgGroup.set_position(shift_converted[0], shift_converted[1])
        self.SvgGroup.redraw()


    def MoveFigure(self, figure, x_direction, y_direction):
        figure = figure     # type: remi.gui.SvgCircle
        zero_converted = self._convert_xy_to_canvas_xy(0, 0)
        shift_converted = self._convert_xy_to_canvas_xy(x_direction, y_direction)
        shift_amount = (shift_converted[0] - zero_converted[0], shift_converted[1] - zero_converted[1])
        if figure is None:
            print('*** WARNING - Your figure is None. It most likely means your did not Finalize your Window ***')
            print('Call Window.Finalize() prior to all graph operations')
            return None
        cur_x = float(figure.attributes['x'])
        cur_y = float(figure.attributes['y'])
        figure.set_position(cur_x - x_direction,cur_y - y_direction)
        figure.redraw()

    def RelocateFigure(self, figure, x, y):
        figure = figure     #type: remi.gui.SvgCircle
        zero_converted = self._convert_xy_to_canvas_xy(0, 0)
        shift_converted = self._convert_xy_to_canvas_xy(x, y)
        shift_amount = (shift_converted[0] - zero_converted[0], shift_converted[1] - zero_converted[1])
        if figure is None:
            print('*** WARNING - Your figure is None. It most likely means your did not Finalize your Window ***')
            print('Call Window.Finalize() prior to all graph operations')
            return None
        # figure.empty()
        figure.set_position(shift_converted[0], shift_converted[1])
        figure.redraw()


    def DeleteFigure(self, figure):
        figure = figure     # type: remi.gui.SvgCircle
        if figure is None:
            print('*** WARNING - Your figure is None. It most likely means your did not Finalize your Window ***')
            print('Call Window.Finalize() prior to all graph operations')
            return None
        self.SvgGroup.remove_child(figure)
        del figure




    def _MouseDownCallback(self, widget, x,y, *args):
        # print(f'Mouse down {x,y}')
        self.MouseButtonDown = True

    def _MouseUpCallback(self, widget, x,y, *args):
        self.ClickPosition = self._convert_canvas_xy_to_xy(int(x), int(y))
        self.MouseButtonDown = False
        if self.ChangeSubmits:
            # self.ClickPosition = (None, None)
            self.ParentForm.LastButtonClicked = self.Key if self.Key is not None else ''
            self.ParentForm.MessageQueue.put(self.ParentForm.LastButtonClicked)

    # def ClickCallback(self, emitter, x, y):
    def ClickCallback(self, widget:remi.gui.Svg, *args):
        return
        self.ClickPosition = (None, None)
        self.ParentForm.LastButtonClicked = self.Key if self.Key is not None else ''
        self.ParentForm.MessageQueue.put(self.ParentForm.LastButtonClicked)

    def _DragCallback(self, emitter, x, y):
        if not self.MouseButtonDown:        # only return drag events when mouse is down
            return
        # print(f'In Drag Callback')
        self.ClickPosition = self._convert_canvas_xy_to_xy(x, y)
        # print(f'Position {self.ClickPosition}')
        self.ParentForm.LastButtonClicked = self.Key if self.Key is not None else ''
        self.ParentForm.MessageQueue.put(self.ParentForm.LastButtonClicked)



    click_callback = ClickCallback
    delete_figure = DeleteFigure
    draw_circle = DrawCircle
    draw_image = DrawImage
    draw_line = DrawLine
    draw_oval = DrawOval
    draw_point = DrawPoint
    draw_rectangle = DrawRectangle
    draw_text = DrawText
    erase = Erase
    move = Move
    move_figure = MoveFigure
    relocate = Relocate
    relocate_figure = RelocateFigure
    update = Update


# ---------------------------------------------------------------------- #
#                           Frame                                        #
# ---------------------------------------------------------------------- #
class Frame(Element):
    def __init__(self, title, layout, title_color=None, background_color=None, title_location=None,
                 relief=DEFAULT_FRAME_RELIEF, size=(None, None), font=None, pad=None, border_width=None, key=None,
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
        self.Justification = 'left'

        self.Layout(layout)

        super().__init__(ELEM_TYPE_FRAME, background_color=background_color, text_color=title_color, size=size,
                         font=font, pad=pad, key=key, tooltip=tooltip)
        return

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
            if element.Key is not None:
                self.UseDictionary = True
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    def Layout(self, rows):
        for row in rows:
            self.AddRow(*row)

    def _GetElementAtLocation(self, location):
        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element

    add_row = AddRow
    layout = Layout


# ---------------------------------------------------------------------- #
#                           Separator                                    #
#  Routes stdout, stderr to a scrolled window                            #
# ---------------------------------------------------------------------- #
class VerticalSeparator(Element):
    def __init__(self, pad=None):
        '''
        VerticalSeperator - A separator that spans only 1 row in a vertical fashion
        :param pad:
        '''
        self.Orientation = 'vertical'  # for now only vertical works

        super().__init__(ELEM_TYPE_SEPARATOR, pad=pad)


VSeperator = VerticalSeparator
VSep = VerticalSeparator


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
        self.Justification = 'left'
        self.TabID = None
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.Widget = None          # type: remi.gui.HBox
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

    # def Update(self, disabled=None):  # TODO Disable / enable of tabs is not complete
    #     print('*** Tab.Update is not implemented ***')
    #     return
    #     if disabled is None:
    #         return
    #     self.Disabled = disabled
    #     state = 'disabled' if disabled is True else 'normal'
    #     self.ParentNotebook.tab(self.TabID, state=state)
    #     return self

    def _GetElementAtLocation(self, location):
        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element


# ---------------------------------------------------------------------- #
#                           TabGroup                                     #
# ---------------------------------------------------------------------- #
class TabGroup(Element):
    def __init__(self, layout, tab_location=None, title_color=None, selected_title_color=None, background_color=None,
                 font=None, change_submits=False, enable_events=False,pad=None, border_width=None, theme=None, key=None, tooltip=None, visible=True):
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
        self.Widget = None      # type: remi.gui.TabBox
        self.Justification = 'left'
        self.TabCount = 0
        self.BorderWidth = border_width
        self.Theme = theme
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.ChangeSubmits = enable_events or change_submits
        self.TabLocation = tab_location
        self.Visible = visible
        self.Disabled = False
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
                 border_width=None, relief=None, change_submits=False, enable_events=False, disabled=False, size=(None, None), font=None,
                 background_color=None, text_color=None, key=None, pad=None, tooltip=None, visible=True, size_px=(None,None)):
        """

        :param range:
        :param default_value:
        :param resolution:
        :param tick_interval:
        :param orientation:
        :param border_width:
        :param relief:
        :param change_submits:
        :param enable_events:
        :param disabled:
        :param visible:
        :param size_px:
        """
        self.TKScale = None
        self.Range = (1, 10) if range == (None, None) else range
        self.DefaultValue = self.Range[0] if default_value is None else default_value
        self.Orientation = orientation if orientation else DEFAULT_SLIDER_ORIENTATION
        self.BorderWidth = border_width if border_width else DEFAULT_SLIDER_BORDER_WIDTH
        self.Relief = relief if relief else DEFAULT_SLIDER_RELIEF
        self.Resolution = 1 if resolution is None else resolution
        self.ChangeSubmits = change_submits or enable_events
        self.Disabled = disabled
        self.TickInterval = tick_interval
        temp_size = size
        if temp_size == (None, None):
            temp_size = (200, 20) if self.Orientation.startswith('h') else (200, 20)
        elif size[0] is not None and size[0] < 100:
            temp_size = size[0]*10, size[1]*3
        self.Widget = None      # type: remi.gui.Slider

        super().__init__(ELEM_TYPE_INPUT_SLIDER, size=temp_size, font=font, background_color=background_color,
                         text_color=text_color, key=key, pad=pad, tooltip=tooltip, visible=visible, size_px=size_px)
        return

    def Update(self, value=None, range=(None, None), disabled=None, visible=None):
        if value is not None:
            self.Widget.set_value(value)
            self.DefaultValue = value
        if range != (None, None):
            self.Widget.attributes['min'] = '{}'.format(range[0])
            self.Widget.attributes['max'] = '{}'.format(range[1])
        super().Update(self.Widget, disabled=disabled, visible=visible)

    def _SliderCallback(self, widget:remi.Widget, value):
        self.ParentForm.LastButtonClicked = self.Key if self.Key is not None else ''
        self.ParentForm.MessageQueue.put(self.ParentForm.LastButtonClicked)

    update = Update

#
# ---------------------------------------------------------------------- #
#                           Column                                       #
# ---------------------------------------------------------------------- #
class Column(Element):
    def __init__(self, layout, background_color=None, size=(None, None), pad=None, scrollable=False, vertical_scroll_only=False, justification='left', key=None):
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
        self.TKFrame = None
        self.Scrollable = scrollable
        self.VerticalScrollOnly = vertical_scroll_only
        self.Justification = justification
        # self.ImageFilename = image_filename
        # self.ImageData = image_data
        # self.ImageSize = image_size
        # self.ImageSubsample = image_subsample
        # bg = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR

        self.Layout(layout)

        super().__init__(ELEM_TYPE_COLUMN, background_color=background_color, size=size, pad=pad, key=key)
        return

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
            if element.Key is not None:
                self.UseDictionary = True
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    def Layout(self, rows):
        for row in rows:
            self.AddRow(*row)

    def _GetElementAtLocation(self, location):
        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element

    add_row = AddRow
    layout = Layout


# ---------------------------------------------------------------------- #
#                           Menu                                       #
# ---------------------------------------------------------------------- #
class Menu(Element):
    def __init__(self, menu_definition, background_color=COLOR_SYSTEM_DEFAULT, text_color=None, size=(None, None), tearoff=False, pad=None, key=None, disabled=False, font=None):
        '''
        Menu Element
        :param menu_definition:
        :param background_color:
        :param size:
        :param tearoff:
        :param pad:
        :param key:
        '''
        back_color = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.MenuDefinition = menu_definition
        self.TKMenu = None
        self.Tearoff = tearoff
        self.Widget = None          # type: remi.gui.MenuBar
        self.MenuItemChosen = None
        self.Disabled = disabled

        super().__init__(ELEM_TYPE_MENUBAR, background_color=back_color, text_color=text_color, size=size, pad=pad, key=key, font=font)
        return



    def _ChangedCallbackMenu(self,  widget, *user_data):
        widget = widget     # type: remi.gui.MenuItem
        chosen = user_data[0]
        self.MenuItemChosen = chosen
        self.ParentForm.LastButtonClicked = chosen
        self.ParentForm.MessageQueue.put(chosen)


# ---------------------------------------------------------------------- #
#                           Table                                        #
# ---------------------------------------------------------------------- #
class Table(Element):
    def __init__(self, values, headings=None, visible_column_map=None, col_widths=None, def_col_width=10,
                 auto_size_columns=True, max_col_width=20, select_mode=None, display_row_numbers=False, row_header_text='Row', starting_row_num=0, num_rows=None, row_height=None, font=None, justification='right', text_color=None, background_color=None, alternating_row_color=None, row_colors=None, vertical_scroll_only=True, disabled=False,
                 size=(None, None), change_submits=False, enable_events=False, bind_return_key=False, pad=None, key=None, tooltip=None, right_click_menu=None, visible=True, size_px=(None, None)):
        '''
        Table
        :param values:
        :param headings:
        :param visible_column_map:
        :param col_widths:
        :param def_col_width:
        :param auto_size_columns:
        :param max_col_width:
        :param select_mode:
        :param display_row_numbers:
        :param num_rows:
        :param row_height:
        :param font:
        :param justification:
        :param text_color:
        :param background_color:
        :param alternating_row_color:
        :param size:
        :param change_submits:
        :param enable_events:
        :param bind_return_key:
        :param pad:
        :param key:
        :param tooltip:
        :param right_click_menu:
        :param visible:
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
        self.RowHeight = row_height
        self.TKTreeview = None
        self.AlternatingRowColor = alternating_row_color
        self.VerticalScrollOnly = vertical_scroll_only
        self.SelectedRows = []
        self.ChangeSubmits = change_submits or enable_events
        self.BindReturnKey = bind_return_key
        self.StartingRowNumber = starting_row_num        # When displaying row numbers, where to start
        self.RowHeaderText = row_header_text
        self.RightClickMenu = right_click_menu
        self.RowColors = row_colors
        self.Disabled = disabled
        self.SelectedItem = None
        self.SelectedRow = None
        self.Widget = None                      # type: remi.Table

        super().__init__(ELEM_TYPE_TABLE, text_color=text_color, background_color=background_color, font=font,
                         size=size, pad=pad, key=key, tooltip=tooltip, visible=visible, size_px=size_px)
        return

    def Update(self, values=None):
        print('*** Table Update not yet supported ***')
        return
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


    def _on_table_row_click(self, table, row, item):
        # self.SelectedRow = row          # type: remi.gui.TableRow
        self.SelectedItem = item.get_text()
        index = -1
        # each widget (and specifically in this case the table) has a _render_children_list attribute that
        # is an ordered list of the children keys
        # first, we search for the row in the children dictionary
        for key, value in table.children.items():
            if value == row:
                # if the row is found, we get the index in the ordered list
                index = table._render_children_list.index(key)
                break
        self.SelectedRow = index
        if self.ChangeSubmits:
            self.ParentForm.LastButtonClicked = self.Key if self.Key is not None else ''
            self.ParentForm.MessageQueue.put(self.ParentForm.LastButtonClicked)
        else:
            self.ParentForm.LastButtonClicked = ''




# ---------------------------------------------------------------------- #
#                           Tree                                         #
# ---------------------------------------------------------------------- #
class Tree(Element):
    def __init__(self, data=None, headings=None, visible_column_map=None, col_widths=None, col0_width=10,
                 def_col_width=10, auto_size_columns=True, max_col_width=20, select_mode=None, show_expanded=False,
                 change_submits=False, font=None,
                 justification='right', text_color=None, background_color=None, num_rows=None, pad=None, key=None,
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

        print('*** Tree Element not yet supported ***')

        super().__init__(ELEM_TYPE_TREE, text_color=text_color, background_color=background_color, font=font, pad=pad,
                         key=key, tooltip=tooltip)


    def add_treeview_data(self, node):
        # print(f'Inserting {node.key} under parent {node.parent}')
        if node.key != '':
            self.TKTreeview.insert(node.parent, 'end', node.key, text=node.text, values=node.values,
                                   open=self.ShowExpanded)
        for node in node.children:
            self.add_treeview_data(node)

    def Update(self, values=None, key=None, value=None, text=None):
        print('*** Tree Element not yet supported ***')
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

    insert = Insert

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

    get = Get
    update = Update


# ------------------------------------------------------------------------- #
#                       Window CLASS                                      #
# ------------------------------------------------------------------------- #
class Window:

    _NumOpenWindows = 0
    user_defined_icon = None
    hidden_master_root = None
    QTApplication = None
    active_popups = {}
    highest_level_app = None
    stdout_is_rerouted = False
    stdout_string_io = None
    stdout_location = None
    port_number = 6900
    active_windows = [ ]        # type:  [Window]
    App = None                  # type: remi.App

    def __init__(self, title, layout=None, default_element_size=DEFAULT_ELEMENT_SIZE, default_button_element_size=(None, None),
                 auto_size_text=None, auto_size_buttons=None, location=(None, None), size=(None, None),
                 element_padding=None, button_color=None, font=None,
                 progress_bar_color=(None, None), background_color=None, border_depth=None, auto_close=False,
                 auto_close_duration=None, icon=DEFAULT_BASE64_ICON, force_toplevel=False,
                 alpha_channel=1, return_keyboard_events=False, return_key_down_events=False, use_default_focus=True, text_justification=None,
                 no_titlebar=False, grab_anywhere=False, keep_on_top=False, resizable=True, disable_close=False,
                 disable_minimize=False, background_image=None, finalize=False,
                 web_debug=False, web_ip='0.0.0.0', web_port=0, web_start_browser=True, web_update_interval=.0000001, web_multiple_instance=False ):
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
        self.DefaultElementSize = convert_tkinter_size_to_Wx(default_element_size)
        self.DefaultButtonElementSize = convert_tkinter_size_to_Wx(
            default_button_element_size) if default_button_element_size != (
            None, None) else DEFAULT_BUTTON_ELEMENT_SIZE
        self.Location = location
        self.ButtonColor = button_color if button_color else DEFAULT_BUTTON_COLOR
        self.BackgroundColor = background_color if background_color else DEFAULT_BACKGROUND_COLOR
        self.ParentWindow = None
        self.Font = font if font else DEFAULT_FONT
        self.RadioDict = {}
        self.BorderDepth = border_depth
        self.WindowIcon = icon if icon is not None else Window.user_defined_icon
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
        self.AllKeysDict = {}
        self.LastButtonClicked = None
        self.LastButtonClickedWasRealtime = False
        self.UseDictionary = False
        self.UseDefaultFocus = use_default_focus
        self.ReturnKeyboardEvents = return_keyboard_events
        self.ReturnKeyDownEvents = return_key_down_events
        self.KeyInfoDict = {}
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
        self._Size = size
        self.ElementPadding = element_padding or DEFAULT_ELEMENT_PADDING
        self.FocusElement = None
        self.BackgroundImage = background_image
        self.XFound = False
        self.DisableMinimize = disable_minimize
        self.OutputElementForStdOut = None      # type: Output
        self.Justification = 'left'
        self.IgnoreClose = False
        self.thread_id = None
        self.App = None         # type: Window.MyApp
        self.web_debug = web_debug
        self.web_ip = web_ip
        self.web_port = web_port
        self.web_start_browser = web_start_browser
        self.web_update_interval = web_update_interval
        self.web_multiple_instance = web_multiple_instance
        self.MessageQueue = Queue()
        self.master_widget = None       # type: remi.gui.VBox
        self.UniqueKeyCounter = 0

        if layout is not None:
            self.Layout(layout)
            if finalize:
                self.Finalize()

    @classmethod
    def IncrementOpenCount(self):
        self._NumOpenWindows += 1
        # print('+++++ INCREMENTING Num Open Windows = {} ---'.format(Window._NumOpenWindows))

    @classmethod
    def _DecrementOpenCount(self):
        self._NumOpenWindows -= 1 * (self._NumOpenWindows != 0)  # decrement if not 0
        # print('----- DECREMENTING Num Open Windows = {} ---'.format(Window._NumOpenWindows))

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
        self._BuildKeyDict()
        return self

    def LayoutAndRead(self, rows, non_blocking=False):
        raise DeprecationWarning(
            'LayoutAndRead is no longer supported... change your call to window.Layout(layout).Read()')
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



    def Read(self, timeout=None, timeout_key=TIMEOUT_KEY):
        # if timeout == 0:  # timeout of zero runs the old readnonblocking
        #     event, values = self._ReadNonBlocking()
        #     if event is None:
        #         event = timeout_key
        #     if values is None:
        #         event = None
        #     return event, values  # make event None if values was None and return
        # Read with a timeout
        self.Timeout = timeout
        self.TimeoutKey = timeout_key
        self.NonBlocking = False
        if not self.Shown:
            self.Show()
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
                Window._DecrementOpenCount()
            results = BuildResults(self, False, self)
            if results[0] != None and results[0] != timeout_key:
                return results
            else:
                pass

            # else:
            #     print("** REALTIME PROBLEM FOUND **", results)
        # print('****************** CALLING MESSAGE QUEUE GET ***********************')
        self.CurrentlyRunningMainloop = True
        if timeout is not None:
            try:
                self.LastButtonClicked = self.MessageQueue.get(timeout=(timeout if timeout else .001)/1000)
                # print(f'Got event {self.LastButtonClicked}')
            except:             # timeout
                self.LastButtonClicked = timeout_key
        else:
            self.LastButtonClicked = self.MessageQueue.get()
            # print(f'Got event {self.LastButtonClicked}')
        # print('--------------------- BACK FROM MESSAGE QUEUE GET ----------------------')

        results = BuildResults(self, False, self)
        return results
        # print(f'In main {self.Title}')
        ################################# CALL GUWxTextCtrlI MAINLOOP ############################
        # self.App.MainLoop()
        # self.CurrentlyRunningMainloop = False
        # self.TimerCancelled = True
        # if timer:
        #     timer.Stop()
        # if Window.stdout_is_rerouted:
        #     sys.stdout = Window.stdout_location
        # if self.RootNeedsDestroying:
            # self.LastButtonClicked = None
            # self.App.Close()
            # try:
            #     self.MasterFrame.Close()
            # except:
            #     pass
            # Window._DecrementOpenCount()
        # if form was closed with X
        # if self.LastButtonClicked is None and self.LastKeyboardEvent is None and self.ReturnValues[0] is None:
        #     Window._DecrementOpenCount()
        # Determine return values
        # if self.LastKeyboardEvent is not None or self.LastButtonClicked is not None:
        #     results = BuildResults(self, False, self)
        #     if not self.LastButtonClickedWasRealtime:
        #         self.LastButtonClicked = None
        #     return results
        # else:
        #     if not self.XFound and self.Timeout != 0 and self.Timeout is not None and self.ReturnValues[
        #         0] is None:  # Special Qt case because returning for no reason so fake timeout
        #         self.ReturnValues = self.TimeoutKey, self.ReturnValues[1]  # fake a timeout
        #     elif not self.XFound and self.ReturnValues[
        #         0] is None:  # TODO HIGHLY EXPERIMENTAL... added due to tray icon interaction
        #         print("*** Faking timeout ***")
                # self.ReturnValues = self.TimeoutKey, self.ReturnValues[1]  # fake a timeout
            # return self.ReturnValues

    def _ReadNonBlocking(self):
        if self.TKrootDestroyed:
            return None, None
        if not self.Shown:
            self.Show(non_blocking=True)
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
            pass  # if user has already closed the frame will get an error

        if self.CurrentlyRunningMainloop:
            self.App.ExitMainLoop()

    def on_key_down(self, emitter, key, keycode, ctrl, shift, alt):
        self.LastButtonClicked = 'DOWN'+key
        self.MessageQueue.put(self.LastButtonClicked)
        self.KeyInfoDict =  { 'key':key, 'keycode':keycode, 'ctrl': ctrl, 'shift':shift, 'alt':alt }

    def on_key_up(self, emitter, key, keycode, ctrl, shift, alt):
        self.LastButtonClicked = key
        self.MessageQueue.put(self.LastButtonClicked)
        self.KeyInfoDict =  { 'key':key, 'keycode':keycode, 'ctrl': ctrl, 'shift':shift, 'alt':alt }


    def callback_keyboard_char(self, event):
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
        #         Window._DecrementOpenCount()
        return self

    def Refresh(self):
        # self.QTApplication.processEvents()              # refresh the window
        return self

    def VisibilityChanged(self):
        self.SizeChanged()
        return self

    def Fill(self, values_dict):
        _FillFormWithValues(self, values_dict)
        return self

    def FindElement(self, key, silent_on_error=False):
        try:
            element = self.AllKeysDict[key]
        except KeyError:
            element = None
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

    Element = FindElement  # shortcut function definition

    def _BuildKeyDict(self):
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

    def GetScreenDimensions(self):      # TODO - Not sure what to return so (0,0) for now
        size = (0,0)
        return size

    def Move(self, x, y):
        self.MasterFrame.SetPosition((x, y))

    def Minimize(self):
        self.MasterFrame.Iconize()

    def Maximize(self):
        self.MasterFrame.Maximize()

    def _Close(self):
        if not self.NonBlocking:
            BuildResults(self, False, self)
        if self.TKrootDestroyed:
            return None
        self.TKrootDestroyed = True
        self.RootNeedsDestroying = True
        self.Close()

    def Close(self):
        if len(Window.active_windows) != 0:
            del(Window.active_windows[-1])          # delete current window from active windows
            if len(Window.active_windows) != 0:
                window = Window.active_windows[-1]      # get prior window to change to
                Window.App.set_root_widget(window.master_widget)
            else:
                self.App.close()
                self.App.server.server_starter_instance._alive = False
                self.App.server.server_starter_instance._sserver.shutdown()
            return

        self.App.close()
        self.App.server.server_starter_instance._alive = False
        self.App.server.server_starter_instance._sserver.shutdown()

    CloseNonBlockingForm = Close
    CloseNonBlocking = Close

    def Disable(self):
        self.MasterFrame.Enable(False)

    def Enable(self):
        self.MasterFrame.Enable(True)

    def Hide(self):
        self._Hidden = True
        self.master_widget.attributes['hidden'] = 'true'
        # self.MasterFrame.Hide()
        return

    def UnHide(self):
        if self._Hidden:
            del(self.master_widget.attributes['hidden'])
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
    increment_open_count = IncrementOpenCount
    layout = Layout
    layout_and_read = LayoutAndRead
    layout_and_show = LayoutAndShow
    load_from_disk = LoadFromDisk
    maximize = Maximize
    minimize = Minimize
    move = Move
    num_open_windows = _NumOpenWindows
    read = Read
    reappear = Reappear
    refresh = Refresh
    save_to_disk = SaveToDisk
    set_alpha = SetAlpha
    set_icon = SetIcon
    show = Show
    size = Size
    size_changed = SizeChanged
    un_hide = UnHide
    visibility_changed = VisibilityChanged





    def remi_thread(self):
        logging.getLogger('remi').setLevel(logging.CRITICAL)
        logging.getLogger('remi').disabled = True
        logging.getLogger('remi.server.ws').disabled = True
        logging.getLogger('remi.server').disabled = True
        logging.getLogger('remi.request').disabled = True
        # use this code to start the application instead of the **start** call
        # s = remi.Server(self.MyApp, start=True, title=self.Title, address='0.0.0.0', port=8081, start_browser=True, userdata=(self,),  multiple_instance=False, update_interval=.001)

        # logging.getLogger('remi').setLevel(level=logging.CRITICAL)
        # logging.getLogger('remi').disabled = True
        # logging.disable(logging.CRITICAL)
        # s = remi.server.StandaloneServer(self.MyApp, width=1100, height=600)
        # s.start()
        Window.port_number += 1
        try:
            remi.start(self.MyApp,
                       title=self.Title,
                       debug=self.web_debug,
                       address=self.web_ip,
                       port=self.web_port,
                       multiple_instance=self.web_multiple_instance,
                       start_browser=self.web_start_browser,
                       update_interval=self.web_update_interval, userdata=(self,))

        except:
            print('*** ERROR Caught inside Remi ***')
            print(traceback.format_exc())
        # remi.start(self.MyApp, title=self.Title ,debug=False,  userdata=(self,), standalone=True)  # standalone=True)

        # remi.start(self.MyApp, standalone=True, debug=True, userdata=(self,) )            # Can't do this because of a threading problem
        print('Returned from Remi Start command... now sending None event')

        self.MessageQueue.put(None)     # if returned from start call, then the window has been destroyed and a None event should be generated

    class MyApp(remi.App):
        def __init__(self,*args, userdata2=None):
            # self.window = window    # type:  Window
            # print(args[-1])
            if userdata2 is None:
                userdata = args[-1].userdata
                self.window = userdata[0]       # type: Window
            else:
                self.window = userdata2         # type: Window
            self.master_widget = None
            # print("new App instance %s" % str(id(self)))
            # self.window.App = self
            #Window.App = self
            self.lines_shown = []

            if userdata2 is None:
                # res_path = os.path.dirname(os.path.abspath(__file__))
                # print('res path', res_path)
                super(Window.MyApp, self).__init__(*args,  static_file_path={'C':'c:','c':'c:','D':'d:', 'd':'d:', 'E':'e:', 'e':'e:', 'dot':'.', '.':'.'})

        def _instance(self):
            remi.App._instance(self)
            self.window.App = remi.server.clients[self.session]

        def log_message(self, *args, **kwargs):
            pass

        def idle(self):
            if Window.stdout_is_rerouted:
                Window.stdout_string_io.seek(0)
                lines = Window.stdout_string_io.readlines()
                # lines.reverse()
                # self.window.OutputElementForStdOut.Widget.set_text("".join(lines))
                # self.window.OutputElementForStdOut.Update("".join(lines))
                if lines != self.lines_shown:
                    self.window.OutputElementForStdOut.Update("".join(lines))
                self.lines_shown = lines

        def main(self, name='world'):
            # margin 0px auto allows to center the app to the screen
            # self.master_widget = remi.gui.VBox()
            # self.master_widget.style['justify-content'] = 'flex-start'
            # self.master_widget.style['align-items'] = 'baseline'
            # if self.window.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
            #     self.master_widget.style['background-color'] = self.window.BackgroundColor
            # try:
            #     PackFormIntoFrame(self.window, self.master_widget, self.window)
            # except:
            #     print('* ERROR PACKING FORM *')
            #     print(traceback.format_exc())
            #
            # if self.window.BackgroundImage:
            #     self.master_widget.style['background-image'] = "url('{}')".format('/'+self.window.BackgroundImage)
            #     # print(f'background info',self.master_widget.attributes['background-image'] )
            #
            # if not self.window.DisableClose:
            #     # add the following 3 lines to your app and the on_window_close method to make the console close automatically
            #     tag = remi.gui.Tag(_type='script')
            #     tag.add_child("javascript", """window.onunload=function(e){sendCallback('%s','%s');return "close?";};""" % (
            #     str(id(self)), "on_window_close"))
            #     self.master_widget.add_child("onunloadevent", tag)

            self.master_widget = setup_remi_window(self, self.window)
            self.window.master_widget = self.master_widget
            # if self.window.WindowIcon:
            #     print('placing icon')
                # self.page.children['head'].set_icon_file("/res:logo.png")
                # self.page.children['head'].set_icon_data( base64_data=self.window.WindowIcon, mimetype="image/png" )

            self.window.MessageQueue.put('Layout complete')     # signal the main code that the layout is all done
            return self.master_widget          # returning the root widget


        def on_window_close(self):
            # here you can handle the unload
            print("app closing")
            self.close()
            self.server.server_starter_instance._alive = False
            self.server.server_starter_instance._sserver.shutdown()
            # self.window.MessageQueue.put(None)
            print("server stopped")

FlexForm = Window




# =========================================================================== #
# Stops the mainloop and sets the event information                           #
# =========================================================================== #

def element_callback_quit_mainloop(element):
    if element.Key is not None:
        element.ParentForm.LastButtonClicked = element.Key
    else:
        element.ParentForm.LastButtonClicked = ''
    try:
        element.ParentForm.LastButtonClicked = element.Key if element.Key is not None else element.ButtonText
    except:
        element.ParentForm.LastButtonClicked = element.Key
    # print(f'Putting into message queue {element.ParentForm.LastButtonClicked}')
    element.ParentForm.MessageQueue.put(element.ParentForm.LastButtonClicked)


def quit_mainloop(window):
    window.App.ExitMainLoop()


# =========================================================================== #
# Stops the mainloop and sets the event information                           #
# =========================================================================== #
def convert_tkinter_size_to_Wx(size):
    """
    Converts size in characters to size in pixels
    :param size:  size in characters, rows
    :return: size in pixels, pixels
    """
    qtsize = size
    if size[1] is not None and size[1] < DEFAULT_PIXEL_TO_CHARS_CUTOFF:        # change from character based size to pixels (roughly)
        qtsize = size[0]*DEFAULT_PIXELS_TO_CHARS_SCALING[0], size[1]*DEFAULT_PIXELS_TO_CHARS_SCALING[1]
    return qtsize


def base64_to_style_image(base64_image):
    x ="url('data:image/png;base64,"
    x += str(base64_image)
    x += "')"
    # print(x)
    return x


def font_parse_string(font):
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
    family = _font[0]
    point_size = int(_font[1])

    style = _font[2:] if len(_font) > 1 else None

    # underline =  'underline' in _font[2:]
    # bold =  'bold' in _font

    return family, point_size, style




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


# -------------------------  SAVE BUTTON Element lazy function  ------------------------- #
def Save(button_text='Save', size=(None, None), auto_size_button=None, button_color=None, bind_return_key=True,
         disabled=False, tooltip=None, font=None, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  SUBMIT BUTTON Element lazy function  ------------------------- #
def Submit(button_text='Submit', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
           bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  OPEN BUTTON Element lazy function  ------------------------- #
def Open(button_text='Open', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
         bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  OK BUTTON Element lazy function  ------------------------- #
def OK(button_text='OK', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
       bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Ok(button_text='Ok', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
       bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  CANCEL BUTTON Element lazy function  ------------------------- #
def Cancel(button_text='Cancel', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
           tooltip=None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  QUIT BUTTON Element lazy function  ------------------------- #
def Quit(button_text='Quit', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
         font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  Exit BUTTON Element lazy function  ------------------------- #
def Exit(button_text='Exit', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
         font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)



# -------------------------  Up arrow BUTTON Element lazy function  ------------------------- #
def Up(button_text='▲', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
        font=None, bind_return_key=True, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  Down arrow BUTTON Element lazy function  ------------------------- #
def Down(button_text='▼', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
        font=None, bind_return_key=True, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  Left arrow BUTTON Element lazy function  ------------------------- #
def Left(button_text='◄', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
        font=None, bind_return_key=True, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  Right arrow BUTTON Element lazy function  ------------------------- #
def Right(button_text='►', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
        font=None, bind_return_key=True, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)



# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Yes(button_text='Yes', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
        font=None, bind_return_key=True, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  NO BUTTON Element lazy function  ------------------------- #
def No(button_text='No', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
       font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  NO BUTTON Element lazy function  ------------------------- #
def Help(button_text='Help', size=(None, None), auto_size_button=None, button_color=None, disabled=False, font=None,
         tooltip=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
def SimpleButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                 border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                 font=None, bind_return_key=False, disabled=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  CLOSE BUTTON Element lazy function  ------------------------- #
def CloseButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
                bind_return_key=False, disabled=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


CButton = CloseButton


# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
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


# -------------------------  Realtime BUTTON Element lazy function  ------------------------- #
def RealtimeButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                   border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                   font=None, disabled=False, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_REALTIME, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)


# -------------------------  Dummy BUTTON Element lazy function  ------------------------- #
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
                    element = element       # type: InputText
                    value = element.Widget.get_value()
                    if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                        element.Widget.set_value('')
                elif element.Type == ELEM_TYPE_INPUT_CHECKBOX:
                    element = element       # type: Checkbox
                    value = element.Widget.get_value()
                elif element.Type == ELEM_TYPE_INPUT_RADIO:
                    # RadVar = element.TKIntVar.get()
                    # this_rowcol = EncodeRadioRowCol(row_num, col_num)
                    value = False
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
                    element = element  # type: Combo
                    value = element.DefaultValue
                elif element.Type == ELEM_TYPE_INPUT_OPTION_MENU:
                    # value = element.TKStringVar.get()
                    value = None
                elif element.Type == ELEM_TYPE_INPUT_LISTBOX:
                    element = element  # type: Listbox
                    value = element.DefaultValues
                    # value = [value,]
                    # items = element.TKListbox.curselection()
                    # value = [element.Values[int(item)] for item in items]
                elif element.Type == ELEM_TYPE_INPUT_SPIN:
                    element = element       # type: Spin
                    value = element.DefaultValue
                    # value = element.Widget.get_value()
                elif element.Type == ELEM_TYPE_INPUT_SLIDER:
                    element = element       # type: Slider
                    value = element.DefaultValue
                elif element.Type == ELEM_TYPE_INPUT_MULTILINE:
                    element = element # type: Multiline
                    value = element.Widget.get_value()
                elif element.Type == ELEM_TYPE_TAB_GROUP:
                    try:
                        value = element.TKNotebook.tab(element.TKNotebook.index('current'))['text']
                        tab_key = element.FindKeyFromTabName(value)
                        if tab_key is not None:
                            value = tab_key
                    except:
                        value = None
                elif element.Type == ELEM_TYPE_TABLE:
                    element = element   # type:Table
                    value = [element.SelectedRow,]
                elif element.Type == ELEM_TYPE_TREE:
                    value = element.SelectedRows
                elif element.Type == ELEM_TYPE_GRAPH:
                    value = element.ClickPosition
                elif element.Type == ELEM_TYPE_MENUBAR:
                    value = element.MenuItemChosen
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


def _FillFormWithValues(form, values_dict):
    _FillSubformWithValues(form, values_dict)


def _FillSubformWithValues(form, values_dict):
    for row_num, row in enumerate(form.Rows):
        for col_num, element in enumerate(row):
            value = None
            if element.Type == ELEM_TYPE_COLUMN:
                _FillSubformWithValues(element, values_dict)
            if element.Type == ELEM_TYPE_FRAME:
                _FillSubformWithValues(element, values_dict)
            if element.Type == ELEM_TYPE_TAB_GROUP:
                _FillSubformWithValues(element, values_dict)
            if element.Type == ELEM_TYPE_TAB:
                _FillSubformWithValues(element, values_dict)
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


def AddMenuItem(top_menu, sub_menu_info, element, is_sub_menu=False, skip=False):
    # m3 = gui.MenuItem('Dialog', width=100, height=30)
    # m3.onclick.connect(self.menu_dialog_clicked)
    # menu.append([m1, m2, m3])

    return_val = None
    if type(sub_menu_info) is str:
        if not is_sub_menu and not skip:
            # print(f'Adding command {sub_menu_info}')
            pos = sub_menu_info.find('&')
            if pos != -1:
                if pos == 0 or sub_menu_info[pos - 1] != "\\":
                    sub_menu_info = sub_menu_info[:pos] + sub_menu_info[pos + 1:]
            if sub_menu_info == '---':
                # top_menu.add('separator')
                pass
            else:
                try:
                    item_without_key = sub_menu_info[:sub_menu_info.index(MENU_KEY_SEPARATOR)]
                except:
                    item_without_key = sub_menu_info
                if item_without_key[0] == MENU_DISABLED_CHARACTER:
                    menu_item =  remi.gui.MenuItem(item_without_key[1:], width=100, height=30)
                    menu_item.set_enabled(False)
                    top_menu.append([menu_item,])

                    # TODO add callback here!
                    # TODO disable entry
                else:
                    menu_item =  remi.gui.MenuItem(item_without_key, width=100, height=30)
                    top_menu.append([menu_item,])
                menu_item.set_on_click_listener(element._ChangedCallbackMenu, sub_menu_info)
    else:
        i = 0
        while i < (len(sub_menu_info)):
            item = sub_menu_info[i]
            if i != len(sub_menu_info) - 1:
                if type(sub_menu_info[i + 1]) == list:
                    pos = sub_menu_info[i].find('&')
                    if pos != -1:
                        if pos == 0 or sub_menu_info[i][pos - 1] != "\\":
                            sub_menu_info[i] = sub_menu_info[i][:pos] + sub_menu_info[i][pos + 1:]
                    if sub_menu_info[i][0] == MENU_DISABLED_CHARACTER:
                        new_menu = remi.gui.MenuItem(sub_menu_info[i][len(MENU_DISABLED_CHARACTER):], width=100, height=30)
                        new_menu.set_enabled(False)

                        # TODO Disable Entry
                    else:
                        new_menu = remi.gui.MenuItem(sub_menu_info[i], width=100, height=30)

                    top_menu.append([new_menu,])
                    return_val = new_menu
                    AddMenuItem(new_menu, sub_menu_info[i + 1], element, is_sub_menu=True)
                    i += 1  # skip the next one
                else:
                    AddMenuItem(top_menu, item, element)
            else:
                AddMenuItem(top_menu, item, element)
            i += 1
    return return_val

"""
          :::::::::       ::::::::::         :::   :::       ::::::::::: 
         :+:    :+:      :+:               :+:+: :+:+:          :+:      
        +:+    +:+      +:+              +:+ +:+:+ +:+         +:+       
       +#++:++#:       +#++:++#         +#+  +:+  +#+         +#+        
      +#+    +#+      +#+              +#+       +#+         +#+         
     #+#    #+#      #+#              #+#       #+#         #+#          
    ###    ###      ##########       ###       ###     ###########    
"""
# ------------------------------------------------------------------------------------------------------------ #
# ===================================== REMI CODE STARTS HERE ================================================ #
# ------------------------------------------------------------------------------------------------------------ #

def PackFormIntoFrame(form, containing_frame, toplevel_form):
    def CharWidthInPixels():
        return tkinter.font.Font().measure('A')  # single character width

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
        font_info = font_parse_string(font)  # family, point size, other
        widget.style['font-family'] = font_info[0]
        if element.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
            widget.style['background-color'] = element.BackgroundColor
        if element.TextColor not in (None, COLOR_SYSTEM_DEFAULT):
            widget.style['color'] = element.TextColor
        widget.style['font-size'] = '{}px'.format(font_info[1])
        if element_size[0]:     # if size is zero, don't set any sizes
            size = convert_tkinter_size_to_Wx(element_size)
            widget.style['height'] = '{}px'.format(size[1])
            widget.style['width'] = '{}px'.format(size[0])
        widget.style['margin'] = '{}px {}px {}px {}px'.format(*full_element_pad)
        if element.Disabled:
            widget.set_enabled(False)
        if not element.Visible:
            widget.attributes['hidden'] = 'true'
        if element.Tooltip is not None:
            widget.attributes['title'] = element.Tooltip

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
        tk_row_frame = remi.gui.HBox()
        if form.Justification.startswith('c'):
            # print('Centering row')
            tk_row_frame.style['align-items'] = 'center'
            tk_row_frame.style['justify-content'] = 'center'
        else:
            tk_row_frame.style['align-items'] = 'flex-start'
            tk_row_frame.style['justify-content'] = 'flex-start'
        if form.BackgroundColor not in(None, COLOR_SYSTEM_DEFAULT):
            tk_row_frame.style['background-color'] = form.BackgroundColor

        for col_num, element in enumerate(flex_row):
            element.ParentForm = toplevel_form  # save the button's parent form object
            if toplevel_form.Font and (element.Font == DEFAULT_FONT or not element.Font):
                font = toplevel_form.Font
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
            if (element_size == (None, None) and element_type != ELEM_TYPE_BUTTON):  # user did not specify a size
                element_size = toplevel_form.DefaultElementSize
            elif (element_size == (None, None) and element_type == ELEM_TYPE_BUTTON):
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

            # -------------------------  COLUMN element  ------------------------- #
            if element_type == ELEM_TYPE_COLUMN:
                element = element   # type: Column
                element.Widget = column_widget = remi.gui.VBox()
                if element.Justification.startswith('c'):
                    # print('CENTERING')
                    column_widget.style['align-items'] = 'center'
                    column_widget.style['justify-content'] = 'center'
                else:
                    column_widget.style['justify-content'] = 'flex-start'
                    column_widget.style['align-items'] = 'baseline'
                if element.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
                    column_widget.style['background-color'] = element.BackgroundColor
                PackFormIntoFrame(element, column_widget, toplevel_form)
                tk_row_frame.append(element.Widget)

            # -------------------------  TEXT element  ------------------------- #
            elif element_type == ELEM_TYPE_TEXT:
                element = element   # type: Text
                element.Widget = remi.gui.Label(element.DisplayText)
                element.Widget.set_layout_orientation(True)
                do_font_and_color(element.Widget)
                if auto_size_text and element.Size == (None, None):
                    del(element.Widget.style['width'])
                if element.Justification:
                    if element.Justification.startswith('c'):
                        element.Widget.style['text-align'] = 'center'
                    elif element.Justification.startswith('r'):
                        element.Widget.style['text-align'] = 'right'
                if element.ClickSubmits:
                    element.Widget.onclick.connect(element._ChangedCallback)
                tk_row_frame.append(element.Widget)

            # -------------------------  BUTTON element  ------------------------- #
            elif element_type == ELEM_TYPE_BUTTON:
                element = element  # type: Button
                size = convert_tkinter_size_to_Wx(element_size)
                element.Widget = remi.gui.Button(element.ButtonText, width=size[0], height=size[1], margin='10px')
                element.Widget.onclick.connect(element._ButtonCallBack)
                do_font_and_color(element.Widget)
                if element.AutoSizeButton or (toplevel_form.AutoSizeButtons and element.AutoSizeButton is not False) and element.Size == (None, None):
                    del (element.Widget.style['width'])
                if element.ImageFilename:
                    element.ImageWidget = SuperImage(element.ImageFilename if element.ImageFilename is not None else element.ImageData)
                    element.Widget.append(element.ImageWidget)
                tk_row_frame.append(element.Widget)

            #     stringvar = tk.StringVar()
            #     element.TKStringVar = stringvar
            #     element.Location = (row_num, col_num)
            #     btext = element.ButtonText
            #     btype = element.BType
            #     if element.AutoSizeButton is not None:
            #         auto_size = element.AutoSizeButton
            #     else:
            #         auto_size = toplevel_form.AutoSizeButtons
            #     if auto_size is False or element.Size[0] is not None:
            #         width, height = element_size
            #     else:
            #         width = 0
            #         height = toplevel_form.DefaultButtonElementSize[1]
            #     if element.ButtonColor != (None, None) and element.ButtonColor != DEFAULT_BUTTON_COLOR:
            #         bc = element.ButtonColor
            #     elif toplevel_form.ButtonColor != (None, None) and toplevel_form.ButtonColor != DEFAULT_BUTTON_COLOR:
            #         bc = toplevel_form.ButtonColor
            #     else:
            #         bc = DEFAULT_BUTTON_COLOR
            #     border_depth = element.BorderWidth
            #     if btype != BUTTON_TYPE_REALTIME:
            #         tkbutton = tk.Button(tk_row_frame, text=btext, width=width, height=height,
            #                              command=element.ButtonCallBack, justify=tk.LEFT, bd=border_depth, font=font)
            #     else:
            #         tkbutton = tk.Button(tk_row_frame, text=btext, width=width, height=height, justify=tk.LEFT,
            #                              bd=border_depth, font=font)
            #         tkbutton.bind('<ButtonRelease-1>', element.ButtonReleaseCallBack)
            #         tkbutton.bind('<ButtonPress-1>', element.ButtonPressCallBack)
            #     if bc != (None, None) and bc != COLOR_SYSTEM_DEFAULT and bc[1] != COLOR_SYSTEM_DEFAULT:
            #         tkbutton.config(foreground=bc[0], background=bc[1], activebackground=bc[1])
            #     elif bc[1] == COLOR_SYSTEM_DEFAULT:
            #         tkbutton.config(foreground=bc[0])
            #
            #     element.TKButton = tkbutton  # not used yet but save the TK button in case
            #     wraplen = tkbutton.winfo_reqwidth()  # width of widget in Pixels
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
            #         element.TKButton.bind('<Return>', element.ReturnKeyHandler)
            #     if element.Focus is True or (toplevel_form.UseDefaultFocus and not focus_set):
            #         focus_set = True
            #         element.TKButton.bind('<Return>', element.ReturnKeyHandler)
            #         element.TKButton.focus_set()
            #         toplevel_form.TKroot.focus_force()
            #     if element.Disabled == True:
            #         element.TKButton['state'] = 'disabled'
            #     if element.Tooltip is not None:
            #         element.TooltipObject = ToolTip(element.TKButton, text=element.Tooltip,
            #                                         timeout=DEFAULT_TOOLTIP_TIME)
            # # -------------------------  INPUT  element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_TEXT:
                element = element  # type: InputText
                element.Widget = InputText.TextInput_raw_onkeyup(hint=element.DefaultText)
                # element.Widget = remi.gui.TextInput(hint=element.DefaultText)
                do_font_and_color(element.Widget)
                if element.ChangeSubmits:
                    element.Widget.onkeyup.connect(element._InputTextCallback)
                    # element.Widget.onkeydown.connect(element._InputTextCallback)
                tk_row_frame.append(element.Widget)

                # show = element.PasswordCharacter if element.PasswordCharacter else ""
                # if element.Justification is not None:
                #     justification = element.Justification
                # else:
                #     justification = DEFAULT_TEXT_JUSTIFICATION
                # justify = tk.LEFT if justification == 'left' else tk.CENTER if justification == 'center' else tk.RIGHT
                # # anchor = tk.NW if justification == 'left' else tk.N if justification == 'center' else tk.NE
                # element.TKEntry = tk.Entry(tk_row_frame, width=element_size[0], textvariable=element.TKStringVar,
                #                            bd=border_depth, font=font, show=show, justify=justify)
                # if element.ChangeSubmits:
                #     element.TKEntry.bind('<Key>', element.KeyboardHandler)
                # element.TKEntry.bind('<Return>', element.ReturnKeyHandler)
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     element.TKEntry.configure(background=element.BackgroundColor)
                # if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                #     element.TKEntry.configure(fg=text_color)
                # element.TKEntry.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1], expand=True, fill='x')
                # if element.Focus is True or (toplevel_form.UseDefaultFocus and not focus_set):
                #     focus_set = True
                #     element.TKEntry.focus_set()
                # if element.Disabled:
                #     element.TKEntry['state'] = 'disabled'
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element.TKEntry, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  COMBO element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_COMBO:
                element = element  # type: Combo
                element.Widget = remi.gui.DropDown.new_from_list(element.Values)
                if element.DefaultValue is not None:
                    element.Widget.select_by_value(element.DefaultValue)
                do_font_and_color(element.Widget)
                if element.ChangeSubmits:
                    element.Widget.onchange.connect(element._ChangedCallback)
                tk_row_frame.append(element.Widget)

            # -------------------------  OPTION MENU (Like ComboBox but different) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_OPTION_MENU:
                element.Widget = remi.gui.FileUploader('./', width=200, height=30, margin='10px')

                # element.Widget = remi.gui.FileFolderNavigator(False, r'a:\TEMP', True, False)
                tk_row_frame.append(element.Widget)
                pass
            # -------------------------  LISTBOX element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_LISTBOX:
                element = element  # type: Listbox
                element.Widget = remi.gui.ListView.new_from_list(element.Values)
                do_font_and_color(element.Widget)
                if element.ChangeSubmits:
                    element.Widget.onselection.connect(element._ChangedCallback)
                tk_row_frame.append(element.Widget)
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
                element = element  # type: Multiline
                element.Widget = remi.gui.TextInput(single_line=False, hint=element.DefaultText)
                do_font_and_color(element.Widget)
                if element.ChangeSubmits:
                    element.Widget.onkeydown.connect(element._InputTextCallback)
                tk_row_frame.append(element.Widget)
                # default_text = element.DefaultText
                # width, height = element_size
                # element.TKText = tk.scrolledtext.ScrolledText(tk_row_frame, width=width, height=height, wrap='word',
                #                                               bd=border_depth, font=font)
                # element.TKText.insert(1.0, default_text)  # set the default text
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     element.TKText.configure(background=element.BackgroundColor)
                #     element.TKText.vbar.config(troughcolor=DEFAULT_SCROLLBAR_COLOR)
                # element.TKText.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1], expand=True, fill='both')
                # if element.ChangeSubmits:
                #     element.TKText.bind('<Key>', element.KeyboardHandler)
                # if element.EnterSubmits:
                #     element.TKText.bind('<Return>', element.ReturnKeyHandler)
                # if element.Focus is True or (toplevel_form.UseDefaultFocus and not focus_set):
                #     focus_set = True
                #     element.TKText.focus_set()
                # if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                #     element.TKText.configure(fg=text_color)
                # if element.Disabled == True:
                #     element.TKText['state'] = 'disabled'
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element.TKText, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)

            # -------------------------  INPUT CHECKBOX element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_CHECKBOX:
                element = element  # type: Checkbox
                element.Widget = remi.gui.CheckBoxLabel(element.Text)
                if element.InitialState:
                    element.Widget.set_value(element.InitialState)
                if element.ChangeSubmits:
                    element.Widget.onchange.connect(element._ChangedCallback)
                do_font_and_color(element.Widget)
                tk_row_frame.append(element.Widget)

            #     width = 0 if auto_size_text else element_size[0]
            #     default_value = element.InitialState
            #     element.TKIntVar = tk.IntVar()
            #     element.TKIntVar.set(default_value if default_value is not None else 0)
            #     if element.ChangeSubmits:
            #         element.TKCheckbutton = tk.Checkbutton(tk_row_frame, anchor=tk.NW, text=element.Text, width=width,
            #                                                variable=element.TKIntVar, bd=border_depth, font=font,
            #                                                command=element.CheckboxHandler)
            #     else:
            #         element.TKCheckbutton = tk.Checkbutton(tk_row_frame, anchor=tk.NW, text=element.Text, width=width,
            #                                                variable=element.TKIntVar, bd=border_depth, font=font)
            #     if default_value is None or element.Disabled:
            #         element.TKCheckbutton.configure(state='disable')
            #     if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
            #         element.TKCheckbutton.configure(background=element.BackgroundColor)
            #         element.TKCheckbutton.configure(selectcolor=element.BackgroundColor)
            #         element.TKCheckbutton.configure(activebackground=element.BackgroundColor)
            #     if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
            #         element.TKCheckbutton.configure(fg=text_color)
            #     element.TKCheckbutton.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
            #     if element.Tooltip is not None:
            #         element.TooltipObject = ToolTip(element.TKCheckbutton, text=element.Tooltip,
            #                                         timeout=DEFAULT_TOOLTIP_TIME)
            # # -------------------------  PROGRESS BAR element  ------------------------- #
            elif element_type == ELEM_TYPE_PROGRESS_BAR:
                pass
            #     # save this form because it must be 'updated' (refreshed) solely for the purpose of updating bar
            #     width = element_size[0]
            #     fnt = tkinter.font.Font()
            #     char_width = fnt.measure('A')  # single character width
            #     progress_length = width * char_width
            #     progress_width = element_size[1]
            #     direction = element.Orientation
            #     if element.BarColor != (None, None):  # if element has a bar color, use it
            #         bar_color = element.BarColor
            #     else:
            #         bar_color = DEFAULT_PROGRESS_BAR_COLOR
            #     element.TKProgressBar = TKProgressBar(tk_row_frame, element.MaxValue, progress_length, progress_width,
            #                                           orientation=direction, BarColor=bar_color,
            #                                           border_width=element.BorderWidth, relief=element.Relief,
            #                                           style=element.BarStyle, key=element.Key)
            #     element.TKProgressBar.TKProgressBarForReal.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # -------------------------  INPUT RADIO BUTTON element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_RADIO:
                pass
                # width = 0 if auto_size_text else element_size[0]
                # default_value = element.InitialState
                # ID = element.GroupID
                # # see if ID has already been placed
                # value = EncodeRadioRowCol(row_num, col_num)  # value to set intvar to if this radio is selected
                # if ID in toplevel_form.RadioDict:
                #     RadVar = toplevel_form.RadioDict[ID]
                # else:
                #     RadVar = tk.IntVar()
                #     toplevel_form.RadioDict[ID] = RadVar
                # element.TKIntVar = RadVar  # store the RadVar in Radio object
                # if default_value:  # if this radio is the one selected, set RadVar to match
                #     element.TKIntVar.set(value)
                # if element.ChangeSubmits:
                #     element.TKRadio = tk.Radiobutton(tk_row_frame, anchor=tk.NW, text=element.Text, width=width,
                #                                      variable=element.TKIntVar, value=value, bd=border_depth, font=font,
                #                                      command=element.RadioHandler)
                # else:
                #     element.TKRadio = tk.Radiobutton(tk_row_frame, anchor=tk.NW, text=element.Text, width=width,
                #                                      variable=element.TKIntVar, value=value, bd=border_depth, font=font)
                # if not element.BackgroundColor in (None, COLOR_SYSTEM_DEFAULT):
                #     element.TKRadio.configure(background=element.BackgroundColor)
                #     element.TKRadio.configure(selectcolor=element.BackgroundColor)
                # if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                #     element.TKRadio.configure(fg=text_color)
                # if element.Disabled:
                #     element.TKRadio['state'] = 'disabled'
                # element.TKRadio.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element.TKRadio, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
                # -------------------------  INPUT SPIN element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SPIN:
                element = element  # type: Spin
                element.Widget = remi.gui.SpinBox(50, 0, 100)
                if element.DefaultValue is not None:
                    element.Widget.set_value(element.DefaultValue)
                do_font_and_color(element.Widget)
                if element.ChangeSubmits:
                    element.Widget.onchange.connect(element._ChangedCallback)
                tk_row_frame.append(element.Widget)
                # width, height = element_size
                # width = 0 if auto_size_text else element_size[0]
                # element.TKStringVar = tk.StringVar()
                # element.TKSpinBox = tk.Spinbox(tk_row_frame, values=element.Values, textvariable=element.TKStringVar,
                #                                width=width, bd=border_depth)
                # element.TKStringVar.set(element.DefaultValue)
                # element.TKSpinBox.configure(font=font)  # set wrap to width of widget
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     element.TKSpinBox.configure(background=element.BackgroundColor)
                # element.TKSpinBox.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                #     element.TKSpinBox.configure(fg=text_color)
                # if element.ChangeSubmits:
                #     element.TKSpinBox.bind('<ButtonRelease-1>', element.SpinChangedHandler)
                # if element.Disabled == True:
                #     element.TKSpinBox['state'] = 'disabled'
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element.TKSpinBox, text=element.Tooltip,
                #                                     timeout=DEFAULT_TOOLTIP_TIME)
                # -------------------------  OUTPUT element  ------------------------- #
            elif element_type == ELEM_TYPE_OUTPUT:
                element=element  # type: Output
                element.Widget = remi.gui.TextInput(single_line=False)
                element.Disabled = True
                do_font_and_color(element.Widget)
                tk_row_frame.append(element.Widget)
                toplevel_form.OutputElementForStdOut = element
                Window.stdout_is_rerouted = True
                Window.stdout_string_io = StringIO()
                sys.stdout = Window.stdout_string_io

                # width, height = element_size
                # element._TKOut = TKOutput(tk_row_frame, width=width, height=height, bd=border_depth,
                #                           background_color=element.BackgroundColor, text_color=text_color, font=font,
                #                           pad=element.Pad)
                # element._TKOut.pack(side=tk.LEFT, expand=True, fill='both')
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element._TKOut, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
                # -------------------------  OUTPUT MULTILINE element  ------------------------- #
            elif element_type == ELEM_TYPE_MULTILINE_OUTPUT:
                element = element  # type: MultilineOutput
                element.Widget = remi.gui.TextInput(single_line=False)
                element.Disabled = True
                do_font_and_color(element.Widget)
                tk_row_frame.append(element.Widget)
                if element.DefaultText:
                    element.Widget.set_value(element.DefaultText)
                # -------------------------  IMAGE element  ------------------------- #
            elif element_type == ELEM_TYPE_IMAGE:
                element = element  # type: Image
                # element.Widget = remi.gui.Image(element.Filename)
                element.Widget = SuperImage(element.Filename if element.Filename is not None else element.Data)
                do_font_and_color(element.Widget)
                if element.EnableEvents:
                    element.Widget.onclick.connect(element._ChangedCallback)
                tk_row_frame.append(element.Widget)
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
                element = element  # type: Graph
                element.Widget = remi.gui.Svg(width=element.CanvasSize[0], height=element.CanvasSize[1])
                element.SvgGroup = remi.gui.SvgGroup(element.CanvasSize[1],0)
                element.Widget.append([element.SvgGroup,])
                do_font_and_color(element.Widget)
                if element.ChangeSubmits:
                    element.Widget.onmouseup.connect(element._MouseUpCallback)
                    # element.Widget.onclick.connect(element.ClickCallback)
                if element.DragSubmits:
                    element.Widget.onmousedown.connect(element._MouseDownCallback)
                    element.Widget.onmouseup.connect(element._MouseUpCallback)
                    element.Widget.onmousemove.connect(element._DragCallback)

                tk_row_frame.append(element.Widget)
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
                element = element       # type: Menu
                menu = remi.gui.Menu(width='100%', height=str(element_size[1]))
                element_size = (0,0)    # makes the menu span across the top
                do_font_and_color(menu)

                menu_def = element.MenuDefinition
                for menu_entry in menu_def:
                    # print(f'Adding a Menubar ENTRY {menu_entry}')
                    pos = menu_entry[0].find('&')
                    # print(pos)
                    if pos != -1:
                        if pos == 0 or menu_entry[0][pos - 1] != "\\":
                            menu_entry[0] = menu_entry[0][:pos] + menu_entry[0][pos + 1:]
                    if menu_entry[0][0] == MENU_DISABLED_CHARACTER:
                        item = remi.gui.MenuItem(menu_entry[0][1:], width=100, height=element_size[1])
                        item.set_enabled(False)
                    else:
                        item = remi.gui.MenuItem(menu_entry[0], width=100, height=element_size[1])
                    do_font_and_color(item)
                    menu.append([item,])
                    if len(menu_entry) > 1:
                        AddMenuItem(item, menu_entry[1], element)

                element.Widget = menubar = remi.gui.MenuBar(width='100%', height='30px')
                element.Widget.style['z-index'] = '1'
                menubar.append(menu)
                # tk_row_frame.append(element.Widget)
                containing_frame.append(element.Widget)

            # -------------------------  Frame element  ------------------------- #
            elif element_type == ELEM_TYPE_FRAME:
                element = element  # type: Frame
                element.Widget = column_widget = remi.gui.VBox()
                if element.Justification.startswith('c'):
                    # print('CENTERING')
                    column_widget.style['align-items'] = 'center'
                    column_widget.style['justify-content'] = 'center'
                else:
                    column_widget.style['justify-content'] = 'flex-start'
                    column_widget.style['align-items'] = 'baseline'
                if element.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
                    column_widget.style['background-color'] = element.BackgroundColor
                PackFormIntoFrame(element, column_widget, toplevel_form)
                tk_row_frame.append(element.Widget)

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
                element = element           # type: Tab
                element.Widget = remi.gui.VBox()
                if element.Justification.startswith('c'):
                    # print('CENTERING')
                    element.Widget.style['align-items'] = 'center'
                    element.Widget.style['justify-content'] = 'center'
                else:
                    element.Widget.style['justify-content'] = 'flex-start'
                    element.Widget.style['align-items'] = 'baseline'
                if element.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
                    element.Widget.style['background-color'] = element.BackgroundColor
                if element.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
                    element.Widget.style['background-color'] = element.BackgroundColor
                PackFormIntoFrame(element, element.Widget, toplevel_form)
                # tk_row_frame.append(element.Widget)
                containing_frame.add_tab(element.Widget, element.Title, None)

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
                element = element           # type: TabGroup
                element.Widget = remi.gui.TabBox()
                # do_font_and_color(element.Widget)
                PackFormIntoFrame(element ,element.Widget, toplevel_form)
                tk_row_frame.append(element.Widget)

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
                # -------------------------  SLIDER element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SLIDER:
                element = element  # type: Slider
                orient = remi.gui.Widget.LAYOUT_HORIZONTAL if element.Orientation.lower().startswith('h') else remi.gui.Widget.LAYOUT_VERTICAL
                element.Widget = remi.gui.Slider(layout_orientation=orient, default_value=element.DefaultValue, min=element.Range[0], max=element.Range[1],step=element.Resolution)
                if element.DefaultValue:
                    element.Widget.set_value(element.DefaultValue)
                # if element.Orientation.startswith('v'):
                #     element.Widget.layout_orientation = remi.gui.Widget.LAYOUT_VERTICAL
                do_font_and_color(element.Widget)
                if element.ChangeSubmits:
                    element.Widget.onchange.connect(element._SliderCallback)
                element.Widget.style['orientation'] = 'vertical'
                element.Widget.attributes['orientation'] = 'vertical'
                # print(f'slider = {element.Widget.style, element.Widget.attributes}')
                tk_row_frame.append(element.Widget)                # slider_length = element_size[0] * CharWidthInPixels()

            # -------------------------  TABLE element  ------------------------- #
            elif element_type == ELEM_TYPE_TABLE:
                element = element       # type: Table
                new_table = []
                for row_num, row in enumerate(element.Values):             # convert entire table to strings
                    new_row= [str(item) for item in row]
                    if element.DisplayRowNumbers:
                        new_row = [element.RowHeaderText if row_num == 0 else str(row_num+element.StartingRowNumber) ,] + new_row
                    new_table.append(new_row)
                element.Widget = remi.gui.Table.new_from_list(new_table)
                do_font_and_color(element.Widget)
                tk_row_frame.append(element.Widget)
                element.Widget.on_table_row_click.connect(element._on_table_row_click)
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
                #     displaycolumns = element.ColumnHeadings if element.ColumnHeadings is not None else element.Values[0]
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
                #                                   selectmode=element.SelectMode,)
                # treeview = element.TKTreeview
                # if element.DisplayRowNumbers:
                #     treeview.heading(element.RowHeaderText, text=element.RowHeaderText)  # make a dummy heading
                #     treeview.column(element.RowHeaderText, width=50, anchor=anchor)
                #
                # headings = element.ColumnHeadings if element.ColumnHeadings is not None else element.Values[0]
                # for i, heading in enumerate(headings):
                #     treeview.heading(heading, text=heading)
                #     if element.AutoSizeColumns:
                #         width = max(column_widths[i], len(heading))
                #     else:
                #         try:
                #             width = element.ColumnWidths[i]
                #         except:
                #             width = element.DefaultColumnWidth
                #     treeview.column(heading, width=width * CharWidthInPixels(), anchor=anchor)
                #
                # # Insert values into the tree
                # for i, value in enumerate(element.Values):
                #     if element.DisplayRowNumbers:
                #         value = [i+element.StartingRowNumber] + value
                #     id = treeview.insert('', 'end', text=value, iid=i + 1, values=value, tag=i)
                # if element.AlternatingRowColor is not None:         # alternating colors
                #     for row in range(0, len(element.Values), 2):
                #         treeview.tag_configure(row, background=element.AlternatingRowColor)
                # if element.RowColors is not None:                   # individual row colors
                #     for row_def in element.RowColors:
                #         if len(row_def) == 2:                       # only background is specified
                #             treeview.tag_configure(row_def[0], background=row_def[1])
                #         else:
                #             treeview.tag_configure(row_def[0], background=row_def[2], foreground=row_def[1])
                #
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     ttk.Style().configure("Treeview", background=element.BackgroundColor,
                #                           fieldbackground=element.BackgroundColor)
                # if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                #     ttk.Style().configure("Treeview", foreground=element.TextColor)
                # if element.RowHeight is not None:
                #     ttk.Style().configure("Treeview", rowheight=element.RowHeight)
                # ttk.Style().configure("Treeview", font=font)
                # # scrollable_frame.pack(side=tk.LEFT,  padx=elementpad[0], pady=elementpad[1], expand=True, fill='both')
                # treeview.bind("<<TreeviewSelect>>", element.treeview_selected)
                # if element.BindReturnKey:
                #     treeview.bind('<Return>', element.treeview_double_click)
                #     treeview.bind('<Double-Button-1>', element.treeview_double_click)
                #
                # scrollbar = tk.Scrollbar(frame)
                # scrollbar.pack(side=tk.RIGHT, fill='y')
                # scrollbar.config(command=treeview.yview)
                #
                # if not element.VerticalScrollOnly:
                #     hscrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
                #     hscrollbar.pack(side=tk.BOTTOM, fill='x')
                #     hscrollbar.config(command=treeview.xview)
                #     treeview.configure(xscrollcommand=hscrollbar.set)
                #
                # treeview.configure(yscrollcommand=scrollbar.set)
                #
                # element.TKTreeview.pack(side=tk.LEFT, expand=True, padx=0, pady=0, fill='both')
                # if element.Visible is False:
                #     element.TKTreeview.pack_forget()
                # frame.pack(side=tk.LEFT, expand=True, padx=0, pady=0)
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element.TKTreeview, text=element.Tooltip,
                #                                     timeout=DEFAULT_TOOLTIP_TIME)
                # if element.RightClickMenu or toplevel_form.RightClickMenu:
                #     menu = element.RightClickMenu or toplevel_form.RightClickMenu
                #     top_menu = tk.Menu(toplevel_form.TKroot, tearoff=False)
                #     AddMenuItem(top_menu, menu[1], element)
                #     element.TKRightClickMenu = top_menu
                #     element.TKTreeview.bind('<Button-3>', element.RightClickMenuCallback)
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
                pass
        #         separator = ttk.Separator(tk_row_frame, orient=element.Orientation, )
        #         separator.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1], fill='both', expand=True)
        #
        # # ............................DONE WITH ROW pack the row of widgets ..........................#
        # done with row, pack the row of widgets
        # tk_row_frame.grid(row=row_num+2, sticky=tk.NW, padx=DEFAULT_MARGINS[0])
        # tk_row_frame.pack(side=tk.TOP, anchor='nw', padx=DEFAULT_MARGINS[0], expand=False)
        # if form.BackgroundColor is not None and form.BackgroundColor != COLOR_SYSTEM_DEFAULT:
        #     tk_row_frame.configure(background=form.BackgroundColor)
        # toplevel_form.TKroot.configure(padx=DEFAULT_MARGINS[0], pady=DEFAULT_MARGINS[1])
        containing_frame.append(tk_row_frame)
    return


def setup_remi_window(app:Window.MyApp, window:Window):
    master_widget = remi.gui.VBox()
    master_widget.style['justify-content'] = 'flex-start'
    master_widget.style['align-items'] = 'baseline'
    if window.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
        master_widget.style['background-color'] = window.BackgroundColor
    try:
        PackFormIntoFrame(window, master_widget, window)
    except:
        print('* ERROR PACKING FORM *')
        print(traceback.format_exc())


    if window.BackgroundImage:
        master_widget.style['background-image'] = "url('{}')".format('/' + window.BackgroundImage)
        # print(f'background info',self.master_widget.attributes['background-image'] )

    if not window.DisableClose:
        # add the following 3 lines to your app and the on_window_close method to make the console close automatically
        tag = remi.gui.Tag(_type='script')
        tag.add_child("javascript", """window.onunload=function(e){sendCallback('%s','%s');return "close?";};""" % (
            str(id(app)), "on_window_close"))
        master_widget.add_child("onunloadevent", tag)

    if window.ReturnKeyboardEvents:
        app.page.children['body'].onkeyup.connect(window.on_key_up)
    if window.ReturnKeyDownEvents:
        app.page.children['body'].onkeydown.connect(window.on_key_down)


    # if window.WindowIcon:
    #     if type(window.WindowIcon) is bytes or len(window.WindowIcon) > 200:
    #         app.page.children['head'].set_icon_data( base64_data=str(window.WindowIcon), mimetype="image/gif" )
    #     else:
    #         app.page.children['head'].set_icon_file("/res:{}".format(window.WindowIcon))
    #         pass
            # mimetype, encoding = mimetypes.guess_type(image_source)
            # with open(image_source, 'rb') as f:
            #     data = f.read()
            # b64 = base64.b64encode(data)
            # b64_str = b64.decode("utf-8")
            # image_string = "data:image/svg;base64,%s"%b64_str
            # rpoint.set_image(image_string)


    return master_widget

# ----====----====----====----====----==== STARTUP TK ====----====----====----====----====----#
def StartupTK(window:Window):
    global _my_windows


    # print('Starting TK open Windows = {}'.format(ow))

    _my_windows.Increment()

    # if not my_flex_form.Resizable:
    #     root.resizable(False, False)

    # if my_flex_form.KeepOnTop:
    #     root.wm_attributes("-topmost", 1)
    # master = window.TKroot
    # Set Title
    # master.title(MyFlexForm.Title)
    # master = 00000

    InitializeResults(window)

    # Does all of the window setup, starting up Remi
    # if no windows exist, start Remi thread which will call same setup_remi_window call as shown below
    if len(Window.active_windows) == 0:
        window.thread_id = threading.Thread(target=window.remi_thread, daemon=True)
        window.thread_id.daemon = True
        window.thread_id.start()
        item = window.MessageQueue.get()        # Get the layout complete message
        Window.active_windows.append(window)
        Window.App = window.App
    else:
        # print('Starting second page')
        # margin 0px auto allows to center the app to the screen
        # master_widget = remi.gui.VBox()
        # master_widget.style['justify-content'] = 'flex-start'
        # master_widget.style['align-items'] = 'baseline'
        # if window.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
        #     master_widget.style['background-color'] = window.BackgroundColor
        # PackFormIntoFrame(window, master_widget, window)
        master_widget = setup_remi_window(Window.App, window)
        window.master_widget = master_widget
        Window.active_windows.append(window)
        Window.App.set_root_widget(master_widget)

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


# ============================== ProgressMeter  =====#
# ===================================================#
def _ProgressMeter(title, max_value, *args, orientation=None, bar_color=(None, None), button_color=None,
                   size=DEFAULT_PROGRESS_BAR_SIZE, border_width=None, grab_anywhere=False):
    '''
    Create and show a form on tbe caller's behalf.
    :param title:
    :param max_value:
    :param args: ANY number of arguments the caller wants to display
    :param orientation:
    :param bar_color:
    :param size:
    :param Style:
    :param StyleOffset:
    :return: ProgressBar object that is in the form
    '''
    local_orientation = DEFAULT_METER_ORIENTATION if orientation is None else orientation
    local_border_width = DEFAULT_PROGRESS_BAR_BORDER_WIDTH if border_width is None else border_width
    bar2 = ProgressBar(max_value, orientation=local_orientation, size=size, bar_color=bar_color,
                       border_width=local_border_width, relief=DEFAULT_PROGRESS_BAR_RELIEF)
    form = Window(title, auto_size_text=True, grab_anywhere=grab_anywhere)

    # Form using a horizontal bar
    if local_orientation[0].lower() == 'h':
        single_line_message, width, height = ConvertArgsToSingleString(*args)
        bar2.TextToDisplay = single_line_message
        bar2.TextToDisplay = single_line_message
        bar2.MaxValue = max_value
        bar2.CurrentValue = 0
        bar_text = Text(single_line_message, size=(width, height + 3), auto_size_text=True)
        form.AddRow(bar_text)
        form.AddRow((bar2))
        form.AddRow((CloseButton('Cancel', button_color=button_color)))
    else:
        single_line_message, width, height = ConvertArgsToSingleString(*args)
        bar2.TextToDisplay = single_line_message
        bar2.MaxValue = max_value
        bar2.CurrentValue = 0
        bar_text = Text(single_line_message, size=(width, height + 3), auto_size_text=True)
        form.AddRow(bar2, bar_text)
        form.AddRow((CloseButton('Cancel', button_color=button_color)))

    form.NonBlocking = True
    form.Show(non_blocking=True)
    return bar2, bar_text


# ============================== ProgressMeterUpdate  =====#
def _ProgressMeterUpdate(bar, value, text_elem, *args):
    '''
    Update the progress meter for a form
    :param form: class ProgressBar
    :param value: int
    :return: True if not cancelled, OK....False if Error
    '''
    global _my_windows
    if bar == None: return False
    if bar.BarExpired: return False
    message, w, h = ConvertArgsToSingleString(*args)
    text_elem.Update(message)
    # bar.TextToDisplay = message
    bar.CurrentValue = value
    rc = bar.UpdateBar(value)
    if value >= bar.MaxValue or not rc:
        bar.BarExpired = True
        bar.ParentForm._Close()
        if rc:  # if update was OK but bar expired, decrement num windows
            _my_windows.Decrement()
    if bar.ParentForm.RootNeedsDestroying:
        try:
            bar.ParentForm.TKroot.destroy()
            # there is a bug with progress meters not decrementing the number of windows
            # correctly when the X is used to close the window
            # uncommenting this line fixes that problem, but causes a double-decrement when
            # the cancel button is used... damned if you do, damned if you don't, so I'm choosing
            # don't, as in don't decrement too many times. It's OK now to have a mismatch in
            # number of windows because of the "hidden" master window. This ensures all windows
            # will be toplevel.  Sorry about the bug, but the user never sees any problems as a result
            # _my_windows.Decrement()
        except:
            pass
        bar.ParentForm.RootNeedsDestroying = False
        return False

    return rc


# ============================== EASY PROGRESS METER ========================================== #
# class to hold the easy meter info (a global variable essentialy)
class EasyProgressMeterDataClass():
    def __init__(self, title='', current_value=1, max_value=10, start_time=None, stat_messages=()):
        self.Title = title
        self.CurrentValue = current_value
        self.MaxValue = max_value
        self.StartTime = start_time
        self.StatMessages = stat_messages
        self.ParentForm = None
        self.MeterID = None
        self.MeterText = None

    # ===========================  COMPUTE PROGRESS STATS ======================#
    def ComputeProgressStats(self):
        utc = datetime.datetime.utcnow()
        time_delta = utc - self.StartTime
        total_seconds = time_delta.total_seconds()
        if not total_seconds:
            total_seconds = 1
        try:
            time_per_item = total_seconds / self.CurrentValue
        except:
            time_per_item = 1
        seconds_remaining = (self.MaxValue - self.CurrentValue) * time_per_item
        time_remaining = str(datetime.timedelta(seconds=seconds_remaining))
        time_remaining_short = (time_remaining).split(".")[0]
        time_delta_short = str(time_delta).split(".")[0]
        total_time = time_delta + datetime.timedelta(seconds=seconds_remaining)
        total_time_short = str(total_time).split(".")[0]
        self.StatMessages = [
            '{} of {}'.format(self.CurrentValue, self.MaxValue),
            '{} %'.format(100 * self.CurrentValue // self.MaxValue),
            '',
            ' {:6.2f} Iterations per Second'.format(self.CurrentValue / total_seconds),
            ' {:6.2f} Seconds per Iteration'.format(total_seconds / (self.CurrentValue if self.CurrentValue else 1)),
            '',
            '{} Elapsed Time'.format(time_delta_short),
            '{} Time Remaining'.format(time_remaining_short),
            '{} Estimated Total Time'.format(total_time_short)]
        return


# ============================== EasyProgressMeter  =====#
def EasyProgressMeter(title, current_value, max_value, *args, orientation=None, bar_color=(None, None),
                      button_color=None, size=DEFAULT_PROGRESS_BAR_SIZE, border_width=None):
    '''
    A ONE-LINE progress meter. Add to your code where ever you need a meter. No need for a second
    function call before your loop. You've got enough code to write!
    :param title: Title will be shown on the window
    :param current_value: Current count of your items
    :param max_value: Max value your count will ever reach. This indicates it should be closed
    :param args:  VARIABLE number of arguements... you request it, we'll print it no matter what the item!
    :param orientation:
    :param bar_color:
    :param size:
    :param Style:
    :param StyleOffset:
    :return: False if should stop the meter
    '''
    local_border_width = DEFAULT_PROGRESS_BAR_BORDER_WIDTH if not border_width else border_width
    # STATIC VARIABLE!
    # This is a very clever form of static variable using a function attribute
    # If the variable doesn't yet exist, then it will create it and initialize with the 3rd parameter
    EasyProgressMeter.Data = getattr(EasyProgressMeter, 'Data', EasyProgressMeterDataClass())
    # if no meter currently running
    if EasyProgressMeter.Data.MeterID is None:  # Starting a new meter
        print(
            "Please change your call of EasyProgressMeter to use OneLineProgressMeter. EasyProgressMeter will be removed soon")
        if int(current_value) >= int(max_value):
            return False
        del (EasyProgressMeter.Data)
        EasyProgressMeter.Data = EasyProgressMeterDataClass(title, 1, int(max_value), datetime.datetime.utcnow(), [])
        EasyProgressMeter.Data.ComputeProgressStats()
        message = "\n".join([line for line in EasyProgressMeter.Data.StatMessages])
        EasyProgressMeter.Data.MeterID, EasyProgressMeter.Data.MeterText = _ProgressMeter(title, int(max_value),
                                                                                          message, *args,
                                                                                          orientation=orientation,
                                                                                          bar_color=bar_color,
                                                                                          size=size,
                                                                                          button_color=button_color,
                                                                                          border_width=local_border_width)
        EasyProgressMeter.Data.ParentForm = EasyProgressMeter.Data.MeterID.ParentForm
        return True
    # if exactly the same values as before, then ignore.
    if EasyProgressMeter.Data.MaxValue == max_value and EasyProgressMeter.Data.CurrentValue == current_value:
        return True
    if EasyProgressMeter.Data.MaxValue != int(max_value):
        EasyProgressMeter.Data.MeterID = None
        EasyProgressMeter.Data.ParentForm = None
        del (EasyProgressMeter.Data)
        EasyProgressMeter.Data = EasyProgressMeterDataClass()  # setup a new progress meter
        return True  # HAVE to return TRUE or else the new meter will thing IT is failing when it hasn't
    EasyProgressMeter.Data.CurrentValue = int(current_value)
    EasyProgressMeter.Data.MaxValue = int(max_value)
    EasyProgressMeter.Data.ComputeProgressStats()
    message = ''
    for line in EasyProgressMeter.Data.StatMessages:
        message = message + str(line) + '\n'
    message = "\n".join(EasyProgressMeter.Data.StatMessages)
    args = args + (message,)
    rc = _ProgressMeterUpdate(EasyProgressMeter.Data.MeterID, current_value,
                              EasyProgressMeter.Data.MeterText, *args)
    # if counter >= max then the progress meter is all done. Indicate none running
    if current_value >= EasyProgressMeter.Data.MaxValue or not rc:
        EasyProgressMeter.Data.MeterID = None
        del (EasyProgressMeter.Data)
        EasyProgressMeter.Data = EasyProgressMeterDataClass()  # setup a new progress meter
        return False  # even though at the end, return True so don't cause error with the app
    return rc  # return whatever the update told us


def EasyProgressMeterCancel(title, *args):
    EasyProgressMeter.EasyProgressMeterData = getattr(EasyProgressMeter, 'EasyProgressMeterData',
                                                      EasyProgressMeterDataClass())
    if EasyProgressMeter.EasyProgressMeterData.MeterID is not None:
        # tell the normal meter update that we're at max value which will close the meter
        rc = EasyProgressMeter(title, EasyProgressMeter.EasyProgressMeterData.MaxValue,
                               EasyProgressMeter.EasyProgressMeterData.MaxValue, ' *** CANCELLING ***',
                               'Caller requested a cancel', *args)
        return rc
    return True


# global variable containing dictionary will all currently running one-line progress meters.
_one_line_progress_meters = {}


# ============================== OneLineProgressMeter  =====#
def OneLineProgressMeter(title, current_value, max_value, key, *args, orientation=None, bar_color=(None, None),
                         button_color=None, size=DEFAULT_PROGRESS_BAR_SIZE, border_width=None, grab_anywhere=False):
    global _one_line_progress_meters

    local_border_width = DEFAULT_PROGRESS_BAR_BORDER_WIDTH if border_width is not None else border_width
    try:
        meter_data = _one_line_progress_meters[key]
    except:  # a new meater is starting
        if int(current_value) >= int(max_value):  # if already expired then it's an old meter, ignore
            return False
        meter_data = EasyProgressMeterDataClass(title, 1, int(max_value), datetime.datetime.utcnow(), [])
        _one_line_progress_meters[key] = meter_data
        meter_data.ComputeProgressStats()
        message = "\n".join([line for line in meter_data.StatMessages])
        meter_data.MeterID, meter_data.MeterText = _ProgressMeter(title, int(max_value), message, *args,
                                                                  orientation=orientation, bar_color=bar_color,
                                                                  size=size, button_color=button_color,
                                                                  border_width=local_border_width,
                                                                  grab_anywhere=grab_anywhere)
        meter_data.ParentForm = meter_data.MeterID.ParentForm
        return True

    # if exactly the same values as before, then ignore, return success.
    if meter_data.MaxValue == max_value and meter_data.CurrentValue == current_value:
        return True
    meter_data.CurrentValue = int(current_value)
    meter_data.MaxValue = int(max_value)
    meter_data.ComputeProgressStats()
    message = ''
    for line in meter_data.StatMessages:
        message = message + str(line) + '\n'
    message = "\n".join(meter_data.StatMessages)
    args = args + (message,)
    rc = _ProgressMeterUpdate(meter_data.MeterID, current_value,
                              meter_data.MeterText, *args)
    # if counter >= max then the progress meter is all done. Indicate none running
    if current_value >= meter_data.MaxValue or not rc:
        del _one_line_progress_meters[key]
        return False
    return rc  # return whatever the update told us


def OneLineProgressMeterCancel(key):
    global _one_line_progress_meters

    try:
        meter_data = _one_line_progress_meters[key]
    except:  # meter is already deleted
        return
    OneLineProgressMeter('', meter_data.MaxValue, meter_data.MaxValue, key=key)


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
_easy_print_data = None  # global variable... I'm cheating


class DebugWin():
    def __init__(self, size=(None, None), location=(None, None), font=None, no_titlebar=False, no_button=False,
                 grab_anywhere=False, keep_on_top=False):
        # Show a form that's a running counter
        win_size = size if size != (None, None) else DEFAULT_DEBUG_WINDOW_SIZE
        self.window = Window('Debug Window', no_titlebar=no_titlebar, auto_size_text=True, location=location,
                             font=font or ('Courier New', 10), grab_anywhere=grab_anywhere, keep_on_top=keep_on_top)
        self.output_element = Output(size=win_size)
        if no_button:
            self.layout = [[self.output_element]]
        else:
            self.layout = [
                [self.output_element],
                [DummyButton('Quit')]
            ]
        self.window.AddRows(self.layout)
        self.window.Read(timeout=0)  # Show a non-blocking form, returns immediately
        return

    def Print(self, *args, end=None, sep=None):
        sepchar = sep if sep is not None else ' '
        endchar = end if end is not None else '\n'

        if self.window is None:  # if window was destroyed already, just print
            print(*args, sep=sepchar, end=endchar)
            return

        event, values = self.window.Read(timeout=0)
        if event == 'Quit' or event is None:
            self.Close()
        print(*args, sep=sepchar, end=endchar)
        # Add extra check to see if the window was closed... if closed by X sometimes am not told
        try:
            state = self.window.TKroot.state()
        except:
            self.Close()

    def Close(self):
        self.window.Close()
        self.window = None


def PrintClose():
    EasyPrintClose()


def EasyPrint(*args, size=(None, None), end=None, sep=None, location=(None, None), font=None, no_titlebar=False,
              no_button=False, grab_anywhere=False, keep_on_top=False):
    global _easy_print_data

    if _easy_print_data is None:
        _easy_print_data = DebugWin(size=size, location=location, font=font, no_titlebar=no_titlebar,
                                    no_button=no_button, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top)
    _easy_print_data.Print(*args, end=end, sep=sep)


Print = EasyPrint
eprint = EasyPrint


def EasyPrintClose():
    global _easy_print_data
    if _easy_print_data is not None:
        _easy_print_data.Close()
        _easy_print_data = None


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
    form.Close()
    return button


ScrolledTextBox = PopupScrolled


# ============================== SetGlobalIcon ======#
# Sets the icon to be used by default                #
# ===================================================#
def SetGlobalIcon(icon):
    global _my_windows

    try:
        with open(icon, 'r') as icon_file:
            pass
    except:
        raise FileNotFoundError
    _my_windows.user_defined_icon = icon
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
    global _my_windows

    if icon:
        try:
            with open(icon, 'r') as icon_file:
                pass
        except:
            raise FileNotFoundError
        _my_windows.user_defined_icon = icon

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
LOOK_AND_FEEL_TABLE = {'SystemDefault':
                           {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
                            'TEXT': COLOR_SYSTEM_DEFAULT,
                            'INPUT': COLOR_SYSTEM_DEFAULT, 'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
                            'SCROLL': COLOR_SYSTEM_DEFAULT,
                            'BUTTON': OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR,
                            'PROGRESS': COLOR_SYSTEM_DEFAULT,
                            'BORDER': 1, 'SLIDER_DEPTH': 1,
                            'PROGRESS_DEPTH': 0},

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
                                   'BORDER': 1, 'SLIDER_DEPTH': 0,
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

                       'Dark': {'BACKGROUND': 'gray25',
                                'TEXT': 'white',
                                'INPUT': 'gray30',
                                'TEXT_INPUT': 'white',
                                'SCROLL': 'gray44',
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

                       'Dark2': {'BACKGROUND': 'gray25',
                                 'TEXT': 'white',
                                 'INPUT': 'white',
                                 'TEXT_INPUT': 'black',
                                 'SCROLL': 'gray44',
                                 'BUTTON': ('white', '#004F00'),
                                 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                 'BORDER': 1,
                                 'SLIDER_DEPTH': 0,
                                 'PROGRESS_DEPTH': 0},

                       'Black': {'BACKGROUND': 'black',
                                 'TEXT': 'white',
                                 'INPUT': 'gray30',
                                 'TEXT_INPUT': 'white',
                                 'SCROLL': 'gray44',
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
                                    'INPUT': '#dfedf2', 'SCROLL': '#dfedf2',
                                    'TEXT_INPUT': 'black',
                                    'BUTTON': ('white', '#183440'),
                                    'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR,
                                    'BORDER': 1,
                                    'SLIDER_DEPTH': 0,
                                    'PROGRESS_DEPTH': 0}
                       }


def ListOfLookAndFeelValues():
    return list(LOOK_AND_FEEL_TABLE.keys())


def ChangeLookAndFeel(index):
    # global LOOK_AND_FEEL_TABLE

    if sys.platform == 'darwin':
        print('*** Changing look and feel is not supported on Mac platform ***')
        return

    # look and feel table

    try:
        colors = LOOK_AND_FEEL_TABLE[index]

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

# ----------------------------------- The mighty Popup! ------------------------------------------------------------ #

def Popup(*args, button_color=None, background_color=None, text_color=None, button_type=POPUP_BUTTONS_OK,
          auto_close=False, auto_close_duration=None, custom_text=(None, None), non_blocking=False,
          icon=DEFAULT_WINDOW_ICON, line_width=None,
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
    title = args_to_print[0] if args_to_print[0] is not None else 'None'
    window = Window(title, auto_size_text=True, background_color=background_color, button_color=button_color,
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
            window.AddRow(PopupButton(custom_text, size=(len(custom_text), 1), button_color=button_color, focus=True,
                                      bind_return_key=True))
        elif custom_text[1] is None:
            window.AddRow(
                PopupButton(custom_text[0], size=(len(custom_text[0]), 1), button_color=button_color, focus=True,
                            bind_return_key=True))
        else:
            window.AddRow(PopupButton(custom_text[0], button_color=button_color, focus=True, bind_return_key=True,
                                      size=(len(custom_text[0]), 1)),
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
    Popup(*args, button_color=button_color, background_color=background_color, text_color=text_color,
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
                   auto_close=True, auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON,
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


def PopupGetFolder(message, default_path='', no_window=False, size=(None, None), button_color=None,
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

    global _my_windows

    if no_window:
        if _my_windows._NumOpenWindows:
            root = tk.Toplevel()
        else:
            root = tk.Tk()
        try:
            root.attributes('-alpha', 0)  # hide window while building it. makes for smoother 'paint'
        except:
            pass
        folder_name = tk.filedialog.askdirectory()  # show the 'get folder' dialog box
        root.destroy()
        return folder_name

    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=size, key='_INPUT_'), FolderBrowse(initial_folder=initial_folder)],
              [Button('Ok', size=(5, 1), bind_return_key=True), Button('Cancel', size=(5, 1))]]

    window = Window(title=message, layout=layout, icon=icon, auto_size_text=True, button_color=button_color,
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

def PopupGetFile(message, default_path='', default_extension='', save_as=False, file_types=(("ALL Files", "*.*"),),
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

    global _my_windows

    if no_window:
        if _my_windows._NumOpenWindows:
            root = tk.Toplevel()
        else:
            root = tk.Tk()
        try:
            root.attributes('-alpha', 0)  # hide window while building it. makes for smoother 'paint'
        except:
            pass
        if save_as:
            filename = tk.filedialog.asksaveasfilename(filetypes=file_types,
                                                       defaultextension=default_extension)  # show the 'get file' dialog box
        else:
            filename = tk.filedialog.askopenfilename(filetypes=file_types,
                                                     defaultextension=default_extension)  # show the 'get file' dialog box
        root.destroy()
        return filename

    browse_button = SaveAs(file_types=file_types, initial_folder=initial_folder) if save_as else FileBrowse(
        file_types=file_types, initial_folder=initial_folder)

    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=size, key='_INPUT_'), browse_button],
              [Button('Ok', size=(6, 1), bind_return_key=True), Button('Cancel', size=(6, 1))]]

    window = Window(title=message, layout = layout, icon=icon, auto_size_text=True, button_color=button_color, font=font,
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

def PopupGetText(message, default_text='', password_char='', size=(None, None), button_color=None,
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
              [Button('Ok', size=(5, 1), bind_return_key=True), Button('Cancel', size=(5, 1))]]

    window = Window(title=message, layout=layout, icon=icon, auto_size_text=True, button_color=button_color, no_titlebar=no_titlebar,
                    background_color=background_color, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    button, values = window.Read()
    window.Close()
    if button != 'Ok':
        return None
    else:
        path = values['_INPUT_']
        return path


change_look_and_feel = ChangeLookAndFeel
easy_print = EasyPrint
easy_print_close = EasyPrintClose
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
rgb = RGB
scrolled_text_box = ScrolledTextBox
set_global_icon = SetGlobalIcon
set_options = SetOptions
timer_start = TimerStart
timer_stop = TimerStop
sprint = sprint


def main():
    ChangeLookAndFeel('GreenTan' )

    # Popup('Popup Test')

    # SetOptions(background_color='blue', text_element_background_color='blue', text_color='white')
    # layout = [[Text('You are running the PySimpleGUI.py file itself', font='Any 25', size=(60,1), tooltip='My tooltip!')],
    #           [Text('You should be importing it rather than running it', size=(60, 1))],
    #           [Text('Here is your sample window....')],
    #           [Text('Source Folder', justification='right', size=(40,1)), InputText('Source', focus=True, disabled=True),
    #            FolderBrowse()],
    #           [Text('Destination Folder', justification='right', size=(40,1)), InputText('Dest'), FolderBrowse()],
    #           [Ok(), Cancel(disabled=True), Exit(tooltip='Exit button'), Button('Hidden Button', visible=False)]]

    menu_def = [['&File', ['&Open', '&Save', 'E&xit', 'Properties']],
                ['&Edit', ['Paste', ['Special', 'Normal', ], '!Undo'], ],
                ['!&Disabled', ['Paste', ['Special', 'Normal', ], '!Undo'], ],
                ['&Help', '&About...'], ]


    menu_def = [['File',  ['&Open::mykey', '&Save', 'E&xit', 'Properties']],
                ['Edit', ['!Paste', ['Special', 'Normal', ], '!Undo'], ],
                ['!Disabled', ['Has Sub', ['Item1', 'Item2', ], 'No Sub'], ],
                ['Help', 'About...'], ]

    col1 = [[Text('Column 1 line  1', background_color='red')], [Text('Column 1 line 2')]]

    layout = [
        [Menu(menu_def, key='_MENU_', text_color='yellow', background_color='#475841',  font='Courier 14')],
        # [T('123435', size=(1,8))],
        [Text('PySimpleGUIWeb Welcomes You...', tooltip='text', font=('Comic sans ms', 20),size=(40,1), text_color='red', enable_events=False, key='_PySimpleGUIWeb_')],
        # [OptionMenu([])],
        [T('System platform = %s'%sys.platform)],
        [Image(data=DEFAULT_BASE64_ICON, enable_events=False)],
        [Image(filename=r'C:\Python\PycharmProjects\GooeyGUI\logo200.png')],
        [Text('VERSION {}'.format(version), text_color='red', font='Courier 24')],
        [T('Current Time '), Text('Text', key='_TEXT_', font='Arial 18', text_color='black', size=(30,1)), Column(col1, background_color='red')],
        [T('Up Time'), Text('Text', key='_TEXT_UPTIME_', font='Arial 18', text_color='black', size=(30,1))],
        [Input('Single Line Input', do_not_clear=True, enable_events=False, size=(30, 1), text_color='red', key='_IN_')],
        [Multiline('Multiline Input', do_not_clear=True, size=(40, 4), enable_events=False, key='_MULTI_IN_')],
        # [Output(size=(60,10))],
        [MultilineOutput('Multiline Output', size=(80, 8), text_color='blue', font='Courier 12', key='_MULTIOUT_', autoscroll=True)],
        [Checkbox('Checkbox 1', enable_events=False, key='_CB1_'), Checkbox('Checkbox 2', default=True, key='_CB2_', enable_events=False)],
        [Combo(values=['Combo 1', 'Combo 2', 'Combo 3'], default_value='Combo 2', key='_COMBO_', enable_events=False,
               readonly=False, tooltip='Combo box', disabled=False, size=(12, 1))],
        [Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), enable_events =True, size=(10, 3), key='_LIST_')],
        # [Image(filename=r'C:\Python\PycharmProjects\GooeyGUI\logo200.png', enable_events=False)],
        [Slider((1, 100), default_value=80, key='_SLIDER_', visible=True, enable_events=False, orientation='v')],
        [Spin(values=(1, 2, 3), initial_value='2', size=(4, 1), key='_SPIN_', enable_events=False)],
        [OK(), Button('Hidden', visible=False, key='_HIDDEN_'), Button('Values'), Button('Exit', button_color=('white', 'red')), Button('UnHide'), B('Popup')]
    ]

    window = Window('PySimpleGUIWeb Test Harness Window', layout,
                    font='Arial 18',
                    icon=DEFAULT_BASE64_ICON,
                    default_element_size=(12,1),
                     auto_size_buttons=False)

    start_time = datetime.datetime.now()
    while True:
        event, values = window.Read(timeout=None)
        window.Element('_TEXT_').Update(str(datetime.datetime.now()))
        window.Element('_TEXT_UPTIME_').Update(str(datetime.datetime.now()-start_time))
        print(event, values) if event != TIMEOUT_KEY else None
        if event in (None, 'Exit'):
            break
        elif event == 'OK':
            window.Element('_MULTIOUT_').Update('You clicked the OK button', append=True)
            window.Element('_PySimpleGUIWeb_').Widget.style['background-image'] = "url('/my_resources:mine.png')"

        elif event == 'Values':
            window.Element('_MULTIOUT_').Update(str(values), append=True)
            nav = remi.gui.FileFolderNavigator(False,r'a:\TEMP', True, False)
            # here is returned the Input Dialog widget, and it will be shown
            # fileselectionDialog.show(window.Element('_IN_').Widget)

        elif event != TIMEOUT_KEY:
            window.Element('_MULTIOUT_').Update('EVENT: ' + str(event), append=True)
        if event == 'Popup':
            Popup('This is a popup!')
        if event == 'UnHide':
            print('Unhiding...')
            window.Element('_HIDDEN_').Update(visible=True)

    window.Close()


if __name__ == '__main__':
    main()
    exit(69)
