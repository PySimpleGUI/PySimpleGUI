#!/usr/bin/python3
version = __version__ = "0.31.0.7 Unreleased - fix for Listbox.update, Graph.change_coordinates, Added Image.Widget, return correct value with ComboBox has manual data entry, added print_to_element, multlineline update moves cursor to end, scrollable columns, listbox.get, fix for visible ignored in Text Element"

port = 'PySimpleGUIQt'

import sys
import types
import datetime
import textwrap
import pickle
import base64
import calendar
from random import randint
import warnings


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

DEFAULT_BASE64_ICON = b'R0lGODlhIQAgAPcAAAAAADBpmDBqmTFqmjJrmzJsnDNtnTRrmTZtmzZumzRtnTdunDRunTRunjVvnzdwnzhwnjlxnzVwoDZxoTdyojhzozl0ozh0pDp1pjp2pjp2pzx0oj12pD52pTt3qD54pjt4qDx4qDx5qTx5qj16qj57qz57rD58rT98rkB4pkJ7q0J9rEB9rkF+rkB+r0d9qkZ/rEl7o0h8p0x9pk5/p0l+qUB+sEyBrE2Crk2Er0KAsUKAskSCtEeEtUWEtkaGuEiHuEiHukiIu0qKu0mJvEmKvEqLvk2Nv1GErVGFr1SFrVGHslaHsFCItFSIs1COvlaPvFiJsVyRuWCNsWSPsWeQs2SQtGaRtW+Wt2qVuGmZv3GYuHSdv3ievXyfvV2XxGWZwmScx2mfyXafwHikyP7TPP/UO//UPP/UPf/UPv7UP//VQP/WQP/WQf/WQv/XQ//WRP7XSf/XSv/YRf/YRv/YR//YSP/YSf/YSv/ZS//aSv/aS/7YTv/aTP/aTf/bTv/bT//cT/7aUf/cUP/cUf/cUv/cU//dVP/dVf7dVv/eVv/eV//eWP/eWf/fWv/fW/7cX/7cYf7cZP7eZf7dav7eb//gW//gXP/gXf/gXv/gX//gYP/hYf/hYv/iYf/iYv7iZP7iZf/iZv/kZv7iaP/kaP/ka//ma//lbP/lbv/mbP/mbv7hdP7lcP/ncP/nc//ndv7gef7gev7iff7ke/7kfv7lf//ocf/ocv/odP/odv/peP/pe//ofIClw4Ory4GszoSszIqqxI+vyoSv0JGvx5OxyZSxyZSzzJi0y5m2zpC10pi715++16C6z6a/05/A2qHC3aXB2K3I3bLH2brP4P7jgv7jh/7mgf7lhP7mhf7liv/qgP7qh/7qiP7rjf7sjP7nkv7nlv7nmP7pkP7qkP7rkv7rlv7slP7sl/7qmv7rnv7snv7sn/7un/7sqv7vq/7vrf7wpv7wqf7wrv7wsv7wtv7ytv7zvP7zv8LU48LV5c3a5f70wP7z0AAAACH5BAEAAP8ALAAAAAAhACAAAAj/AP8JHEiwoMGDCA1uoYIF4bhK1vwlPOjlQICLApwVpFTGzBk1siYSrCLgoskFyQZKMsOypRyR/GKYnBkgQbF/s8603KnmWkIaNIMaw6lzZ8tYB2cIWMo0KIJj/7YV9XgGDRo14gpOIUBggNevXpkKGCDsXySradSoZcMmDsFnDxpEKEC3bl2uXCFQ+7emjV83bt7AgTNroJINAq0wWBxBgYHHdgt0+cdnMJw5c+jQqYNnoARkAx04kPEvS4PTqBswuPIPUp06duzcuYMHT55wAjkwEahsQgqBNSQIHy582D9BePTs2dOnjx8/f1gJ9GXhRpTqApFQoDChu3cOAps///9D/g+gQvYGjrlw4cU/fUnYX6hAn34HgZMABQo0iJB/Qoe8UxAXOQiEg3wIXvCBQLUU4mAhh0R4SCLqJOSEBhhqkAEGHIYgUDaGICIiIoossogj6yBUTQ4htNgiCCB4oIJAtJTIyI2MOOLIIxMtQQIJIwQZpAgwCKRNI43o6Igll1ySSTsI7dOECSaUYOWVKwhkiyVMYuJlJpp0IpA6oJRTkBQopHnCmmu2IBA2mmQi5yZ0fgJKPP+0IwoooZwzkDQ2uCCoCywUyoIW/5DDyaKefOLoJ6LU8w87pJgDTzqmDNSMDpzqYMOnn/7yTyiglBqKKKOMUopA7JgCy0DdeMEjUDM71GqrrcH8QwqqqpbiayqToqJKLwN5g45A0/TAw7LL2krGP634aoopp5yiiiqrZLuKK+jg444uBIHhw7g+MMsDFP/k4wq22rririu4xItLLriAUxAQ5ObrwzL/0PPKu7fIK3C8uxz0w8EIIwzMP/cM7HC88hxEzBBCBGGxxT8AwQzDujws7zcJQVMEEUKUbPITAt1D78OSivSFEUXEXATKA+HTscC80CPSQNGEccQRYhjUDzfxcjPPzkgnLVBAADs='


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

