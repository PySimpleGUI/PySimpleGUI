#!/usr/bin/python3
import sys
import types
import datetime
import textwrap
import pickle
import base64
import calendar

FORCE_PYQT5 = False

if not FORCE_PYQT5:
    try:
        from PySide2.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QComboBox, QFormLayout, QVBoxLayout, \
            QHBoxLayout, QListWidget, QDial, QTableWidget
        from PySide2.QtWidgets import QSlider, QCheckBox, QRadioButton, QSpinBox, QPushButton, QTextEdit, QMainWindow, QDialog, QAbstractItemView
        from PySide2.QtWidgets import QSpacerItem, QFrame, QGroupBox, QTextBrowser, QPlainTextEdit, QButtonGroup, QFileDialog, QTableWidget, QTabWidget, QTabBar, QTreeWidget, QTreeWidgetItem, QLayout, QTreeWidgetItemIterator, QProgressBar
        from PySide2.QtWidgets import QTableWidgetItem, QGraphicsView, QGraphicsScene, QGraphicsItemGroup, QMenu, QMenuBar, QAction, QSystemTrayIcon, QColorDialog
        from PySide2.QtGui import QPainter, QPixmap, QPen, QColor, QBrush, QPainterPath, QFont, QImage, QIcon
        from PySide2.QtCore import Qt,QProcess, QEvent, QSize
        import PySide2.QtGui as QtGui
        import PySide2.QtCore as QtCore
        import PySide2.QtWidgets as QtWidgets
        using_pyqt5 = False
    except:
        from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QComboBox, QFormLayout, QVBoxLayout, \
            QHBoxLayout, QListWidget, QDial, QTableWidget
        from PyQt5.QtWidgets import QSlider, QCheckBox, QRadioButton, QSpinBox, QPushButton, QTextEdit, QMainWindow, QDialog, QAbstractItemView
        from PyQt5.QtWidgets import QSpacerItem, QFrame, QGroupBox, QTextBrowser, QPlainTextEdit, QButtonGroup, QFileDialog, QTableWidget, QTabWidget, QTabBar, QTreeWidget, QTreeWidgetItem, QLayout, QTreeWidgetItemIterator, QProgressBar
        from PyQt5.QtWidgets import QTableWidgetItem, QGraphicsView, QGraphicsScene, QGraphicsItemGroup, QMenu, QMenuBar, QAction, QSystemTrayIcon, QColorDialog
        from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QBrush, QPainterPath, QFont, QImage, QIcon
        from PyQt5.QtCore import Qt,QProcess, QEvent, QSize
        import PyQt5.QtGui as QtGui
        import PyQt5.QtCore as QtCore
        import PyQt5.QtWidgets as QtWidgets
        using_pyqt5 = True
else:
    from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QComboBox, QFormLayout, QVBoxLayout, \
        QHBoxLayout, QListWidget, QDial, QTableWidget
    from PyQt5.QtWidgets import QSlider, QCheckBox, QRadioButton, QSpinBox, QPushButton, QTextEdit, QMainWindow, \
        QDialog, QAbstractItemView
    from PyQt5.QtWidgets import QSpacerItem, QFrame, QGroupBox, QTextBrowser, QPlainTextEdit, QButtonGroup, QFileDialog, \
        QTableWidget, QTabWidget, QTabBar, QTreeWidget, QTreeWidgetItem, QLayout, QTreeWidgetItemIterator, QProgressBar, QColorDialog
    from PyQt5.QtWidgets import QTableWidgetItem, QGraphicsView, QGraphicsScene, QGraphicsItemGroup, QMenu, QMenuBar, \
        QAction, QSystemTrayIcon
    from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor, QBrush, QPainterPath, QFont, QImage, QIcon
    from PyQt5.QtCore import Qt, QProcess, QEvent
    import PyQt5.QtGui as QtGui
    import PyQt5.QtCore as QtCore
    import PyQt5.QtWidgets as QtWidgets
    using_pyqt5 = True

"""
    The QT version if PySimpleGUI.
    Still being developed.  Very limited features.  Been in development for less than 2 days so don't expect much!!
    
    So far can interact with the basic Widgets and get button clicks back.  Can't yet read which button caused the event.
"""

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
DEFAULT_WINDOW_ICON = 'default_icon.ico'
DEFAULT_ELEMENT_SIZE = (250, 22)  # In PIXELS
DEFAULT_BUTTON_ELEMENT_SIZE = (80, 25 )  # In PIXELS
DEFAULT_MARGINS = (10, 5)  # Margins for each LEFT/RIGHT margin is first term
DEFAULT_ELEMENT_PADDING = (4, 2)  # Padding between elements (row, col) in pixels
# DEFAULT_ELEMENT_PADDING = (0, 0)  # Padding between elements (row, col) in pixels

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

RELIEF_TICK_POSITION_NO_TICKS = 'none'
RELIEF_TICK_POSITION_BOTH_SIDES = 'both'
RELIEF_TICK_POSITION_ABOVE = 'above'
RELIEF_TICK_POSITION_BELOW = 'below'
RELIEF_TICK_POSITION_LEFT = 'left'
RELIEF_TICK_POSITION_RIGHT = 'right'


DEFAULT_PROGRESS_BAR_COLOR = (GREENS[0], '#D0D0D0')  # a nice green progress bar
DEFAULT_PROGRESS_BAR_SIZE = (250, 20)  # Size of Progress Bar (characters for length, pixels for width)
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

# a shameful global variable. This represents the top-level window information. Needed because opening a second window is different than opening the first.
class MyWindows():
    def __init__(self):
        self.NumOpenWindows = 0
        self.user_defined_icon = None
        self.hidden_master_root = None
        self.QTApplication = None
        self.active_popups = {}
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
                 key=None, pad=None, tooltip=None, visible=True):

        if elem_type != ELEM_TYPE_GRAPH:
            self.Size = convert_tkinter_size_to_Qt(size)
        else:
            self.Size = size
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

    def TextClickedHandler(self, event):
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = self.DisplayText
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def ReturnKeyHandler(self, event):
        MyForm = self.ParentForm
        button_element = self.FindReturnKeyBoundButton(MyForm)
        if button_element is not None:
            button_element.ButtonCallBack()

    def ListboxSelectHandler(self, event):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def ComboboxSelectHandler(self, event):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def RadioHandler(self):
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()

    def CheckboxHandler(self):
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()

    def TabGroupSelectHandler(self, event):
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()

    def KeyboardHandler(self, event):
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()


    def Update(self, widget, background_color=None, text_color=None, font=None, visible=None):
        style = str(widget.styleSheet())
        if font is not None:
            style += create_style_from_font(font)
        if text_color is not None:
            style += 'color: %s;' % text_color
        if background_color is not None:
            style += 'background-color: %s;' % background_color
        # print(style)
        widget.setStyleSheet(style)
        set_widget_visiblity(widget, visible)



    def __del__(self):
        try:
            self.TKStringVar.__del__()
        except:
            pass
        try:
            self.TKIntVar.__del__()
        except:
            pass
        try:
            self.TKText.__del__()
        except:
            pass
        try:
            self.TKEntry.__del__()
        except:
            pass


# ---------------------------------------------------------------------- #
#                           Input Class                                  #
# ---------------------------------------------------------------------- #
class InputText(Element):
    def __init__(self, default_text='', size=(None, None), disabled=False, password_char='',
                 justification=None, background_color=None, text_color=None, font=None, tooltip=None,
                 change_submits=False, enable_events=False,
                 do_not_clear=False, key=None, focus=False, pad=None, visible=True):
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
        super().__init__(ELEM_TYPE_INPUT_TEXT, size=size, background_color=bg, text_color=fg, key=key, pad=pad,
                         font=font, tooltip=tooltip, visible=visible)


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


    def QtCallbackFocusInEvent(self,value):
        print('Got focus!')


    def QtCallbackTextChanged(self, value):
        if not self.ChangeSubmits:
            return
        element_callback_quit_mainloop(self)

    def QtCallbackReturnPressed(self):
        self.ReturnKeyHandler(None)
        return

    def Update(self, value=None, disabled=None, select=None, background_color=None, text_color=None, font=None, visible=None):
        if disabled is True:
            self.QT_QLineEdit.setDisabled(True)
        elif disabled is False:
            self.QT_QLineEdit.setDisabled(False)
        if value is not None:
            self.QT_QLineEdit.setText(str(value))
            self.DefaultText = value
        if select:
            self.QT_QLineEdit.setSelection(0,QtGui.QTextCursor.End )
        super().Update(self.QT_QLineEdit, background_color=background_color, text_color=text_color, font=font, visible=visible)



    def Get(self):
        return self.QT_QLineEdit.text()
        return self.QT_QLineEdit.text()
        # return self.TKStringVar.get()

    def SetFocus(self):
        self.QT_QLineEdit.setFocus()

    def __del__(self):
        super().__del__()


# -------------------------  INPUT TEXT Element lazy functions  ------------------------- #
In = InputText
Input = InputText


