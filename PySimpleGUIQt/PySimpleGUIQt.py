#!/usr/bin/python3
version = __version__ = "0.35.0.12 Unreleased\nMassive update of docstrings (thanks nngogol), default for slider tick interval set automatically now, margins added to Window but not yet hooked up, VSeparator added (spelling error), added Radio.reset_group and removed clearing all when one of them is cleared (recent change), added default key for one_line_progress_meter, auto-add keys to tables & trees, InputText element gets new disabled-readonly foreground and background color settings and also a readonly parameter, InputText gets border_width parameter, fixed up some docstrings, popup gets new image and any_key_closes parms, input type popups also get image parameter, error checks for trying to manipulate a window prior to finalize, added a dummy Element.expand method, added theme_add_new, added Window.set_title"

port = 'PySimpleGUIQt'

import sys
import datetime
import textwrap
import pickle
import random
import warnings
try:        # Because Raspberry Pi is still on 3.4....it's not critical if this module isn't imported on the Pi
    from typing import List, Any, Union, Tuple, Dict    # because this code has to run on 2.7 can't use real type hints.  Must do typing only in comments
except:
    print('*** Skipping import of Typing module. "pip3 install typing" to remove this warning ***')

######           #####                                       #####   #     #  ###   #####
#     #  #   #  #     #  #  #    #  #####   #       ######  #     #  #     #   #   #     #  #####
#     #   # #   #        #  ##  ##  #    #  #       #       #        #     #   #   #     #    #
######     #     #####   #  # ## #  #    #  #       #####   #  ####  #     #   #   #     #    #
#          #          #  #  #    #  #####   #       #       #     #  #     #   #   #   # #    #
#          #    #     #  #  #    #  #       #       #       #     #  #     #   #   #    #     #
#          #     #####   #  #    #  #       ######  ######   #####    #####   ###   #### #    #

from PySide2.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QComboBox, QFormLayout, QVBoxLayout, QHBoxLayout, QListWidget, QDial, QTableWidget
from PySide2.QtWidgets import QSlider, QCheckBox, QRadioButton, QSpinBox, QPushButton, QTextEdit, QMainWindow, QDialog, QAbstractItemView
from PySide2.QtWidgets import QSpacerItem, QFrame, QGroupBox, QTextBrowser, QPlainTextEdit, QButtonGroup, QFileDialog, QTableWidget, QTabWidget, QTabBar, QTreeWidget, QTreeWidgetItem, QLayout, QTreeWidgetItemIterator, QProgressBar
from PySide2.QtWidgets import QTableWidgetItem, QGraphicsView, QGraphicsScene, QGraphicsItemGroup, QMenu, QMenuBar, QAction, QSystemTrayIcon, QColorDialog
from PySide2.QtGui import QPainter, QPixmap, QPen, QColor, QBrush, QPainterPath, QFont, QImage, QIcon
from PySide2.QtCore import Qt,QProcess, QEvent, QSize
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets

using_pyqt5 = False



"""
    The QT version if PySimpleGUI.
    Still being developed.  Very limited features.  Been in development for less than 2 days so don't expect much!!
    
    So far can interact with the basic Widgets and get button clicks back.  Can't yet read which button caused the event.
"""

DEFAULT_BASE64_ICON = b'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'


FACE_PALM = b'iVBORw0KGgoAAAANSUhEUgAAAEkAAAA8CAMAAAAdQmecAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAAB8SDx4UEiAUDyAUEiMZFSUbGSsUEy8aFiwbGTsUFTkdICwiHTIjHDQrHzsiGysjIjIlIDMqIzMsKjsgIzotID0uKT01IzszMUkYHE0ZIFkbKEQhHkUqH0sgHUUgI0MtIkUoKEsmIEwqIkwqL00rM0I1I0s1JEswKE04J0w7LUc9OVYpJ1omMVM0JVQ1K1I4JVU7KlszK1k6J1s7KVw4NGEdLmQeMWghNmE5LWQ4NXIiPWs2RHkkQnAzRVRENVNDOF1ENFxEOVpKOWNDM2NHPWNMPGxFOWxKPG9QPnJKPHVQP05HRFJMSltUUWpLQ2lUQ2NcWndNQndIU3JUQ3JUSHRZTHxSRHxVSHxZSnlaVH1YYmZgX39gVmZjYnZran14doFURoNWSYNbTYNeUoleUItbaYRgT4VhU4JiWIVoXIpjVIxlWo1oVo1pWpFiVpFlWZJsXZRxX4JmZYVsY4trY4pzaoN9e5NtYpRtaJltY5ZxYpRyaZpzZZx1ap14a5N4eJx1cJp3eJ15cZp6eqB2a6J6baN8cqJ7eax9cah+epx7hImBf5uBeqWAdKOCe6qCdKqDequJfbKJfY2EgpmIiZqVk52Zk6SBhKaFiKyDgqqFiayJgqyNi6aLkayNlKGQi6uRja+QlqySm6qZlLKMhLKOi7SRi76Th7qTi7KTk7KVm7KYk7SZm7iWk7yZk7ucm7Sco7ScqbqeorOfsK2knrmhnKukoqyop7GrqrqhpLqlq7mup7urqrSosbKuubqjsrymubyps7qqub6xrbSxsLizvbe1wr68ycKYi8OcmsCmo8KmqcGup8Ooq8qqqcersMGvv8yutMKxu8uwtM2zusy+v9G3usCwwsS0yca8xsW7y82/x8m9ysm90Ne8wMjAvMPCxsLAyc3Ax8vAy8/IzMbD0c3F08zK2NPLx9DJztnBydLO09LL2tPS19TS29rU29bU4dnT5NzV6NvZ4+Hf5uDd6+Pi7eXj8ejl9Ozp9/Lw+wAAAAAAAAAAAAAAAErQjXwAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAHU0lEQVRYR5WWf1gbZx3A8bw2y7nJVq00ZM9Eq63t0o3QFNKkrLbjoRjXsWFHCI+T0gNNe2nWm4Ndm9xFTLmj1UFONsUU1s2aZRRxdP7otNZN1Omc1inTdbad06danzlkVoR2/hG/7w8gNG/Y9iE/uPf9vp/7vt/37r0UZPLx34nxiYmJNybp4VuSxzQ9MXn5zempqelLlybfpotteu31ifFzfzp7/sL45PT09MS/aPOCME1jZ8+fGxs9Njw0fGLswuT01D/+SjsWgmU6fnJs7IUTx7410N8/MDx64eKlqV++DRXD9M2BkZOnfjicTvV0d/f0Hx09f/HNf//iL7QzP7mmn0XN9BMjR9PpfhOpkkdHz0z97+9PT9DuvOSa7gvHus2vYEzT6E4MDP10/PKlM0/T7rzkmoLBeyORWMwwzf6UaZowvydPX7z8nzPP0v585JhO7pIkWZbvVXUzlUomzYNmcui7L49fvPDs6zQiDzmmr9UHg7vDu8MRVTcOHESq5KEjz7z8yitnfkwj8pBr2njHNjEo7ZbliGFAQsk+eB155vTpc6f/RkPY5JiOr7i1uh5UYUVROw4ehEolk1193zj2k9+NLpxUbsWXrt5YfdfnpDAUS9UgLaCrq2/g6JETT9IINrmmJStWb9wUCKK6K0h1wDCMDs1IHjr8Tk23F63aeOsdooSXUNU6O7QOTdM7937x0NAbNIRJrumrS4tWb64OiFKrJEshWdnXqWr7QqGO/fuHztIQJrmmzKKiFauc9aLYIkp7xHvkfXtCLSG5Y+TU1w8foRFMGKat7y1asbLaH/CLkNeO5h2trZJk/Oq3I/uHh/9IQ1gwTD+4qnBpkbPK5xf9zTua/c1+fyT1WLLnvi+8MPwoDWHBMEWDjuuFpc5P+Hz3iM3Ndb5mPZVOKfU93xnqj/2GxjDINb3q8PicJYUly2vkutZWURR1PdErtwz8+vloQPk+DWLAyMnjWb58ZUnhrsf3SJ9s8fl1TVWlwODzI/HaxrYFpscw1fscxY7Slc7Yc5LkatDhTpZE3YzH133+1EsP0RgGDNOPqm74cJWrtHRbond9Q0LVdSmsmWa4rf3Ffw4/QmMYMEyZ9rIy502u0hpDlRK6HtNN40BCjI68+IeBtndWp0xmU5VrpWttFdqiensff27QjIuxwf6+/Y13v0YjGDBNr25yrV3rqoL7t7fX1A/0Girs6Eqw7fcPfJlGMGCaMt+rdt7k3Natqwkjpmnm4BNpQ27o+fNLD7yL4xYt+/RxGjYPtimTKSxxqYluEOm63psaTBtB89tDfe2LeY7neW7xnT+ncXPkMT109aoaJaYaugY7CmxSj6UHU12haNPV4EFw3I00cpY8psWLVlcHIxFdVTUtFod9Lm0aO+/adSMVAZy1icZSmKb738fzSzY1yJCRYcBGF48qWpdW11j/AapBQMW203gMw7SVRG4ORBKaqsXjWjSqaRGldkvV5utIF8JqFazWB+kQRI5pK4eLyvPVElQbyqRF92rxDll0rK+pXQRd8LK+/6MbNtzidrvXHKOjgCtMTVTD8++uDet6J1RJaVOie5XglrK6xlrUYf3QOo8HLG6v1+uuOEwHXmHajs45w05Fhx3c0JRQOBRUAi7P+pprIJuPrHHY7cXwZ3eAraJ8Nqss01NLqANzTbumxLSIrijhnTvDQWepq+x6oVAQBAuCh7dgs9sryj10dJbpttmJYT7eDlWOaJEwiO5uuRlJLNDMcSgK3lBOjkeyE3Q8NW1fNk8D1WiD9YJnZ1gOB1sCH0MK2oO/LYIF0gO3RWgkBmJ6cG51yRk5vkbR1IgcDisxWWwoIX0ILBAEm2AjCPx7sIeYbpvLx3odmgLPCaFIREY/WGDnrYOM5sAqUNgJNkEgImRaTGN44YPF0AFYhJsDIXicS/I+EC2n3QBHc7LZYO0q0KXgtttmTdfijDhLMQAiGxxYINK3Ax6ccqcq3jCzVrBaWAKdOKNyckk56N5esJ3UBqLQrAGYHg531CGV5ENtuAEDuSDWVKCMvN5Kb6X7s9R0O8poZvZ4FB0n2MrqGhr8vjLSij5JnYnMDSpIqbLS66amZbOiOSB9PNzmqdtSVVhL2rAcXtCHTeVIVQl4yfQKrs0WoWuNDKLp2dZ5eCvVzkGSmlWRpMCEhtORxIqj8TEBH88ja4IoKfxrqAC2wbmxUG0O7id6NAM+no+9GMuo6hZs+gxZKQQaRTPMFjFMUCuaFlo/Mr2CJkgJReNPfIFfmRM+ZIBVFfhS+BLOCZWb3C7kPofLEkM0CNqQy4zKuwGZ7iTRWIURIPW3mt0MMyo0vYL7s64luCt4Hu6ZeR4EHcgAuaBYcJ0XZPATAC0ampyAJ0fHz0IGZTPXiFTgQiYyJwAnh+pNd4QsZrcjgDYB5Bir7BvAhB5vKCvUZ+F4vMQ4cB54EP0/C2ik9/TDBZmnyG6BGqHuWJR9XvqdD2yCXcq+Dna6JtpIYJ15QWB+5W6v+1P/B0gPXHqaGwimAAAAAElFTkSuQmCC'


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
    print(int(g_time_delta*1000))


"""
    Welcome to the "core" PySimpleGUI code....

    It's a mess.... really... it's a mess internally... it's the external-facing interfaces that
    are not a mess.  The Elements and the methods for them are well-designed.
    PEP8 - this code is far far from PEP8 compliant. 
    It was written PRIOR to learning that PEP8 existed. 

    The variable and function naming in particular are not compliant.  There is
    liberal use of CamelVariableAndFunctionNames.  If you've got a serious enough problem with this
    that you'll pass on this package, then that's your right and I invite you to do so.  However, if
    perhaps you're a practical thinker where it's the results that matter, then you'll have no
    trouble with this code base.  There is consisency however.  

    I truly hope you get a lot of enjoyment out of using PySimpleGUI.  It came from good intentions.
"""

# ----====----====----==== Constants the user CAN safely change ====----====----====----#
DEFAULT_WINDOW_ICON = DEFAULT_BASE64_ICON
DEFAULT_ELEMENT_SIZE = (250, 22)  # In PIXELS
DEFAULT_BUTTON_ELEMENT_SIZE = (80, 25 )  # In PIXELS
DEFAULT_MARGINS = (10, 5)  # Margins for each LEFT/RIGHT margin is first term
DEFAULT_ELEMENT_PADDING = (4, 2)  # Padding between elements (row, col) in pixels
# DEFAULT_ELEMENT_PADDING = (0, 0)  # Padding between elements (row, col) in pixels
DEFAULT_PIXELS_TO_CHARS_SCALING = (10,35)      # 1 character represents x by y pixels
DEFAULT_PIXELS_TO_CHARS_SCALING_MULTILINE_TEXT = (10,20)      # 1 character represents x by y pixels
DEFAULT_PIXEL_TO_CHARS_CUTOFF = 15             # number of chars that triggers using pixels instead of chars
DEFAULT_PIXEL_TO_CHARS_CUTOFF_MULTILINE = 70             # number of chars that triggers using pixels instead of chars
DEFAULT_AUTOSIZE_TEXT = True
DEFAULT_AUTOSIZE_BUTTONS = True
DEFAULT_FONT = ("Helvetica", 10)
DEFAULT_TEXT_JUSTIFICATION = 'left'
DEFAULT_BORDER_WIDTH = 1
DEFAULT_AUTOCLOSE_TIME = 3  # time in seconds to show an autoclose form
DEFAULT_DEBUG_WINDOW_SIZE = (800, 400)
DEFAULT_WINDOW_LOCATION = (None, None)
MAX_SCROLLED_TEXT_BOX_HEIGHT = 50
DEFAULT_TOOLTIP_TIME = 400
DEFAULT_TOOLTIP_OFFSET = (20,-20)
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

DEFAULT_BUTTON_COLOR = ('white', BLUES[0])  # Foreground, Background (None, None) == System Default
OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR = ('white', BLUES[0])  # Colors should never be this long


CURRENT_LOOK_AND_FEEL = 'DarkBlue3'

DEFAULT_ERROR_BUTTON_COLOR = ("#FFFFFF", "#FF0000")
DEFAULT_BACKGROUND_COLOR = None
DEFAULT_ELEMENT_BACKGROUND_COLOR = None
DEFAULT_ELEMENT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR = None
DEFAULT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_INPUT_ELEMENTS_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_INPUT_TEXT_COLOR = COLOR_SYSTEM_DEFAULT
DEFAULT_SCROLLBAR_COLOR = None

# A transparent button is simply one that matches the background
TRANSPARENT_BUTTON = 'This constant has been depricated. You must set your button background = background it is on for it to be transparent appearing'
# --------------------------------------------------------------------------------
# Progress Bar Relief Choices
RELIEF_RAISED = 'raised'
RELIEF_SUNKEN = 'sunken'
RELIEF_FLAT = 'flat'
RELIEF_RIDGE = 'ridge'
RELIEF_GROOVE = 'groove'
RELIEF_SOLID = 'solid'

RELIEF_TICK_POSITION_NO_TICKS = 'none'
RELIEF_TICK_POSITION_BOTH_SIDES = 'both'
RELIEF_TICK_POSITION_ABOVE = 'above'
RELIEF_TICK_POSITION_BELOW = 'below'
RELIEF_TICK_POSITION_LEFT = 'left'
RELIEF_TICK_POSITION_RIGHT = 'right'


DEFAULT_PROGRESS_BAR_COLOR = (GREENS[0], '#D0D0D0')  # a nice green progress bar
DEFAULT_PROGRESS_BAR_COLOR_OFFICIAL = (GREENS[0], '#D0D0D0')  # a nice green progress bar
DEFAULT_PROGRESS_BAR_SIZE = (200, 20)  # Size of Progress Bar (characters for length, pixels for width)
DEFAULT_PROGRESS_BAR_BORDER_WIDTH = 1
DEFAULT_PROGRESS_BAR_RELIEF = RELIEF_GROOVE
PROGRESS_BAR_STYLES = ('default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative')
DEFAULT_PROGRESS_BAR_STYLE = 'default'
DEFAULT_METER_ORIENTATION = 'Horizontal'
DEFAULT_SLIDER_ORIENTATION = 'vertical'
DEFAULT_SLIDER_BORDER_WIDTH = 1

DEFAULT_SLIDER_RELIEF = RELIEF_TICK_POSITION_BOTH_SIDES
DEFAULT_FRAME_RELIEF = 'groove'

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

TABLE_SELECT_MODE_NONE = 'NONE'
TABLE_SELECT_MODE_BROWSE = 'BROWSE'
TABLE_SELECT_MODE_EXTENDED = 'EXTENDED'
DEFAULT_TABLE_SECECT_MODE = TABLE_SELECT_MODE_EXTENDED

TITLE_LOCATION_TOP = 'N'
TITLE_LOCATION_BOTTOM = 'S'
TITLE_LOCATION_LEFT = 'W'
TITLE_LOCATION_RIGHT = 'E'
TITLE_LOCATION_TOP_LEFT = 'NW'
TITLE_LOCATION_TOP_RIGHT = 'NE'
TITLE_LOCATION_BOTTOM_LEFT = 'SW'
TITLE_LOCATION_BOTTOM_RIGHT = 'SE'

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

# Icons for displaying system tray messages
SYSTEM_TRAY_MESSAGE_ICON_INFORMATION = QSystemTrayIcon.Information
SYSTEM_TRAY_MESSAGE_ICON_WARNING = QSystemTrayIcon.Warning
SYSTEM_TRAY_MESSAGE_ICON_CRITICAL = QSystemTrayIcon.Critical
SYSTEM_TRAY_MESSAGE_ICON_NOICON = QSystemTrayIcon.NoIcon

# "Special" Key Values.. reserved
# Key representing a Read timeout
EVENT_TIMEOUT = TIMEOUT_EVENT = TIMEOUT_KEY = '__TIMEOUT__'
# Window closed event (user closed with X or destroyed using OS)
WIN_CLOSED = WINDOW_CLOSED = None

# Key indicating should not create any return values for element
WRITE_ONLY_KEY = '__WRITE ONLY__'
EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED = '__DOUBLE_CLICKED__'
EVENT_SYSTEM_TRAY_ICON_ACTIVATED = '__ACTIVATED__'
EVENT_SYSTEM_TRAY_MESSAGE_CLICKED = '__MESSAGE_CLICKED__'

# Meny key indicator character / string
MENU_KEY_SEPARATOR = '::'
MENU_DISABLED_CHARACTER = '!'

SUPPRESS_ERROR_POPUPS = False


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
# was an Enum previously ButtonType(Enum):
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

BROWSE_FILES_DELIMITER = ';'            # the delimeter to be used between each file in the returned string

# -------------------------  Element types  ------------------------- #
# Used in Element - Was an enum once ElementType(Enum):
ELEM_TYPE_TEXT = 'text'
ELEM_TYPE_INPUT_TEXT = 'input'
ELEM_TYPE_INPUT_COMBO = 'combo'
ELEM_TYPE_INPUT_OPTION_MENU = 'option menu'
ELEM_TYPE_INPUT_RADIO = 'radio'
ELEM_TYPE_INPUT_MULTILINE = 'multiline'
ELEM_TYPE_MULTILINE_OUTPUT = 'multioutput'
ELEM_TYPE_INPUT_CHECKBOX = 'checkbox'
ELEM_TYPE_INPUT_SPIN = 'spind'
ELEM_TYPE_BUTTON = 'button'
ELEM_TYPE_IMAGE = 'image'
ELEM_TYPE_CANVAS = 'canvas'
ELEM_TYPE_FRAME = 'frame'
ELEM_TYPE_GRAPH = 'graph'
ELEM_TYPE_TAB = 'tab'
ELEM_TYPE_TAB_GROUP = 'tabgroup'
ELEM_TYPE_INPUT_SLIDER = 'slider'
ELEM_TYPE_INPUT_DIAL = 'dial'
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
ELEM_TYPE_STRETCH = 'stretch'
ELEM_TYPE_BUTTONMENU = 'buttonmenu'

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
                 key=None, k=None, pad=None, tooltip=None, visible=True, size_px=(None, None), metadata=None):
        """
        :param elem_type: ???
        :type elem_type: ???
        :param size: w=characters-wide, h=rows-high
        :type size: Tuple[int, int]  (width, height)
        :param auto_size_text: True if the Widget should be shrunk to exactly fit the number of chars to show
        :type auto_size_text: bool
        :param font: specifies the font family, size, etc (see docs for exact formats)
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of background. Can be in #RRGGBB format or a color name "black"
        :type background_color: (str)
        :param text_color: element's text color. Can be in #RRGGBB format or a color name "black"
        :type text_color: (str)
        :param key: Identifies an Element. Should be UNIQUE to this window.
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element (Default = True)
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """

        if size_px != (None, None):
            self.Size = size_px
        else:
            self.Size = _convert_tkinter_size_to_Qt(size)

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

        self.ParentForm = None
        self.ParentContainer = None  # will be a Form, Column, or Frame element
        self.TextInputDefault = None
        self.Position = (0, 0)  # Default position Row 0, Col 0
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_ELEMENT_BACKGROUND_COLOR
        self.TextColor = text_color if text_color is not None else DEFAULT_ELEMENT_TEXT_COLOR
        self.Key = key  # dictionary key for return values
        self.Tooltip = tooltip
        self.TooltipObject = None
        self.Visible = visible
        self.metadata = metadata                # type: Any
        self.row_frame = None                   # type: QHBoxLayout


    def _FindReturnKeyBoundButton(self, form):
        for row in form.Rows:
            for element in row:
                if element.Type == ELEM_TYPE_BUTTON:
                    if element.BindReturnKey:
                        return element
                if element.Type == ELEM_TYPE_COLUMN:
                    rc = self._FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
                if element.Type == ELEM_TYPE_FRAME:
                    rc = self._FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
                if element.Type == ELEM_TYPE_TAB_GROUP:
                    rc = self._FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
                if element.Type == ELEM_TYPE_TAB:
                    rc = self._FindReturnKeyBoundButton(element)
                    if rc is not None:
                        return rc
        return None


    def _ReturnKeyHandler(self, event):
        MyForm = self.ParentForm
        button_element = self._FindReturnKeyBoundButton(MyForm)
        if button_element is not None:
            button_element._ButtonCallBack()

    def _widget_was_created(self):
        """
        Determines if a Widget was created for this element.

        :return: True if a Widget has been created previously (Widget is not None)
        :rtype: (bool)
        """
        if self.Widget is not None:
            return True
        else:
            warnings.warn('You cannot Update element with key = {} until the window has been Read or Finalized'.format(self.Key), UserWarning)
            if not SUPPRESS_ERROR_POPUPS:
                popup_error('Unable to complete operation on element with key {}'.format(self.Key),
                    'You cannot perform operations (such as calling update) on an Element until Window is read or finalized.',
                         'Adding a "finalize=True" parameter to your Window creation will likely fix this.', image=_random_error_icon())
            return False


    def Update(self, widget, background_color=None, text_color=None, font=None, visible=None):
        if not self._widget_was_created():
            return
        style = str(widget.styleSheet())
        add_brace = False
        if len(style) != 0 and style[-1] == '}':
            style = style[:-1]
            add_brace = True
        if font is not None:
            style += create_style_from_font(font)
        if text_color is not None:
            style += ' color: %s;' % text_color
            self.TextColor = text_color
        if background_color is not None:
            style += 'background-color: %s;' % background_color
        if add_brace:
            style += '}'
        widget.setStyleSheet(style)
        set_widget_visiblity(widget, visible)


    # ---------------------------------- DUMMY METHODS - They don't do anything! ----------------------------------

    # These methods are here for porting purposes only.  They are meant to allow you to change your import statement
    # from PySimpleGUI to PySimpleGUIQt and still be able to run your program.

    def expand(self, expand_x=False, expand_y=False, expand_row=True):
        """
        WARNING - NOT USED IN PySimpleGUIQt port. Provided as dummy method

        :param expand_x: If True Element will expand in the Horizontal directions
        :type expand_x: (bool)
        :param expand_y: If True Element will expand in the Vertical directions
        :type expand_y: (bool)
        :param expand_row: If True the row containing the element will also expand. Without this your element is "trapped" within the row
        :type expand_row: (bool)
        :return: None
        :rtype: None
        """

        return


    def __call__(self, *args, **kwargs):
        """
        Makes it possible to "call" an already existing element.  When you do make the "call", it actually calls
        the Update method for the element.
        Example:    If this text element was in yoiur layout:
                    sg.Text('foo', key='T')
                    Then you can call the Update method for that element by writing:
                    window.FindElement('T')('new text value')


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
                 justification=None, background_color=None, text_color=None, font=None, tooltip=None, disabled_readonly_background_color=None, disabled_readonly_text_color=None,
                 change_submits=False, enable_events=False, readonly=False, border_width=None,
                 do_not_clear=True, key=None, k=None, focus=False, pad=None, visible=True, size_px=(None,None), metadata=None):
        """
        Input a line of text Element
        :param default_text: Text initially shown in the input box as a default value(Default value = '')
        :type default_text: (str)
        :param size: w=characters-wide, h=rows-high
        :type size: Tuple[int, int]  (width, height)
        :param disabled: set disable state for element (Default = False)
        :type disabled: (bool)
        :param password_char: Password character if this is a password field (Default value = '')
        :type password_char: (char)
        :param justification: justification for data display. Valid choices - left, right, center
        :type justification: (str)
        :param background_color: color of background in one of the color formats
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param disabled_readonly_background_color: If state is set to readonly or disabled, the color to use for the background
        :type disabled_readonly_background_color: (str)
        :param disabled_readonly_text_color: If state is set to readonly or disabled, the color to use for the text
        :type disabled_readonly_text_color: (str)
        :param change_submits: * DEPRICATED DO NOT USE. Use `enable_events` instead
        :type change_submits: (bool)
        :param enable_events: If True then changes to this element are immediately reported as an event. Use this instead of change_submits (Default = False)
        :type enable_events: (bool)
        :param do_not_clear: If False then the field will be set to blank after ANY event (button, any event) (Default = True)
        :type do_not_clear: (bool)
        :param readonly: If True then the user cannot modify the field (Default = False)
        :type readonly: (bool)
        :param border_width: width of border around element in pixels
        :type border_width: (int)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param focus: Determines if initial focus should go to this element.
        :type focus: (bool)
        :param pad: Amount of padding to put around element. Normally (horizontal pixels, vertical pixels) but can be split apart further into ((horizontal left, horizontal right), (vertical above, vertical below))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param visible: set visibility state of the element (Default = True)
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.DefaultText = default_text
        self.PasswordCharacter = password_char
        bg = background_color if background_color is not None else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Focus = focus
        self.do_not_clear = do_not_clear
        self.Justification = justification or 'left'
        self.Disabled = disabled
        self.ReadOnly = readonly
        self.disabled_readonly_background_color = disabled_readonly_background_color
        self.disabled_readonly_text_color = disabled_readonly_text_color
        self.ChangeSubmits = change_submits or enable_events
        self.BorderWidth = border_width if border_width is not None else DEFAULT_BORDER_WIDTH
        self.Widget = self.QT_QLineEdit = None          # type: QLineEdit
        self.ValueWasChanged = False
        super().__init__(ELEM_TYPE_INPUT_TEXT, size=size, background_color=bg, text_color=fg, key=key, pad=pad,
                         font=font, tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)


    def _dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def _dropEvent(self, e):
        self.QT_QLineEdit.setText(e.mimeData().text())



    class InputTextWidget(QWidget):
        def __init__(self, qt_qlineedit, element):
            self.QT_QLineEdit = qt_qlineedit
            self.Element = element
            super().__init__()

        def eventFilter(self, widget, event):
            # print(f'Got input text event {event}')
            if event.type() == QEvent.FocusIn and widget is self.QT_QLineEdit:
                self.Element.ParentForm.FocusElement = self.Element
            return QWidget.eventFilter(self, widget, event)



    def _QtCallbackFocusInEvent(self,value):
        return


    def _QtCallbackFocusInEvent(self, value):
        if not self.ChangeSubmits:
            return
        # if was changed using an "update" call, then skip the next changed callback
        if self.ValueWasChanged:
            self.ValueWasChanged = False
            print('skipping update')
            return
        _element_callback_quit_mainloop(self)

    def _QtCallbackReturnPressed(self):
        self._ReturnKeyHandler(None)
        return

    def Update(self, value=None, disabled=None, select=None, background_color=None, text_color=None, font=None, visible=None):
        if disabled is True:
            self.QT_QLineEdit.setDisabled(True)
        elif disabled is False:
            self.QT_QLineEdit.setDisabled(False)
        if value is not None:
            self.QT_QLineEdit.setText(str(value))
            self.DefaultText = value
            # was getting into an infinite loop when the update was triggering a text changed callback, but unable
            # to dupliate this
            # self.ValueWasChanged = True
        if select:
            self.QT_QLineEdit.setSelection(0,QtGui.QTextCursor.End )
        super().Update(self.QT_QLineEdit, background_color=background_color, text_color=text_color, font=font, visible=visible)



    def Get(self):
        return self.QT_QLineEdit.text()
        # return self.TKStringVar.get()

    def SetFocus(self):
        self.QT_QLineEdit.setFocus()

    get = Get
    set_focus = SetFocus
    update = Update

# -------------------------  INPUT TEXT lazy functions  ------------------------- #
In = InputText
Input = InputText
I = InputText


# ---------------------------------------------------------------------- #
#                           Combo                                        #
# ---------------------------------------------------------------------- #
class Combo(Element):
    def __init__(self, values, default_value=None, size=(None, None), auto_size_text=None, background_color=None,
                 text_color=None, change_submits=False, enable_events=False, disabled=False, key=None, k=None, pad=None, tooltip=None,
                 readonly=False, visible_items=10, font=None, auto_complete=True, visible=True, size_px=(None,None), metadata=None):
        """
        Input Combo Box Element (also called Dropdown box)

        :param values: values to choose. While displayed as text, the items returned are what the caller supplied, not text
        :type values: List[Any] or Tuple[Any]
        :param default_value: Choice to be displayed as initial value. Must match one of values variable contents
        :type default_value: (Any)
        :param size: width = characters-wide, height = rows-high
        :type size: Tuple[int, int] (width, height)
        :param auto_size_text: True if element should be the same size as the contents
        :type auto_size_text: (bool)
        :param background_color: Color for Element. Text or RGB Hex
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param change_submits: DEPRICATED DO NOT USE. Use `enable_events` instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Combo event is when a choice is made
        :type enable_events: (bool)
        :param disabled: set disable state for element
        :type disabled: (bool)
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text that will appear when mouse hovers over this element
        :type tooltip: (str)
        :param readonly: make element readonly (user can't change). True means user cannot change
        :type readonly: (bool)
        :param visible_items: ???
        :type visible_items: ???
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param auto_complete: ???
        :type auto_complete: ???
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.Values = values
        self.DefaultValue = default_value
        self.ChangeSubmits = change_submits or enable_events
        self.TKCombo = None
        # self.InitializeAsDisabled = disabled
        self.Disabled = disabled
        self.Readonly = readonly
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.VisibleItems = visible_items
        self.AutoComplete = auto_complete
        self.Widget = self.QT_ComboBox = None               # type: QComboBox
        super().__init__(ELEM_TYPE_INPUT_COMBO, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, size_px=size_px, metadata=metadata)


    def _QtCurrentItemChanged(self, state):
        if self.ChangeSubmits:
            _element_callback_quit_mainloop(self)


    def Update(self, value=None, values=None, set_to_index=None, disabled=None, readonly=None,  background_color=None, text_color=None, font=None, visible=None):
        if values is not None:
            self.Values = values
            for i in range(self.QT_ComboBox.count()):
                self.QT_ComboBox.removeItem(0)
            self.QT_ComboBox.addItems(values)
        if value is not None:
            for index, v in enumerate(self.Values):
                if v == value:
                    self.QT_ComboBox.setCurrentIndex(index)
                    break
        if set_to_index is not None:
            self.QT_ComboBox.setCurrentIndex(set_to_index)
        if disabled == True:
            self.QT_ComboBox.setDisabled(True)
        elif disabled == False:
            self.QT_ComboBox.setDisabled(False)
        if readonly is not None:
            self.Readonly = readonly

        super().Update(self.QT_ComboBox, background_color=background_color, text_color=text_color, font=font, visible=visible)

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
                 background_color=None, text_color=None, key=None, k=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
        """
        InputOptionMenu - NOT USED IN QT
        :param values: Values to be displayed
        :type values: List[Any] or Tuple[Any]
        :param default_value: the value to choose by default
        :type default_value: (Any)
        :param size: size in characters (wide) and rows (high)
        :type size: Tuple[int, int] (width, height)
        :param disabled: control enabled / disabled
        :type disabled: (bool)
        :param auto_size_text: True if size of Element should match the contents of the items
        :type auto_size_text: (bool)
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text that will appear when mouse hovers over this element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.Values = values
        self.DefaultValue = default_value
        self.TKOptionMenu = None
        self.Disabled = disabled
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_OPTION_MENU, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)

    def Update(self, value=None, values=None, disabled=None):
        return

    update = Update

# -------------------------  OPTION MENU Element lazy functions  ------------------------- #
InputOptionMenu = OptionMenu


# ---------------------------------------------------------------------- #
#                           Listbox                                      #
# ---------------------------------------------------------------------- #
class Listbox(Element):
    def __init__(self, values, default_values=None, select_mode=None, change_submits=False, enable_events=False, bind_return_key=False, size=(None, None), disabled=False, auto_size_text=None, font=None, background_color=None,
                 text_color=None, key=None, k=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
        """
        :param values: list of values to display. Can be any type including mixed types as long as they have __str__ method
        :type values: List[Any] or Tuple[Any]
        :param default_values: which values should be initially selected
        :type default_values: List[Any]
        :param select_mode: Select modes are used to determine if only 1 item can be selected or multiple and how they can be selected.   Valid choices begin with "LISTBOX_SELECT_MODE_" and include: LISTBOX_SELECT_MODE_SINGLE LISTBOX_SELECT_MODE_MULTIPLE LISTBOX_SELECT_MODE_BROWSE LISTBOX_SELECT_MODE_EXTENDED
        :type select_mode: [enum]
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Listbox generates events when an item is clicked
        :type enable_events: (bool)
        :param bind_return_key: If True, then the return key will cause a the Listbox to generate an event
        :type bind_return_key: (bool)
        :param size: width = characters-wide, height = rows-high
        :type size: Tuple(int, int) (width, height)
        :param disabled: set disable state for element
        :type disabled: (bool)
        :param auto_size_text: True if element should be the same size as the contents
        :type auto_size_text: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
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
        self.Widget = self.QT_ListWidget = None                 # type: QListWidget
        tsize = size                # convert tkinter size to pixels
        if size[0] is not None and size[0] < 100:
            tsize = size[0]*DEFAULT_PIXELS_TO_CHARS_SCALING[0], size[1]*DEFAULT_PIXELS_TO_CHARS_SCALING[1]

        super().__init__(ELEM_TYPE_INPUT_LISTBOX, size=tsize, auto_size_text=auto_size_text, font=font,
                         background_color=bg, text_color=fg, key=key, pad=pad, tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)

    def _QtCurrentRowChanged(self, state):
        if self.ChangeSubmits:
            _element_callback_quit_mainloop(self)


    def Update(self, values=None, disabled=None, set_to_index=None,background_color=None, text_color=None, font=None, visible=None):
        if values is not None:
            self.Values = values
            for i in range(self.QT_ListWidget.count()):
                self.QT_ListWidget.takeItem(0)
            items = [str(v) for v in self.Values]
            self.QT_ListWidget.addItems(items)
        if disabled == True:
            self.QT_ListWidget.setDisabled(True)
        elif disabled == False:
            self.QT_ListWidget.setDisabled(False)
        if set_to_index is not None:
            self.QT_ListWidget.setCurrentRow(set_to_index)
        super().Update(self.QT_ListWidget, background_color=background_color, text_color=text_color, font=font, visible=visible)

        return

    def SetValue(self, values):
        # for index, item in enumerate(self.Values):
        for index, value in enumerate(self.Values):
            item = self.QT_ListWidget.item(index)
            if value in values:
                self.QT_ListWidget.setItemSelected(item, True)


    def GetListValues(self):
        return self.Values


    def get(self):
        """
        Gets the current value of the Element as it would be represented in the results dictionary.
        Normally you would NOT be using this method, but instead using the return values dictionary
        that is returned from reading your window

        :return: (List[Any]) The currently selected items in the listbox
        """
        value = []
        selected_items = [item.text() for item in self.QT_ListWidget.selectedItems()]
        for v in self.Values:
            if str(v) in selected_items:
                value.append(v)
        return value

    get_list_values = GetListValues
    set_value = SetValue
    update = Update


# ---------------------------------------------------------------------- #
#                           Radio                                        #
# ---------------------------------------------------------------------- #
class Radio(Element):
    def __init__(self, text, group_id, default=False, disabled=False, size=(None, None), auto_size_text=None,
                 background_color=None, text_color=None, font=None, key=None, k=None, pad=None, tooltip=None,
                 change_submits=False,  enable_events=False, visible=True, size_px=(None,None), metadata=None):
        """
        :param text: Text to display next to button
        :type text: (str)
        :param group_id: Groups together multiple Radio Buttons. Any type works
        :type group_id: (Any)
        :param default: Set to True for the one element of the group you want initially selected
        :type default: (bool)
        :param disabled: set disable state
        :type disabled: (bool)
        :param size: (width, height) width = characters-wide, height = rows-high
        :type size: Tuple[int, int]
        :param auto_size_text: if True will size the element to match the length of the text
        :type auto_size_text: (bool)
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Radio Button events happen when an item is selected
        :type enable_events: (bool)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.InitialState = default
        self.Text = text
        self.GroupID = group_id
        self.Value = None
        self.Disabled = disabled
        self.TextColor = text_color or DEFAULT_TEXT_COLOR
        self.ChangeSubmits = change_submits or enable_events
        self.Widget = self.QT_Radio_Button = None           # type: QRadioButton
        self.QT_RadioButtonGroup = None                     # type: QButtonGroup

        super().__init__(ELEM_TYPE_INPUT_RADIO, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)

    def Update(self, value=None, disabled=None, background_color=None, text_color=None, font=None, visible=None):
        if value is not None:
            self.InitialState = value
        if disabled:
            self.QT_Radio_Button.setDisabled(True)
        else:
            self.QT_Radio_Button.setDisabled(False)
        if value is True:
            self.QT_Radio_Button.setChecked(True)
        if value is False:
            self.QT_RadioButtonGroup.setExclusive(False)
            self.QT_Radio_Button.setChecked(False)
            self.QT_RadioButtonGroup.setExclusive(True)
        super().Update(self.QT_Radio_Button, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def reset_group(self):
        self.QT_Radio_Button.setChecked(True)
        self.QT_RadioButtonGroup.setExclusive(False)
        self.QT_Radio_Button.setChecked(False)
        self.QT_RadioButtonGroup.setExclusive(True)


    def _QtCallbackValueChanged(self, value):
        if not self.ChangeSubmits:
            return
        _element_callback_quit_mainloop(self)

    update = Update

# ---------------------------------------------------------------------- #
#                           Checkbox                                     #
# ---------------------------------------------------------------------- #
class Checkbox(Element):
    def __init__(self, text, default=False, size=(None, None), auto_size_text=None, font=None, background_color=None,
                 text_color=None, change_submits=False, enable_events=False, disabled=False, key=None, k=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
        """
        :param text: Text to display next to checkbox
        :type text: (str)
        :param default: Set to True if you want this checkbox initially checked
        :type default: (bool)
        :param size: (width, height) width = characters-wide, height = rows-high
        :type size: Tuple[int, int]
        :param auto_size_text: if True will size the element to match the length of the text
        :type auto_size_text: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Checkbox events happen when an item changes
        :type enable_events: (bool)
        :param disabled: set disable state
        :type disabled: (bool)
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.Text = text
        self.InitialState = default
        self.Value = None
        self.TKCheckbutton = None
        self.Disabled = disabled
        self.TextColor = text_color if text_color else DEFAULT_TEXT_COLOR
        self.ChangeSubmits = change_submits or enable_events
        self.Widget = self.QT_Checkbox = None           # type: QCheckBox

        super().__init__(ELEM_TYPE_INPUT_CHECKBOX, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)

    def QtCallbackStateChanged(self, state):
        if self.ChangeSubmits:
            _element_callback_quit_mainloop(self)


    def Get(self):
        return self.QT_Checkbox.isChecked()

    def Update(self, value=None, disabled=None, background_color=None, text_color=None, font=None, visible=None):
        self.QT_Checkbox.setChecked(value or False)
        if disabled == True:
            self.QT_Checkbox.setDisabled(True)
        elif disabled == False:
            self.QT_Checkbox.setDisabled(False)
        super().Update(self.QT_Checkbox, background_color=background_color, text_color=text_color, font=font, visible=visible)

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
    def __init__(self, values, initial_value=None, disabled=False, change_submits=False,  enable_events=False, size=(None, None),
                 auto_size_text=None, font=None, background_color=None, text_color=None, key=None, k=None, pad=None,
                 tooltip=None, visible=True, size_px=(None,None), metadata=None):
        """
        Spinner Element
        :param values: List of valid values
        :type values: Tuple[Any] or List[Any]
        :param initial_value: Initial item to show in window. Choose from list of values supplied
        :type initial_value: (Any)
        :param disabled: set disable state
        :type disabled: (bool)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Spin events happen when an item changes
        :type enable_events: (bool)
        :param size: (width, height) width = characters-wide, height = rows-high
        :type size: Tuple[int, int]
        :param auto_size_text: if True will size the element to match the length of the text
        :type auto_size_text: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.Values = values
        self.DefaultValue = initial_value
        self.ChangeSubmits = change_submits or enable_events
        self.Disabled = disabled
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Widget = self.QT_Spinner = None            # type: StringBox

        super().__init__(ELEM_TYPE_INPUT_SPIN, size, auto_size_text, font=font, background_color=bg, text_color=fg,
                         key=key, pad=pad, tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)
        return

    class StringBox(QSpinBox):
        def __init__(self, strings, parent=None):
            super(Spin.StringBox, self).__init__(parent)
            self.setStrings(strings)

        def strings(self):
            return self._strings

        def setStrings(self, strings):
            self._strings = tuple(strings)
            self._values = dict(zip(strings, range(len(strings))))
            self.setRange(0, len(strings) - 1)

        def textFromValue(self, value):
            return str(self._strings[value])

        def valueFromText(self, text):
            return self._values[text]


    def _QtCallbackValueChanged(self, value):
        if not self.ChangeSubmits:
            return
        _element_callback_quit_mainloop(self)

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
        return self.QT_Spinner.value()

    get = Get
    update = Update


# ---------------------------------------------------------------------- #
#                           Multiline                                    #
# ---------------------------------------------------------------------- #
class Multiline(Element):
    def __init__(self, default_text='', enter_submits=False, disabled=False, autoscroll=False, size=(None, None),
                 auto_size_text=None, background_color=None, text_color=None, change_submits=False, enable_events=False, do_not_clear=True,
                 key=None, k=None, write_only=False, focus=False, font=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):

        """
        :param default_text: Initial text to show
        :type default_text: (str)
        :param enter_submits: if True, the Window.Read call will return is enter key is pressed in this element
        :type enter_submits: (bool)
        :param disabled: set disable state
        :type disabled: (bool)
        :param autoscroll: If True the contents of the element will automatically scroll as more data added to the end
        :type autoscroll: (bool)
        :param size: (width, height) width = characters-wide, height = rows-high
        :type size: Tuple[int, int]
        :param auto_size_text: if True will size the element to match the length of the text
        :type auto_size_text: (bool)
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Spin events happen when an item changes
        :type enable_events: (bool)
        :param do_not_clear: if False the element will be cleared any time the Window.Read call returns
        :type do_not_clear: bool
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param write_only: If True then no entry will be added to the values dictionary when the window is read
        :type write_only: bool
        :param focus: if True initial focus will go to this element
        :type focus: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.DefaultText = default_text
        self.EnterSubmits = enter_submits
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        self.Focus = focus
        self.do_not_clear = do_not_clear
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Autoscroll = autoscroll
        self.Disabled = disabled
        self.ChangeSubmits = change_submits or enable_events
        self.WriteOnly = write_only
        tsize = _convert_tkinter_size_to_Qt(size, scaling=DEFAULT_PIXELS_TO_CHARS_SCALING_MULTILINE_TEXT,height_cutoff=DEFAULT_PIXEL_TO_CHARS_CUTOFF_MULTILINE) if size[0] is not None else size_px

        self.Widget = self.QT_TextEdit = None               # type: QTextEdit

        super().__init__(ELEM_TYPE_INPUT_MULTILINE, size=(None, None), auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, size_px=tsize, metadata=metadata)
        return


    class MultiQWidget(QWidget):
        def __init__(self, qt_textedit, element):
            self.QT_TextEdit = qt_textedit
            self.Element = element
            super().__init__()

        def eventFilter(self, widget, event):
            if self.Element.EnterSubmits and event.type() == QEvent.KeyPress and widget is self.QT_TextEdit:
                key = event.key()
                if key in (Qt.Key_Return, Qt.Key_Enter):
                    self.Element._ReturnKeyHandler(0)
            if event.type() == QEvent.FocusIn and widget is self.QT_TextEdit:
                self.Element.ParentForm.FocusElement = self.Element
            return QWidget.eventFilter(self, widget, event)


    def _QtCallbackFocusInEvent(self):
        if not self.ChangeSubmits:
            return
        _element_callback_quit_mainloop(self)



    def _dragEnterEvent(self, e):
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()

    def _dropEvent(self, e):
        self.Widget.setText(e.mimeData().text())


    def Update(self, value=None, disabled=None, append=False, autoscroll=False, background_color=None, text_color=None, font=None, text_color_for_value=None, background_color_for_value=None, visible=None, readonly=None):
        """
        Changes some of the settings for the Multiline Element. Must call `Window.read` or `Window.finalize` or "finalize" the window using finalize parameter prior

        :param value: (str) new text to display
        :param disabled: (bool) disable or enable state of the element
        :param append: (bool) if True then new value will be added onto the end of the current value. if False then contents will be replaced.
        :param autoscroll: (bool)  if True cursor will be moved to end of element after updating
        :param background_color: (str) color of background
        :param text_color: (str) color of the text
        :param font: Union[str, Tuple[str, int]] specifies the font family, size, etc
        :param text_color_for_value: (str) color of the new text being added
        :param visible: (bool) set visibility state of the element
        :param autoscroll: (bool) if True then contents of element are scrolled down when new text is added to the end
        """

        if value is not None and not append:
            self.DefaultText = value
            self.QT_TextEdit.setText(str(value))
        elif value is not None and append:
            self.DefaultText = value
            # self.QT_TextEdit.setText(self.QT_TextEdit.toPlainText() + str(value)) # original code
            # self.QT_TextEdit.append(str(value))   # can't use because adds a newline
            if text_color_for_value is not None:
                self.QT_TextEdit.setTextColor(text_color_for_value)
            if background_color_for_value is not None:
                self.QT_TextEdit.setTextBackgroundColor(background_color_for_value)
            self.QT_TextEdit.insertPlainText(str(value))
            if self.Autoscroll or autoscroll and autoscroll is not False:
                self.QT_TextEdit.moveCursor(QtGui.QTextCursor.End)
            if text_color_for_value is not None:
                self.QT_TextEdit.setTextColor(self.TextColor)
            if background_color_for_value is not None:
                self.QT_TextEdit.setTextBackgroundColor(self.BackgroundColor)
        if disabled is True:
            self.QT_TextEdit.setDisabled(True)
        elif disabled is False:
            self.QT_TextEdit.setDisabled(False)
        if readonly is True:
            self.QT_TextEdit.setReadOnly(True)
        elif readonly is False:
            self.QT_TextEdit.setReadOnly(False)
        super().Update(self.QT_TextEdit, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def Get(self):
        return self.QT_TextEdit.toPlainText()

    def SetFocus(self):
        self.QT_TextEdit.setFocus()


    def print(self, *args, end=None, sep=None, text_color=None, background_color=None, autoscroll=True):
        """
        Print like Python normally prints except route the output to a multline element and also add colors if desired

        :param args: The arguments to print
        :type args: List[Any]
        :param end: (str) The end char to use just like print uses
        :type end: (str)
        :param sep: (str) The separation character like print uses
        :type sep: (str)
        :param text_color: The color of the text
        :type text_color: (str)
        :param background_color: The background color of the line
        :type background_color: (str)
        :param autoscroll: (bool) If True cursor is moved to end after print
        :type autoscroll: (bool)
        """
        _print_to_element(self, *args, end=end, sep=sep, text_color=text_color, background_color=background_color, autoscroll=autoscroll)




    get = Get
    set_focus = SetFocus
    update = Update

ML = Multiline
MLine = Multiline


# ---------------------------------------------------------------------- #
#                           ScrolledOutput                               #
# ---------------------------------------------------------------------- #
class MultilineOutput(Element):
    def __init__(self, default_text='', enter_submits=False, disabled=False, autoscroll=False, size=(None, None), auto_size_text=None, background_color=None, text_color=None, change_submits=False, enable_events=False, do_not_clear=True, key=None, k=None, focus=False, font=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
        """
        :param default_text: default value to put into input area
        :type default_text: (str)
        :param enter_submits: if True, the Window.Read call will return is enter key is pressed in this element
        :type enter_submits: (bool)
        :param disabled: set disable state
        :type disabled: (bool)
        :param autoscroll: If True cursor is moved to end after print
        :typep autoscroll: (bool)
        :param size: (width, height) width = characters-wide, height = rows-high
        :type size: Tuple[int, int]
        :param auto_size_text: if True size of the Text Element will be sized to fit the string provided in 'text' parm
        :type auto_size_text: (bool)
        :param background_color: color of background in one of the color formats
        :type background_color: (str)
        ::param text_color: color of the text
        :type text_color: (str)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. If this button is a target, should it generate an event when filled in
        :type enable_events: (bool)
        :param do_not_clear: if False the element will be cleared any time the Window.Read call returns
        :type do_not_clear: (bool)
        :param focus: if True, initial focus will be put on this button
        :type focus: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.DefaultText = default_text
        self.EnterSubmits = enter_submits
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        self.Focus = focus
        self.do_not_clear = do_not_clear
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Autoscroll = autoscroll
        self.Disabled = disabled
        self.ChangeSubmits = change_submits or enable_events
        self.Widget = self.QT_TextBrowser = None            # type: QTextBrowser
        tsize = _convert_tkinter_size_to_Qt(size, scaling=DEFAULT_PIXELS_TO_CHARS_SCALING_MULTILINE_TEXT,height_cutoff=DEFAULT_PIXEL_TO_CHARS_CUTOFF_MULTILINE) if size[0] is not None else size_px
        super().__init__(ELEM_TYPE_MULTILINE_OUTPUT, size=(None, None), auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, size_px=tsize, metadata=metadata)
        return


    def Update(self, value=None, disabled=None, append=False, autoscroll=None, background_color=None, text_color=None, font=None, text_color_for_value=None, background_color_for_value=None, visible=None):
        if value is not None and not append:
            self.QT_TextBrowser.setText(str(value))
        elif value is not None and append:
            self.QT_TextBrowser.insertPlainText(str(value))
            # self.QT_TextBrowser.moveCursor(QtGui.QTextCursor.End)
        if disabled == True:
            self.QT_TextBrowser.setDisabled(True)
        elif disabled == False:
            self.QT_TextBrowser.setDisabled(False)
        if self.Autoscroll or autoscroll and autoscroll is not False:
            self.QT_TextBrowser.moveCursor(QtGui.QTextCursor.End)
        super().Update(self.QT_TextBrowser, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def Get(self):
        return self.QT_TextBrowser.toPlainText()


    def print(self, *args, end=None, sep=None, text_color=None, background_color=None, autoscroll=True):
        """
        Print like Python normally prints except route the output to a multline element and also add colors if desired

        :param args: The arguments to print
        :type args: List[Any]
        :param end: The end char to use just like print uses
        :type end: (str)
        :param sep: The separation character like print uses
        :type sep: (str)
        :param text_color: The color of the text
        :type text_color: (str)
        :param background_color: The background color of the line
        :type background_color: (str)
        :param autoscroll: If True cursor is moved to end after print
        :typep autoscroll: (bool)
        """
        _print_to_element(self, *args, end=end, sep=sep, text_color=text_color, background_color=background_color, autoscroll=autoscroll)



    get = Get
    update = Update

MLineOut = Multiline

# ---------------------------------------------------------------------- #
#                                       Text                             #
# ---------------------------------------------------------------------- #
class Text(Element):
    def __init__(self, text='', size=(None, None),  auto_size_text=None, click_submits=None, enable_events=False, relief=None, font=None, text_color=None, background_color=None, justification=None, pad=None, margins=None, key=None, k=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):

        """
        :param text: The text to display. Can include /n to achieve multiple lines.  Will convert (optional) parameter into a string
        :type text: (Any)
        :param size: (width, height) width = characters-wide, height = rows-high
        :type size: Tuple[int, int]
        :param auto_size_text: if True size of the Text Element will be sized to fit the string provided in 'text' parm
        :type auto_size_text: (bool)
        :param click_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type click_submits: (bool)
        :param enable_events: Turns on the element specific events. Text events happen when the text is clicked
        :type enable_events: (bool)
        :param relief: relief style around the text. Values are same as progress meter relief values. Should be a constant that is defined at starting with "RELIEF_" - `RELIEF_RAISED, RELIEF_SUNKEN, RELIEF_FLAT, RELIEF_RIDGE, RELIEF_GROOVE, RELIEF_SOLID`
        :type relief: (str/enum)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param text_color: color of the text
        :type text_color: (str)
        :param background_color: color of background
        :type background_color: (str)
        :param justification: how string should be aligned within space provided by size. Valid choices = `left`, `right`, `center`
        :type justification: (str)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param margins: ???
        :type margins: ???
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.DisplayText = str(text)
        self.TextColor = text_color if text_color else DEFAULT_TEXT_COLOR
        self.Justification = justification or 'left'
        self.Relief = relief
        self.ClickSubmits = click_submits or enable_events
        self.Margins = margins
        if background_color is None:
            bg = DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR
        else:
            bg = background_color
        self.Widget = self.QT_Label = None              # type: QLabel

        super().__init__(ELEM_TYPE_TEXT, size, auto_size_text, background_color=bg, font=font if font else DEFAULT_FONT,
                         text_color=self.TextColor, visible=visible, pad=pad, key=key, tooltip=tooltip, size_px=size_px, metadata=metadata)
        return

    def _QtCallbackTextClicked(self, event):
        if not self.ClickSubmits:
            return
        _element_callback_quit_mainloop(self)

    def Update(self, value=None, background_color=None, text_color=None, font=None, visible=None):
        """

        :param value:
        :param background_color:
        :param text_color:
        :param font:
        :param visible:
        :return:
        """
        if value is not None:
            self.DisplayText = str(value)
            self.QT_Label.setText(str(value))
        super().Update(self.QT_Label, background_color=background_color, text_color=text_color, font=font, visible=visible)

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
                 key=None, k=None, visible=True, size_px=(None,None), metadata=None):
        """
        :param size: (width, height) w=characters-wide, h=rows-high
        :type size: Tuple[int, int]
        :param background_color: color of background
        :type background_color: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self._TKOut = None
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR
        self.Widget = self.QT_TextBrowser = None            # type: QTextBrowser
        tsize = size_px if size_px != (None,None) else _convert_tkinter_size_to_Qt(size, scaling=DEFAULT_PIXELS_TO_CHARS_SCALING_MULTILINE_TEXT,height_cutoff=DEFAULT_PIXEL_TO_CHARS_CUTOFF_MULTILINE) if size[0] is not None else size

        super().__init__(ELEM_TYPE_OUTPUT, size=(None, None), background_color=bg, text_color=fg, pad=pad, font=font,
                         tooltip=tooltip, key=key, visible=visible, size_px=tsize, metadata=metadata)

    def _reroute_stdout(self):
        self.my_stdout = sys.stdout
        self.my_stderr = sys.stderr
        sys.stdout = self
        sys.stderr = self


    def write(self, m):
        """
        MUST be called write. Don't mess with. It's called by Python itself because of reroute
        :param m:
        :return:
        """
        self.QT_TextBrowser.moveCursor(QtGui.QTextCursor.End)
        self.QT_TextBrowser.insertPlainText( str(m))

        # if self.my_stdout:
        #     self.my_stdout.write(str(m))


    def Update(self,value=None, background_color=None, text_color=None, font=None, visible=None):
        if value is not None:
            self.QT_TextBrowser.setText(value)
        super().Update(self.QT_TextBrowser, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def __del__(self):
        sys.stdout = self.my_stdout
        sys.stderr = self.my_stderr

    update = Update
    write = write


# ---------------------------------------------------------------------- #
#                           Button Class                                 #
# ---------------------------------------------------------------------- #
class Button(Element):
    def __init__(self, button_text='', button_type=BUTTON_TYPE_READ_FORM, target=(None, None), tooltip=None,
                 file_types=(("ALL Files", "*"),), initial_folder=None, disabled=False, change_submits=False, enable_events=False,
                 image_filename=None, image_data=None, image_size=(None, None), image_subsample=None, border_width=None,
                 size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False,
                 focus=False, pad=None, key=None, k=None, visible=True, size_px=(None,None), metadata=None):
        """
        :param button_text: Text to be displayed on the button
        :type button_text: (str)
        :param button_type: You  should NOT be setting this directly. ONLY the shortcut functions set this
        :type button_type: (int)
        :param target: key or (row,col) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button
        :type target: Union[str, Tuple[int, int]]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param file_types: the filetypes that will be used to match files. To indicate all files: (("ALL Files", "*.*"),).  Note - NOT SUPPORTED ON MAC
        :type file_types: Tuple[Tuple[str, str], ...]
        :param initial_folder: starting path for folders and files
        :type initial_folder: (str)
        :param disabled: If True button will be created disabled
        :type disabled: (bool)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. If this button is a target, should it generate an event when filled in
        :type enable_events: (bool)
        :param image_filename: image filename if there is a button image. GIFs and PNGs only.
        :type image_filename: (str)
        :param image_data: Raw or Base64 representation of the image to put on button. Choose either filename or data
        :type image_data: Union[bytes, str]
        :param image_size: Size of the image in pixels (width, height)
        :type image_size: Tuple[int, int]
        :param image_subsample: amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
        :type image_subsample: (int)
        :param border_width: width of border around button in pixels
        :type border_width: (int)
        :param size: (width, height) of the button in characters wide, rows high
        :type size: Tuple[int, int]
        :param auto_size_button: if True the button size is sized to fit the text
        :type auto_size_button: (bool)
        :param button_color: of button. Easy to remember which is which if you say "ON" between colors. "red" on "green".
        :type button_color: Tuple[str, str] == (text color, background color)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param bind_return_key: If True the return key will cause this button to be pressed
        :type bind_return_key: (bool)
        :param focus: if True, initial focus will be put on this button
        :type focus: (bool)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.AutoSizeButton = auto_size_button
        self.BType = button_type
        self.FileTypes = file_types
        self.TKButton = None
        self.Target = target
        self.ButtonText = str(button_text)

        # Button colors can be a tuple (text, background) or a string with format "text on background"
        if button_color is None:
            button_color = DEFAULT_BUTTON_COLOR
        else:
            try:
                if isinstance(button_color,str):
                    button_color = button_color.split(' on ')
            except Exception as e:
                print('* cprint warning * you messed up with color formatting', e)

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
        self.Widget = self.QT_QPushButton = None            # type: QPushButton
        self.ColorChosen = None
        # self.temp_size = size if size != (NONE, NONE) else

        super().__init__(ELEM_TYPE_BUTTON, size=size, font=font, pad=pad, key=key, tooltip=tooltip, text_color=self.TextColor, background_color=self.BackgroundColor, visible=visible, size_px=size_px, metadata=metadata)
        return

    # Realtime button release callback
    def _ButtonReleaseCallBack(self, parm):
        self.LastButtonClickedWasRealtime = False
        self.ParentForm.LastButtonClicked = None

    # Realtime button callback
    def _ButtonPressCallBack(self, parm):
        self.ParentForm.LastButtonClickedWasRealtime = True
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = self.ButtonText
        if self.ParentForm.CurrentlyRunningMainloop:
            pass  # kick out of loop if read was called

    # -------  Button Callback  ------- #
    def _ButtonCallBack(self):

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
        if self.BType == BUTTON_TYPE_BROWSE_FOLDER:
            folder_name = QFileDialog.getExistingDirectory(dir=self.InitialFolder)
            if folder_name != '':
                if target_element.Type == ELEM_TYPE_BUTTON:
                    target_element.FileOrFolderName = folder_name
                else:
                    target_element.Update(folder_name)
        elif self.BType == BUTTON_TYPE_BROWSE_FILE:
            qt_types = convert_tkinter_filetypes_to_qt(self.FileTypes)
            file_name = QFileDialog.getOpenFileName(dir=self.InitialFolder, filter=qt_types)
            if file_name != '':
                if target_element.Type == ELEM_TYPE_BUTTON:
                    target_element.FileOrFolderName = file_name
                else:
                    target_element.Update(file_name[0])
        elif self.BType == BUTTON_TYPE_COLOR_CHOOSER:
            qcolor = QColorDialog.getColor()
            rgb_color = qcolor.getRgb()
            color= '#' + ''.join('%02x'% i for i in rgb_color[:3])
            if self.Target == (None, None):
                self.FileOrFolderName = color
            else:
                target_element.Update(color)
        elif self.BType == BUTTON_TYPE_BROWSE_FILES:
            qt_types = convert_tkinter_filetypes_to_qt(self.FileTypes)
            file_name = QFileDialog.getOpenFileNames(dir=self.InitialFolder, filter=qt_types)
            if file_name != '':
                file_name = BROWSE_FILES_DELIMITER.join(file_name[0])
                if target_element.Type == ELEM_TYPE_BUTTON:
                    target_element.FileOrFolderName = file_name
                else:
                    target_element.Update(file_name)
        elif self.BType == BUTTON_TYPE_SAVEAS_FILE:
            qt_types = convert_tkinter_filetypes_to_qt(self.FileTypes)
            file_name = QFileDialog.getSaveFileName(dir=self.InitialFolder, filter=qt_types)
            if file_name != '':
                if target_element.Type == ELEM_TYPE_BUTTON:
                    target_element.FileOrFolderName = file_name
                else:
                    target_element.Update(file_name[0])
        elif self.BType == BUTTON_TYPE_CLOSES_WIN:  # this is a return type button so GET RESULTS and destroy window
            # first, get the results table built
            # modify the Results table in the parent FlexForm object
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = self.ButtonText
            self.ParentForm.FormRemainedOpen = False
            self.ParentForm._Close()
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.QTApplication.exit()            # Exit the mainloop
            self.ParentForm.QT_QMainWindow.close()
            if self.ParentForm.NonBlocking:
                # TODO DESTROY WIN
                Window.DecrementOpenCount()
        elif self.BType == BUTTON_TYPE_READ_FORM:  # LEAVE THE WINDOW OPEN!! DO NOT CLOSE
            # first, get the results table built
            # modify the Results table in the parent FlexForm object
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = self.ButtonText
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:  # if this window is running the mainloop, kick out
                self.ParentForm.QTApplication.exit()
        elif self.BType == BUTTON_TYPE_CLOSES_WIN_ONLY:  # special kind of button that does not exit main loop
            self.ParentForm._Close()
            self.ParentForm.QT_QMainWindow.close()
            if self.ParentForm.CurrentlyRunningMainloop:  # if this window is running the mainloop, kick out
                self.ParentForm.QTApplication.exit()
            Window.DecrementOpenCount()
        elif self.BType == BUTTON_TYPE_CALENDAR_CHOOSER:  # this is a return type button so GET RESULTS and destroy window
            should_submit_window = False

        if should_submit_window:
            self.ParentForm.LastButtonClicked = target_element.Key
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.QTApplication.exit()
                pass # TODO # kick the users out of the mainloop
        return

    def Update(self, text=None, button_color=(None, None), disabled=None, image_data=None, image_filename=None, font=None, visible=None):
        if text is not None:
            self.QT_QPushButton.setText(str(text))
            self.ButtonText = text
        if self.ParentForm.Font and (self.Font == DEFAULT_FONT or not self.Font):
            font = self.ParentForm.Font
        elif self.Font is not None:
            font = self.Font
        else:
            font = DEFAULT_FONT

        fg = bg = None
        if button_color != (None, None):
            self.ButtonColor = button_color
            fg, bg = button_color
        if self.Disabled != disabled and disabled is not None:
            if not disabled:            # if enabling buttons, set the color
                fg, bg = self.ButtonColor
            self.Disabled = disabled
            if disabled:
                self.QT_QPushButton.setDisabled(True)
            else:
                self.QT_QPushButton.setDisabled(False)
        # fg, bg = self.ButtonColor
        # print(f'Button update fg, bg {fg}, {bg}')
        super().Update(self.QT_QPushButton, background_color=bg, text_color=fg, font=font, visible=visible)


    def GetText(self):
        return self.ButtonText

    def SetFocus(self):
        self.QT_QPushButton.setFocus()

    def Click(self):
        if self.Widget is None:
            return
        try:
            self.Widget.click()
        except Exception as e:
            print('Exception {} \nclicking button {}'.format(e, self.ButtonText))

    click = Click
    get_text = GetText
    set_focus = SetFocus
    update = Update

# -------------------------  Button lazy functions  ------------------------- #
B = Button
Btn = Button



# ---------------------------------------------------------------------- #
#                           ButtonMenu Class                             #
# ---------------------------------------------------------------------- #
class ButtonMenu(Element):
    def __init__(self, button_text ,menu_def, tooltip=None,disabled=False,
                 image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,border_width=None,
                 size=(None, None), auto_size_button=None, button_color=None, font=None, pad=None, key=None, k=None, visible=True, size_px=(None,None), metadata=None):
        """
        :param button_text: Text to be displayed on the button
        :type button_text: (str)
        :param menu_def: A list of lists of Menu items to show when this element is clicked. See docs for format as they are the same for all menu types
        :type menu_def: List[List[str]]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param disabled: If True button will be created disabled
        :type disabled: (bool)
        :param image_filename: image filename if there is a button image. GIFs and PNGs only.
        :type image_filename: (str)
        :param image_data: Raw or Base64 representation of the image to put on button. Choose either filename or data
        :type image_data: Union[bytes, str]
        :param image_size: Size of the image in pixels (width, height)
        :type image_size: Tuple[int, int]
        :param image_subsample: amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
        :type image_subsample: (int)
        :param border_width: width of border around button in pixels
        :type border_width: (int)
        :param size: (width, height) of the button in characters wide, rows high
        :type size: Tuple[int, int]
        :param auto_size_button: if True the button size is sized to fit the text
        :type auto_size_button: (bool)
        :param button_color: of button. Easy to remember which is which if you say "ON" between colors. "red" on "green"
        :type button_color: Tuple[str, str] == (text color, background color)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.MenuDefinition = menu_def
        self.AutoSizeButton = auto_size_button
        self.ButtonText = button_text
        self.ButtonColor = button_color if button_color else DEFAULT_BUTTON_COLOR
        self.TextColor = self.ButtonColor[0]
        self.BackgroundColor = self.ButtonColor[1]
        self.BorderWidth = border_width
        self.ImageFilename = image_filename
        self.ImageData = image_data
        self.ImageSize = image_size
        self.ImageSubsample = image_subsample
        self.Disabled = disabled
        self.Widget = self.QT_QPushButton = None        # type: QPushButton
        self.IsButtonMenu = True
        self.MenuItemChosen = None

        # self.temp_size = size if size != (NONE, NONE) else

        super().__init__(ELEM_TYPE_BUTTONMENU, size=size, font=font, pad=pad, key=key, tooltip=tooltip, text_color=self.TextColor, background_color=self.BackgroundColor, visible=visible, size_px=size_px, metadata=metadata)
        return


    def _QT_MenuItemChosenCallback(self, item_chosen):
        # print('IN BUTTON MENU ITEM CALLBACK', item_chosen)
        self.Key = item_chosen.replace('&','')                   # fool the quit function into thinking this was a key
        _element_callback_quit_mainloop(self)


    def Update(self, menu_definition=None, text=None, button_color=(None, None), font=None, visible=None):
        if menu_definition is not None:
            menu_def = menu_definition
            qmenu = QMenu(self.QT_QPushButton)
            qmenu.setTitle(menu_def[0])
            AddMenuItem(qmenu, menu_def[1], self)
            self.QT_QPushButton.setMenu(qmenu)
        super().Update(self.QT_QPushButton, background_color=button_color[1], text_color=button_color[0], font=font, visible=visible)


    def Click(self):
        """ """
        try:
            self.QT_QPushButton.click()
        except Exception as e:
            print('Exception {} clicking button. Has your Window been Finalized() or Read()?'.format(e))

    click = Click
    update = Update

BMenu = ButtonMenu

# ---------------------------------------------------------------------- #
#                           ProgreessBar                                 #
# ---------------------------------------------------------------------- #
class ProgressBar(Element):
    def __init__(self, max_value, orientation=None, size=(None, None),start_value=0,  auto_size_text=None, bar_color=(None, None),
                 style=None, border_width=None, relief=None, key=None, k=None, pad=None, visible=True, size_px=(None,None), metadata=None):

        """
        :param max_value: max value of progressbar
        :type max_value: (int)
        :param orientation: 'horizontal' or 'vertical'
        :type orientation: (str)
        :param size: Size of the bar.  If horizontal (chars wide, pixels high), vert (pixels wide, rows high)
        :type size: Tuple[int, int]
        :param start_value: ???
        :type start_value: ???
        :param auto_size_text: Not sure why this is here
        :type auto_size_text: (bool)
        :param bar_color: The 2 colors that make up a progress bar. One is the background, the other is the bar
        :type bar_color: Tuple[str, str]
        :param style: Progress bar style defined as one of these 'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative'
        :type style: (str)
        :param border_width: The amount of pixels that go around the outside of the bar
        :type border_width: (int)
        :param relief: relief style. Values are same as progress meter relief values.  Can be a constant or a string: `RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID` (Default value = DEFAULT_PROGRESS_BAR_RELIEF)
        :type relief: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
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
        tsize = size
        if size[0] is not None and size[0] < 100:
            # tsize = size[0] * DEFAULT_PIXELS_TO_CHARS_SCALING[0], size[1] * DEFAULT_PIXELS_TO_CHARS_SCALING[1]
            tsize = size[0]*10, size[1]
        self.Widget = self.QT_QProgressBar = None               # type: QProgressBar

        super().__init__(ELEM_TYPE_PROGRESS_BAR, size=tsize, auto_size_text=auto_size_text, key=key, pad=pad, visible=visible, size_px=size_px, metadata=metadata)

    # returns False if update failed
    def UpdateBar(self, current_count, max=None):
        if max is not None:
            self.QT_QProgressBar.setMaximum(max)
        self.QT_QProgressBar.setValue(current_count)
        self.ParentForm.QTApplication.processEvents()  # refresh the window
        return True


    def Update(self, visible=None):
        super().Update(self.QT_QProgressBar, visible=visible)

    update = Update
    update_bar = UpdateBar

PBar = ProgressBar
Prog = ProgressBar

# ---------------------------------------------------------------------- #
#                           Image                                        #
# ---------------------------------------------------------------------- #
class Image(Element):
    def __init__(self, filename=None, data=None, data_base64=None, background_color=None, size=(None, None), pad=None, key=None, k=None, tooltip=None, click_submits=False,  enable_events=False, visible=True, size_px=(None,None), metadata=None):
        """
        :param filename: image filename if there is a button image. GIFs and PNGs only.
        :type filename: (str)
        :param data: Raw or Base64 representation of the image to put on button. Choose either filename or data
        :type data: Union[bytes, str]
        :param data_base64: ???
        :type data_base64: ???
        :param background_color: color of background
        :type background_color:
        :param size: (width, height) size of image in pixels
        :type size: Tuple[int, int]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param click_submits: ???
        :type click_submits: (bool)
        :param enable_events: Turns on the element specific events. For an Image element, the event is "image clicked"
        :type enable_events: (bool)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.Filename = filename
        self.Data = data
        self.DataBase64 = data_base64
        self.tktext_label = None
        self.BackgroundColor = background_color
        self.ClickSubmits = click_submits or enable_events
        if data is None and filename is None and data_base64 is None:
            print('* Warning... no image specified in Image Element! *')
        self.Widget = self.QT_QLabel = None             # type: QLabel

        super().__init__(ELEM_TYPE_IMAGE, size=size, background_color=background_color, pad=pad, key=key,
                         tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)
        return


    def QtCallbackImageClicked(self, event):
        if not self.ClickSubmits:
            return
        _element_callback_quit_mainloop(self)


    def Update(self, filename=None, data=None, data_base64=None, size=(None, None), visible=None):
        if filename is not None:
            qlabel = self.QT_QLabel
            qlabel.setText('')
            w = QtGui.QPixmap(filename).width()
            h = QtGui.QPixmap(filename).height()
            qlabel.setGeometry(QtCore.QRect(0, 0, w, h))
            qlabel.setPixmap(QtGui.QPixmap(filename))
        elif data is not None:
            qlabel = self.QT_QLabel
            qlabel.setText('')
            ba = QtCore.QByteArray.fromRawData(data)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(ba)
            qlabel.setPixmap(pixmap)
        elif data_base64 is not None:
            qlabel = self.QT_QLabel
            qlabel.setText('')
            ba = QtCore.QByteArray.fromBase64(data_base64)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(ba)
            qlabel.setPixmap(pixmap)
        super().Update(self.QT_QLabel, visible=visible)

    update = Update


# ---------------------------------------------------------------------- #
#                           Canvas                                       #
# ---------------------------------------------------------------------- #
class Canvas(Element):
    def __init__(self, canvas=None, background_color=None, size=(None, None), pad=None, key=None, k=None, tooltip=None, metadata=None):
        """
        Canvas Element - NOT USED IN QT PORT ?
        :param canvas: Your own tk.Canvas if you already created it. Leave blank to create a Canvas
        :type canvas: (tk.Canvas)
        :param background_color: color of background
        :type background_color: (str)
        :param size: (width in char, height in rows) size in pixels to make canvas
        :type size: Tuple[int,int]
        :param pad: Amount of padding to put around element
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self._TKCanvas = canvas

        super().__init__(ELEM_TYPE_CANVAS, background_color=background_color, size=size, pad=pad, key=key,
                         tooltip=tooltip, metadata=metadata)
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
    def __init__(self, canvas_size, graph_bottom_left, graph_top_right, background_color=None, pad=None, key=None, k=None,
                 tooltip=None, visible=True, change_submits=False, enable_events=False, drag_submits=False, metadata=None):
        """
        :param canvas_size: size of the canvas area in pixels
        :type canvas_size: Tuple[int, int]
        :param graph_bottom_left: (x,y) The bottoms left corner of your coordinate system
        :type graph_bottom_left: Tuple[int, int]
        :param graph_top_right: (x,y) The top right corner of  your coordinate system
        :type graph_top_right: Tuple[int, int]
        :param background_color: background color of the drawing area
        :type background_color: (str)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element (Default = True)
        :type visible: (bool)
        :param change_submits: * DEPRICATED DO NOT USE. Use `enable_events` instead
        :type change_submits: (bool)
        :param enable_events: If True then clicks on the Graph are immediately reported as an event. Use this instead of change_submits
        :type enable_events: (bool)
        :param drag_submits: if True and Events are enabled for the Graph, will report Events any time the mouse moves while button down
        :type drag_submits: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.CanvasSize = canvas_size
        self.BottomLeft = graph_bottom_left
        self.TopRight = graph_top_right
        self.x  = self.y = 0
        self.Widget = self.QT_QGraphicsScene = None       # type: QGraphicsScene

        super().__init__(ELEM_TYPE_GRAPH, background_color=background_color, size=(None, None), pad=pad, key=key,
                         tooltip=tooltip, visible=visible, size_px=canvas_size, metadata=metadata)
        return




    def _convert_xy_to_canvas_xy(self, x_in, y_in):
        scale_x = (self.CanvasSize[0] - 0) / (self.TopRight[0] - self.BottomLeft[0])
        scale_y = (0 - self.CanvasSize[1]) / (self.TopRight[1] - self.BottomLeft[1])
        new_x = 0 + scale_x * (x_in - self.BottomLeft[0])
        new_y = self.CanvasSize[1] + scale_y * (y_in - self.BottomLeft[1])
        return new_x, new_y

    def DrawLine(self, point_from, point_to, color='black', width=1):
        converted_point_from = self._convert_xy_to_canvas_xy(point_from[0], point_from[1])
        converted_point_to = self._convert_xy_to_canvas_xy(point_to[0], point_to[1])

        qcolor = QColor(color)
        pen = QPen(qcolor, width)
        line = self.QT_QGraphicsScene.addLine(self.x+converted_point_from[0],self.y+ converted_point_from[1], self.x+converted_point_to[0],self.y+ converted_point_to[1], pen=pen)
        # self.QT_QGraphicsItemGroup.addToGroup(line)
        return line

    def DrawRectangle(self, top_left, bottom_right, fill_color=None, line_color=None):
        converted_point_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_point_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0],  bottom_right[1])

        qcolor = QColor(line_color)
        pen = QPen(qcolor, 1)
        qcolor = QColor(fill_color)
        brush = QBrush(qcolor)
        line = self.QT_QGraphicsScene.addRect(converted_point_top_left[0],converted_point_top_left[1],
                                              converted_point_bottom_right[0]-converted_point_top_left[0],
                                              converted_point_bottom_right[1]-converted_point_top_left[1],
                                             pen, brush)
        # self.QT_QGraphicsItemGroup.addToGroup(line)


    def DrawCircle(self, center_location, radius, fill_color=None, line_color='black'):
        converted_point = self._convert_xy_to_canvas_xy(center_location[0], center_location[1])
        qcolor = QColor(line_color)
        pen = QPen(qcolor)
        qcolor = QColor(fill_color)
        brush = QBrush(qcolor)
        circle_id = self.QT_QGraphicsScene.addEllipse(self.x+converted_point[0], self.y+converted_point[1],
                                           radius, radius, pen=pen, brush=brush)
        return circle_id            # type: QGraphicsEllipseItem

    def RelocateFigure(self, id, x, y):
        id=id           # type: QtWidgets.QGraphicsEllipseItem
        converted_point = self._convert_xy_to_canvas_xy(x, y)
        id.setX(converted_point[0])
        id.setY(converted_point[1])



    def DrawText(self, text, location, color='black', font=None, angle=0):
        converted_point = self._convert_xy_to_canvas_xy(location[0], location[1])

        qcolor = QColor(color)
        qpath = QPainterPath()
        _font = font or ('courier', 12)
        qfont = QFont(_font[0], _font[1])
        # qfont.setWeight(.5)

        text_id = qpath.addText(self.x+converted_point[0], self.y+converted_point[1], qfont, str(text))
        self.QT_QGraphicsScene.addPath(qpath, qcolor)
        return text_id

    def Move(self, x_direction, y_direction):
        x_direction = -x_direction
        y_direction = -y_direction
        zero_converted = self._convert_xy_to_canvas_xy(0, 0)
        shift_converted = self._convert_xy_to_canvas_xy(x_direction, y_direction)
        shift_amount = (shift_converted[0] - zero_converted[0], shift_converted[1] - zero_converted[1])
        rect =  self.QT_QGraphicsScene.sceneRect()
        rect.translate(shift_amount[0], shift_amount[1])
        self.x += shift_amount[0]
        self.y += shift_amount[1]
        self.QT_QGraphicsScene.setSceneRect(rect)
        # items = self.QT_QGraphicsScene.items()
        # print(len(items))
        # for item in items:
        #     if not item.isActive():
        #         print('*', end='')
        #         item.removeFromIndex()

        # print(rect)



    def DrawOval(self, top_left, bottom_right, fill_color=None, line_color=None):
        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return self._TKCanvas2.create_oval(converted_top_left[0], converted_top_left[1], converted_bottom_right[0],
                                           converted_bottom_right[1], fill=fill_color, outline=line_color)

    def DrawPoint(self, point, size=2, color='black'):
        converted_point = self._convert_xy_to_canvas_xy(point[0], point[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return self._TKCanvas2.create_oval(converted_point[0] - size, converted_point[1] - size,
                                           converted_point[0] + size, converted_point[1] + size, fill=color,
                                           outline=color)


    def DrawArc(self, top_left, bottom_right, extent, start_angle, style=None, arc_color='black'):
        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return self._TKCanvas2.create_arc(converted_top_left[0], converted_top_left[1], converted_bottom_right[0],
                                          converted_bottom_right[1], extent=extent, start=start_angle, style='tkstyle',
                                          outline=arc_color)

    def DrawRectangleOld(self, top_left, bottom_right, fill_color=None, line_color=None):
        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return self._TKCanvas2.create_rectangle(converted_top_left[0], converted_top_left[1], converted_bottom_right[0],
                                                converted_bottom_right[1], fill=fill_color, outline=line_color)


    def Erase(self):
        if self.QT_QGraphicsScene is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        self.QT_QGraphicsScene.clear()

    def Update(self, background_color, visible=None):
        # TODO
        # if self._TKCanvas2 is None:
        #     print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
        #     print('Call Window.Finalize() prior to this operation')
        #     return None
        # self._TKCanvas2.configure(background=background_color)
        super().Update(self.QT_QGraphicsScene, visible=visible)

    def MoveFigure(self, figure, x_direction, y_direction):
        zero_converted = self._convert_xy_to_canvas_xy(0, 0)
        shift_converted = self._convert_xy_to_canvas_xy(x_direction, y_direction)
        shift_amount = (shift_converted[0] - zero_converted[0], shift_converted[1] - zero_converted[1])
        if figure is None:
            print('*** WARNING - Your figure is None. It most likely means your did not Finalize your Window ***')
            print('Call Window.Finalize() prior to all graph operations')
            return None
        self._TKCanvas2.move(figure, shift_amount[0], shift_amount[1])


    def change_coordinates(self, graph_bottom_left, graph_top_right):
        """
        Changes the corrdinate system to a new one.  The same 2 points in space are used to define the coorinate
        system - the bottom left and the top right values of your graph.

        :param graph_bottom_left: Tuple[int, int] (x,y) The bottoms left corner of your coordinate system
        :param graph_top_right: Tuple[int, int]  (x,y) The top right corner of  your coordinate system
        """
        self.BottomLeft = graph_bottom_left
        self.TopRight = graph_top_right


    @property
    def TKCanvas(self):
        if self._TKCanvas2 is None:
            print('*** Did you forget to call Finalize()? Your code should look something like: ***')
            print('*** form = sg.Window("My Form").Layout(layout).Finalize() ***')
        return self._TKCanvas2


    draw_arc = DrawArc
    draw_circle = DrawCircle
    draw_line = DrawLine
    draw_oval = DrawOval
    draw_point = DrawPoint
    draw_rectangle = DrawRectangle
    draw_rectangle_old = DrawRectangleOld
    draw_text = DrawText
    erase = Erase
    move = Move
    move_figure = MoveFigure
    relocate_figure = RelocateFigure
    update = Update


# ---------------------------------------------------------------------- #
#                           Frame                                        #
# ---------------------------------------------------------------------- #
class Frame(Element):
    def __init__(self, title, layout, title_color=None, background_color=None, title_location=None,
                 relief=DEFAULT_FRAME_RELIEF, element_justification='float', size=(None, None), font=None, pad=None, border_width=None, key=None, k=None,
                 tooltip=None, visible=True, size_px=(None,None), metadata=None):
        """
        :param title: text that is displayed as the Frame's "label" or title
        :type title: (str)
        :param layout: The layout to put inside the Frame
        :type layout: List[List[Elements]]
        :param title_color: color of the title text
        :type title_color: (str)
        :param background_color: background color of the Frame
        :type background_color: (str)
        :param title_location: location to place the text title.  Choices include: TITLE_LOCATION_TOP TITLE_LOCATION_BOTTOM TITLE_LOCATION_LEFT TITLE_LOCATION_RIGHT TITLE_LOCATION_TOP_LEFT TITLE_LOCATION_TOP_RIGHT TITLE_LOCATION_BOTTOM_LEFT TITLE_LOCATION_BOTTOM_RIGHT
        :type title_location: (enum)
        :param relief: relief style. Values are same as other elements with reliefs. Choices include RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID
        :type relief: (enum)
        :param element_justification: All elements inside the Frame will have this justification 'left', 'right', 'center' are valid values
        :type element_justification: (str)
        :param size: (width, height) (note this parameter may not always work)
        :type size: Tuple[int, int]
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param border_width: width of border around element in pixels
        :type border_width: (int)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
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
        self.ElementJustification = element_justification
        self.Widget = self.QT_QGroupBox = None              # type: QGroupBox
        self.Layout(layout)

        super().__init__(ELEM_TYPE_FRAME, background_color=background_color, text_color=title_color, size=size,
                         font=font, pad=pad, key=key, tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)
        return

    def AddRow(self, *args):
        """ Parms are a variable number of Elements """
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

    def Update(self, visible=None):
        super().Update(self.QT_QGroupBox, visible=visible)

    add_row = AddRow
    layout = Layout
    update = Update


# ---------------------------------------------------------------------- #
#                           Separator                                    #
# ---------------------------------------------------------------------- #
class VerticalSeparator(Element):
    def __init__(self, pad=None):
        """
        VerticalSeperator - A separator that spans only 1 row in a vertical fashion
        :param pad:
        """
        self.Orientation = 'vertical'  # for now only vertical works

        super().__init__(ELEM_TYPE_SEPARATOR, pad=pad)




VSeperator = VerticalSeparator
VSeparator = VerticalSeparator
VSep = VerticalSeparator


# ---------------------------------------------------------------------- #
#                           Separator                                    #
# ---------------------------------------------------------------------- #
class HorizontalSeparator(Element):
    def __init__(self, pad=None, size_px=(None,None)):
        """
        VerticalSeperator - A separator that spans only 1 row in a vertical fashion
        :param pad:
        """
        self.Orientation = 'horizontal'  # for now only vertical works

        super().__init__(ELEM_TYPE_SEPARATOR, pad=pad)



HSeperator = HorizontalSeparator
HSep = HorizontalSeparator



# ---------------------------------------------------------------------- #
#                           Tab                                          #
# ---------------------------------------------------------------------- #
class Tab(Element):
    def __init__(self, title, layout, title_color=None, element_justification='float', background_color=None, font=None, pad=None, disabled=False,
                 border_width=None, key=None, k=None, tooltip=None, visible=True, metadata=None):
        """
        :param title: text to show on the tab
        :type title: (str)
        :param layout: The element layout that will be shown in the tab
        :type layout: List[List[Element]]
        :param title_color: color of the tab text (note not currently working on tkinter)
        :type title_color: (str)
        :param element_justification: All elements inside the Tab will have this justification 'left', 'right', 'center' are valid values
        :type element_justification: (str)
        :param background_color: color of background of the entire layout
        :type background_color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param disabled: If True button will be created disabled
        :type disabled: (bool)
        :param border_width: width of border around element in pixels
        :type border_width: (int)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
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
        self.ParentTabGroup = None                          # type: TabGroup
        self.TabID = None
        self.ElementJustification = element_justification
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.Widget = self.QT_QWidget = None                # type: QWidget



        self.Layout(layout)

        super().__init__(ELEM_TYPE_TAB, background_color=background_color, text_color=title_color, font=font, pad=pad,
                         key=key, tooltip=tooltip, visible=visible, metadata=metadata)
        return

    def AddRow(self, *args):
        """ Parms are a variable number of Elements """
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
        return self

    def Update(self, disabled=None, visible=None):  # TODO Disable / enable of tabs is not complete
        if disabled is None:
            return
        self.Disabled = disabled
        # state = 'disabled' if disabled is True else 'normal'
        # self.ParentNotebook.tab(self.TabID, state=state)
        super().Update(self.QT_QWidget, visible=visible)

        return self

    def _GetElementAtLocation(self, location):
        (row_num, col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element


    def Select(self):
        """
        Selects this tab.  Mimics user clicking on this tab. Must have called window.Finalize / Read first!
        """
        try:
            index = self.ParentTabGroup.TabList.index(self)
            self.ParentTabGroup.QT_QTabWidget.setCurrentIndex(index)
        except:
            print('** EXCEPTION while trying to Select tab with key =', self.Key)

    add_row = AddRow
    layout = Layout
    select = Select
    update = Update

# ---------------------------------------------------------------------- #
#                           TabGroup                                     #
# ---------------------------------------------------------------------- #
class TabGroup(Element):
    def __init__(self, layout, tab_location=None, title_color=None, selected_title_color=None, background_color=None,
                 font=None, change_submits=False, enable_events=False, pad=None, border_width=None, theme=None, key=None, k=None, tooltip=None, visible=True, metadata=None):
        """
        :param layout: Layout of Tabs. Different than normal layouts. ALL Tabs should be on first row
        :type layout: List[List[Tab]]
        :param tab_location: location that tabs will be displayed. Choices are left, right, top, bottom, lefttop, leftbottom, righttop, rightbottom, bottomleft, bottomright, topleft, topright
        :type tab_location: (str)
        :param title_color: color of text on tabs
        :type title_color: (str)
        :param selected_title_color: color of tab text when it is selected
        :type selected_title_color: (str)
        :param background_color: color of background area that tabs are located on
        :type background_color: (str)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param change_submits: * DEPRICATED DO NOT USE. Use `enable_events` instead
        :type change_submits: (bool)
        :param enable_events: If True then switching tabs will generate an Event
        :type enable_events: (bool)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param border_width: width of border around element in pixels
        :type border_width: (int)
        :param theme: DEPRICATED - You can only specify themes using set options or when window is created. It's not possible to do it on an element basis
        :type theme: (enum)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
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
        self.BackgroundColor = background_color if background_color is not None else COLOR_SYSTEM_DEFAULT
        self.ChangeSubmits = change_submits or enable_events
        self.TabLocation = tab_location
        self.TabList = []                                   # type: List[Tab]
        self.Widget = self.QT_QTabWidget = None             # type: QTabWidget
        self.ElementJustification = 'float'                 # not actually used, but needed for packer to work
        self.Layout(layout)

        super().__init__(ELEM_TYPE_TAB_GROUP, background_color=self.BackgroundColor, text_color=title_color, font=font,
                         pad=pad, key=key, tooltip=tooltip, visible=visible, metadata=metadata)
        return

    def AddRow(self, *args):
        """ Parms are a variable number of Elements """
        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            element.ParentTabGroup = self
            CurrentRow.append(element)
            if element.Key is not None:
                self.UseDictionary = True
            self.TabList.append(element)
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

    def FindKeyFromTabName(self, tab_name):
        for row in self.Rows:
            for element in row:
                if element.Title == tab_name:
                    return element.Key
        return None


    def Update(self, visible=None):
        super().Update(self.QT_QTabWidget, visible=visible)
        return self

    def QtCallbackStateChanged(self, state):
        if self.ChangeSubmits:
            _element_callback_quit_mainloop(self)

    def Get(self):
        """
        Returns the current value for the Tab Group, which will be the currently selected tab's KEY or the text on
        the tab if no key is defined.  Returns None if an error occurs.
        Note that this is exactly the same data that would be returned from a call to Window.Read. Are you sure you
        are using this method correctly?

        :return: Union[Any, None] The key of the currently selected tab or the tab's text if it has no key
        """
        value = None
        try:
            cur_index = self.QT_QTabWidget.currentIndex()
            tab_element = self.TabList[cur_index]
            value = tab_element.Key
        except:
            value = None
        return value

    add_row = AddRow
    find_key_from_tab_name = FindKeyFromTabName
    get = Get
    update = Update


# ---------------------------------------------------------------------- #
#                           Slider                                       #
# ---------------------------------------------------------------------- #
class Slider(Element):
    def __init__(self, range=(None, None), default_value=None, resolution=None, tick_interval=None, orientation=None,
                 border_width=None, relief=None, change_submits=False, enable_events=False, disabled=False, size=(None, None), font=None,
                 background_color=None, text_color=None, key=None, k=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
        """
        :param range: slider's range (min value, max value)
        :type range: Union[Tuple[int, int], Tuple[float, float]]
        :param default_value: starting value for the slider
        :type default_value: Union[int, float]
        :param resolution: the smallest amount the slider can be moved
        :type resolution: Union[int, float]
        :param tick_interval: how often a visible tick should be shown next to slider
        :type tick_interval: Union[int, float]
        :param orientation: 'horizontal' or 'vertical' ('h' or 'v' also work)
        :type orientation: (str)
        :param border_width: width of border around element in pixels
        :type border_width: (int)
        :param relief: relief style. RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID
        :type relief: (enum)
        :param change_submits: * DEPRICATED DO NOT USE. Use `enable_events` instead
        :type change_submits: (bool)
        :param enable_events: If True then moving the slider will generate an Event
        :type enable_events: (bool)
        :param disabled: set disable state for element
        :type disabled: (bool)
        :param size: (w=characters-wide, h=rows-high)
        :type size: Tuple[int, int]
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of slider's background
        :type background_color: (str)
        :param text_color: color of the slider's text
        :type text_color: (str)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.TKScale = None
        self.Range = (1, 10) if range == (None, None) else range
        self.DefaultValue = self.Range[0] if default_value is None else default_value
        self.Orientation = orientation if orientation else DEFAULT_SLIDER_ORIENTATION
        self.BorderWidth = border_width if border_width else DEFAULT_SLIDER_BORDER_WIDTH
        self.Relief = relief if relief else DEFAULT_SLIDER_RELIEF
        self.Resolution = 1 if resolution is None else resolution
        self.ChangeSubmits = change_submits or enable_events
        self.Disabled = disabled
        self.TickInterval = tick_interval if tick_interval is not None else self.Range[1]//10
        temp_size = size
        if temp_size == (None, None):
            temp_size = (150, 30) if self.Orientation.startswith('h') else (30, 150)
        elif size[0] is not None and size[0] < 100:
            temp_size = size[0]*10, size[1]*3
        self.Widget = self.QT_Slider = None         # type:QSlider

        super().__init__(ELEM_TYPE_INPUT_SLIDER, size=temp_size, font=font, background_color=background_color,
                         text_color=text_color, key=key, pad=pad, tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)
        return


    def _QtCallbackValueChanged(self, value):
        if not self.ChangeSubmits:
            return
        _element_callback_quit_mainloop(self)

    def Update(self, value=None, range=(None, None), disabled=None, visible=None):
        if value is not None:
            self.QT_Slider.setValue(int(value))
            self.DefaultValue = value
        if disabled == True:
            self.QT_Slider.setDisabled(True)
        elif disabled == False:
            self.QT_Slider.setDisabled(False)
        if range != (None, None):
            self.Range = range
            self.QT_Slider.setMinimum(range[0])
            self.QT_Slider.setMaximum(range[1])
        super().Update(self.QT_Slider, visible=visible)


    update = Update



# ---------------------------------------------------------------------- #
#                           Dial                                         #
# ---------------------------------------------------------------------- #
class Dial(Element):
    def __init__(self, range=(None, None), default_value=None, resolution=None, tick_interval=None, orientation=None,
                 border_width=None, relief=None, change_submits=False, enable_events=False, disabled=False, size=(None, None), font=None,
                 background_color=None, text_color=None, key=None, k=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
        """
        :param range: slider's range (min value, max value)
        :type range: Union[Tuple[int, int], Tuple[float, float]]
        :param default_value: Choice to be displayed as initial value. Must match one of values variable contents
        :type default_value: (Any)
        :param resolution: the smallest amount the slider can be moved
        :type resolution: Union[int, float]
        :param tick_interval: how often a visible tick should be shown next to slider
        :type tick_interval: Union[int, float]
        :param orientation: 'horizontal' or 'vertical' ('h' or 'v' also work)
        :type orientation: (str)
        :param border_width: width of border around button in pixels
        :type border_width: (int)
        :param relief: relief style. RELIEF_RAISED RELIEF_SUNKEN RELIEF_FLAT RELIEF_RIDGE RELIEF_GROOVE RELIEF_SOLID
        :type relief: (enum)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. If this button is a target, should it generate an event when filled in
        :type enable_events: (bool)
        :param disabled: set disable state for element
        :type disabled: (bool)
        :param size: (width, height) of the button in characters wide, rows high
        :type size: Tuple[int, int]
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of slider's background
        :type background_color: (str)
        :param text_color: color of the element's text
        :type text_color: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
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
            temp_size = (20, 20) if self.Orientation.startswith('h') else (8, 20)
        self.Widget = self.QT_Dial = None           # type: QDial

        super().__init__(ELEM_TYPE_INPUT_DIAL, size=temp_size, font=font, background_color=background_color,
                         text_color=text_color, key=key, pad=pad, tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)
        return


    def Update(self, value=None, range=(None, None), disabled=None, visible=None):
        if value is not None:           # TODO clearly not done!
            pass
            self.DefaultValue = value
        if disabled == True:
            pass
        elif disabled == False:
            pass
        super().Update(self.QT_Dial, visible=visible)


    def _QtCallbackValueChanged(self, value):
        if not self.ChangeSubmits:
            return
        _element_callback_quit_mainloop(self)

    update = Update

# ---------------------------------------------------------------------- #
#                           Stretch                                       #
# ---------------------------------------------------------------------- #
class Stretch(Element):
    def __init__(self, size=(None, None), font=None, background_color=None, text_color=None, key=None, k=None, pad=None, tooltip=None):
        """
        :param size: (width, height) of the button in characters wide, rows high
        :type size: Tuple[int, int]
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param background_color: color of slider's background
        :type background_color: (str)
        :param text_color: color of the element's text
        :type text_color: (str)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        """
        key = key if key is not None else k
        self.Widget = None          # type: Stretch
        super().__init__(ELEM_TYPE_STRETCH, size=size, font=font, background_color=background_color,
                         text_color=text_color, key=key, pad=pad, tooltip=tooltip)
        return




# ---------------------------------------------------------------------- #
#                           Column                                       #
# ---------------------------------------------------------------------- #
class Column(Element):
    def __init__(self, layout, background_color=None, element_justification='float', size=(None, None), pad=None, scrollable=False, key=None, k=None, visible=True, metadata=None):

        """
        :param layout: Layout that will be shown in the Column container
        :type layout: List[List[Element]]
        :param background_color: color of background of entire Column
        :type background_color: (str)
        :param element_justification: All elements inside the Column will have this justification 'left', 'right', 'center' are valid values
        :type element_justification: (str)
        :param size: (width, height) size in pixels (doesn't work quite right, sometimes only 1 dimension is set by tkinter
        :type size: Tuple[int, int]
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param scrollable: if True then scrollbars will be added to the column
        :type scrollable: (bool)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.UseDictionary = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.ParentWindow = None
        self.Rows = []
        self.TKFrame = None
        self.Scrollable = scrollable
        # self.ImageFilename = image_filename
        # self.ImageData = image_data
        # self.ImageSize = image_size
        # self.ImageSubsample = image_subsample
        bg = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.ElementJustification = element_justification
        self.Widget = self.QT_QGroupBox = None          # type: QGroupBox
        self.vbox_layout = None                         # type: QVBoxLayout
        self.Layout(layout)

        super().__init__(ELEM_TYPE_COLUMN, background_color=bg, size=size, pad=pad, key=key, visible=visible, metadata=metadata)
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


    def Update(self, visible=None):

        super().Update(self.QT_QGroupBox, visible=visible)

    add_row = AddRow
    layout = Layout
    update = Update

Col = Column

# ---------------------------------------------------------------------- #
#                           Menu                                       #
# ---------------------------------------------------------------------- #
class Menu(Element):
    def __init__(self, menu_definition, background_color=None, size=(None, None), tearoff=False, pad=None, key=None, k=None, visible=True, metadata=None):
        """
        :param menu_definition: a menu definition (in menu definition format)
        :type menu_definition: List[List[Tuple[str, List[str]]]
        :param background_color: color of the background
        :type background_color: (str)
        :param size: Not used in the tkinter port
        :type size: Tuple[int, int]
        :param tearoff: if True, then can tear the menu off from the window ans use as a floating window. Very cool effect
        :type tearoff: (bool)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Value that uniquely identifies this element from all other elements. Used when Finding an element or in return values. Must be unique to the window
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.MenuDefinition = menu_definition
        self.TKMenu = None
        self.Tearoff = tearoff
        self.IsButtonMenu = False
        self.MenuItemChosen = None
        self.Widget = self.QT_QMenuBar = None           # type: QMenuBar

        super().__init__(ELEM_TYPE_MENUBAR, background_color=background_color, size=size, pad=pad, key=key, visible=visible, metadata=metadata)


    def _QT_MenuItemChosenCallback(self, item_chosen):
        # print('IN MENU ITEM CALLBACK', item_chosen)
        self.MenuItemChosen = item_chosen.replace('&','')
        _element_callback_quit_mainloop(self)
        # self.ParentForm.LastButtonClicked = item_chosen
        # self.ParentForm.FormRemainedOpen = True
        # if self.ParentForm.CurrentlyRunningMainloop:
        #     pass # TODO  # kick the users out of the mainloop

    def Update(self, menu_definition=None, visible=None):
        if menu_definition is not None:
            menu_def = menu_definition
            self.MenuDefinition = menu_def
            self.QT_QMenuBar = QMenuBar(self.ParentForm.QT_QMainWindow)

            for menu_entry in menu_def:
                # print(f'Adding a Menubar ENTRY {menu_entry}')
                baritem = QMenu(self.QT_QMenuBar)
                if menu_entry[0][0] == MENU_DISABLED_CHARACTER:
                    baritem.setDisabled(True)
                    baritem.setTitle(menu_entry[0][1:])
                else:
                    baritem.setTitle(menu_entry[0])
                self.QT_QMenuBar.addAction(baritem.menuAction())
                AddMenuItem(baritem, menu_entry[1], self)

            self.ParentForm.QT_QMainWindow.setMenuBar(self.QT_QMenuBar)
        super().Update(self.QT_QMenuBar, visible=visible)

    update = Update

# ---------------------------------------------------------------------- #
#                           Table                                        #
# ---------------------------------------------------------------------- #
class Table(Element):
    def __init__(self, values, headings=None, visible_column_map=None, col_widths=None, def_col_width=10,
                 auto_size_columns=True, max_col_width=20, select_mode=None, display_row_numbers=False, num_rows=None,
                 font=None, justification='right',header_text_color=None, header_background_color=None, header_font=None,  text_color=None, background_color=None, alternating_row_color=None,
                 size=(None, None), change_submits=False, enable_events=False, bind_return_key=False, pad=None, key=None, k=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
        """
        :param values: ???
        :type values: List[List[Union[str, int, float]]]
        :param headings: The headings to show on the top line
        :type headings: Union[List[str], Tuple[str]]
        :param visible_column_map: One entry for each column. False indicates the column is not shown
        :type visible_column_map: List[bool]
        :param col_widths: Number of characters that each column will occupy
        :type col_widths: List[int]
        :param def_col_width: Default column width in characters
        :type def_col_width: (int)
        :param auto_size_columns: if True columns will be sized automatically
        :type auto_size_columns: (bool)
        :param max_col_width: Maximum width for all columns in characters
        :type max_col_width: (int)
        :param select_mode: Select Mode. Valid values start with "TABLE_SELECT_MODE_".  Valid values are: TABLE_SELECT_MODE_NONE TABLE_SELECT_MODE_BROWSE TABLE_SELECT_MODE_EXTENDED
        :type select_mode: (enum)
        :param display_row_numbers: if True, the first column of the table will be the row #
        :type display_row_numbers: (bool)
        :param num_rows: The number of rows of the table to display at a time
        :type num_rows: (int)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param justification: 'left', 'right', 'center' are valid choices
        :type justification: (str)
        :param header_text_color: sets the text color for the header
        :type header_text_color: (str)
        :param header_background_color: sets the background color for the header
        :type header_background_color: (str)
        :param header_font: specifies the font family, size, etc
        :type header_font: Union[str, Tuple[str, int]]
        :param text_color: color of the text
        :type text_color: (str)
        :param background_color: color of background
        :type background_color: (str)
        :param alternating_row_color: if set then every other row will have this color in the background.
        :type alternating_row_color: (str)
        :param size: DO NOT USE! Use num_rows instead
        :type size: Tuple[int, int]
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Table events happen when row is clicked
        :type enable_events: (bool)
        :param bind_return_key: if True, pressing return key will cause event coming from Table, ALSO a left button double click will generate an event if this parameter is True
        :type bind_return_key: (bool)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
        self.Values = values
        self.ColumnHeadings = headings
        self.ColumnsToDisplay = visible_column_map
        self.ColumnWidths = col_widths
        self.MaxColumnWidth = max_col_width
        self.DefaultColumnWidth = def_col_width
        self.AutoSizeColumns = auto_size_columns
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.TextColor = text_color
        self.HeaderTextColor = header_text_color if header_text_color is not None else LOOK_AND_FEEL_TABLE[CURRENT_LOOK_AND_FEEL]['TEXT_INPUT']
        self.HeaderBackgroundColor = header_background_color if header_background_color is not None else LOOK_AND_FEEL_TABLE[CURRENT_LOOK_AND_FEEL]['INPUT']
        self.HeaderFont = header_font
        self.Justification = justification
        self.InitialState = None
        self.SelectMode = select_mode
        self.DisplayRowNumbers = display_row_numbers
        self.NumRows = num_rows if num_rows is not None else size[1]
        self.TKTreeview = None
        self.AlternatingRowColor = alternating_row_color
        self.SelectedRows = []
        self.ChangeSubmits = change_submits or enable_events
        self.BindReturnKey = bind_return_key
        self.Widget = self.QT_TableWidget = None                    # type: QTableWidget

        super().__init__(ELEM_TYPE_TABLE, text_color=text_color, background_color=background_color, font=font,
                         size=size, pad=pad, key=key, tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)
        return


    def _QtCallbackCellActivated(self, value=None):
        # print('CELL ACTIVATED ', value)
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if not self.ChangeSubmits:
            return
        _element_callback_quit_mainloop(self)


    def _QtCallbackVerticalHeader(self, value):
        print('Vertical Header value ', value)


    def Update(self, values=None, num_rows=None, visible=None):
        if values is not None:
            self.Values = values
            self.SelectedRows = []
            self.QT_TableWidget.clearContents()
            if len(values) != 0:
                self.QT_TableWidget.setRowCount(len(self.Values))
                self.QT_TableWidget.setColumnCount(len(self.Values[0]))
                for rownum, rows in enumerate(self.Values):
                    # self.QT_TableWidget.insertRow(rownum)
                    for colnum, columns in enumerate(rows):
                        self.QT_TableWidget.setItem(rownum, colnum, QTableWidgetItem(self.Values[rownum][colnum]))
        if num_rows is not None:
            self.QT_TableWidget.setFixedHeight(num_rows * 35 + 25)  # convert num rows into pixels...crude but effective

        super().Update(self.QT_TableWidget, visible=visible)


    def Get(self):
        num_rows = self.QT_TableWidget.rowCount()
        num_cols = self.QT_TableWidget.columnCount()
        table = []
        for row in range(num_rows):
            row_list = []
            for col in range(num_cols):
                item = self.QT_TableWidget.item(row, col).text()
                row_list.append(item)
            table.append(row_list)

        return table

    def _treeview_selected(self, event):
        if self.ChangeSubmits:
            MyForm = self.ParentForm
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = ''
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                pass # TODO Quit mainloop


    def treeview_double_click(self, event):
        if self.BindReturnKey:
            MyForm = self.ParentForm
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = ''
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                pass # TODO Quit mainloop


    class QTTableWidget(QTableWidget):
        def __init__(self, enable_key_events, window):
            self.KeyEventsEnabled = enable_key_events
            self.Window = window
            super().__init__()

        def eventFilter(self, widget, event):
            # print(event.type())
            if event.type() == QEvent.MouseButtonPress and self.Window.GrabAnywhere:
                self.mouse_offset = event.pos()
            if event.type() == QEvent.MouseMove and self.Window.GrabAnywhere:
                x = event.globalX()
                y = event.globalY()
                x_w = self.mouse_offset.x()
                y_w = self.mouse_offset.y()
                self.move(x - x_w, y - y_w)

            if event.type() == QEvent.KeyRelease and self.KeyEventsEnabled:
                # print("got key event")
                key = event.key()
                try:
                    self.Window.LastButtonClicked = chr(key).lower()
                except:
                    self.Window.LastButtonClicked = "special %s" % key
                self.Window.FormRemainedOpen = True
                if self.Window.CurrentlyRunningMainloop:
                    self.Window.QTApplication.exit()
            return QWidget.eventFilter(self, widget, event)

    get = Get
    update = Update

# ---------------------------------------------------------------------- #
#                           Tree                                         #
# ---------------------------------------------------------------------- #
class Tree(Element):
    def __init__(self, data=None, headings=None, visible_column_map=None, col_widths=None, col0_width=10,
                 def_col_width=10, auto_size_columns=True, max_col_width=20, select_mode=None, show_expanded=False,
                 change_submits=False, enable_events=False, font=None, size=(200,600),
                 justification='right', text_color=None, background_color=None, num_rows=None, pad=None, key=None, k=None,
                 tooltip=None, visible=True, size_px=(None,None), metadata=None):
        """
        :param data: The data represented using a PySimpleGUI provided TreeData class
        :type data: (TreeData)
        :param headings: List of individual headings for each column
        :type headings: List[str]
        :param visible_column_map: Determines if a column should be visible. If left empty, all columns will be shown
        :type visible_column_map: List[bool]
        :param col_widths: List of column widths so that individual column widths can be controlled
        :type col_widths: List[int]
        :param col0_width: Size of Column 0 which is where the row numbers will be optionally shown
        :type col0_width: (int)
        :param def_col_width: default column width
        :type def_col_width: (int)
        :param auto_size_columns: if True, the size of a column is determined  using the contents of the column
        :type auto_size_columns: (bool)
        :param max_col_width: the maximum size a column can be
        :type max_col_width: (int)
        :param select_mode: Use same values as found on Table Element.  Valid values include: TABLE_SELECT_MODE_NONE TABLE_SELECT_MODE_BROWSE TABLE_SELECT_MODE_EXTENDED
        :type select_mode: (enum)
        :param show_expanded: if True then the tree will be initially shown with all nodes completely expanded
        :type show_expanded: (bool)
        :param change_submits: DO NOT USE. Only listed for backwards compat - Use enable_events instead
        :type change_submits: (bool)
        :param enable_events: Turns on the element specific events. Tree events happen when row is clicked
        :type enable_events: (bool)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param size: ???
        :type size: ???
        :param justification: 'left', 'right', 'center' are valid choices
        :type justification: (str)
        :param text_color: color of the text
        :type text_color: (str)
        :param background_color: color of background
        :type background_color: (str)
        :param num_rows: The number of rows of the table to display at a time
        :type num_rows: (int)
        :param pad: Amount of padding to put around element (left/right, top/bottom) or ((left, right), (top, bottom))
        :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
        :param key: Used with window.FindElement and with return values to uniquely identify this element to uniquely identify this element
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        :param tooltip: text, that will appear when mouse hovers over the element
        :type tooltip: (str)
        :param visible: set visibility state of the element
        :type visible: (bool)
        :param size_px: size in pixels (width, height). Will override the size parameter
        :type size_px: Tupple[int, int] (width, height)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        key = key if key is not None else k
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
        self.ChangeSubmits = change_submits or enable_events
        self.Size = size
        self.Widget = self.QT_QTreeWidget = None      # type: QTreeWidget
        super().__init__(ELEM_TYPE_TREE, text_color=text_color, background_color=background_color, font=font, pad=pad,
                         key=key, tooltip=tooltip, size=size, visible=visible, size_px=size_px, metadata=metadata)
        return

    def _treeview_selected(self, event):
        selections = 000000
        self.SelectedRows = [x for x in selections]
        # print('Got selection')
        if self.ChangeSubmits:
            _element_callback_quit_mainloop(self)

    def _QtCallbackCellActivated(self, value=None):
        # print('CELL ACTIVATED ', value)
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if not self.ChangeSubmits:
            return
        _element_callback_quit_mainloop(self)

        # if self.ChangeSubmits:
        #     MyForm = self.ParentForm
        #     if self.Key is not None:
        #         self.ParentForm.LastButtonClicked = self.Key
        #     else:
        #         self.ParentForm.LastButtonClicked = ''
        #     self.ParentForm.FormRemainedOpen = True
        #     if self.ParentForm.CurrentlyRunningMainloop:
        #         self.ParentForm.TKroot.quit()


    def Update(self, values=None, key=None, value=None, text=None, visible=None):
        if values is not None:
            self.TreeData = values
            self.SelectedRows = []
            # self.QT_QTreeWidget = QTreeWidget()
            TreeWidgetItems = QTreeWidgetItemIterator(self.QT_QTreeWidget)

            for item in TreeWidgetItems:
                item2 = item.value()
                self.QT_QTreeWidget.removeItemWidget(item2, 0)

            # def add_treeview_data(node, widget):
            #     # print(f'Inserting {node.key} under parent {node.parent}')
            #     child = QTreeWidgetItem(widget)
            #     if node.key != '':
            #         child.setText(0, str(node.text))
            #         # child.setData(0,0,node.values)
            #         if node.icon is not None:
            #             qicon = QIcon(node.icon)
            #             child.setIcon(0, qicon)
            #     for node in node.children:
            #         add_treeview_data(node, child)


            def add_treeview_data(node, widget):
                # print(f'Inserting {node.key} under parent {node.parent}')
                if node != self.TreeData.root_node:
                    child = QTreeWidgetItem(widget)
                    child.setText(0, str(node.text))
                else:
                    child = widget
                # if node.key != '':
                # child.setData(0,0,node.values)
                if type(node.icon) is bytes:
                    ba = QtCore.QByteArray.fromBase64(node.icon)
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(ba)
                    qicon = QIcon(pixmap)
                    child.setIcon(0, qicon)
                elif node.icon is not None:
                    qicon = QIcon(node.icon)
                    child.setIcon(0, qicon)
                for node in node.children:
                    add_treeview_data(node, child)
                return

            add_treeview_data(self.TreeData.root_node, self.QT_QTreeWidget)

        if key is not None:
            pass
        super().Update(self.QT_QTreeWidget, visible=visible)

        return self

    update = Update

class TreeData(object):
    class Node(object):
        def __init__(self, parent, key, text, values, icon=None):
            self.parent = parent
            self.children = []
            self.key = key
            self.text = text
            self.values = values
            self.icon = icon

        def _Add(self, node):
            self.children.append(node)

    def __init__(self):
        self.tree_dict = {}
        self.root_node = self.Node("", "", 'root', [], None)
        self.tree_dict[""] = self.root_node

    def _AddNode(self, key, node):
        self.tree_dict[key] = node

    def Insert(self, parent, key, text, values, icon=None):
        node = self.Node(parent, key, text, values, icon)
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
    def __init__(self, key=None, k=None):
        """
        Error Element
        :param key: key for uniquely identify this element (for window.FindElement)
        :type key: (Any)
        :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
        :type k: Union[str, int, tuple, object]
        """
        self.Key = key
        self.Widget = None

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


# ---------------------------------------------------------------------- #
#                           Pane  Element                                #
# ---------------------------------------------------------------------- #

# This is for source code compatibility with tkinter version. No Qt equivalent
Pane = ErrorElement

# ------------------------------------------------------------------------- #
#                       Tray CLASS                                      #
# ------------------------------------------------------------------------- #
class SystemTray:
    def __init__(self, menu=None, filename=None, data=None, data_base64=None, tooltip=None, metadata=None):
        """
        SystemTray - create an icon in the system tray
        :param menu: Menu definition. Example - ['UNUSED', ['My', 'Simple', '---', 'Menu', 'Exit']]
        :type menu: List[List[List[str] or str]]
        :param filename: filename for icon
        :type filename: (str)
        :param data: in-ram image for icon (same as data_base64 parm)
        :type data: (bytes)
        :param data_base64: base-64 data for icon
        :type data_base64: (bytes)
        :param tooltip: tooltip string
        :type tooltip: (str)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        self.Menu = menu
        self.TrayIcon = None
        self.Shown = False
        self.MenuItemChosen = TIMEOUT_KEY
        self.LastMessage = None
        self.LastTitle = None
        self.metadata = metadata

        if Window.QTApplication is None:
            Window.QTApplication = QApplication(sys.argv)
        self.App = Window.QTApplication
        self.Widget = self.QWidget = QWidget()              # type: QWidget

        if filename is None and data is None and data_base64 is None:
            data_base64 = DEFAULT_BASE64_ICON
        qicon = None
        if filename is not None:
            qicon = QIcon(filename)
        elif data is not None:
            ba = QtCore.QByteArray.fromRawData(data)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(ba)
            qicon = QIcon(pixmap)
        elif data_base64 is not None:
            ba = QtCore.QByteArray.fromBase64(data_base64)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(ba)
            qicon = QIcon(pixmap)
        if qicon is None:
            PopupError('ERROR - Tray must have one form of Icon specified')
            return
        self.TrayIcon = QSystemTrayIcon(qicon)

        if self.Menu is not None:
            qmenu = QMenu()
            qmenu.setTitle(self.Menu[0])
            AddTrayMenuItem(qmenu, self.Menu[1], self)
            self.TrayIcon.setContextMenu(qmenu)

        if tooltip is not None:
            self.TrayIcon.setToolTip(str(tooltip))

        self.TrayIcon.messageClicked.connect(self._message_clicked)
        self.TrayIcon.activated.connect(self._double_clicked)

        self.TrayIcon.show()

    def _QT_MenuItemChosenCallback(self, item_chosen):
        self.MenuItemChosen = item_chosen.replace('&','')
        self.App.exit()                         # kick the users out of the mainloop

    # callback function when message is clicked
    def _message_clicked(self):
        self.MenuItemChosen = EVENT_SYSTEM_TRAY_MESSAGE_CLICKED
        self.App.exit()


    def _double_clicked(self, reason):
        # print(reason)
        if reason == QSystemTrayIcon.DoubleClick:
            self.MenuItemChosen = EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED
            self.App.exit()
        if reason == QSystemTrayIcon.Trigger:
            self.MenuItemChosen = EVENT_SYSTEM_TRAY_ICON_ACTIVATED
            self.App.exit()


    def Read(self, timeout=None):
        """
        Reads the context menu
        :param timeout: Optional.  Any value other than None indicates a non-blocking read
        :return:
        """
        if not self.Shown:
            self.Shown = True
            self.TrayIcon.show()
        if timeout is None:
            self.App.exec_()
        elif timeout == 0:
            self.App.processEvents()
        else:
            self.timer = start_systray_read_timer(self, timeout)
            self.App.exec_()

            if self.timer:
                stop_timer(self.timer)

        item = self.MenuItemChosen
        self.MenuItemChosen = TIMEOUT_KEY
        return item

    def _timer_timeout(self):
        self.App.exit()  # kick the users out of the mainloop

    def Hide(self):
        self.TrayIcon.hide()


    def UnHide(self):
        self.TrayIcon.show()


    def ShowMessage(self, title, message, filename=None, data=None, data_base64=None, messageicon=None, time=10000):
        """
        Shows a balloon above icon in system tray
        :param title:  Title shown in balloon
        :param message: Message to be displayed
        :param filename: Optional icon filename
        :param data: Optional in-ram icon
        :param data_base64: Optional base64 icon
        :param time: How long to display message in milliseconds
        :return:
        """
        qicon = None
        if filename is not None:
            qicon = QIcon(filename)
        elif data is not None:
            ba = QtCore.QByteArray.fromRawData(data)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(ba)
            qicon = QIcon(pixmap)
        elif data_base64 is not None:
            ba = QtCore.QByteArray.fromBase64(data_base64)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(ba)
            qicon = QIcon(pixmap)

        if qicon is not None:
            self.TrayIcon.showMessage(title, message, qicon, time)
        elif messageicon is not None:
            self.TrayIcon.showMessage(title, message, messageicon, time)
        else:
            self.TrayIcon.showMessage(title, message, QIcon(), time)

        self.LastMessage = message
        self.LastTitle = title
        return self

    def Close(self):
        """

        :return:
        """
        self.Hide()
        # Don't close app because windows could be depending on it
        # self.App.quit()


    def Update(self, menu=None, tooltip=None,filename=None, data=None, data_base64=None,):
        """
        Updates the menu, tooltip or icon
        :param menu: menu defintion
        :param tooltip: string representing tooltip
        :param filename:  icon filename
        :param data:  icon raw image
        :param data_base64: icon base 64 image
        :return:
        """
        # Menu
        if menu is not None:
            self.Menu = menu
            qmenu = QMenu()
            qmenu.setTitle(self.Menu[0])
            AddTrayMenuItem(qmenu, self.Menu[1], self)
            self.TrayIcon.setContextMenu(qmenu)
        # Tooltip
        if tooltip is not None:
            self.TrayIcon.setToolTip(str(tooltip))
        # Icon
        qicon = None
        if filename is not None:
            qicon = QIcon(filename)
        elif data is not None:
            ba = QtCore.QByteArray.fromRawData(data)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(ba)
            qicon = QIcon(pixmap)
        elif data_base64 is not None:
            ba = QtCore.QByteArray.fromBase64(data_base64)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(ba)
            qicon = QIcon(pixmap)
        if qicon is not None:
            self.TrayIcon.setIcon(qicon)

    close = Close
    hide = Hide
    read = Read
    show_message = ShowMessage
    un_hide = UnHide
    update = Update

# ------------------------------------------------------------------------- #
#                       Window CLASS                                      #
# ------------------------------------------------------------------------- #
class Window:

    NumOpenWindows = 0
    user_defined_icon = None
    hidden_master_root = None
    QTApplication = None
    active_popups = {}

    def __init__(self, title, layout=None, default_element_size=DEFAULT_ELEMENT_SIZE, default_button_element_size=(None, None),
                 auto_size_text=None, auto_size_buttons=None, location=(None, None), size=(None, None), element_padding=None, margins=(None, None),button_color=None, font=None, progress_bar_color=(None, None), background_color=None, border_depth=None, auto_close=False, auto_close_duration=DEFAULT_AUTOCLOSE_TIME, icon=DEFAULT_WINDOW_ICON, force_toplevel=False, alpha_channel=1, return_keyboard_events=False, use_default_focus=True, text_justification=None, element_justification='float', no_titlebar=False, grab_anywhere=False, keep_on_top=False, resizable=True, disable_close=False, disable_minimize=False, background_image=None, finalize=False, metadata=None):
        """
        :param title: The title that will be displayed in the Titlebar and on the Taskbar
        :type title: (str)
        :param layout: The layout for the window. Can also be specified in the Layout method
        :type layout: List[List[Elements]]
        :param default_element_size: size in characters (wide) and rows (high) for all elements in this window
        :type default_element_size: Tuple[int, int] - (width, height)
        :param default_button_element_size: (width, height) size in characters (wide) and rows (high) for all Button elements in this window
        :type default_button_element_size: Tuple[int, int]
        :param auto_size_text: True if Elements in Window should be sized to exactly fir the length of text
        :type auto_size_text: (bool)
        :param auto_size_buttons: True if Buttons in this Window should be sized to exactly fit the text on this.
        :type auto_size_buttons: (bool)
        :param location: (x,y) location, in pixels, to locate the upper left corner of the window on the screen. Default is to center on screen.
        :type location: Tuple[int, int]
        :param size: (width, height) size in pixels for this window. Normally the window is autosized to fit contents, not set to an absolute size by the user
        :type size: Tuple[int, int]
        :param element_padding: Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom))
        :type element_padding: Tuple[int, int] or ((int, int),(int,int))
        :param margins: (left/right, top/bottom) Not yet implemented!  Parameter here for potability purposes.
        :type margins: Tuple[int, int]
        :param button_color: Default button colors for all buttons in the window
        :type button_color: Tuple[str, str] == (text color, button color)
        :param font: specifies the font family, size, etc
        :type font: Union[str, Tuple[str, int]]
        :param progress_bar_color: (bar color, background color) Sets the default colors for all progress bars in the window
        :type progress_bar_color: Tuple[str, str]
        :param background_color: color of background
        :type background_color: (str)
        :param border_depth: Default border depth (width) for all elements in the window
        :type border_depth: (int)
        :param auto_close: If True, the window will automatically close itself
        :type auto_close: (bool)
        :param auto_close_duration: Number of seconds to wait before closing the window
        :type auto_close_duration: (int)
        :param icon: Can be either a filename or Base64 value. For Windows if filename, it MUST be ICO format. For Linux, must NOT be ICO
        :type icon: Union[str, str]
        :param force_toplevel: If True will cause this window to skip the normal use of a hidden master window
        :type force_toplevel: (bool)
        :param alpha_channel: Sets the opacity of the window. 0 = invisible 1 = completely visible. Values bewteen 0 & 1 will produce semi-transparent windows in SOME environments (The Raspberry Pi always has this value at 1 and cannot change.
        :type alpha_channel: (float)
        :param return_keyboard_events: if True key presses on the keyboard will be returned as Events from Read calls
        :type return_keyboard_events: (bool)
        :param use_default_focus: If True will use the default focus algorithm to set the focus to the "Correct" element
        :type use_default_focus: (bool)
        :param text_justification: Default text justification for all Text Elements in window
        :type text_justification: Union['left', 'right', 'center']
        :param element_justification: All elements in the Window itself will have this justification 'left', 'right', 'center' are valid values
        :type element_justification: (str)
        :param no_titlebar: If true, no titlebar nor frame will be shown on window. This means you cannot minimize the window and it will not show up on the taskbar
        :type no_titlebar: (bool)
        :param grab_anywhere: If True can use mouse to click and drag to move the window. Almost every location of the window will work except input fields on some systems
        :type grab_anywhere: (bool)
        :param keep_on_top: If True, window will be created on top of all other windows on screen. It can be bumped down if another window created with this parm
        :type keep_on_top: (bool)
        :param resizable: If True, allows the user to resize the window. Note the not all Elements will change size or location when resizing.
        :type resizable: (bool)
        :param disable_close: If True, the X button in the top right corner of the window will no work.  Use with caution and always give a way out toyour users
        :type disable_close: (bool)
        :param disable_minimize: if True the user won't be able to minimize window.  Good for taking over entire screen and staying that way.
        :type disable_minimize: (bool)
        :param background_image: ???
        :type background_image: ???
        :param finalize: If True then the Finalize method will be called. Use this rather than chaining .Finalize for cleaner code
        :type finalize: (bool)
        :param metadata: User metadata that can be set to ANYTHING
        :type metadata: (Any)
        """
        self.AutoSizeText = auto_size_text if auto_size_text is not None else DEFAULT_AUTOSIZE_TEXT
        self.AutoSizeButtons = auto_size_buttons if auto_size_buttons is not None else DEFAULT_AUTOSIZE_BUTTONS
        self.Title = title
        self.Rows = []  # a list of ELEMENTS for this row
        self.DefaultElementSize = _convert_tkinter_size_to_Qt(default_element_size)
        self.DefaultButtonElementSize = _convert_tkinter_size_to_Qt(default_button_element_size) if default_button_element_size != (
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
        self.TimeoutKey = '_timeout_'
        self.TimerCancelled = False
        self.DisableClose = disable_close
        self._Hidden = False
        self.QTApplication = None
        self.QT_QMainWindow = None
        self.QTWindow = None        # type Window.QTMainWindow
        self._Size=size
        self.ElementPadding = element_padding or DEFAULT_ELEMENT_PADDING
        self.FocusElement = None
        self.BackgroundImage = background_image
        self.XFound = False
        self.DisableMinimize = disable_minimize
        self.UniqueKeyCounter = 0
        self.metadata = metadata
        self.ElementJustification = element_justification


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
        """ Parms are a variable number of Elements """
        NumRows = len(self.Rows)  # number of existing rows is our row number
        CurrentRowNumber = NumRows  # this row's number
        CurrentRow = []  # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):  # Loop through list of elements and add them to the row
            if type(element) == list:
                PopupError('Error creating layout',
                      'Layout has a LIST instead of an ELEMENT',
                      'This means you have a badly placed ]',
                      'The offensive list is:',
                      element,
                      'This list will be stripped from your layout'
                      )
                continue
            elif callable(element) and not isinstance(element, Element):
                PopupError('Error creating layout',
                      'Layout has a FUNCTION instead of an ELEMENT',
                      'This means you are missing () from your layout',
                      'The offensive list is:',
                      element,
                      'This item will be stripped from your layout')
                continue
            if element.ParentContainer is not None:
                warnings.warn('*** YOU ARE ATTEMPTING TO RESUSE A LAYOUT! You must not attempt this kind of re-use ***', UserWarning)
                PopupError('Error creating layout',
                      'The layout specified has already been used',
                      'You MUST start witha "clean", unused layout every time you create a window',
                      'The offensive Element = ',
                      element,
                      'and has a key = ', element.Key,
                      'This item will be stripped from your layout')
                continue
            element.Position = (CurrentRowNumber, i)
            element.ParentContainer = self
            CurrentRow.append(element)
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    # ------------------------- Add Multiple Rows to Form ------------------------- #
    def AddRows(self, rows):
        for row in rows:
            try:
                iter(row)
            except TypeError:
                PopupError('Error creating layout',
                      'Your row is not an iterable (e.g. a list)',
                      'The offensive row = ',
                      row,
                      'This item will be stripped from your layout')
                continue
            self.AddRow(*row)

    def Layout(self, rows):
        self.AddRows(rows)
        self._BuildKeyDict()
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

    def _timer_timeout(self):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if self.TimerCancelled:
            return
        self.LastButtonClicked = self.TimeoutKey
        self.FormRemainedOpen = True
        if self.CurrentlyRunningMainloop:
            self.QTApplication.exit()  # kick the users out of the mainloop

    def _autoclose_timer_callback(self):
        # print('*** TIMEOUT CALLBACK ***')
        self.autoclose_timer.stop()
        self.QT_QMainWindow.close()
        if self.CurrentlyRunningMainloop:
            # print("quitting window")
            self.QTApplication.exit()  # kick the users out of the mainloop


    def Read(self, timeout=None, timeout_key=TIMEOUT_KEY, close=False):
        """
        THE biggest deal method in the Window class! This is how you get all of your data from your Window.
            Pass in a timeout (in milliseconds) to wait for a maximum of timeout milliseconds. Will return timeout_key
            if no other GUI events happen first.
        Use the close parameter to close the window after reading

        :param timeout: (int) Milliseconds to wait until the Read will return IF no other GUI events happen first
        :param timeout_key: (Any) The value that will be returned from the call if the timer expired
        :param close: (bool) if True the window will be closed prior to returning
        :return: Tuple[(Any), Union[Dict[Any:Any]], List[Any], None] (event, values)
        """
        results = self._read(timeout=timeout, timeout_key=timeout_key)
        if close:
            self.close()

        return results



    def _read(self, timeout=None, timeout_key=TIMEOUT_KEY):
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
                timer = start_window_read_timer(self, timeout)
            else:
                timer = None
            self.CurrentlyRunningMainloop = True
            # print(f'In main {self.Title}')
            ################################# CALL GUI MAINLOOP ############################

            self.QTApplication.exec_()
            # self.LastButtonClicked = 'TEST'
            self.CurrentlyRunningMainloop = False
            self.TimerCancelled = True
            if timer:
                stop_timer(timer)
            if self.RootNeedsDestroying:
                self.LastButtonClicked = None
                self.QTApplication.exit()
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
            self.QTApplication.processEvents()              # refresh the window
        if 0:       # TODO add window closed with X logic
            self.TKrootDestroyed = True
            _my_windows.Decrement()
            # print("read failed")
            # return None, None
        return BuildResults(self, False, self)


    def Finalize(self):
        if self.TKrootDestroyed:
            return self
        if not self.Shown:
            self.Show(non_blocking=True)
        else:
            try:
                self.QTApplication.processEvents()              # refresh the window
            except:
                print('* ERROR FINALIZING *')
                self.TKrootDestroyed = True
                Window.DecrementOpenCount()
        return self


    def Refresh(self):
        self.QTApplication.processEvents()              # refresh the window
        return self

    def VisibilityChanged(self):
        self.Refresh()
        self.Size = self.Size
        self.Refresh()
        self.Size = self.Size
        self.Refresh()
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

    Element =  FindElement          # Shortcut function

    def _BuildKeyDict(self):
        dict = {}
        self.AllKeysDict = self._BuildKeyDictForWindow(self,self, dict)

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
                    elif element.Type == ELEM_TYPE_TAB:
                        element.Key = element.Title
                    if element.Type in (ELEM_TYPE_MENUBAR, ELEM_TYPE_BUTTONMENU, ELEM_TYPE_CANVAS,
                                        ELEM_TYPE_INPUT_SLIDER, ELEM_TYPE_GRAPH, ELEM_TYPE_IMAGE,
                                        ELEM_TYPE_INPUT_CHECKBOX, ELEM_TYPE_INPUT_LISTBOX, ELEM_TYPE_INPUT_COMBO,
                                        ELEM_TYPE_INPUT_MULTILINE, ELEM_TYPE_INPUT_OPTION_MENU, ELEM_TYPE_INPUT_SPIN,
                                        ELEM_TYPE_TABLE, ELEM_TYPE_TREE,
                                        ELEM_TYPE_INPUT_TEXT):
                        element.Key = top_window.DictionaryKeyCounter
                        top_window.DictionaryKeyCounter += 1
                if element.Key is not None:
                    if element.Key in key_dict.keys():
                        print('*** Duplicate key found in your layout {} ***'.format(element.Key)) if element.Type != ELEM_TYPE_BUTTON else None
                        element.Key = str(element.Key) + str(self.UniqueKeyCounter)
                        self.UniqueKeyCounter += 1
                        print('*** Replaced new key with {} ***'.format(element.Key)) if element.Type != ELEM_TYPE_BUTTON else None
                    key_dict[element.Key] = element
        return key_dict

    def FindElementWithFocus(self):
        return _FindElementWithFocusInSubForm(self)
        # return self.FocusElement

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
        if Window.QTApplication is None:
            Window.QTApplication = QApplication(sys.argv)
        try:
            screen = Window.QTApplication.primaryScreen()
        except:
            return None, None
        size = screen.size()
        screen_width = size.width()
        screen_height = size.height()
        return screen_width, screen_height

    def Move(self, x, y):
        if not self._is_window_created():
            return
        self.QT_QMainWindow.move(x, y)

    def Minimize(self):
        if not self._is_window_created():
            return
        self.QT_QMainWindow.setWindowState(Qt.WindowMinimized)

    def Maximize(self):
        if not self._is_window_created():
            return
        self.QT_QMainWindow.setWindowState(Qt.WindowMaximized)


    def StartMove(self, event):
        try:
            self.TKroot.x = event.x
            self.TKroot.y = event.y
        except:
            pass

    def StopMove(self, event):
        try:
            self.TKroot.x = None
            self.TKroot.y = None
        except:
            pass

    def OnMotion(self, event):
        try:
            deltax = event.x - self.TKroot.x
            deltay = event.y - self.TKroot.y
            x = self.TKroot.winfo_x() + deltax
            y = self.TKroot.winfo_y() + deltay
            self.TKroot.geometry("+%s+%s" % (x, y))
        except:
            pass

    def _KeyboardCallback(self, event):
        self.LastButtonClicked = None
        self.FormRemainedOpen = True
        if event.char != '':
            self.LastKeyboardEvent = event.char
        else:
            self.LastKeyboardEvent = str(event.keysym) + ':' + str(event.keycode)
        if not self.NonBlocking:
            BuildResults(self, False, self)
        if self.CurrentlyRunningMainloop:  # quit if this is the current mainloop, otherwise don't quit!
            self.TKroot.quit()

    def _MouseWheelCallback(self, event):
        self.LastButtonClicked = None
        self.FormRemainedOpen = True
        self.LastKeyboardEvent = 'MouseWheel:Down' if event.delta < 0 else 'MouseWheel:Up'
        if not self.NonBlocking:
            BuildResults(self, False, self)
        if self.CurrentlyRunningMainloop:  # quit if this is the current mainloop, otherwise don't quit!
            self.TKroot.quit()

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
        return None

    def Close(self):
        if self.TKrootDestroyed:
            return
        try:
            self.QT_QMainWindow.close()
        except:
            print('error closing window')

    CloseNonBlockingForm = Close
    CloseNonBlocking = Close


    def Disable(self):
        if not self._is_window_created():
            return
        self.QT_QMainWindow.setEnabled(False)

    def Enable(self):
        if not self._is_window_created():
            return
        self.QT_QMainWindow.setEnabled(True)

    def Hide(self):
        if not self._is_window_created():
            return
        self._Hidden = True
        self.QT_QMainWindow.hide()
        return

    def UnHide(self):
        if not self._is_window_created():
            return
        if self._Hidden:
            self.QT_QMainWindow.show()
            self._Hidden = False

    def Disappear(self):
        self.AlphaChannel = 0

    def Reappear(self):
        self.AlphaChannel = 255

    def SetAlpha(self, alpha):
        """
        Change the window's transparency
        :param alpha: From 0 to 1 with 0 being completely transparent
        :return:
        """
        if not self._is_window_created():
            return
        self._AlphaChannel = alpha
        if self._AlphaChannel is not None:
            self.QT_QMainWindow.setWindowOpacity(self._AlphaChannel)

    @property
    def AlphaChannel(self):
        return self._AlphaChannel

    @AlphaChannel.setter
    def AlphaChannel(self, alpha):
        if not self._is_window_created():
            return
        self._AlphaChannel = alpha
        if self._AlphaChannel is not None:
            self.QT_QMainWindow.setWindowOpacity(self._AlphaChannel)

    def BringToFront(self):
        if not self._is_window_created():
            return
        self.QTMainWindow.activateWindow(self.QT_QMainWindow)
        self.QTMainWindow.raise_(self.QT_QMainWindow)


    def CurrentLocation(self):
        if not self._is_window_created():
            return
        location = self.QT_QMainWindow.geometry()
        return location.left(), location.top()


    def set_title(self, title):
        """
        Change the title of the window

        :param title: The string to set the title to
        :type title: (str)
        """
        if not self._is_window_created():
            return
        self.Title = str(title)
        self.QT_QMainWindow.setWindowTitle(self.Title)



    class QTMainWindow(QWidget):
        def __init__(self,enable_key_events, window):
            self.KeyEventsEnabled = enable_key_events
            self.Window = window
            super().__init__(window.QT_QMainWindow)

        def eventFilter(self, widget, event):
            # print(event.type())
            if event.type() == QEvent.MouseButtonPress and self.Window.GrabAnywhere:
                self.mouse_offset = event.pos()
            if event.type() == QEvent.MouseMove and self.Window.GrabAnywhere:
                x = event.globalX()
                y = event.globalY()
                x_w = self.mouse_offset.x()
                y_w = self.mouse_offset.y()
                self.move(x - x_w, y - y_w)

            if event.type() == QEvent.KeyRelease and self.KeyEventsEnabled:
                # print("got key event")
                key = event.key()
                try:
                    self.Window.LastButtonClicked = chr(key).lower()
                except:
                    self.Window.LastButtonClicked = "special %s" % key
                self.Window.FormRemainedOpen = True
                if self.Window.CurrentlyRunningMainloop:
                    self.Window.QTApplication.exit()
            return QWidget.eventFilter(self, widget, event)


    class QT_QMainWindowClass(QMainWindow):
        def __init__(self,enable_key_events, window):
            self.KeyEventsEnabled = enable_key_events
            self.Window = window
            super().__init__()

        def eventFilter(self, widget, event):
            # print(event.type())
            if event.type() == QEvent.MouseButtonPress and self.Window.GrabAnywhere:
                self.mouse_offset = event.pos()
            if event.type() == QEvent.MouseMove and self.Window.GrabAnywhere:
                x = event.globalX()
                y = event.globalY()
                x_w = self.mouse_offset.x()
                y_w = self.mouse_offset.y()
                self.move(x - x_w, y - y_w)

            if event.type() == QEvent.KeyRelease and self.KeyEventsEnabled:
                # print("got key event")
                key = event.key()
                try:
                    self.Window.LastButtonClicked = chr(key).lower()
                except:
                    self.Window.LastButtonClicked = "special %s" % key
                self.Window.FormRemainedOpen = True
                if self.Window.CurrentlyRunningMainloop:
                    self.Window.QTApplication.exit()
            return QWidget.eventFilter(self, widget, event)

        def closeEvent(self, event):
            if self.Window.DisableClose:
                event.ignore()
                return
            # print('GOT A CLOSE EVENT!', event, self.Window.Title)
            self.Window.LastButtonClicked = None
            self.Window.XFound = True
            if not self.Window.CurrentlyRunningMainloop:  # quit if this is the current mainloop, otherwise don't quit!
                self.Window.RootNeedsDestroying = True
            else:
                self.Window.RootNeedsDestroying = True
                self.Window.QTApplication.exit()  # kick the users out of the mainloop
            self.Window.QT_QMainWindow.close()
            self.Window.TKrootDestroyed = True
            self.Window.RootNeedsDestroying = True

        # if self.CurrentlyRunningMainloop:
        #     print("quitting window")
        #     self.QTApplication.exit()  # kick the users out of the mainloop

    @property
    def Size(self):
        if not self._is_window_created():
            return
        size =  self.QT_QMainWindow.sizeHint()
        return [size.width(), size.height()]

    @Size.setter
    def Size(self, size):
        if not self._is_window_created():
            return
        self.QT_QMainWindow.resize(QSize(size[0], size[1]))


    def _is_window_created(self):
        if self.QT_QMainWindow is None:
            warnings.warn('You cannot perform operations on a Window until it is read or finalized. Adding a "finalize=True" parameter to your Window creation will fix this', UserWarning)
            popup_error('You cannot perform operations on a Window until it is read or finalized.',
                        'Yea, I know, it\'s a weird thing, but easy to fix.... ',
                         'Adding a "finalize=True" parameter to your Window creation will likely fix this', image=FACE_PALM)
            return False
        return True



    def __getitem__(self, key):
        """
        Returns Element that matches the passed in key.
        This is "called" by writing code as thus:
        window['element key'].Update

        :param key: The key to find
        :type key: Union[str, int, tuple, object]
        :return: Union[Element, None] The element found or None if no element was found
        :rtype: Element
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

        :param args: *
        :type args: (any)
        :param kwargs: **
        :type kaargs: (any)
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
    un_hide = UnHide
    visibility_changed = VisibilityChanged

FlexForm = Window



# =========================================================================== #
# Stops the mainloop and sets the event information                           #
# =========================================================================== #

def _element_callback_quit_mainloop(element):
    if element.Key is not None:
        element.ParentForm.LastButtonClicked = element.Key
    else:
        element.ParentForm.LastButtonClicked = ''
    element.ParentForm.FormRemainedOpen = True
    if element.ParentForm.CurrentlyRunningMainloop:
        element.ParentForm.QTApplication.exit()  # kick the users out of the mainloop


# =========================================================================== #
# Convert from characters to pixels                                           #
# =========================================================================== #
def _convert_tkinter_size_to_Qt(size, scaling=DEFAULT_PIXELS_TO_CHARS_SCALING, height_cutoff=DEFAULT_PIXEL_TO_CHARS_CUTOFF):
    """
    Converts size in characters to size in pixels
    :param size:  size in characters, rows
    :return: size in pixels, pixels
    """
    qtsize = size
    if size[1] is not None and size[1] < height_cutoff:        # change from character based size to pixels (roughly)
        qtsize = size[0]*scaling[0], size[1]*scaling[1]
    return qtsize



# =========================================================================== #
# Stops the mainloop and sets the event information                           #
# =========================================================================== #
def convert_tkinter_filetypes_to_qt(filetypes):
    qt_filetypes = ''
    for i, item in enumerate(filetypes):
        filetype = item[0] + ' (' + item[1] + ')' + (';;' if i != len(filetypes)-1 else '')
        qt_filetypes += filetype
    return qt_filetypes

# =========================================================================== #
# Converts a "Font" string or tuple into Qt Style Sheet Entries               #
# =========================================================================== #
def create_style_from_font(font):
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

    style = ''
    style += 'font-family: %s;\n' % _font[0]
    style += 'font-size: %spt;\n' % _font[1]
    font_items = ''
    for item in _font[2:]:
        if item == 'underline':
            style += 'text-decoration: underline;\n'
        else:
            font_items += item + ' '
    if font_items != '':
        style += 'font: %s;\n' % (font_items)
    return style

def set_widget_visiblity(widget, visible):
    if visible is False:
        widget.setVisible(False)
    elif visible is True:
        widget.setVisible(True)


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
                 auto_size_button=None, button_color=None, disabled=False, change_submits=False, enable_events=False, font=None, pad=None,
                 key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FOLDER, target=target,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  disabled=disabled, button_color=button_color, change_submits=change_submits, enable_events=enable_events, font=font, pad=pad,
                  key=key, k=k, metadata=metadata)


# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileBrowse(button_text='Browse', target=(ThisRow, -1), file_types=(("ALL Files", "*"),), initial_folder=None,
               tooltip=None, size=(None, None), auto_size_button=None, button_color=None, change_submits=False, enable_events=False,
               font=None, disabled=False,
               pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  change_submits=change_submits, enable_events=enable_events, disabled=disabled, button_color=button_color, font=font, pad=pad,
                  key=key, k=k, metadata=metadata)


# -------------------------  FILES BROWSE Element (Multiple file selection) lazy function  ------------------------- #
def FilesBrowse(button_text='Browse', target=(ThisRow, -1), file_types=(("ALL Files", "*"),), disabled=False,
                initial_folder=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                change_submits=False, enable_events=False,
                font=None, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FILES, target=target, file_types=file_types,
                  initial_folder=initial_folder, change_submits=change_submits, enable_events=enable_events, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button,
                  disabled=disabled, button_color=button_color, font=font, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileSaveAs(button_text='Save As...', target=(ThisRow, -1), file_types=(("ALL Files", "*"),), initial_folder=None,
               disabled=False, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
               change_submits=False, enable_events=False, font=None,
               pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_SAVEAS_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, change_submits=change_submits, enable_events=enable_events,
                  font=font, pad=pad, key=key, metadata=metadata)


# -------------------------  SAVE AS Element lazy function  ------------------------- #
def SaveAs(button_text='Save As...', target=(ThisRow, -1), file_types=(("ALL Files", "*"),), initial_folder=None,
           disabled=False, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
           change_submits=False, enable_events=False, font=None,
           pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_SAVEAS_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, change_submits=change_submits, enable_events=enable_events,
                  font=font, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  SAVE BUTTON Element lazy function  ------------------------- #
def Save(button_text='Save', size=(None, None), auto_size_button=None, button_color=None, bind_return_key=True,
         disabled=False, tooltip=None, font=None, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  SUBMIT BUTTON Element lazy function  ------------------------- #
def Submit(button_text='Submit', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
           bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  OPEN BUTTON Element lazy function  ------------------------- #
# -------------------------  OPEN BUTTON Element lazy function  ------------------------- #
def Open(button_text='Open', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
         bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  OK BUTTON Element lazy function  ------------------------- #
def OK(button_text='OK', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
       bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Ok(button_text='Ok', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
       bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  CANCEL BUTTON Element lazy function  ------------------------- #
def Cancel(button_text='Cancel', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
           tooltip=None, font=None, bind_return_key=False, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  QUIT BUTTON Element lazy function  ------------------------- #
def Quit(button_text='Quit', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
         font=None, bind_return_key=False, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  Exit BUTTON Element lazy function  ------------------------- #
def Exit(button_text='Exit', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
         font=None, bind_return_key=False, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Yes(button_text='Yes', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
        font=None, bind_return_key=True, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  NO BUTTON Element lazy function  ------------------------- #
def No(button_text='No', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
       font=None, bind_return_key=False, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  NO BUTTON Element lazy function  ------------------------- #
def Help(button_text='Help', size=(None, None), auto_size_button=None, button_color=None, disabled=False, font=None,
         tooltip=None, bind_return_key=False, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
def SimpleButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                 border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                 font=None, bind_return_key=False, disabled=False, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  CLOSE BUTTON Element lazy function  ------------------------- #
def CloseButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
                bind_return_key=False, disabled=False, focus=False, pad=None, key=None, k=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


CButton = CloseButton


# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
def ReadButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
               border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
               bind_return_key=False, disabled=False, focus=False, pad=None, key=None, k=None, metadata=None):
    """
    :param button_text: text in the button
    :type button_text: (str)
    :param image_filename: image filename if there is a button image. GIFs and PNGs only.
    :type image_filename: (str)
    :param image_data: Raw or Base64 representation of the image to put on button. Choose either filename or data
    :type image_data: Union[bytes, str]
    :param image_size: Size of the image in pixels (width, height)
    :type image_size: Tuple[int, int]
    :param image_subsample: amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    :type image_subsample: (int)
    :param border_width: width of border around element
    :type border_width: (int)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button: True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param font: specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key: (Default = False) If True, then the return key will cause a the Listbox to generate an event
    :type bind_return_key: (bool)
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param focus: if focus should be set to this
    :type focus: idk_yetReally
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple, object]
    :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k: Union[str, int, tuple, object]
    :param metadata: Anything you want to store along with this button
    :type metadata: (Any)
    """

    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


ReadFormButton = ReadButton
RButton = ReadFormButton


# -------------------------  Realtime BUTTON Element lazy function  ------------------------- #
def RealtimeButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                   border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                   font=None, disabled=False, bind_return_key=False, focus=False, pad=None, key=None, k=None, metadata=None):
    """
    :param button_text: text in the button
    :type button_text: (str)
    :param image_filename: image filename if there is a button image. GIFs and PNGs only.
    :type image_filename: (str)
    :param image_data: Raw or Base64 representation of the image to put on button. Choose either filename or data
    :type image_data: Union[bytes, str]
    :param image_size: Size of the image in pixels (width, height)
    :type image_size: Tuple[int, int]
    :param image_subsample: amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    :type image_subsample: (int)
    :param border_width:  width of border around element
    :type border_width: (int)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button: True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param bind_return_key: (Default = False) If True, then the return key will cause a the Listbox to generate an event
    :type bind_return_key: (bool)
    :param focus: if focus should be set to this
    :type focus: (bool)
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple, object]
    :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k: Union[str, int, tuple, object]
    :param metadata: Anything you want to store along with this button
    :type metadata: (Any)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_REALTIME, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  Dummy BUTTON Element lazy function  ------------------------- #
def DummyButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
                disabled=False, bind_return_key=False, focus=False, pad=None, key=None, k=None, metadata=None):
    """
    :param button_text: text in the button
    :type button_text: (str)
    :param image_filename: image filename if there is a button image. GIFs and PNGs only.
    :type image_filename: (str)
    :param image_data: Raw or Base64 representation of the image to put on button. Choose either filename or data
    :type image_data: Union[bytes, str]
    :param image_size: Size of the image in pixels (width, height)
    :type image_size: Tuple[int, int]
    :param image_subsample: amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    :type image_subsample: (int)
    :param border_width:  width of border around element
    :type border_width: (int)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button: True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param bind_return_key: (Default = False) If True, then the return key will cause a the Listbox to generate an event
    :type bind_return_key: (bool)
    :param focus: if focus should be set to this
    :type focus: (bool)
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param key: key for uniquely identify this element (for window.FindElement)
    :type key: Union[str, int, tuple, object]
    :param k: Same as the Key. You can use either k or key. Which ever is set will be used.
    :type k: Union[str, int, tuple, object]
    :param metadata: Anything you want to store along with this button
    :type metadata: (Any)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN_ONLY, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  button_color=button_color, font=font, disabled=disabled, bind_return_key=bind_return_key, focus=focus,
                  pad=pad, key=key, k=k, metadata=metadata)


# -------------------------  Calendar Chooser Button lazy function  ------------------------- #
def CalendarButton(button_text, target=(None, None), close_when_date_chosen=True, default_date_m_d_y=(None, None, None),
                   image_filename=None, image_data=None, image_size=(None, None),
                   image_subsample=None, tooltip=None, border_width=None, size=(None, None), auto_size_button=None,
                   button_color=None, disabled=False, font=None, bind_return_key=False, focus=False, pad=None,
                   key=None, k=None, metadata=None):
    button = Button(button_text=button_text, button_type=BUTTON_TYPE_CALENDAR_CHOOSER, target=target,
                    image_filename=image_filename, image_data=image_data, image_size=image_size,
                    image_subsample=image_subsample, border_width=border_width, tooltip=tooltip, size=size,
                    auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                    bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)
    button.CalendarCloseWhenChosen = close_when_date_chosen
    button.DefaultDate_M_D_Y = default_date_m_d_y
    return button


# -------------------------  Calendar Chooser Button lazy function  ------------------------- #
def ColorChooserButton(button_text, target=(None, None), image_filename=None, image_data=None, image_size=(None, None),
                       image_subsample=None, tooltip=None, border_width=None, size=(None, None), auto_size_button=None,
                       button_color=None, disabled=False, font=None, bind_return_key=False, focus=False, pad=None,
                       key=None, k=None, metadata=None):
    """
    :param button_text: text in the button
    :type button_text: (str)
    :param target: key or (row,col) target for the button. Note that -1 for column means 1 element to the left of this one. The constant ThisRow is used to indicate the current row. The Button itself is a valid target for some types of button
    :type target: Union[str, Tuple[int, int]]
    :param image_filename: image filename if there is a button image. GIFs and PNGs only.
    :type image_filename: (str)
    :param image_data: Raw or Base64 representation of the image to put on button. Choose either filename or data
    :type image_data: Union[bytes, str]
    :param image_size: Size of the image in pixels (width, height)
    :type image_size: Tuple[int, int]
    :param image_subsample: amount to reduce the size of the image. Divides the size by this number. 2=1/2, 3=1/3, 4=1/4, etc
    :type image_subsample: (int)
    :param tooltip: text, that will appear when mouse hovers over the element
    :type tooltip: (str)
    :param border_width:  width of border around element
    :type border_width: (int)
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param auto_size_button: True if button size is determined by button text
    :type auto_size_button: (bool)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param disabled: set disable state for element (Default = False)
    :type disabled: (bool)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param bind_return_key: (Default = False) If True, then the return key will cause a the Listbox to generate an event
    :type bind_return_key: (bool)
    :param focus: if focus should be set to this
    :type focus: (bool)
    :param pad: Amount of padding to put around element in pixels (left/right, top/bottom)
    :type pad: (int, int) or ((int, int),(int,int)) or (int,(int,int)) or  ((int, int),int)
    :param metadata: Anything you want to store along with this button
    :type metadata: (Any)
    """
    return Button(button_text=button_text, button_type=BUTTON_TYPE_COLOR_CHOOSER, target=target,
                  image_filename=image_filename, image_data=image_data, image_size=image_size,
                  image_subsample=image_subsample, border_width=border_width, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, k=k, metadata=metadata)


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
                    value = element.QT_QLineEdit.text()
                    if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                        element.QT_QLineEdit.setText('')

                elif element.Type == ELEM_TYPE_INPUT_CHECKBOX:
                    value = element.QT_Checkbox.isChecked()
                elif element.Type == ELEM_TYPE_INPUT_RADIO:
                    this_rowcol = EncodeRadioRowCol(row_num, col_num)
                    value = element.QT_Radio_Button.isChecked()
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
                            value = element.FileOrFolderName
                        except:
                            value = None
                elif element.Type == ELEM_TYPE_INPUT_COMBO:
                    element = element           # type: Combo
                    index = element.QT_ComboBox.currentIndex()  # index into the list of values, but can be larger if manual entry
                    if index < len(element.Values):
                        value = element.Values[index]
                    else:       # if not a valid index, then get what was typed in
                        value = element.QT_ComboBox.currentText()
                elif element.Type == ELEM_TYPE_INPUT_OPTION_MENU:
                    value = 0
                elif element.Type == ELEM_TYPE_INPUT_LISTBOX:
                    element = element            # type: Listbox
                    # print(f'selected indexes = {element.QT_ListWidget.selectedIndexes()}')
                    value = []
                    # value = [element.Values[int(i)] for i in element.QT_ListWidget.selectedIndexes()]
                    # value= [ for i, item in enumerate(element.QT_ListWidget.selectedItems()]
                    selected_items = [item.text() for item in element.QT_ListWidget.selectedItems()]
                    for v in element.Values:
                        if str(v) in selected_items:
                            value.append(v)
                    # try:
                    #     value= [item.index() for item in element.QT_ListWidget.selectedItems()]
                    #     # value= [item.text() for item in element.QT_ListWidget.selectedItems()]
                    # except:
                    #     value = []
                elif element.Type == ELEM_TYPE_INPUT_SPIN:
                    # value = str(element.QT_Spinner.value())
                    # value = str(element.QT_Spinner.textFromValue(element.QT_Spinner.value()))
                    value = element.Values[element.QT_Spinner.value()]
                elif element.Type == ELEM_TYPE_INPUT_DIAL:
                    value = str(element.QT_Dial.value())
                elif element.Type == ELEM_TYPE_INPUT_SLIDER:
                    value = element.QT_Slider.value()
                elif element.Type == ELEM_TYPE_INPUT_MULTILINE:
                    if element.WriteOnly:
                        continue
                    value = element.QT_TextEdit.toPlainText()
                    if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                        element.QT_TextEdit.setText('')
                elif element.Type == ELEM_TYPE_TAB_GROUP:
                    element = element   # type: TabGroup
                    cur_index = element.QT_QTabWidget.currentIndex()
                    tab_element = element.TabList[cur_index]
                    value = tab_element.Key
                elif element.Type == ELEM_TYPE_TABLE:
                    value = []
                    indexes = element.QT_TableWidget.selectionModel().selectedRows()
                    for index in sorted(indexes):
                        value.append(index.row())
                elif element.Type == ELEM_TYPE_TREE:
                    value = []
                    indexes = element.QT_QTreeWidget.selectionModel().selectedRows()
                    for index in sorted(indexes):
                        value.append(index.row())
                elif element.Type == ELEM_TYPE_BUTTONMENU:
                    value = element.MenuItemChosen
                    element.MenuItemChosen = None
                elif element.Type == ELEM_TYPE_MENUBAR:
                    if element.MenuItemChosen is not None:
                        top_level_form.LastButtonClicked = element.MenuItemChosen
                    button_pressed_text = top_level_form.LastButtonClicked
                    value = element.MenuItemChosen
                    element.MenuItemChosen = None
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
            try:
                if element.Widget.hasFocus():
                    return element
            except:
                continue
            # if element.Type == ELEM_TYPE_INPUT_TEXT:
            #     if element.QT_QLineEdit is not None:
            #         if element.QT_QLineEdit is element.TKEntry.focus_get():
            #             return element


def AddTrayMenuItem(top_menu, sub_menu_info, element, is_sub_menu=False, skip=False):
    if type(sub_menu_info) is str:
        if not is_sub_menu and not skip:
            # print(f'Adding command {sub_menu_info}')
            action = QAction(top_menu)
            if sub_menu_info == '---':
                action.setSeparator(True)
            else:
                try:
                    item_without_key = sub_menu_info[:sub_menu_info.index(MENU_KEY_SEPARATOR)]
                except:
                    item_without_key = sub_menu_info
                if item_without_key[0] == MENU_DISABLED_CHARACTER:
                    action.setText(item_without_key[len(MENU_DISABLED_CHARACTER):])
                    action.setDisabled(True)
                else:
                    action.setText(item_without_key)
                action.triggered.connect(lambda: SystemTray._QT_MenuItemChosenCallback(element, sub_menu_info))
            top_menu.addAction(action)
    else:
        i = 0
        while i < (len(sub_menu_info)):
            item = sub_menu_info[i]
            if i != len(sub_menu_info) - 1:
                if type(sub_menu_info[i + 1]) == list:
                    new_menu = QMenu(top_menu)
                    item = sub_menu_info[i]
                    try:
                        item_without_key = item[:item.index(MENU_KEY_SEPARATOR)]
                    except:
                        item_without_key = item
                    if item_without_key[0] == MENU_DISABLED_CHARACTER:
                        new_menu.setTitle(item_without_key[len(MENU_DISABLED_CHARACTER):])
                        new_menu.setDisabled(True)
                    else:
                        new_menu.setTitle(item_without_key)
                    top_menu.addAction(new_menu.menuAction())
                    # print(f'Adding submenu {sub_menu_info[i]}')
                    AddTrayMenuItem(new_menu, sub_menu_info[i + 1], element, is_sub_menu=True)
                    i += 1  # skip the next one
                else:
                    AddTrayMenuItem(top_menu, item, element)
            else:
                AddTrayMenuItem(top_menu, item, element)
            i += 1


def AddMenuItem(top_menu, sub_menu_info, element, is_sub_menu=False, skip=False):
    if type(sub_menu_info) is str:
        if not is_sub_menu and not skip:
            # print(f'Adding command {sub_menu_info}')
            action = QAction(top_menu)

            if sub_menu_info == '---':
                action.setSeparator(True)
            else:

                # Key handling.... strip off key before setting text
                try:
                    item_without_key = sub_menu_info[:sub_menu_info.index(MENU_KEY_SEPARATOR)]
                except:
                    item_without_key = sub_menu_info
                if item_without_key[0] == MENU_DISABLED_CHARACTER:
                    action.setText(item_without_key[len(MENU_DISABLED_CHARACTER):])
                    action.setDisabled(True)
                else:
                    action.setText(item_without_key)
                action.triggered.connect(lambda: Menu._QT_MenuItemChosenCallback(element, sub_menu_info))
            top_menu.addAction(action)
    else:
        i = 0
        while i < (len(sub_menu_info)):
            item = sub_menu_info[i]
            if i != len(sub_menu_info) - 1:
                if type(sub_menu_info[i + 1]) == list:
                    new_menu = QMenu(top_menu)
                    # Key handling.... strip off key before setting text
                    item = sub_menu_info[i]
                    try:
                        item_without_key = item[:item.index(MENU_KEY_SEPARATOR)]
                    except:
                        item_without_key = item
                    if item_without_key[0] == MENU_DISABLED_CHARACTER:
                        new_menu.setTitle(item_without_key[len(MENU_DISABLED_CHARACTER):])
                        new_menu.setDisabled(True)
                    else:
                        new_menu.setTitle(item_without_key)
                    top_menu.addAction(new_menu.menuAction())
                    # print(f'Adding submenu {sub_menu_info[i]}')
                    AddMenuItem(new_menu, sub_menu_info[i + 1], element, is_sub_menu=True)
                    i += 1  # skip the next one
                else:
                    AddMenuItem(top_menu, item, element)
            else:
                AddMenuItem(top_menu, item, element)
            i += 1


"""
     QQQQQQQQQ              tttt          
   QQ:::::::::QQ         ttt:::t          
 QQ:::::::::::::QQ       t:::::t          
Q:::::::QQQ:::::::Q      t:::::t          
Q::::::O   Q::::::Qttttttt:::::ttttttt    
Q:::::O     Q:::::Qt:::::::::::::::::t    
Q:::::O     Q:::::Qt:::::::::::::::::t    
Q:::::O     Q:::::Qtttttt:::::::tttttt    
Q:::::O     Q:::::Q      t:::::t          
Q:::::O     Q:::::Q      t:::::t          
Q:::::O  QQQQ:::::Q      t:::::t          
Q::::::O Q::::::::Q      t:::::t    tttttt
Q:::::::QQ::::::::Q      t::::::tttt:::::t
 QQ::::::::::::::Q       tt::::::::::::::t
   QQ:::::::::::Q          tt:::::::::::tt
     QQQQQQQQ::::QQ          ttttttttttt  
             Q:::::Q                      
              QQQQQQ                      
"""

# My crappy Qt code starts here

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
# =====================================   Qt CODE STARTS HERE ====================================================== #
# ------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #
def style_entry(**kwargs):
    generated_style = ''
    for Qt_property, value in kwargs.items():
        generated_style += "\t{} : {};\n".format(Qt_property.replace('_','-'), value)

        # generated_style += "}"
    return generated_style

def style_generate(qt_element_type, entries):
    generated_style = qt_element_type + " {\n"
    generated_style += entries
    generated_style += "}"
    return generated_style


class Style(object):
    def __init__(self, id, **kwargs):
        self.content = id + " {\n}"
        self.add(**kwargs)

    def add(self, **kwargs):
        self.content = self.content[:-1]
        for key, value in kwargs.items():
            if isinstance(value, (tuple, list)):
                value, isnot = value
            else:
                isnot = None
            if value is not None and value != isnot:
                self.content += "\t{} : {};\n".format(key.replace("_", "-"), value)
        self.content += "}"

    def append(self, value):
        self.content = self.content[:-1] + value + "\n}"

    def __repr__(self):
        return self.content


def PackFormIntoFrame(container_elem, containing_frame, toplevel_win):
    """
    :param form: a window class
    :type form: (Window)
    :param containing_frame: ???
    :type containing_frame: ???
    :param toplevel_form: ???
    :type toplevel_form: (Window)
    """

    border_depth = toplevel_win.BorderDepth if toplevel_win.BorderDepth is not None else DEFAULT_BORDER_WIDTH
    # --------------------------------------------------------------------------- #
    # ****************  Use FlexForm to build the tkinter window ********** ----- #
    # Building is done row by row.                                                #
    # --------------------------------------------------------------------------- #
    focus_set = False
    ######################### LOOP THROUGH ROWS #########################
    # *********** -------  Loop through ROWS  ------- ***********#
    for row_num, flex_row in enumerate(container_elem.Rows):
        ######################### LOOP THROUGH ELEMENTS ON ROW #########################
        # *********** -------  Loop through ELEMENTS  ------- ***********#
        # *********** Make TK Row                             ***********#
        qt_row_layout = QHBoxLayout()
        if container_elem.ElementJustification.startswith('c'):
            qt_row_layout.setAlignment(Qt.AlignCenter)
        elif container_elem.ElementJustification.startswith('r'):
            qt_row_layout.setAlignment(Qt.AlignRight)
        elif container_elem.ElementJustification.startswith('l'):
            qt_row_layout.setAlignment(Qt.AlignLeft)
        for col_num, element in enumerate(flex_row):
            element.ParentForm = toplevel_win  # save the button's parent form object
            element.row_frame = qt_row_layout
            if toplevel_win.Font and (element.Font == DEFAULT_FONT or not element.Font):
                font = toplevel_win.Font
                element.Font = font
            elif element.Font is not None:
                font = element.Font
            else:
                font = DEFAULT_FONT
            # -------  Determine Auto-Size setting on a cascading basis ------- #
            if element.AutoSizeText is not None:  # if element overide
                auto_size_text = element.AutoSizeText
            elif toplevel_win.AutoSizeText is not None:  # if form override
                auto_size_text = toplevel_win.AutoSizeText
            else:
                auto_size_text = DEFAULT_AUTOSIZE_TEXT
            element_type = element.Type
            # Set foreground color
            text_color = element.TextColor
            # Determine Element size
            element_size = element.Size
            if (element_size == (None, None) and element_type not in (ELEM_TYPE_BUTTON, ELEM_TYPE_BUTTONMENU)):  # user did not specify a size
                element_size = toplevel_win.DefaultElementSize
            elif (element_size == (None, None) and element_type in (ELEM_TYPE_BUTTON, ELEM_TYPE_BUTTONMENU)):
                element_size = toplevel_win.DefaultButtonElementSize
            else:
                auto_size_text = False  # if user has specified a size then it shouldn't autosize
            full_element_pad = [0,0,0,0]       # Top, Right, Bottom, Left
            elementpad = element.Pad if element.Pad is not None else toplevel_win.ElementPadding
            if type(elementpad[0]) != tuple:   # left and right
                full_element_pad[1] = full_element_pad[3] = elementpad[0]
            else:
                full_element_pad[3], full_element_pad[1] = elementpad[0]
            if type(elementpad[1]) != tuple:   # top and bottom
                full_element_pad[0] = full_element_pad[2] = elementpad[1]
            else:
                full_element_pad[0], full_element_pad[2] = elementpad[1]

            border_depth = toplevel_win.BorderDepth if toplevel_win.BorderDepth is not None else DEFAULT_BORDER_WIDTH
            try:
                if element.BorderWidth is not None:
                    border_depth = element.BorderWidth
            except:
                pass

            # -------------------------  COLUMN placement element  ------------------------- #
            if element_type == ELEM_TYPE_COLUMN:
                element = element           # type: Column
                # column_widget = QWidget()
                column_widget = QGroupBox()
                element.Widget = element.QT_QGroupBox = column_widget
                # column_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
                style = create_style_from_font(font)
                if element.BackgroundColor is not None:
                    style = style_entry(background_color=element.BackgroundColor)
                    # style += 'background-color: %s;' % element.BackgroundColor
                style += style_entry(border='0px solid gray')
                # style += style_entry(margin='{}px {}px {}px {}px'.format(*full_element_pad))
                # style += style_entry(margin='0px 0px 0px 0px')
                # style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)

                # style += 'border: 0px solid gray; '
                style = style_generate('QGroupBox', style)
                column_widget.setStyleSheet(style)

                column_layout = QFormLayout()
                element.vbox_layout = column_vbox = QVBoxLayout()
                PackFormIntoFrame(element, column_layout, toplevel_win)

                scroll = None
                if element.Scrollable and (element_size[0] is not None or element_size[1] is not None):
                    scroll = QtWidgets.QScrollArea()
                    scroll.setWidget(column_widget)
                    if element_size[0] is not None:
                        scroll.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        scroll.setFixedHeight(element_size[1])
                    scroll.setWidgetResizable(True)

                column_vbox.addLayout(column_layout)
                column_widget.setLayout(column_vbox)

                # column_widget.setStyleSheet(style)
                if not element.Visible:
                    column_widget.setVisible(False)

                if scroll:
                    qt_row_layout.addWidget(scroll)
                else:
                    qt_row_layout.addWidget(column_widget)
            # -------------------------  TEXT placement element  ------------------------- #
            elif element_type == ELEM_TYPE_TEXT:
                element.Widget = element.QT_Label = qlabel = QLabel(element.DisplayText, toplevel_win.QTWindow)
                if element.Justification is not None:
                    justification = element.Justification
                elif toplevel_win.TextJustification is not None:
                    justification = toplevel_win.TextJustification
                else:
                    justification = DEFAULT_TEXT_JUSTIFICATION
                if justification[0] == 'c':
                    element.QT_Label.setAlignment(Qt.AlignCenter)
                elif justification[0] == 'r':
                    element.QT_Label.setAlignment(Qt.AlignRight)
                if not auto_size_text:
                    if element_size[0] is not None:
                        element.QT_Label.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_Label.setFixedHeight(element_size[1])
                # element.QT_Label.setWordWrap(True)
                style = Style('QLabel')
                style.append(create_style_from_font(font))
                style.add(color=(element.TextColor, COLOR_SYSTEM_DEFAULT))
                style.add(background_color=(element.BackgroundColor, COLOR_SYSTEM_DEFAULT))
                element.QT_Label.setStyleSheet(style.content)

                if element.ClickSubmits:
                    element.QT_Label.mousePressEvent = element._QtCallbackTextClicked

                if element.Relief is not None:
                    if element.Relief in (RELIEF_RIDGE, RELIEF_RAISED):
                        qlabel.setFrameStyle(QFrame.Panel | QFrame.Raised)
                    elif element.Relief in (RELIEF_SUNKEN, RELIEF_GROOVE):
                        qlabel.setFrameStyle(QFrame.Panel | QFrame.Sunken)
                    elif element.Relief == RELIEF_FLAT:
                        qlabel.setFrameStyle(QFrame.Panel | QFrame.NoFrame)

                if element.Margins is not None:
                    m = element.Margins
                    qlabel.setContentsMargins(m[0], m[2], m[1], m[3])  # L T B R
                if element.Tooltip:
                    element.QT_Label.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_Label.setVisible(False)
                qt_row_layout.addWidget(element.QT_Label)
            # -------------------------  BUTTON placement element  ------------------------- #
            elif element_type == ELEM_TYPE_BUTTON:
                element = element            #type: Button
                btext = element.ButtonText
                btype = element.BType
                element.Widget = element.QT_QPushButton = QPushButton(btext)
                style = Style('QPushButton')
                style.append(create_style_from_font(font))
                style.add(color=(element.TextColor, COLOR_SYSTEM_DEFAULT))
                style.add(background_color=(element.BackgroundColor))
                if element.BorderWidth == 0:
                    style.add(border='none')
                style.add(margin='{}px {}px {}px {}px'.format(*full_element_pad))
                # style.add(border='{}px solid gray '.format(border_depth))
                element.QT_QPushButton.setStyleSheet(style.content)
                # element.QT_QPushButton.setFlat(False)
                if (element.AutoSizeButton is False or toplevel_win.AutoSizeButtons is False or element.Size[0] is not None) and element.ImageData is None:
                    if element_size[0] is not None:
                        element.QT_QPushButton.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_QPushButton.setFixedHeight(element_size[1])

                #
                # elif element.Data is not None:
                #     qlabel.setText('')
                #     ba = QtCore.QByteArray.fromRawData(element.Data)
                #     pixmap = QtGui.QPixmap()
                #     pixmap.loadFromData(ba)
                #     qlabel.setPixmap(pixmap)
                # elif element.DataBase64:
                #     qlabel.setText('')
                #     ba = QtCore.QByteArray.fromBase64(element.DataBase64)
                #     pixmap = QtGui.QPixmap()
                #     pixmap.loadFromData(ba)
                #     qlabel.setPixmap(pixmap)

                if element.ImageFilename is not None:
                    element.QT_QPushButton.setIcon(QtGui.QPixmap(element.ImageFilename))
                    element.QT_QPushButton.setIconSize(QtGui.QPixmap(element.ImageFilename).rect().size())
                if element.ImageData:
                    ba = QtCore.QByteArray.fromBase64(element.ImageData)
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(ba)
                    element.QT_QPushButton.setIcon(pixmap)
                    element.QT_QPushButton.setIconSize(pixmap.rect().size())

                if element.Disabled:
                    element.QT_QPushButton.setDisabled(True)

                if element.Tooltip:
                    element.QT_QPushButton.setToolTip(element.Tooltip)
                element.QT_QPushButton.clicked.connect(element._ButtonCallBack)
                if not element.Visible:
                    element.QT_QPushButton.setVisible(False)

                qt_row_layout.addWidget(element.QT_QPushButton)
            # -------------------------  INPUT placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_TEXT:
                element = element       # type: InputText
                default_text = element.DefaultText
                element.Widget = element.QT_QLineEdit = qlineedit = QLineEdit()

                qlineedit.setAcceptDrops(True)
                qlineedit.dragEnterEvent = element._dragEnterEvent
                qlineedit.dropEvent = element._dropEvent

                if element.Justification[0] == 'c':
                    element.QT_QLineEdit.setAlignment(Qt.AlignCenter)
                elif element.Justification[0] == 'r':
                    element.QT_QLineEdit.setAlignment(Qt.AlignRight)
                element.QT_QLineEdit.setText(str(default_text))

                style = Style('QLineEdit')
                style.append(create_style_from_font(font))
                if element.Disabled or element.ReadOnly:
                    if element.disabled_readonly_background_color:
                        style.add(background_color=(element.disabled_readonly_background_color, COLOR_SYSTEM_DEFAULT))
                    else:
                        style.add(background_color=(element.BackgroundColor, COLOR_SYSTEM_DEFAULT))
                    if element.disabled_readonly_text_color:
                        style.add(color=(element.disabled_readonly_text_color, COLOR_SYSTEM_DEFAULT))
                    else:
                        style.add(color=(element.TextColor, COLOR_SYSTEM_DEFAULT))
                else:
                    style.add(background_color=(element.BackgroundColor, COLOR_SYSTEM_DEFAULT))
                    style.add(color=(element.TextColor, COLOR_SYSTEM_DEFAULT))
                style.add(margin='{}px {}px {}px {}px'.format(*full_element_pad))
                style.add(border='{}px solid gray '.format(border_depth))
                element.QT_QLineEdit.setStyleSheet(style.content)

                if element.AutoSizeText is False or toplevel_win.AutoSizeText is False or element.Size[0] is not None:
                    if element_size[0] is not None:
                        element.QT_QLineEdit.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_QLineEdit.setFixedHeight(element_size[1])

                if (element.Focus or toplevel_win.UseDefaultFocus) and not focus_set:
                    focus_set = True
                    toplevel_win.FocusElement = element.QT_QLineEdit

                if element.Disabled:
                    element.QT_QLineEdit.setDisabled(True)

                if element.ReadOnly:
                    element.QT_QLineEdit.setReadOnly(True)

                if element.ChangeSubmits:
                    element.QT_QLineEdit.textChanged.connect(element._QtCallbackFocusInEvent)

                element.QT_QLineEdit.returnPressed.connect(element._QtCallbackReturnPressed)

                if element.PasswordCharacter != '':
                    qlineedit.setEchoMode(QLineEdit.Password)
                if element.Tooltip:
                    element.QT_QLineEdit.setToolTip(element.Tooltip)

                element.InputTextWidget = Input.InputTextWidget(element.QT_QLineEdit, element)
                element.QT_QLineEdit.installEventFilter(element.InputTextWidget)
                if not element.Visible:
                    element.QT_QLineEdit.setVisible(False)
                qt_row_layout.addWidget(element.QT_QLineEdit)
            # -------------------------  COMBO placement BOX (Drop Down) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_COMBO:
                element.Widget = element.QT_ComboBox = QComboBox()
                max_line_len = max([len(str(l)) for l in element.Values])
                if auto_size_text is False:
                    width = element_size[0]
                else:
                    width = max_line_len

                style = Style('QComboBox')
                style.append(create_style_from_font(font))
                style.add(color=(element.TextColor, COLOR_SYSTEM_DEFAULT))
                style.add(background_color=(element.BackgroundColor, COLOR_SYSTEM_DEFAULT))
                style.add(border='{}px solid gray '.format(border_depth))
                style2 = Style('QListView')
                style2.add(color=(element.TextColor, COLOR_SYSTEM_DEFAULT))
                style2.add(background_color=(element.BackgroundColor, COLOR_SYSTEM_DEFAULT))

                element.QT_ComboBox.setStyleSheet(style.content+style2.content)

                if not auto_size_text:
                    if element_size[0] is not None:
                        element.QT_ComboBox.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_ComboBox.setFixedHeight(element_size[1])

                if element.Disabled:
                    element.QT_ComboBox.setDisabled(True)
                items_as_strings = [str(v) for v in element.Values]
                # element.QT_ComboBox.addItems(element.Values)
                element.QT_ComboBox.addItems(items_as_strings)

                element.QT_ComboBox.setMaxVisibleItems(element.VisibleItems)
                if element.DefaultValue is not None:
                    for index, v in enumerate(element.Values):
                        if v == element.DefaultValue:
                            element.QT_ComboBox.setCurrentIndex(index)
                            break

                if element.ChangeSubmits:
                    element.QT_ComboBox.currentIndexChanged.connect(element._QtCurrentItemChanged)
                if element.Tooltip:
                    element.QT_ComboBox.setToolTip(element.Tooltip)
                if not element.Readonly:
                    element.QT_ComboBox.setEditable(True)
                if not element.AutoComplete:
                    element.QT_ComboBox.setAutoCompletion(True)
                if not element.Visible:
                    element.QT_ComboBox.setVisible(False)
                qt_row_layout.addWidget(element.QT_ComboBox)
            # -------------------------  OPTION MENU (Like ComboBox but different) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_OPTION_MENU:
                max_line_len = max([len(str(l)) for l in element.Values])
            # -------------------------  LISTBOX placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_LISTBOX:
                element = element       # type: Listbox
                max_line_len = max([len(str(l)) for l in element.Values]) if len(element.Values) != 0 else 0
                element.Widget = element.QT_ListWidget = QListWidget()
                style = element.QT_ListWidget.styleSheet()
                # style += """QScrollBar:vertical {
                #             border: none;
                #             background:lightgray;
                #             width:12px;
                #             margin: 0px 0px 0px 0px;
                #         } """
                style = 'QListWidget {'
                style += create_style_from_font(font)

                if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                style += '}'
                element.QT_ListWidget.setStyleSheet(style)
                if not auto_size_text:
                    if element_size[0] is not None:
                        element.QT_ListWidget.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_ListWidget.setFixedHeight(element_size[1])

                if element.SelectMode == SELECT_MODE_MULTIPLE:
                    element.QT_ListWidget.setSelectionMode(QAbstractItemView.MultiSelection)
                elif element.SelectMode == SELECT_MODE_EXTENDED:
                    element.QT_ListWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
                elif element.SelectMode == SELECT_MODE_CONTIGUOUS:
                    element.QT_ListWidget.setSelectionMode(QAbstractItemView.ContiguousSelection)
                elif element.SelectMode == SELECT_MODE_SINGLE:
                    element.QT_ListWidget.setSelectionMode(QAbstractItemView.SingleSelection)

                if element.Disabled:
                    element.QT_ListWidget.setDisabled(True)

                if element.ChangeSubmits:
                    element.QT_ListWidget.currentRowChanged.connect(element._QtCurrentRowChanged)
                # add all Values to the ListWidget
                items = [str(v) for v in element.Values]
                element.QT_ListWidget.addItems(items)
                # select the default items
                for index, value in enumerate(element.Values):
                    item = element.QT_ListWidget.item(index)
                    if element.DefaultValues is not None and value in element.DefaultValues:
                        element.QT_ListWidget.setItemSelected(item, True)

                if element.Tooltip:
                    element.QT_ListWidget.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_ListWidget.setVisible(False)
                qt_row_layout.addWidget(element.QT_ListWidget)
            # -------------------------  INPUT MULTILINE placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_MULTILINE:
                element = element           # type: Multiline
                default_text = element.DefaultText
                width, height = element_size
                element.Widget = element.QT_TextEdit = QTextEdit()

                element.QT_TextEdit.setAcceptDrops(True)
                element.QT_TextEdit.dragEnterEvent = element._dragEnterEvent
                element.QT_TextEdit.dropEvent = element._dropEvent

                style = 'QTextEdit {'
                style += create_style_from_font(font)

                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                style += '}'
                element.QT_TextEdit.setStyleSheet(style)

                if element.AutoSizeText is False or element.Size[0] is not None:
                    if element_size[0] is not None:
                        element.QT_TextEdit.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_TextEdit.setFixedHeight(element_size[1])

                if element.Disabled:
                    element.QT_TextEdit.setDisabled(True)

                element.MultiQWidget = Multiline.MultiQWidget(element.QT_TextEdit, element)
                element.QT_TextEdit.installEventFilter(element.MultiQWidget)

                if element.ChangeSubmits:
                    element.QT_TextEdit.textChanged.connect(element._QtCallbackFocusInEvent)

                if (element.Focus or toplevel_win.UseDefaultFocus) and not focus_set:
                    focus_set = True
                    toplevel_win.FocusElement = element.QT_TextEdit

                element.QT_TextEdit.setText(str(default_text))
                element.QT_TextEdit.moveCursor(QtGui.QTextCursor.End)
                if element.Tooltip:
                    element.QT_TextEdit.setToolTip(element.Tooltip)
                # qt_row_layout.setContentsMargins(*full_element_pad)
                if not element.Visible:
                    element.QT_TextEdit.setVisible(False)
                qt_row_layout.addWidget(element.QT_TextEdit)
            # ------------------------- OUTPUT MULTILINE placement element  ------------------------- #
            elif element_type == ELEM_TYPE_MULTILINE_OUTPUT:
                element = element           # type: MultilineOutput
                default_text = element.DefaultText
                width, height = element_size
                element.Widget = element.QT_TextBrowser = QTextBrowser()
                element.QT_TextBrowser.setDisabled(False)
                style = 'QTextBrowser {'
                style += create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                style += '}'
                element.QT_TextBrowser.setStyleSheet(style)

                if element.AutoSizeText is False or element.Size[0] is not None:
                    if element_size[0] is not None:
                        element.QT_TextBrowser.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_TextBrowser.setFixedHeight(element_size[1])

                element.QT_TextBrowser.insertPlainText(default_text)
                element.QT_TextBrowser.moveCursor(QtGui.QTextCursor.End)
                if element.Tooltip:
                    element.QT_TextBrowser.setToolTip(element.Tooltip)
                # qt_row_layout.setContentsMargins(*full_element_pad)
                if not element.Visible:
                    element.QT_TextBrowser.setVisible(False)
                qt_row_layout.addWidget(element.QT_TextBrowser)
            # -------------------------  INPUT CHECKBOX placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_CHECKBOX:
                element = element           # type: Checkbox
                element.QT_Checkbox = QCheckBox(element.Text)
                element.QT_Checkbox.setChecked(element.InitialState)
                if element.Disabled:
                    element.QT_Checkbox.setDisabled(True)
                style = create_style_from_font(font)

                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                element.QT_Checkbox.setStyleSheet(style)

                if element.AutoSizeText is False or element.Size[0] is not None:
                    if element_size[0] is not None:
                        element.QT_Checkbox.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_Checkbox.setFixedHeight(element_size[1])
                if element.ChangeSubmits:
                    element.QT_Checkbox.stateChanged.connect(element.QtCallbackStateChanged)
                # qt_row_layout.setContentsMargins(*full_element_pad)
                if element.Tooltip:
                    element.QT_Checkbox.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_Checkbox.setVisible(False)
                qt_row_layout.addWidget(element.QT_Checkbox)
              # -------------------------  PROGRESSBAR placement element  ------------------------- #
            elif element_type == ELEM_TYPE_PROGRESS_BAR:
                element.Widget = element.QT_QProgressBar = QProgressBar()
                orientation = element.Orientation.lower()[0]
                if element.Size[0] is not None:
                    if element_size[0] is not None:
                        element.QT_QProgressBar.setFixedWidth(element_size[orientation != 'h'])
                    if element_size[1] is not None:
                        element.QT_QProgressBar.setFixedHeight(element_size[orientation == 'h'])

                element.QT_QProgressBar.setMaximum(element.MaxValue)
                element.QT_QProgressBar.setValue(element.StartValue)
                if element.Orientation.lower().startswith('v'):
                    element.QT_QProgressBar.setOrientation(QtCore.Qt.Vertical)
                style = ''
                # style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                # style += 'border: {}px solid gray; '.format(border_depth)
                if element.BarColor != (None, None):
                    if element.BarColor[0] is not None:
                        style += "QProgressBar::chunk { background-color: %s; }"%element.BarColor[0]
                    if element.BarColor[1] is not None:
                        style += "QProgressBar { border: %spx solid grey; border-radius: 0px; background-color: %s; }"%(border_depth, element.BarColor[1])
                    else:
                        style += "QProgressBar { border: %spx solid grey; border-radius: 0px; background-color: %s}"%(border_depth, DEFAULT_PROGRESS_BAR_COLOR[1])

                element.QT_QProgressBar.setStyleSheet(style)

                element.QT_QProgressBar.setTextVisible(False)
                if element.Tooltip:
                    element.QT_QProgressBar.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_QProgressBar.setVisible(False)

                qt_row_layout.addWidget(element.QT_QProgressBar)
            # -------------------------  INPUT RADIO placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_RADIO:
                element = element           # type: Radio
                default_value = element.InitialState
                element.Widget = qradio = QRadioButton(element.Text)
                element.QT_Radio_Button = qradio
                if element.Disabled:
                    element.QT_Radio_Button.setDisabled(True)
                if default_value:
                    qradio.setChecked(True)
                style = create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                element.QT_Radio_Button.setStyleSheet(style)

                if element.AutoSizeText is False or element.Size[0] is not None:
                    if element_size[0] is not None:
                        element.QT_Radio_Button.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_Radio_Button.setFixedHeight(element_size[1])

                if element.GroupID in toplevel_win.RadioDict:
                    element.QT_RadioButtonGroup = toplevel_win.RadioDict[element.GroupID]
                else:
                    element.QT_RadioButtonGroup = QButtonGroup(toplevel_win.QTApplication)
                    toplevel_win.RadioDict[element.GroupID] = element.QT_RadioButtonGroup
                    element.QT_RadioButtonGroup.setExclusive(True)

                element.QT_RadioButtonGroup.addButton(element.QT_Radio_Button)

                if element.ChangeSubmits:
                    element.QT_Radio_Button.toggled.connect(element._QtCallbackValueChanged)

                # qt_row_layout.setContentsMargins(*full_element_pad)
                if element.Tooltip:
                    element.QT_Radio_Button.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_Radio_Button.setVisible(False)
                qt_row_layout.addWidget(element.QT_Radio_Button)
                # -------------------------  INPUT SPIN placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SPIN:
                # element.QT_Spinner = QSpinBox()
                element = element               # type: Spin
                element.Widget = element.QT_Spinner = Spin.StringBox(element.Values)
                if element.DefaultValue is not None:         # try to set the default value without crashing on error
                    try:
                        element.QT_Spinner.setValue(element.QT_Spinner.valueFromText(element.DefaultValue))
                    except:
                        pass
                style = 'QSpinBox {'
                style += create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                style += '}'
                element.QT_Spinner.setStyleSheet(style)
                # element.QT_Spinner.setRange(element.Values[0], element.Values[1])
                if not auto_size_text:
                    if element_size[0] is not None:
                        element.QT_Spinner.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_Spinner.setFixedHeight(element_size[1])

                if element.Disabled:
                    element.QT_Spinner.setDisabled(True)
                if element.ChangeSubmits:
                    element.QT_Spinner.valueChanged.connect(element._QtCallbackValueChanged)
                if element.Tooltip:
                    element.QT_Spinner.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_Spinner.setVisible(False)
                qt_row_layout.addWidget(element.QT_Spinner)
            # -------------------------  OUTPUT placement element  ------------------------- #
            elif element_type == ELEM_TYPE_OUTPUT:
                element = element       # type: Output
                element.Widget = element.QT_TextBrowser = QTextBrowser()
                element.QT_TextBrowser.setDisabled(False)
                style = 'QTextBrowser {'
                style += create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                # style += """QScrollBar:vertical {
                #             border: none;
                #             background:lightgray;
                #             width:12px;
                #             margin: 0px 0px 0px 0px;
                #         } """
                style += '}'
                element.QT_TextBrowser.setStyleSheet(style)

                if element.AutoSizeText is False or element.Size[0] is not None:
                    if element_size[0] is not None:
                        element.QT_TextBrowser.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_TextBrowser.setFixedHeight(element_size[1])

                element.QT_TextBrowser.moveCursor(QtGui.QTextCursor.End)
                element._reroute_stdout()
                if element.Tooltip:
                    element.QT_TextBrowser.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_TextBrowser.setVisible(False)
                qt_row_layout.addWidget(element.QT_TextBrowser)
            # -------------------------  IMAGE placement element  ------------------------- #
            elif element_type == ELEM_TYPE_IMAGE:
                element = element           # type: Image
                element.Widget = element.QT_QLabel = qlabel = QLabel()
                if element.Filename is not None:
                    qlabel.setText('')
                    w = QtGui.QPixmap(element.Filename).width()
                    h = QtGui.QPixmap(element.Filename).height()
                    qlabel.setGeometry(QtCore.QRect(0, 0, w, h))
                    qlabel.setPixmap(QtGui.QPixmap(element.Filename))
                elif element.Data is not None:
                    qlabel.setText('')
                    ba = QtCore.QByteArray.fromRawData(element.Data)
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(ba)
                    qlabel.setPixmap(pixmap)
                elif element.DataBase64:
                    qlabel.setText('')
                    ba = QtCore.QByteArray.fromBase64(element.DataBase64)
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(ba)
                    qlabel.setPixmap(pixmap)

                style = ''
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                element.QT_QLabel.setStyleSheet(style)
                if element.Tooltip:
                    element.QT_QLabel.setToolTip(element.Tooltip)

                if element.ClickSubmits:
                    element.QT_QLabel.mousePressEvent = element.QtCallbackImageClicked
                if not element.Visible:
                    element.QT_QLabel.setVisible(False)
                qt_row_layout.addWidget(element.QT_QLabel)
            # -------------------------  Canvas placement element  ------------------------- #
            elif element_type == ELEM_TYPE_CANVAS:
                width, height = element_size
            # -------------------------  Graph placement element  ------------------------- #
            elif element_type == ELEM_TYPE_GRAPH:
                element = element               # type: Graph
                width, height = element_size
                # print(f'Graph element size = {element_size}')
                element.Widget = element.QT_QGraphicsView = qgraphicsview = QGraphicsView()
                # element.QT_QGraphicsView.setGeometry(0,0,element.CanvasSize[0],element.CanvasSize[1])
                # print(f'Graph Canvas size = {element.CanvasSize}')

                element.QT_QGraphicsScene = QGraphicsScene()
                element.QT_QGraphicsScene.setSceneRect(0,0,element.CanvasSize[0],element.CanvasSize[1])
                element.QT_QGraphicsView.setScene(element.QT_QGraphicsScene)

                style = Style('QGraphicsView')
                style.add(background_color=(element.BackgroundColor, COLOR_SYSTEM_DEFAULT))
                style.add(margin='{}px {}px {}px {}px'.format(*full_element_pad))
                style.add(border='{}px solid gray '.format(border_depth))
                # print(f'style content = {style.content}')
                element.QT_QGraphicsView.setStyleSheet(style.content)

                qgraphicsview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                qgraphicsview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                # qt_row_layout.setContentsMargins(*full_element_pad)
                if element.Tooltip:
                    element.QT_QGraphicsView.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_QGraphicsView.setVisible(False)
                qt_row_layout.addWidget(element.QT_QGraphicsView)
            # -------------------------  MENUBAR placement element  ------------------------- #
            elif element_type == ELEM_TYPE_MENUBAR:
                element = element           # type: Menu
                menu_def = element.MenuDefinition
                element.Widget = element.QT_QMenuBar = QMenuBar(toplevel_win.QT_QMainWindow)

                for menu_entry in menu_def:
                    # print(f'Adding a Menubar ENTRY {menu_entry}')
                    baritem = QMenu(element.QT_QMenuBar)
                    if menu_entry[0][0] == MENU_DISABLED_CHARACTER:
                        baritem.setDisabled(True)
                        baritem.setTitle(menu_entry[0][1:])
                    else:
                        baritem.setTitle(menu_entry[0])
                    element.QT_QMenuBar.addAction(baritem.menuAction())
                    AddMenuItem(baritem, menu_entry[1], element)
                if element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    style = Style('QMenuBar')
                    style.add(background_color=(element.BackgroundColor))
                    element.QT_QMenuBar.setStyleSheet(style.content)
                if not element.Visible:
                    element.QT_QMenuBar.setVisible(False)
                toplevel_win.QT_QMainWindow.setMenuBar(element.QT_QMenuBar)
            # -------------------------  BUTTONMENU placement element  ------------------------- #
            elif element_type == ELEM_TYPE_BUTTONMENU:
                btext = element.ButtonText
                element.Widget = element.QT_QPushButton = QPushButton(btext)
                style = create_style_from_font(font)
                if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    style += 'background-color: %s;' % element.BackgroundColor
                if element.BorderWidth == 0:
                    style += 'border: none;'
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                # style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_QPushButton.setStyleSheet(style)
                if (element.AutoSizeButton is False or toplevel_win.AutoSizeButtons is False or element.Size[0] is not None) and element.ImageData is None:
                    if element_size[0] is not None:
                        element.QT_QPushButton.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_QPushButton.setFixedHeight(element_size[1])

                if element.ImageData:
                    ba = QtCore.QByteArray.fromBase64(element.ImageData)
                    pixmap = QtGui.QPixmap()
                    pixmap.loadFromData(ba)
                    element.QT_QPushButton.setIcon(pixmap)
                    element.QT_QPushButton.setIconSize(pixmap.rect().size())

                if element.Disabled:
                    element.QT_QPushButton.setDisabled(True)

                if element.Tooltip:
                    element.QT_QPushButton.setToolTip(element.Tooltip)
                # element.QT_QPushButton.clicked.connect(element._ButtonCallBack)

                menu_def = element.MenuDefinition

                qmenu = QMenu(element.QT_QPushButton)
                qmenu.setTitle(menu_def[0])
                AddMenuItem(qmenu, menu_def[1], element)

                element.QT_QPushButton.setMenu(qmenu)
                if element.Tooltip:
                    element.QT_QPushButton.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_QPushButton.setVisible(False)
                qt_row_layout.addWidget(element.QT_QPushButton)
            # -------------------------  Frame placement element  ------------------------- #
            elif element_type == ELEM_TYPE_FRAME:
                element.Widget = column_widget = QGroupBox()
                element.QT_QGroupBox = column_widget
                style = create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                # style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                # style += 'border: {}px solid gray; '.format(border_depth)
                column_widget.setStyleSheet(style)

                column_widget.setTitle(element.Title)
                column_layout = QFormLayout()
                column_vbox = QVBoxLayout()
                PackFormIntoFrame(element, column_layout, toplevel_win)
                column_vbox.addLayout(column_layout)
                column_widget.setLayout(column_vbox)
                if element.Tooltip:
                    column_widget.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_QGroupBox.setVisible(False)
                qt_row_layout.addWidget(column_widget)
            # -------------------------  Tab placement element  ------------------------- #
            elif element_type == ELEM_TYPE_TAB:
                element.Widget = tab_widget = QWidget()
                element.QT_QWidget = tab_widget
                # tab_widget.setFrameShape(QtWidgets.QFrame.NoFrame)
                style = create_style_from_font(font)
                if element.BackgroundColor is not None:
                    # style += 'background-color: %s;' % element.BackgroundColor
                    # style += 'QTabWidget > QWidget > QWidget {background: %s;}'% element.BackgroundColor
                    style += 'QTabWidget::pane {background: %s;}'% element.BackgroundColor
                    # style += 'background-color: %s;' % element.BackgroundColor
                    tab_widget.setAutoFillBackground(True)
                    palette = tab_widget.palette()
                    palette.setColor(tab_widget.backgroundRole(), element.BackgroundColor)
                    tab_widget.setPalette(palette)

                # style += 'border: {}px solid gray; '.format(border_depth)
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                # print(f'Tab widget style {style}')
                tab_widget.setStyleSheet(style)

                column_layout = QFormLayout()
                column_vbox = QVBoxLayout()

                PackFormIntoFrame(element, column_layout, toplevel_win)

                column_vbox.addLayout(column_layout)
                tab_widget.setLayout(column_vbox)
                if element.Tooltip:
                    tab_widget.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_QWidget.setVisible(False)
                container_elem.QT_QTabWidget.addTab(tab_widget, element.Title)
            # -------------------------  TabGroup placement element  ------------------------- #
            elif element_type == ELEM_TYPE_TAB_GROUP:
                element = element       # type:TabGroup
                element.Widget = element.QT_QTabWidget = qtab =QTabWidget()

                style = qtab.styleSheet()
                if element.SelectedTitleColor not in (None, COLOR_SYSTEM_DEFAULT):
                    style += 'QTabBar::tab:selected {background: %s;}'%element.SelectedTitleColor
                if element.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
                    style += 'QTabBar::tab {background: %s;}'% element.BackgroundColor
                if element.TextColor not in (None, COLOR_SYSTEM_DEFAULT):
                    style += 'QTabBar::tab {color: %s;}'%element.TextColor
                qtab.setStyleSheet(style)

                if element.TabLocation is not None:
                    position_dict = {'left': QtWidgets.QTabWidget.TabPosition.West, 'right': QtWidgets.QTabWidget.TabPosition.East, 'top': QtWidgets.QTabWidget.TabPosition.North, 'bottom': QtWidgets.QTabWidget.TabPosition.South, 'lefttop': QtWidgets.QTabWidget.TabPosition.North,
                                     'leftbottom': QtWidgets.QTabWidget.TabPosition.South, 'righttop': QtWidgets.QTabWidget.TabPosition.North, 'rightbottom': QtWidgets.QTabWidget.TabPosition.South, 'bottomleft': QtWidgets.QTabWidget.TabPosition.South,
                                     'bottomright': QtWidgets.QTabWidget.TabPosition.South, 'topleft': QtWidgets.QTabWidget.TabPosition.North, 'topright': QtWidgets.QTabWidget.TabPosition.North}
                    try:
                        element.Widget.setTabPosition(position_dict[element.TabLocation])
                    except:
                        print('Bad tab position specified {}', element.TabLocation)
                PackFormIntoFrame(element, element.ParentForm.QFormLayout, toplevel_win)

                qt_row_layout.addWidget(element.QT_QTabWidget)
                if not element.Visible:
                    element.QT_QTabWidget.setVisible(False)

                if element.ChangeSubmits:
                    element.QT_QTabWidget.currentChanged.connect(element.QtCallbackStateChanged)
            # -------------------------  SLIDER placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SLIDER:
                element = element           # type: Slider
                element.Widget = element.QT_Slider = QSlider()
                if element.Orientation.startswith('h'):
                    element.QT_Slider.setOrientation(Qt.Horizontal)
                else:
                    element.QT_Slider.setOrientation(Qt.Vertical)
                if element.Disabled:
                    element.QT_Slider.setDisabled(True)
                style = create_style_from_font(font)
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_Slider.setStyleSheet(style)

                element.QT_Slider.setMinimum(element.Range[0])
                element.QT_Slider.setMaximum(element.Range[1])

                position = QSlider.TicksBothSides
                if element.Relief == RELIEF_TICK_POSITION_NO_TICKS:
                    position = QSlider.NoTicks
                elif element.Relief == RELIEF_TICK_POSITION_BOTH_SIDES:
                    position = QSlider.TicksBothSides
                elif element.Relief == RELIEF_TICK_POSITION_ABOVE:
                    position = QSlider.TicksAbove
                elif element.Relief == RELIEF_TICK_POSITION_BELOW:
                    position = QSlider.TicksBelow
                elif element.Relief == RELIEF_TICK_POSITION_LEFT:
                    position = QSlider.TicksLeft
                elif element.Relief == RELIEF_TICK_POSITION_RIGHT:
                    position = QSlider.TicksRight
                element.QT_Slider.setTickPosition(position)

                if element.TickInterval is not None:
                    element.QT_Slider.setTickInterval(element.TickInterval)
                if element.Resolution is not None:
                    element.QT_Slider.setSingleStep(element.Resolution)
                    element.QT_Slider.setPageStep(element.Resolution)
                if element_size[0] is not None:
                    element.QT_Slider.setFixedWidth(element_size[0])
                if element_size[1] is not None:
                    element.QT_Slider.setFixedHeight(element_size[1])
                element.QT_Slider.setValue(element.DefaultValue)

                if element.ChangeSubmits:
                    element.QT_Slider.valueChanged.connect(element._QtCallbackValueChanged)
                if element.Tooltip:
                    element.QT_Slider.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_Slider.setVisible(False)
                qt_row_layout.addWidget(element.QT_Slider)
            # -------------------------  DIAL placement element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_DIAL:
                element.Widget = element.QT_Dial = qdial = QDial()

                style = create_style_from_font(font)
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_Dial.setStyleSheet(style)

                if element.Disabled:
                    element.QT_Dial.setDisabled(True)

                element.QT_Dial.setMinimum(element.Range[0])
                element.QT_Dial.setMaximum(element.Range[1])

                qdial.setNotchesVisible(True)
                if element.TickInterval is not None:
                    qdial.setNotchTarget(element.TickInterval)
                if element.Resolution is not None:
                    element.QT_Dial.setSingleStep(element.Resolution)
                if element_size[0] is not None:
                    element.QT_Dial.setFixedWidth(element_size[0])
                if element_size[1] is not None:
                    element.QT_Dial.setFixedHeight(element_size[1])
                element.QT_Dial.setValue(element.DefaultValue)

                if element.ChangeSubmits:
                    element.QT_Dial.valueChanged.connect(element._QtCallbackValueChanged)
                if element.Tooltip:
                    element.QT_Dial.setToolTip(element.Tooltip)
                # qt_row_layout.setContentsMargins(*full_element_pad)
                if not element.Visible:
                    element.QT_Dial.setVisible(False)
                qt_row_layout.addWidget(element.QT_Dial)
            # -------------------------  Stretch placement element  ------------------------- #
            elif element_type == ELEM_TYPE_STRETCH:
                element = element       # type: Stretch
                element.Widget = qt_row_layout.addStretch(1)
            # -------------------------  TABLE placement element  ------------------------- #
            elif element_type == ELEM_TYPE_TABLE:
                element = element       # type: Table
                element.Widget = element.QT_TableWidget = Table.QTTableWidget(toplevel_win.ReturnKeyboardEvents, toplevel_win)
                if element.NumRows is not None:
                    element.QT_TableWidget.setFixedHeight(element.NumRows*35+25)
                # element.QT_TableWidget = QTableWidget()
                style = ''
                if element.HeaderBackgroundColor is not None:
                    style += 'QHeaderView::section {background-color: %s;}\n' % element.HeaderBackgroundColor
                if element.HeaderTextColor is not None:
                    style += 'QHeaderView::section {color: %s;}\n' % element.HeaderTextColor
                style += 'QTableWidget {'
                style += create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;\n' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor


                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                style += '}'
                style += """QScrollBar:vertical {
                            border: none;
                            background:lightgray;
                            width:12px;
                            margin: 0px 0px 0px 0px;
                        } """
                element.QT_TableWidget.setStyleSheet(style)
                if element.ChangeSubmits:
                    element.QT_TableWidget.itemSelectionChanged.connect(element._QtCallbackCellActivated)
                element.QT_TableWidget.setRowCount(len(element.Values))
                element.QT_TableWidget.setColumnCount(len(element.Values[0]))
                for rownum, rows in enumerate(element.Values):
                    # element.QT_TableWidget.insertRow(rownum)
                    for colnum, columns in enumerate(rows):
                        element.QT_TableWidget.setItem(rownum, colnum, QTableWidgetItem(element.Values[rownum][colnum]))

                if element.ColumnHeadings is not None:
                    element.QT_TableWidget.setHorizontalHeaderLabels(element.ColumnHeadings)

                element.QT_TableWidget.installEventFilter(element.QT_TableWidget)
                element.QT_TableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
                if element.Tooltip:
                    element.QT_TableWidget.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_TableWidget.setVisible(False)

                qt_row_layout.addWidget(element.QT_TableWidget)
            # -------------------------  Tree placement element  ------------------------- #
            elif element_type == ELEM_TYPE_TREE:
                element = element   # type: Tree
                element.Widget = element.QT_QTreeWidget = QTreeWidget()
                if element_size != (None, None):
                    element.QT_QTreeWidget.setFixedWidth(element_size[0])
                    element.QT_QTreeWidget.setFixedHeight(element_size[1])
                height = element.NumRows
                element.QT_QTreeWidget.setFixedHeight(height*25)        # convert num rows into pixels...crude but effective

                if element.ColumnsToDisplay is None:  # Which cols to display
                    displaycolumns = element.ColumnHeadings
                else:
                    displaycolumns = []
                    for i, should_display in enumerate(element.ColumnsToDisplay):
                        if should_display:
                            displaycolumns.append(element.ColumnHeadings[i])
                column_headings = element.ColumnHeadings
                # ------------- GET THE TREEVIEW WIDGET -------------
                for i, heading in enumerate(element.ColumnHeadings):  # Configure cols + headings
                    # QTree.heading(heading, text=heading)
                    if element.AutoSizeColumns:
                        width = min(element.MaxColumnWidth, len(heading) + 1)
                    else:
                        try:
                            width = element.ColumnWidths[i]
                        except:
                            width = element.DefaultColumnWidth
                    # treeview.column(heading, width=width * CharWidthInPixels(), anchor=anchor)
                def add_treeview_data(node, widget):
                    # print(f'Inserting {node.key} under parent {node.parent}')
                    if node != element.TreeData.root_node:
                        child = QTreeWidgetItem(widget)
                        child.setText(0, str(node.text))
                    else:
                        child = widget
                    # if node.key != '':
                    # child.setData(0,0,node.values)
                    if type(node.icon) is bytes:
                        ba = QtCore.QByteArray.fromBase64(node.icon)
                        pixmap = QtGui.QPixmap()
                        pixmap.loadFromData(ba)
                        qicon = QIcon(pixmap)
                        child.setIcon(0, qicon)
                    elif node.icon is not None:
                        qicon = QIcon(node.icon)
                        child.setIcon(0, qicon)

                    for node in node.children:
                        add_treeview_data(node, child)

                # for node in element.TreeData.root_node.children:
                #     add_treeview_data(node, element.QT_QTreeWidget)

                add_treeview_data(element.TreeData.root_node, element.QT_QTreeWidget)

                style = 'QTreeWidget {'
                style += create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;\n' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                style += '}'
                style += """QScrollBar:vertical {              
                            border: none;
                            background:lightgray;
                            width:12px;
                            margin: 0px 0px 0px 0px;
                        } """
                element.QT_QTreeWidget.setStyleSheet(style)
                if element.ChangeSubmits:
                    element.QT_QTreeWidget.itemSelectionChanged.connect(element._QtCallbackCellActivated)

                if element.ShowExpanded:
                    element.QT_QTreeWidget.expandAll()
                    element.QT_QTreeWidget.show()
                if element.Tooltip:
                    element.QT_QTreeWidget.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_QTreeWidget.setVisible(False)
                qt_row_layout.addWidget(element.QT_QTreeWidget)
            # -------------------------  Separator placement element  ------------------------- #
            elif element_type == ELEM_TYPE_SEPARATOR:
                element = element           # type: HorizontalSeparator
                element.Widget = element.QT_Label = qlabel = QLabel('', toplevel_win.QTWindow)
                if not auto_size_text:
                    if element_size[0] is not None:
                        element.QT_Label.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_Label.setFixedHeight(element_size[1])
                style = ''
                if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                element.QT_Label.setStyleSheet(style)

                qlabel.setFrameStyle(QFrame.VLine if element.Orientation[0] =='v' else QFrame.HLine)

                qt_row_layout.addWidget(element.QT_Label)

                pass

        # ............................DONE WITH ROW pack the row of widgets ..........................#
        qt_row_layout.setSpacing(toplevel_win.ElementPadding[0])
        containing_frame.setSpacing(toplevel_win.ElementPadding[1])
        containing_frame.addRow('', qt_row_layout)

        # done with row, pack the row of widgets
        # tk_row_frame.grid(row=row_num+2, sticky=tk.NW, padx=DEFAULT_MARGINS[0])
    return


def ConvertFlexToTK(window):
    InitializeResults(window)
    pass
    master = 000000
    PackFormIntoFrame(window, window.QFormLayout, window)
    # ....................................... DONE creating and laying out window ..........................#
    screen_width = 000000 # get window info to move to middle of screen
    screen_height = 000000
    if window.Location != (None, None):
        window.QT_QMainWindow.move(window.Location[0], window.Location[1])
        x, y = window.Location
    elif DEFAULT_WINDOW_LOCATION != (None, None):
        x, y = DEFAULT_WINDOW_LOCATION
    else:
        win_width = 0000000
        win_height = 000000
        x = screen_width / 2 - win_width / 2
        y = screen_height / 2 - win_height / 2
        if y + win_height > screen_height:
            y = screen_height - win_height
        if x + win_width > screen_width:
            x = screen_width - win_width



    return

# ----====----====----====----====----==== Start timer ====----====----====----====----====----#

def start_window_read_timer(window, amount):
    timer = QtCore.QTimer()
    timer.timeout.connect(window._timer_timeout)
    timer.start(amount)
    return timer


def start_systray_read_timer(tray, amount):
    timer = QtCore.QTimer()
    timer.timeout.connect(tray._timer_timeout)
    timer.start(amount)
    return timer


def start_window_autoclose_timer(window, amount):
    timer = QtCore.QTimer()
    window.autoclose_timer = timer
    timer.timeout.connect(window._autoclose_timer_callback)
    timer.start(amount)
    return timer

def stop_timer(timer):
    timer.stop()

# ----====----====----====----====----==== STARTUP TK ====----====----====----====----====----#
def StartupTK(window):
    """
    Does the building of the window with all the widgets
    :param my_flex_form: you window object
    :type my_flex_form: (Window)
    """

    global using_pyqt5

    ow = Window.NumOpenWindows

    if Window.QTApplication is None:
        Window.QTApplication = QApplication(sys.argv)

    window.QTApplication = Window.QTApplication

    Window.IncrementOpenCount()

    # window.QTWindow = QWidget()

    window.QT_QMainWindow = Window.QT_QMainWindowClass(window.ReturnKeyboardEvents, window)
    window.QTWindow = Window.QTMainWindow(window.ReturnKeyboardEvents, window)
    window.QT_QMainWindow.setCentralWidget(window.QTWindow)

    window.QT_QMainWindow.installEventFilter(window.QT_QMainWindow)

    window.QTApplication.setActiveWindow(window.QT_QMainWindow)

    flags = QtCore.Qt.WindowFlags()
    if window.NoTitleBar:
        flags |= Qt.FramelessWindowHint
        flags |= QtCore.Qt.Tool
    if window.KeepOnTop:
        flags |= Qt.WindowStaysOnTopHint

    if not using_pyqt5 and flags is not None:
        window.QT_QMainWindow.setWindowFlags(flags)
    if window.AlphaChannel:
        window.QT_QMainWindow.setWindowOpacity(window.AlphaChannel)
    if window.WindowIcon is not None:
        if type(window.WindowIcon) is bytes:
            ba = QtCore.QByteArray.fromBase64(window.WindowIcon)
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(ba)
            qicon = QIcon(pixmap)
            window.QT_QMainWindow.setWindowIcon(qicon)
        else:
            window.QT_QMainWindow.setWindowIcon(QtGui.QIcon(window.WindowIcon))
    if window.DisableMinimize:
        window.QT_QMainWindow.setWindowFlags(window.QT_QMainWindow.windowFlags()&~Qt.WindowMinimizeButtonHint)
        window.QT_QMainWindow.setWindowFlags(window.QT_QMainWindow.windowFlags()&~Qt.WindowMaximizeButtonHint)
    if window.DisableClose:
        window.QT_QMainWindow.setWindowFlags(window.QT_QMainWindow.windowFlags()&~Qt.WindowCloseButtonHint)

    # window.QTWindow.setAttribute(Qt.WA_TranslucentBackground)
    # shadow = QtWidgets.QGraphicsDropShadowEffect()
    # shadow.setBlurRadius(9.0)
    # shadow.setBlurRadius(50)
    # window.QTWindow.setGraphicsEffect(shadow)

    # if window.KeepOnTop:
    #     window.QTWindow.setWindowFlags(Qt.WindowStaysOnTopHint)


    # style = 'QMainWindow {'
    # style = window.QT_QMainWindow.styleSheet()
    if window.BackgroundColor is not None and window.BackgroundColor != COLOR_SYSTEM_DEFAULT:
        style = 'background-color: %s;' % window.BackgroundColor
        # style += '}'
        window.QT_QMainWindow.setStyleSheet(style)

    if window.BackgroundImage is not None:
        qlabel = QLabel(window.QTWindow)
        qlabel.setText('')
        w = QtGui.QPixmap(window.BackgroundImage).width()
        h = QtGui.QPixmap(window.BackgroundImage).height()
        qlabel.setGeometry(QtCore.QRect(0,0, w, h))
        # qlabel.setGeometry(window.QTWindow.geometry())
        qlabel.setPixmap(QtGui.QPixmap(window.BackgroundImage))
        # style += 'background-image: url(%s);' % window.BackgroundImage


    window.QT_QMainWindow.setWindowTitle(window.Title)

    if (window.GrabAnywhere is not False and not (
            window.NonBlocking and window.GrabAnywhere is not True)):
        pass

    window.QFormLayout = QFormLayout()
    window.QT_Box_Layout = QVBoxLayout()
    ConvertFlexToTK(window)
    window.QT_Box_Layout.addLayout(window.QFormLayout)


    # shadow = QtWidgets.QGraphicsDropShadowEffect( window.QFormLayout)
    # window.QTWindow.setGraphicsEffect(shadow)



    # Make window visible again
    pass

    if window.ReturnKeyboardEvents and not window.NonBlocking:
        pass
    elif window.ReturnKeyboardEvents:
        pass

    # print('..... CALLING MainLoop')
    window.CurrentlyRunningMainloop = True
    window.QTWindow.setLayout(window.QT_Box_Layout)

    if window.FocusElement is not None:
        window.FocusElement.setFocus()

    # Resize the window to the size it should be at... dunno why I need to do this but I do...
    # add 5 pixels onto it because stuff was getting cut off
    qsize = window.QT_QMainWindow.sizeHint()
    size = [qsize.width(), qsize.height()]
    size[0] += 10
    window.QT_QMainWindow.resize(*size)

    if window._Size != (None, None):
        window.QT_QMainWindow.resize(window._Size[0], window._Size[1])

    if not window.Resizable:
        window.QT_QMainWindow.setFixedSize(*size)



    timer = None
    if window.AutoClose:
        timer = start_window_autoclose_timer(window, window.AutoCloseDuration*1000)

    if not window.NonBlocking:
        if window.Timeout:
            timer = start_window_read_timer(window, window.Timeout)
        window.QT_QMainWindow.show()              ####### The thing that causes the window to be visible ######
        #### ------------------------------ RUN MAIN LOOP HERE ------------------------------ #####
        window.QTApplication.exec_()
        if timer:
            stop_timer(timer)
    else:                                   # Non-blocking window
        window.QT_QMainWindow.show()              ####### The thing that causes the window to be visible ######
        window.QTApplication.processEvents()



        window.CurrentlyRunningMainloop = False
        window.TimerCancelled = True
        # print('..... BACK from MainLoop')
        if not window.FormRemainedOpen:
            Window.DecrementOpenCount()
        if window.RootNeedsDestroying:
            # print('** Destroying window **')
            window.QT_QMainWindow.close()         # destroy the window
            window.RootNeedsDestroying = False
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
            col = [[T(''.join(map(lambda x: str(x)+'\n',args)),key='_OPTMSG_')]] ### convert all *args into one string that can be updated
            col += [[T('', size=(25,5), key='_STATS_')],
                   [ProgressBar(max_value=self.max_value, orientation='h', key='_PROG_', size=self.size,
                                bar_color=self.bar_color)],
                   [Cancel(button_color=self.button_color), Stretch()]]
            layout += [Column(col)]
        else:
            col = [[ProgressBar(max_value=self.max_value, orientation='v', key='_PROG_', size=self.size, bar_color=self.bar_color)]]
            col2 = [[T(''.join(map(lambda x: str(x)+'\n',args)),key='_OPTMSG_')]] ### convert all *args into one string that can be updated
            col2 += [[T('', size=(25,5), key='_STATS_')],[Cancel(button_color=self.button_color), Stretch()]]
            layout += [Column(col), Column(col2)]
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


def OneLineProgressMeter(title, current_value, max_value, key='OK for 1 meter', *args, orientation='v', bar_color=(None, None),
                         button_color=None, size=DEFAULT_PROGRESS_BAR_SIZE, border_width=None, grab_anywhere=False):
    """
    :param orientation: 'horizontal' or 'vertical' ('h' or 'v' work) (Default value = 'vertical' / 'v')
    :type orientation: (str)
    :param bar_color: color of a bar line
    :type bar_color: Tuple(str, str)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param size: (w,h) w=characters-wide, h=rows-high (Default value = DEFAULT_PROGRESS_BAR_SIZE)
    :type size: Tuple[int, int]
    :param border_width:  width of border around element
    :type border_width: (int)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    """
    if key not in QuickMeter.active_meters:
        meter = QuickMeter(title, current_value, max_value, key, *args, orientation=orientation, bar_color=bar_color,
                           button_color=button_color, size=size, border_width=border_width, grab_anywhere=grab_anywhere)
        QuickMeter.active_meters[key] = meter
    else:
        meter = QuickMeter.active_meters[key]

    rc = meter.UpdateMeter(current_value, max_value, *args)
    OneLineProgressMeter.exit_reasons = getattr(OneLineProgressMeter,'exit_reasons', QuickMeter.exit_reasons)
    return rc == METER_OK

def OneLineProgressMeterCancel(key='OK for 1 meter'):
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
    """
    :param color: color string, like "#RRGGBB"
    :type color: (str)
    :return color: color string, like "#RRGGBB"
    :type color: (str)
    """
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
        self.output_element = MultilineOutput(size=win_size, key='_MULTILINE_') if do_not_reroute_stdout else Output(size=win_size)

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
            end_str = str(end) if end is not None else '\n'
            sep_str = str(sep) if sep is not None else ' '

            outstring = ''
            num_args = len(args)
            for i, arg in enumerate(args):
                outstring += str(arg)
                if i != num_args - 1:
                    outstring += sep_str
            outstring += end_str
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

    """
    :param args: The arguments to display
    :type args: List[Any]
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param end:  The end char to use just like print uses
    :type end: (str)
    :param sep: end character
    :type end: (str)
    :param sep: separator character
    :type sep: (str)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param no_button: don't show button
    :type no_button: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param do_not_reroute_stdout: do not reroute stdout
    :type do_not_reroute_stdout: (bool)
    :param text_color: color of the text
    :type text_color: (str)
    :param background_color: color of background
    :type background_color: (str)
    """

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




#                            d8b          888
#                            Y8P          888
#                                         888
#   .d8888b 88888b.  888d888 888 88888b.  888888
#  d88P"    888 "88b 888P"   888 888 "88b 888
#  888      888  888 888     888 888  888 888
#  Y88b.    888 d88P 888     888 888  888 Y88b.
#   "Y8888P 88888P"  888     888 888  888  "Y888
#           888
#           888
#           888



CPRINT_DESTINATION_WINDOW = None
CPRINT_DESTINATION_MULTILINE_ELMENT_KEY = None

def cprint_set_output_destination(window, multiline_key):
    """
    Sets up the color print (cprint) output destination
    :param window: The window that the cprint call will route the output to
    :type window: (Window)
    :param multiline_key: Key for the Multiline Element where output will be sent
    :type multiline_key: (Any)
    :return: None
    :rtype: None
    """

    global CPRINT_DESTINATION_WINDOW, CPRINT_DESTINATION_MULTILINE_ELMENT_KEY

    CPRINT_DESTINATION_WINDOW = window
    CPRINT_DESTINATION_MULTILINE_ELMENT_KEY = multiline_key



# def cprint(*args, **kwargs):
def cprint(*args, end=None, sep=' ', text_color=None, t=None, background_color=None, b=None, colors=None, c=None, window=None, key=None):
    """
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

    :param *args: stuff to output
    :type *args: (Any)
    :param text_color: Color of the text
    :type text_color: (str)
    :param background_color: The background color of the line
    :type background_color: (str)
    :param colors: Either a tuple or a string that has both the text and background colors
    :type colors: (str) or Tuple[str, str]
    :param t: Color of the text
    :type t: (str)
    :param b: The background color of the line
    :type b: (str)
    :param c: Either a tuple or a string that has both the text and background colors
    :type c: (str) or Tuple[str, str]
    :param end: end character
    :type end: (str)
    :param sep: separator character
    :type sep: (str)
    :param key: key of multiline to output to (if you want to override the one previously set)
    :type key: (Any)
    :param window: Window containing the multiline to output to (if you want to override the one previously set)
    :type window: (Window)
    :return: None
    :rtype: None
    """

    destination_key = CPRINT_DESTINATION_MULTILINE_ELMENT_KEY if key is None else key
    destination_window = window or CPRINT_DESTINATION_WINDOW

    if (destination_window is None and window is None) or (destination_key is None and key is None):
        print('** Warning ** Attempting to perform a cprint without a valid window & key',
              'Will instead print on Console',
              'You can specify window and key in this cprint call, or set ahead of time using cprint_set_output_destination')
        print(*args)
        return

    kw_text_color = text_color or t
    kw_background_color = background_color or b
    dual_color = colors or c
    try:
        if isinstance(dual_color, tuple):
            kw_text_color = dual_color[0]
            kw_background_color = dual_color[1]
        elif isinstance(dual_color, str):
            kw_text_color = dual_color.split(' on ')[0]
            kw_background_color = dual_color.split(' on ')[1]
    except Exception as e:
        print('* cprint warning * you messed up with color formatting', e)

    mline = destination_window.find_element(destination_key, silent_on_error=True)      # type: Multiline
    try:
        # mline = destination_window[destination_key]     # type: # Multiline
        if end is None:
            mline.print(*args, text_color=kw_text_color, background_color=kw_background_color, end='', sep=sep)
            mline.print('')
        else:
            mline.print(*args,text_color=kw_text_color, background_color=kw_background_color, end=end, sep=sep)
    except Exception as e:
        print('** cprint error trying to print to the multiline. Printing to console instead **', e)
        print(*args, end=end, sep=sep)



# ------------------------------------------------------------------------------------------------ #
# A print-like call that can be used to output to a multiline element as if it's an Output element #
# ------------------------------------------------------------------------------------------------ #


def _print_to_element(multiline_element, *args, end=None, sep=None, text_color=None, background_color=None, autoscroll=True):
    """
    Print like Python normally prints except route the output to a multline element and also add colors if desired

    :param multiline_element:  The multiline element to be output to
    :type multiline_element: (Multiline)
    :param args:  The arguments to print
    :type args: List[Any]
    :param end:  The end char to use just like print uses
    :type end: (str)
    :param sep:  The separation character like print uses
    :type sep: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param background_color: The background color of the line
    :type background_color: (str)
    :param autoscroll: If True (the default), the element will scroll to bottom after updating
    :type autoscroll: Bool
    """
    end_str = str(end) if end is not None else '\n'
    sep_str = str(sep) if sep is not None else ' '

    outstring = ''
    num_args = len(args)
    for i, arg in enumerate(args):
        outstring += str(arg)
        if i != num_args-1:
            outstring += sep_str
    outstring += end_str

    multiline_element.update(outstring, append=True, text_color_for_value=text_color, background_color_for_value=background_color, autoscroll=autoscroll)



# ========================  Scrolled Text Box   =====#
# ===================================================#
def PopupScrolled(*args, button_color=None, yes_no=False, auto_close=False, auto_close_duration=None,
                  size=(None, None), location=(None, None), title=None, non_blocking=False):
    """
    :param args: The arguments to display
    :type args: List[Any]
    :param title: Title to display in the window.
    :type title: (str)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param yes_no: If True, displays Yes and No buttons instead of Ok
    :type yes_no: (bool)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param size: (w,h) w=characters-wide, h=rows-high
    :type size: Tuple[int, int]
    :param location: Location on the screen to place the upper left corner of the window
    :type location: Tuple[int, int]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    """
    if not args: return
    width, height = size
    width = width if width else MESSAGE_BOX_LINE_WIDTH
    window = Window(title=title or args[0], auto_size_text=True, button_color=button_color, auto_close=auto_close,
                  auto_close_duration=auto_close_duration, location=location)
    max_line_total, max_line_width, total_lines, height_computed = 0, 0, 0, 0
    complete_output = ''
    for message in args:
        # fancy code to check if string and convert if not is not need. Just always convert to string :-)
        # if not isinstance(message, str): message = str(message) - new
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
    computed_size = (max_line_width*10, height_computed*16)
    window.AddRow(MultilineOutput(complete_output, size=computed_size))
    pad = max_line_total - 15 if max_line_total > 15 else 1
    # show either an OK or Yes/No depending on paramater
    button = DummyButton if non_blocking else Button
    if yes_no:
        window.AddRow(Text('', size=(pad, 1), auto_size_text=False), button('Yes'), button('No'))
    else:
        window.AddRow(Text('', size=(pad, 1), auto_size_text=False), button('OK', size=(5, 1), button_color=button_color))

    if non_blocking:
        button, values = window.Read(timeout=0)
        Window.active_popups[window] = title
    else:
        button, values = window.Read()
    return button


ScrolledTextBox = PopupScrolled


# ============================== SetGlobalIcon ======#
# Sets the icon to be used by default                #
# ===================================================#
def SetGlobalIcon(icon):
    """
    :param icon: Either a Base64 byte string or a filename
    :type icon: Union[bytes, str]
    """

    try:
        with open(icon, 'r') as icon_file:
            pass
    except:
        raise FileNotFoundError
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
               window_location=(None, None), error_button_color=(None,None),
               tooltip_time=None):
    """
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param button_color: Color of the button (text, background)
    :type button_color: Tuple[str, str]
    :param element_size: element size (width, height) in characters
    :type element_size: Tuple[int, int]
    :param button_element_size: Size of button
    :type button_element_size: Tuple[int, int]
    :param margins: (left/right, top/bottom) tkinter margins around outsize. Amount of pixels to leave inside the window's frame around the edges before your elements are shown.
    :type margins: Tuple[int, int]
    :param element_padding: Default amount of padding to put around elements in window (left/right, top/bottom) or ((left, right), (top, bottom))
    :type element_padding: Tuple[int, int] or ((int, int),(int,int))
    :param auto_size_text: True if the Widget should be shrunk to exactly fit the number of chars to show
    :type auto_size_text: bool
    :param auto_size_buttons: True if Buttons in this Window should be sized to exactly fit the text on this.
    :type auto_size_buttons: (bool)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param border_width:  width of border around element
    :type border_width: (int)
    :param slider_border_width: ???
    :type slider_border_width: ???
    :param slider_relief: ???
    :type slider_relief: ???
    :param slider_orientation: ???
    :type slider_orientation: ???
    :param autoclose_time: ???
    :type autoclose_time: ???
    :param message_box_line_width: ???
    :type message_box_line_width: ???
    :param progress_meter_border_depth: ???
    :type progress_meter_border_depth: ???
    :param progress_meter_style: You can no longer set a progress bar style. All ttk styles must be the same for the window
    :type progress_meter_style: ???
    :param progress_meter_relief:
    :type progress_meter_relief: ???
    :param progress_meter_color: ???
    :type progress_meter_color: ???
    :param progress_meter_size: ???
    :type progress_meter_size: ???
    :param text_justification: Default text justification for all Text Elements in window
    :type text_justification: Union['left', 'right', 'center']
    :param background_color: color of background
    :type background_color: (str)
    :param element_background_color: element background color
    :type element_background_color: (str)
    :param text_element_background_color: text element background color
    :type text_element_background_color: (str)
    :param input_elements_background_color: ???
    :type input_elements_background_color: idk_yetReally
    :param input_text_color: ???
    :type input_text_color: ???
    :param scrollbar_color: ???
    :type scrollbar_color: ???
    :param text_color: color of the text
    :type text_color: (str)
    :param element_text_color: ???
    :type element_text_color: ???
    :param debug_win_size: window size
    :type debug_win_size: Tuple[int, int]
    :param window_location: (Default = (None))
    :type window_location: ???
    :param error_button_color: (Default = (None))
    :type error_button_color: ???
    :param tooltip_time: time in milliseconds to wait before showing a tooltip. Default is 400ms
    :type tooltip_time: (int)
    :param tooltip_font: font to use for all tooltips
    :type tooltip_font: str or Tuple[str, int] or Tuple[str, int, str]
    :param use_ttk_buttons: if True will cause all buttons to be ttk buttons
    :type use_ttk_buttons: (bool)
    :param ttk_theme: Theme to use with ttk widgets.  Choices (on Windows) include - 'default', 'winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative'
    :type ttk_theme: (str)
    """
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
    global DEFAULT_ERROR_BUTTON_COLOR

    if icon:
        Window.user_defined_icon = icon

    if button_color != None:
        DEFAULT_BUTTON_COLOR = button_color

    if element_size != (None, None):
        DEFAULT_ELEMENT_SIZE = _convert_tkinter_size_to_Qt(element_size)

    if button_element_size != (None, None):
        DEFAULT_BUTTON_ELEMENT_SIZE = _convert_tkinter_size_to_Qt(button_element_size)

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

    if error_button_color != (None,None):
        print('error button')
        DEFAULT_ERROR_BUTTON_COLOR = error_button_color

    return True


# ----------------------------------------------------------------- #

# .########.##.....##.########.##.....##.########..######.
# ....##....##.....##.##.......###...###.##.......##....##
# ....##....##.....##.##.......####.####.##.......##......
# ....##....#########.######...##.###.##.######....######.
# ....##....##.....##.##.......##.....##.##.............##
# ....##....##.....##.##.......##.....##.##.......##....##
# ....##....##.....##.########.##.....##.########..######.

# ----------------------------------------------------------------- #

# The official Theme code

#################### ChangeLookAndFeel #######################
# Predefined settings that will change the colors and styles #
# of the elements.                                           #
##############################################################
LOOK_AND_FEEL_TABLE = {'SystemDefault':
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

                       'SystemDefault1':
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
                       'Default':  # plain gray but blue buttons
                           {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
                            'TEXT': COLOR_SYSTEM_DEFAULT,
                            'INPUT': COLOR_SYSTEM_DEFAULT,
                            'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
                            'SCROLL': COLOR_SYSTEM_DEFAULT,
                            'BUTTON': OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR,
                            'PROGRESS': COLOR_SYSTEM_DEFAULT,
                            'BORDER': 1, 'SLIDER_DEPTH': 1,
                            'PROGRESS_DEPTH': 0},

                       'Default1':  # everything is gray
                           {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
                            'TEXT': COLOR_SYSTEM_DEFAULT,
                            'INPUT': COLOR_SYSTEM_DEFAULT,
                            'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
                            'SCROLL': COLOR_SYSTEM_DEFAULT,
                            'BUTTON': COLOR_SYSTEM_DEFAULT,
                            'PROGRESS': COLOR_SYSTEM_DEFAULT,
                            'BORDER': 1, 'SLIDER_DEPTH': 1,
                            'PROGRESS_DEPTH': 0},

                       'DefaultNoMoreNagging':  # a duplicate of "Default" for users that are tired of the nag screen
                           {'BACKGROUND': COLOR_SYSTEM_DEFAULT,
                            'TEXT': COLOR_SYSTEM_DEFAULT,
                            'INPUT': COLOR_SYSTEM_DEFAULT,
                            'TEXT_INPUT': COLOR_SYSTEM_DEFAULT,
                            'SCROLL': COLOR_SYSTEM_DEFAULT,
                            'BUTTON': OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR,
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
                       'LightBrown4': {'BACKGROUND': '#d7c79e', 'TEXT': '#a35638', 'INPUT': '#9dab86', 'TEXT_INPUT': '#000000', 'SCROLL': '#a35638',
                                       'BUTTON': ('white', '#a35638'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#a35638', '#9dab86', '#e08f62', '#d7c79e'], },
                       'DarkTeal': {'BACKGROUND': '#003f5c', 'TEXT': '#fb5b5a', 'INPUT': '#bc4873', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#bc4873',
                                    'BUTTON': ('white', '#fb5b5a'),
                                    'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                    'COLOR_LIST': ['#003f5c', '#472b62', '#bc4873', '#fb5b5a'], },
                       'DarkPurple': {'BACKGROUND': '#472b62', 'TEXT': '#fb5b5a', 'INPUT': '#bc4873', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#bc4873',
                                      'BUTTON': ('#FFFFFF', '#472b62'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#003f5c', '#472b62', '#bc4873', '#fb5b5a'], },
                       'LightGreen6': {'BACKGROUND': '#eafbea', 'TEXT': '#1f6650', 'INPUT': '#6f9a8d', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#1f6650',
                                       'BUTTON': ('white', '#1f6650'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#1f6650', '#6f9a8d', '#ea5e5e', '#eafbea'], },
                       'DarkGrey2': {'BACKGROUND': '#2b2b28', 'TEXT': '#f8f8f8', 'INPUT': '#f1d6ab', 'TEXT_INPUT': '#000000', 'SCROLL': '#f1d6ab',
                                     'BUTTON': ('#2b2b28', '#e3b04b'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#2b2b28', '#e3b04b', '#f1d6ab', '#f8f8f8'], },
                       'LightBrown6': {'BACKGROUND': '#f9b282', 'TEXT': '#8f4426', 'INPUT': '#de6b35', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#8f4426',
                                       'BUTTON': ('white', '#8f4426'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#8f4426', '#de6b35', '#64ccda', '#f9b282'], },
                       'DarkTeal1': {'BACKGROUND': '#396362', 'TEXT': '#ffe7d1', 'INPUT': '#f6c89f', 'TEXT_INPUT': '#000000', 'SCROLL': '#f6c89f',
                                     'BUTTON': ('#ffe7d1', '#4b8e8d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#396362', '#4b8e8d', '#f6c89f', '#ffe7d1'], },
                       'LightBrown7': {'BACKGROUND': '#f6c89f', 'TEXT': '#396362', 'INPUT': '#4b8e8d', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#396362',
                                       'BUTTON': ('white', '#396362'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#396362', '#4b8e8d', '#f6c89f', '#ffe7d1'], },
                       'DarkPurple1': {'BACKGROUND': '#0c093c', 'TEXT': '#fad6d6', 'INPUT': '#eea5f6', 'TEXT_INPUT': '#000000', 'SCROLL': '#eea5f6',
                                       'BUTTON': ('#FFFFFF', '#df42d1'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#0c093c', '#df42d1', '#eea5f6', '#fad6d6'], },
                       'DarkGrey3': {'BACKGROUND': '#211717', 'TEXT': '#dfddc7', 'INPUT': '#f58b54', 'TEXT_INPUT': '#000000', 'SCROLL': '#f58b54',
                                     'BUTTON': ('#dfddc7', '#a34a28'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#211717', '#a34a28', '#f58b54', '#dfddc7'], },
                       'LightBrown8': {'BACKGROUND': '#dfddc7', 'TEXT': '#211717', 'INPUT': '#a34a28', 'TEXT_INPUT': '#dfddc7', 'SCROLL': '#211717',
                                       'BUTTON': ('#dfddc7', '#a34a28'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#211717', '#a34a28', '#f58b54', '#dfddc7'], },
                       'DarkBlue4': {'BACKGROUND': '#494ca2', 'TEXT': '#e3e7f1', 'INPUT': '#c6cbef', 'TEXT_INPUT': '#000000', 'SCROLL': '#c6cbef',
                                     'BUTTON': ('#FFFFFF', '#8186d5'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#494ca2', '#8186d5', '#c6cbef', '#e3e7f1'], },
                       'LightBlue4': {'BACKGROUND': '#5c94bd', 'TEXT': '#470938', 'INPUT': '#1a3e59', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#470938',
                                      'BUTTON': ('white', '#470938'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#470938', '#1a3e59', '#5c94bd', '#f2d6eb'], },
                       'DarkTeal2': {'BACKGROUND': '#394a6d', 'TEXT': '#c0ffb3', 'INPUT': '#52de97', 'TEXT_INPUT': '#000000', 'SCROLL': '#52de97',
                                     'BUTTON': ('#c0ffb3', '#394a6d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#394a6d', '#3c9d9b', '#52de97', '#c0ffb3'], },
                       'DarkTeal3': {'BACKGROUND': '#3c9d9b', 'TEXT': '#c0ffb3', 'INPUT': '#52de97', 'TEXT_INPUT': '#000000', 'SCROLL': '#52de97',
                                     'BUTTON': ('#c0ffb3', '#394a6d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#394a6d', '#3c9d9b', '#52de97', '#c0ffb3'], },
                       'DarkPurple5': {'BACKGROUND': '#730068', 'TEXT': '#f6f078', 'INPUT': '#01d28e', 'TEXT_INPUT': '#000000', 'SCROLL': '#01d28e',
                                       'BUTTON': ('#f6f078', '#730068'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#730068', '#434982', '#01d28e', '#f6f078'], },
                       'DarkPurple2': {'BACKGROUND': '#202060', 'TEXT': '#b030b0', 'INPUT': '#602080', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#602080',
                                       'BUTTON': ('white', '#202040'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#202040', '#202060', '#602080', '#b030b0'], },
                       'DarkBlue5': {'BACKGROUND': '#000272', 'TEXT': '#ff6363', 'INPUT': '#a32f80', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#a32f80',
                                     'BUTTON': ('#FFFFFF', '#341677'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#000272', '#341677', '#a32f80', '#ff6363'], },
                       'LightGrey2': {'BACKGROUND': '#f6f6f6', 'TEXT': '#420000', 'INPUT': '#d4d7dd', 'TEXT_INPUT': '#420000', 'SCROLL': '#420000',
                                      'BUTTON': ('#420000', '#d4d7dd'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#420000', '#d4d7dd', '#eae9e9', '#f6f6f6'], },
                       'LightGrey3': {'BACKGROUND': '#eae9e9', 'TEXT': '#420000', 'INPUT': '#d4d7dd', 'TEXT_INPUT': '#420000', 'SCROLL': '#420000',
                                      'BUTTON': ('#420000', '#d4d7dd'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#420000', '#d4d7dd', '#eae9e9', '#f6f6f6'], },
                       'DarkBlue6': {'BACKGROUND': '#01024e', 'TEXT': '#ff6464', 'INPUT': '#8b4367', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#8b4367',
                                     'BUTTON': ('#FFFFFF', '#543864'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#01024e', '#543864', '#8b4367', '#ff6464'], },
                       'DarkBlue7': {'BACKGROUND': '#241663', 'TEXT': '#eae7af', 'INPUT': '#a72693', 'TEXT_INPUT': '#eae7af', 'SCROLL': '#a72693',
                                     'BUTTON': ('#eae7af', '#160f30'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#160f30', '#241663', '#a72693', '#eae7af'], },
                       'LightBrown9': {'BACKGROUND': '#f6d365', 'TEXT': '#3a1f5d', 'INPUT': '#c83660', 'TEXT_INPUT': '#f6d365', 'SCROLL': '#3a1f5d',
                                       'BUTTON': ('#f6d365', '#c83660'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#3a1f5d', '#c83660', '#e15249', '#f6d365'], },
                       'DarkPurple3': {'BACKGROUND': '#6e2142', 'TEXT': '#ffd692', 'INPUT': '#e16363', 'TEXT_INPUT': '#ffd692', 'SCROLL': '#e16363',
                                       'BUTTON': ('#ffd692', '#943855'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#6e2142', '#943855', '#e16363', '#ffd692'], },
                       'LightBrown10': {'BACKGROUND': '#ffd692', 'TEXT': '#6e2142', 'INPUT': '#943855', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#6e2142',
                                        'BUTTON': ('white', '#6e2142'),
                                        'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        'COLOR_LIST': ['#6e2142', '#943855', '#e16363', '#ffd692'], },
                       'DarkPurple4': {'BACKGROUND': '#200f21', 'TEXT': '#f638dc', 'INPUT': '#5a3d5c', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#5a3d5c',
                                       'BUTTON': ('#FFFFFF', '#382039'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#200f21', '#382039', '#5a3d5c', '#f638dc'], },
                       'LightBlue5': {'BACKGROUND': '#b2fcff', 'TEXT': '#3e64ff', 'INPUT': '#5edfff', 'TEXT_INPUT': '#000000', 'SCROLL': '#3e64ff',
                                      'BUTTON': ('white', '#3e64ff'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#3e64ff', '#5edfff', '#b2fcff', '#ecfcff'], },
                       'DarkTeal4': {'BACKGROUND': '#464159', 'TEXT': '#c7f0db', 'INPUT': '#8bbabb', 'TEXT_INPUT': '#000000', 'SCROLL': '#8bbabb',
                                     'BUTTON': ('#FFFFFF', '#6c7b95'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#464159', '#6c7b95', '#8bbabb', '#c7f0db'], },
                       'LightTeal': {'BACKGROUND': '#c7f0db', 'TEXT': '#464159', 'INPUT': '#6c7b95', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#464159',
                                     'BUTTON': ('white', '#464159'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#464159', '#6c7b95', '#8bbabb', '#c7f0db'], },
                       'DarkTeal5': {'BACKGROUND': '#8bbabb', 'TEXT': '#464159', 'INPUT': '#6c7b95', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#464159',
                                     'BUTTON': ('#c7f0db', '#6c7b95'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#464159', '#6c7b95', '#8bbabb', '#c7f0db'], },
                       'LightGrey4': {'BACKGROUND': '#faf5ef', 'TEXT': '#672f2f', 'INPUT': '#99b19c', 'TEXT_INPUT': '#672f2f', 'SCROLL': '#672f2f',
                                      'BUTTON': ('#672f2f', '#99b19c'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#672f2f', '#99b19c', '#d7d1c9', '#faf5ef'], },
                       'LightGreen7': {'BACKGROUND': '#99b19c', 'TEXT': '#faf5ef', 'INPUT': '#d7d1c9', 'TEXT_INPUT': '#000000', 'SCROLL': '#d7d1c9',
                                       'BUTTON': ('#FFFFFF', '#99b19c'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#672f2f', '#99b19c', '#d7d1c9', '#faf5ef'], },
                       'LightGrey5': {'BACKGROUND': '#d7d1c9', 'TEXT': '#672f2f', 'INPUT': '#99b19c', 'TEXT_INPUT': '#672f2f', 'SCROLL': '#672f2f',
                                      'BUTTON': ('white', '#672f2f'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#672f2f', '#99b19c', '#d7d1c9', '#faf5ef'], },
                       'DarkBrown3': {'BACKGROUND': '#a0855b', 'TEXT': '#f9f6f2', 'INPUT': '#f1d6ab', 'TEXT_INPUT': '#000000', 'SCROLL': '#f1d6ab',
                                      'BUTTON': ('white', '#38470b'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#38470b', '#a0855b', '#f1d6ab', '#f9f6f2'], },
                       'LightBrown11': {'BACKGROUND': '#f1d6ab', 'TEXT': '#38470b', 'INPUT': '#a0855b', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#38470b',
                                        'BUTTON': ('#f9f6f2', '#a0855b'),
                                        'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                        'COLOR_LIST': ['#38470b', '#a0855b', '#f1d6ab', '#f9f6f2'], },
                       'DarkRed': {'BACKGROUND': '#83142c', 'TEXT': '#f9d276', 'INPUT': '#ad1d45', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#ad1d45',
                                   'BUTTON': ('#f9d276', '#ad1d45'),
                                   'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                   'COLOR_LIST': ['#44000d', '#83142c', '#ad1d45', '#f9d276'], },
                       'DarkTeal6': {'BACKGROUND': '#204969', 'TEXT': '#fff7f7', 'INPUT': '#dadada', 'TEXT_INPUT': '#000000', 'SCROLL': '#dadada',
                                     'BUTTON': ('black', '#fff7f7'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#204969', '#08ffc8', '#dadada', '#fff7f7'], },
                       'DarkBrown4': {'BACKGROUND': '#252525', 'TEXT': '#ff0000', 'INPUT': '#af0404', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#af0404',
                                      'BUTTON': ('white', '#252525'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#252525', '#414141', '#af0404', '#ff0000'], },
                       'LightYellow': {'BACKGROUND': '#f4ff61', 'TEXT': '#27aa80', 'INPUT': '#32ff6a', 'TEXT_INPUT': '#000000', 'SCROLL': '#27aa80',
                                       'BUTTON': ('#f4ff61', '#27aa80'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#27aa80', '#32ff6a', '#a8ff3e', '#f4ff61'], },
                       'DarkGreen1': {'BACKGROUND': '#2b580c', 'TEXT': '#fdef96', 'INPUT': '#f7b71d', 'TEXT_INPUT': '#000000', 'SCROLL': '#f7b71d',
                                      'BUTTON': ('#fdef96', '#2b580c'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#2b580c', '#afa939', '#f7b71d', '#fdef96'], },

                       'LightGreen8': {'BACKGROUND': '#c8dad3', 'TEXT': '#63707e', 'INPUT': '#93b5b3', 'TEXT_INPUT': '#000000', 'SCROLL': '#63707e',
                                       'BUTTON': ('white', '#63707e'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#63707e', '#93b5b3', '#c8dad3', '#f2f6f5'], },

                       'DarkTeal7': {'BACKGROUND': '#248ea9', 'TEXT': '#fafdcb', 'INPUT': '#aee7e8', 'TEXT_INPUT': '#000000', 'SCROLL': '#aee7e8',
                                     'BUTTON': ('black', '#fafdcb'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#248ea9', '#28c3d4', '#aee7e8', '#fafdcb'], },
                       'DarkBlue8': {'BACKGROUND': '#454d66', 'TEXT': '#d9d872', 'INPUT': '#58b368', 'TEXT_INPUT': '#000000', 'SCROLL': '#58b368',
                                     'BUTTON': ('black', '#009975'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#009975', '#454d66', '#58b368', '#d9d872'], },
                       'DarkBlue9': {'BACKGROUND': '#263859', 'TEXT': '#ff6768', 'INPUT': '#6b778d', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#6b778d',
                                     'BUTTON': ('#ff6768', '#263859'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#17223b', '#263859', '#6b778d', '#ff6768'], },
                       'DarkBlue10': {'BACKGROUND': '#0028ff', 'TEXT': '#f1f4df', 'INPUT': '#10eaf0', 'TEXT_INPUT': '#000000', 'SCROLL': '#10eaf0',
                                      'BUTTON': ('#f1f4df', '#24009c'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#24009c', '#0028ff', '#10eaf0', '#f1f4df'], },
                       'DarkBlue11': {'BACKGROUND': '#6384b3', 'TEXT': '#e6f0b6', 'INPUT': '#b8e9c0', 'TEXT_INPUT': '#000000', 'SCROLL': '#b8e9c0',
                                      'BUTTON': ('#e6f0b6', '#684949'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#684949', '#6384b3', '#b8e9c0', '#e6f0b6'], },

                       'DarkTeal8': {'BACKGROUND': '#71a0a5', 'TEXT': '#212121', 'INPUT': '#665c84', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#212121',
                                     'BUTTON': ('#fab95b', '#665c84'),
                                     'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                     'COLOR_LIST': ['#212121', '#665c84', '#71a0a5', '#fab95b']},
                       'DarkRed1': {'BACKGROUND': '#c10000', 'TEXT': '#eeeeee', 'INPUT': '#dedede', 'TEXT_INPUT': '#000000', 'SCROLL': '#dedede',
                                    'BUTTON': ('#c10000', '#eeeeee'),
                                    'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                    'COLOR_LIST': ['#c10000', '#ff4949', '#dedede', '#eeeeee'], },
                       'LightBrown5': {'BACKGROUND': '#fff591', 'TEXT': '#e41749', 'INPUT': '#f5587b', 'TEXT_INPUT': '#000000', 'SCROLL': '#e41749',
                                       'BUTTON': ('#fff591', '#e41749'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0, 'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#e41749', '#f5587b', '#ff8a5c', '#fff591']},
                       'LightGreen9': {'BACKGROUND': '#f1edb3', 'TEXT': '#3b503d', 'INPUT': '#4a746e', 'TEXT_INPUT': '#f1edb3', 'SCROLL': '#3b503d',
                                       'BUTTON': ('#f1edb3', '#3b503d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0,
                                       'COLOR_LIST': ['#3b503d', '#4a746e', '#c8cf94', '#f1edb3'], 'DESCRIPTION': ['Green', 'Turquoise', 'Yellow']},
                       'DarkGreen2': {'BACKGROUND': '#3b503d', 'TEXT': '#f1edb3', 'INPUT': '#c8cf94', 'TEXT_INPUT': '#000000', 'SCROLL': '#c8cf94',
                                      'BUTTON': ('#f1edb3', '#3b503d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0,
                                      'COLOR_LIST': ['#3b503d', '#4a746e', '#c8cf94', '#f1edb3'], 'DESCRIPTION': ['Green', 'Turquoise', 'Yellow']},
                       'LightGray1': {'BACKGROUND': '#f2f2f2', 'TEXT': '#222831', 'INPUT': '#393e46', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#222831',
                                      'BUTTON': ('#f2f2f2', '#222831'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#222831', '#393e46', '#f96d00', '#f2f2f2'],
                                      'DESCRIPTION': ['Black', 'Grey', 'Orange', 'Grey', 'Autumn']},
                       'DarkGrey4': {'BACKGROUND': '#52524e', 'TEXT': '#e9e9e5', 'INPUT': '#d4d6c8', 'TEXT_INPUT': '#000000', 'SCROLL': '#d4d6c8',
                                     'BUTTON': ('#FFFFFF', '#9a9b94'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#52524e', '#9a9b94', '#d4d6c8', '#e9e9e5'],
                                     'DESCRIPTION': ['Grey', 'Pastel', 'Winter']},
                       'DarkBlue12': {'BACKGROUND': '#324e7b', 'TEXT': '#f8f8f8', 'INPUT': '#86a6df', 'TEXT_INPUT': '#000000', 'SCROLL': '#86a6df',
                                      'BUTTON': ('#FFFFFF', '#5068a9'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#324e7b', '#5068a9', '#86a6df', '#f8f8f8'],
                                      'DESCRIPTION': ['Blue', 'Grey', 'Cold', 'Winter']},
                       'DarkPurple6': {'BACKGROUND': '#070739', 'TEXT': '#e1e099', 'INPUT': '#c327ab', 'TEXT_INPUT': '#e1e099', 'SCROLL': '#c327ab',
                                       'BUTTON': ('#e1e099', '#521477'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                       'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#070739', '#521477', '#c327ab', '#e1e099'],
                                       'DESCRIPTION': ['Black', 'Purple', 'Yellow', 'Dark']},
                       'DarkBlue13': {'BACKGROUND': '#203562', 'TEXT': '#e3e8f8', 'INPUT': '#c0c5cd', 'TEXT_INPUT': '#000000', 'SCROLL': '#c0c5cd',
                                      'BUTTON': ('#FFFFFF', '#3e588f'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#203562', '#3e588f', '#c0c5cd', '#e3e8f8'],
                                      'DESCRIPTION': ['Blue', 'Grey', 'Wedding', 'Cold']},
                       'DarkBrown5': {'BACKGROUND': '#3c1b1f', 'TEXT': '#f6e1b5', 'INPUT': '#e2bf81', 'TEXT_INPUT': '#000000', 'SCROLL': '#e2bf81',
                                      'BUTTON': ('#3c1b1f', '#f6e1b5'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#3c1b1f', '#b21e4b', '#e2bf81', '#f6e1b5'],
                                      'DESCRIPTION': ['Brown', 'Red', 'Yellow', 'Warm']},
                       'DarkGreen3': {'BACKGROUND': '#062121', 'TEXT': '#eeeeee', 'INPUT': '#e4dcad', 'TEXT_INPUT': '#000000', 'SCROLL': '#e4dcad',
                                      'BUTTON': ('#eeeeee', '#181810'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#062121', '#181810', '#e4dcad', '#eeeeee'],
                                      'DESCRIPTION': ['Black', 'Black', 'Brown', 'Grey']},
                       'DarkBlack1': {'BACKGROUND': '#181810', 'TEXT': '#eeeeee', 'INPUT': '#e4dcad', 'TEXT_INPUT': '#000000', 'SCROLL': '#e4dcad',
                                      'BUTTON': ('white', '#062121'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#062121', '#181810', '#e4dcad', '#eeeeee'],
                                      'DESCRIPTION': ['Black', 'Black', 'Brown', 'Grey']},
                       'DarkGrey5': {'BACKGROUND': '#343434', 'TEXT': '#f3f3f3', 'INPUT': '#e9dcbe', 'TEXT_INPUT': '#000000', 'SCROLL': '#e9dcbe',
                                     'BUTTON': ('#FFFFFF', '#8e8b82'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#343434', '#8e8b82', '#e9dcbe', '#f3f3f3'], 'DESCRIPTION': ['Grey', 'Brown']},
                       'LightBrown12': {'BACKGROUND': '#8e8b82', 'TEXT': '#f3f3f3', 'INPUT': '#e9dcbe', 'TEXT_INPUT': '#000000', 'SCROLL': '#e9dcbe',
                                        'BUTTON': ('#f3f3f3', '#8e8b82'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#343434', '#8e8b82', '#e9dcbe', '#f3f3f3'], 'DESCRIPTION': ['Grey', 'Brown']},
                       'DarkTeal9': {'BACKGROUND': '#13445a', 'TEXT': '#fef4e8', 'INPUT': '#446878', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#446878',
                                     'BUTTON': ('#fef4e8', '#446878'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#13445a', '#970747', '#446878', '#fef4e8'],
                                     'DESCRIPTION': ['Red', 'Grey', 'Blue', 'Wedding', 'Retro']},
                       'DarkBlue14': {'BACKGROUND': '#21273d', 'TEXT': '#f1f6f8', 'INPUT': '#b9d4f1', 'TEXT_INPUT': '#000000', 'SCROLL': '#b9d4f1',
                                      'BUTTON': ('#FFFFFF', '#6a759b'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#21273d', '#6a759b', '#b9d4f1', '#f1f6f8'],
                                      'DESCRIPTION': ['Blue', 'Black', 'Grey', 'Cold', 'Winter']},
                       'LightBlue6': {'BACKGROUND': '#f1f6f8', 'TEXT': '#21273d', 'INPUT': '#6a759b', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#21273d',
                                      'BUTTON': ('#f1f6f8', '#6a759b'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#21273d', '#6a759b', '#b9d4f1', '#f1f6f8'],
                                      'DESCRIPTION': ['Blue', 'Black', 'Grey', 'Cold', 'Winter']},
                       'DarkGreen4': {'BACKGROUND': '#044343', 'TEXT': '#e4e4e4', 'INPUT': '#045757', 'TEXT_INPUT': '#e4e4e4', 'SCROLL': '#045757',
                                      'BUTTON': ('#e4e4e4', '#045757'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#222222', '#044343', '#045757', '#e4e4e4'],
                                      'DESCRIPTION': ['Black', 'Turquoise', 'Grey', 'Dark']},
                       'DarkGreen5': {'BACKGROUND': '#1b4b36', 'TEXT': '#e0e7f1', 'INPUT': '#aebd77', 'TEXT_INPUT': '#000000', 'SCROLL': '#aebd77',
                                      'BUTTON': ('#FFFFFF', '#538f6a'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#1b4b36', '#538f6a', '#aebd77', '#e0e7f1'], 'DESCRIPTION': ['Green', 'Grey']},
                       'DarkTeal10': {'BACKGROUND': '#0d3446', 'TEXT': '#d8dfe2', 'INPUT': '#71adb5', 'TEXT_INPUT': '#000000', 'SCROLL': '#71adb5',
                                      'BUTTON': ('#FFFFFF', '#176d81'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#0d3446', '#176d81', '#71adb5', '#d8dfe2'],
                                      'DESCRIPTION': ['Grey', 'Turquoise', 'Winter', 'Cold']},
                       'DarkGrey6': {'BACKGROUND': '#3e3e3e', 'TEXT': '#ededed', 'INPUT': '#68868c', 'TEXT_INPUT': '#ededed', 'SCROLL': '#68868c',
                                     'BUTTON': ('#FFFFFF', '#405559'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#3e3e3e', '#405559', '#68868c', '#ededed'],
                                     'DESCRIPTION': ['Grey', 'Turquoise', 'Winter']},
                       'DarkTeal11': {'BACKGROUND': '#405559', 'TEXT': '#ededed', 'INPUT': '#68868c', 'TEXT_INPUT': '#ededed', 'SCROLL': '#68868c',
                                      'BUTTON': ('#ededed', '#68868c'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#3e3e3e', '#405559', '#68868c', '#ededed'],
                                      'DESCRIPTION': ['Grey', 'Turquoise', 'Winter']},
                       'LightBlue7': {'BACKGROUND': '#9ed0e0', 'TEXT': '#19483f', 'INPUT': '#5c868e', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#19483f',
                                      'BUTTON': ('white', '#19483f'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#19483f', '#5c868e', '#ff6a38', '#9ed0e0'],
                                      'DESCRIPTION': ['Orange', 'Blue', 'Turquoise']},
                       'LightGreen10': {'BACKGROUND': '#d8ebb5', 'TEXT': '#205d67', 'INPUT': '#639a67', 'TEXT_INPUT': '#FFFFFF', 'SCROLL': '#205d67',
                                        'BUTTON': ('#d8ebb5', '#205d67'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#205d67', '#639a67', '#d9bf77', '#d8ebb5'],
                                        'DESCRIPTION': ['Blue', 'Green', 'Brown', 'Vintage']},
                       'DarkBlue15': {'BACKGROUND': '#151680', 'TEXT': '#f1fea4', 'INPUT': '#375fc0', 'TEXT_INPUT': '#f1fea4', 'SCROLL': '#375fc0',
                                      'BUTTON': ('#f1fea4', '#1c44ac'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#151680', '#1c44ac', '#375fc0', '#f1fea4'],
                                      'DESCRIPTION': ['Blue', 'Yellow', 'Cold']},
                       'DarkBlue16': {'BACKGROUND': '#1c44ac', 'TEXT': '#f1fea4', 'INPUT': '#375fc0', 'TEXT_INPUT': '#f1fea4', 'SCROLL': '#375fc0',
                                      'BUTTON': ('#f1fea4', '#151680'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#151680', '#1c44ac', '#375fc0', '#f1fea4'],
                                      'DESCRIPTION': ['Blue', 'Yellow', 'Cold']},
                       'DarkTeal12': {'BACKGROUND': '#004a7c', 'TEXT': '#fafafa', 'INPUT': '#e8f1f5', 'TEXT_INPUT': '#000000', 'SCROLL': '#e8f1f5',
                                      'BUTTON': ('#fafafa', '#005691'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#004a7c', '#005691', '#e8f1f5', '#fafafa'],
                                      'DESCRIPTION': ['Grey', 'Blue', 'Cold', 'Winter']},
                       'LightBrown13': {'BACKGROUND': '#ebf5ee', 'TEXT': '#921224', 'INPUT': '#bdc6b8', 'TEXT_INPUT': '#921224', 'SCROLL': '#921224',
                                        'BUTTON': ('white', '#921224'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                        'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#921224', '#bdc6b8', '#bce0da', '#ebf5ee'],
                                        'DESCRIPTION': ['Red', 'Blue', 'Grey', 'Vintage', 'Wedding']},
                       'DarkBlue17': {'BACKGROUND': '#21294c', 'TEXT': '#f9f2d7', 'INPUT': '#f2dea8', 'TEXT_INPUT': '#000000', 'SCROLL': '#f2dea8',
                                      'BUTTON': ('#f9f2d7', '#141829'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#141829', '#21294c', '#f2dea8', '#f9f2d7'],
                                      'DESCRIPTION': ['Black', 'Blue', 'Yellow']},
                       'DarkBrown6': {'BACKGROUND': '#785e4d', 'TEXT': '#f2eee3', 'INPUT': '#baaf92', 'TEXT_INPUT': '#000000', 'SCROLL': '#baaf92',
                                      'BUTTON': ('white', '#785e4d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#785e4d', '#ff8426', '#baaf92', '#f2eee3'],
                                      'DESCRIPTION': ['Grey', 'Brown', 'Orange', 'Autumn']},
                       'DarkGreen6': {'BACKGROUND': '#5c715e', 'TEXT': '#f2f9f1', 'INPUT': '#ddeedf', 'TEXT_INPUT': '#000000', 'SCROLL': '#ddeedf',
                                      'BUTTON': ('#f2f9f1', '#5c715e'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#5c715e', '#b6cdbd', '#ddeedf', '#f2f9f1'],
                                      'DESCRIPTION': ['Grey', 'Green', 'Vintage']},
                       'DarkGrey7': {'BACKGROUND': '#4b586e', 'TEXT': '#dddddd', 'INPUT': '#574e6d', 'TEXT_INPUT': '#dddddd', 'SCROLL': '#574e6d',
                                     'BUTTON': ('#dddddd', '#43405d'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                     'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#43405d', '#4b586e', '#574e6d', '#dddddd'],
                                     'DESCRIPTION': ['Grey', 'Winter', 'Cold']},
                       'DarkRed2': {'BACKGROUND': '#ab1212', 'TEXT': '#f6e4b5', 'INPUT': '#cd3131', 'TEXT_INPUT': '#f6e4b5', 'SCROLL': '#cd3131',
                                    'BUTTON': ('#f6e4b5', '#ab1212'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                    'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#ab1212', '#1fad9f', '#cd3131', '#f6e4b5'],
                                    'DESCRIPTION': ['Turquoise', 'Red', 'Yellow']},
                       'LightGrey6': {'BACKGROUND': '#e3e3e3', 'TEXT': '#233142', 'INPUT': '#455d7a', 'TEXT_INPUT': '#e3e3e3', 'SCROLL': '#233142',
                                      'BUTTON': ('#e3e3e3', '#455d7a'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0, 'COLOR_LIST': ['#233142', '#455d7a', '#f95959', '#e3e3e3'],
                                      'DESCRIPTION': ['Black', 'Blue', 'Red', 'Grey']},
                       'HotDogStand': {'BACKGROUND': 'red', 'TEXT': 'yellow', 'INPUT': 'yellow', 'TEXT_INPUT': 'black', 'SCROLL': 'yellow',
                                      'BUTTON': ('red', 'yellow'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                      'PROGRESS_DEPTH': 0,
                                     },
                       }


def ListOfLookAndFeelValues():
    """
    Get a list of the valid values to pass into your call to change_look_and_feel
    :return: List[str] - list of valid string values
    """
    return sorted(list(LOOK_AND_FEEL_TABLE.keys()))


def theme(new_theme=None):
    """
    Sets / Gets the current Theme.  If none is specified then returns the current theme.
    This call replaces the ChangeLookAndFeel / change_look_and_feel call which only sets the theme.

    :param new_theme: (str) the new theme name to use
    :return: (str) the currently selected theme
    """
    if new_theme is not None:
        change_look_and_feel(new_theme)
    return CURRENT_LOOK_AND_FEEL


def theme_background_color(color=None):
    """
    Sets/Returns the background color currently in use
    Used for Windows and containers (Column, Frame, Tab) and tables

    :return: (str) - color string of the background color currently in use
    """
    if color is not None:
        set_options(background_color=color)
    return DEFAULT_BACKGROUND_COLOR


def theme_element_background_color(color=None):
    """
    Sets/Returns the background color currently in use for all elements except containers

    :return: (str) - color string of the element background color currently in use
    """
    if color is not None:
        set_options(element_background_color=color)
    return DEFAULT_ELEMENT_BACKGROUND_COLOR


def theme_text_color(color=None):
    """
    Sets/Returns the text color currently in use

    :return: (str) - color string of the text color currently in use
    """
    if color is not None:
        set_options(text_color=color)
    return DEFAULT_TEXT_COLOR



def theme_input_background_color(color=None):
    """
    Sets/Returns the input element background color currently in use

    :return: (str) - color string of the input element background color currently in use
    """
    if color is not None:
        set_options(input_elements_background_color=color)
    return DEFAULT_INPUT_ELEMENTS_COLOR


def theme_input_text_color(color=None):
    """
    Sets/Returns the input element entry color (not the text but the thing that's displaying the text)

    :return: (str) - color string of the input element color currently in use
    """
    if color is not None:
        set_options(input_text_color=color)
    return DEFAULT_INPUT_TEXT_COLOR



def theme_button_color(color=None):
    """
    Sets/Returns the button color currently in use

    :return: Tuple[str, str] - TUPLE with color strings of the button color currently in use (button text color, button background color)
    """
    if color is not None:
        set_options(button_color=color)
    return DEFAULT_BUTTON_COLOR


def theme_progress_bar_color(color=None):
    """
    Sets/Returns the progress bar colors by the current color theme

    :return: Tuple[str, str] - TUPLE with color strings of the ProgressBar color currently in use(button text color, button background color)
    """
    if color is not None:
        set_options(progress_meter_color=color)
    return DEFAULT_PROGRESS_BAR_COLOR


def theme_slider_color(color=None):
    """
    Sets/Returns the slider color (used for sliders)

    :return: (str) - color string of the slider color currently in use
    """
    if color is not None:
        set_options(scrollbar_color=color)
    return DEFAULT_SCROLLBAR_COLOR


def theme_border_width(border_width=None):
    """
    Sets/Returns the border width currently in use
    Used by non ttk elements at the moment

    :return: (int) - border width currently in use
    """
    if border_width is not None:
        set_options(border_width=border_width)
    return DEFAULT_BORDER_WIDTH


def theme_slider_border_width(border_width=None):
    """
    Sets/Returns the slider border width currently in use

    :return: (int) - border width currently in use
    """
    if border_width is not None:
        set_options(slider_border_width=border_width)
    return DEFAULT_SLIDER_BORDER_WIDTH


def theme_progress_bar_border_width(border_width=None):
    """
    Sets/Returns the progress meter border width currently in use

    :return: (int) - border width currently in use
    """
    if border_width is not None:
        set_options(progress_meter_border_depth=border_width)
    return DEFAULT_PROGRESS_BAR_BORDER_WIDTH



def theme_element_text_color(color=None):
    """
    Sets/Returns the text color used by elements that have text as part of their display (Tables, Trees and Sliders)

    :return: (str) - color string currently in use
    """
    if color is not None:
        set_options(element_text_color=color)
    return DEFAULT_ELEMENT_TEXT_COLOR


def theme_list():
    """
    Returns a sorted list of the currently available color themes

    :return: List[str] - A sorted list of the currently available color themes
    """
    return list_of_look_and_feel_values()



def theme_add_new(new_theme_name, new_theme_dict):
    """
    Add a new theme to the dictionary of themes

    :param new_theme_name: text to display in element
    :type new_theme_name: (str)
    :param new_theme_dict: text to display in element
    :type new_theme_dict: (dict)
    """
    global LOOK_AND_FEEL_TABLE
    try:
        LOOK_AND_FEEL_TABLE[new_theme_name] = new_theme_dict
    except Exception as e:
        print('Exception during adding new theme {}'.format(e))




def theme_previewer(columns=12):
    """
    Show a window with all of the color themes - takes a while so be patient

    :param columns: (int) number of themes in a single row
    """
    preview_all_look_and_feel_themes(columns)

def ChangeLookAndFeel(index, force=False):
    """
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
    :param index: the name of the index into the Look and Feel table (does not have to be exact, can be "fuzzy")
    :type index: (str)
    :param force: no longer used
    :type force: (bool)
    """

    global CURRENT_LOOK_AND_FEEL

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
        ix = random.random.randint(0, len(lf_values) - 1)
        print('** Warning - {} Theme is not a valid theme. Change your theme call. **'.format(index))
        print('valid values are', list_of_look_and_feel_values())
        print('Instead, please enjoy a random Theme named {}'.format(list_of_look_and_feel_values()[ix]))

    selection = list_of_look_and_feel_values()[ix]
    CURRENT_LOOK_AND_FEEL = selection
    try:
        colors = LOOK_AND_FEEL_TABLE[selection]

        # Color the progress bar using button background and input colors...unless they're the same
        if colors['PROGRESS'] != COLOR_SYSTEM_DEFAULT:
            if colors['BUTTON'][1] != colors['INPUT'] and colors['BUTTON'][1] != colors['BACKGROUND']:
                colors['PROGRESS'] = colors['BUTTON'][1], colors['INPUT']
            else:  # if the same, then use text input on top of input color
                colors['PROGRESS'] = (colors['TEXT_INPUT'], colors['INPUT'])
        else:
            colors['PROGRESS'] = DEFAULT_PROGRESS_BAR_COLOR_OFFICIAL
        # call to change all the colors
        SetOptions(background_color=colors['BACKGROUND'],
                   text_element_background_color=colors['BACKGROUND'],
                   element_background_color=colors['BACKGROUND'],
                   text_color=colors['TEXT'],
                   input_elements_background_color=colors['INPUT'],
                   # button_color=colors['BUTTON'] if not sys.platform.startswith('darwin') else None,
                   button_color=colors['BUTTON'],
                   progress_meter_color=colors['PROGRESS'],
                   border_width=colors['BORDER'],
                   slider_border_width=colors['SLIDER_DEPTH'],
                   progress_meter_border_depth=colors['PROGRESS_DEPTH'],
                   scrollbar_color=(colors['SCROLL']),
                   element_text_color=colors['TEXT'],
                   input_text_color=colors['TEXT_INPUT'])
    except:  # most likely an index out of range
        print('** Warning - Theme value not valid. Change your theme call. **')
        print('valid values are', list_of_look_and_feel_values())



def preview_all_look_and_feel_themes(columns=12):
    """
    Displays a "Quick Reference Window" showing all of the different Look and Feel settings that are available.
    They are sorted alphabetically.  The legacy color names are mixed in, but otherwise they are sorted into Dark and Light halves
    :param columns: (int) The number of themes to display per row
    """

    # Show a "splash" type message so the user doesn't give up waiting
    popup_quick_message('Hang on for a moment, this will take a bit to create....', background_color='red', text_color='white', auto_close=True, non_blocking=True)

    web = False

    win_bg = 'black'

    def sample_layout():
        return [[Text('Text element'), InputText('Input data here', size=(10, 1))],
                [Button('Ok'), Button('Cancel'), Slider((1, 10), orientation='h', size=(5, 15))]]

    layout = [[Text('Here is a complete list of themes', font='Default 18', background_color=win_bg)]]

    names = list_of_look_and_feel_values()
    names.sort()
    row = []
    for count, theme in enumerate(names):
        change_look_and_feel(theme)
        if not count % columns:
            layout += [row]
            row = []
        row += [Frame(theme, sample_layout() if not web else [[T(theme)]] + sample_layout())]
    if row:
        layout += [row]

    window = Window('Preview of all Look and Feel choices', layout, background_color=win_bg)
    window.read()
    window.close()


# ============================== sprint ======#
# Is identical to the Scrolled Text Box       #
# Provides a crude 'print' mechanism but in a #
# GUI environment                             #
# ============================================#
sprint = ScrolledTextBox


# Converts an object's contents into a nice printable string.  Great for dumping debug data
def ObjToStringSingleObj(obj):
    """
    Dumps an Object's values as a formatted string.  Very nicely done. Great way to display an object's member variables in human form
    Returns only the top-most object's variables instead of drilling down to dispolay more
    :param obj: The object to display
    :type obj: (Any)
    :return: Formatted output of the object's values
    :rtype: (str)
    """
    if obj is None:
        return 'None'
    return str(obj.__class__) + '\n' + '\n'.join(
        (repr(item) + ' = ' + repr(obj.__dict__[item]) for item in sorted(obj.__dict__)))


def ObjToString(obj, extra='    '):
    """
    Dumps an Object's values as a formatted string.  Very nicely done. Great way to display an object's member variables in human form
    :param obj: The object to display
    :type obj: (Any)
    :param extra: extra stuff (Default value = '    ')
    :type extra: (str)
    :return:  Formatted output of the object's values
    :rtype: (str)
    """
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

def Popup(*args, title=None, button_color=None, background_color=None, text_color=None, button_type=POPUP_BUTTONS_OK,
          auto_close=False, auto_close_duration=None, custom_text=(None, None), non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None,
          font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None), any_key_closes=False, image=None):
    """
    Popup - Display a popup box with as many parms as you wish to include
    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param title: Optional title for the window. If none provided, the first arg will be used instead.
    :type title: (str)
    :param button_color: Color of the buttons shown (text color, button color)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param button_type: NOT USER SET!  Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK). There are many Popup functions and they call Popup, changing this parameter to get the desired effect.
    :type button_type: (int)
    :param auto_close: If True the window will automatically close
    :type auto_close: (bool)
    :param auto_close_duration: time in seconds to keep window open before closing it automatically
    :type auto_close_duration: (int)
    :param custom_text: A string or pair of strings that contain the text to display on the buttons
    :type custom_text: Union[Tuple[str, str], str]
    :param non_blocking: If True then will immediately return from the function without waiting for the user's input.
    :type non_blocking: (bool)
    :param icon: icon to display on the window. Same format as a Window call
    :type icon: Union[str, bytes]
    :param line_width: Width of lines in characters.  Defaults to MESSAGE_BOX_LINE_WIDTH
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location on screen to display the top left corner of window. Defaults to window centered on screen
    :type location: Tuple[int, int]
    :param any_key_closes: If True then will turn on return_keyboard_events for the window which will cause window to close as soon as any key is pressed.  Normally the return key only will close the window.  Default is false.
    :type any_key_closes: (bool)
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    :return: Returns text of the button that was pressed.  None will be returned if user closed window with X
    :rtype: Union[str, None]
    """

    if not args:
        args_to_print = ['']
    else:
        args_to_print = args
    if line_width != None:
        local_line_width = line_width
    else:
        local_line_width = MESSAGE_BOX_LINE_WIDTH

    _title = title if title is not None else args_to_print[0]
    _title = str(_title)
    window = Window(_title, auto_size_text=True, background_color=background_color, button_color=button_color,
                    auto_close=auto_close, auto_close_duration=auto_close_duration, icon=icon, font=font,
                    no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location,
                    return_keyboard_events=any_key_closes)
    max_line_total, total_lines = 0, 0
    layout = [[]]
    if image is not None:
        if isinstance(image, str):
            layout += [[Image(filename=image)]]
        else:
            layout += [[Image(data_base64=image)]]

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
        layout.append([Text(message_wrapped, auto_size_text=True, text_color=text_color, background_color=background_color)])
        total_lines += height

    # if total_lines < 3:
    #     layout.append([Text('',text_color=text_color, background_color=background_color)])
    if non_blocking:
        PopupButton = DummyButton  # important to use or else button will close other windows too!
    else:
        PopupButton = Button
    # show either an OK or Yes/No depending on paramater
    # show either an OK or Yes/No depending on paramater
    if custom_text != (None, None):
        if type(custom_text) is not tuple:
            layout.append([PopupButton(custom_text, button_color=button_color, focus=True, bind_return_key=True)])
        elif custom_text[1] is None:
            layout.append([PopupButton(custom_text[0], button_color=button_color, focus=True, bind_return_key=True)])
        else:
            layout.append([PopupButton(custom_text[0], button_color=button_color, focus=True, bind_return_key=True),
                          PopupButton(custom_text[1], button_color=button_color),Stretch()])
    elif button_type is POPUP_BUTTONS_YES_NO:
        layout.append([PopupButton('Yes', button_color=button_color, focus=True, bind_return_key=True, size=(60, 20)), PopupButton('No', button_color=button_color, size=(60, 20))])
    elif button_type is POPUP_BUTTONS_CANCELLED:
        layout.append([PopupButton('Cancelled', button_color=button_color, focus=True, bind_return_key=True), Stretch()])
    elif button_type is POPUP_BUTTONS_ERROR:
        layout.append([PopupButton('Error', size=(60, 20), button_color=button_color, focus=True, bind_return_key=True), Stretch()])
    elif button_type is POPUP_BUTTONS_OK_CANCEL:
        layout.append([PopupButton('OK', size=(60, 20), button_color=button_color, focus=True, bind_return_key=True),
                      PopupButton('Cancel', size=(60, 20), button_color=button_color), Stretch()])
    elif button_type is POPUP_BUTTONS_NO_BUTTONS:
        pass
    else:
        layout.append([PopupButton('OK', size=(60, 20), button_color=button_color, focus=True, bind_return_key=True), Stretch()])

    window.Layout(layout)
    if non_blocking:
        button, values = window.Read(timeout=0)
        Window.active_popups[window] = title
    else:
        button, values = window.Read()
        window.close()

    return button


# ==============================  MsgBox============#
# Lazy function. Same as calling Popup with parms   #
# This function WILL Disappear perhaps today        #
# ==================================================#
# MsgBox is the legacy call and should not be used any longer
def MsgBox(*args):
    raise DeprecationWarning('MsgBox is no longer supported... change your call to Popup')


# --------------------------- PopupNoButtons ---------------------------
def PopupNoButtons(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
                   auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
                   no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None), image=None):
    """
    Show a Popup but without any buttons
    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    """
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=POPUP_BUTTONS_NO_BUTTONS,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location, image=image)


# --------------------------- PopupNonBlocking ---------------------------
def PopupNonBlocking(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
                     auto_close=False, auto_close_duration=None, non_blocking=True, icon=DEFAULT_WINDOW_ICON,
                     line_width=None, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False,
                     location=(None, None), image=None):
    """
        Show Popup box and immediately return (does not block)
    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_type:
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    """
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location, image=image)


PopupNoWait = PopupNonBlocking


# --------------------------- PopupQuick - a NonBlocking, Self-closing Popup  ---------------------------
def PopupQuick(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
               auto_close=True, auto_close_duration=2, non_blocking=True, icon=DEFAULT_WINDOW_ICON, line_width=None,
               font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None), image=None):
    """
        Show Popup box that doesn't block and closes itself
    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_type: Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK).
    :type button_type: (int)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    """
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location, image=image)


# --------------------------- PopupQuick - a NonBlocking, Self-closing Popup with no titlebar and no buttons ---------------------------
def PopupQuickMessage(*args, title=None, button_type=POPUP_BUTTONS_NO_BUTTONS, button_color=None, background_color=None,
                      text_color=None,
                      auto_close=True, auto_close_duration=3, non_blocking=True, icon=DEFAULT_WINDOW_ICON,
                      line_width=None,
                      font=None, no_titlebar=True, grab_anywhere=False, keep_on_top=False, location=(None, None), image=None):
    """
        Show Popup box that doesn't block and closes itself
    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_type: Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK).
    :type button_type: (int)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    """
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location, image=image)


# --------------------------- PopupNoTitlebar ---------------------------
def PopupNoTitlebar(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
                    auto_close=False, auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON,
                    line_width=None, font=None, grab_anywhere=True, keep_on_top=False, location=(None, None), image=None):
    """
        Display a Popup without a titlebar.   Enables grab anywhere so you can move it
    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_type: Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK).
    :type button_type: (int)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    """
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=True, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location, image=image)


PopupNoFrame = PopupNoTitlebar
PopupNoBorder = PopupNoTitlebar
PopupAnnoying = PopupNoTitlebar


# --------------------------- PopupAutoClose ---------------------------
def PopupAutoClose(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
                   auto_close=True, auto_close_duration=DEFAULT_AUTOCLOSE_TIME, non_blocking=False, icon=DEFAULT_WINDOW_ICON,
                   line_width=None, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False,
                   location=(None, None), image=None):
    """
        Popup that closes itself after some time period
    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_type: Determines which pre-defined buttons will be shown (Default value = POPUP_BUTTONS_OK).
    :type button_type: (int)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    """
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location, image=image)


PopupTimed = PopupAutoClose


# --------------------------- PopupError ---------------------------
def PopupError(*args, title=None, button_color=(None, None), background_color=None, text_color=None, auto_close=False,
               auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
               no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None), image=None):
    """
        Popup with colored button and 'Error' as button text
    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    """
    tbutton_color = DEFAULT_ERROR_BUTTON_COLOR if button_color == (None, None) else button_color
    Popup(*args, title=title, button_type=POPUP_BUTTONS_ERROR, background_color=background_color, text_color=text_color,
          non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=tbutton_color, auto_close=auto_close,
          auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
          keep_on_top=keep_on_top, location=location, image=image)


# --------------------------- PopupCancel ---------------------------
def PopupCancel(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
                auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
                no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None), image=None):
    """
        Display Popup with "cancelled" button text
    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param title: Title to display in the window.
    :type title: (str)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    """
    Popup(*args, title=title, button_type=POPUP_BUTTONS_CANCELLED, background_color=background_color, text_color=text_color,
          non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color, auto_close=auto_close,
          auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
          keep_on_top=keep_on_top, location=location, image=image)


# --------------------------- PopupOK ---------------------------
def PopupOK(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
            auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
            no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
    Display Popup with OK button only
    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    """
    Popup(*args, title=title, button_type=POPUP_BUTTONS_OK, background_color=background_color, text_color=text_color,
          non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color, auto_close=auto_close,
          auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
          keep_on_top=keep_on_top, location=location, image=image)


# --------------------------- PopupOKCancel ---------------------------
def PopupOKCancel(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
                  auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
                  no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None), image=None):
    """
    Display popup with OK and Cancel buttons
    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    :return: OK, Cancel or None
    :rtype: Union[str, None]
    """
    return Popup(*args, title=title, button_type=POPUP_BUTTONS_OK_CANCEL, background_color=background_color, text_color=text_color,
                 non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color,
                 auto_close=auto_close, auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar,
                 grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location, image=image)


# --------------------------- PopupYesNo ---------------------------
def PopupYesNo(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
               auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
               no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None), image=None):
    """
    Display Popup with Yes and No buttons

    :param *args:  Variable number of your arguments.  Load up the call with stuff to see!
    :type *args: (Any)
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param auto_close: if True window will close itself
    :type auto_close: (bool)
    :param auto_close_duration: Older versions only accept int. Time in seconds until window will close
    :type auto_close_duration: Union[int, float]
    :param non_blocking: if True the call will immediately return rather than waiting on user input
    :type non_blocking: (bool)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param line_width: Width of lines in characters
    :type line_width: (int)
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    :return: Yes, No or None
    :rtype: Union[str, None]
    """
    return Popup(*args, title=title, button_type=POPUP_BUTTONS_YES_NO, background_color=background_color, text_color=text_color,
                 non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color,
                 auto_close=auto_close, auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar,
                 grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location, image=image)


##############################################################################
#   The PopupGet_____ functions - Will return user input                     #
##############################################################################

# --------------------------- PopupGetFolder ---------------------------


def PopupGetFolder(message, title=None, default_path='', no_window=False, size=(None, None), button_color=None,
                   background_color=None, text_color=None, icon=DEFAULT_WINDOW_ICON, font=None, no_titlebar=False,
                   grab_anywhere=False, keep_on_top=False, location=(None, None), initial_folder=None, image=None):
    """
    Display popup with text entry field and browse button. Browse for folder
    :param message: message displayed to user
    :type message: (str)
    :param title: Window title
    :type title: (str)
    :param default_path: path to display to user as starting point (filled into the input field)
    :type default_path: (str)
    :param no_window: if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown
    :type no_window: (bool)
    :param size: (width, height) of the InputText Element
    :type size: Tuple[int, int]
    :param button_color: button color (foreground, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param initial_folder: location in filesystem to begin browsing
    :type initial_folder: (str)
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    :return: Contents of text field. None if closed using X or cancelled
    :rtype: Union[str, None]
    """


    if no_window:
        if Window.QTApplication is None:
            Window.QTApplication = QApplication(sys.argv)

        folder_name = QFileDialog.getExistingDirectory(dir=initial_folder)
        return folder_name

    if image is not None:
        if isinstance(image, str):
            layout = [[Image(filename=image)]]
        else:
            layout = [[Image(data_base64=image)]]
    else:
        layout = [[]]
    layout += [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=size, key='_INPUT_'), FolderBrowse(initial_folder=initial_folder)],
              [Button('Ok', size=(60, 20), bind_return_key=True), Button('Cancel', size=(60, 20))]]

    _title = title if title is not None else message
    window = Window(title=_title, layout=layout, icon=icon, auto_size_text=True, button_color=button_color,
                    background_color=background_color,
                    font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    button, values = window.Read()
    window.close()
    if button != 'Ok':
        return None
    else:
        path = values['_INPUT_']
        return path


# --------------------------- PopupGetFile ---------------------------

def PopupGetFile(message, title=None, default_path='', default_extension='', save_as=False, file_types=(("ALL Files", "*"),),
                 no_window=False, size=(None, None), button_color=None, background_color=None, text_color=None,
                 icon=DEFAULT_WINDOW_ICON, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False,
                 location=(None, None), initial_folder=None, image=None):
    """
        Display popup with text entry field and browse button. Browse for file

    :param message: message displayed to user
    :type message: (str)
    :param title: Window title
    :type title: (str)
    :param default_path: path to display to user as starting point (filled into the input field)
    :type default_path: (str)
    :param default_extension: If no extension entered by user, add this to filename (only used in saveas dialogs)
    :type default_extension: (str)
    :param save_as: if True, the "save as" dialog is shown which will verify before overwriting
    :type save_as: (bool)
    :param multiple_files: if True, then allows multiple files to be selected that are returned with ';' between each filename
    :type multiple_files: (bool)
    :param file_types: List of extensions to show using wildcards. All files (the default) = (("ALL Files", "*.*"),)
    :type file_types: Tuple[Tuple[str,str]]
    :param no_window: if True, no PySimpleGUI window will be shown. Instead just the tkinter dialog is shown
    :type no_window: (bool)
    :param size: (width, height) of the InputText Element
    :type size: Tuple[int, int]
    :param button_color: Color of the button (text, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param font:  specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top:  If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: Location of upper left corner of the window
    :type location: Tuple[int, int]
    :param initial_folder: location in filesystem to begin browsing
    :type initial_folder: (str)
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    :return:  string representing the path chosen, None if cancelled or window closed with X
    :rtype: Union[str, None]
    """

    if no_window:
        if Window.QTApplication is None:
            Window.QTApplication = QApplication(sys.argv)

        if save_as:
            qt_types = convert_tkinter_filetypes_to_qt(file_types)
            filename = QFileDialog.getSaveFileName(dir=initial_folder, filter=qt_types)
        else:
            qt_types = convert_tkinter_filetypes_to_qt(file_types)
            filename = QFileDialog.getOpenFileName(dir=initial_folder, filter=qt_types)
        return filename[0]


    browse_button = SaveAs(file_types=file_types, initial_folder=initial_folder) if save_as else FileBrowse(
        file_types=file_types, initial_folder=initial_folder)


    if image is not None:
        if isinstance(image, str):
            layout = [[Image(filename=image)]]
        else:
            layout = [[Image(data_base64=image)]]
    else:
        layout = [[]]

    layout += [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=(30,1), key='_INPUT_'), browse_button],
              [Button('Ok', size=(60, 20), bind_return_key=True), Button('Cancel', size=(60, 20))]]

    _title = title if title is not None else message

    window = Window(title=_title, layout=layout, icon=icon, auto_size_text=True, button_color=button_color, font=font,
                    background_color=background_color,
                    no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)

    button, values = window.Read()
    window.close()
    if button != 'Ok':
        return None
    else:
        path = values['_INPUT_']
        return path


# --------------------------- PopupGetText ---------------------------

def PopupGetText(message, title=None, default_text='', password_char='', size=(None, None), button_color=None,
                 background_color=None, text_color=None, icon=DEFAULT_WINDOW_ICON, font=None, no_titlebar=False,
                 grab_anywhere=False, keep_on_top=False, location=(None, None), image=None):
    """
    Display Popup with text entry field
    :param message: message displayed to user
    :type message: (str)
    :param title: Window title
    :type title: (str)
    :param default_text: default value to put into input area
    :type default_text: (str)
    :param password_char: character to be shown instead of actually typed characters
    :type password_char: (str)
    :param size: (width, height) of the InputText Element
    :type size: Tuple[int, int]
    :param button_color: Color of the button (text, background)
    :type button_color: Tuple[str, str]
    :param background_color: color of background
    :type background_color: (str)
    :param text_color: color of the text
    :type text_color: (str)
    :param icon: filename or base64 string to be used for the window's icon
    :type icon: Union[bytes, str]
    :param font: specifies the font family, size, etc
    :type font: Union[str, Tuple[str, int]]
    :param no_titlebar: If True no titlebar will be shown
    :type no_titlebar: (bool)
    :param grab_anywhere: If True, than can grab anywhere to move the window (Default = False)
    :type grab_anywhere: (bool)
    :param keep_on_top: If True the window will remain above all current windows
    :type keep_on_top: (bool)
    :param location: (x,y) Location on screen to display the upper left corner of window
    :type location: Tuple[int, int]
    :param image:  Image to include at the top of the popup window
    :type image: (str) or (bytes)
    :return: Text entered or None if window was closed
    :rtype: Union[str, None]
    """

    if image is not None:
        if isinstance(image, str):
            layout = [[Image(filename=image)]]
        else:
            layout = [[Image(data_base64=image)]]
    else:
        layout = [[]]

    layout += [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color, font=font)],
              [InputText(default_text=default_text, size=size, password_char=password_char, key='_INPUT_')],
              [Button('Ok', size=(60, 20), bind_return_key=True), Button('Cancel', size=(60, 20))]]

    _title = title if title is not None else message

    window = Window(title=_title, layout=layout, icon=icon, auto_size_text=True, button_color=button_color, no_titlebar=no_titlebar,
                    background_color=background_color, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    button, values = window.Read()
    window.close()

    if button != 'Ok':
        return None
    else:
        return values['_INPUT_']


# --------------------------------------- a few icons in base64 ---------------------------------------


ICON_BASE64_BLOB_PALM = b'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/GMzLdsAADpCaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjIzMTksIDIwMTgvMDIvMTUtMjA6Mjk6NDMgICAgICAgICI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICAgICAgICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iPgogICAgICAgICA8eG1wOkNyZWF0b3JUb29sPkFkb2JlIFBob3Rvc2hvcCBFbGVtZW50cyAxNy4wIChXaW5kb3dzKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAyMC0wNy0wMlQxNjo1ODowNy0wNDowMDwveG1wOkNyZWF0ZURhdGU+CiAgICAgICAgIDx4bXA6TWV0YWRhdGFEYXRlPjIwMjAtMDctMDJUMTY6NTg6MDctMDQ6MDA8L3htcDpNZXRhZGF0YURhdGU+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDIwLTA3LTAyVDE2OjU4OjA3LTA0OjAwPC94bXA6TW9kaWZ5RGF0ZT4KICAgICAgICAgPHhtcE1NOkluc3RhbmNlSUQ+eG1wLmlpZDo4NWFmYzM1My1hMzMyLWFlNGQtOGE0ZC1lYTExOTk1MDU5M2E8L3htcE1NOkluc3RhbmNlSUQ+CiAgICAgICAgIDx4bXBNTTpEb2N1bWVudElEPmFkb2JlOmRvY2lkOnBob3Rvc2hvcDpiMWM2N2U0Zi1iY2E2LTExZWEtYTEwYi1iMTlmYTMxNTc1YWQ8L3htcE1NOkRvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+eG1wLmRpZDphNzVkMDNmMS1lNjE3LWM0NDktYjYxNy0zZjc4YWFjMDBjNTQ8L3htcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkhpc3Rvcnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5jcmVhdGVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6YTc1ZDAzZjEtZTYxNy1jNDQ5LWI2MTctM2Y3OGFhYzAwYzU0PC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDIwLTA3LTAyVDE2OjU4OjA3LTA0OjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6c29mdHdhcmVBZ2VudD5BZG9iZSBQaG90b3Nob3AgRWxlbWVudHMgMTcuMCAoV2luZG93cyk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOjg1YWZjMzUzLWEzMzItYWU0ZC04YTRkLWVhMTE5OTUwNTkzYTwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAyMC0wNy0wMlQxNjo1ODowNy0wNDowMDwvc3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIEVsZW1lbnRzIDE3LjAgKFdpbmRvd3MpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2UvcG5nPC9kYzpmb3JtYXQ+CiAgICAgICAgIDxwaG90b3Nob3A6Q29sb3JNb2RlPjM8L3Bob3Rvc2hvcDpDb2xvck1vZGU+CiAgICAgICAgIDxwaG90b3Nob3A6SUNDUHJvZmlsZT5zUkdCIElFQzYxOTY2LTIuMTwvcGhvdG9zaG9wOklDQ1Byb2ZpbGU+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjc4PC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjcxPC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz62g3pFAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAABdqSURBVHja7Jz3c1xXlt+/5977cucANCKRmINAShoqzYxGOzsu79Ta/g/8L/kvsctll721nl1b3t1ZaShRFClRgkiQIAgih250eOkG/9ANEgRBECABSa7Sq+p6XQQL7+LzTj73XDLG4Jfr6Jf4uSxk+tp1Osr/v3Xz85/0jdNPJXF7QNFL7vtdZr/7jw3yRwe3CxgBYLvuvHff+U57AJreRwHQvc/Od7Pr/qNA/FHA7QOLARCcGcvi2rGFcYUwnmtpx3OUF7jacS3NLaE5Z4YBQCKZjlOWhDFL2xEP45RFiaQokRSnkkVKU6INyd0wTxLgiYPrQdsBZtlC24Gr/Jwvc/lAFfK+rOZ9Wcr6shy4qpBxVTbwlO9Yxu6BEzCQiWRIUpaECQvbIe+0It5sRXy9GfKNRlusNjpic7stGs1QtDoJ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'

ICON_BASE64_BLOB_PAT = b'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/GMzLdsAADpCaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjIzMTksIDIwMTgvMDIvMTUtMjA6Mjk6NDMgICAgICAgICI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICAgICAgICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iPgogICAgICAgICA8eG1wOkNyZWF0b3JUb29sPkFkb2JlIFBob3Rvc2hvcCBFbGVtZW50cyAxNy4wIChXaW5kb3dzKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAyMC0wNy0wMlQxNjo1OTowNi0wNDowMDwveG1wOkNyZWF0ZURhdGU+CiAgICAgICAgIDx4bXA6TWV0YWRhdGFEYXRlPjIwMjAtMDctMDJUMTY6NTk6MDYtMDQ6MDA8L3htcDpNZXRhZGF0YURhdGU+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDIwLTA3LTAyVDE2OjU5OjA2LTA0OjAwPC94bXA6TW9kaWZ5RGF0ZT4KICAgICAgICAgPHhtcE1NOkluc3RhbmNlSUQ+eG1wLmlpZDpiMWNmNDU1YS04Yjk4LTFmNDYtYmJlNi1iNmY1ZGMxMGYwYWE8L3htcE1NOkluc3RhbmNlSUQ+CiAgICAgICAgIDx4bXBNTTpEb2N1bWVudElEPmFkb2JlOmRvY2lkOnBob3Rvc2hvcDpkM2FmN2UyNi1iY2E2LTExZWEtYTEwYi1iMTlmYTMxNTc1YWQ8L3htcE1NOkRvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+eG1wLmRpZDo0YjE4ZTE1Mi0yNWMzLWY3NDAtOWU4Yi0zYmRjNjFjMjI5Njk8L3htcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkhpc3Rvcnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5jcmVhdGVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6NGIxOGUxNTItMjVjMy1mNzQwLTllOGItM2JkYzYxYzIyOTY5PC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDIwLTA3LTAyVDE2OjU5OjA2LTA0OjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6c29mdHdhcmVBZ2VudD5BZG9iZSBQaG90b3Nob3AgRWxlbWVudHMgMTcuMCAoV2luZG93cyk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOmIxY2Y0NTVhLThiOTgtMWY0Ni1iYmU2LWI2ZjVkYzEwZjBhYTwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAyMC0wNy0wMlQxNjo1OTowNi0wNDowMDwvc3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIEVsZW1lbnRzIDE3LjAgKFdpbmRvd3MpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2UvcG5nPC9kYzpmb3JtYXQ+CiAgICAgICAgIDxwaG90b3Nob3A6Q29sb3JNb2RlPjM8L3Bob3Rvc2hvcDpDb2xvck1vZGU+CiAgICAgICAgIDxwaG90b3Nob3A6SUNDUHJvZmlsZT5zUkdCIElFQzYxOTY2LTIuMTwvcGhvdG9zaG9wOklDQ1Byb2ZpbGU+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjgxPC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjc1PC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz6vCsFxAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAABGmSURBVHja7Jx5cJzlfce/z/Meex+SdqWVVpdZWbIlY1lWjIhx42ZIYopT7jFgDCZOAy2QozChSWaShjQpAylkmhCaGHAHN5hjCuWoaaEl0A50SsHGMpaNbQlfyJZk3Vrtvsdz9I93dfpaW7vGJnpmdnTs7rvv+3l/9+/3LJFSYnbNbNFZBLMQZyHOQpxdsxBnIc5CnIU4u46z1PP55Fdf0eiPhXlzUUA0+D2yRFWEX0rCLIbRlEF6+5NKW++w0rbxxdbefJ4HOV8zlrvXNly6amnyPwu8Al5dQFMASiQkCIQAmABMTjGcIjjUp7a2HnQ9+qNf71o/CzGz/uKGhsbLGlNPLptvNuqKhEIlKJl4XgKQEhCSwOZAyqToH6U41Kft3nHItWHHQdf6jf+ybfAPWp3nRO2VF1ZajUG3cCSBnOiV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'

ICON_BASE64_BLOB_THINK = b'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/GMzLdsAADpCaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjIzMTksIDIwMTgvMDIvMTUtMjA6Mjk6NDMgICAgICAgICI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICAgICAgICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iPgogICAgICAgICA8eG1wOkNyZWF0b3JUb29sPkFkb2JlIFBob3Rvc2hvcCBFbGVtZW50cyAxNy4wIChXaW5kb3dzKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAyMC0wNy0wMlQxNzowNjozMi0wNDowMDwveG1wOkNyZWF0ZURhdGU+CiAgICAgICAgIDx4bXA6TWV0YWRhdGFEYXRlPjIwMjAtMDctMDJUMTc6MDY6MzItMDQ6MDA8L3htcDpNZXRhZGF0YURhdGU+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDIwLTA3LTAyVDE3OjA2OjMyLTA0OjAwPC94bXA6TW9kaWZ5RGF0ZT4KICAgICAgICAgPHhtcE1NOkluc3RhbmNlSUQ+eG1wLmlpZDpjZGY4YTM3NS05ODVkLTdhNGQtOTU5OS1iOGJmYjZiZGMwYmI8L3htcE1NOkluc3RhbmNlSUQ+CiAgICAgICAgIDx4bXBNTTpEb2N1bWVudElEPmFkb2JlOmRvY2lkOnBob3Rvc2hvcDpkZWE3YjA5Yi1iY2E3LTExZWEtYTEwYi1iMTlmYTMxNTc1YWQ8L3htcE1NOkRvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+eG1wLmRpZDo5YjY3OTMyNi04MjExLTZjNDgtYjk0NS00NzY2MzI1NDU3M2Y8L3htcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkhpc3Rvcnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5jcmVhdGVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6OWI2NzkzMjYtODIxMS02YzQ4LWI5NDUtNDc2NjMyNTQ1NzNmPC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDIwLTA3LTAyVDE3OjA2OjMyLTA0OjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6c29mdHdhcmVBZ2VudD5BZG9iZSBQaG90b3Nob3AgRWxlbWVudHMgMTcuMCAoV2luZG93cyk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOmNkZjhhMzc1LTk4NWQtN2E0ZC05NTk5LWI4YmZiNmJkYzBiYjwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAyMC0wNy0wMlQxNzowNjozMi0wNDowMDwvc3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIEVsZW1lbnRzIDE3LjAgKFdpbmRvd3MpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2UvcG5nPC9kYzpmb3JtYXQ+CiAgICAgICAgIDxwaG90b3Nob3A6Q29sb3JNb2RlPjM8L3Bob3Rvc2hvcDpDb2xvck1vZGU+CiAgICAgICAgIDxwaG90b3Nob3A6SUNDUHJvZmlsZT5zUkdCIElFQzYxOTY2LTIuMTwvcGhvdG9zaG9wOklDQ1Byb2ZpbGU+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjU0PC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjUyPC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz7BeLFDAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAArWSURBVHja7FppcFRVFv7ue6/3nXQ20kmAkJgQkjSGpKEhQiEIgkZQQBjEQXRwqUHU2YxDUaWjjFVayhQz4zbMoOWCzjC4MCAG2Q0DhBBMgjEGQkJIyEaW3vu9d+/8CGBQknSHBEeLW9U/Xte7957vnnO++91zH2GM4afYOPxE208WmDAUg86eke0cGS2lJ0RK6ZEmOcGip7E6NTMrBaYCgKBEAh4/6Wh3c40tnXxdXYtQUdMkVGwrPFo0WDaQwcqxSc6cJPuowIwpYwOLUm1Bp8XAFAaNDJXAIAgEHLl8HsoIJIkhIBG4fDzaXUSsrFcW7S1XbSo9pSr8oujIyR8U2I3ZudHjkoK3LJvuWpuRGLRp1Qz8AANcpoDXT1BWq6zfuNPw1LGTys9Kjh5uuubApuaNT192s3vtgjxPvlo5uOzq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'

ICON_BASE64_BLOB_THINK2 = b'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/GMzLdsAADpCaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjIzMTksIDIwMTgvMDIvMTUtMjA6Mjk6NDMgICAgICAgICI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICAgICAgICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iPgogICAgICAgICA8eG1wOkNyZWF0b3JUb29sPkFkb2JlIFBob3Rvc2hvcCBFbGVtZW50cyAxNy4wIChXaW5kb3dzKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAyMC0wNy0wMlQxNzowOTozMy0wNDowMDwveG1wOkNyZWF0ZURhdGU+CiAgICAgICAgIDx4bXA6TWV0YWRhdGFEYXRlPjIwMjAtMDctMDJUMTc6MDk6MzMtMDQ6MDA8L3htcDpNZXRhZGF0YURhdGU+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDIwLTA3LTAyVDE3OjA5OjMzLTA0OjAwPC94bXA6TW9kaWZ5RGF0ZT4KICAgICAgICAgPHhtcE1NOkluc3RhbmNlSUQ+eG1wLmlpZDpiYzcxZTAzMC1hY2UwLWFlNGMtYTI2YS1hNGJlM2E4NDNlMDA8L3htcE1NOkluc3RhbmNlSUQ+CiAgICAgICAgIDx4bXBNTTpEb2N1bWVudElEPmFkb2JlOmRvY2lkOnBob3Rvc2hvcDo0OWE4ZGNmZC1iY2E4LTExZWEtYTEwYi1iMTlmYTMxNTc1YWQ8L3htcE1NOkRvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+eG1wLmRpZDpjMWE2NTcxYS1lNGJlLTczNDMtYjAzNy1lYmE3NmRjMTA3YWI8L3htcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkhpc3Rvcnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5jcmVhdGVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6YzFhNjU3MWEtZTRiZS03MzQzLWIwMzctZWJhNzZkYzEwN2FiPC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDIwLTA3LTAyVDE3OjA5OjMzLTA0OjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6c29mdHdhcmVBZ2VudD5BZG9iZSBQaG90b3Nob3AgRWxlbWVudHMgMTcuMCAoV2luZG93cyk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOmJjNzFlMDMwLWFjZTAtYWU0Yy1hMjZhLWE0YmUzYTg0M2UwMDwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAyMC0wNy0wMlQxNzowOTozMy0wNDowMDwvc3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIEVsZW1lbnRzIDE3LjAgKFdpbmRvd3MpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2UvcG5nPC9kYzpmb3JtYXQ+CiAgICAgICAgIDxwaG90b3Nob3A6Q29sb3JNb2RlPjM8L3Bob3Rvc2hvcDpDb2xvck1vZGU+CiAgICAgICAgIDxwaG90b3Nob3A6SUNDUHJvZmlsZT5zUkdCIElFQzYxOTY2LTIuMTwvcGhvdG9zaG9wOklDQ1Byb2ZpbGU+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjU4PC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjU1PC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz5uOveQAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAqxSURBVHja7Fp5VJTXFf+9b5kFBoYdDciwiMhe0xhFwYQYTdUTl7hErVWJWYptNGoalwQ92mOiydGqaRajiWarRk1jbIItjUHEiNYYRKKgMiMDiCDrMGyzfN/rH+PgAMMyAybmxHvOd2DuvPvN7/fu/d69776PUErxaxAGvxK5R/Qe0XtE7xG9K4S7Uzde9WxsRKi/OSJsgGmom5y6dTe2vJYtvVHHlmpvcppNu/Iv3wk8pD/z6MqnY8Of+V3jclepqFDIqLuLTJzsiH1zK3OkyUAa8zSSs99ekH29eXf+1buKaMqM3yiWTdWtj1aZhgFI7idsmZdK+NytXyjX7Tl0vvFnJ7r/tYj5MxObFvYjwU6ED5503Tt79eWPfhaiqb+P90md0LA6MsgUzxCMvb28SQH3kSCyIEDiDar7HtD/DxCN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'

ICON_BASE64_BROW = b'iVBORw0KGgoAAAANSUhEUgAAADUAAAA1CAYAAADh5qNwAAAACXBIWXMAAAsTAAALEwEAmpwYAAAKT2lDQ1BQaG90b3Nob3AgSUNDIHByb2ZpbGUAAHjanVNnVFPpFj333vRCS4iAlEtvUhUIIFJCi4AUkSYqIQkQSoghodkVUcERRUUEG8igiAOOjoCMFVEsDIoK2AfkIaKOg6OIisr74Xuja9a89+bN/rXXPues852zzwfACAyWSDNRNYAMqUIeEeCDx8TG4eQuQIEKJHAAEAizZCFz/SMBAPh+PDwrIsAHvgABeNMLCADATZvAMByH/w/qQplcAYCEAcB0kThLCIAUAEB6jkKmAEBGAYCdmCZTAKAEAGDLY2LjAFAtAGAnf+bTAICd+Jl7AQBblCEVAaCRACATZYhEAGg7AKzPVopFAFgwABRmS8Q5ANgtADBJV2ZIALC3AMDOEAuyAAgMADBRiIUpAAR7AGDIIyN4AISZABRG8lc88SuuEOcqAAB4mbI8uSQ5RYFbCC1xB1dXLh4ozkkXKxQ2YQJhmkAuwnmZGTKBNA/g88wAAKCRFRHgg/P9eM4Ors7ONo62Dl8t6r8G/yJiYuP+5c+rcEAAAOF0ftH+LC+zGoA7BoBt/qIl7gRoXgugdfeLZrIPQLUAoOnaV/Nw+H48PEWhkLnZ2eXk5NhKxEJbYcpXff5nwl/AV/1s+X48/Pf14L7iJIEyXYFHBPjgwsz0TKUcz5IJhGLc5o9H/LcL//wd0yLESWK5WCoU41EScY5EmozzMqUiiUKSKcUl0v9k4t8s+wM+3zUAsGo+AXuRLahdYwP2SycQWHTA4vcAAPK7b8HUKAgDgGiD4c93/+8//UegJQCAZkmScQAAXkQkLlTKsz/HCAAARKCBKrBBG/TBGCzABhzBBdzBC/xgNoRCJMTCQhBCCmSAHHJgKayCQiiGzbAdKmAv1EAdNMBRaIaTcA4uwlW4Dj1wD/phCJ7BKLyBCQRByAgTYSHaiAFiilgjjggXmYX4IcFIBBKLJCDJiBRRIkuRNUgxUopUIFVIHfI9cgI5h1xGupE7yAAygvyGvEcxlIGyUT3UDLVDuag3GoRGogvQZHQxmo8WoJvQcrQaPYw2oefQq2gP2o8+Q8cwwOgYBzPEbDAuxsNCsTgsCZNjy7EirAyrxhqwVqwDu4n1Y8+xdwQSgUXACTYEd0IgYR5BSFhMWE7YSKggHCQ0EdoJNwkDhFHCJyKTqEu0JroR+cQYYjIxh1hILCPWEo8TLxB7iEPENyQSiUMyJ7mQAkmxpFTSEtJG0m5SI+ksqZs0SBojk8naZGuyBzmULCAryIXkneTD5DPkG+Qh8lsKnWJAcaT4U+IoUspqShnlEOU05QZlmDJBVaOaUt2ooVQRNY9aQq2htlKvUYeoEzR1mjnNgxZJS6WtopXTGmgXaPdpr+h0uhHdlR5Ol9BX0svpR+iX6AP0dwwNhhWDx4hnKBmbGAcYZxl3GK+YTKYZ04sZx1QwNzHrmOeZD5lvVVgqtip8FZHKCpVKlSaVGyovVKmqpqreqgtV81XLVI+pXlN9rkZVM1PjqQnUlqtVqp1Q61MbU2epO6iHqmeob1Q/pH5Z/YkGWcNMw09DpFGgsV/jvMYgC2MZs3gsIWsNq4Z1gTXEJrHN2Xx2KruY/R27iz2qqaE5QzNKM1ezUvOUZj8H45hx+Jx0TgnnKKeX836K3hTvKeIpG6Y0TLkxZVxrqpaXllirSKtRq0frvTau7aedpr1Fu1n7gQ5Bx0onXCdHZ4/OBZ3nU9lT3acKpxZNPTr1ri6qa6UbobtEd79up+6Ynr5egJ5Mb6feeb3n+hx9L/1U/W36p/VHDFgGswwkBtsMzhg8xTVxbzwdL8fb8VFDXcNAQ6VhlWGX4YSRudE8o9VGjUYPjGnGXOMk423GbcajJgYmISZLTepN7ppSTbmmKaY7TDtMx83MzaLN1pk1mz0x1zLnm+eb15vft2BaeFostqi2uGVJsuRaplnutrxuhVo5WaVYVVpds0atna0l1rutu6cRp7lOk06rntZnw7Dxtsm2qbcZsOXYBtuutm22fWFnYhdnt8Wuw+6TvZN9un2N/T0HDYfZDqsdWh1+c7RyFDpWOt6azpzuP33F9JbpL2dYzxDP2DPjthPLKcRpnVOb00dnF2e5c4PziIuJS4LLLpc+Lpsbxt3IveRKdPVxXeF60vWdm7Obwu2o26/uNu5p7ofcn8w0nymeWTNz0MPIQ+BR5dE/C5+VMGvfrH5PQ0+BZ7XnIy9jL5FXrdewt6V3qvdh7xc+9j5yn+M+4zw33jLeWV/MN8C3yLfLT8Nvnl+F30N/I/9k/3r/0QCngCUBZwOJgUGBWwL7+Hp8Ib+OPzrbZfay2e1BjKC5QRVBj4KtguXBrSFoyOyQrSH355jOkc5pDoVQfujW0Adh5mGLw34MJ4WHhVeGP45wiFga0TGXNXfR3ENz30T6RJZE3ptnMU85ry1KNSo+qi5qPNo3ujS6P8YuZlnM1VidWElsSxw5LiquNm5svt/87fOH4p3iC+N7F5gvyF1weaHOwvSFpxapLhIsOpZATIhOOJTwQRAqqBaMJfITdyWOCnnCHcJnIi/RNtGI2ENcKh5O8kgqTXqS7JG8NXkkxTOlLOW5hCepkLxMDUzdmzqeFpp2IG0yPTq9MYOSkZBxQqohTZO2Z+pn5mZ2y6xlhbL+xW6Lty8elQfJa7OQrAVZLQq2QqboVFoo1yoHsmdlV2a/zYnKOZarnivN7cyzytuQN5zvn//tEsIS4ZK2pYZLVy0dWOa9rGo5sjxxedsK4xUFK4ZWBqw8uIq2Km3VT6vtV5eufr0mek1rgV7ByoLBtQFr6wtVCuWFfevc1+1dT1gvWd+1YfqGnRs+FYmKrhTbF5cVf9go3HjlG4dvyr+Z3JS0qavEuWTPZtJm6ebeLZ5bDpaql+aXDm4N2dq0Dd9WtO319kXbL5fNKNu7g7ZDuaO/PLi8ZafJzs07P1SkVPRU+lQ27tLdtWHX+G7R7ht7vPY07NXbW7z3/T7JvttVAVVN1WbVZftJ+7P3P66Jqun4lvttXa1ObXHtxwPSA/0HIw6217nU1R3SPVRSj9Yr60cOxx++/p3vdy0NNg1VjZzG4iNwRHnk6fcJ3/ceDTradox7rOEH0x92HWcdL2pCmvKaRptTmvtbYlu6T8w+0dbq3nr8R9sfD5w0PFl5SvNUyWna6YLTk2fyz4ydlZ19fi753GDborZ752PO32oPb++6EHTh0kX/i+c7vDvOXPK4dPKy2+UTV7hXmq86X23qdOo8/pPTT8e7nLuarrlca7nuer21e2b36RueN87d9L158Rb/1tWeOT3dvfN6b/fF9/XfFt1+cif9zsu72Xcn7q28T7xf9EDtQdlD3YfVP1v+3Njv3H9qwHeg89HcR/cGhYPP/pH1jw9DBY+Zj8uGDYbrnjg+OTniP3L96fynQ89kzyaeF/6i/suuFxYvfvjV69fO0ZjRoZfyl5O/bXyl/erA6xmv28bCxh6+yXgzMV70VvvtwXfcdx3vo98PT+R8IH8o/2j5sfVT0Kf7kxmTk/8EA5jz/GMzLdsAADpCaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjIzMTksIDIwMTgvMDIvMTUtMjA6Mjk6NDMgICAgICAgICI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICAgICAgICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iPgogICAgICAgICA8eG1wOkNyZWF0b3JUb29sPkFkb2JlIFBob3Rvc2hvcCBFbGVtZW50cyAxNy4wIChXaW5kb3dzKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAyMC0wNy0wMlQxNjo1MzowNC0wNDowMDwveG1wOkNyZWF0ZURhdGU+CiAgICAgICAgIDx4bXA6TWV0YWRhdGFEYXRlPjIwMjAtMDctMDJUMTY6NTM6MDQtMDQ6MDA8L3htcDpNZXRhZGF0YURhdGU+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDIwLTA3LTAyVDE2OjUzOjA0LTA0OjAwPC94bXA6TW9kaWZ5RGF0ZT4KICAgICAgICAgPHhtcE1NOkluc3RhbmNlSUQ+eG1wLmlpZDo5ZGMyYTFmMC02ZWJhLWQ3NDYtOGIzMC1jYzYwMWM0ZGIzMzE8L3htcE1NOkluc3RhbmNlSUQ+CiAgICAgICAgIDx4bXBNTTpEb2N1bWVudElEPmFkb2JlOmRvY2lkOnBob3Rvc2hvcDplNjE1MzI2Zi1iY2E1LTExZWEtYTEwYi1iMTlmYTMxNTc1YWQ8L3htcE1NOkRvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+eG1wLmRpZDpiMzM5ZDA0Mi1mNGFkLTQ5NDUtOTBiZS1hZTg0ZTE2ZGNiZDI8L3htcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkhpc3Rvcnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5jcmVhdGVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6YjMzOWQwNDItZjRhZC00OTQ1LTkwYmUtYWU4NGUxNmRjYmQyPC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDIwLTA3LTAyVDE2OjUzOjA0LTA0OjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6c29mdHdhcmVBZ2VudD5BZG9iZSBQaG90b3Nob3AgRWxlbWVudHMgMTcuMCAoV2luZG93cyk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOjlkYzJhMWYwLTZlYmEtZDc0Ni04YjMwLWNjNjAxYzRkYjMzMTwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAyMC0wNy0wMlQxNjo1MzowNC0wNDowMDwvc3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIEVsZW1lbnRzIDE3LjAgKFdpbmRvd3MpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2UvcG5nPC9kYzpmb3JtYXQ+CiAgICAgICAgIDxwaG90b3Nob3A6Q29sb3JNb2RlPjM8L3Bob3Rvc2hvcDpDb2xvck1vZGU+CiAgICAgICAgIDxwaG90b3Nob3A6SUNDUHJvZmlsZT5zUkdCIElFQzYxOTY2LTIuMTwvcGhvdG9zaG9wOklDQ1Byb2ZpbGU+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjUzPC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjUzPC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz6xTRINAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAeISURBVHja3Jp7UFTXHce/d3fZZR8sIPJQeSwghFeAsTVBIriWphkMGB9kGmOYaXWa1mQm0VJjCGGmDzdoUtT+0w7Q0GbUkNYHhBUz49iGRwKkolVQoKTA7gIqILIsu3ff9/YP0x3JPi+5IPj7a/fc8zt7Pvs753d/v3N+BE3TeNyEg8dQHksoHtsDHnw1NzEznp8pW8WVRYfyogJEhFTsT4gAwGCiyVmS1mkmbSOqO3ZVn9rae/iPLTfZngPBxp46UiLPKtggLEyV8VIIguAA2OqjaiNN09StYWvvhU6T8u3K5s5HDvXRe3k7ijaJdor9CQkDELeARjNFnm8z1e8+dPnviw71wVubN762VbJPLGQFxgmONNFkdZOhav97/2xeFKj++vyjSdF+SQsA4wTXr7b2J+347NCCQe3fkytT7A1U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'

ICON_BASE64_BLOB_HEADACHE = b'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/GMzLdsAADpCaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjIzMTksIDIwMTgvMDIvMTUtMjA6Mjk6NDMgICAgICAgICI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICAgICAgICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iPgogICAgICAgICA8eG1wOkNyZWF0b3JUb29sPkFkb2JlIFBob3Rvc2hvcCBFbGVtZW50cyAxNy4wIChXaW5kb3dzKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAyMC0wNy0wMlQxNjo1NToyNi0wNDowMDwveG1wOkNyZWF0ZURhdGU+CiAgICAgICAgIDx4bXA6TWV0YWRhdGFEYXRlPjIwMjAtMDctMDJUMTY6NTU6MjYtMDQ6MDA8L3htcDpNZXRhZGF0YURhdGU+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDIwLTA3LTAyVDE2OjU1OjI2LTA0OjAwPC94bXA6TW9kaWZ5RGF0ZT4KICAgICAgICAgPHhtcE1NOkluc3RhbmNlSUQ+eG1wLmlpZDoxYzUxOTkzZi05MjNiLTM2NGItYWY5ZS1mNGE3MzViYjgxYTI8L3htcE1NOkluc3RhbmNlSUQ+CiAgICAgICAgIDx4bXBNTTpEb2N1bWVudElEPmFkb2JlOmRvY2lkOnBob3Rvc2hvcDo1MDgwYWJhOC1iY2E2LTExZWEtYTEwYi1iMTlmYTMxNTc1YWQ8L3htcE1NOkRvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+eG1wLmRpZDo3YWMwMzdjMC03ZmMzLWNhNDgtYmVlYi1lM2Q0ZDJjODJiNTU8L3htcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkhpc3Rvcnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5jcmVhdGVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6N2FjMDM3YzAtN2ZjMy1jYTQ4LWJlZWItZTNkNGQyYzgyYjU1PC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDIwLTA3LTAyVDE2OjU1OjI2LTA0OjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6c29mdHdhcmVBZ2VudD5BZG9iZSBQaG90b3Nob3AgRWxlbWVudHMgMTcuMCAoV2luZG93cyk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOjFjNTE5OTNmLTkyM2ItMzY0Yi1hZjllLWY0YTczNWJiODFhMjwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAyMC0wNy0wMlQxNjo1NToyNi0wNDowMDwvc3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIEVsZW1lbnRzIDE3LjAgKFdpbmRvd3MpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2UvcG5nPC9kYzpmb3JtYXQ+CiAgICAgICAgIDxwaG90b3Nob3A6Q29sb3JNb2RlPjM8L3Bob3Rvc2hvcDpDb2xvck1vZGU+CiAgICAgICAgIDxwaG90b3Nob3A6SUNDUHJvZmlsZT5zUkdCIElFQzYxOTY2LTIuMTwvcGhvdG9zaG9wOklDQ1Byb2ZpbGU+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjcxPC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjcxPC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz5o6m+QAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAABbGSURBVHja7HxZcGTXed73n3Puvb13oxtrYx1gMJjBLMTOWUiKiiRGcuxS2Y7K5bhsObEdOXmIk5TzkJQqSfkpecxTqpyUK3mwrUiqKHbJkkxRIk1KwyFnBrNzFgwGGKyDrbH0fu9Z8nDRBIboBockhpJcc6pQ/dIXOOe7//J93zkHZIzBs1F9sGcQPAPnGTjPwHkGzs/HED/rCXzmxRFyLEBwQ4IbWBzEyIARiAjQxv9RiozSgNRkPAnjSYKnCD89f/GptVv6NFv50PAYBWzDGuNKNCRUMBnTibqwakpETFs4oJtDjmkJOSZhMRMRDEFi4FoDnoJyPSoWPcoVXbaWLdJytsDmt4psPpNlc2ubbHNti7sbeabGL79rfmHAGR4Zo5BjWGeTDHQ2ynRbvRxJRfVnE2E1Gg2ZdNjRkYBtLEsY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'

ICON_BASE64_LEGO_THINK = b'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/GMzLdsAADpEaVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjIzMTksIDIwMTgvMDIvMTUtMjA6Mjk6NDMgICAgICAgICI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iCiAgICAgICAgICAgIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgICAgICAgICB4bWxuczp0aWZmPSJodHRwOi8vbnMuYWRvYmUuY29tL3RpZmYvMS4wLyIKICAgICAgICAgICAgeG1sbnM6ZXhpZj0iaHR0cDovL25zLmFkb2JlLmNvbS9leGlmLzEuMC8iPgogICAgICAgICA8eG1wOkNyZWF0b3JUb29sPkFkb2JlIFBob3Rvc2hvcCBFbGVtZW50cyAxNy4wIChXaW5kb3dzKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAyMC0wNy0wMlQxNzoxNTozNC0wNDowMDwveG1wOkNyZWF0ZURhdGU+CiAgICAgICAgIDx4bXA6TWV0YWRhdGFEYXRlPjIwMjAtMDctMDJUMTc6MTU6MzQtMDQ6MDA8L3htcDpNZXRhZGF0YURhdGU+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDIwLTA3LTAyVDE3OjE1OjM0LTA0OjAwPC94bXA6TW9kaWZ5RGF0ZT4KICAgICAgICAgPHhtcE1NOkluc3RhbmNlSUQ+eG1wLmlpZDpkYzQ2ZDAwNS1hY2U0LTkwNDUtODUzMC1iY2Y4Zjc3Y2U2NjA8L3htcE1NOkluc3RhbmNlSUQ+CiAgICAgICAgIDx4bXBNTTpEb2N1bWVudElEPmFkb2JlOmRvY2lkOnBob3Rvc2hvcDoyM2FiN2M2NS1iY2E5LTExZWEtYTEwYi1iMTlmYTMxNTc1YWQ8L3htcE1NOkRvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+eG1wLmRpZDowNDRhZDA4Zi03ZmQ0LWMwNGItYmY1Yy01MTI4NzQzMjcyNTA8L3htcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOkhpc3Rvcnk+CiAgICAgICAgICAgIDxyZGY6U2VxPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5jcmVhdGVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6MDQ0YWQwOGYtN2ZkNC1jMDRiLWJmNWMtNTEyODc0MzI3MjUwPC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDIwLTA3LTAyVDE3OjE1OjM0LTA0OjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6c29mdHdhcmVBZ2VudD5BZG9iZSBQaG90b3Nob3AgRWxlbWVudHMgMTcuMCAoV2luZG93cyk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICAgICA8cmRmOmxpIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmFjdGlvbj5zYXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOmRjNDZkMDA1LWFjZTQtOTA0NS04NTMwLWJjZjhmNzdjZTY2MDwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAyMC0wNy0wMlQxNzoxNTozNC0wNDowMDwvc3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIEVsZW1lbnRzIDE3LjAgKFdpbmRvd3MpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2UvcG5nPC9kYzpmb3JtYXQ+CiAgICAgICAgIDxwaG90b3Nob3A6Q29sb3JNb2RlPjM8L3Bob3Rvc2hvcDpDb2xvck1vZGU+CiAgICAgICAgIDxwaG90b3Nob3A6SUNDUHJvZmlsZT5zUkdCIElFQzYxOTY2LTIuMTwvcGhvdG9zaG9wOklDQ1Byb2ZpbGU+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjEwMzwvZXhpZjpQaXhlbFhEaW1lbnNpb24+CiAgICAgICAgIDxleGlmOlBpeGVsWURpbWVuc2lvbj4xMTI8L2V4aWY6UGl4ZWxZRGltZW5zaW9uPgogICAgICA8L3JkZjpEZXNjcmlwdGlvbj4KICAgPC9yZGY6UkRGPgo8L3g6eG1wbWV0YT4KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAKPD94cGFja2V0IGVuZD0idyI/PnSBBO0AAAAgY0hSTQAAeiUAAICDAAD5/wAAgOkAAHUwAADqYAAAOpgAABdvkl/FRgAADbNJREFUeNrsnXuMXFUdxz/nznNn3y92u215s9tSrEXEF1BwqdgVJchDJSKaYKJEjZoYgxhEJSYSefhIJBgSjDS8o/KyJkClLSpt0ZRKlb62tLYWumz3PTu7M/ce//idW/Yuu8PM7szuLT2/ZHP23jn3zp3z+33P73nOVVprLIWTHDsEljmWLHMscyxZ5liyzAkxRcP2QD/65kXOLb943tv6aJcCVG1NBIBkTAEQi4jpH3Pk2FFy7Jjj6cjzNID2tPTLyjFZV44zWTkeGHIV4Dy+cdQF1C2/eN6br7FQYfZztj7adXVtTSQJuMmYcgE3FtHSOsoDco7SHuA5jsqZy1zAm/Tnep7WgOtppQGd9XTOMMcFdCYr9xkYcvWKq9buC8PvDy1z9EufigA7gYVmgPWEwc6BmnisDVP0pL7+OT2B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'

ICON_BASE64_THINK = b'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/GMzLdsAAD+paVRYdFhNTDpjb20uYWRvYmUueG1wAAAAAAA8P3hwYWNrZXQgYmVnaW49Iu+7vyIgaWQ9Ilc1TTBNcENlaGlIenJlU3pOVGN6a2M5ZCI/Pgo8eDp4bXBtZXRhIHhtbG5zOng9ImFkb2JlOm5zOm1ldGEvIiB4OnhtcHRrPSJBZG9iZSBYTVAgQ29yZSA1LjYtYzE0NSA3OS4xNjIzMTksIDIwMTgvMDIvMTUtMjA6Mjk6NDMgICAgICAgICI+CiAgIDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+CiAgICAgIDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiCiAgICAgICAgICAgIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIKICAgICAgICAgICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICAgICAgICAgICB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIKICAgICAgICAgICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgICAgICAgICAgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiCiAgICAgICAgICAgIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIj4KICAgICAgICAgPHhtcDpDcmVhdG9yVG9vbD5BZG9iZSBQaG90b3Nob3AgRWxlbWVudHMgMTcuMCAoV2luZG93cyk8L3htcDpDcmVhdG9yVG9vbD4KICAgICAgICAgPHhtcDpDcmVhdGVEYXRlPjIwMjAtMDctMDJUMTc6MDI6MDUtMDQ6MDA8L3htcDpDcmVhdGVEYXRlPgogICAgICAgICA8eG1wOk1ldGFkYXRhRGF0ZT4yMDIwLTA3LTAyVDE3OjAyOjUxLTA0OjAwPC94bXA6TWV0YWRhdGFEYXRlPgogICAgICAgICA8eG1wOk1vZGlmeURhdGU+MjAyMC0wNy0wMlQxNzowMjo1MS0wNDowMDwveG1wOk1vZGlmeURhdGU+CiAgICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2UvcG5nPC9kYzpmb3JtYXQ+CiAgICAgICAgIDx4bXBNTTpJbnN0YW5jZUlEPnhtcC5paWQ6NGZjMmNkMTQtYjBhZi05ODQ0LTkyNTAtZTk1NTRhYjMzYzJmPC94bXBNTTpJbnN0YW5jZUlEPgogICAgICAgICA8eG1wTU06RG9jdW1lbnRJRD5hZG9iZTpkb2NpZDpwaG90b3Nob3A6NTU3OWQyOWUtYmNhNy0xMWVhLWExMGItYjE5ZmEzMTU3NWFkPC94bXBNTTpEb2N1bWVudElEPgogICAgICAgICA8eG1wTU06T3JpZ2luYWxEb2N1bWVudElEPnhtcC5kaWQ6OWUzNGE0MWQtOTM2YS1jZTRhLTgzNTMtZWVhYWEyYWQ2NjU1PC94bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ+CiAgICAgICAgIDx4bXBNTTpIaXN0b3J5PgogICAgICAgICAgICA8cmRmOlNlcT4KICAgICAgICAgICAgICAgPHJkZjpsaSByZGY6cGFyc2VUeXBlPSJSZXNvdXJjZSI+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDphY3Rpb24+Y3JlYXRlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6aW5zdGFuY2VJRD54bXAuaWlkOjllMzRhNDFkLTkzNmEtY2U0YS04MzUzLWVlYWFhMmFkNjY1NTwvc3RFdnQ6aW5zdGFuY2VJRD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OndoZW4+MjAyMC0wNy0wMlQxNzowMjowNS0wNDowMDwvc3RFdnQ6d2hlbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OnNvZnR3YXJlQWdlbnQ+QWRvYmUgUGhvdG9zaG9wIEVsZW1lbnRzIDE3LjAgKFdpbmRvd3MpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgICAgPHJkZjpsaSByZGY6cGFyc2VUeXBlPSJSZXNvdXJjZSI+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDphY3Rpb24+c2F2ZWQ8L3N0RXZ0OmFjdGlvbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0Omluc3RhbmNlSUQ+eG1wLmlpZDoxMGZiMmQwMi04NmUzLTAyNDMtYTc0Ny1hOGVkODM3NDU3NDk8L3N0RXZ0Omluc3RhbmNlSUQ+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDp3aGVuPjIwMjAtMDctMDJUMTc6MDI6NTEtMDQ6MDA8L3N0RXZ0OndoZW4+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpzb2Z0d2FyZUFnZW50PkFkb2JlIFBob3Rvc2hvcCBFbGVtZW50cyAxNy4wIChXaW5kb3dzKTwvc3RFdnQ6c29mdHdhcmVBZ2VudD4KICAgICAgICAgICAgICAgICAgPHN0RXZ0OmNoYW5nZWQ+Lzwvc3RFdnQ6Y2hhbmdlZD4KICAgICAgICAgICAgICAgPC9yZGY6bGk+CiAgICAgICAgICAgICAgIDxyZGY6bGkgcmRmOnBhcnNlVHlwZT0iUmVzb3VyY2UiPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6YWN0aW9uPmNvbnZlcnRlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6cGFyYW1ldGVycz5mcm9tIGFwcGxpY2F0aW9uL3ZuZC5hZG9iZS5waG90b3Nob3AgdG8gaW1hZ2UvcG5nPC9zdEV2dDpwYXJhbWV0ZXJzPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgICAgPHJkZjpsaSByZGY6cGFyc2VUeXBlPSJSZXNvdXJjZSI+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDphY3Rpb24+ZGVyaXZlZDwvc3RFdnQ6YWN0aW9uPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6cGFyYW1ldGVycz5jb252ZXJ0ZWQgZnJvbSBhcHBsaWNhdGlvbi92bmQuYWRvYmUucGhvdG9zaG9wIHRvIGltYWdlL3BuZzwvc3RFdnQ6cGFyYW1ldGVycz4KICAgICAgICAgICAgICAgPC9yZGY6bGk+CiAgICAgICAgICAgICAgIDxyZGY6bGkgcmRmOnBhcnNlVHlwZT0iUmVzb3VyY2UiPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6YWN0aW9uPnNhdmVkPC9zdEV2dDphY3Rpb24+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDppbnN0YW5jZUlEPnhtcC5paWQ6NGZjMmNkMTQtYjBhZi05ODQ0LTkyNTAtZTk1NTRhYjMzYzJmPC9zdEV2dDppbnN0YW5jZUlEPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6d2hlbj4yMDIwLTA3LTAyVDE3OjAyOjUxLTA0OjAwPC9zdEV2dDp3aGVuPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6c29mdHdhcmVBZ2VudD5BZG9iZSBQaG90b3Nob3AgRWxlbWVudHMgMTcuMCAoV2luZG93cyk8L3N0RXZ0OnNvZnR3YXJlQWdlbnQ+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpjaGFuZ2VkPi88L3N0RXZ0OmNoYW5nZWQ+CiAgICAgICAgICAgICAgIDwvcmRmOmxpPgogICAgICAgICAgICA8L3JkZjpTZXE+CiAgICAgICAgIDwveG1wTU06SGlzdG9yeT4KICAgICAgICAgPHhtcE1NOkRlcml2ZWRGcm9tIHJkZjpwYXJzZVR5cGU9IlJlc291cmNlIj4KICAgICAgICAgICAgPHN0UmVmOmluc3RhbmNlSUQ+eG1wLmlpZDoxMGZiMmQwMi04NmUzLTAyNDMtYTc0Ny1hOGVkODM3NDU3NDk8L3N0UmVmOmluc3RhbmNlSUQ+CiAgICAgICAgICAgIDxzdFJlZjpkb2N1bWVudElEPnhtcC5kaWQ6OWUzNGE0MWQtOTM2YS1jZTRhLTgzNTMtZWVhYWEyYWQ2NjU1PC9zdFJlZjpkb2N1bWVudElEPgogICAgICAgICAgICA8c3RSZWY6b3JpZ2luYWxEb2N1bWVudElEPnhtcC5kaWQ6OWUzNGE0MWQtOTM2YS1jZTRhLTgzNTMtZWVhYWEyYWQ2NjU1PC9zdFJlZjpvcmlnaW5hbERvY3VtZW50SUQ+CiAgICAgICAgIDwveG1wTU06RGVyaXZlZEZyb20+CiAgICAgICAgIDxwaG90b3Nob3A6Q29sb3JNb2RlPjM8L3Bob3Rvc2hvcDpDb2xvck1vZGU+CiAgICAgICAgIDxwaG90b3Nob3A6SUNDUHJvZmlsZT5zUkdCIElFQzYxOTY2LTIuMTwvcGhvdG9zaG9wOklDQ1Byb2ZpbGU+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjcyMDAwMC8xMDAwMDwvdGlmZjpYUmVzb2x1dGlvbj4KICAgICAgICAgPHRpZmY6WVJlc29sdXRpb24+NzIwMDAwLzEwMDAwPC90aWZmOllSZXNvbHV0aW9uPgogICAgICAgICA8dGlmZjpSZXNvbHV0aW9uVW5pdD4yPC90aWZmOlJlc29sdXRpb25Vbml0PgogICAgICAgICA8ZXhpZjpDb2xvclNwYWNlPjE8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjUwPC9leGlmOlBpeGVsWERpbWVuc2lvbj4KICAgICAgICAgPGV4aWY6UGl4ZWxZRGltZW5zaW9uPjUwPC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz7Z0mgMAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAzySURBVHjatFp7UFzndf+d7959wPLcFQKEQBiEDHoDltB75Ei25WTsNIkdeayJXTudJp04mbT+w/0jM53OONN4kr6cNJ5p6zgPN9NWSWvFiS25lZrI0QPJIPQASQgJEAhYYGHZ991773f6x+6iZbUvUPTNLMtw7/3u+Z3X75zzQcyMB7k2t3UQAPR0d3K264mV6b5c76DFAskm2KFndtHmRktp6xpreWONxVJRQvYCKxUBQDjKkSkfa7fG9FD39Wjg4k09NO4x9UBImpqO5L14KYAWBWRzWwelvuArX9ojtjRbLDvW2ZyNNepWq0qPwZT1AAoBKiRCAQAwQwKsAQhDEZ6owaM37xiXTvdqF89f04euDkXn/CGWSeLwYsDkDSQZRGtbB7W3WGyf211Y2dZkXVtZLrYJxg4ADwEoAWABoAIQAChJ0xKACUAHEAIwy4QR96x5umtA/+17J0PXPrmqz6VIlBegnEBSXWnnjm3iTz9bXPP0TtuBEps4oAg0A6gAUBAHoMSFTwBIBpL4ToAyAIQBzJgS/T5NfvSrU9rRfz7ivx2McHQxrpYVSCqIz31mh/LNgyXrd6+1viQIjwKoYuYiU7LVlCzATCQIiiBShMj2Xk6xUsJCE5Lx+4+vRn/xD//u6xwaNwMcU0ROMDmBJB5+4dldlm9+sWRra4PyCoE6gmF92fhUwD41E1I8s2EKhKLEzLBZVZSV2OAqK0TV8iJUlBdAEOUClQCkAZhhcE/PLePdvz/s/+jSgO7LxzJ5xciXn99te+1Qyd6mKuXPAGwZHPWWf3BiwDox6RPeuTBFdYnkbRQFcBTasHxZEdo3VGPfzodAucMw2To+BvoG3PLtN971vt91TffFt6ee7k6Z7mGRK7d/8emdyqsHi7c3VSrfIGAbiJzdl8dtl69OCPd0kIgEVte7sLujDvt3NWB720pULy9FMKTj5pAHHxzvh5SMPPRFcXmsAMoIWLd6uXj5Lw6WrG1aqaKnu5N7ujtlKu8klporxb7wpGNFc43yJSJsAlAKKa2P7WmgUNighroytG6oRmGBBWCO6ZQIIMKUJ4AzXXdQ4SyAUAiUX3JMJAkVQCkR1jXXKAdf/LTjKgBvNhrI6lqvv/po2avPFn29wEIvAlgBwBZ/hqAIQMaETxcCzAAEAcyZ3YoSPxi4VwwJIApgPKTjzb877H/rW3/7f9qigRzYv8P69l86D60oF98goDFGcAt4YX5FdBOX+twQCmFtUwUKrAooQ4AzEeb8EYxP+jEzG0ZEk1BVQmmxLZYcnA4IAuhuzEQYGBibla98+Tszp47+72lOB0bNpKyvfaGoubqM/oiAGgD2bCC+/845jI55ARA2tlTi5efakC4oZuYi+PmRXgyPzkLXTUgp4zFOICIoikCFy4HdHavQvrGaCiyKAGAjoKa6jF782ueLLgOYS5e90gb7wc/uVPe32x4VRA8DcCSR3D2ucfqTEdwa9iCiGYhoOs52j6LvxhTusTQBPX1uXBtwIxjUYBgmolEDWtSEFjWgRQ1EdQPDIzP46eEL+Jd3u6CbMpEAHIJo+2OP2NdkUnxaIE9uL3BZQTsBOONZJK2fMANDI16wvCu0EMCFy+OxX1KS66aW5djRXodP7WrApvXVUNS799htKvbvacKW1pWorCiC1xeBjO1L8YqhwkK8/sff2a/klbUO7NtO3/5K2SahoDFedohMQFJpOtdylRXguafWQdNNHP7wKnRDzm8cCuuory3FgT0NGHX7IQBYYkATVikUgtZuaLDY4lVAdousqrGoNS7RTjFrWLKBIALqa8sgxN1bTAm0bqwGpEzvAoJgmhKRsLFAA8yAL6DBZhFYXVuGhtqy5IqAAFgJaKlxiaq8XKvWJYpdxaIlKTaymmLHI7VoXOWC3abCbrNge1st1q5eljFrAYDVqqCs1AYSydUAodLlyPY2AaDZVSwef/3P99pSyfse16pdrrpUlarA87GR1a3sFgWvvLQVl666IUQs/UJmIJcEEFXBhocrcfmaGxPuABSFsKGlEjWVxZkUkJDDpaq0tXa5+ksAU8nZawGQXTu30bdeKKmiWE+h5AKRDGbrxhWL6jSb6svx3NMb0DcwhUK7Ba3rquCwq7lY30JASaVTWHft3Ea/P3U2PY+oKpGzWKwEzwf5A1uqIrC2cRmaVpWDiKAqApRbbQIMu7NYqKpKmWNEERCFNnKC5zMVPUgwRIDVosCi5gWC4knBUVAg7L/93RlOjhGRcicJhVSmB2uN+0MPoQhY9j+6nTJaRAKsG6xRrMbJTRFZCk7OfnkpK8GOUtcZMlv6NU02AyE5HO+jZS4QZjgENs0FEjMBLAhSMkwpY4CE+EMBkwBCgaCMmiZnZvbfnTzLR37w+HUmuInRnG1HbeA69PE7IKsN9uZ1UMrKwQDOdI3iyLHrCIU1SMmwWlVUOIvQsmYZNq2rwnJnIQrtaq72NyMQJnim/BwyjBwlypjHnGBGHwHb46U73xP0RJChIEgIwNAR6bsM+8ZWiKJiDI144QuEoQgBoRCiUQPDd2YwODqD/zl5Ew83uLDtkTqsXe1CcaF1MW4lAUSZMTPuMTU9F5DRSTMS1rjHYSN/fEYl0rmVUlYO6ZuLpR5pQr8zAtuaFuzb9RDqakpgtagQgmAYJmZ8GoZGvOi/OY3e/kkMjsyidcMKPLV/DcqLbVmrgBQw4bDGd0YnzYiezbUA4PaEzlNec8BRqY4BqErbszBDlJQuMJUM+AFNQ6XLMd8cJfKBKSWiugmPT8PR4zdw/uIoznSNoK6mFHu31uULwgAwN+U1+29P6JFEvCWY/R5t/+yXp3hkWg4z0BufaMj0HJDyqGlCapFYBqGFXKEqAoV2C1ZWOPAnh9rwxwfbUFtdihWVxYtxqwgDV0amZe/QhGmmNlZpa4LTvdHZbS3WixaBpzJ1hzIUWPgHZrBp5CBAAiRj++YV6Ni8AoIoX8Y1AXh1k//zdG908ONTZ2VejdVrb5zQPQF5jhmT8U14ocwSxsT4wsKQCKSouTmHADZ0sHcW+sgwtIHrMKbc4PRlP8ffH2ZGvyeIztfeOGHm3SECwI9+HehjQccABJOBMEtEB/ohQ8GUtKFCFBTe224RgSXDDPgRvT2I8MVuhLvPQ7t2BfrtIRgTY4jeHozFWPoJpA7AzQLvv/PrwPSSRqYXf/Fk3cZ69S0i2gfAyrpO0eFBGO6xhSQIwNa4BpbK6phmWUJqGqTPC2PGA+n3gQ0dBEpb3pOqwtrUDNVVkUp+MRDM/3VpyPjupmc+HFtUz55YP/zvwIjbJ/8GwBBLk/XRYRju8XsoWlisIFVFdPQ2tBtXEe7pQqTnE0Rv3oD0zgKmGUsOySA4Pj2xWiGcLghHUSoIA8AMgBNun3zrh+8FJu7rWOEHf/Up8dITji9Ypkff0odvuTK1sBAi1t5yhpqZOXZJUSAcRRBFxbFvux2isAhktSa7kwHAA+BYUOM33zkWvPTKX58w0w3mFjXE/uAf9xTvoZ4jxLx3SaW9okBdthxKuROiqBikqgCJWGVw10rJMeEDcFwyf+9YV/TSt3/qk4GwlNmOFdR85BjtHSFeyxpRRn3n7ohKymIxkJ7FE9kpGp/xXoga/HbXgN77+o+9CGq5D3ryAtKyLFwPRj0IS6tfTROmZxKq0wWyWNKRnRmvuCcBnPJH+GfHPomce/OwXw9q85bCfQMpVEynEHDEXyqW5l6W5KEdp1hhCsAFZhz3hPjETz4M3nz/VFj3hTjv0928gBiSwswIEcFczFBiPhBtdlhX1oIUhVMOdGbjAI6CcPL8Lf3W937uDw6NGzjXeXZR1lfzOXabClvdjPAoAZXxod2iYoV1HaZvjoWjSAKIxD+DUuKjkMbv3Zk1+/7teDhy7HSINWNp/zSQl0Uuugs8e1fNnUbseMGebR6cNpClqcugf5yZb+omumaC7J/wmFcG3ebH569FvWcua9IbkHyhq3PJPWRGID3dnZywysnbRcGvtovf2BTZRkARgNI8piyx7pYxrrP47rErtv8YvhQITHs5Ou2XysS0oU9Mm6ZmLCzHs3HFfREiALS1d9DLm6cKX9o4dQjAVwHUx0eqaib6SxAbAx8d6Xc+f+ifhgPZ3DjX8fN9u1ZCQ9u2bAm1VwWPra8IPySI9wGoQ8w6lpRSJ8HMGoAZMOZ21wXsAAIPAsCiYiQG5jw///jGka9vcf/r+orwDBHvoZhlSuNniyIpGwWY4QbwMRGO9ntsZt0DArAo10r222f2baLPN8+WP9E4t7lAlR1Soh5AeTwBmILgJYE7EV1cGfVbT58bKxx7v9+JoTnrgjnZHxJE3kDSBeGz+zcpTzTOOXasDDirHNFyMBVMhCx693hB4OKkw3Njxu73a0rk+KkuflBWWBKQTBklLmDiM19OPCiBM63/HwAQrmGURDhdsAAAAABJRU5ErkJggg=='


ICON_BASE64_PALM = b'iVBORw0KGgoAAAANSUhEUgAAAEkAAAA8CAMAAAAdQmecAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAAB8SDx4UEiAUDyAUEiMZFSUbGSsUEy8aFiwbGTsUFTkdICwiHTIjHDQrHzsiGysjIjIlIDMqIzMsKjsgIzotID0uKT01IzszMUkYHE0ZIFkbKEQhHkUqH0sgHUUgI0MtIkUoKEsmIEwqIkwqL00rM0I1I0s1JEswKE04J0w7LUc9OVYpJ1omMVM0JVQ1K1I4JVU7KlszK1k6J1s7KVw4NGEdLmQeMWghNmE5LWQ4NXIiPWs2RHkkQnAzRVRENVNDOF1ENFxEOVpKOWNDM2NHPWNMPGxFOWxKPG9QPnJKPHVQP05HRFJMSltUUWpLQ2lUQ2NcWndNQndIU3JUQ3JUSHRZTHxSRHxVSHxZSnlaVH1YYmZgX39gVmZjYnZran14doFURoNWSYNbTYNeUoleUItbaYRgT4VhU4JiWIVoXIpjVIxlWo1oVo1pWpFiVpFlWZJsXZRxX4JmZYVsY4trY4pzaoN9e5NtYpRtaJltY5ZxYpRyaZpzZZx1ap14a5N4eJx1cJp3eJ15cZp6eqB2a6J6baN8cqJ7eax9cah+epx7hImBf5uBeqWAdKOCe6qCdKqDequJfbKJfY2EgpmIiZqVk52Zk6SBhKaFiKyDgqqFiayJgqyNi6aLkayNlKGQi6uRja+QlqySm6qZlLKMhLKOi7SRi76Th7qTi7KTk7KVm7KYk7SZm7iWk7yZk7ucm7Sco7ScqbqeorOfsK2knrmhnKukoqyop7GrqrqhpLqlq7mup7urqrSosbKuubqjsrymubyps7qqub6xrbSxsLizvbe1wr68ycKYi8OcmsCmo8KmqcGup8Ooq8qqqcersMGvv8yutMKxu8uwtM2zusy+v9G3usCwwsS0yca8xsW7y82/x8m9ysm90Ne8wMjAvMPCxsLAyc3Ax8vAy8/IzMbD0c3F08zK2NPLx9DJztnBydLO09LL2tPS19TS29rU29bU4dnT5NzV6NvZ4+Hf5uDd6+Pi7eXj8ejl9Ozp9/Lw+wAAAAAAAAAAAAAAAErQjXwAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAHU0lEQVRYR5WWf1gbZx3A8bw2y7nJVq00ZM9Eq63t0o3QFNKkrLbjoRjXsWFHCI+T0gNNe2nWm4Ndm9xFTLmj1UFONsUU1s2aZRRxdP7otNZN1Omc1inTdbad06danzlkVoR2/hG/7w8gNG/Y9iE/uPf9vp/7vt/37r0UZPLx34nxiYmJNybp4VuSxzQ9MXn5zempqelLlybfpotteu31ifFzfzp7/sL45PT09MS/aPOCME1jZ8+fGxs9Njw0fGLswuT01D/+SjsWgmU6fnJs7IUTx7410N8/MDx64eKlqV++DRXD9M2BkZOnfjicTvV0d/f0Hx09f/HNf//iL7QzP7mmn0XN9BMjR9PpfhOpkkdHz0z97+9PT9DuvOSa7gvHus2vYEzT6E4MDP10/PKlM0/T7rzkmoLBeyORWMwwzf6UaZowvydPX7z8nzPP0v585JhO7pIkWZbvVXUzlUomzYNmcui7L49fvPDs6zQiDzmmr9UHg7vDu8MRVTcOHESq5KEjz7z8yitnfkwj8pBr2njHNjEo7ZbliGFAQsk+eB155vTpc6f/RkPY5JiOr7i1uh5UYUVROw4ehEolk1193zj2k9+NLpxUbsWXrt5YfdfnpDAUS9UgLaCrq2/g6JETT9IINrmmJStWb9wUCKK6K0h1wDCMDs1IHjr8Tk23F63aeOsdooSXUNU6O7QOTdM7937x0NAbNIRJrumrS4tWb64OiFKrJEshWdnXqWr7QqGO/fuHztIQJrmmzKKiFauc9aLYIkp7xHvkfXtCLSG5Y+TU1w8foRFMGKat7y1asbLaH/CLkNeO5h2trZJk/Oq3I/uHh/9IQ1gwTD+4qnBpkbPK5xf9zTua/c1+fyT1WLLnvi+8MPwoDWHBMEWDjuuFpc5P+Hz3iM3Ndb5mPZVOKfU93xnqj/2GxjDINb3q8PicJYUly2vkutZWURR1PdErtwz8+vloQPk+DWLAyMnjWb58ZUnhrsf3SJ9s8fl1TVWlwODzI/HaxrYFpscw1fscxY7Slc7Yc5LkatDhTpZE3YzH133+1EsP0RgGDNOPqm74cJWrtHRbond9Q0LVdSmsmWa4rf3Ffw4/QmMYMEyZ9rIy502u0hpDlRK6HtNN40BCjI68+IeBtndWp0xmU5VrpWttFdqiensff27QjIuxwf6+/Y13v0YjGDBNr25yrV3rqoL7t7fX1A/0Girs6Eqw7fcPfJlGMGCaMt+rdt7k3Natqwkjpmnm4BNpQ27o+fNLD7yL4xYt+/RxGjYPtimTKSxxqYluEOm63psaTBtB89tDfe2LeY7neW7xnT+ncXPkMT109aoaJaYaugY7CmxSj6UHU12haNPV4EFw3I00cpY8psWLVlcHIxFdVTUtFod9Lm0aO+/adSMVAZy1icZSmKb738fzSzY1yJCRYcBGF48qWpdW11j/AapBQMW203gMw7SVRG4ORBKaqsXjWjSqaRGldkvV5utIF8JqFazWB+kQRI5pK4eLyvPVElQbyqRF92rxDll0rK+pXQRd8LK+/6MbNtzidrvXHKOjgCtMTVTD8++uDet6J1RJaVOie5XglrK6xlrUYf3QOo8HLG6v1+uuOEwHXmHajs45w05Fhx3c0JRQOBRUAi7P+pprIJuPrHHY7cXwZ3eAraJ8Nqss01NLqANzTbumxLSIrijhnTvDQWepq+x6oVAQBAuCh7dgs9sryj10dJbpttmJYT7eDlWOaJEwiO5uuRlJLNDMcSgK3lBOjkeyE3Q8NW1fNk8D1WiD9YJnZ1gOB1sCH0MK2oO/LYIF0gO3RWgkBmJ6cG51yRk5vkbR1IgcDisxWWwoIX0ILBAEm2AjCPx7sIeYbpvLx3odmgLPCaFIREY/WGDnrYOM5sAqUNgJNkEgImRaTGN44YPF0AFYhJsDIXicS/I+EC2n3QBHc7LZYO0q0KXgtttmTdfijDhLMQAiGxxYINK3Ax6ccqcq3jCzVrBaWAKdOKNyckk56N5esJ3UBqLQrAGYHg531CGV5ENtuAEDuSDWVKCMvN5Kb6X7s9R0O8poZvZ4FB0n2MrqGhr8vjLSij5JnYnMDSpIqbLS66amZbOiOSB9PNzmqdtSVVhL2rAcXtCHTeVIVQl4yfQKrs0WoWuNDKLp2dZ5eCvVzkGSmlWRpMCEhtORxIqj8TEBH88ja4IoKfxrqAC2wbmxUG0O7id6NAM+no+9GMuo6hZs+gxZKQQaRTPMFjFMUCuaFlo/Mr2CJkgJReNPfIFfmRM+ZIBVFfhS+BLOCZWb3C7kPofLEkM0CNqQy4zKuwGZ7iTRWIURIPW3mt0MMyo0vYL7s64luCt4Hu6ZeR4EHcgAuaBYcJ0XZPATAC0ampyAJ0fHz0IGZTPXiFTgQiYyJwAnh+pNd4QsZrcjgDYB5Bir7BvAhB5vKCvUZ+F4vMQ4cB54EP0/C2ik9/TDBZmnyG6BGqHuWJR9XvqdD2yCXcq+Dna6JtpIYJ15QWB+5W6v+1P/B0gPXHqaGwimAAAAAElFTkSuQmCC'


ICON_BASE64_LIST = [ICON_BASE64_BLOB_HEADACHE, ICON_BASE64_BLOB_PALM, ICON_BASE64_BLOB_PAT, ICON_BASE64_BLOB_THINK, ICON_BASE64_BLOB_THINK2, ICON_BASE64_BROW, ICON_BASE64_LEGO_THINK, ICON_BASE64_PALM, ICON_BASE64_THINK]

def _random_error_icon():
    return random.choice(ICON_BASE64_LIST)



#                        d8b
#                        Y8P
#
# 88888b.d88b.   8888b.  888 88888b.
# 888 "888 "88b     "88b 888 888 "88b
# 888  888  888 .d888888 888 888  888
# 888  888  888 888  888 888 888  888
# 888  888  888 "Y888888 888 888  888


def main():
    # theme('SystemDefaultForReal')

    # preview_all_look_and_feel_themes()
    # ChangeLookAndFeel('Dark Red')
    # theme('Dark Red')
    # SetOptions(progress_meter_color=(COLOR_SYSTEM_DEFAULT))
    # SetOptions(element_padding=(0,0))
    # ------ Menu Definition ------ #

    ver = version.split('\n')[0]


    menu_def = [['&File', ['!&Open::KeyOpen', '&Save::KeySave', '---', '&Properties::KeyProp', 'E&xit']],
                ['&Edit', ['&Paste', ['Special::KeySpecial', '!Normal', ], 'Undo'], ],
                ['!&Toolbar', ['Command &1', 'Command &2', 'Command &3', 'Command &4']],
                ['&Help', '&About...'], ]

    treedata = TreeData()

    treedata.Insert("", '_A_', 'Tree Item 1', [1, 2, 3], )
    treedata.Insert("", '_B_', 'B', [4, 5, 6], )
    treedata.Insert("_A_", '_A1_', 'Sub Item 1', ['can', 'be', 'anything'], )
    treedata.Insert("", '_C_', 'C', [], )
    treedata.Insert("_C_", '_C1_', 'C1', ['or'], )
    treedata.Insert("_A_", '_A2_', 'Sub Item 2', [None, None])
    treedata.Insert("_A1_", '_A3_', 'A30', ['getting deep'])
    treedata.Insert("_C_", '_C2_', 'C2', ['nothing', 'at', 'all'])

    for i in range(100):
        treedata.Insert('_C_', i, i, [])

    frame1 = [
        [Input('Input Text', do_not_clear=True, size=(250, 35), tooltip='Input'), FileBrowse(), Stretch()],
        [Multiline(size=(250, 75), do_not_clear=True, default_text='Multiline Input', tooltip='Multiline input'),
         MultilineOutput(size=(250, 75), default_text='Multiline Output', tooltip='Multiline output', key='-MLINE-')],
    ]

    frame2 = [
        [Listbox(['Listbox 1', 'Listbox 2', 'Listbox 3', 'Item 4', 'Item 5'], default_values=['Listbox 2', 'Listbox 3'], size=(200, 85), tooltip='Listbox',
                    key='_LISTBOX_', font='Courier 12', text_color='red',)],
        [Combo([1,2,3], size=(200, 35), tooltip='Combo', visible_items=2, key='_COMBO_')],
        [Spin([1, 2, 3], size=(40, 30), tooltip='Spinner', key='_SPIN1_')],
        [Spin(['Combo item 1', 'Combo item 2', 'Combo item 3'], size=(240, 30), tooltip='Spinner', key='_SPIN2_')],
    ]

    frame3 = [
        [Checkbox('Checkbox1', True, tooltip='Checkbox'), Checkbox('Checkbox1')],
        [Radio('Radio Button1', 1, tooltip='Radio'), Radio('Radio Button2', 1, default=True), Stretch()],
    ]

    frame4 = [
        [Slider(range=(0, 100), tick_interval=None, orientation='v', size=(3, 30), default_value=40, tooltip='Slider'),
         Dial(range=(0, 100), tick_interval=1, resolution=1, size=(150, 150), default_value=40, tooltip='Dial'),
         Stretch()],
    ]
    matrix = [[str(x * y) for x in range(4)] for y in range(8)]

    frame5 = [
        [Table(values=matrix, max_col_width=25, headings=('aaa', 'bbb', 'ccc', 'ddd'),
                  auto_size_columns=True, display_row_numbers=True, enable_events=True, bind_return_key=True,
                  justification='right', num_rows=6, alternating_row_color='lightblue', key='_table_',
                   tooltip='Table'),
         Tree(data=treedata, headings=['col1', 'col2', 'col3'], enable_events=True, auto_size_columns=True,
                 num_rows=10, col0_width=10, key='_TREE_', show_expanded=True, size=(200, 150), tooltip='Tree'),
         Stretch()],
    ]

    graph_elem = Graph((880, 150), (0, 0), (600, 300), key='+GRAPH+', tooltip='Graph')

    frame6 = [
        [graph_elem, Stretch()],
    ]

    tab1 = Tab('Graph Number 1', frame6, tooltip='Tab 1')
    tab2 = Tab('Graph Number 2', [[]])

    layout = [
        [Menu(menu_def, key='_REALMENU_', background_color='white')],
        [Text('You are running the PySimpleGUI.py file itself', font=('ANY', 15, 'Bold'), text_color='yellow')],
                  [Text('You should be importing it rather than running it', font='ANY 15')],
        [Text('VERSION {}'.format(ver), size=(85,1), text_color='yellow', font='ANY 18')],

        # [Image(data_base64=logo, tooltip='Image', click_submits=True, key='_IMAGE_'),
         [Frame('Input Text Group', frame1, title_color='yellow', tooltip='Text Group'), Stretch()],
        [Frame('Multiple Choice Group', frame2, title_color='green'),
         Frame('Binary Choice Group', frame3, title_color='purple'),
         Frame('Variable Choice Group', frame4, title_color='blue'), Stretch()],
        [Frame('Structured Data Group', frame5, title_color='yellow'), ],
        # [Frame('Graphing Group', frame6)],
        [TabGroup([[tab1, tab2]],title_color='black')],
        [ProgressBar(max_value=600, start_value=400, size=(600, 25), key='+PROGRESS+'),
         Text('', key='_PROGTEXT_'), Stretch(),
         ButtonMenu('&Menu', ['Menu', ['&Pause Graph', 'Menu item::optional_key']], key='_MENU_',
                       tooltip='Button Menu'),
         Button('Button'), Button('Exit', tooltip='Exit button')],
    ]

    window = Window('Window Title', layout,
                       font=('Helvetica', 13),
                       default_button_element_size=(100, 30),
                       auto_size_buttons=False,
                       default_element_size=(200, 22),
                       # border_depth=1,
                       )
    # graph_elem.DrawCircle((200, 200), 50, 'blue')
    i = 0
    graph_paused = False

    # window.Element('_LISTBOX_').SetValue(['Listbox 1','Listbox 3'])
    while True:  # Event Loop
        # TimerStart()
        event, values = window.read(timeout=10)
        print(event, values) if event != TIMEOUT_KEY else None
        window['-MLINE-'].update(value=str(values), append=True) if event != TIMEOUT_KEY else None
        if event is None or event == 'Exit':
            break
        if values['_MENU_'] == 'Pause Graph':
            graph_paused = not graph_paused
        if event == 'About...':
            Popup('You are running PySimpleGUIQt', 'The version number is', version)
        if not graph_paused:

            if i < 600:
                graph_elem.DrawLine((i, 0), (i, random.randint(0, 300)), width=1,
                                    color='#{:06x}'.format(random.randint(0, 0xffffff)))
            else:
                graph_elem.Move(-1, 0)
                graph_elem.DrawLine((i, 0), (i, random.randint(0, 300)), width=1,
                                    color='#{:06x}'.format(random.randint(0, 0xffffff)))

        window.FindElement('+PROGRESS+').UpdateBar(i % 600)
        window.FindElement('_PROGTEXT_').Update((i % 600) // 6)
        i += 1

        # TimerStop()
    window.close()



    # layout = [[Text('You are running the PySimpleGUI.py file itself')],
    #           [Text('You should be importing it rather than running it')],
    #           [Text('Here is your sample input window....')],
    #           [Text('Source File', size=(150, 25), justification='right'), InputText('Source', focus=True), FileBrowse()],
    #           [Text('Destination Folder', size=(150, 25), justification='right'), InputText('Dest'), FolderBrowse()],
    #           [Ok(bind_return_key=True), Cancel()]]
    #
    # window = Window('Demo window..',
    #                 auto_size_buttons=False,
    #                 default_element_size=(280,22),
    #                 auto_size_text=False,
    #                 default_button_element_size=(80,22)
    #                 ).Layout(layout)
    # event, values = window.Read()
    # print(event, values)
    # window.Close()

#------------------------------------------------------------------#
#------------------------ PEP8-ify The SDK ------------------------#
#------------------------------------------------------------------#

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
rgb = RGB
scrolled_text_box = ScrolledTextBox
set_global_icon = SetGlobalIcon
set_options = SetOptions
timer_start = TimerStart
timer_stop = TimerStop


#------------------------ Set the "Official PySimpleGUI Theme Colors" ------------------------
theme(CURRENT_LOOK_AND_FEEL)


if __name__ == '__main__':
    main()
    exit(69)