DEFAULT_SLIDER_RELIEF = 'flat'
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
# Events that are pre-defined
# Key representing a Read timeout
TIMEOUT_KEY = '__TIMEOUT__'
# Key indicating should not create any return values for element
WRITE_ONLY_KEY = '__WRITE ONLY__'
EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED = '__DOUBLE_CLICKED__'
EVENT_SYSTEM_TRAY_ICON_ACTIVATED = '__ACTIVATED__'
EVENT_SYSTEM_TRAY_MESSAGE_CLICKED = '__MESSAGE_CLICKED__'

# Meny key indicator character / string
MENU_KEY_SEPARATOR = '::'
MENU_DISABLED_CHARACTER = '!'



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
                 key=None, pad=None, tooltip=None, visible=True, size_px=(None, None), metadata=None):

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


    def Update(self, widget, background_color=None, text_color=None, font=None, visible=None):
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



# ---------------------------------------------------------------------- #
#                           Input Class                                  #
# ---------------------------------------------------------------------- #
class InputText(Element):
    def __init__(self, default_text='', size=(None,None), disabled=False, password_char='',
                 justification=None, background_color=None, text_color=None, font=None, tooltip=None,
                 change_submits=False, enable_events=False,
                 do_not_clear=True, key=None, focus=False, pad=None, visible=True, size_px=(None,None), metadata=None):
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
                 text_color=None, change_submits=False, enable_events=False, disabled=False, key=None, pad=None, tooltip=None,
                 readonly=False, visible_items=10, font=None, auto_complete=True, visible=True, size_px=(None,None), metadata=None):
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
                 background_color=None, text_color=None, key=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
        '''
        InputOptionMenu - NOT USED IN QT
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
                 text_color=None, key=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
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
                 background_color=None, text_color=None, font=None, key=None, pad=None, tooltip=None,
                 change_submits=False,  enable_events=False, visible=True, size_px=(None,None), metadata=None):
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
        self.Widget = self.QT_Radio_Button = None           # type: QRadioButton

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
        if value:
            self.QT_Radio_Button.setChecked(True)
        super().Update(self.QT_Radio_Button, background_color=background_color, text_color=text_color, font=font, visible=visible)


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
                 text_color=None, change_submits=False, enable_events=False, disabled=False, key=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
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
                 auto_size_text=None, font=None, background_color=None, text_color=None, key=None, pad=None,
                 tooltip=None, visible=True, size_px=(None,None), metadata=None):
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
                 key=None, focus=False, font=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
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




    def Update(self, value=None, disabled=None, append=False, background_color=None, text_color=None, font=None, text_color_for_value=None, background_color_for_value=None, visible=None):
        """
        Changes some of the settings for the Multiline Element. Must call `Window.read` or `Window.finalize` or "finalize" the window using finalize parameter prior

        :param value: (str) new text to display
        :param disabled: (bool) disable or enable state of the element
        :param append: (bool) if True then new value will be added onto the end of the current value. if False then contents will be replaced.
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
            if self.Autoscroll:
                self.QT_TextEdit.moveCursor(QtGui.QTextCursor.End)
            if text_color_for_value is not None:
                self.QT_TextEdit.setTextColor(self.TextColor)
            if background_color_for_value is not None:
                self.QT_TextEdit.setTextBackgroundColor(self.BackgroundColor)
        if disabled == True:
            self.QT_TextEdit.setDisabled(True)
        elif disabled == False:
            self.QT_TextEdit.setDisabled(False)
        super().Update(self.QT_TextEdit, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def Get(self):
        self.QT_TextEdit.toPlainText()

    def SetFocus(self):
        self.QT_TextEdit.setFocus()

    get = Get
    set_focus = SetFocus
    update = Update

ML = Multiline
MLine = Multiline


# ---------------------------------------------------------------------- #
#                           ScrolledOutput                               #
# ---------------------------------------------------------------------- #
class MultilineOutput(Element):
    def __init__(self, default_text='', enter_submits=False, disabled=False, autoscroll=False, size=(None, None), auto_size_text=None, background_color=None, text_color=None, change_submits=False, enable_events=False, do_not_clear=True, key=None, focus=False, font=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
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
        self.Widget = self.QT_TextBrowser = None            # type: QTextBrowser
        tsize = _convert_tkinter_size_to_Qt(size, scaling=DEFAULT_PIXELS_TO_CHARS_SCALING_MULTILINE_TEXT,height_cutoff=DEFAULT_PIXEL_TO_CHARS_CUTOFF_MULTILINE) if size[0] is not None else size_px
        super().__init__(ELEM_TYPE_MULTILINE_OUTPUT, size=(None, None), auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible, size_px=tsize, metadata=metadata)
        return


    def Update(self, value=None, disabled=None, append=False, background_color=None, text_color=None, font=None, visible=None):
        if value is not None and not append:
            self.QT_TextBrowser.setText(str(value))
        elif value is not None and append:
            self.QT_TextBrowser.insertPlainText(str(value))
            self.QT_TextBrowser.moveCursor(QtGui.QTextCursor.End)
        if disabled == True:
            self.QT_TextBrowser.setDisabled(True)
        elif disabled == False:
            self.QT_TextBrowser.setDisabled(False)
        super().Update(self.QT_TextBrowser, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def Get(self):
        self.QT_TextBrowser.toPlainText()

    get = Get
    update = Update

MLineOut = Multiline

# ---------------------------------------------------------------------- #
#                                       Text                             #
# ---------------------------------------------------------------------- #
class Text(Element):
    def __init__(self, text='', size=(None, None),  auto_size_text=None, click_submits=None, enable_events=False, relief=None, font=None, text_color=None, background_color=None, justification=None, pad=None, margins=None, key=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
        '''
        Text Element
        :param text:
        :param size:
        :param auto_size_text:
        :param click_submits:
        :param relief:
        :param font:
        :param text_color:
        :param background_color:
        :param justification:
        :param pad:
        :param key:
        :param tooltip:
        '''
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
        '''

        :param value:
        :param background_color:
        :param text_color:
        :param font:
        :param visible:
        :return:
        '''
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
                 key=None, visible=True, size_px=(None,None), metadata=None):
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
                 focus=False, pad=None, key=None, visible=True, size_px=(None,None), metadata=None):
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
                 size=(None, None), auto_size_button=None, button_color=None, font=None, pad=None, key=None, visible=True, size_px=(None,None), metadata=None):
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
                 style=None, border_width=None, relief=None, key=None, pad=None, visible=True, size_px=(None,None), metadata=None):
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
    def __init__(self, filename=None, data=None, data_base64=None, background_color=None, size=(None, None), pad=None, key=None, tooltip=None, click_submits=False,  enable_events=False, visible=True, size_px=(None,None), metadata=None):
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
    def __init__(self, canvas=None, background_color=None, size=(None, None), pad=None, key=None, tooltip=None, metadata=None):
        '''
        Canvas Element - NOT USED IN QT PORT
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
    def __init__(self, canvas_size, graph_bottom_left, graph_top_right, background_color=None, pad=None, key=None,
                 tooltip=None, visible=True, change_submits=False, enable_events=False, drag_submits=False, metadata=None):
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
                 relief=DEFAULT_FRAME_RELIEF, size=(None, None), font=None, pad=None, border_width=None, key=None,
                 tooltip=None, visible=True, size_px=(None,None), metadata=None):
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
        self.Widget = self.QT_QGroupBox = None              # type: QGroupBox
        self.Layout(layout)

        super().__init__(ELEM_TYPE_FRAME, background_color=background_color, text_color=title_color, size=size,
                         font=font, pad=pad, key=key, tooltip=tooltip, visible=visible, size_px=size_px, metadata=metadata)
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