# ---------------------------------------------------------------------- #
#                           Combo                                        #
# ---------------------------------------------------------------------- #
class Combo(Element):
    def __init__(self, values, default_value=None, size=(None, None), auto_size_text=None, background_color=None,
                 text_color=None, change_submits=False, enable_events=False, disabled=False, key=None, pad=None, tooltip=None,
                 readonly=False, visible_items=10, font=None, auto_complete=True, visible=True):
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
        self.QT_ComboBox = None
        super().__init__(ELEM_TYPE_INPUT_COMBO, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible)


    def QtCurrentItemChanged(self, state):
        if self.ChangeSubmits:
            element_callback_quit_mainloop(self)


    def Qt_init(self):
        self.QT_ComboBox = QComboBox()
        self.QT_ComboBox.addItems(self.Values)


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



    def __del__(self):
        try:
            self.TKCombo.__del__()
        except:
            pass
        super().__del__()


# -------------------------  INPUT COMBO Element lazy functions  ------------------------- #
InputCombo = Combo
DropDown = InputCombo
Drop = InputCombo


# ---------------------------------------------------------------------- #
#                           Option Menu                                  #
# ---------------------------------------------------------------------- #
class OptionMenu(Element):
    def __init__(self, values, default_value=None, size=(None, None), disabled=False, auto_size_text=None,
                 background_color=None, text_color=None, key=None, pad=None, tooltip=None, visible=True):
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
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, visible=visible)

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

    def __del__(self):
        try:
            self.TKOptionMenu.__del__()
        except:
            pass
        super().__del__()


# -------------------------  OPTION MENU Element lazy functions  ------------------------- #
InputOptionMenu = OptionMenu


# ---------------------------------------------------------------------- #
#                           Listbox                                      #
# ---------------------------------------------------------------------- #
class Listbox(Element):
    def __init__(self, values, default_values=None, select_mode=None, change_submits=False, enable_events=False, bind_return_key=False,
                 size=(None, None), disabled=False, auto_size_text=None, font=None, background_color=None,
                 text_color=None, key=None, pad=None, tooltip=None, visible=True):
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
        self.QT_ListWidget = None

        super().__init__(ELEM_TYPE_INPUT_LISTBOX, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=bg, text_color=fg, key=key, pad=pad, tooltip=tooltip, visible=visible)

    def QtCurrentRowChanged(self, state):
        if self.ChangeSubmits:
            element_callback_quit_mainloop(self)


    def Update(self, values=None, disabled=None, set_to_index=None,background_color=None, text_color=None, font=None, visible=None):
        if values is not None:
            self.Values = values
            for i in range(self.QT_ListWidget.count()):
                self.QT_ListWidget.takeItem(0)
            self.QT_ListWidget.addItems(values)
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

    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Radio                                        #
# ---------------------------------------------------------------------- #
class Radio(Element):
    def __init__(self, text, group_id, default=False, disabled=False, size=(None, None), auto_size_text=None,
                 background_color=None, text_color=None, font=None, key=None, pad=None, tooltip=None,
                 change_submits=False,  enable_events=False, visible=True):
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
        self.ChangeSubmits = change_submits or enable_events
        self.QT_Radio_Button = None

        super().__init__(ELEM_TYPE_INPUT_RADIO, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip, visible=visible)

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



    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Checkbox                                     #
