#!/usr/bin/python3
#!/usr/bin/python3
import sys

import wx
import wx.adv
import wx.lib.inspection
import types
import datetime
import textwrap
import pickle
import calendar
import base64
import os

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
    print(g_time_delta)


"""
    21-Dec-2018
    Welcome to the "core" PySimpleGUIWx port!
    
    This marks the 3rd port of the PySimpleGUI GUI SDK.  Each port gets a little better than
    the previous.  

    It will take a while for this Wx port to be completed, but should be running with a fully selection
    of widgets fairly quickly.  The Qt port required 1 week to get to "Alpha" condition

    Enjoy!
"""

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
DEFAULT_PIXEL_TO_CHARS_CUTOFF = 15             # number of chars that triggers using pixels instead of chars

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
DEFAULT_PROGRESS_BAR_SIZE = (25, 20)  # Size of Progress Bar (characters for length, pixels for width)
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
ELEM_TYPE_INPUT_CHECKBOX = 'checkbox'
ELEM_TYPE_INPUT_SPIN = 'spind'
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


# ------------------------------------------------------------------------- #
#                       ToolTip used by the Elements                        #
# ------------------------------------------------------------------------- #

class ToolTip:
    """ Create a tooltip for a given widget

    (inspired by https://stackoverflow.com/a/36221216)
    """

    def __init__(self, widget, text, timeout=DEFAULT_TOOLTIP_TIME):
        self.widget = widget
        self.text = text
        self.timeout = timeout
        # self.wraplength = wraplength if wraplength else widget.winfo_screenwidth() // 2
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.timeout, self.showtip)

    def unschedule(self):
        if self.id:
            self.widget.after_cancel(self.id)
        self.id = None

    def showtip(self):
        if self.tipwindow:
            return
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + self.widget.winfo_height() - 20
        self.tipwindow = tk.Toplevel(self.widget)
        self.tipwindow.wm_overrideredirect(True)
        self.tipwindow.wm_geometry("+%d+%d" % (x, y))
        label = ttk.Label(self.tipwindow, text=self.text, justify=tk.LEFT,
                          background="#ffffe0", relief=tk.SOLID, borderwidth=1)
        label.pack()

    def hidetip(self):
        if self.tipwindow:
            self.tipwindow.destroy()
        self.tipwindow = None


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
        add_brace = False
        if len(style) != 0 and style[-1] == '}':
            style = style[:-1]
            add_brace = True
        if font is not None:
            style += create_style_from_font(font)
        if text_color is not None:
            style += ' color: %s;' % text_color
        if background_color is not None:
            style += 'background-color: %s;' % background_color
        if add_brace:
            style += '}'
        widget.setStyleSheet(style)
        set_widget_visiblity(widget, visible)

    def __del__(self):
        pass

# ---------------------------------------------------------------------- #
#                           Input Class                                  #
# ---------------------------------------------------------------------- #
class InputText(Element):
    def __init__(self, default_text='', size=(None, None), disabled=False, password_char='',
                 justification=None, background_color=None, text_color=None, font=None, tooltip=None,
                 change_submits=False,
                 do_not_clear=False, key=None, focus=False, pad=None):
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
        self.Justification = justification
        self.Disabled = disabled
        self.ChangeSubmits = change_submits
        super().__init__(ELEM_TYPE_INPUT_TEXT, size=size, background_color=bg, text_color=fg, key=key, pad=pad,
                         font=font, tooltip=tooltip)

    def Update(self, value=None, disabled=None):
        if disabled is True:
            self.TKEntry['state'] = 'disabled'
        elif disabled is False:
            self.TKEntry['state'] = 'normal'
        if value is not None:
            try:
                self.TKStringVar.set(value)
            except:
                pass
            self.DefaultText = value

    def Get(self):
        return self.TKStringVar.get()

    def SetFocus(self):
        try:
            self.TKEntry.focus_set()
        except:
            pass

    def __del__(self):
        super().__del__()


# -------------------------  INPUT TEXT Element lazy functions  ------------------------- #
In = InputText
Input = InputText


# ---------------------------------------------------------------------- #
#                           Combo                                        #
# ---------------------------------------------------------------------- #
class InputCombo(Element):
    def __init__(self, values, default_value=None, size=(None, None), auto_size_text=None, background_color=None,
                 text_color=None, change_submits=False, disabled=False, key=None, pad=None, tooltip=None,
                 readonly=False, font=None):
        '''
        Input Combo Box Element (also called Dropdown box)
        :param values:
        :param size: Size of field in characters
        :param auto_size_text: True if should shrink field to fit the default text
        :param background_color: Color for Element. Text or RGB Hex
        '''
        self.Values = values
        self.DefaultValue = default_value
        self.ChangeSubmits = change_submits
        self.TKCombo = None
        # self.InitializeAsDisabled = disabled
        self.Disabled = disabled
        self.Readonly = readonly
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_COMBO, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT)

    def Update(self, value=None, values=None, set_to_index=None, disabled=None, readonly=None, font=None):
        if values is not None:
            try:
                self.TKCombo['values'] = values
                self.TKCombo.current(0)
            except:
                pass
            self.Values = values
        if value is not None:
            for index, v in enumerate(self.Values):
                if v == value:
                    try:
                        self.TKCombo.current(index)
                    except:
                        pass
                    self.DefaultValue = value
                    break
        if set_to_index is not None:
            try:
                self.TKCombo.current(set_to_index)
                self.DefaultValue = self.Values[set_to_index]
            except:
                pass
        if disabled == True:
            self.TKCombo['state'] = 'disable'
        elif disabled == False:
            self.TKCombo['state'] = 'enable'
            if readonly is not None:
                self.Readonly = readonly
            if self.Readonly:
                self.TKCombo['state'] = 'readonly'
        if font is not None:
            self.TKText.configure(font=font)

    def __del__(self):
        try:
            self.TKCombo.__del__()
        except:
            pass
        super().__del__()