# ---------------------------------------------------------------------- #
#                           Separator                                    #
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
#                           Separator                                    #
# ---------------------------------------------------------------------- #
class HorizontalSeparator(Element):
    def __init__(self, pad=None, size_px=(None,None)):
        '''
        VerticalSeperator - A separator that spans only 1 row in a vertical fashion
        :param pad:
        '''
        self.Orientation = 'horizontal'  # for now only vertical works

        super().__init__(ELEM_TYPE_SEPARATOR, pad=pad)



HSeperator = HorizontalSeparator
HSep = HorizontalSeparator



# ---------------------------------------------------------------------- #
#                           Tab                                          #
# ---------------------------------------------------------------------- #
class Tab(Element):
    def __init__(self, title, layout, title_color=None, background_color=None, font=None, pad=None, disabled=False,
                 border_width=None, key=None, tooltip=None, visible=True, metadata=None):
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
        self.ParentTabGroup = None                          # type: TabGroup
        self.TabID = None
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.Widget = self.QT_QWidget = None                # type: QWidget

        self.Layout(layout)

        super().__init__(ELEM_TYPE_TAB, background_color=background_color, text_color=title_color, font=font, pad=pad,
                         key=key, tooltip=tooltip, visible=visible, metadata=metadata)
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
                 font=None, change_submits=False, enable_events=False, pad=None, border_width=None, theme=None, key=None, tooltip=None, visible=True, metadata=None):
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
        self.BackgroundColor = background_color if background_color is not None else COLOR_SYSTEM_DEFAULT
        self.ChangeSubmits = change_submits or enable_events
        self.TabLocation = tab_location
        self.TabList = []                                   # type: List[Tab]
        self.Widget = self.QT_QTabWidget = None             # type: QTabWidget
        self.Layout(layout)

        super().__init__(ELEM_TYPE_TAB_GROUP, background_color=self.BackgroundColor, text_color=title_color, font=font,
                         pad=pad, key=key, tooltip=tooltip, visible=visible, metadata=metadata)
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
                 background_color=None, text_color=None, key=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
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
        self.ChangeSubmits = change_submits or enable_events
        self.Disabled = disabled
        self.TickInterval = tick_interval
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
                 background_color=None, text_color=None, key=None, pad=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
        '''
        Dial Element
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
    def __init__(self, size=(None, None), font=None, background_color=None, text_color=None, key=None, pad=None, tooltip=None):
        '''
        Stretch Element
        :param size:
        :param font:
        :param background_color:
        :param text_color:
        :param key:
        :param pad:
        :param tooltip:
        '''
        self.Widget = None          # type: Stretch
        super().__init__(ELEM_TYPE_STRETCH, size=size, font=font, background_color=background_color,
                         text_color=text_color, key=key, pad=pad, tooltip=tooltip)
        return




# ---------------------------------------------------------------------- #
#                           Column                                       #
# ---------------------------------------------------------------------- #
class Column(Element):
    def __init__(self, layout, background_color=None, size=(None, None), pad=None, scrollable=False, key=None, visible=True, metadata=None):
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
        # self.ImageFilename = image_filename
        # self.ImageData = image_data
        # self.ImageSize = image_size
        # self.ImageSubsample = image_subsample
        bg = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.Widget = self.QT_QGroupBox = None              # type: QGroupBox
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
    def __init__(self, menu_definition, background_color=None, size=(None, None), tearoff=False, pad=None, key=None, visible=True, metadata=None):
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
                 font=None, justification='right', text_color=None, background_color=None, alternating_row_color=None,
                 size=(None, None), change_submits=False, enable_events=False, bind_return_key=False, pad=None, key=None, tooltip=None, visible=True, size_px=(None,None), metadata=None):
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
                 justification='right', text_color=None, background_color=None, num_rows=None, pad=None, key=None,
                 tooltip=None, visible=True, size_px=(None,None), metadata=None):
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
    def __init__(self, key=None):
        '''
        Error Element
        :param key:
        '''
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
        '''
        Reads the context menu
        :param timeout: Optional.  Any value other than None indicates a non-blocking read
        :return:
        '''
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
        '''

        :return:
        '''
        self.Hide()
        # Don't close app because windows could be depending on it
        # self.App.quit()


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
                 auto_size_text=None, auto_size_buttons=None, location=(None, None), size=(None, None), element_padding=None, button_color=None, font=None,
                 progress_bar_color=(None, None), background_color=None, border_depth=None, auto_close=False,
                 auto_close_duration=DEFAULT_AUTOCLOSE_TIME, icon=DEFAULT_WINDOW_ICON, force_toplevel=False,
                 alpha_channel=1, return_keyboard_events=False, use_default_focus=True, text_justification=None,
                 no_titlebar=False, grab_anywhere=False, keep_on_top=False, resizable=True, disable_close=False, disable_minimize=False, background_image=None, finalize=False, metadata=None):
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
        self._Size=size
        self.ElementPadding = element_padding or DEFAULT_ELEMENT_PADDING
        self.FocusElement = None
        self.BackgroundImage = background_image
        self.XFound = False
        self.DisableMinimize = disable_minimize
        self.UniqueKeyCounter = 0
        self.metadata = metadata


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
        self.QT_QMainWindow.move(x, y)

    def Minimize(self):
        self.QT_QMainWindow.setWindowState(Qt.WindowMinimized)

    def Maximize(self):
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
        self.QT_QMainWindow.setEnabled(False)

    def Enable(self):
        self.QT_QMainWindow.setEnabled(True)

    def Hide(self):
        self._Hidden = True
        self.QT_QMainWindow.hide()
        return

    def UnHide(self):
        if self._Hidden:
            self.QT_QMainWindow.show()
            self._Hidden = False

    def Disappear(self):
        self.AlphaChannel = 0

    def Reappear(self):
        self.AlphaChannel = 255

    def SetAlpha(self, alpha):
        '''
        Change the window's transparency
        :param alpha: From 0 to 1 with 0 being completely transparent
        :return:
        '''
        self._AlphaChannel = alpha
        if self._AlphaChannel is not None:
            self.QT_QMainWindow.setWindowOpacity(self._AlphaChannel)

    @property
    def AlphaChannel(self):
        return self._AlphaChannel

    @AlphaChannel.setter
    def AlphaChannel(self, alpha):
        self._AlphaChannel = alpha
        if self._AlphaChannel is not None:
            self.QT_QMainWindow.setWindowOpacity(self._AlphaChannel)

    def BringToFront(self):
        self.QTMainWindow.activateWindow(self.QT_QMainWindow)
        self.QTMainWindow.raise_(self.QT_QMainWindow)


    def CurrentLocation(self):
        location = self.QT_QMainWindow.geometry()
        return location.left(), location.top()

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
        size =  self.QT_QMainWindow.sizeHint()
        return [size.width(), size.height()]

    @Size.setter
    def Size(self, size):
        self.QT_QMainWindow.resize(QSize(size[0], size[1]))

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
                 key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FOLDER, target=target,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  disabled=disabled, button_color=button_color, change_submits=change_submits, enable_events=enable_events, font=font, pad=pad,
                  key=key, metadata=metadata)


# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileBrowse(button_text='Browse', target=(ThisRow, -1), file_types=(("ALL Files", "*"),), initial_folder=None,
               tooltip=None, size=(None, None), auto_size_button=None, button_color=None, change_submits=False, enable_events=False,
               font=None, disabled=False,
               pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  change_submits=change_submits, enable_events=enable_events, disabled=disabled, button_color=button_color, font=font, pad=pad,
                  key=key, metadata=metadata)


# -------------------------  FILES BROWSE Element (Multiple file selection) lazy function  ------------------------- #
def FilesBrowse(button_text='Browse', target=(ThisRow, -1), file_types=(("ALL Files", "*"),), disabled=False,
                initial_folder=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                change_submits=False, enable_events=False,
                font=None, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FILES, target=target, file_types=file_types,
                  initial_folder=initial_folder, change_submits=change_submits, enable_events=enable_events, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button,
                  disabled=disabled, button_color=button_color, font=font, pad=pad, key=key, metadata=metadata)


# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileSaveAs(button_text='Save As...', target=(ThisRow, -1), file_types=(("ALL Files", "*"),), initial_folder=None,
               disabled=False, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
               change_submits=False, enable_events=False, font=None,
               pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_SAVEAS_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, change_submits=change_submits, enable_events=enable_events,
                  font=font, pad=pad, key=key, metadata=metadata)


# -------------------------  SAVE AS Element lazy function  ------------------------- #
def SaveAs(button_text='Save As...', target=(ThisRow, -1), file_types=(("ALL Files", "*"),), initial_folder=None,
           disabled=False, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
           change_submits=False, enable_events=False, font=None,
           pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_SAVEAS_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, change_submits=change_submits, enable_events=enable_events,
                  font=font, pad=pad, key=key, metadata=metadata)


# -------------------------  SAVE BUTTON Element lazy function  ------------------------- #
def Save(button_text='Save', size=(None, None), auto_size_button=None, button_color=None, bind_return_key=True,
         disabled=False, tooltip=None, font=None, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  SUBMIT BUTTON Element lazy function  ------------------------- #
def Submit(button_text='Submit', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
           bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  OPEN BUTTON Element lazy function  ------------------------- #
# -------------------------  OPEN BUTTON Element lazy function  ------------------------- #
def Open(button_text='Open', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
         bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  OK BUTTON Element lazy function  ------------------------- #
def OK(button_text='OK', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
       bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Ok(button_text='Ok', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
       bind_return_key=True, tooltip=None, font=None, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  CANCEL BUTTON Element lazy function  ------------------------- #
def Cancel(button_text='Cancel', size=(None, None), auto_size_button=None, button_color=None, disabled=False,
           tooltip=None, font=None, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  QUIT BUTTON Element lazy function  ------------------------- #
def Quit(button_text='Quit', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
         font=None, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  Exit BUTTON Element lazy function  ------------------------- #
def Exit(button_text='Exit', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
         font=None, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Yes(button_text='Yes', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
        font=None, bind_return_key=True, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  NO BUTTON Element lazy function  ------------------------- #
def No(button_text='No', size=(None, None), auto_size_button=None, button_color=None, disabled=False, tooltip=None,
       font=None, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  NO BUTTON Element lazy function  ------------------------- #
def Help(button_text='Help', size=(None, None), auto_size_button=None, button_color=None, disabled=False, font=None,
         tooltip=None, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
def SimpleButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                 border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                 font=None, bind_return_key=False, disabled=False, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  CLOSE BUTTON Element lazy function  ------------------------- #
def CloseButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
                bind_return_key=False, disabled=False, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


CButton = CloseButton


# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
def ReadButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
               border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
               bind_return_key=False, disabled=False, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_READ_FORM, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


ReadFormButton = ReadButton
RButton = ReadFormButton


# -------------------------  Realtime BUTTON Element lazy function  ------------------------- #
def RealtimeButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                   border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                   font=None, disabled=False, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_REALTIME, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, disabled=disabled, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


# -------------------------  Dummy BUTTON Element lazy function  ------------------------- #
def DummyButton(button_text, image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,
                border_width=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None, font=None,
                disabled=False, bind_return_key=False, focus=False, pad=None, key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_CLOSES_WIN_ONLY, image_filename=image_filename,
                  image_data=image_data, image_size=image_size, image_subsample=image_subsample,
                  border_width=border_width, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  button_color=button_color, font=font, disabled=disabled, bind_return_key=bind_return_key, focus=focus,
                  pad=pad, key=key, metadata=metadata)


# -------------------------  Calendar Chooser Button lazy function  ------------------------- #
def CalendarButton(button_text, target=(None, None), close_when_date_chosen=True, default_date_m_d_y=(None, None, None),
                   image_filename=None, image_data=None, image_size=(None, None),
                   image_subsample=None, tooltip=None, border_width=None, size=(None, None), auto_size_button=None,
                   button_color=None, disabled=False, font=None, bind_return_key=False, focus=False, pad=None,
                   key=None, metadata=None):
    button = Button(button_text=button_text, button_type=BUTTON_TYPE_CALENDAR_CHOOSER, target=target,
                    image_filename=image_filename, image_data=image_data, image_size=image_size,
                    image_subsample=image_subsample, border_width=border_width, tooltip=tooltip, size=size,
                    auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                    bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)
    button.CalendarCloseWhenChosen = close_when_date_chosen
    button.DefaultDate_M_D_Y = default_date_m_d_y
    return button


# -------------------------  Calendar Chooser Button lazy function  ------------------------- #
def ColorChooserButton(button_text, target=(None, None), image_filename=None, image_data=None, image_size=(None, None),
                       image_subsample=None, tooltip=None, border_width=None, size=(None, None), auto_size_button=None,
                       button_color=None, disabled=False, font=None, bind_return_key=False, focus=False, pad=None,
                       key=None, metadata=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_COLOR_CHOOSER, target=target,
                  image_filename=image_filename, image_data=image_data, image_size=image_size,
                  image_subsample=image_subsample, border_width=border_width, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button, button_color=button_color, font=font, disabled=disabled,
                  bind_return_key=bind_return_key, focus=focus, pad=pad, key=key, metadata=metadata)


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


def PackFormIntoFrame(window, containing_frame, toplevel_win):

    border_depth = toplevel_win.BorderDepth if toplevel_win.BorderDepth is not None else DEFAULT_BORDER_WIDTH
    # --------------------------------------------------------------------------- #
    # ****************  Use FlexForm to build the tkinter window ********** ----- #
    # Building is done row by row.                                                #
    # --------------------------------------------------------------------------- #
    focus_set = False
    ######################### LOOP THROUGH ROWS #########################
    # *********** -------  Loop through ROWS  ------- ***********#
    for row_num, flex_row in enumerate(window.Rows):
        ######################### LOOP THROUGH ELEMENTS ON ROW #########################
        # *********** -------  Loop through ELEMENTS  ------- ***********#
        # *********** Make TK Row                             ***********#
        qt_row_layout = QHBoxLayout()
        for col_num, element in enumerate(flex_row):
            element.ParentForm = toplevel_win  # save the button's parent form object
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
                # style += 'border: 0px solid gray; '
                style = style_generate('QGroupBox', style)
                column_widget.setStyleSheet(style)

                column_layout = QFormLayout()
                column_vbox = QVBoxLayout()
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
                style.add(color=(element.TextColor, COLOR_SYSTEM_DEFAULT))
                style.add(background_color=(element.BackgroundColor, COLOR_SYSTEM_DEFAULT))
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
                    QT_RadioButtonGroup = toplevel_win.RadioDict[element.GroupID]
                else:
                    QT_RadioButtonGroup = QButtonGroup(toplevel_win.QTApplication)
                    toplevel_win.RadioDict[element.GroupID] = QT_RadioButtonGroup

                QT_RadioButtonGroup.addButton(element.QT_Radio_Button)

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
                window.QT_QTabWidget.addTab(tab_widget, element.Title)
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
                style = 'QTableWidget {'
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


# ------------------------------------------------------------------------------------------------ #
# A print-like call that can be used to output to a multiline element as if it's an Output element #
# ------------------------------------------------------------------------------------------------ #

def print_to_element(multiline_element, *args, end=None, sep=None, text_color=None, background_color=None):
    """
    Print like Python normally prints except route the output to a multline element and also add colors if desired

    :param multiline_element: (Multiline) The multiline element to be output to
    :param args: List[Any] The arguments to print
    :param end: (str) The end char to use just like print uses
    :param sep: (str) The separation character like print uses
    :param text_color: The color of the text
    :param background_color: The background color of the line
    """
    sepchar = sep if sep is not None else ' '
    endchar = end if end is not None else '\n'

    outstring = ''
    for arg in args:
        outstring += str(arg) + sepchar
    outstring += endchar
    multiline_element.update(outstring, append=True, text_color_for_value=text_color, background_color_for_value=background_color)



# ========================  Scrolled Text Box   =====#
# ===================================================#
def PopupScrolled(*args, button_color=None, yes_no=False, auto_close=False, auto_close_duration=None,
                  size=(None, None), location=(None, None), title=None, non_blocking=False):
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
    :param index: (str) the name of the index into the Look and Feel table (does not have to be exact, can be "fuzzy")
    :param force: (bool) no longer used
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
        ix = randint(0, len(lf_values) - 1)
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

    _title = title if title is not None else args_to_print[0]
    _title = str(_title)
    window = Window(_title, auto_size_text=True, background_color=background_color, button_color=button_color,
                    auto_close=auto_close, auto_close_duration=auto_close_duration, icon=icon, font=font,
                    no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)
    max_line_total, total_lines = 0, 0
    layout = []
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
        PopupButton = CloseButton
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
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=POPUP_BUTTONS_NO_BUTTONS,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupNonBlocking ---------------------------
def PopupNonBlocking(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
                     auto_close=False, auto_close_duration=None, non_blocking=True, icon=DEFAULT_WINDOW_ICON,
                     line_width=None, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False,
                     location=(None, None)):
    """
        Show Popup box and immediately return (does not block)
    :param args:
    :param title:
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
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


PopupNoWait = PopupNonBlocking


# --------------------------- PopupQuick - a NonBlocking, Self-closing Popup  ---------------------------
def PopupQuick(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
               auto_close=True, auto_close_duration=2, non_blocking=True, icon=DEFAULT_WINDOW_ICON, line_width=None,
               font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
        Show Popup box that doesn't block and closes itself
    :param args:
    :param title:
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
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupQuick - a NonBlocking, Self-closing Popup with no titlebar and no buttons ---------------------------
def PopupQuickMessage(*args, title=None, button_type=POPUP_BUTTONS_NO_BUTTONS, button_color=None, background_color=None,
                      text_color=None,
                      auto_close=True, auto_close_duration=3, non_blocking=True, icon=DEFAULT_WINDOW_ICON,
                      line_width=None,
                      font=None, no_titlebar=True, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
        Show Popup box that doesn't block and closes itself
    :param args:
    :param title:
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
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupNoTitlebar ---------------------------
def PopupNoTitlebar(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
                    auto_close=False, auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON,
                    line_width=None, font=None, grab_anywhere=True, keep_on_top=False, location=(None, None)):
    """
        Display a Popup without a titlebar.   Enables grab anywhere so you can move it
    :param args:
    :param title:
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
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=True, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


PopupNoFrame = PopupNoTitlebar
PopupNoBorder = PopupNoTitlebar
PopupAnnoying = PopupNoTitlebar


# --------------------------- PopupAutoClose ---------------------------
def PopupAutoClose(*args, title=None, button_type=POPUP_BUTTONS_OK, button_color=None, background_color=None, text_color=None,
                   auto_close=True, auto_close_duration=DEFAULT_AUTOCLOSE_TIME, non_blocking=False, icon=DEFAULT_WINDOW_ICON,
                   line_width=None, font=None, no_titlebar=False, grab_anywhere=False, keep_on_top=False,
                   location=(None, None)):
    """
        Popup that closes itself after some time period
    :param args:
    :param title:
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
    Popup(*args, title=title, button_color=button_color, background_color=background_color, text_color=text_color,
          button_type=button_type,
          auto_close=auto_close, auto_close_duration=auto_close_duration, non_blocking=non_blocking, icon=icon,
          line_width=line_width,
          font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


PopupTimed = PopupAutoClose


# --------------------------- PopupError ---------------------------
def PopupError(*args, title=None, button_color=(None, None), background_color=None, text_color=None, auto_close=False,
               auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
               no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
        Popup with colored button and 'Error' as button text
    :param args:
    :param title:
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
    tbutton_color = DEFAULT_ERROR_BUTTON_COLOR if button_color == (None, None) else button_color
    Popup(*args, title=title, button_type=POPUP_BUTTONS_ERROR, background_color=background_color, text_color=text_color,
          non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=tbutton_color, auto_close=auto_close,
          auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
          keep_on_top=keep_on_top, location=location)


# --------------------------- PopupCancel ---------------------------
def PopupCancel(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
                auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None,
                no_titlebar=False, grab_anywhere=False, keep_on_top=False, location=(None, None)):
    """
        Display Popup with "cancelled" button text
    :param args:
    :param title:
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
    Popup(*args, title=title, button_type=POPUP_BUTTONS_CANCELLED, background_color=background_color, text_color=text_color,
          non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color, auto_close=auto_close,
          auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
          keep_on_top=keep_on_top, location=location)


# --------------------------- PopupOK ---------------------------
def PopupOK(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
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
    Popup(*args, title=title, button_type=POPUP_BUTTONS_OK, background_color=background_color, text_color=text_color,
          non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color, auto_close=auto_close,
          auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere,
          keep_on_top=keep_on_top, location=location)


# --------------------------- PopupOKCancel ---------------------------
def PopupOKCancel(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
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
    return Popup(*args, title=title, button_type=POPUP_BUTTONS_OK_CANCEL, background_color=background_color, text_color=text_color,
                 non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color,
                 auto_close=auto_close, auto_close_duration=auto_close_duration, font=font, no_titlebar=no_titlebar,
                 grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)


# --------------------------- PopupYesNo ---------------------------
def PopupYesNo(*args, title=None, button_color=None, background_color=None, text_color=None, auto_close=False,
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
    return Popup(*args, title=title, button_type=POPUP_BUTTONS_YES_NO, background_color=background_color, text_color=text_color,
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
        if Window.QTApplication is None:
            Window.QTApplication = QApplication(sys.argv)

        folder_name = QFileDialog.getExistingDirectory(dir=initial_folder)
        return folder_name

    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=size, key='_INPUT_'), FolderBrowse(initial_folder=initial_folder)],
              [CloseButton('Ok', size=(60, 20), bind_return_key=True), CloseButton('Cancel', size=(60, 20))]]

    _title = title if title is not None else message
    window = Window(title=_title, layout=layout, icon=icon, auto_size_text=True, button_color=button_color,
                    background_color=background_color,
                    font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    button, values = window.Read()

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

    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=(30,1), key='_INPUT_'), browse_button],
              [CButton('Ok', size=(60, 20), bind_return_key=True), CButton('Cancel', size=(60, 20))]]

    _title = title if title is not None else message

    window = Window(title=_title, layout=layout, icon=icon, auto_size_text=True, button_color=button_color, font=font,
                    background_color=background_color,
                    no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)

    button, values = window.Read()
    # window.Close()
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
              [InputText(default_text=default_text, size=size, password_char=password_char, key='_INPUT_')],
              [CloseButton('Ok', size=(60, 20), bind_return_key=True), CloseButton('Cancel', size=(60, 20))]]

    _title = title if title is not None else message

    window = Window(title=_title, layout=layout, icon=icon, auto_size_text=True, button_color=button_color, no_titlebar=no_titlebar,
                    background_color=background_color, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    button, values = window.Read()

    if button != 'Ok':
        return None
    else:
        return values['_INPUT_']


def main():
    theme('SystemDefaultForReal')

    # preview_all_look_and_feel_themes()
    # ChangeLookAndFeel('Dark Red')
    # theme('Dark Red')
    # SetOptions(progress_meter_color=(COLOR_SYSTEM_DEFAULT))
    # SetOptions(element_padding=(0,0))
    # ------ Menu Definition ------ #
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
         MultilineOutput(size=(250, 75), default_text='Multiline Output', tooltip='Multiline output')],
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
        [Slider(range=(0, 100), orientation='v', size=(3, 30), default_value=40, tooltip='Slider'),
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
        [Text('You are running the PySimpleGUI.py file itself', font=('ANY', 15, 'Bold'), text_color='red')],
                  [Text('You should be importing it rather than running it', font='ANY 15')],
        [Text('VERSION {}'.format(__version__), size=(85,1), text_color='red', font='ANY 18')],

        # [Image(data_base64=logo, tooltip='Image', click_submits=True, key='_IMAGE_'),
         [Frame('Input Text Group', frame1, title_color='red', tooltip='Text Group'), Stretch()],
        [Frame('Multiple Choice Group', frame2, title_color='green'),
         Frame('Binary Choice Group', frame3, title_color='purple'),
         Frame('Variable Choice Group', frame4, title_color='blue'), Stretch()],
        [Frame('Structured Data Group', frame5, title_color='red'), ],
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
        event, values = window.Read(timeout=10)
        print(event, values) if event != TIMEOUT_KEY else None
        if event is None or event == 'Exit':
            break
        if values['_MENU_'] == 'Pause Graph':
            graph_paused = not graph_paused
        if event == 'About...':
            Popup('You are running PySimpleGUIQt', 'The version number is', version)
        if not graph_paused:
            i += 1

            if i < 600:
                graph_elem.DrawLine((i, 0), (i, randint(0, 300)), width=1,
                                    color='#{:06x}'.format(randint(0, 0xffffff)))
            else:
                graph_elem.Move(-1, 0)
                graph_elem.DrawLine((i, 0), (i, randint(0, 300)), width=1,
                                    color='#{:06x}'.format(randint(0, 0xffffff)))

        window.FindElement('+PROGRESS+').UpdateBar(i % 600)
        window.FindElement('_PROGTEXT_').Update((i % 600) // 6)

        # TimerStop()
    window.Close()



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