# ---------------------------------------------------------------------- #
class Checkbox(Element):
    def __init__(self, text, default=False, size=(None, None), auto_size_text=None, font=None, background_color=None,
                 text_color=None, change_submits=False, enable_events=False, disabled=False, key=None, pad=None, tooltip=None, visible=True):
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
        self.QT_Checkbox = None

        super().__init__(ELEM_TYPE_INPUT_CHECKBOX, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip, visible=visible)

    def QtCallbackStateChanged(self, state):
        if self.ChangeSubmits:
            element_callback_quit_mainloop(self)


    def Get(self):
        return self.TKIntVar.get()

    def Update(self, value=None, disabled=None, background_color=None, text_color=None, font=None, visible=None):
        self.QT_Checkbox.setChecked(value or False)
        if disabled == True:
            self.QT_Checkbox.setDisabled(True)
        elif disabled == False:
            self.QT_Checkbox.setDisabled(False)
        super().Update(self.QT_Checkbox, background_color=background_color, text_color=text_color, font=font, visible=visible)

    def __del__(self):
        super().__del__()


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
                 tooltip=None, visible=True):
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
        self.QT_Spinner = None

        super().__init__(ELEM_TYPE_INPUT_SPIN, size, auto_size_text, font=font, background_color=bg, text_color=fg,
                         key=key, pad=pad, tooltip=tooltip, visible=visible)
        return


    def QtCallbackValueChanged(self, value):
        if not self.ChangeSubmits:
            return
        element_callback_quit_mainloop(self)

    def Update(self, value=None, values=None, disabled=None, background_color=None, text_color=None, font=None, visible=None):
        if values != None:
            self.Values = values
            self.QT_Spinner.setRange(self.Values[0], self.Values[1])
        if value is not None:
            self.QT_Spinner.setValue(value)
            self.DefaultValue = value
        if disabled == True:
            self.QT_Spinner.setDisabled(True)
        elif disabled == False:
            self.QT_Spinner.setDisabled(False)
        super().Update(self.QT_Spinner, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Multiline                                    #
# ---------------------------------------------------------------------- #
class Multiline(Element, QWidget):
    def __init__(self, default_text='', enter_submits=False, disabled=False, autoscroll=False, size=(None, None),
                 auto_size_text=None, background_color=None, text_color=None, change_submits=False, enable_events=False, do_not_clear=False,
                 key=None, focus=False,
                 font=None, pad=None, tooltip=None, visible=True):
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
            tsize = convert_tkinter_size_to_Qt(size)
        self.QT_TextEdit = None

        super().__init__(ELEM_TYPE_INPUT_MULTILINE, size=tsize, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible)
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
                    self.Element.ReturnKeyHandler(0)
            if event.type() == QEvent.FocusIn and widget is self.QT_TextEdit:
                self.Element.ParentForm.FocusElement = self.Element
            return QWidget.eventFilter(self, widget, event)


    def QtCallbackTextChanged(self):
        if not self.ChangeSubmits:
            return
        element_callback_quit_mainloop(self)


    def Update(self, value=None, disabled=None, append=False, background_color=None, text_color=None, font=None, visible=None):
        if value is not None and not append:
            self.DefaultText = value
            self.QT_TextEdit.setText(str(value))
        elif value is not None and append:
            self.DefaultText = value
            self.QT_TextEdit.setText(self.QT_TextEdit.toPlainText() + str(value))
        if disabled == True:
            self.QT_TextEdit.setDisabled(True)
        elif disabled == False:
            self.QT_TextEdit.setDisabled(False)
        super().Update(self.QT_TextEdit, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def Get(self):
        self.QT_TextEdit.toPlainText()

    def SetFocus(self):
        self.QT_TextEdit.setFocus()


    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           ScrolledOutput                               #
# ---------------------------------------------------------------------- #
class MultilineOutput(Element):
    def __init__(self, default_text='', enter_submits=False, disabled=False, autoscroll=False, size=(None, None), auto_size_text=None, background_color=None, text_color=None, change_submits=False, enable_events=False, do_not_clear=False, key=None, focus=False, font=None, pad=None, tooltip=None, visible=True):
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
        self.QT_TextBrowser = None

        super().__init__(ELEM_TYPE_MULTILINE_OUTPUT, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT, visible=visible)
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

    def __del__(self):
        super().__del__()





# ---------------------------------------------------------------------- #
#                                       Text                             #
# ---------------------------------------------------------------------- #
class Text(Element):
    def __init__(self, text, size=(None, None),  auto_size_text=None, click_submits=None, enable_events=False, relief=None, font=None, text_color=None, background_color=None, justification=None, pad=None, margins=None, key=None, tooltip=None, visible=True):
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
        self.DisplayText = text
        self.TextColor = text_color if text_color else DEFAULT_TEXT_COLOR
        self.Justification = justification or 'left'
        self.Relief = relief
        self.ClickSubmits = click_submits or enable_events
        self.Margins = margins
        if background_color is None:
            bg = DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR
        else:
            bg = background_color
        self.QT_Label = None

        super().__init__(ELEM_TYPE_TEXT, size, auto_size_text, background_color=bg, font=font if font else DEFAULT_FONT,
                         text_color=self.TextColor, pad=pad, key=key, tooltip=tooltip)
        return

    def QtCallbackTextClicked(self, event):
        if not self.ClickSubmits:
            return
        element_callback_quit_mainloop(self)

    def Update(self, value=None, background_color=None, text_color=None, font=None, visible=None):
        if value is not None:
            self.DisplayText = str(value)
            self.QT_Label.setText(str(value))
        super().Update(self.QT_Label, background_color=background_color, text_color=text_color, font=font, visible=visible)


    def __del__(self):
        super().__del__()


# -------------------------  Text Element lazy functions  ------------------------- #
Txt = Text
T = Text


# ---------------------------------------------------------------------- #
#                           Output                                       #
#  Routes stdout, stderr to a scrolled window                            #
# ---------------------------------------------------------------------- #
class Output(Element):
    def __init__(self, size=(None, None), background_color=None, text_color=None, pad=None, font=None, tooltip=None,
                 key=None, visible=True):
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
        self.QT_TextBrowser = None

        tsize = convert_tkinter_size_to_Qt(size) if size[0] is not None and size[0] < 100 else size

        super().__init__(ELEM_TYPE_OUTPUT, size=tsize, background_color=bg, text_color=fg, pad=pad, font=font,
                         tooltip=tooltip, key=key, visible=visible)

    def reroute_stdout(self):
        self.my_stdout = sys.stdout
        self.my_stderr = sys.stderr
        sys.stdout = self
        sys.stderr = self


    def write(self, m):
        self.QT_TextBrowser.moveCursor(QtGui.QTextCursor.End)
        self.QT_TextBrowser.insertPlainText( str(m))

        # if self.my_stdout:
        #     self.my_stdout.write(str(m))


    def Output(self,value=None, background_color=None, text_color=None, font=None):
        if value is not None:
            self.QT_TextBrowser.setText(value)
        super().Update(self.QT_TextBrowser, background_color=background_color, text_color=text_color, font=font)


    def __del__(self):
        sys.stdout = self.my_stdout
        sys.stderr = self.my_stderr
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Button Class                                 #
# ---------------------------------------------------------------------- #
class Button(Element):
    def __init__(self, button_text='', button_type=BUTTON_TYPE_READ_FORM, target=(None, None), tooltip=None,
                 file_types=(("ALL Files", "*.*"),), initial_folder=None, disabled=False, change_submits=False, enable_events=False,
                 image_filename=None, image_data=None, image_size=(None, None), image_subsample=None, border_width=None,
                 size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False,
                 focus=False, pad=None, key=None, visible=True):
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
        self.ButtonText = button_text
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
        # self.temp_size = size if size != (NONE, NONE) else

        super().__init__(ELEM_TYPE_BUTTON, size=size, font=font, pad=pad, key=key, tooltip=tooltip, text_color=self.TextColor, background_color=self.BackgroundColor, visible=visible)
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
    def ButtonCallBack(self):
        global _my_windows


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
        filetypes = (("ALL Files", "*.*"),) if self.FileTypes is None else self.FileTypes
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
            if target_element.Type == ELEM_TYPE_BUTTON:
                target_element.ColorChosen = color
            else:
                target_element.Update(color)
        elif self.BType == BUTTON_TYPE_BROWSE_FILES:
            qt_types = convert_tkinter_filetypes_to_qt(self.FileTypes)
            file_name = QFileDialog.getOpenFileNames(dir=self.InitialFolder, filter=qt_types)
            if file_name != '':
                file_name = ';'.join(file_name[0])
                if target_element.Type == ELEM_TYPE_BUTTON:
                    target_element.FileOrFolderName = file_name
                else:
                    target_element.Update(file_name[0])
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
                _my_windows.Decrement()
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
            _my_windows.Decrement()
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


    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           ButtonMenu Class                             #
# ---------------------------------------------------------------------- #
class ButtonMenu(Element):
    def __init__(self, button_text ,menu_def, tooltip=None,disabled=False,
                 image_filename=None, image_data=None, image_size=(None, None), image_subsample=None,border_width=None,
                 size=(None, None), auto_size_button=None, button_color=None, font=None, pad=None, key=None, visible=True):
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
        self.QT_QPushButton = None
        self.IsButtonMenu = True
        self.MenuItemChosen = None

        # self.temp_size = size if size != (NONE, NONE) else

        super().__init__(ELEM_TYPE_BUTTONMENU, size=size, font=font, pad=pad, key=key, tooltip=tooltip, text_color=self.TextColor, background_color=self.BackgroundColor, visible=visible)
        return


    def QT_MenuItemChosenCallback(self, item_chosen):
        print('IN BUTTON MENU ITEM CALLBACK', item_chosen)
        self.Key = item_chosen.replace('&','')                   # fool the quit function into thinking this was a key
        element_callback_quit_mainloop(self)


    def Update(self, menu_definition=None, text=None, button_color=(None, None), font=None, visible=None):
        if menu_definition is not None:
            menu_def = menu_definition
            qmenu = QMenu(self.QT_QPushButton)
            qmenu.setTitle(menu_def[0])
            AddMenuItem(qmenu, menu_def[1], self)
            self.QT_QPushButton.setMenu(qmenu)
        super().Update(self.QT_QPushButton, background_color=button_color[1], text_color=button_color[0], font=font, visible=visible)



    def __del__(self):
        super().__del__()



# ---------------------------------------------------------------------- #
#                           ProgreessBar                                 #
# ---------------------------------------------------------------------- #
class ProgressBar(Element):
    def __init__(self, max_value, orientation=None, size=(None, None),start_value=0,  auto_size_text=None, bar_color=(None, None),
                 style=None, border_width=None, relief=None, key=None, pad=None, visible=True):
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
        self.StartValue = start_value
        tsize = size
        if size[0] is not None and size[0] < 100:
            tsize = size[0]*10, size[1]*3
        self.QT_QProgressBar = None

        super().__init__(ELEM_TYPE_PROGRESS_BAR, size=tsize, auto_size_text=auto_size_text, key=key, pad=pad, visible=visible)

    # returns False if update failed
    def UpdateBar(self, current_count, max=None):
        if max is not None:
            self.QT_QProgressBar.setMaximum(max)
        self.QT_QProgressBar.setValue(current_count)
        self.ParentForm.QTApplication.processEvents()  # refresh the window
        return True


    def Update(self, visible=None):
        super().Update(self.QT_QProgressBar, visible=visible)

    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Image                                        #
# ---------------------------------------------------------------------- #
class Image(Element):
    def __init__(self, filename=None, data=None, data_base64=None, background_color=None, size=(None, None), pad=None, key=None,
                 tooltip=None, click_submits=False,  enable_events=False, visible=True):
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
        self.QT_QLabel = None

        super().__init__(ELEM_TYPE_IMAGE, size=size, background_color=background_color, pad=pad, key=key,
                         tooltip=tooltip, visible=visible)
        return


    def QtCallbackImageClicked(self, event):
        if not self.ClickSubmits:
            return
        element_callback_quit_mainloop(self)


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

    def __del__(self):
        super().__del__()


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

    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Graph                                        #
# ---------------------------------------------------------------------- #
class Graph(Element):
    def __init__(self, canvas_size, graph_bottom_left, graph_top_right, background_color=None, pad=None, key=None,
                 tooltip=None, visible=True):
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
        self.QT_QGraphicsScene = None

        super().__init__(ELEM_TYPE_GRAPH, background_color=background_color, size=canvas_size, pad=pad, key=key,
                         tooltip=tooltip, visible=visible)
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



    def DrawCircle(self, center_location, radius, fill_color=None, line_color='black'):
        converted_point = self._convert_xy_to_canvas_xy(center_location[0], center_location[1])
        qcolor = QColor(line_color)
        pen = QPen(qcolor)
        qcolor = QColor(fill_color)
        brush = QBrush(qcolor)
        line = self.QT_QGraphicsScene.addEllipse(self.x+converted_point[0], self.y+converted_point[1],
                                           radius, radius, pen=pen, brush=brush)


    def DrawText(self, text, location, color='black', font=None, angle=0):
        converted_point = self._convert_xy_to_canvas_xy(location[0], location[1])

        qcolor = QColor(color)
        qpath = QPainterPath()
        _font = font or ('courier', 12)
        qfont = QFont(_font[0], _font[1])
        # qfont.setWeight(.5)

        qpath.addText(self.x+converted_point[0], self.y+converted_point[1], qfont, str(text))
        self.QT_QGraphicsScene.addPath(qpath, qcolor)


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

    def DrawRectangle(self, top_left, bottom_right, fill_color=None, line_color=None):
        converted_top_left = self._convert_xy_to_canvas_xy(top_left[0], top_left[1])
        converted_bottom_right = self._convert_xy_to_canvas_xy(bottom_right[0], bottom_right[1])
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        return self._TKCanvas2.create_rectangle(converted_top_left[0], converted_top_left[1], converted_bottom_right[0],
                                                converted_bottom_right[1], fill=fill_color, outline=line_color)


    def Erase(self):
        if self._TKCanvas2 is None:
            print('*** WARNING - The Graph element has not been finalized and cannot be drawn upon ***')
            print('Call Window.Finalize() prior to this operation')
            return None
        self._TKCanvas2.delete('all')

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

    @property
    def TKCanvas(self):
        if self._TKCanvas2 is None:
            print('*** Did you forget to call Finalize()? Your code should look something like: ***')
            print('*** form = sg.Window("My Form").Layout(layout).Finalize() ***')
        return self._TKCanvas2

    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Frame                                        #
# ---------------------------------------------------------------------- #
class Frame(Element):
    def __init__(self, title, layout, title_color=None, background_color=None, title_location=None,
                 relief=DEFAULT_FRAME_RELIEF, size=(None, None), font=None, pad=None, border_width=None, key=None,
                 tooltip=None, visible=True):
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
        self.QT_QGroupBox = None
        self.Layout(layout)

        super().__init__(ELEM_TYPE_FRAME, background_color=background_color, text_color=title_color, size=size,
                         font=font, pad=pad, key=key, tooltip=tooltip, visible=visible)
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


    def __del__(self):
        for row in self.Rows:
            for element in row:
                element.__del__()
        super().__del__()


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

    def __del__(self):
        super().__del__()


VSeperator = VerticalSeparator
VSep = VerticalSeparator


# ---------------------------------------------------------------------- #
#                           Separator                                    #
# ---------------------------------------------------------------------- #
class HorizontalSeparator(Element):
    def __init__(self, pad=None):
        '''
        VerticalSeperator - A separator that spans only 1 row in a vertical fashion
        :param pad:
        '''
        self.Orientation = 'horizontal'  # for now only vertical works

        super().__init__(ELEM_TYPE_SEPARATOR, pad=pad)

    def __del__(self):
        super().__del__()


HSeperator = HorizontalSeparator
HSep = HorizontalSeparator



# ---------------------------------------------------------------------- #
#                           Tab                                          #
# ---------------------------------------------------------------------- #
class Tab(Element):
    def __init__(self, title, layout, title_color=None, background_color=None, font=None, pad=None, disabled=False,
                 border_width=None, key=None, tooltip=None, visible=True):
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
        self.QT_QWidget = None

        self.Layout(layout)

        super().__init__(ELEM_TYPE_TAB, background_color=background_color, text_color=title_color, font=font, pad=pad,
                         key=key, tooltip=tooltip, visible=visible)
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

    def __del__(self):
        for row in self.Rows:
            for element in row:
                element.__del__()
        super().__del__()


# ---------------------------------------------------------------------- #
#                           TabGroup                                     #
# ---------------------------------------------------------------------- #
class TabGroup(Element):
    def __init__(self, layout, tab_location=None, title_color=None, selected_title_color=None, background_color=None,
                 font=None, change_submits=False, enable_events=False, pad=None, border_width=None, theme=None, key=None, tooltip=None, visible=True):
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
        self.QT_QTabWidget = None
        self.Layout(layout)

        super().__init__(ELEM_TYPE_TAB_GROUP, background_color=self.BackgroundColor, text_color=title_color, font=font,
                         pad=pad, key=key, tooltip=tooltip, visible=visible)
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

    def FindKeyFromTabName(self, tab_name):
        for row in self.Rows:
            for element in row:
                if element.Title == tab_name:
                    return element.Key
        return None


    def Update(self, visible=None):
        super().Update(self.QT_QTabWidget, visible=visible)

        return self

    def __del__(self):
        for row in self.Rows:
            for element in row:
                element.__del__()
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Slider                                       #
# ---------------------------------------------------------------------- #
class Slider(Element):
    def __init__(self, range=(None, None), default_value=None, resolution=None, tick_interval=None, orientation=None,
                 border_width=None, relief=None, change_submits=False, enable_events=False, disabled=False, size=(None, None), font=None,
                 background_color=None, text_color=None, key=None, pad=None, tooltip=None, visible=True):
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
        self.QT_Slider = None

        super().__init__(ELEM_TYPE_INPUT_SLIDER, size=temp_size, font=font, background_color=background_color,
                         text_color=text_color, key=key, pad=pad, tooltip=tooltip, visible=visible)
        return


    def QtCallbackValueChanged(self, value):
        if not self.ChangeSubmits:
            return
        element_callback_quit_mainloop(self)

    def Update(self, value=None, range=(None, None), disabled=None, visible=None):
        if value is not None:
            self.QT_Slider.setValue(int(value))
            self.DefaultValue = value
        if disabled == True:
            self.QT_Slider.setDisabled(True)
        elif disabled == False:
            self.QT_Slider.setDisabled(False)
        super().Update(self.QT_Slider, visible=visible)


    def SliderChangedHandler(self, event):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            pass # TODO  # kick the users out of the mainloop

    def __del__(self):
        super().__del__()

# ---------------------------------------------------------------------- #
#                           Dial                                       #
# ---------------------------------------------------------------------- #
class Dial(Element):
    def __init__(self, range=(None, None), default_value=None, resolution=None, tick_interval=None, orientation=None,
                 border_width=None, relief=None, change_submits=False, enable_events=False, disabled=False, size=(None, None), font=None,
                 background_color=None, text_color=None, key=None, pad=None, tooltip=None, visible=True):
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
        self.QT_Dial = None

        super().__init__(ELEM_TYPE_INPUT_DIAL, size=temp_size, font=font, background_color=background_color,
                         text_color=text_color, key=key, pad=pad, tooltip=tooltip, visible=visible)
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


    def QtCallbackValueChanged(self, value):
        if not self.ChangeSubmits:
            return
        element_callback_quit_mainloop(self)

    def __del__(self):
        super().__del__()



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

        super().__init__(ELEM_TYPE_STRETCH, size=size, font=font, background_color=background_color,
                         text_color=text_color, key=key, pad=pad, tooltip=tooltip)
        return


    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Column                                       #
# ---------------------------------------------------------------------- #
class Column(Element):
    def __init__(self, layout, background_color=None, size=(None, None), pad=None, scrollable=False, key=None, visible=True):
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
        self.QT_QGroupBox = None
        self.Layout(layout)

        super().__init__(ELEM_TYPE_COLUMN, background_color=bg, size=size, pad=pad, key=key, visible=visible)
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


    def __del__(self):
        for row in self.Rows:
            for element in row:
                element.__del__()
        super().__del__()



# ---------------------------------------------------------------------- #
#                           Menu                                       #
# ---------------------------------------------------------------------- #
class Menu(Element):
    def __init__(self, menu_definition, background_color=None, size=(None, None), tearoff=False, pad=None, key=None, visible=True):
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
        self.QT_QMenuBar = None
        super().__init__(ELEM_TYPE_MENUBAR, background_color=background_color, size=size, pad=pad, key=key, visible=visible)


    def QT_MenuItemChosenCallback(self, item_chosen):
        # print('IN MENU ITEM CALLBACK', item_chosen)
        self.MenuItemChosen = item_chosen.replace('&','')
        element_callback_quit_mainloop(self)
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


    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Table                                        #
# ---------------------------------------------------------------------- #
class Table(Element):
    def __init__(self, values, headings=None, visible_column_map=None, col_widths=None, def_col_width=10,
                 auto_size_columns=True, max_col_width=20, select_mode=None, display_row_numbers=False, num_rows=None,
                 font=None, justification='right', text_color=None, background_color=None, alternating_row_color=None,
                 size=(None, None), change_submits=False, enable_events=False, bind_return_key=False, pad=None, key=None, tooltip=None, visible=True):
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
        self.QT_TableWidget = None

        super().__init__(ELEM_TYPE_TABLE, text_color=text_color, background_color=background_color, font=font,
                         size=size, pad=pad, key=key, tooltip=tooltip, visible=visible)
        return


    def QtCallbackCellActivated(self, value=None):
        # print('CELL ACTIVATED ', value)
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if not self.ChangeSubmits:
            return
        element_callback_quit_mainloop(self)


    def QtCallbackVerticalHeader(self, value):
        print('Vertical Header value ', value)


    def Update(self, values=None, visible=None):
        if values is not None:
            self.Values = values
            self.SelectedRows = []
            self.QT_TableWidget.clear()
            self.QT_TableWidget.setRowCount(len(self.Values))
            self.QT_TableWidget.setColumnCount(len(self.Values[0]))
            for rownum, rows in enumerate(self.Values):
                # self.QT_TableWidget.insertRow(rownum)
                for colnum, columns in enumerate(rows):
                    self.QT_TableWidget.setItem(rownum, colnum, QTableWidgetItem(self.Values[rownum][colnum]))
        super().Update(self.QT_TableWidget, visible=visible)




    def treeview_selected(self, event):
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
        def __init__(self, window):
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





    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Tree                                         #
# ---------------------------------------------------------------------- #
class Tree(Element):
    def __init__(self, data=None, headings=None, visible_column_map=None, col_widths=None, col0_width=10,
                 def_col_width=10, auto_size_columns=True, max_col_width=20, select_mode=None, show_expanded=False,
                 change_submits=False, enable_events=False, font=None, size=(200,600),
                 justification='right', text_color=None, background_color=None, num_rows=None, pad=None, key=None,
                 tooltip=None, visible=True):
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
        self.QT_QTreeWidget = None
        super().__init__(ELEM_TYPE_TREE, text_color=text_color, background_color=background_color, font=font, pad=pad,
                         key=key, tooltip=tooltip, size=size, visible=visible)
        return

    def treeview_selected(self, event):
        selections = 000000
        self.SelectedRows = [x for x in selections]
        if self.ChangeSubmits:
            MyForm = self.ParentForm
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = ''
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.TKroot.quit()


    def Update(self, values=None, key=None, value=None, text=None, visible=None):
        if values is not None:
            self.TreeData = values
            self.SelectedRows = []
            # self.QT_QTreeWidget = QTreeWidget()
            TreeWidgetItems = QTreeWidgetItemIterator(self.QT_QTreeWidget)

            for item in TreeWidgetItems.Enabled:
                self.QT_QTreeWidget.removeItemWidget(item, 0)
            def add_treeview_data(node, widget):
                # print(f'Inserting {node.key} under parent {node.parent}')
                child = QTreeWidgetItem(widget)
                if node.key != '':
                    child.setText(0, str(node.text))
                    # child.setData(0,0,node.values)
                    if node.icon is not None:
                        qicon = QIcon(node.icon)
                        child.setIcon(0, qicon)
                for node in node.children:
                    add_treeview_data(node, child)
            add_treeview_data(self.TreeData.root_node, self.QT_QTreeWidget)
        if key is not None:
            pass
        super().Update(self.QT_QTreeWidget, visible=visible)

        return self

    def __del__(self):
        super().__del__()


class TreeData(object):
    class Node(object):
        def __init__(self, parent, key, text, values, icon):
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

    def __del__(self):
        super().__del__()


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

        global _my_windows

        if _my_windows.QTApplication is None:
            _my_windows.QTApplication = QApplication(sys.argv)
        self.App = _my_windows.QTApplication
        self.QWidget = QWidget()

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

        self.TrayIcon.messageClicked.connect(self.messageClicked)
        self.TrayIcon.activated.connect(self.doubleClicked)

        self.TrayIcon.show()

    def QT_MenuItemChosenCallback(self, item_chosen):
        self.MenuItemChosen = item_chosen.replace('&','')
        self.App.exit()                         # kick the users out of the mainloop

    # callback function when message is clicked
    def messageClicked(self):
        self.MenuItemChosen = EVENT_SYSTEM_TRAY_MESSAGE_CLICKED
        self.App.exit()


    def doubleClicked(self, reason):
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

    def timer_timeout(self):
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
            self.TrayIcon.showMessage(title, message, time)

        self.LastMessage = message
        self.LastTitle = title
        return self

    def Close(self):
        '''

        :return:
        '''
        self.TrayIcon.Hide()
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



# ------------------------------------------------------------------------- #
#                       Window CLASS                                      #
# ------------------------------------------------------------------------- #
class Window:

    def __init__(self, title, default_element_size=DEFAULT_ELEMENT_SIZE, default_button_element_size=(None, None),
                 auto_size_text=None, auto_size_buttons=None, location=(None, None), size=(None, None), element_padding=None, button_color=None, font=None,
                 progress_bar_color=(None, None), background_color=None, border_depth=None, auto_close=False,
                 auto_close_duration=DEFAULT_AUTOCLOSE_TIME, icon=DEFAULT_WINDOW_ICON, force_toplevel=False,
                 alpha_channel=1, return_keyboard_events=False, use_default_focus=True, text_justification=None,
                 no_titlebar=False, grab_anywhere=False, keep_on_top=False, resizable=False, disable_close=False, background_image=None):
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
        self.DefaultElementSize = convert_tkinter_size_to_Qt(default_element_size)
        self.DefaultButtonElementSize = convert_tkinter_size_to_Qt(default_button_element_size) if default_button_element_size != (
            None, None) else DEFAULT_BUTTON_ELEMENT_SIZE
        self.Location = location
        self.ButtonColor = button_color if button_color else DEFAULT_BUTTON_COLOR
        self.BackgroundColor = background_color if background_color else DEFAULT_BACKGROUND_COLOR
        self.ParentWindow = None
        self.Font = font if font else DEFAULT_FONT
        self.RadioDict = {}
        self.BorderDepth = border_depth
        self.WindowIcon = icon if icon is not None else _my_windows.user_defined_icon
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
        self._Size=size
        self.ElementPadding = element_padding or DEFAULT_ELEMENT_PADDING
        self.FocusElement = None
        self.BackgroundImage = background_image
        self.XFound = False

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

    def timer_timeout(self):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if self.TimerCancelled:
            return
        self.LastButtonClicked = self.TimeoutKey
        self.FormRemainedOpen = True
        if self.CurrentlyRunningMainloop:
            self.QTApplication.exit()  # kick the users out of the mainloop

    def autoclose_timer_callback(self):
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
                    _my_windows.Decrement()
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
                _my_windows.Decrement()
            # if form was closed with X
            if self.LastButtonClicked is None and self.LastKeyboardEvent is None and self.ReturnValues[0] is None:
                _my_windows.Decrement()
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
                _my_windows.Decrement()
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

    def FindElement(self, key):
        element = _FindElementFromKeyInSubForm(self, key)
        if element is None:
            print('*** WARNING = FindElement did not find the key. Please check your key\'s spelling ***')
            PopupError('Keyword error in FindElement Call',
                       'Bad key = {}'.format(key),
                       'Your bad line of code may resemble this:',
                       'window.FindElement("{}")'.format(key))
            return ErrorElement(key=key)
        return element

    Element = FindElement

    def FindElementWithFocus(self):
        return self.FocusElement
        element = _FindElementWithFocusInSubForm(self)
        return element

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
        if _my_windows.QTApplication is None:
            _my_windows.QTApplication = QApplication(sys.argv)
        try:
            screen = _my_windows.QTApplication.primaryScreen()
        except:
            return None, None
        size = screen.size()
        screen_width = size.width()
        screen_height = size.height()
        return screen_width, screen_height

    def Move(self, x, y):
        # TODO
        return

    def Minimize(self):
        # TODO
        return

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
        self.__del__()
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

    # IT FINALLY WORKED! 29-Oct-2018 was the first time this damned thing got called
    def OnClosingCallback(self):
        if self.DisableClose:
            return
        print('Got closing callback')
        self.TKroot.quit()  # kick the users out of the mainloop
        if self.CurrentlyRunningMainloop:  # quit if this is the current mainloop, otherwise don't quit!
            self.TKroot.destroy()  # kick the users out of the mainloop
        else:
            self.RootNeedsDestroying = True
        self.TKrootDestroyed = True

        return

    def Disable(self):
        # TODO
        return

    def Enable(self):
        # TODO
        return

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
        try:
            self.TKroot.lift()
        except:
            pass

    def CurrentLocation(self):
        return int(self.TKroot.winfo_x()), int(self.TKroot.winfo_y())

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



    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.__del__()
        return False

    def __del__(self):
        # print(f'+++++ Window {self.Title} being deleted +++++')
        for row in self.Rows:
            for element in row:
                element.__del__()


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
        element.ParentForm.QTApplication.exit()  # kick the users out of the mainloop


# =========================================================================== #
# Stops the mainloop and sets the event information                           #
# =========================================================================== #
def convert_tkinter_size_to_Qt(size):
    """
    Converts size in characters to size in pixels
    :param size:  size in characters, rows
    :return: size in pixels, pixels
    """
    qtsize = size
    if size[1] is not None and size[1] < 10:        # change from character based size to pixels (roughly)
        qtsize = size[0]*10, size[1]*25
    return qtsize



# =========================================================================== #
# Stops the mainloop and sets the event information                           #
# =========================================================================== #
def convert_tkinter_filetypes_to_qt(filetypes):
    qt_filetypes = ''
    for item in filetypes:
        filetype = item[0] + ' (' + item[1] + ');;'
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
    style += 'font-family: %s;' % _font[0]
    style += 'font-size: %spt;' % _font[1]
    font_items = ''
    for item in _font[2:]:
        if item == 'underline':
            style += 'text-decoration: underline;'
        else:
            font_items += item + ' '
    if font_items != '':
        style += 'font: %s;' % font_items
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
                 key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FOLDER, target=target,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  disabled=disabled, button_color=button_color, change_submits=change_submits, enable_events=enable_events, font=font, pad=pad,
                  key=key)


# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileBrowse(button_text='Browse', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), initial_folder=None,
               tooltip=None, size=(None, None), auto_size_button=None, button_color=None, change_submits=False, enable_events=False,
               font=None, disabled=False,
               pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, auto_size_button=auto_size_button,
                  change_submits=change_submits, enable_events=enable_events, disabled=disabled, button_color=button_color, font=font, pad=pad,
                  key=key)