# -------------------------  INPUT COMBO Element lazy functions  ------------------------- #
Combo = InputCombo
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
    def __init__(self, values, default_values=None, select_mode=None, change_submits=False, bind_return_key=False,
                 size=(None, None), disabled=False, auto_size_text=None, font=None, background_color=None,
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
                         background_color=bg, text_color=fg, key=key, pad=pad, tooltip=tooltip)

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

    def __del__(self):
        try:
            self.TKListBox.__del__()
        except:
            pass
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Radio                                        #
# ---------------------------------------------------------------------- #
class Radio(Element):
    def __init__(self, text, group_id, default=False, disabled=False, size=(None, None), auto_size_text=None,
                 background_color=None, text_color=None, font=None, key=None, pad=None, tooltip=None,
                 change_submits=False):
        '''
        Radio Button
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

        super().__init__(ELEM_TYPE_INPUT_RADIO, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip)

    def Update(self, value=None, disabled=None):
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

    def __del__(self):
        try:
            self.TKRadio.__del__()
        except:
            pass
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Checkbox                                     #
# ---------------------------------------------------------------------- #
class Checkbox(Element):
    def __init__(self, text, default=False, size=(None, None), auto_size_text=None, font=None, background_color=None,
                 text_color=None, change_submits=False, disabled=False, key=None, pad=None, tooltip=None):
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
        self.ChangeSubmits = change_submits

        super().__init__(ELEM_TYPE_INPUT_CHECKBOX, size=size, auto_size_text=auto_size_text, font=font,
                         background_color=background_color, text_color=self.TextColor, key=key, pad=pad,
                         tooltip=tooltip)

    def Get(self):
        return self.TKIntVar.get()

    def Update(self, value=None, disabled=None):
        if value is not None:
            try:
                self.TKIntVar.set(value)
                self.InitialState = value
            except:
                pass
        if disabled == True:
            self.TKCheckbutton.configure(state='disabled')
        elif disabled == False:
            self.TKCheckbutton.configure(state='normal')

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
    def __init__(self, values, initial_value=None, disabled=False, change_submits=False, size=(None, None),
                 auto_size_text=None, font=None, background_color=None, text_color=None, key=None, pad=None,
                 tooltip=None):
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
        self.ChangeSubmits = change_submits
        self.TKSpinBox = None
        self.Disabled = disabled
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_SPIN, size, auto_size_text, font=font, background_color=bg, text_color=fg,
                         key=key, pad=pad, tooltip=tooltip)
        return

    def Update(self, value=None, values=None, disabled=None):
        if values != None:
            old_value = self.TKStringVar.get()
            self.Values = values
            self.TKSpinBox.configure(values=values)
            self.TKStringVar.set(old_value)
        if value is not None:
            try:
                self.TKStringVar.set(value)
            except:
                pass
        self.DefaultValue = value
        if disabled == True:
            self.TKSpinBox.configure(state='disabled')
        elif disabled == False:
            self.TKSpinBox.configure(state='normal')

    def SpinChangedHandler(self, event):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def __del__(self):
        try:
            self.TKSpinBox.__del__()
        except:
            pass
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Multiline                                    #
# ---------------------------------------------------------------------- #
class Multiline(Element):
    def __init__(self, default_text='', enter_submits=False, disabled=False, autoscroll=False, size=(None, None),
                 auto_size_text=None, background_color=None, text_color=None, change_submits=False, do_not_clear=False,
                 key=None, focus=False,
                 font=None, pad=None, tooltip=None):
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
        self.ChangeSubmits = change_submits

        super().__init__(ELEM_TYPE_INPUT_MULTILINE, size=size, auto_size_text=auto_size_text, background_color=bg,
                         text_color=fg, key=key, pad=pad, tooltip=tooltip, font=font or DEFAULT_FONT)
        return

    def Update(self, value=None, disabled=None, append=False, font=None, text_color=None, background_color=None):
        if value is not None:
            try:
                if not append:
                    self.TKText.delete('1.0', tk.END)
                self.TKText.insert(tk.END, value)
            except:
                pass
            self.DefaultText = value
        if self.Autoscroll:
            self.TKText.see(tk.END)
        if disabled == True:
            self.TKText.configure(state='disabled')
        elif disabled == False:
            self.TKText.configure(state='normal')
        if background_color is not None:
            self.TKText.configure(background=background_color)
        if text_color is not None:
            self.TKText.configure(fg=text_color)
        if font is not None:
            self.TKText.configure(font=font)

    def Get(self):
        return self.TKText.get(1.0, tk.END)

    def SetFocus(self):
        try:
            self.TKText.focus_set()
        except:
            pass

    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                                       Text                             #
# ---------------------------------------------------------------------- #
class Text(Element):
    def __init__(self, text, size=(None, None), auto_size_text=None, click_submits=None, relief=None, font=None,
                 text_color=None, background_color=None, justification=None, pad=None, key=None, tooltip=None):
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
        self.Justification = justification
        self.Relief = relief
        self.ClickSubmits = click_submits
        if background_color is None:
            bg = DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR
        else:
            bg = background_color
        pixelsize = size
        if size[1] is not None and size[1] < 10:
            pixelsize = size[0]*10, size[1]*20
        super().__init__(ELEM_TYPE_TEXT, pixelsize, auto_size_text, background_color=bg, font=font if font else DEFAULT_FONT,
                         text_color=self.TextColor, pad=pad, key=key, tooltip=tooltip)
        return

    def Update(self, value=None, background_color=None, text_color=None, font=None):
        if value is not None:
            self.DisplayText = value
            stringvar = self.TKStringVar
            stringvar.set(value)
        if background_color is not None:
            self.TKText.configure(background=background_color)
        if text_color is not None:
            self.TKText.configure(fg=text_color)
        if font is not None:
            self.TKText.configure(font=font)

    def __del__(self):
        super().__del__()


# -------------------------  Text Element lazy functions  ------------------------- #
Txt = Text
T = Text


# ---------------------------------------------------------------------- #
#                       TKProgressBar                                    #
#  Emulate the TK ProgressBar using canvas and rectangles
# ---------------------------------------------------------------------- #

class TKProgressBar():
    def __init__(self, root, max, length=400, width=DEFAULT_PROGRESS_BAR_SIZE[1], style=DEFAULT_PROGRESS_BAR_STYLE,
                 relief=DEFAULT_PROGRESS_BAR_RELIEF, border_width=DEFAULT_PROGRESS_BAR_BORDER_WIDTH,
                 orientation='horizontal', BarColor=(None, None), key=None):
        self.Length = length
        self.Width = width
        self.Max = max
        self.Orientation = orientation
        self.Count = None
        self.PriorCount = 0

        if orientation[0].lower() == 'h':
            s = ttk.Style()
            s.theme_use(style)
            if BarColor != COLOR_SYSTEM_DEFAULT:
                s.configure(str(key) + "my.Horizontal.TProgressbar", background=BarColor[0], troughcolor=BarColor[1],
                            troughrelief=relief, borderwidth=border_width, thickness=width)
            else:
                s.configure(str(key) + "my.Horizontal.TProgressbar", troughrelief=relief, borderwidth=border_width,
                            thickness=width)

            self.TKProgressBarForReal = ttk.Progressbar(root, maximum=self.Max,
                                                        style=str(key) + 'my.Horizontal.TProgressbar', length=length,
                                                        orient=tk.HORIZONTAL, mode='determinate')
        else:
            s = ttk.Style()
            s.theme_use(style)
            if BarColor != COLOR_SYSTEM_DEFAULT:
                s.configure(str(length) + str(width) + "my.Vertical.TProgressbar", background=BarColor[0],
                            troughcolor=BarColor[1], troughrelief=relief, borderwidth=border_width, thickness=width)
            else:
                s.configure(str(length) + str(width) + "my.Vertical.TProgressbar", troughrelief=relief,
                            borderwidth=border_width, thickness=width)
            self.TKProgressBarForReal = ttk.Progressbar(root, maximum=self.Max,
                                                        style=str(length) + str(width) + 'my.Vertical.TProgressbar',
                                                        length=length, orient=tk.VERTICAL, mode='determinate')

    def Update(self, count=None, max=None):
        if max is not None:
            self.Max = max
            try:
                self.TKProgressBarForReal.config(maximum=max)
            except:
                return False
        if count is not None and count > self.Max: return False
        if count is not None:
            try:
                self.TKProgressBarForReal['value'] = count
            except:
                return False
        return True

    def __del__(self):
        try:
            self.TKProgressBarForReal.__del__()
        except:
            pass


# ---------------------------------------------------------------------- #
#                           TKOutput                                     #
#   New Type of TK Widget that's a Text Widget in disguise               #
#       Note that it's inherited from the TKFrame class so that the      #
#       Scroll bar will span the length of the frame                     #
# ---------------------------------------------------------------------- #
class TKOutput():
    def __init__(self, parent, width, height, bd, background_color=None, text_color=None, font=None, pad=None):
        self.previous_stdout = sys.stdout
        self.previous_stderr = sys.stderr

        sys.stdout = self
        sys.stderr = self

    def write(self, txt):
        pass

    def Close(self):
        sys.stdout = self.previous_stdout
        sys.stderr = self.previous_stderr

    def flush(self):
        sys.stdout = self.previous_stdout
        sys.stderr = self.previous_stderr

    def __del__(self):
        sys.stdout = self.previous_stdout
        sys.stderr = self.previous_stderr


# ---------------------------------------------------------------------- #
#                           Output                                       #
#  Routes stdout, stderr to a scrolled window                            #
# ---------------------------------------------------------------------- #
class Output(Element):
    def __init__(self, size=(None, None), background_color=None, text_color=None, pad=None, font=None, tooltip=None,
                 key=None):
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

        super().__init__(ELEM_TYPE_OUTPUT, size=size, background_color=bg, text_color=fg, pad=pad, font=font,
                         tooltip=tooltip, key=key)

    @property
    def TKOut(self):
        if self._TKOut is None:
            print('*** Did you forget to call Finalize()? Your code should look something like: ***')
            print('*** form = sg.Window("My Form").Layout(layout).Finalize() ***')
        return self._TKOut

    def Update(self, value=None):
        if value is not None:
            # try:
            self._TKOut.output.delete('1.0', tk.END)
            self._TKOut.output.insert(tk.END, value)
            # except:
            #     pass

    def __del__(self):
        try:
            self._TKOut.__del__()
        except:
            pass
        super().__del__()


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
        Button
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
            self.ParentForm.TKroot.quit()  # kick out of loop if read was called

    # -------  Button Callback  ------- #
    def ButtonCallBack(self):

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
            folder_name = tk.filedialog.askdirectory(initialdir=self.InitialFolder)  # show the 'get folder' dialog box
            if folder_name != '':
                try:
                    strvar.set(folder_name)
                    self.TKStringVar.set(folder_name)
                except:
                    pass
        elif self.BType == BUTTON_TYPE_BROWSE_FILE:
            if sys.platform == 'darwin':
                file_name = tk.filedialog.askopenfilename(
                    initialdir=self.InitialFolder)  # show the 'get file' dialog box
            else:
                file_name = tk.filedialog.askopenfilename(filetypes=filetypes,
                                                          initialdir=self.InitialFolder)  # show the 'get file' dialog box
            if file_name != '':
                strvar.set(file_name)
                self.TKStringVar.set(file_name)
        elif self.BType == BUTTON_TYPE_COLOR_CHOOSER:
            color = tk.colorchooser.askcolor()  # show the 'get file' dialog box
            color = color[1]  # save only the #RRGGBB portion
            strvar.set(color)
            self.TKStringVar.set(color)
        elif self.BType == BUTTON_TYPE_BROWSE_FILES:
            if sys.platform == 'darwin':
                file_name = tk.filedialog.askopenfilenames(initialdir=self.InitialFolder)
            else:
                file_name = tk.filedialog.askopenfilenames(filetypes=filetypes, initialdir=self.InitialFolder)
            if file_name != '':
                file_name = ';'.join(file_name)
                strvar.set(file_name)
                self.TKStringVar.set(file_name)
        elif self.BType == BUTTON_TYPE_SAVEAS_FILE:
            if sys.platform == 'darwin':
                file_name = tk.filedialog.asksaveasfilename(
                    initialdir=self.InitialFolder)  # show the 'get file' dialog box
            else:
                file_name = tk.filedialog.asksaveasfilename(filetypes=filetypes,
                                                            initialdir=self.InitialFolder)  # show the 'get file' dialog box
            if file_name != '':
                strvar.set(file_name)
                self.TKStringVar.set(file_name)
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
                self.ParentForm.TKroot.quit()
            if self.ParentForm.NonBlocking:
                self.ParentForm.TKroot.destroy()
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
                self.ParentForm.TKroot.quit()  # kick the users out of the mainloop
        elif self.BType == BUTTON_TYPE_CLOSES_WIN_ONLY:  # special kind of button that does not exit main loop
            self.ParentForm._Close()
            if self.ParentForm.NonBlocking:
                self.ParentForm.TKroot.destroy()
                _my_windows.Decrement()
        elif self.BType == BUTTON_TYPE_CALENDAR_CHOOSER:  # this is a return type button so GET RESULTS and destroy window
            should_submit_window = False
            root = tk.Toplevel()
            root.title('Calendar Chooser')
            self.TKCal = TKCalendar(master=root, firstweekday=calendar.SUNDAY, target_element=target_element,
                                    close_when_chosen=self.CalendarCloseWhenChosen, default_date=self.DefaultDate_M_D_Y)
            self.TKCal.pack(expand=1, fill='both')
            root.update()

        if should_submit_window:
            self.ParentForm.LastButtonClicked = target_element.Key
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

        return

    def Update(self, text=None, button_color=(None, None), disabled=None, image_data=None, image_filename=None):
        try:
            if text is not None:
                self.TKButton.configure(text=text)
                self.ButtonText = text
            if button_color != (None, None):
                self.TKButton.config(foreground=button_color[0], background=button_color[1])
        except:
            return
        if disabled == True:
            self.TKButton['state'] = 'disabled'
        elif disabled == False:
            self.TKButton['state'] = 'normal'
        if image_data is not None:
            image = tk.PhotoImage(data=image_data)
            width, height = image.width(), image.height()
            self.TKButton.config(image=image, width=width, height=height)
            self.TKButton.image = image
        if image_filename is not None:
            self.TKButton.config(highlightthickness=0)
            photo = tk.PhotoImage(file=image_filename)
            width, height = photo.width(), photo.height()
            self.TKButton.config(image=photo, width=width, height=height)
            self.TKButton.image = photo

    def GetText(self):
        return self.ButtonText

    def __del__(self):
        try:
            self.TKButton.__del__()
        except:
            pass
        super().__del__()


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
        if self.ParentForm.TKrootDestroyed:
            return False
        self.TKProgressBar.Update(current_count, max=max)
        try:
            self.ParentForm.TKroot.update()
        except:
            _my_windows.Decrement()
            return False
        return True

    def __del__(self):
        try:
            self.TKProgressBar.__del__()
        except:
            pass
        super().__del__()


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
                         tooltip=tooltip)
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
    def __init__(self, canvas_size, graph_bottom_left, graph_top_right, background_color=None, pad=None,
                 change_submits=False, drag_submits=False, key=None,
                 tooltip=None):
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
        super().__init__(ELEM_TYPE_GRAPH, background_color=background_color, size=canvas_size, pad=pad, key=key,
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

    def __del__(self):
        super().__del__()


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

    def __del__(self):
        for row in self.Rows:
            for element in row:
                element.__del__()
        super().__del__()


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

    def __del__(self):
        super().__del__()


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
        self.TabID = None
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR

        self.Layout(layout)

        super().__init__(ELEM_TYPE_TAB, background_color=background_color, text_color=title_color, font=font, pad=pad,
                         key=key, tooltip=tooltip)
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

        self.Layout(layout)

        super().__init__(ELEM_TYPE_TAB_GROUP, background_color=background_color, text_color=title_color, font=font,
                         pad=pad, key=key, tooltip=tooltip)
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
                 border_width=None, relief=None, change_submits=False, disabled=False, size=(None, None), font=None,
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
                         text_color=text_color, key=key, pad=pad, tooltip=tooltip)
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

    def SliderChangedHandler(self, event):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        if self.Key is not None:
            self.ParentForm.LastButtonClicked = self.Key
        else:
            self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def __del__(self):
        super().__del__()


#
# ---------------------------------------------------------------------- #
#                           Column                                       #
# ---------------------------------------------------------------------- #
class Column(Element):
    def __init__(self, layout, background_color=None, size=(None, None), pad=None, scrollable=False,
                 vertical_scroll_only=False, key=None):
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
        # self.ImageFilename = image_filename
        # self.ImageData = image_data
        # self.ImageSize = image_size
        # self.ImageSubsample = image_subsample
        bg = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR

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

    def __del__(self):
        for row in self.Rows:
            for element in row:
                element.__del__()
        try:
            del (self.TKFrame)
        except:
            pass
        super().__del__()


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

    def MenuItemChosenCallback(self, item_chosen):
        # print('IN MENU ITEM CALLBACK', item_chosen)
        self.ParentForm.LastButtonClicked = item_chosen
        self.ParentForm.FormRemainedOpen = True
        if self.ParentForm.CurrentlyRunningMainloop:
            self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def __del__(self):
        super().__del__()


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

    def treeview_selected(self, event):
        selections = self.TKTreeview.selection()
        self.SelectedRows = [int(x) - 1 for x in selections]
        if self.ChangeSubmits:
            MyForm = self.ParentForm
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = ''
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.TKroot.quit()

    def treeview_double_click(self, event):
        selections = self.TKTreeview.selection()
        self.SelectedRows = [int(x) - 1 for x in selections]
        if self.BindReturnKey:
            MyForm = self.ParentForm
            if self.Key is not None:
                self.ParentForm.LastButtonClicked = self.Key
            else:
                self.ParentForm.LastButtonClicked = ''
            self.ParentForm.FormRemainedOpen = True
            if self.ParentForm.CurrentlyRunningMainloop:
                self.ParentForm.TKroot.quit()

    def __del__(self):
        super().__del__()


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

        super().__init__(ELEM_TYPE_TREE, text_color=text_color, background_color=background_color, font=font, pad=pad,
                         key=key, tooltip=tooltip)
        return

    def treeview_selected(self, event):
        selections = self.TKTreeview.selection()
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

    def __del__(self):
        super().__del__()


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

    def __del__(self):
        super().__del__()

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

        self.App = wx.App(False)
        frame = wx.Frame(None, title='Tray icon frame')
        self.TaskBarIcon = SystemTray.CustomTaskBarIcon(frame, self.App, self.Menu, filename=self.Filename, tooltip=tooltip)

        # self.App.MainLoop()


    class CustomTaskBarIcon(wx.adv.TaskBarIcon):
        def __init__(self, frame, app, menu, filename=None, data_base64=None, tooltip=None):
            wx.adv.TaskBarIcon.__init__(self)
            self.frame = frame
            self.app = app
            self.menu_item_chosen = None
            self.menu = menu
            self.id_to_text = {}
            if filename:
                icon = wx.Icon(filename, wx.BITMAP_TYPE_ICO)
                if tooltip is not None:
                    self.SetIcon(icon, tooltip=tooltip)
                else:
                    self.SetIcon(icon)
            elif data_base64:
                ico1 = base64.b64decode(data_base64)
                fout = open("zzztemp_icon.ico", "wb")
                fout.write(ico1)
                fout.close()
                icon = wx.Icon('zzztemp_icon.ico', wx.BITMAP_TYPE_ICO)
                self.TrayIcon.SetIcon(icon, tooltip=tooltip)
                # os.remove("zzztemp_icon.ico")
            self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.OnTaskBarLeftClick)
            self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.OnTaskBarLeftDoubleClick)
            self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, self.OnTaskBarRightClick)
            self.Bind(wx.EVT_MENU, self.OnMenu)

        def OnTaskBarActivate(self, evt):
            pass

        def OnTaskBarClose(self, evt):
            self.frame.Close()

        def OnTaskBarLeftClick(self, evt):
            # print('Got a LEFT click!')
            self.menu_item_chosen = EVENT_SYSTEM_TRAY_ICON_ACTIVATED
            self.app.ExitMainLoop()


        def OnTaskBarLeftDoubleClick(self, evt):
            # print('Got a double click!')
            self.menu_item_chosen = EVENT_SYSTEM_TRAY_ICON_DOUBLE_CLICKED
            self.app.ExitMainLoop()

        def CreatePopupMenu(self):
            # print(f'Popup menu = {self.menu}')
            menu = wx.Menu()
            AddMenuItem(menu, self.menu[1], self)
            # print(f'Dictionary = {self.id_to_text}')
            # menu = wx.Menu()
            # menu.Append(wx.ID_ANY, 'Exit')
            # menu.Append(wx.ID_ANY, 'Item2')
            # submenu = wx.Menu()
            # submenu.Append(-1, 'Sub item')
            # menu.AppendSubMenu(submenu, 'sub')
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

    # callback function when message is clicked
    def messageClicked(self):
        self.MenuItemChosen = EVENT_SYSTEM_TRAY_MESSAGE_CLICKED
        self.App.exit()



    def start_systray_read_timer(tray, amount):
        timer = QtCore.QTimer()
        timer.timeout.connect(tray.timer_timeout)
        timer.start(amount)
        return timer

    def stop_timer(timer):
        timer.stop()

    def Read(self, timeout=None):
        '''
        Reads the context menu
        :param timeout: Optional.  Any value other than None indicates a non-blocking read
        :return:
        '''
        # if not self.Shown:
        #     self.Shown = True
        #     self.TrayIcon.show()
        if timeout == 0:
            self.App.processEvents()
            return self.MenuItemChosen
        elif timeout is not None:
            self.timer = wx.Timer(self.TaskBarIcon)
            self.TaskBarIcon.Bind(wx.EVT_TIMER, self.timer_timeout)
            self.timer.Start(milliseconds=timeout, oneShot=wx.TIMER_ONE_SHOT)
        self.RunningMainLoop = True
        self.App.MainLoop()
        self.RunningMainLoop = False
        if self.timer:
            self.timer.Stop()
        self.MenuItemChosen = self.TaskBarIcon.menu_item_chosen
        return self.MenuItemChosen

    def timer_timeout(self, event):
        # print('GOT TIMEOUT')
        self.timer.Stop()
        self.timer = None
        self.TaskBarIcon.menu_item_chosen = TIMEOUT_KEY
        self.App.ExitMainLoop()


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
        if messageicon is None:
            self.TaskBarIcon.ShowBalloon(title, message, msec=time)
        else:
            self.TaskBarIcon.ShowBalloon(title, message, msec=time, flags=messageicon)

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
            self.TaskBarIcon.menu = menu
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





# ------------------------------------------------------------------------- #
#                       Window CLASS                                      #
# ------------------------------------------------------------------------- #
class Window:

    NumOpenWindows = 0
    user_defined_icon = None
    hidden_master_root = None
    QTApplication = None
    active_popups = {}


    def __init__(self, title, default_element_size=DEFAULT_ELEMENT_SIZE, default_button_element_size=(None, None),
                 auto_size_text=None, auto_size_buttons=None, location=(None, None), size=(None, None), element_padding=None, button_color=None, font=None,
                 progress_bar_color=(None, None), background_color=None, border_depth=None, auto_close=False,
                 auto_close_duration=DEFAULT_AUTOCLOSE_TIME, icon=DEFAULT_WINDOW_ICON, force_toplevel=False,
                 alpha_channel=1, return_keyboard_events=False, use_default_focus=True, text_justification=None,
                 no_titlebar=False, grab_anywhere=False, keep_on_top=False, resizable=True, disable_close=False, disable_minimize=False, background_image=None):
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
        self.DefaultButtonElementSize = convert_tkinter_size_to_Wx(default_button_element_size) if default_button_element_size != (
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
        self.App = None
        self.MasterFrame =  None
        self.MasterPanel = None


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

    Element = FindElement       # shortcut function definition

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
            self.MasterFrame.Close()
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

    # class QTMainWindow(QWidget):
    #     def __init__(self,enable_key_events, window):
    #         self.KeyEventsEnabled = enable_key_events
    #         self.Window = window
    #         super().__init__(window.QT_QMainWindow)
    #
    #     def eventFilter(self, widget, event):
    #         # print(event.type())
    #         if event.type() == QEvent.MouseButtonPress and self.Window.GrabAnywhere:
    #             self.mouse_offset = event.pos()
    #         if event.type() == QEvent.MouseMove and self.Window.GrabAnywhere:
    #             x = event.globalX()
    #             y = event.globalY()
    #             x_w = self.mouse_offset.x()
    #             y_w = self.mouse_offset.y()
    #             self.move(x - x_w, y - y_w)
    #
    #         if event.type() == QEvent.KeyRelease and self.KeyEventsEnabled:
    #             # print("got key event")
    #             key = event.key()
    #             try:
    #                 self.Window.LastButtonClicked = chr(key).lower()
    #             except:
    #                 self.Window.LastButtonClicked = "special %s" % key
    #             self.Window.FormRemainedOpen = True
    #             if self.Window.CurrentlyRunningMainloop:
    #                 self.Window.QTApplication.exit()
    #         return QWidget.eventFilter(self, widget, event)
    #
    #
    # class QT_QMainWindowClass(QMainWindow):
    #     def __init__(self,enable_key_events, window):
    #         self.KeyEventsEnabled = enable_key_events
    #         self.Window = window
    #         super().__init__()
    #
    #     def eventFilter(self, widget, event):
    #         # print(event.type())
    #         if event.type() == QEvent.MouseButtonPress and self.Window.GrabAnywhere:
    #             self.mouse_offset = event.pos()
    #         if event.type() == QEvent.MouseMove and self.Window.GrabAnywhere:
    #             x = event.globalX()
    #             y = event.globalY()
    #             x_w = self.mouse_offset.x()
    #             y_w = self.mouse_offset.y()
    #             self.move(x - x_w, y - y_w)
    #
    #         if event.type() == QEvent.KeyRelease and self.KeyEventsEnabled:
    #             # print("got key event")
    #             key = event.key()
    #             try:
    #                 self.Window.LastButtonClicked = chr(key).lower()
    #             except:
    #                 self.Window.LastButtonClicked = "special %s" % key
    #             self.Window.FormRemainedOpen = True
    #             if self.Window.CurrentlyRunningMainloop:
    #                 self.Window.QTApplication.exit()
    #         return QWidget.eventFilter(self, widget, event)

    def OnClose(self, event):
        print(f'CLOSE EVENT! event = {event}')
        if self.DisableClose:
            return
        # print('GOT A CLOSE EVENT!', event, self.Window.Title)
        self.LastButtonClicked = None
        self.XFound = True
        if not self.CurrentlyRunningMainloop:  # quit if this is the current mainloop, otherwise don't quit!
            self.RootNeedsDestroying = True
        else:
            self.RootNeedsDestroying = True
            self.App.ExitMainLoop()  # kick the users out of the mainloop
        self.MasterFrame.Destroy()
        self.TKrootDestroyed = True
        self.RootNeedsDestroying = True

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
                    value = element.TKStringVar.get()
                    if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                        element.TKStringVar.set('')
                elif element.Type == ELEM_TYPE_INPUT_CHECKBOX:
                    value = element.TKIntVar.get()
                    value = (value != 0)
                elif element.Type == ELEM_TYPE_INPUT_RADIO:
                    RadVar = element.TKIntVar.get()
                    this_rowcol = EncodeRadioRowCol(row_num, col_num)
                    value = RadVar == this_rowcol
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
                    value = element.TKStringVar.get()
                elif element.Type == ELEM_TYPE_INPUT_OPTION_MENU:
                    value = element.TKStringVar.get()
                elif element.Type == ELEM_TYPE_INPUT_LISTBOX:
                    try:
                        items = element.TKListbox.curselection()
                        value = [element.Values[int(item)] for item in items]
                    except:
                        value = ''
                elif element.Type == ELEM_TYPE_INPUT_SPIN:
                    try:
                        value = element.TKStringVar.get()
                    except:
                        value = 0
                elif element.Type == ELEM_TYPE_INPUT_SLIDER:
                    try:
                        value = element.TKIntVar.get()
                    except:
                        value = 0
                elif element.Type == ELEM_TYPE_INPUT_MULTILINE:
                    try:
                        value = element.TKText.get(1.0, tk.END)
                        if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                            element.TKText.delete('1.0', tk.END)
                    except:
                        value = None
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
                                         command=lambda: Menu.MenuItemChosenCallback(element, sub_menu_info))
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


# ------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #
# =====================================   TK CODE STARTS HERE ====================================================== #
# ------------------------------------------------------------------------------------------------------------------ #
# ------------------------------------------------------------------------------------------------------------------ #

def PackFormIntoFrame(form, containing_frame, toplevel_form):
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
        tk_row_frame = 00000        # TODO Get horizontal ROW widget to put others into
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
                pass
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
                statictext = element.WxStaticText = wx.StaticText(form.MasterPanel, -1, element.DisplayText)
                # auto_size_text = element.AutoSizeText
                display_text = element.DisplayText  # text to display
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
                lrsizer = wx.BoxSizer(wx.HORIZONTAL)
                if full_element_pad[1] == full_element_pad[3]:   # if right = left
                    lrsizer.Add(element.WxStaticText, 0, wx.LEFT|wx.RIGHT,  border=full_element_pad[1])
                else:
                    sizer = wx.BoxSizer(wx.HORIZONTAL)
                    sizer.Add(element.WxStaticText,0,wx.LEFT, border=full_element_pad[3])
                    lrsizer.Add(sizer, 0, wx.RIGHT, border=full_element_pad[1])

                top_bottom_sizer  = wx.BoxSizer(wx.HORIZONTAL)
                if full_element_pad[0] == full_element_pad[2]:   # if top = bottom
                    top_bottom_sizer.Add(lrsizer, 0, wx.TOP|wx.BOTTOM,  border=full_element_pad[0])
                else:
                    sizer = wx.BoxSizer(wx.HORIZONTAL)
                    sizer.Add(lrsizer,0,wx.TOP, border=full_element_pad[0])
                    top_bottom_sizer.Add(sizer, 0, wx.BOTTOM, border=full_element_pad[2])

                hsizer.Add(top_bottom_sizer, 0)

                # print(element_size,element.Size, width, height)
                if not auto_size_text:
                    statictext.SetMinSize((width,height))
                # ---===--- LABEL widget create and place --- #
                # stringvar = tk.StringVar()
                # element.TKStringVar = stringvar
                # stringvar.set(display_text)
                # if auto_size_text:
                #     width = 0
                # if element.Justification is not None:
                #     justification = element.Justification
                # elif toplevel_form.TextJustification is not None:
                #     justification = toplevel_form.TextJustification
                # else:
                #     justification = DEFAULT_TEXT_JUSTIFICATION
                # justify = tk.LEFT if justification == 'left' else tk.CENTER if justification == 'center' else tk.RIGHT
                # anchor = tk.NW if justification == 'left' else tk.N if justification == 'center' else tk.NE
                # tktext_label = tk.Label(tk_row_frame, textvariable=stringvar, width=width, height=height,
                #                         justify=justify, bd=border_depth, font=font)
                # Set wrap-length for text (in PIXELS) == PAIN IN THE ASS
                # wraplen = tktext_label.winfo_reqwidth() + 40  # width of widget in Pixels
                # if not auto_size_text and height == 1:
                #     wraplen = 0
                # print("wraplen, width, height", wraplen, width, height)
                # tktext_label.configure(anchor=anchor, wraplen=wraplen)  # set wrap to width of widget
                # if element.Relief is not None:
                #     tktext_label.configure(relief=element.Relief)
                # if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                #     tktext_label.configure(background=element.BackgroundColor)
                # if element.TextColor != COLOR_SYSTEM_DEFAULT and element.TextColor is not None:
                #     tktext_label.configure(fg=element.TextColor)
                # tktext_label.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1], expand=True)
                # element.TKText = tktext_label
                # if element.ClickSubmits:
                #     tktext_label.bind('<Button-1>', element.TextClickedHandler)
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element.TKText, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
            # -------------------------  BUTTON element  ------------------------- #
            elif element_type == ELEM_TYPE_BUTTON:
                element.WxButton = button = wx.Button(form.MasterPanel, style=wx.BORDER_NONE)
                button.SetLabelText(element.ButtonText)

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
                    element.WxButton.SetMinSize(convert_tkinter_size_to_Wx((width,height)))
                if element.ButtonColor != (None, None) and element.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = element.ButtonColor
                elif toplevel_form.ButtonColor != (None, None) and toplevel_form.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = toplevel_form.ButtonColor
                else:
                    bc = DEFAULT_BUTTON_COLOR

                button.SetBackgroundColour(bc[1])
                button.SetForegroundColour(bc[0])

                lrsizer = wx.BoxSizer(wx.HORIZONTAL)
                if full_element_pad[1] == full_element_pad[3]:   # if right = left
                    lrsizer.Add(button, 0, wx.LEFT|wx.RIGHT,  border=full_element_pad[1])
                else:
                    sizer = wx.BoxSizer(wx.HORIZONTAL)
                    sizer.Add(button,0,wx.LEFT, border=full_element_pad[3])
                    lrsizer.Add(sizer, 0, wx.RIGHT, border=full_element_pad[1])

                top_bottom_sizer  = wx.BoxSizer(wx.HORIZONTAL)
                if full_element_pad[0] == full_element_pad[2]:   # if top = bottom
                    top_bottom_sizer.Add(lrsizer, 0, wx.TOP|wx.BOTTOM,  border=full_element_pad[0])
                else:
                    sizer = wx.BoxSizer(wx.HORIZONTAL)
                    sizer.Add(lrsizer,0,wx.TOP, border=full_element_pad[0])
                    top_bottom_sizer.Add(sizer, 0, wx.BOTTOM, border=full_element_pad[2])

                hsizer.Add(top_bottom_sizer, 0)


                # border_depth = element.BorderWidth
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

            # # -------------------------  INPUT (Single Line) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_TEXT:
                element.WxTextControl = text_ctrl = wx.TextCtrl(form.MasterPanel)
                text_ctrl.SetMinSize(element_size)

                lrsizer = wx.BoxSizer(wx.HORIZONTAL)
                if full_element_pad[1] == full_element_pad[3]:   # if right = left
                    lrsizer.Add(element.WxTextControl, 0, wx.LEFT|wx.RIGHT,  border=full_element_pad[1])
                else:
                    sizer = wx.BoxSizer(wx.HORIZONTAL)
                    sizer.Add(element.WxTextControl,0,wx.LEFT, border=full_element_pad[3])
                    lrsizer.Add(sizer, 0, wx.RIGHT, border=full_element_pad[1])

                top_bottom_sizer  = wx.BoxSizer(wx.HORIZONTAL)
                if full_element_pad[0] == full_element_pad[2]:   # if top = bottom
                    top_bottom_sizer.Add(lrsizer, 0, wx.TOP|wx.BOTTOM,  border=full_element_pad[0])
                else:
                    sizer = wx.BoxSizer(wx.HORIZONTAL)
                    sizer.Add(lrsizer,0,wx.TOP, border=full_element_pad[0])
                    top_bottom_sizer.Add(sizer, 0, wx.BOTTOM, border=full_element_pad[2])

                hsizer.Add(top_bottom_sizer, 0)



                # default_text = element.DefaultText
                # element.TKStringVar = tk.StringVar()
                # element.TKStringVar.set(default_text)
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
            # -------------------------  COMBO BOX (Drop Down) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_COMBO:
                pass

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
            # -------------------------  OPTION MENU (Like ComboBox but different) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_OPTION_MENU:
                pass
            #     max_line_len = max([len(str(l)) for l in element.Values])
            #     if auto_size_text is False:
            #         width = element_size[0]
            #     else:
            #         width = max_line_len
            #     element.TKStringVar = tk.StringVar()
            #     default = element.DefaultValue if element.DefaultValue else element.Values[0]
            #     element.TKStringVar.set(default)
            #     element.TKOptionMenu = tk.OptionMenu(tk_row_frame, element.TKStringVar, *element.Values)
            #     element.TKOptionMenu.config(highlightthickness=0, font=font, width=width)
            #     element.TKOptionMenu.config(borderwidth=border_depth)
            #     if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
            #         element.TKOptionMenu.configure(background=element.BackgroundColor)
            #     if element.TextColor != COLOR_SYSTEM_DEFAULT and element.TextColor is not None:
            #         element.TKOptionMenu.configure(fg=element.TextColor)
            #     element.TKOptionMenu.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
            #     if element.Disabled == True:
            #         element.TKOptionMenu['state'] = 'disabled'
            #     if element.Tooltip is not None:
            #         element.TooltipObject = ToolTip(element.TKOptionMenu, text=element.Tooltip,
            #                                         timeout=DEFAULT_TOOLTIP_TIME)
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
            # -------------------------  INPUT MULTI LINE element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_MULTILINE:
                pass
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
                pass
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
                # -------------------------  INPUT SPIN Box element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SPIN:
                pass
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
                pass
                # width, height = element_size
                # element._TKOut = TKOutput(tk_row_frame, width=width, height=height, bd=border_depth,
                #                           background_color=element.BackgroundColor, text_color=text_color, font=font,
                #                           pad=element.Pad)
                # element._TKOut.pack(side=tk.LEFT, expand=True, fill='both')
                # if element.Tooltip is not None:
                #     element.TooltipObject = ToolTip(element._TKOut, text=element.Tooltip, timeout=DEFAULT_TOOLTIP_TIME)
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
                pass
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
def StartupTK(window):

    ow = Window.NumOpenWindows
    app = wx.App()
    frame = wx.Frame(None, title=window.Title)
    panel = wx.Panel(frame)

    window.App = app
    window.MasterFrame =  frame
    window.MasterPanel = panel
    window.MasterFrame.panel = panel

    frame.Bind(wx.EVT_CLOSE, window.OnClose)

    frame.SetIcon(wx.Icon(window.WindowIcon))

    if window.BackgroundColor is not None and window.BackgroundColor != COLOR_SYSTEM_DEFAULT:
        panel.SetBackgroundColour(window.BackgroundColor)
    Window.IncrementOpenCount()

    # Make moveable window
    if (window.GrabAnywhere is not False and not (window.NonBlocking and window.GrabAnywhere is not True)):
            pass #TODO make moveable


    # if not window.Resizable:
    #     root.resizable(False, False)

    # if window.KeepOnTop:
    #     root.wm_attributes("-topmost", 1)


    InitializeResults(window)
    # if window.NoTitleBar:
    #     window.TKroot.wm_overrideredirect(True)
    vsizer = wx.BoxSizer(wx.VERTICAL)
    PackFormIntoFrame(window, vsizer, window)

    outersizer = wx.BoxSizer(wx.VERTICAL)
    outersizer.Fit(window.MasterFrame)
    outersizer.Add(vsizer, 1, wx.TOP|wx.BOTTOM|wx.EXPAND, border=DEFAULT_MARGINS[1])

    outer2 = wx.BoxSizer(wx.VERTICAL)
    outer2.Fit(window.MasterFrame)
    outer2.Add(outersizer, 1, wx.LEFT|wx.RIGHT|wx.EXPAND, border=DEFAULT_MARGINS[0])

    window.MasterPanel.SetSizer(outer2)
    # TODO - If there's a manually set Size and Location, set them here


    outer2.Fit(window.MasterFrame)
    window.MasterFrame.Show()
    # ....................................... DONE creating and laying out window ..........................#
    wx.lib.inspection.InspectionTool().Show()
    window.CurrentlyRunningMainloop = True
    window.App.MainLoop()
    window.CurrentlyRunningMainloop = False
    # window.SetIcon(window.WindowIcon)

    # root.attributes('-alpha', window.AlphaChannel)  # Make window visible again

    # if window.ReturnKeyboardEvents and not window.NonBlocking:
    #     root.bind("<KeyRelease>", window._KeyboardCallback)
    #     root.bind("<MouseWheel>", window._MouseWheelCallback)
    # elif window.ReturnKeyboardEvents:
    #     root.bind("<Key>", window._KeyboardCallback)
    #     root.bind("<MouseWheel>", window._MouseWheelCallback)

    # if window.AutoClose:
    #     duration = DEFAULT_AUTOCLOSE_TIME if window.AutoCloseDuration is None else window.AutoCloseDuration
    #     window.TKAfterID = root.after(duration * 1000, window._AutoCloseAlarmCallback)
    #
    # if window.Timeout != None:
    #     window.TKAfterID = root.after(window.Timeout, window._TimeoutAlarmCallback)
    # if window.NonBlocking:
    #     window.TKroot.protocol("WM_DESTROY_WINDOW", window.OnClosingCallback)
    #     window.TKroot.protocol("WM_DELETE_WINDOW", window.OnClosingCallback)
    # else:  # it's a blocking form
        # print('..... CALLING MainLoop')
        # window.CurrentlyRunningMainloop = True
        # window.TKroot.protocol("WM_DESTROY_WINDOW", window.OnClosingCallback)
        # window.TKroot.protocol("WM_DELETE_WINDOW", window.OnClosingCallback)
        # window.TKroot.mainloop()
        # window.CurrentlyRunningMainloop = False
        # window.TimerCancelled = True
        # print('..... BACK from MainLoop')
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
            col += [[T(arg)] for arg in args]
            col += [[T('', size=(30,10), key='_STATS_')],
                    [ProgressBar(max_value=self.max_value, orientation='h', key='_PROG_', size=self.size)],
                    [Cancel(button_color=self.button_color), Stretch()]]
            layout = [Column(col)]
        else:
            col = [[ProgressBar(max_value=self.max_value, orientation='v', key='_PROG_', size=self.size)]]
            col2 = []
            col2 += [[T(arg)] for arg in args]
            col2 += [[T('', size=(30,10), key='_STATS_')],
                     [Cancel(button_color=self.button_color), Stretch()]]
            layout = [Column(col), Column(col2)]
        self.window = Window(self.title, grab_anywhere=self.grab_anywhere, border_depth=self.border_width)
        self.window.Layout([layout]).Finalize()

        return self.window

    def UpdateMeter(self, current_value, max_value):
        self.current_value = current_value
        self.max_value = max_value
        self.window.Element('_PROG_').UpdateBar(self.current_value, self.max_value)
        self.window.Element('_STATS_').Update('\n'.join(self.ComputeProgressStats()))
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

    rc = meter.UpdateMeter(current_value, max_value)
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
                 grab_anywhere=False, keep_on_top=False, do_not_reroute_stdout=True):
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
        self.window = Window('Debug Window', no_titlebar=no_titlebar, auto_size_text=True, location=location,
                             font=font or ('Courier New', 10), grab_anywhere=grab_anywhere, keep_on_top=keep_on_top)
        self.output_element = Multiline(size=win_size, autoscroll=True, key='_MULTILINE_') if do_not_reroute_stdout else Output(size=win_size)

        if no_button:
            self.layout = [[self.output_element]]
        else:
            self.layout = [
                [self.output_element],
                [DummyButton('Quit'), Stretch()]
            ]
        self.window.AddRows(self.layout)
        self.window.Read(timeout=0)  # Show a non-blocking form, returns immediately
        return

    def Print(self, *args, end=None, sep=None):
        sepchar = sep if sep is not None else ' '
        endchar = end if end is not None else '\n'

        if self.window is None:  # if window was destroyed alread re-open it
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
        self.window.__del__()
        self.window = None


def PrintClose():
    EasyPrintClose()


def EasyPrint(*args, size=(None, None), end=None, sep=None, location=(None, None), font=None, no_titlebar=False,
              no_button=False, grab_anywhere=False, keep_on_top=False, do_not_reroute_stdout=False):


    if DebugWin.debug_window is None:
        DebugWin.debug_window = DebugWin(size=size, location=location, font=font, no_titlebar=no_titlebar,
                                    no_button=no_button, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, do_not_reroute_stdout=do_not_reroute_stdout)
    DebugWin.debug_window.Print(*args, end=end, sep=sep)


def PrintClose():
    EasyPrintClose()


def EasyPrint(*args, size=(None, None), end=None, sep=None, location=(None, None), font=None, no_titlebar=False,
              no_button=False, grab_anywhere=False, keep_on_top=False, do_not_reroute_stdout=False):


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
        PopupButton = CloseButton
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


    if no_window:
        if Window.NumOpenWindows:
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
              [InputText(default_text=default_path, size=size), FolderBrowse(initial_folder=initial_folder)],
              [CloseButton('Ok', size=(5, 1), bind_return_key=True), CloseButton('Cancel', size=(5, 1))]]

    window = Window(title=message, icon=icon, auto_size_text=True, button_color=button_color,
                    background_color=background_color,
                    font=font, no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    (button, input_values) = window.LayoutAndRead(layout)

    if button != 'Ok':
        return None
    else:
        path = input_values[0]
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


    if no_window:
        if Window.NumOpenWindows:
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
              [InputText(default_text=default_path, size=size), browse_button],
              [CloseButton('Ok', size=(6, 1), bind_return_key=True), CloseButton('Cancel', size=(6, 1))]]

    window = Window(title=message, icon=icon, auto_size_text=True, button_color=button_color, font=font,
                    background_color=background_color,
                    no_titlebar=no_titlebar, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top, location=location)

    (button, input_values) = window.Layout(layout).Read()
    if button != 'Ok':
        return None
    else:
        path = input_values[0]
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
              [InputText(default_text=default_text, size=size, password_char=password_char)],
              [CloseButton('Ok', size=(5, 1), bind_return_key=True), CloseButton('Cancel', size=(5, 1))]]

    window = Window(title=message, icon=icon, auto_size_text=True, button_color=button_color, no_titlebar=no_titlebar,
                    background_color=background_color, grab_anywhere=grab_anywhere, keep_on_top=keep_on_top,
                    location=location)

    (button, input_values) = window.Layout(layout).Read()

    if button != 'Ok':
        return None
    else:
        return input_values[0]


def main():
    layout = [[Text('TEXT1',), Text('TEXT2', )],
              [Text('You should be importing it rather than running it', justification='r', size=(50, 1))],
              [Text('Here is your sample input window....')],
              [Text('Source Folder', size=(15, 1), justification='right'), InputText('Source', focus=True),
               FolderBrowse()],
              [Text('Destination Folder', size=(15, 1), justification='right'), InputText('Dest'), FolderBrowse()],
              [Button('Ok')]]

    window = Window('Demo window..',
                    # default_element_size=(35,1),
                    auto_size_text=True,
                    auto_size_buttons=True,
                    disable_close=False,
                    ).Layout(layout)
    event, values = window.Read()
    print(event, values)
    window.Close()


if __name__ == '__main__':
    main()
    sys.exit(69)