# -------------------------  FILES BROWSE Element (Multiple file selection) lazy function  ------------------------- #
def FilesBrowse(button_text='Browse', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), disabled=False,
                initial_folder=None, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
                change_submits=False, enable_events=False,
                font=None, pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_BROWSE_FILES, target=target, file_types=file_types,
                  initial_folder=initial_folder, change_submits=change_submits, enable_events=enable_events, tooltip=tooltip, size=size,
                  auto_size_button=auto_size_button,
                  disabled=disabled, button_color=button_color, font=font, pad=pad, key=key)


# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileSaveAs(button_text='Save As...', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), initial_folder=None,
               disabled=False, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
               change_submits=False, enable_events=False, font=None,
               pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_SAVEAS_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, change_submits=change_submits, enable_events=enable_events,
                  font=font, pad=pad, key=key)


# -------------------------  SAVE AS Element lazy function  ------------------------- #
def SaveAs(button_text='Save As...', target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), initial_folder=None,
           disabled=False, tooltip=None, size=(None, None), auto_size_button=None, button_color=None,
           change_submits=False, enable_events=False, font=None,
           pad=None, key=None):
    return Button(button_text=button_text, button_type=BUTTON_TYPE_SAVEAS_FILE, target=target, file_types=file_types,
                  initial_folder=initial_folder, tooltip=tooltip, size=size, disabled=disabled,
                  auto_size_button=auto_size_button, button_color=button_color, change_submits=change_submits, enable_events=enable_events,
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
                    value = element.QT_ComboBox.currentText()
                elif element.Type == ELEM_TYPE_INPUT_OPTION_MENU:
                    value = 0
                elif element.Type == ELEM_TYPE_INPUT_LISTBOX:
                    try:
                        value= [item.text() for item in element.QT_ListWidget.selectedItems()]
                    except:
                        value = []
                elif element.Type == ELEM_TYPE_INPUT_SPIN:
                    value = str(element.QT_Spinner.value())
                elif element.Type == ELEM_TYPE_INPUT_DIAL:
                    value = str(element.QT_Dial.value())
                elif element.Type == ELEM_TYPE_INPUT_SLIDER:
                    value = element.QT_Slider.value()
                elif element.Type == ELEM_TYPE_INPUT_MULTILINE:
                    value = element.QT_TextEdit.toPlainText()
                    if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                        element.QT_TextEdit.setText('')
                elif element.Type == ELEM_TYPE_TAB_GROUP:
                    value = 0
                elif element.Type == ELEM_TYPE_TABLE:
                    value = []
                    indexes = element.QT_TableWidget.selectionModel().selectedRows()
                    for index in sorted(indexes):
                        value.append(index.row())
                elif element.Type == ELEM_TYPE_TREE:
                    value = 0
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
            if element.Type == ELEM_TYPE_INPUT_TEXT:
                if element.QT_QLineEdit is not None:
                    if element.QT_QLineEdit is element.TKEntry.focus_get():
                        return element


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
                action.triggered.connect(lambda: SystemTray.QT_MenuItemChosenCallback(element, sub_menu_info))
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
                action.triggered.connect(lambda: Menu.QT_MenuItemChosenCallback(element, sub_menu_info))
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

# ------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #
# =====================================   TK CODE STARTS HERE ====================================================== #
# ------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #

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
        tk_row_frame = 000000 #TODO get something to "pack into"
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

            # -------------------------  COLUMN element  ------------------------- #
            if element_type == ELEM_TYPE_COLUMN:
                # column_widget = QWidget()
                column_widget = QGroupBox()
                element.QT_QGroupBox = column_widget
                # column_widget.setFrameShape(QtWidgets.QFrame.NoFrame)

                style = create_style_from_font(font)
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'border: 0px solid gray; '
                column_widget.setStyleSheet(style)

                column_layout = QFormLayout()
                column_vbox = QVBoxLayout()

                PackFormIntoFrame(element, column_layout, toplevel_win)

                column_vbox.addLayout(column_layout)
                column_widget.setLayout(column_vbox)

                column_widget.setStyleSheet(style)
                if not element.Visible:
                    column_widget.setVisible(False)

                qt_row_layout.addWidget(column_widget)
            # -------------------------  TEXT element  ------------------------- #
            elif element_type == ELEM_TYPE_TEXT:
                element.QT_Label = qlabel = QLabel(element.DisplayText, toplevel_win.QTWindow)
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
                style = create_style_from_font(font)
                if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    style += 'background-color: %s;' % element.BackgroundColor
                element.QT_Label.setStyleSheet(style)

                if element.ClickSubmits:
                    element.QT_Label.mousePressEvent = element.QtCallbackTextClicked

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
            # -------------------------  BUTTON element  ------------------------- #
            elif element_type == ELEM_TYPE_BUTTON:
                btext = element.ButtonText
                btype = element.BType
                element.QT_QPushButton = QPushButton(btext)
                style = create_style_from_font(font)
                if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    style += 'background-color: %s;' % element.BackgroundColor
                if element.BorderWidth == 0:
                    style += 'border: none;'
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_QPushButton.setStyleSheet(style)
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
                element.QT_QPushButton.clicked.connect(element.ButtonCallBack)
                if not element.Visible:
                    element.QT_QPushButton.setVisible(False)

                qt_row_layout.addWidget(element.QT_QPushButton)
            # -------------------------  INPUT (Single Line) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_TEXT:
                default_text = element.DefaultText
                element.QT_QLineEdit = qlineedit = QLineEdit()

                if element.Justification[0] == 'c':
                    element.QT_QLineEdit.setAlignment(Qt.AlignCenter)
                elif element.Justification[0] == 'r':
                    element.QT_QLineEdit.setAlignment(Qt.AlignRight)

                element.QT_QLineEdit.setText(str(default_text))
                style = create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)

                element.QT_QLineEdit.setStyleSheet(style)

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
                    element.QT_QLineEdit.textChanged.connect(element.QtCallbackTextChanged)

                element.QT_QLineEdit.returnPressed.connect(element.QtCallbackReturnPressed)

                if element.PasswordCharacter != '':
                    qlineedit.setEchoMode(QLineEdit.Password)
                if element.Tooltip:
                    element.QT_QLineEdit.setToolTip(element.Tooltip)

                element.InputTextWidget = Input.InputTextWidget(element.QT_QLineEdit, element)
                element.QT_QLineEdit.installEventFilter(element.InputTextWidget)
                if not element.Visible:
                    element.QT_QLineEdit.setVisible(False)
                qt_row_layout.addWidget(element.QT_QLineEdit)
            # -------------------------  COMBO BOX (Drop Down) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_COMBO:
                element.QT_ComboBox = QComboBox()
                max_line_len = max([len(str(l)) for l in element.Values])
                if auto_size_text is False:
                    width = element_size[0]
                else:
                    width = max_line_len
                style = create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_ComboBox.setStyleSheet(style)

                if not auto_size_text:
                    if element_size[0] is not None:
                        element.QT_ComboBox.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_ComboBox.setFixedHeight(element_size[1])

                if element.Disabled:
                    element.QT_ComboBox.setDisabled(True)

                element.QT_ComboBox.addItems(element.Values)

                element.QT_ComboBox.setMaxVisibleItems(element.VisibleItems)
                if element.DefaultValue is not None:
                    for index, v in enumerate(element.Values):
                        if v == element.DefaultValue:
                            element.QT_ComboBox.setCurrentIndex(index)
                            break

                if element.ChangeSubmits:
                    element.QT_ComboBox.currentIndexChanged.connect(element.QtCurrentItemChanged)
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
            # -------------------------  LISTBOX element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_LISTBOX:
                max_line_len = max([len(str(l)) for l in element.Values]) if len(element.Values) != 0 else 0
                element.QT_ListWidget = QListWidget()
                style = ''
                style = create_style_from_font(font)

                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
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
                    element.QT_ListWidget.currentRowChanged.connect(element.QtCurrentRowChanged)

                element.QT_ListWidget.addItems(element.Values)
                if element.Tooltip:
                    element.QT_ListWidget.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_ListWidget.setVisible(False)
                qt_row_layout.addWidget(element.QT_ListWidget)
            # -------------------------  INPUT MULTI LINE element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_MULTILINE:
                default_text = element.DefaultText
                width, height = element_size
                element.QT_TextEdit = QTextEdit()
                style = create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_TextEdit.setStyleSheet(style)

                if element.AutoSizeText is False or toplevel_win.AutoSizeButtons is False or element.Size[0] is not None:
                    if element_size[0] is not None:
                        element.QT_TextEdit.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_TextEdit.setFixedHeight(element_size[1])

                if element.Disabled:
                    element.QT_TextEdit.setDisabled(True)

                element.MultiQWidget = Multiline.MultiQWidget(element.QT_TextEdit, element)
                element.QT_TextEdit.installEventFilter(element.MultiQWidget)

                if element.ChangeSubmits:
                    element.QT_TextEdit.textChanged.connect(element.QtCallbackTextChanged)

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
            # ------------------------- OUTPUT MULTI LINE element  ------------------------- #
            elif element_type == ELEM_TYPE_MULTILINE_OUTPUT:
                default_text = element.DefaultText
                width, height = element_size
                element.QT_TextBrowser = QTextBrowser()
                element.QT_TextBrowser.setDisabled(False)
                style = create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_TextBrowser.setStyleSheet(style)

                if element.AutoSizeText is False or toplevel_win.AutoSizeButtons is False or element.Size[0] is not None:
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
            # -------------------------  INPUT CHECKBOX element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_CHECKBOX:
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

                if element.AutoSizeText is False or toplevel_win.AutoSizeButtons is False or element.Size[0] is not None:
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
              # -------------------------  PROGRESS BAR element  ------------------------- #
            elif element_type == ELEM_TYPE_PROGRESS_BAR:
                element.QT_QProgressBar = QProgressBar()

                if element.Size[0] is not None:
                    if element_size[0] is not None:
                        element.QT_QProgressBar.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_QProgressBar.setFixedHeight(element_size[1])

                element.QT_QProgressBar.setMaximum(element.MaxValue)
                element.QT_QProgressBar.setValue(element.StartValue)

                style = ''
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_QProgressBar.setStyleSheet(style)

                element.QT_QProgressBar.setTextVisible(False)
                if element.Tooltip:
                    element.QT_QProgressBar.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_QProgressBar.setVisible(False)
                qt_row_layout.addWidget(element.QT_QProgressBar)
            # -------------------------  INPUT RADIO BUTTON element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_RADIO:
                default_value = element.InitialState
                ID = element.GroupID
                qradio = QRadioButton(element.Text)
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

                if element.AutoSizeText is False or toplevel_win.AutoSizeButtons is False or element.Size[0] is not None:
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

                # qt_row_layout.setContentsMargins(*full_element_pad)
                if element.Tooltip:
                    element.QT_Radio_Button.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_Radio_Button.setVisible(False)
                qt_row_layout.addWidget(element.QT_Radio_Button)
                # -------------------------  INPUT SPIN Box element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SPIN:
                width, height = element_size
                width = 0 if auto_size_text else element_size[0]
                element.QT_Spinner = QSpinBox()
                style = create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_Spinner.setStyleSheet(style)
                element.QT_Spinner.setRange(element.Values[0], element.Values[1])
                if not auto_size_text:
                    if element_size[0] is not None:
                        element.QT_Spinner.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_Spinner.setFixedHeight(element_size[1])

                if element.Disabled:
                    element.QT_Spinner.setDisabled(True)
                if element.ChangeSubmits:
                    element.QT_Spinner.valueChanged.connect(element.QtCallbackValueChanged)
                if element.Tooltip:
                    element.QT_Spinner.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_Spinner.setVisible(False)
                qt_row_layout.addWidget(element.QT_Spinner)
            # -------------------------  OUTPUT element  ------------------------- #
            elif element_type == ELEM_TYPE_OUTPUT:
                element.QT_TextBrowser = QTextBrowser()
                element.QT_TextBrowser.setDisabled(False)
                style = create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_TextBrowser.setStyleSheet(style)

                if element.AutoSizeText is False or toplevel_win.AutoSizeButtons is False or element.Size[0] is not None:
                    if element_size[0] is not None:
                        element.QT_TextBrowser.setFixedWidth(element_size[0])
                    if element_size[1] is not None:
                        element.QT_TextBrowser.setFixedHeight(element_size[1])

                element.QT_TextBrowser.moveCursor(QtGui.QTextCursor.End)
                element.reroute_stdout()
                if element.Tooltip:
                    element.QT_TextBrowser.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_TextBrowser.setVisible(False)
                qt_row_layout.addWidget(element.QT_TextBrowser)
            # -------------------------  IMAGE element  ------------------------- #
            elif element_type == ELEM_TYPE_IMAGE:
                qlabel = QLabel()
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

                element.QT_QLabel = qlabel
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
            # -------------------------  Canvas element  ------------------------- #
            elif element_type == ELEM_TYPE_CANVAS:
                width, height = element_size
            # -------------------------  Graph element  ------------------------- #
            elif element_type == ELEM_TYPE_GRAPH:
                width, height = element_size
                element.QT_QGraphicsView = qgraphicsview = QGraphicsView()
                # element.QT_QGraphicsView.setGeometry(0,0,element.CanvasSize[0],element.CanvasSize[1])
                element.QT_QGraphicsScene = QGraphicsScene()
                element.QT_QGraphicsScene.setSceneRect(0,0,element.CanvasSize[0],element.CanvasSize[1])
                element.QT_QGraphicsView.setScene(element.QT_QGraphicsScene)
                style = ''
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                element.QT_QGraphicsView.setStyleSheet(style)

                qgraphicsview.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                qgraphicsview.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                # qt_row_layout.setContentsMargins(*full_element_pad)
                if element.Tooltip:
                    element.QT_QGraphicsView.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_QGraphicsView.setVisible(False)
                qt_row_layout.addWidget(element.QT_QGraphicsView)
            # -------------------------  MENUBAR element  ------------------------- #
            elif element_type == ELEM_TYPE_MENUBAR:
                menu_def = element.MenuDefinition
                element.QT_QMenuBar = QMenuBar(toplevel_win.QT_QMainWindow)

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
                if not element.Visible:
                    element.QT_QMenuBar.setVisible(False)
                toplevel_win.QT_QMainWindow.setMenuBar(element.QT_QMenuBar)
            # -------------------------  BUTTONMENU element  ------------------------- #
            elif element_type == ELEM_TYPE_BUTTONMENU:
                btext = element.ButtonText
                element.QT_QPushButton = QPushButton(btext)
                style = create_style_from_font(font)
                if element.TextColor is not None and element.TextColor != COLOR_SYSTEM_DEFAULT:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    style += 'background-color: %s;' % element.BackgroundColor
                if element.BorderWidth == 0:
                    style += 'border: none;'
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
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
                # element.QT_QPushButton.clicked.connect(element.ButtonCallBack)

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
            # -------------------------  Frame element  ------------------------- #
            elif element_type == ELEM_TYPE_FRAME:
                column_widget = QGroupBox()
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
            # -------------------------  Tab element  ------------------------- #
            elif element_type == ELEM_TYPE_TAB:

                tab_widget = QWidget()
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
            # -------------------------  TabGroup element  ------------------------- #
            elif element_type == ELEM_TYPE_TAB_GROUP:

                element.QT_QTabWidget = qtab =QTabWidget()

                style = qtab.styleSheet()
                if element.SelectedTitleColor not in (None, COLOR_SYSTEM_DEFAULT):
                    style += 'QTabBar::tab:selected {background: %s;}'%element.SelectedTitleColor
                if element.BackgroundColor not in (None, COLOR_SYSTEM_DEFAULT):
                    style += 'QTabBar::tab {background: %s;}'% element.BackgroundColor
                if element.TextColor not in (None, COLOR_SYSTEM_DEFAULT):
                    style += 'QTabBar::tab {color: %s;}'%element.TextColor
                qtab.setStyleSheet(style)

                PackFormIntoFrame(element, element.ParentForm.QFormLayout, toplevel_win)

                qt_row_layout.addWidget(element.QT_QTabWidget)
                if not element.Visible:
                    element.QT_QTabWidget.setVisible(False)

                if element.ChangeSubmits:
                    pass
            # -------------------------  SLIDER element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SLIDER:
                element.QT_Slider = QSlider()
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
                    element.QT_Slider.valueChanged.connect(element.QtCallbackValueChanged)
                if element.Tooltip:
                    element.QT_Slider.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_Slider.setVisible(False)
                qt_row_layout.addWidget(element.QT_Slider)
            # -------------------------  DIAL element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_DIAL:
                element.QT_Dial = qdial = QDial()

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
                    element.QT_Dial.valueChanged.connect(element.QtCallbackValueChanged)
                if element.Tooltip:
                    element.QT_Dial.setToolTip(element.Tooltip)
                # qt_row_layout.setContentsMargins(*full_element_pad)
                if not element.Visible:
                    element.QT_Dial.setVisible(False)
                qt_row_layout.addWidget(element.QT_Dial)
            # -------------------------  Stretch element  ------------------------- #
            elif element_type == ELEM_TYPE_STRETCH:
                qt_row_layout.addStretch(1)
            # -------------------------  TABLE element  ------------------------- #
            elif element_type == ELEM_TYPE_TABLE:
                element.QT_TableWidget = Table.QTTableWidget(toplevel_win)
                # element.QT_TableWidget = QTableWidget()
                style = create_style_from_font(font)
                if element.TextColor is not None:
                    style += 'color: %s;' % element.TextColor
                if element.BackgroundColor is not None:
                    style += 'background-color: %s;' % element.BackgroundColor
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_TableWidget.setStyleSheet(style)

                if element.ChangeSubmits:
                    element.QT_TableWidget.itemSelectionChanged.connect(element.QtCallbackCellActivated)
                element.QT_TableWidget.setRowCount(len(element.Values))
                element.QT_TableWidget.setColumnCount(len(element.Values[0]))
                for rownum, rows in enumerate(element.Values):
                    # element.QT_TableWidget.insertRow(rownum)
                    for colnum, columns in enumerate(rows):
                        element.QT_TableWidget.setItem(rownum, colnum, QTableWidgetItem(element.Values[rownum][colnum]))

                element.QT_TableWidget.installEventFilter(element.QT_TableWidget)

                element.QT_TableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
                if element.Tooltip:
                    element.QT_TableWidget.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_TableWidget.setVisible(False)
                qt_row_layout.addWidget(element.QT_TableWidget)
            # -------------------------  Tree element  ------------------------- #
            elif element_type == ELEM_TYPE_TREE:
                element.QT_QTreeWidget = QTreeWidget()
                if element_size != (None, None):
                    element.QT_QTreeWidget.setFixedWidth(element_size[0])
                    element.QT_QTreeWidget.setFixedHeight(element_size[1])
                height = element.NumRows

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
                    child = QTreeWidgetItem(widget)
                    if node.key != '':
                        child.setText(0, str(node.text))
                        # child.setData(0,0,node.values)
                        if node.icon is not None:
                            qicon = QIcon(node.icon)
                            child.setIcon(0, qicon)
                    for node in node.children:
                        add_treeview_data(node, child)

                add_treeview_data(element.TreeData.root_node, element.QT_QTreeWidget)

                style = ''
                style += 'margin: {}px {}px {}px {}px;'.format(*full_element_pad)
                style += 'border: {}px solid gray; '.format(border_depth)
                element.QT_QTreeWidget.setStyleSheet(style)

                if element.ShowExpanded:
                    element.QT_QTreeWidget.expandAll()
                    element.QT_QTreeWidget.show()
                if element.Tooltip:
                    element.QT_QTreeWidget.setToolTip(element.Tooltip)
                if not element.Visible:
                    element.QT_QTreeWidget.setVisible(False)
                qt_row_layout.addWidget(element.QT_QTreeWidget)
            # -------------------------  Separator element  ------------------------- #
            elif element_type == ELEM_TYPE_SEPARATOR:
                element.QT_Label = qlabel = QLabel('', toplevel_win.QTWindow)
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
    timer.timeout.connect(window.timer_timeout)
    timer.start(amount)
    return timer


def start_systray_read_timer(tray, amount):
    timer = QtCore.QTimer()
    timer.timeout.connect(tray.timer_timeout)
    timer.start(amount)
    return timer


def start_window_autoclose_timer(window, amount):
    timer = QtCore.QTimer()
    window.autoclose_timer = timer
    timer.timeout.connect(window.autoclose_timer_callback)
    timer.start(amount)
    return timer

def stop_timer(timer):
    timer.stop()

# ----====----====----====----====----==== STARTUP TK ====----====----====----====----====----#
def StartupTK(window):
    global _my_windows
    global using_pyqt5

    ow = _my_windows.NumOpenWindows

    if _my_windows.QTApplication is None:
        _my_windows.QTApplication = QApplication(sys.argv)

    window.QTApplication = _my_windows.QTApplication

    _my_windows.Increment()


    # window.QTWindow = QWidget()

    window.QT_QMainWindow = window.QT_QMainWindowClass(window.ReturnKeyboardEvents, window)
    window.QTWindow = window.QTMainWindow(window.ReturnKeyboardEvents, window)
    window.QT_QMainWindow.setCentralWidget(window.QTWindow)

    window.QT_QMainWindow.installEventFilter(window.QT_QMainWindow)

    window.QTApplication.setActiveWindow(window.QT_QMainWindow)

    flags = 0
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
        window.QT_QMainWindow.setWindowIcon(QtGui.QIcon(window.WindowIcon))

    # window.QTWindow.setAttribute(Qt.WA_TranslucentBackground)
    # shadow = QtWidgets.QGraphicsDropShadowEffect()
    # shadow.setBlurRadius(9.0)
    # shadow.setBlurRadius(50)
    # window.QTWindow.setGraphicsEffect(shadow)

    # if window.KeepOnTop:
    #     window.QTWindow.setWindowFlags(Qt.WindowStaysOnTopHint)


    style = ''
    if window.BackgroundColor is not None and window.BackgroundColor != COLOR_SYSTEM_DEFAULT:
        style += 'background-color: %s;' % window.BackgroundColor
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
    if not window.Resizable:
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
    size[0] += 5
    window.QT_QMainWindow.resize(*size)

    if window._Size != (None, None):
        window.QT_QMainWindow.resize(window._Size[0], window._Size[1])

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
            _my_windows.Decrement()
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
        bar2.MaxValue = max_value
        bar2.CurrentValue = 0
        bar_text = Text(single_line_message, size=(width*10, height*25 + 70), auto_size_text=True)
        form.AddRow(bar_text)
        form.AddRow((bar2))
        form.AddRow((CloseButton('Cancel', button_color=button_color)))
    else:
        single_line_message, width, height = ConvertArgsToSingleString(*args)
        bar2.TextToDisplay = single_line_message
        bar2.MaxValue = max_value
        bar2.CurrentValue = 0
        bar_text = Text(single_line_message, size=(width*10, height*25 + 3), auto_size_text=True)
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
            bar.ParentForm.QT_QMainWindow.close()

            # bar.ParentForm.TKroot.destroy()
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
        bar.ParentForm.__del__()
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
    global _my_windows
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
        _my_windows.active_popups[self.window] = 'debug window'
        return

    def Print(self, *args, end=None, sep=None):
        sepchar = sep if sep is not None else ' '
        endchar = end if end is not None else '\n'

        if self.window is None:  # if window was destroyed already, just print
            print(*args, sep=sepchar, end=endchar)
            return
        _my_windows.active_popups[self.window] = 'debug window'
        event, values = self.window.Read(timeout=0)
        if event == 'Quit' or event is None:
            self.Close()
        print(*args, sep=sepchar, end=endchar)
        # TODO
        # Add extra check to see if the window was closed... if closed by X sometimes am not told
        # try:
        #     state = self.window.TKroot.state()
        # except:
        #     self.Close()

    def Close(self):
        self.window.Close()
        self.window.__del__()
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
                  size=(None, None), location=(None, None)):
    if not args: return
    width, height = size
    width = width if width else MESSAGE_BOX_LINE_WIDTH
    form = Window(args[0], auto_size_text=True, button_color=button_color, auto_close=auto_close,
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
    form.AddRow(MultilineOutput(complete_output, size=computed_size))
    pad = max_line_total - 15 if max_line_total > 15 else 1
    # show either an OK or Yes/No depending on paramater
    if yes_no:
        form.AddRow(Text('', size=(pad, 1), auto_size_text=False), Yes(), No())
        button, values = form.Read()
        form.Close()
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
        DEFAULT_ELEMENT_SIZE = convert_tkinter_size_to_Qt(element_size)

    if button_element_size != (None, None):
        DEFAULT_BUTTON_ELEMENT_SIZE = convert_tkinter_size_to_Qt(button_element_size)

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
    #
    # if sys.platform == 'darwin':
    #     print('*** Changing look and feel is not supported on Mac platform ***')
    #     return

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
    global _my_windows


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
        _my_windows.active_popups[window] = title
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
def PopupError(*args, title=None, button_color=DEFAULT_ERROR_BUTTON_COLOR, background_color=None, text_color=None, auto_close=False,
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
    Popup(*args, title=title, button_type=POPUP_BUTTONS_ERROR, background_color=background_color, text_color=text_color,
          non_blocking=non_blocking, icon=icon, line_width=line_width, button_color=button_color, auto_close=auto_close,
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

    global _my_windows

    if no_window:
        if _my_windows.QTApplication is None:
            _my_windows.QTApplication = QApplication(sys.argv)

        folder_name = QFileDialog.getExistingDirectory(dir=initial_folder)
        return folder_name

    layout = [[Text(message, auto_size_text=True, text_color=text_color, background_color=background_color)],
              [InputText(default_text=default_path, size=size), FolderBrowse(initial_folder=initial_folder)],
              [CloseButton('Ok', size=(60, 20), bind_return_key=True), CloseButton('Cancel', size=(60, 20))]]

    _title = title if title is not None else message
    window = Window(title=_title, icon=icon, auto_size_text=True, button_color=button_color,
                    background_color=background_color,
                    font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    (button, input_values) = window.Layout(layout).Read()

    if button != 'Ok':
        return None
    else:
        path = input_values[0]
        return path


# --------------------------- PopupGetFile ---------------------------

def PopupGetFile(message, title=None, default_path='', default_extension='', save_as=False, file_types=(("ALL Files", "*.*"),),
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
        if _my_windows.QTApplication is None:
            _my_windows.QTApplication = QApplication(sys.argv)

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
              [InputText(default_text=default_path, size=(30,1)), browse_button],
              [CButton('Ok', size=(60, 20), bind_return_key=True), CButton('Cancel', size=(60, 20))]]

    _title = title if title is not None else message

    window = Window(title=_title, icon=icon, auto_size_text=True, button_color=button_color, font=font,
                    background_color=background_color,
                    no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)

    (button, input_values) = window.Layout(layout).Read()
    # window.Close()
    if button != 'Ok':
        return None
    else:
        path = input_values[0]
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
              [InputText(default_text=default_text, size=size, password_char=password_char)],
              [CloseButton('Ok', size=(60, 20), bind_return_key=True), CloseButton('Cancel', size=(60, 20))]]

    _title = title if title is not None else message

    window = Window(title=_title, icon=icon, auto_size_text=True, button_color=button_color, no_titlebar=no_titlebar,
                    background_color=background_color, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    (button, input_values) = window.Layout(layout).Read()

    if button != 'Ok':
        return None
    else:
        return input_values[0]


def main():
    layout = [[Text('You are running the PySimpleGUI.py file itself')],
              [Text('You should be importing it rather than running it')],
              [Text('Here is your sample input window....')],
              [Text('Source File', size=(150, 25), justification='right'), InputText('Source', focus=True), FileBrowse()],
              [Text('Destination Folder', size=(150, 25), justification='right'), InputText('Dest'), FolderBrowse()],
              [Ok(bind_return_key=True), Cancel()]]

    window = Window('Demo window..',
                    auto_size_buttons=False,
                    default_element_size=(280,22),
                    auto_size_text=False,
                    default_button_element_size=(80,22)
                    ).Layout(layout)
    event, values = window.Read()
    print(event, values)
    window.Close()
    window.Close()


if __name__ == '__main__':
    main()
    exit(69)
