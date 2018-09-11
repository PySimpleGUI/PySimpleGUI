#!/usr/bin/python3
import tkinter as tk
from tkinter import filedialog
from tkinter.colorchooser import askcolor
from tkinter import ttk
import tkinter.scrolledtext as tkst
import tkinter.font
import datetime
import sys
import textwrap
import pickle
import calendar


# ----====----====----==== Constants the user CAN safely change ====----====----====----#
DEFAULT_WINDOW_ICON = 'default_icon.ico'
DEFAULT_ELEMENT_SIZE = (45,1)           # In CHARACTERS
DEFAULT_BUTTON_ELEMENT_SIZE = (10,1)           # In CHARACTERS
DEFAULT_MARGINS = (10,5)                # Margins for each LEFT/RIGHT margin is first term
DEFAULT_ELEMENT_PADDING = (5,3)         # Padding between elements (row, col) in pixels
DEFAULT_AUTOSIZE_TEXT = True
DEFAULT_AUTOSIZE_BUTTONS = True
DEFAULT_FONT = ("Helvetica", 10)
DEFAULT_TEXT_JUSTIFICATION = 'left'
DEFAULT_BORDER_WIDTH = 1
DEFAULT_AUTOCLOSE_TIME = 3              # time in seconds to show an autoclose form
DEFAULT_DEBUG_WINDOW_SIZE = (80,20)
DEFAULT_WINDOW_LOCATION = (None,None)
MAX_SCROLLED_TEXT_BOX_HEIGHT = 50
#################### COLOR STUFF ####################
BLUES = ("#082567","#0A37A3","#00345B")
PURPLES = ("#480656","#4F2398","#380474")
GREENS = ("#01826B","#40A860","#96D2AB", "#00A949","#003532")
YELLOWS = ("#F3FB62", "#F0F595")
TANS = ("#FFF9D5","#F4EFCF","#DDD8BA")
NICE_BUTTON_COLORS = ((GREENS[3], TANS[0]), ('#000000','#FFFFFF'),('#FFFFFF', '#000000'), (YELLOWS[0], PURPLES[1]),
               (YELLOWS[0], GREENS[3]), (YELLOWS[0], BLUES[2]))

COLOR_SYSTEM_DEFAULT = '1234567890'           # Colors should never be this long
if sys.platform == 'darwin':
    DEFAULT_BUTTON_COLOR = COLOR_SYSTEM_DEFAULT   # Foreground, Background (None, None) == System Default
    OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR = COLOR_SYSTEM_DEFAULT       # Colors should never be this long
else:
    DEFAULT_BUTTON_COLOR = ('white', BLUES[0])    # Foreground, Background (None, None) == System Default
    OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR = ('white', BLUES[0])           # Colors should never be this long

DEFAULT_ERROR_BUTTON_COLOR =("#FFFFFF", "#FF0000")
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
#--------------------------------------------------------------------------------
# Progress Bar Relief Choices
RELIEF_RAISED = 'raised'
RELIEF_SUNKEN = 'sunken'
RELIEF_FLAT = 'flat'
RELIEF_RIDGE = 'ridge'
RELIEF_GROOVE = 'groove'
RELIEF_SOLID = 'solid'

DEFAULT_PROGRESS_BAR_COLOR = (GREENS[0], '#D0D0D0')     # a nice green progress bar
DEFAULT_PROGRESS_BAR_SIZE = (25,20)         # Size of Progress Bar (characters for length, pixels for width)
DEFAULT_PROGRESS_BAR_BORDER_WIDTH=1
DEFAULT_PROGRESS_BAR_RELIEF = RELIEF_GROOVE
PROGRESS_BAR_STYLES = ('default','winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative')
DEFAULT_PROGRESS_BAR_STYLE = 'default'
DEFAULT_METER_ORIENTATION = 'Horizontal'
DEFAULT_SLIDER_ORIENTATION = 'vertical'
DEFAULT_SLIDER_BORDER_WIDTH=1
DEFAULT_SLIDER_RELIEF = tk.FLAT

DEFAULT_LISTBOX_SELECT_MODE = tk.SINGLE
SELECT_MODE_MULTIPLE = tk.MULTIPLE
LISTBOX_SELECT_MODE_MULTIPLE = 'multiple'
SELECT_MODE_BROWSE = tk.BROWSE
LISTBOX_SELECT_MODE_BROWSE = 'browse'
SELECT_MODE_EXTENDED = tk.EXTENDED
LISTBOX_SELECT_MODE_EXTENDED = 'extended'
SELECT_MODE_SINGLE = tk.SINGLE
LISTBOX_SELECT_MODE_SINGLE = 'single'

# DEFAULT_METER_ORIENTATION = 'Vertical'
# ----====----====----==== Constants the user should NOT f-with ====----====----====----#
ThisRow = 555666777         # magic number


# DEFAULT_WINDOW_ICON = ''
MESSAGE_BOX_LINE_WIDTH = 60

# a shameful global variable. This represents the top-level window information. Needed because opening a second window is different than opening the first.
class MyWindows():
    def __init__(self):
        self.NumOpenWindows = 0
        self.user_defined_icon = None

    def Decrement(self):
        self.NumOpenWindows -= 1 * (self.NumOpenWindows != 0)  # decrement if not 0
        # print('---- DECREMENTING Num Open Windows = {} ---'.format(self.NumOpenWindows))

    def Increment(self):
        self.NumOpenWindows += 1
        # print('++++ INCREMENTING Num Open Windows = {} ++++'.format(self.NumOpenWindows))

_my_windows = MyWindows()            # terrible hack using globals... means need a class for collecing windows

# ====================================================================== #
# One-liner functions that are handy as f_ck                             #
# ====================================================================== #
def RGB(red,green,blue): return '#%02x%02x%02x' % (red,green,blue)

# ====================================================================== #
# Enums for types                                                        #
# ====================================================================== #
# -------------------------  Button types  ------------------------- #
#todo Consider removing the Submit, Cancel types... they are just 'RETURN' type in reality
#uncomment this line and indent to go back to using Enums
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
ELEM_TYPE_TEXT = 1
ELEM_TYPE_INPUT_TEXT = 20
ELEM_TYPE_INPUT_COMBO = 21
ELEM_TYPE_INPUT_OPTION_MENU = 22
ELEM_TYPE_INPUT_RADIO = 5
ELEM_TYPE_INPUT_MULTILINE = 7
ELEM_TYPE_INPUT_CHECKBOX = 8
ELEM_TYPE_INPUT_SPIN = 9
ELEM_TYPE_BUTTON = 3
ELEM_TYPE_IMAGE = 30
ELEM_TYPE_CANVAS = 40
ELEM_TYPE_FRAME = 41
ELEM_TYPE_INPUT_SLIDER = 10
ELEM_TYPE_INPUT_LISTBOX = 11
ELEM_TYPE_OUTPUT = 300
ELEM_TYPE_COLUMN = 555
ELEM_TYPE_MENUBAR = 600
ELEM_TYPE_PROGRESS_BAR = 200
ELEM_TYPE_BLANK = 100

# -------------------------  MsgBox Buttons Types  ------------------------- #
MSG_BOX_YES_NO = 1
MSG_BOX_CANCELLED = 2
MSG_BOX_ERROR = 3
MSG_BOX_OK_CANCEL = 4
MSG_BOX_OK = 0
MSG_BOX_NO_BUTTONS = 5

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
    def __init__(self, type, scale=(None, None), size=(None, None), auto_size_text=None, font=None, background_color=None, text_color=None, key=None, pad=None):
        self.Size = size
        self.Type = type
        self.AutoSizeText = auto_size_text
        self.Scale = scale
        self.Pad = DEFAULT_ELEMENT_PADDING if pad is None else pad
        self.Font = font

        self.TKStringVar = None
        self.TKIntVar = None
        self.TKText = None
        self.TKEntry = None
        self.TKImage = None

        self.ParentForm=None
        self.TextInputDefault = None
        self.Position = (0,0)       # Default position Row 0, Col 0
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_ELEMENT_BACKGROUND_COLOR
        self.TextColor = text_color if text_color is not None else DEFAULT_ELEMENT_TEXT_COLOR
        self.Key = key             # dictionary key for return values

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
        return None

    def ReturnKeyHandler(self, event):
        MyForm = self.ParentForm
        button_element = self.FindReturnKeyBoundButton(MyForm)
        if button_element is not None:
            button_element.ButtonCallBack()


    def ListboxSelectHandler(self, event):
        MyForm = self.ParentForm
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def ComboboxSelectHandler(self, event):
        MyForm = self.ParentForm
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

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
    def __init__(self, default_text ='', scale=(None, None), size=(None, None), auto_size_text=None, password_char='',
                 justification=None, background_color=None, text_color=None, do_not_clear=False, key=None, focus=False, pad=None):
        '''
        Input a line of text Element
        :param default_text: Default value to display
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        :param auto_size_text: True if should shrink field to fit the default text
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
        super().__init__(ELEM_TYPE_INPUT_TEXT, scale=scale, size=size, auto_size_text=auto_size_text, background_color=bg, text_color=fg, key=key, pad=pad)


    def Update(self, value=None, disabled=None):
        if disabled is True:
            self.TKEntry['state'] = 'disabled'
        elif disabled is False:
            self.TKEntry['state'] = 'normal'
        if value is not None:
            try:
                self.TKStringVar.set(value)
            except: pass
            self.DefaultText = value

    def Get(self):
        return self.TKStringVar.get()

    def __del__(self):
        super().__del__()

# ---------------------------------------------------------------------- #
#                           Combo                                        #
# ---------------------------------------------------------------------- #
class InputCombo(Element):
    def __init__(self, values, default_value=None, scale=(None, None), size=(None, None), auto_size_text=None, background_color=None, text_color=None, change_submits=False, disabled=False, key=None, pad=None):
        '''
        Input Combo Box Element (also called Dropdown box)
        :param values:
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        :param auto_size_text: True if should shrink field to fit the default text
        :param background_color: Color for Element. Text or RGB Hex
        '''
        self.Values = values
        self.DefaultValue = default_value
        self.ChangeSubmits = change_submits
        self.TKCombo = None
        self.InitializeAsDisabled = disabled
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_COMBO, scale=scale, size=size, auto_size_text=auto_size_text, background_color=bg, text_color=fg, key=key, pad=pad)

    def Update(self, value=None, values=None, disabled=None):
        if values is not None:
            try:
                self.TKCombo['values'] = values
                self.TKCombo.current(0)
            except: pass
            self.Values = values
            for index, v in enumerate(self.Values):
                if v == value:
                    try:
                        self.TKCombo.current(index)
                    except: pass
                    self.DefaultValue = value
                    break
        if disabled == True:
            self.TKCombo['state'] = 'disable'
        elif disabled == False:
            self.TKCombo['state'] = 'enable'


    def __del__(self):
        try:
            self.TKCombo.__del__()
        except:
            pass
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Option Menu                                  #
# ---------------------------------------------------------------------- #
class InputOptionMenu(Element):
    def __init__(self, values, default_value=None, scale=(None, None), size=(None, None), auto_size_text=None, background_color=None, text_color=None, key=None, pad=None):
        '''
        Input Combo Box Element (also called Dropdown box)
        :param values:
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        :param auto_size_text: True if should shrink field to fit the default text
        :param background_color: Color for Element. Text or RGB Hex
        '''
        self.Values = values
        self.DefaultValue = default_value
        self.TKOptionMenu = None
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_OPTION_MENU, scale=scale, size=size, auto_size_text=auto_size_text, background_color=bg, text_color=fg, key=key, pad=pad)

    def Update(self, value=None, values=None, disabled=None):
        if values is not None:
            self.Values = values
        if self.Values is not None:
            for index, v in enumerate(self.Values):
                if v == value:
                    try:
                        self.TKStringVar.set(value)
                    except: pass
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

# ---------------------------------------------------------------------- #
#                           Listbox                                      #
# ---------------------------------------------------------------------- #
class Listbox(Element):
    def __init__(self, values, default_values=None, select_mode=None, change_submits=False, scale=(None, None), size=(None, None), auto_size_text=None, font=None, background_color=None, text_color=None, key=None, pad=None):
        '''
        Listbox Element
        :param values:
        :param select_mode: SELECT_MODE_BROWSE, SELECT_MODE_EXTENDED, SELECT_MODE_MULTIPLE, SELECT_MODE_SINGLE
        :param font:
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        :param auto_size_text: True if should shrink field to fit the default text
        :param background_color: Color for Element. Text or RGB Hex        '''
        self.Values = values
        self.DefaultValues = default_values
        self.TKListbox = None
        self.ChangeSubmits = change_submits
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

        super().__init__(ELEM_TYPE_INPUT_LISTBOX, scale=scale, size=size, auto_size_text=auto_size_text, font=font, background_color=bg, text_color=fg, key=key, pad=pad)

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
            except: pass
        self.DefaultValues = values

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
    def __init__(self, text, group_id, default=False, scale=(None, None), size=(None, None), auto_size_text=None, background_color=None, text_color=None, font=None, key=None, pad=None):
        '''
        Radio Button Element
        :param text:
        :param group_id:
        :param default:
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        :param auto_size_text: True if should shrink field to fit the default text
        :param background_color: Color for Element. Text or RGB Hex
        :param font:
        '''
        self.InitialState = default
        self.Text = text
        self.TKRadio = None
        self.GroupID = group_id
        self.Value = None
        self.TextColor = text_color if text_color else DEFAULT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_RADIO, scale=scale , size=size, auto_size_text=auto_size_text, font=font, background_color=background_color, text_color=self.TextColor, key=key, pad=pad)

    def Update(self, value=None, disabled=None):
        location = EncodeRadioRowCol(self.Position[0], self.Position[1])
        if value is not None:
            try:
                self.TKIntVar.set(location)
            except: pass
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
    def __init__(self, text, default=False, scale=(None, None), size=(None, None), auto_size_text=None, font=None, background_color=None, text_color=None, key=None, pad=None):
        '''
        Check Box Element
        :param text:
        :param default:
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        :param auto_size_text: True if should shrink field to fit the default text
        :param background_color: Color for Element. Text or RGB Hex
        :param font:
        '''
        self.Text = text
        self.InitialState = default
        self.Value = None
        self.TKCheckbutton = None
        self.TextColor = text_color if text_color else DEFAULT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_CHECKBOX, scale=scale, size=size, auto_size_text=auto_size_text, font=font, background_color=background_color, text_color=self.TextColor, key=key, pad=pad)

    def Get(self):
        return self.TKIntVar.get()

    def Update(self, value=None, disabled=None):
        if value is not None:
            try:
                self.TKIntVar.set(value)
                self.InitialState = value
            except: pass
        if disabled == True:
            self.TKCheckbutton.configure(state='disabled')
        elif disabled == False:
            self.TKCheckbutton.configure(state='normal')


    def __del__(self):
        super().__del__()

# ---------------------------------------------------------------------- #
#                           Spin                                         #
# ---------------------------------------------------------------------- #

class Spin(Element):
    # Values = None
    # TKSpinBox = None
    def __init__(self, values, initial_value=None, change_submits=False, scale=(None, None), size=(None, None), auto_size_text=None, font=None, background_color=None, text_color=None, key=None, pad=None):
        '''
        Spin Box Element
        :param values:
        :param initial_value:
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        :param auto_size_text: True if should shrink field to fit the default text
        :param background_color: Color for Element. Text or RGB Hex
        :param font:
        '''
        self.Values = values
        self.DefaultValue = initial_value
        self.ChangeSubmits = change_submits
        self.TKSpinBox = None
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_SPIN, scale, size, auto_size_text, font=font,background_color=bg, text_color=fg, key=key, pad=pad)
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
            except: pass
        self.DefaultValue = value
        if disabled == True:
            self.TKSpinBox.configure(state='disabled')
        elif disabled == False:
            self.TKSpinBox.configure(state='normal')


    def SpinChangedHandler(self, event):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
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
    def __init__(self, default_text='', enter_submits = False, scale=(None, None), size=(None, None), auto_size_text=None, background_color=None, text_color=None, do_not_clear=False, key=None, focus=False, pad=None):
        '''
        Input Multi-line Element
        :param default_text:
        :param enter_submits:
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        :param auto_size_text: True if should shrink field to fit the default text
        :param background_color: Color for Element. Text or RGB Hex
        '''
        self.DefaultText = default_text
        self.EnterSubmits = enter_submits
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        self.Focus = focus
        self.do_not_clear = do_not_clear
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_INPUT_MULTILINE, scale=scale, size=size, auto_size_text=auto_size_text, background_color=bg, text_color=fg, key=key, pad=pad)
        return

    def Update(self, value=None, disabled=None):
        if value is not None:
            try:
                self.TKText.delete('1.0', tk.END)
                self.TKText.insert(1.0, value)
            except: pass
            self.DefaultText = value
        if disabled == True:
            self.TKText.configure(state='disabled')
        elif disabled == False:
            self.TKText.configure(state='normal')

    def Get(self):
        return  self.TKText.get(1.0, tk.END)


    def __del__(self):
        super().__del__()

# ---------------------------------------------------------------------- #
#                                       Text                             #
# ---------------------------------------------------------------------- #
class Text(Element):
    def __init__(self, text, scale=(None, None), size=(None, None), auto_size_text=None, font=None, text_color=None, background_color=None,justification=None, pad=None, key=None):
        '''
        Text Element - Displays text in your form.  Can be updated in non-blocking forms
        :param text: The text to display
        :param scale: Scaling factor (w,h) (2,2)= 2 * Size
        :param size: Size of Element in Characters
        :param auto_size_text: True if the field should shrink to fit the text
        :param font: Font name and size ("name", size)
        :param text_color: Text Color name or RGB hex value '#RRGGBB'
        :param background_color: Background color for text (name or RGB Hex)
        :param justification: 'left', 'right', 'center'
        '''
        self.DisplayText = text
        self.TextColor = text_color if text_color else DEFAULT_TEXT_COLOR
        self.Justification = justification
        if background_color is None:
            bg = DEFAULT_TEXT_ELEMENT_BACKGROUND_COLOR
        else:
            bg = background_color
        super().__init__(ELEM_TYPE_TEXT, scale, size, auto_size_text, background_color=bg, font=font if font else DEFAULT_FONT, text_color=self.TextColor, pad=pad, key=key)
        return

    def Update(self, value = None, background_color=None, text_color=None, font=None):
        if value is not None:
            self.DisplayText=value
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


# ---------------------------------------------------------------------- #
#                       TKProgressBar                                    #
#  Emulate the TK ProgressBar using canvas and rectangles
# ---------------------------------------------------------------------- #

class TKProgressBar():
    def __init__(self, root, max, length=400, width=DEFAULT_PROGRESS_BAR_SIZE[1], style=DEFAULT_PROGRESS_BAR_STYLE, relief=DEFAULT_PROGRESS_BAR_RELIEF, border_width=DEFAULT_PROGRESS_BAR_BORDER_WIDTH, orientation='horizontal', BarColor=(None,None)):
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
                s.configure(str(length)+str(width)+"my.Horizontal.TProgressbar", background=BarColor[0], troughcolor=BarColor[1], troughrelief=relief, borderwidth=border_width, thickness=width)
            else:
                s.configure(str(length)+str(width)+"my.Horizontal.TProgressbar", troughrelief=relief, borderwidth=border_width, thickness=width)

            self.TKProgressBarForReal = ttk.Progressbar(root, maximum=self.Max, style=str(length)+str(width)+'my.Horizontal.TProgressbar', length=length, orient=tk.HORIZONTAL, mode='determinate')
        else:
            s = ttk.Style()
            s.theme_use(style)
            if BarColor != COLOR_SYSTEM_DEFAULT:
                s.configure(str(length)+str(width)+"my.Vertical.TProgressbar", background=BarColor[0], troughcolor=BarColor[1], troughrelief=relief, borderwidth=border_width, thickness=width)
            else:
                s.configure(str(length)+str(width)+"my.Vertical.TProgressbar",  troughrelief=relief, borderwidth=border_width, thickness=width)
            self.TKProgressBarForReal = ttk.Progressbar(root,  maximum=self.Max, style=str(length)+str(width)+'my.Vertical.TProgressbar', length=length, orient=tk.VERTICAL, mode='determinate')

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
            except: return False
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
class TKOutput(tk.Frame):
    def __init__(self, parent, width, height, bd, background_color=None, text_color=None, font=None, pad=None):
        frame = tk.Frame(parent)
        tk.Frame.__init__(self, frame)
        self.output = tk.Text(frame, width=width, height=height, bd=bd, font=font)
        if background_color and background_color != COLOR_SYSTEM_DEFAULT:
            self.output.configure(background=background_color)
            frame.configure(background=background_color)
        if text_color and text_color != COLOR_SYSTEM_DEFAULT:
            self.output.configure(fg=text_color)
        self.vsb = tk.Scrollbar(frame, orient="vertical", command=self.output.yview)
        self.output.configure(yscrollcommand=self.vsb.set)
        self.output.pack(side="left", fill="both")
        self.vsb.pack(side="left", fill="y")
        frame.pack(side="left", padx=pad[0], pady=pad[1])
        self.previous_stdout = sys.stdout
        self.previous_stderr = sys.stderr

        sys.stdout = self
        sys.stderr = self
        self.pack()

    def write(self, txt):
        try:
            self.output.insert(tk.END, str(txt))
            self.output.see(tk.END)
        except:
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
    def __init__(self, scale=(None, None), size=(None, None), background_color=None, text_color=None, pad=None, font=None):
        '''
        Output Element - reroutes stdout, stderr to this window
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        :param background_color: Color for Element. Text or RGB Hex
        '''
        self.TKOut = None
        bg = background_color if background_color else DEFAULT_INPUT_ELEMENTS_COLOR
        fg = text_color if text_color is not None else DEFAULT_INPUT_TEXT_COLOR

        super().__init__(ELEM_TYPE_OUTPUT, scale=scale, size=size, background_color=bg, text_color=fg, pad=pad, font=font)

    def __del__(self):
        try:
            self.TKOut.__del__()
        except:
            pass
        super().__del__()

# ---------------------------------------------------------------------- #
#                           Button Class                                 #
# ---------------------------------------------------------------------- #
class Button(Element):
    def __init__(self, button_type=BUTTON_TYPE_CLOSES_WIN, target=(None, None), button_text='', file_types=(("ALL Files", "*.*"),), image_filename=None, image_size=(None, None), image_subsample=None, border_width=None, scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, default_value = None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
        '''
        Button Element - Specifies all types of buttons
        :param button_type:
        :param target:
        :param button_text:
        :param file_types:
        :param image_filename:
        :param image_size:
        :param image_subsample:
        :param border_width:
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        :param auto_size_button:
        :param button_color:
        :param font:
        '''
        self.AutoSizeButton = auto_size_button
        self.BType = button_type
        self.FileTypes = file_types
        self.TKButton = None
        self.Target = target
        self.ButtonText = button_text
        self.ButtonColor = button_color if button_color else DEFAULT_BUTTON_COLOR
        self.ImageFilename = image_filename
        self.ImageSize = image_size
        self.ImageSubsample = image_subsample
        self.UserData = None
        self.BorderWidth = border_width if border_width is not None else DEFAULT_BORDER_WIDTH
        self.BindReturnKey = bind_return_key
        self.Focus = focus
        self.TKCal = None
        self.DefaultValue = None
        super().__init__(ELEM_TYPE_BUTTON, scale=scale, size=size, font=font, pad=pad, key=key)
        return

    # Realtime button release callback
    def ButtonReleaseCallBack(self, parm):
        r, c = self.Position
        self.LastButtonClickedWasRealtime = False
        self.ParentForm.LastButtonClicked = None

    # Realtime button callback
    def ButtonPressCallBack(self, parm):
        r, c = self.Position
        self.ParentForm.LastButtonClickedWasRealtime = True
        self.ParentForm.LastButtonClicked = self.ButtonText

    # -------  Button Callback  ------- #
    def ButtonCallBack(self):
        global _my_windows
        # Buttons modify targets or return from the form
        # If modifying target, get the element object at the target and modify its StrVar
        target = self.Target
        target_element = None
        if target[0] == ThisRow:
            target = [self.Position[0], target[1]]
            if target[1] < 0:
                target[1] = self.Position[1] + target[1]
        strvar = None
        if target == (None, None):
            strvar = self.TKStringVar
        else:
            if target[0] < 0:
                target = [self.Position[0] + target[0], target[1]]
            target_element = self.ParentForm._GetElementAtLocation(target)
            try:
                strvar = target_element.TKStringVar
            except: pass
        filetypes = [] if self.FileTypes is None else self.FileTypes
        if self.BType == BUTTON_TYPE_BROWSE_FOLDER:
            folder_name = tk.filedialog.askdirectory()  # show the 'get folder' dialog box
            try:
                strvar.set(folder_name)
                self.TKStringVar.set(folder_name)
            except: pass
        elif self.BType == BUTTON_TYPE_BROWSE_FILE:
            file_name = tk.filedialog.askopenfilename(filetypes=filetypes)  # show the 'get file' dialog box
            strvar.set(file_name)
            self.TKStringVar.set(file_name)
        elif self.BType == BUTTON_TYPE_COLOR_CHOOSER:
            color = tk.colorchooser.askcolor()  # show the 'get file' dialog box
            color = color[1]         # save only the #RRGGBB portion
            strvar.set(color)
            self.TKStringVar.set(color)
        elif self.BType == BUTTON_TYPE_BROWSE_FILES:
            file_name = tk.filedialog.askopenfilenames(filetypes=filetypes)
            file_name = ';'.join(file_name)
            strvar.set(file_name)
            self.TKStringVar.set(file_name)
        elif self.BType == BUTTON_TYPE_SAVEAS_FILE:
            file_name = tk.filedialog.asksaveasfilename(filetypes=filetypes)  # show the 'get file' dialog box
            strvar.set(file_name)
            self.TKStringVar.set(file_name)
        elif self.BType == BUTTON_TYPE_CLOSES_WIN:  # this is a return type button so GET RESULTS and destroy window
            # first, get the results table built
            # modify the Results table in the parent FlexForm object
            r,c = self.Position
            self.ParentForm.LastButtonClicked = self.ButtonText
            self.ParentForm.FormRemainedOpen = False
            # if the form is tabbed, must collect all form's results and destroy all forms
            if self.ParentForm.IsTabbedForm:
                self.ParentForm.UberParent._Close()
            else:
                self.ParentForm._Close()
            self.ParentForm.TKroot.quit()
            if self.ParentForm.NonBlocking:
                self.ParentForm.TKroot.destroy()
                _my_windows.Decrement()
        elif self.BType == BUTTON_TYPE_READ_FORM:                   # LEAVE THE WINDOW OPEN!! DO NOT CLOSE
            # first, get the results table built
            # modify the Results table in the parent FlexForm object
            self.ParentForm.LastButtonClicked = self.ButtonText
            self.ParentForm.FormRemainedOpen = True
            self.ParentForm.TKroot.quit()               # kick the users out of the mainloop
        elif self.BType == BUTTON_TYPE_CLOSES_WIN_ONLY:  # this is a return type button so GET RESULTS and destroy window
            # if the form is tabbed, must collect all form's results and destroy all forms
            if self.ParentForm.IsTabbedForm:
                self.ParentForm.UberParent._Close()
            else:
                self.ParentForm._Close()
            if self.ParentForm.NonBlocking:
                self.ParentForm.TKroot.destroy()
                _my_windows.Decrement()
        elif self.BType == BUTTON_TYPE_CALENDAR_CHOOSER:  # this is a return type button so GET RESULTS and destroy window
            root = tk.Toplevel()
            root.title('Calendar Chooser')
            self.TKCal = TKCalendar(master=root, firstweekday=calendar.SUNDAY, target_element=target_element)
            self.TKCal.pack(expand=1, fill='both')
            # self.ParentForm.TKRroot.mainloop()
            root.update()
            # root.mainloop()
            # root.update()
            # strvar.set(ttkcal.selection)

        return

    def Update(self, value=None, text=None, button_color=(None, None), disabled=None):
        try:
            if text is not None:
                self.TKButton.configure(text=text)
                self.ButtonText = text
            if button_color != (None, None):
                self.TKButton.config(foreground=button_color[0], background=button_color[1])
        except:
            return
        if value is not None:
            self.DefaultValue = value
        if disabled == True:
            self.TKButton['state'] = 'disabled'
        elif disabled == False:
            self.TKButton['state'] = 'normal'



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
    def __init__(self, max_value, orientation=None, scale=(None, None), size=(None, None), auto_size_text=None, bar_color=(None, None), style=None, border_width=None, relief=None, key=None, pad=None):
        '''
        Progress Bar Element
        :param max_value:
        :param orientation:
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        :param auto_size_text: True if should shrink field to fit the default text
        :param bar_color:
        :param style:
        :param border_width:
        :param relief:
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
        super().__init__(ELEM_TYPE_PROGRESS_BAR, scale=scale, size=size, auto_size_text=auto_size_text, key=key, pad=pad)
        return

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
    def __init__(self, filename=None, data=None,scale=(None, None), size=(None, None), pad=None, key=None):
        '''
        Image Element
        :param filename:
        :param scale: Adds multiplier to size (w,h)
        :param size: Size of field in characters
        '''
        self.Filename = filename
        self.Data = data
        self.tktext_label = None
        if data is None and filename is None:
            print('* Warning... no image specified in Image Element! *')
        super().__init__(ELEM_TYPE_IMAGE, scale=scale, size=size, pad=pad, key=key)
        return

    def Update(self, filename=None, data=None):
        if filename is not None:
            image = tk.PhotoImage(file=filename)
        elif data is not None:
            if type(data) is bytes:
                image = tk.PhotoImage(data=data)
            else:
                image = data
        else: return
        width, height = image.width(), image.height()
        self.tktext_label.configure(image=image, width=width, height=height)
        # self.tktext_label.configure(image=image)
        self.tktext_label.image = image

    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Canvas                                       #
# ---------------------------------------------------------------------- #
class Canvas(Element):
    def __init__(self, canvas=None, background_color=None, scale=(None, None), size=(None, None), pad=None, key=None):
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.TKCanvas = canvas

        super().__init__(ELEM_TYPE_CANVAS, background_color=background_color, scale=scale, size=size, pad=pad, key=key)
        return

    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Frame                                        #
# ---------------------------------------------------------------------- #
class Frame(Element):
    def __init__(self, frame=None, background_color=None, scale=(None, None), size=(None, None), pad=None, key=None):
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.TKFrame = frame

        super().__init__(ELEM_TYPE_FRAME, background_color=background_color, scale=scale, size=size, pad=pad, key=key)
        return

    def __del__(self):
        super().__del__()

# ---------------------------------------------------------------------- #
#                           Slider                                       #
# ---------------------------------------------------------------------- #
class Slider(Element):
    def __init__(self, range=(None,None), default_value=None, resolution=None, orientation=None, border_width=None, relief=None, change_submits=False, scale=(None, None), size=(None, None), font=None, background_color=None, text_color=None, key=None, pad=None):
        '''
        Slider
        :param range:
        :param default_value:
        :param resolution:
        :param orientation:
        :param border_width:
        :param relief:
        :param change_submits:
        :param scale:
        :param size:
        :param font:
        :param background_color:
        :param text_color:
        :param key:
        :param pad:
        '''
        self.TKScale = None
        self.Range = (1,10) if range == (None, None) else range
        self.DefaultValue = self.Range[0] if default_value is None else default_value
        self.Orientation = orientation if orientation else DEFAULT_SLIDER_ORIENTATION
        self.BorderWidth = border_width if border_width else DEFAULT_SLIDER_BORDER_WIDTH
        self.Relief = relief if relief else DEFAULT_SLIDER_RELIEF
        self.Resolution = 1 if resolution is None else resolution
        self.ChangeSubmits = change_submits

        super().__init__(ELEM_TYPE_INPUT_SLIDER, scale=scale, size=size, font=font, background_color=background_color, text_color=text_color, key=key, pad=pad)
        return

    def Update(self, value=None, range=(None, None), disabled=None):
        if value is not None:
            try:
                self.TKIntVar.set(value)
                if range != (None, None):
                    self.TKScale.config(from_ = range[0], to_ = range[1])
            except: pass
            self.DefaultValue = value
        if disabled == True:
            self.TKScale['state'] = 'disabled'
        elif disabled == False:
            self.TKScale['state'] = 'normal'

    def SliderChangedHandler(self, event):
        # first, get the results table built
        # modify the Results table in the parent FlexForm object
        self.ParentForm.LastButtonClicked = ''
        self.ParentForm.FormRemainedOpen = True
        self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                          TkScrollableFrame (Used by Column (SOON)      #
# ---------------------------------------------------------------------- #
class TkScrollableFrame(tk.Frame):
    def __init__(self, master, **kwargs):
        tk.Frame.__init__(self, master, **kwargs)

        # create a canvas object and a vertical scrollbar for scrolling it
        self.vscrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.vscrollbar.pack(side='right', fill="y",  expand="false")

        self.hscrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.hscrollbar.pack(side='bottom', fill="x",  expand="false")

        self.canvas = tk.Canvas(self, yscrollcommand=self.vscrollbar.set, xscrollcommand=self.hscrollbar.set)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.vscrollbar.config(command=self.canvas.yview)
        self.hscrollbar.config(command=self.canvas.xview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.TKFrame = tk.Frame(self.canvas, **kwargs)
        self.canvas.create_window(0, 0, window=self.TKFrame, anchor="nw")
        self.canvas.config(borderwidth=0, highlightthickness=0)
        self.TKFrame.config(borderwidth=0, highlightthickness=0)
        self.config(borderwidth=0, highlightthickness=0)

        self.bind('<Configure>', self.set_scrollregion)

        self.bind_mouse_scroll(self.canvas, self.yscroll)
        self.bind_mouse_scroll(self.hscrollbar, self.xscroll)
        self.bind_mouse_scroll(self.vscrollbar, self.yscroll)


    def yscroll(self, event):
        if event.num == 5 or event.delta < 0:
            self.canvas.yview_scroll(1, "unit")
        elif event.num == 4 or event.delta > 0:
            self.canvas.yview_scroll(-1, "unit")

    def xscroll(self, event):
        if event.num == 5 or event.delta < 0:
            self.canvas.xview_scroll(1, "unit")
        elif event.num == 4 or event.delta > 0:
            self.canvas.xview_scroll(-1, "unit")

    def bind_mouse_scroll(self, parent, mode):
        # ~~ Windows only
        parent.bind("<MouseWheel>", mode)
        # ~~ Unix only
        parent.bind("<Button-4>", mode)
        parent.bind("<Button-5>", mode)

    def set_scrollregion(self, event=None):
        """ Set the scroll region on the canvas"""
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))


# ---------------------------------------------------------------------- #
#                           Column                                       #
# ---------------------------------------------------------------------- #
class Column(Element):
    def __init__(self, layout, background_color = None, size=(None, None), pad=None, scrollable=False):
        self.UseDictionary = False
        self.ReturnValues = None
        self.ReturnValuesList = []
        self.ReturnValuesDictionary = {}
        self.DictionaryKeyCounter = 0
        self.ParentWindow = None
        self.Rows = []
        self.ParentForm = None
        self.TKFrame = None
        self.Scrollable = scrollable
        bg = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR

        self.Layout(layout)

        super().__init__(ELEM_TYPE_COLUMN, background_color=background_color, size=size, pad=pad)
        return

    def AddRow(self, *args):
        ''' Parms are a variable number of Elements '''
        NumRows = len(self.Rows)               # number of existing rows is our row number
        CurrentRowNumber = NumRows             # this row's number
        CurrentRow = []                     # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):                    # Loop through list of elements and add them to the row
            element.Position = (CurrentRowNumber, i)
            CurrentRow.append(element)
            if element.Key is not None:
                self.UseDictionary = True
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    def Layout(self, rows):
        for row in rows:
            self.AddRow(*row)

    def __del__(self):
        for row in self.Rows:
            for element in row:
                element.__del__()
        try:
            del(self.TKFrame)
        except:
            pass
        super().__del__()


# ---------------------------------------------------------------------- #
#                           Calendar                                     #
# ---------------------------------------------------------------------- #
class TKCalendar(ttk.Frame):
    """
    This code was shamelessly lifted from moshekaplan's repository - moshekaplan/tkinter_components
    """
    # XXX ToDo: cget and configure

    datetime = calendar.datetime.datetime
    timedelta = calendar.datetime.timedelta

    def __init__(self, master=None, target_element=None, **kw):
        """
        WIDGET-SPECIFIC OPTIONS

            locale, firstweekday, year, month, selectbackground,
            selectforeground
        """
        self._TargetElement = target_element
        # remove custom options from kw before initializating ttk.Frame
        fwday = kw.pop('firstweekday', calendar.MONDAY)
        year = kw.pop('year', self.datetime.now().year)
        month = kw.pop('month', self.datetime.now().month)
        locale = kw.pop('locale', None)
        sel_bg = kw.pop('selectbackground', '#ecffc4')
        sel_fg = kw.pop('selectforeground', '#05640e')

        self._date = self.datetime(year, month, 1)
        self._selection = None # no date selected
        ttk.Frame.__init__(self, master, **kw)

        # instantiate proper calendar class
        if locale is None:
            self._cal = calendar.TextCalendar(fwday)
        else:
            self._cal =  calendar.LocaleTextCalendar(fwday, locale)

        self.__setup_styles()       # creates custom styles
        self.__place_widgets()      # pack/grid used widgets
        self.__config_calendar()    # adjust calendar columns and setup tags
        # configure a canvas, and proper bindings, for selecting dates
        self.__setup_selection(sel_bg, sel_fg)

        # store items ids, used for insertion later
        self._items = [self._calendar.insert('', 'end', values='')
                            for _ in range(6)]
        # insert dates in the currently empty calendar
        self._build_calendar()

    def __setitem__(self, item, value):
        if item in ('year', 'month'):
            raise AttributeError("attribute '%s' is not writeable" % item)
        elif item == 'selectbackground':
            self._canvas['background'] = value
        elif item == 'selectforeground':
            self._canvas.itemconfigure(self._canvas.text, item=value)
        else:
            ttk.Frame.__setitem__(self, item, value)

    def __getitem__(self, item):
        if item in ('year', 'month'):
            return getattr(self._date, item)
        elif item == 'selectbackground':
            return self._canvas['background']
        elif item == 'selectforeground':
            return self._canvas.itemcget(self._canvas.text, 'fill')
        else:
            r = ttk.tclobjs_to_py({item: ttk.Frame.__getitem__(self, item)})
            return r[item]

    def __setup_styles(self):
        # custom ttk styles
        style = ttk.Style(self.master)
        arrow_layout = lambda dir: (
            [('Button.focus', {'children': [('Button.%sarrow' % dir, None)]})]
        )
        style.layout('L.TButton', arrow_layout('left'))
        style.layout('R.TButton', arrow_layout('right'))

    def __place_widgets(self):
        # header frame and its widgets
        hframe = ttk.Frame(self)
        lbtn = ttk.Button(hframe, style='L.TButton', command=self._prev_month)
        rbtn = ttk.Button(hframe, style='R.TButton', command=self._next_month)
        self._header = ttk.Label(hframe, width=15, anchor='center')
        # the calendar
        self._calendar = ttk.Treeview(self, show='', selectmode='none', height=7)

        # pack the widgets
        hframe.pack(in_=self, side='top', pady=4, anchor='center')
        lbtn.grid(in_=hframe)
        self._header.grid(in_=hframe, column=1, row=0, padx=12)
        rbtn.grid(in_=hframe, column=2, row=0)
        self._calendar.pack(in_=self, expand=1, fill='both', side='bottom')

    def __config_calendar(self):
        cols = self._cal.formatweekheader(3).split()
        self._calendar['columns'] = cols
        self._calendar.tag_configure('header', background='grey90')
        self._calendar.insert('', 'end', values=cols, tag='header')
        # adjust its columns width
        font = tkinter.font.Font()
        maxwidth = max(font.measure(col) for col in cols)
        for col in cols:
            self._calendar.column(col, width=maxwidth, minwidth=maxwidth,
                anchor='e')

    def __setup_selection(self, sel_bg, sel_fg):
        self._font = tkinter.font.Font()
        self._canvas = canvas = tk.Canvas(self._calendar,
            background=sel_bg, borderwidth=0, highlightthickness=0)
        canvas.text = canvas.create_text(0, 0, fill=sel_fg, anchor='w')

        canvas.bind('<ButtonPress-1>', lambda evt: canvas.place_forget())
        self._calendar.bind('<Configure>', lambda evt: canvas.place_forget())
        self._calendar.bind('<ButtonPress-1>', self._pressed)

    def __minsize(self, evt):
        width, height = self._calendar.master.geometry().split('x')
        height = height[:height.index('+')]
        self._calendar.master.minsize(width, height)

    def _build_calendar(self):
        year, month = self._date.year, self._date.month

        # update header text (Month, YEAR)
        header = self._cal.formatmonthname(year, month, 0)
        self._header['text'] = header.title()

        # update calendar shown dates
        cal = self._cal.monthdayscalendar(year, month)
        for indx, item in enumerate(self._items):
            week = cal[indx] if indx < len(cal) else []
            fmt_week = [('%02d' % day) if day else '' for day in week]
            self._calendar.item(item, values=fmt_week)

    def _show_selection(self, text, bbox):
        """Configure canvas for a new selection."""
        x, y, width, height = bbox

        textw = self._font.measure(text)

        canvas = self._canvas
        canvas.configure(width=width, height=height)
        canvas.coords(canvas.text, width - textw, height / 2 - 1)
        canvas.itemconfigure(canvas.text, text=text)
        canvas.place(in_=self._calendar, x=x, y=y)

    # Callbacks

    def _pressed(self, evt):
        """Clicked somewhere in the calendar."""
        x, y, widget = evt.x, evt.y, evt.widget
        item = widget.identify_row(y)
        column = widget.identify_column(x)

        if not column or not item in self._items:
            # clicked in the weekdays row or just outside the columns
            return

        item_values = widget.item(item)['values']
        if not len(item_values): # row is empty for this month
            return

        text = item_values[int(column[1]) - 1]
        if not text: # date is empty
            return

        bbox = widget.bbox(item, column)
        if not bbox: # calendar not visible yet
            return

        # update and then show selection
        text = '%02d' % text
        self._selection = (text, item, column)
        self._show_selection(text, bbox)
        year, month = self._date.year, self._date.month
        try:
            self._TargetElement.Update(self.datetime(year, month, int(self._selection[0])))
        except: pass

    def _prev_month(self):
        """Updated calendar to show the previous month."""
        self._canvas.place_forget()

        self._date = self._date - self.timedelta(days=1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstuct calendar

    def _next_month(self):
        """Update calendar to show the next month."""
        self._canvas.place_forget()

        year, month = self._date.year, self._date.month
        self._date = self._date + self.timedelta(
            days=calendar.monthrange(year, month)[1] + 1)
        self._date = self.datetime(self._date.year, self._date.month, 1)
        self._build_calendar() # reconstruct calendar

    # Properties

    @property
    def selection(self):
        """Return a datetime representing the current selected date."""
        if not self._selection:
            return None

        year, month = self._date.year, self._date.month
        return self.datetime(year, month, int(self._selection[0]))


# ---------------------------------------------------------------------- #
#                           Canvas                                       #
# ---------------------------------------------------------------------- #
class Menu(Element):
    def __init__(self, menu_definition, command=None, background_color=None, scale=(None, None), size=(None, None), pad=None, key=None):
        self.BackgroundColor = background_color if background_color is not None else DEFAULT_BACKGROUND_COLOR
        self.Command = command
        self.MenuDefinition = menu_definition
        self.TKMenu = None

        super().__init__(ELEM_TYPE_MENUBAR, background_color=background_color, scale=scale, size=size, pad=pad, key=key)
        return

    def MenuItemChosenCallback(self, item_chosen):
        # print('IN MENU ITEM CALLBACK', item_chosen)
        self.ParentForm.LastButtonClicked = item_chosen
        self.ParentForm.FormRemainedOpen = True
        self.ParentForm.TKroot.quit()  # kick the users out of the mainloop

    def __del__(self):
        super().__del__()


# ------------------------------------------------------------------------- #
#                       FlexForm CLASS                                      #
# ------------------------------------------------------------------------- #
class FlexForm:
    '''
    Display a user defined for and return the filled in data
    '''
    def __init__(self, title, default_element_size=DEFAULT_ELEMENT_SIZE, default_button_element_size = (None, None), auto_size_text=None, auto_size_buttons=None, scale=(None, None), location=(None, None), button_color=None, font=None, progress_bar_color=(None, None), background_color=None, is_tabbed_form=False, border_depth=None, auto_close=False, auto_close_duration=DEFAULT_AUTOCLOSE_TIME, icon=DEFAULT_WINDOW_ICON, return_keyboard_events=False, use_default_focus=True, text_justification=None, no_titlebar=False, grab_anywhere=None, keep_on_top=False):
        self.AutoSizeText = auto_size_text if auto_size_text is not None else DEFAULT_AUTOSIZE_TEXT
        self.AutoSizeButtons = auto_size_buttons if auto_size_buttons is not None else DEFAULT_AUTOSIZE_BUTTONS
        self.Title = title
        self.Rows = []                     # a list of ELEMENTS for this row
        self.DefaultElementSize = default_element_size
        self.DefaultButtonElementSize = default_button_element_size if default_button_element_size != (None, None) else DEFAULT_BUTTON_ELEMENT_SIZE
        self.Scale = scale
        self.Location = location
        self.ButtonColor = button_color if button_color else DEFAULT_BUTTON_COLOR
        self.BackgroundColor = background_color if background_color else DEFAULT_BACKGROUND_COLOR
        self.IsTabbedForm = is_tabbed_form
        self.ParentWindow = None
        self.Font = font if font else DEFAULT_FONT
        self.RadioDict = {}
        self.BorderDepth = border_depth
        # self.WindowIcon = icon
        # self.WindowIcon = icon if icon else icon_tempfile
        self.WindowIcon = icon if not None else _my_windows.user_defined_icon
        self.AutoClose = auto_close
        self.NonBlocking = False
        self.TKroot = None
        self.TKrootDestroyed = False
        self.FormRemainedOpen = False
        self.TKAfterID = None
        self.ProgressBarColor = progress_bar_color
        self.AutoCloseDuration = auto_close_duration
        self.UberParent = None
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

    # ------------------------- Add ONE Row to Form ------------------------- #
    def AddRow(self, *args):
        ''' Parms are a variable number of Elements '''
        NumRows = len(self.Rows)               # number of existing rows is our row number
        CurrentRowNumber = NumRows             # this row's number
        CurrentRow = []                     # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):                    # Loop through list of elements and add them to the row
            element.Position = (CurrentRowNumber, i)
            CurrentRow.append(element)
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    # ------------------------- Add Multiple Rows to Form ------------------------- #
    def AddRows(self,rows):
        for row in rows:
            self.AddRow(*row)

    def Layout(self,rows):
        self.AddRows(rows)

    def LayoutAndRead(self,rows, non_blocking=False):
        self.AddRows(rows)
        self.Show(non_blocking=non_blocking)
        return self.ReturnValues

    def LayoutAndShow(self, rows):
        raise DeprecationWarning('LayoutAndShow is no longer supported... change your call to LayoutAndRead')

    # ------------------------- ShowForm   THIS IS IT! ------------------------- #
    def Show(self, non_blocking=False):
        self.Shown = True
        # Compute num rows & num cols (it'll come in handy debugging)
        self.NumRows = len(self.Rows)
        self.NumCols = max(len(row) for row in self.Rows)
        self.NonBlocking=non_blocking

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
    def SetIcon(self, icon):
        self.WindowIcon = icon
        try:
            self.TKroot.iconbitmap(icon)
        except: pass

    def _GetElementAtLocation(self, location):
        (row_num,col_num) = location
        row = self.Rows[row_num]
        element = row[col_num]
        return element

    def _GetDefaultElementSize(self):
        return self.DefaultElementSize

    def _AutoCloseAlarmCallback(self):
        try:
            if self.UberParent:
                window = self.UberParent
            else:
                window = self
            if window:
                window._Close()
                self.TKroot.quit()
                self.RootNeedsDestroying = True
        except:
            pass

    def Read(self):
        self.NonBlocking = False
        if self.TKrootDestroyed:
            return None, None
        if not self.Shown:
            self.Show()
        else:
            InitializeResults(self)
            self.TKroot.mainloop()
            if self.RootNeedsDestroying:
                self.TKroot.destroy()
                _my_windows.Decrement()
            # if form was closed with X
            if self.LastButtonClicked is None and self.LastKeyboardEvent is None and self.ReturnValues[0] is None:
                _my_windows.Decrement()
        if self.LastKeyboardEvent is not None or self.LastButtonClicked is not None:
            return BuildResults(self, False, self)
        else:
            return self.ReturnValues

    def ReadNonBlocking(self, Message=''):
        if self.TKrootDestroyed:
            return None, None
        if not self.Shown:
            self.Show(non_blocking=True)
        if Message:
            print(Message)
        try:
            rc = self.TKroot.update()
        except:
            self.TKrootDestroyed = True
            _my_windows.Decrement()
            # return None, None
        return BuildResults(self, False, self)

    def Refresh(self):
        if self.TKrootDestroyed:
            return
        try:
            rc = self.TKroot.update()
        except:
            pass


    def Fill(self, values_dict):
        FillFormWithValues(self, values_dict)


    def FindElement(self, key):
        return _FindElementFromKeyInSubForm(self, key)


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
        if self.TKrootDestroyed:
            return None, None
        screen_width = self.TKroot.winfo_screenwidth()  # get window info to move to middle of screen
        screen_height = self.TKroot.winfo_screenheight()
        return screen_width, screen_height


    def StartMove(self, event):
        try:
            self.TKroot.x = event.x
            self.TKroot.y = event.y
        except: pass

    def StopMove(self, event):
        try:
            self.TKroot.x = None
            self.TKroot.y = None
        except: pass

    def OnMotion(self, event):
        try:
            deltax = event.x - self.TKroot.x
            deltay = event.y - self.TKroot.y
            x = self.TKroot.winfo_x() + deltax
            y = self.TKroot.winfo_y() + deltay
            self.TKroot.geometry("+%s+%s" % (x, y))
        except:
            pass


    def _KeyboardCallback(self, event ):
        self.LastButtonClicked = None
        self.FormRemainedOpen = True
        if event.char != '':
            self.LastKeyboardEvent = event.char
        else:
            self.LastKeyboardEvent = str(event.keysym) + ':' + str(event.keycode)
        if not self.NonBlocking:
            BuildResults(self, False, self)
        self.TKroot.quit()

    def _MouseWheelCallback(self, event ):
        self.LastButtonClicked = None
        self.FormRemainedOpen = True
        self.LastKeyboardEvent = 'MouseWheel:Down' if event.delta < 0 else 'MouseWheel:Up'
        if not self.NonBlocking:
            BuildResults(self, False, self)
        self.TKroot.quit()


    def _Close(self):
        try:
            self.TKroot.update()
        except: pass
        if not self.NonBlocking:
            BuildResults(self, False, self)
        if self.TKrootDestroyed:
            return None
        self.TKrootDestroyed = True
        self.RootNeedsDestroying = True
        return None

    def CloseNonBlockingForm(self):
        if self.TKrootDestroyed:
            return
        try:
            self.TKroot.destroy()
            _my_windows.Decrement()
        except: pass

    def OnClosingCallback(self):
        return

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.__del__()
        return False

    def __del__(self):
        for row in self.Rows:
            for element in row:
                element.__del__()
        # try:
        #     del(self.TKroot)
        # except:
        #     pass

# ------------------------------------------------------------------------- #
#                       UberForm CLASS                                      #
#   Used to make forms into TABS (it's  trick)                              #
# ------------------------------------------------------------------------- #
class UberForm():
    FormList = None         # list of all the forms in this window
    FormReturnValues = None
    TKroot = None           # tk root for the overall window
    TKrootDestroyed = False
    def __init__(self):
        self.FormList = []
        self.FormReturnValues = []
        self.TKroot = None
        self.TKrootDestroyed = False

    def AddForm(self, form):
        self.FormList.append(form)

    def _Close(self):
        self.FormReturnValues = []
        for form in self.FormList:
            form._Close()
            self.FormReturnValues.append(form.ReturnValues)
        if not self.TKrootDestroyed:
            self.TKrootDestroyed = True
            self.TKroot.destroy()
            _my_windows.Decrement()

    def __del__(self):
        return

# ====================================================================== #
# BUTTON Lazy Functions                                                  #
# ====================================================================== #

# -------------------------  INPUT TEXT Element lazy functions  ------------------------- #
In = InputText
Input = InputText
####  TODO REMOVE THESE COMMENTS  - was the old way, but want to keep around for a bit just in case
# def In(default_text ='', scale=(None, None), size=(None, None), auto_size_text=None, password_char='', background_color=None, text_color=None, do_not_clear=False, key=None, focus=False):
#     return InputText(default_text=default_text, scale=scale, size=size, auto_size_text=auto_size_text, password_char=password_char, background_color=background_color, text_color=text_color, do_not_clear=do_not_clear, focus=focus, key=key)

# def Input(default_text ='', scale=(None, None), size=(None, None), auto_size_text=None, password_char='', background_color=None, text_color=None, do_not_clear=False, key=None, focus=False):
#     return InputText(default_text=default_text, scale=scale, size=size, auto_size_text=auto_size_text, password_char=password_char, background_color=background_color, text_color=text_color, do_not_clear=do_not_clear, focus=focus, key=key)

# -------------------------  CHECKBOX Element lazy functions  ------------------------- #
CB = Checkbox
CBox = Checkbox
Check = Checkbox

# -------------------------  INPUT COMBO Element lazy functions  ------------------------- #

Combo = InputCombo
DropDown = InputCombo
Drop = InputCombo


# -------------------------  OPTION MENU Element lazy functions  ------------------------- #

OptionMenu = InputOptionMenu



# def Combo(values, scale=(None, None), size=(None, None), auto_size_text=None, background_color=None):
#     return InputCombo(values=values, scale=scale, size=size, auto_size_text=auto_size_text, background_color=background_color)
#
# def DropDown(values, scale=(None, None), size=(None, None), auto_size_text=None):
#     return InputCombo(values=values, scale=scale, size=size, auto_size_text=auto_size_text)
#
# def Drop(values, scale=(None, None), size=(None, None), auto_size_text=None):
#     return InputCombo(values=values, scale=scale, size=size, auto_size_text=auto_size_text)
# -------------------------  TEXT Element lazy functions  ------------------------- #

Txt = Text
T = Text

# def Txt(display_text, scale=(None, None), size=(None, None), auto_size_text=None, font=None, text_color=None, justification=None):
#     return Text(display_text, scale=scale, size=size, auto_size_text=auto_size_text, font=font, text_color=text_color, justification=justification)
#
# def T(display_text, scale=(None, None), size=(None, None), auto_size_text=None, font=None, text_color=None, justification=None):
#     return Text(display_text, scale=scale, size=size, auto_size_text=auto_size_text, font=font, text_color=text_color, justification=justification)

# -------------------------  FOLDER BROWSE Element lazy function  ------------------------- #
def FolderBrowse(target=(ThisRow, -1), button_text='Browse', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, pad=None, key=None):
    return Button(BUTTON_TYPE_BROWSE_FOLDER, target=target, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, pad=pad, key=key)

# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileBrowse(target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), button_text='Browse', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, pad=None, key=None):
    return Button(BUTTON_TYPE_BROWSE_FILE, target, button_text=button_text, file_types=file_types, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, pad=pad, key=key)

# -------------------------  FILES BROWSE Element (Multiple file selection) lazy function  ------------------------- #
def FilesBrowse(target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), button_text='Browse', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, pad=None, key=None):
    return Button(BUTTON_TYPE_BROWSE_FILES, target, button_text=button_text, file_types=file_types, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, pad=pad, key=key)

# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileSaveAs(target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), button_text='Save As...', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, pad=None, key=None):
    return Button(BUTTON_TYPE_SAVEAS_FILE, target, button_text=button_text, file_types=file_types, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, pad=pad, key=key)

# -------------------------  SAVE AS Element lazy function  ------------------------- #
def SaveAs(target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), button_text='Save As...', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, pad=None, key=None):
    return Button(BUTTON_TYPE_SAVEAS_FILE, target, button_text=button_text, file_types=file_types, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, pad=pad, key=key)

# -------------------------  SAVE BUTTON Element lazy function  ------------------------- #
def Save(button_text='Save', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, bind_return_key=True,font=None, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color,font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  SUBMIT BUTTON Element lazy function  ------------------------- #
def Submit(button_text='Submit', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, bind_return_key=True,font=None, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color,font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  OPEN BUTTON Element lazy function  ------------------------- #
def Open(button_text='Open', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, bind_return_key=True,font=None, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color,font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  OK BUTTON Element lazy function  ------------------------- #
def OK(button_text='OK', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, bind_return_key=True, font=None,focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color,font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Ok(button_text='Ok', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, bind_return_key=True, font=None,focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  CANCEL BUTTON Element lazy function  ------------------------- #
def Cancel(button_text='Cancel', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  QUIT BUTTON Element lazy function  ------------------------- #
def Quit(button_text='Quit', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  Exit BUTTON Element lazy function  ------------------------- #
def Exit(button_text='Exit', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Yes(button_text='Yes', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None,font=None, bind_return_key=True, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  NO BUTTON Element lazy function  ------------------------- #
def No(button_text='No', scale=(None, None), size=(None, None), auto_size_button=None, button_color=None,font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
def SimpleButton(button_text, image_filename=None, image_size=(None, None), image_subsample=None, border_width=None, scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN, image_filename=image_filename, image_size=image_size, image_subsample=image_subsample, button_text=button_text, border_width=border_width, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)
# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
def ReadFormButton(button_text, image_filename=None, image_size=(None, None),image_subsample=None,border_width=None,scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_READ_FORM, image_filename=image_filename, image_size=image_size, image_subsample=image_subsample, border_width=border_width, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)
# -------------------------  Realtime BUTTON Element lazy function  ------------------------- #
def RealtimeButton(button_text, image_filename=None, image_size=(None, None),image_subsample=None,border_width=None,scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_REALTIME, image_filename=image_filename, image_size=image_size, image_subsample=image_subsample, border_width=border_width, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)
# -------------------------  Dummy BUTTON Element lazy function  ------------------------- #
def DummyButton(button_text, image_filename=None, image_size=(None, None),image_subsample=None,border_width=None,scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CLOSES_WIN_ONLY, image_filename=image_filename, image_size=image_size, image_subsample=image_subsample, border_width=border_width, button_text=button_text, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)
# -------------------------  Calendar Chooser Button lazy function  ------------------------- #
def CalendarButton(button_text, target=(None,None), image_filename=None, image_size=(None, None), image_subsample=None, border_width=None, scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_CALENDAR_CHOOSER, target=target, image_filename=image_filename, image_size=image_size, image_subsample=image_subsample, button_text=button_text, border_width=border_width, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)

# -------------------------  Calendar Chooser Button lazy function  ------------------------- #
def ColorChooserButton(button_text, target=(None,None), image_filename=None, image_size=(None, None), image_subsample=None, border_width=None, scale=(None, None), size=(None, None), auto_size_button=None, button_color=None, font=None, bind_return_key=False, focus=False, pad=None, key=None):
    return Button(BUTTON_TYPE_COLOR_CHOOSER, target=target, image_filename=image_filename, image_size=image_size, image_subsample=image_subsample, button_text=button_text, border_width=border_width, scale=scale, size=size, auto_size_button=auto_size_button, button_color=button_color, font=font, bind_return_key=bind_return_key, focus=focus, pad=pad, key=key)
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


#----------------------------------------------------------------------------#
# -------  FUNCTION InitializeResults.  Sets up form results matrix  --------#
def InitializeResults(form):
    BuildResults(form, True, form)
    return

#=====  Radio Button RadVar encoding and decoding =====#
#=====  The value is simply the row * 1000 + col  =====#
def DecodeRadioRowCol(RadValue):
    row = RadValue//1000
    col = RadValue%1000
    return row,col

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
    for row_num,row in enumerate(form.Rows):
        for col_num, element in enumerate(row):
            value = None
            if element.Type == ELEM_TYPE_COLUMN:
                element.DictionaryKeyCounter = top_level_form.DictionaryKeyCounter
                element.ReturnValuesList = []
                element.ReturnValuesDictionary = {}
                BuildResultsForSubform(element, initialize_only, top_level_form)
                for item in element.ReturnValuesList:
                    AddToReturnList(top_level_form, item)
                # for key in element.ReturnValuesDictionary:
                #     top_level_form.ReturnValuesDictionary[key] = element.ReturnValuesDictionary[key]
                # top_level_form.DictionaryKeyCounter += element.DictionaryKeyCounter
                if element.UseDictionary:
                    top_level_form.UseDictionary = True
                if element.ReturnValues[0] is not None:         # if a button was clicked
                    button_pressed_text = element.ReturnValues[0]

            if not initialize_only:
                if element.Type == ELEM_TYPE_INPUT_TEXT:
                    value=element.TKStringVar.get()
                    if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                        element.TKStringVar.set('')
                elif element.Type == ELEM_TYPE_INPUT_CHECKBOX:
                    value = element.TKIntVar.get()
                    value = (value != 0)
                elif element.Type == ELEM_TYPE_INPUT_RADIO:
                    RadVar=element.TKIntVar.get()
                    this_rowcol = EncodeRadioRowCol(row_num,col_num)
                    value = RadVar == this_rowcol
                elif element.Type == ELEM_TYPE_BUTTON:
                    if top_level_form.LastButtonClicked == element.ButtonText:
                        button_pressed_text = top_level_form.LastButtonClicked
                        if element.BType != BUTTON_TYPE_REALTIME:   # Do not clear realtime buttons
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
                    value=element.TKStringVar.get()
                elif element.Type == ELEM_TYPE_INPUT_OPTION_MENU:
                    value=element.TKStringVar.get()
                elif element.Type == ELEM_TYPE_INPUT_LISTBOX:
                    try:
                        items=element.TKListbox.curselection()
                        value = [element.Values[int(item)] for item in items]
                    except:
                        value = ''
                elif element.Type == ELEM_TYPE_INPUT_SPIN:
                    try:
                        value=element.TKStringVar.get()
                    except:
                        value = 0
                elif element.Type == ELEM_TYPE_INPUT_SLIDER:
                    try:
                        value=element.TKIntVar.get()
                    except:
                        value = 0
                elif element.Type == ELEM_TYPE_INPUT_MULTILINE:
                    try:
                        value=element.TKText.get(1.0, tk.END)
                        if not top_level_form.NonBlocking and not element.do_not_clear and not top_level_form.ReturnKeyboardEvents:
                            element.TKText.delete('1.0', tk.END)
                    except:
                        value = None
            else:
                value = None

            # if an input type element, update the results
            if element.Type != ELEM_TYPE_BUTTON and element.Type != ELEM_TYPE_TEXT and element.Type != ELEM_TYPE_IMAGE and\
                    element.Type != ELEM_TYPE_OUTPUT and element.Type != ELEM_TYPE_PROGRESS_BAR and \
                    element.Type!= ELEM_TYPE_COLUMN:
                AddToReturnList(form, value)
                AddToReturnDictionary(top_level_form, element, value)
            elif (element.Type == ELEM_TYPE_BUTTON and element.BType == BUTTON_TYPE_CALENDAR_CHOOSER and element.Target == (None,None)) or \
                    (element.Type == ELEM_TYPE_BUTTON and element.BType == BUTTON_TYPE_COLOR_CHOOSER and element.Target == (None,None)) or \
                (element.Type == ELEM_TYPE_BUTTON and element.Key is not None and (element.BType in (BUTTON_TYPE_SAVEAS_FILE, BUTTON_TYPE_BROWSE_FILE, BUTTON_TYPE_BROWSE_FILES, BUTTON_TYPE_BROWSE_FOLDER))):
                AddToReturnList(form, value)
                AddToReturnDictionary(top_level_form, element, value)

    # if this is a column, then will fail so need to wrap with tr
    try:
        if form.ReturnKeyboardEvents and form.LastKeyboardEvent is not None:
            button_pressed_text = form.LastKeyboardEvent
            form.LastKeyboardEvent = None
    except: pass

    try:
        form.ReturnValuesDictionary.pop(None, None)     # clean up dictionary include None was included
    except: pass

    if not form.UseDictionary:
        form.ReturnValues = button_pressed_text, form.ReturnValuesList
    else:
        form.ReturnValues = button_pressed_text, form.ReturnValuesDictionary

    return form.ReturnValues

def FillFormWithValues(form, values_dict):
    FillSubformWithValues(form, values_dict)

def FillSubformWithValues(form, values_dict):
    for row_num,row in enumerate(form.Rows):
        for col_num, element in enumerate(row):
            value = None
            if element.Type == ELEM_TYPE_COLUMN:
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
            if element.Key == key:
                return element


def AddMenuItem(top_menu, sub_menu_info, element, is_sub_menu=False, skip=False):
    if type(sub_menu_info) is str:
        if not is_sub_menu and not skip:
            # print(f'Adding command {sub_menu_info}')
            top_menu.add_command(label=sub_menu_info, command=lambda: Menu.MenuItemChosenCallback(element, sub_menu_info))
    else:
        i = 0
        while i < (len(sub_menu_info)):
            item = sub_menu_info[i]
            if i != len(sub_menu_info) - 1:
                if type(sub_menu_info[i+1]) == list:
                    new_menu = tk.Menu(top_menu)
                    top_menu.add_cascade(label=sub_menu_info[i], menu=new_menu)
                    AddMenuItem(new_menu, sub_menu_info[i+1], element, is_sub_menu=True)
                    i += 1  # skip the next one
                else:
                    AddMenuItem(top_menu, item, element)
            else:
                AddMenuItem(top_menu, item, element)
            i += 1

# ------------------------------------------------------------------------------------------------------------------ #
# =====================================   TK CODE STARTS HERE ====================================================== #
# ------------------------------------------------------------------------------------------------------------------ #

def PackFormIntoFrame(form, containing_frame, toplevel_form):
    def CharWidthInPixels():
        return tkinter.font.Font().measure('A')  # single character width
    # only set title on non-tabbed forms
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
        tk_row_frame = tk.Frame(containing_frame)
        for col_num, element in enumerate(flex_row):
            element.ParentForm = toplevel_form  # save the button's parent form object
            if toplevel_form.Font and (element.Font == DEFAULT_FONT or not element.Font):
                font = toplevel_form.Font
            elif element.Font is not None:
                font = element.Font
            else:
                font = DEFAULT_FONT
            # -------  Determine Auto-Size setting on a cascading basis ------- #
            if element.AutoSizeText is not None:            # if element overide
                auto_size_text = element.AutoSizeText
            elif toplevel_form.AutoSizeText is not None:       # if form override
                auto_size_text = toplevel_form.AutoSizeText
            else:
                auto_size_text = DEFAULT_AUTOSIZE_TEXT
            element_type = element.Type
            # Set foreground color
            text_color = element.TextColor
            # Determine Element size
            element_size = element.Size
            if (element_size == (None, None) and element_type != ELEM_TYPE_BUTTON):      # user did not specify a size
                element_size = toplevel_form.DefaultElementSize
            elif (element_size == (None, None) and element_type == ELEM_TYPE_BUTTON):
                element_size = toplevel_form.DefaultButtonElementSize
            else: auto_size_text = False                # if user has specified a size then it shouldn't autosize
            # Apply scaling... Element scaling is higher priority than form level
            if element.Scale != (None, None):
                element_size = (int(element_size[0] * element.Scale[0]), int(element_size[1] * element.Scale[1]))
            elif toplevel_form.Scale != (None, None):
                element_size = (int(element_size[0] * toplevel_form.Scale[0]), int(element_size[1] * toplevel_form.Scale[1]))
            # -------------------------  COLUMN element  ------------------------- #
            if element_type == ELEM_TYPE_COLUMN:
                if element.Scrollable:
                    col_frame = TkScrollableFrame(tk_row_frame)           # do not use yet!  not working
                    PackFormIntoFrame(element, col_frame.TKFrame, toplevel_form)
                    col_frame.TKFrame.update()
                    if element.Size == (None, None):            # if no size specified, use column width x column height/2
                        col_frame.canvas.config(width=col_frame.TKFrame.winfo_reqwidth(),height=col_frame.TKFrame.winfo_reqheight()/2)
                    else:
                        col_frame.canvas.config(width=element.Size[0],height=element.Size[1])

                    if not element.BackgroundColor in (None, COLOR_SYSTEM_DEFAULT):
                        col_frame.canvas.config(background=element.BackgroundColor)
                        col_frame.TKFrame.config(background=element.BackgroundColor, borderwidth =0, highlightthickness=0)
                        col_frame.config(background=element.BackgroundColor, borderwidth =0, highlightthickness=0)
                else:
                    col_frame = tk.Frame(tk_row_frame)
                    PackFormIntoFrame(element, col_frame, toplevel_form)

                col_frame.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                if element.BackgroundColor != COLOR_SYSTEM_DEFAULT and element.BackgroundColor is not None:
                    col_frame.configure(background=element.BackgroundColor, highlightbackground=element.BackgroundColor, highlightcolor=element.BackgroundColor)
            # -------------------------  TEXT element  ------------------------- #
            elif element_type == ELEM_TYPE_TEXT:
                display_text = element.DisplayText         # text to display
                if auto_size_text is False:
                    width, height=element_size
                else:
                    lines = display_text.split('\n')
                    max_line_len = max([len(l) for l in lines])
                    num_lines = len(lines)
                    if max_line_len > element_size[0]:       # if text exceeds element size, the will have to wrap
                        width = element_size[0]
                    else:
                        width=max_line_len
                    height=num_lines
                # ---===--- LABEL widget create and place --- #
                stringvar = tk.StringVar()
                element.TKStringVar = stringvar
                stringvar.set(display_text)
                if auto_size_text:
                    width = 0
                if element.Justification is not None:
                    justification = element.Justification
                elif toplevel_form.TextJustification is not None:
                    justification = toplevel_form.TextJustification
                else:
                    justification = DEFAULT_TEXT_JUSTIFICATION
                justify = tk.LEFT if justification == 'left' else tk.CENTER if justification == 'center' else tk.RIGHT
                anchor = tk.NW if justification == 'left' else tk.N if justification == 'center' else tk.NE
                tktext_label = tk.Label(tk_row_frame, textvariable=stringvar, width=width, height=height, justify=justify, bd=border_depth, font=font)
                # Set wrap-length for text (in PIXELS) == PAIN IN THE ASS
                wraplen = tktext_label.winfo_reqwidth()+40  # width of widget in Pixels
                if not auto_size_text:
                    wraplen = 0
                # print("wraplen, width, height", wraplen, width, height)
                tktext_label.configure(anchor=anchor, wraplen=wraplen)  # set wrap to width of widget
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    tktext_label.configure(background=element.BackgroundColor)
                if element.TextColor != COLOR_SYSTEM_DEFAULT and element.TextColor is not None:
                    tktext_label.configure(fg=element.TextColor)
                tktext_label.pack(side=tk.LEFT,padx=element.Pad[0], pady=element.Pad[1])
                element.TKText = tktext_label
            # -------------------------  BUTTON element  ------------------------- #
            elif element_type == ELEM_TYPE_BUTTON:
                stringvar = tk.StringVar()
                element.TKStringVar = stringvar
                element.Location = (row_num, col_num)
                btext = element.ButtonText
                btype = element.BType
                if element.AutoSizeButton is not None:
                    auto_size = element.AutoSizeButton
                else: auto_size = toplevel_form.AutoSizeButtons
                if auto_size is False or element.Size[0] is not None:
                    width, height = element_size
                else:
                    width = 0
                    height= toplevel_form.DefaultButtonElementSize[1]
                if element.ButtonColor != (None, None)and element.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = element.ButtonColor
                elif toplevel_form.ButtonColor != (None, None) and toplevel_form.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = toplevel_form.ButtonColor
                else:
                    bc = DEFAULT_BUTTON_COLOR
                border_depth = element.BorderWidth
                if btype != BUTTON_TYPE_REALTIME:
                    tkbutton = tk.Button(tk_row_frame, text=btext, width=width, height=height,command=element.ButtonCallBack, justify=tk.LEFT, bd=border_depth, font=font)
                else:
                    tkbutton = tk.Button(tk_row_frame, text=btext, width=width, height=height, justify=tk.LEFT, bd=border_depth, font=font)
                    tkbutton.bind('<ButtonRelease-1>', element.ButtonReleaseCallBack)
                    tkbutton.bind('<ButtonPress-1>', element.ButtonPressCallBack)
                if bc != (None, None) and bc != COLOR_SYSTEM_DEFAULT:
                    tkbutton.config(foreground=bc[0], background=bc[1])
                element.TKButton = tkbutton          # not used yet but save the TK button in case
                wraplen = tkbutton.winfo_reqwidth()  # width of widget in Pixels
                if element.ImageFilename:           # if button has an image on it
                    tkbutton.config(highlightthickness=0)
                    photo = tk.PhotoImage(file=element.ImageFilename)
                    if element.ImageSize != (None, None):
                        width, height = element.ImageSize
                        if element.ImageSubsample:
                            photo = photo.subsample(element.ImageSubsample)
                    else:
                        width, height = photo.width(), photo.height()
                    tkbutton.config(image=photo, width=width, height=height)
                    tkbutton.image = photo
                if width != 0:
                    tkbutton.configure(wraplength=wraplen+10)  # set wrap to width of widget
                tkbutton.pack(side=tk.LEFT,  padx=element.Pad[0], pady=element.Pad[1])
                if element.BindReturnKey:
                    element.TKButton.bind('<Return>', element.ReturnKeyHandler)
                if element.Focus is True or (toplevel_form.UseDefaultFocus and not focus_set):
                    focus_set = True
                    element.TKButton.bind('<Return>', element.ReturnKeyHandler)
                    element.TKButton.focus_set()
                    toplevel_form.TKroot.focus_force()
            # -------------------------  INPUT (Single Line) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_TEXT:
                default_text = element.DefaultText
                element.TKStringVar = tk.StringVar()
                element.TKStringVar.set(default_text)
                show = element.PasswordCharacter if element.PasswordCharacter else ""
                if element.Justification is not None:
                    justification = element.Justification
                else:
                    justification = DEFAULT_TEXT_JUSTIFICATION
                justify = tk.LEFT if justification == 'left' else tk.CENTER if justification == 'center' else tk.RIGHT
                anchor = tk.NW if justification == 'left' else tk.N if justification == 'center' else tk.NE
                element.TKEntry = tk.Entry(tk_row_frame, width=element_size[0], textvariable=element.TKStringVar, bd=border_depth, font=font, show=show, justify=justify)
                element.TKEntry.bind('<Return>', element.ReturnKeyHandler)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKEntry.configure(background=element.BackgroundColor)
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKEntry.configure(fg=text_color)
                element.TKEntry.pack(side=tk.LEFT,padx=element.Pad[0], pady=element.Pad[1])
                if element.Focus is True or (toplevel_form.UseDefaultFocus and not focus_set):
                    focus_set = True
                    element.TKEntry.focus_set()
            # -------------------------  COMBO BOX (Drop Down) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_COMBO:
                max_line_len = max([len(str(l)) for l in element.Values])
                if auto_size_text is False: width=element_size[0]
                else: width = max_line_len
                element.TKStringVar = tk.StringVar()
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    combostyle = ttk.Style()
                    try:
                        combostyle.theme_create('combostyle',
                                                settings={'TCombobox':
                                                              {'configure':
                                                                   {'selectbackground': element.BackgroundColor,
                                                                    'fieldbackground':  element.BackgroundColor,
                                                                    'foreground': text_color,
                                                                    'background':  element.BackgroundColor}
                                                               }})
                    except:
                        try:
                            combostyle.theme_settings('combostyle',
                                                settings={'TCombobox':
                                                              {'configure':
                                                                   {'selectbackground': element.BackgroundColor,
                                                                    'fieldbackground':  element.BackgroundColor,
                                                                    'foreground': text_color,
                                                                    'background':  element.BackgroundColor}
                                                               }})
                        except: pass
                    # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
                    combostyle.theme_use('combostyle')
                element.TKCombo = ttk.Combobox(tk_row_frame, width=width, textvariable=element.TKStringVar,font=font )
                if element.Size[1] != 1 and element.Size[1] is not None:
                    element.TKCombo.configure(height=element.Size[1])
                # element.TKCombo['state']='readonly'
                element.TKCombo['values'] = element.Values
                if element.InitializeAsDisabled:
                    element.TKCombo['state'] = 'disabled'
                # if element.BackgroundColor is not None:
                #     element.TKCombo.configure(background=element.BackgroundColor)
                element.TKCombo.pack(side=tk.LEFT,padx=element.Pad[0], pady=element.Pad[1])
                if element.DefaultValue:
                    for i, v in enumerate(element.Values):
                        if v == element.DefaultValue:
                            element.TKCombo.current(i)
                            break
                else:
                    element.TKCombo.current(0)
                if element.ChangeSubmits:
                    element.TKCombo.bind('<<ComboboxSelected>>', element.ComboboxSelectHandler)
            # -------------------------  OPTION MENU (Like ComboBox but different) element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_OPTION_MENU:
                max_line_len = max([len(str(l)) for l in element.Values])
                if auto_size_text is False: width=element_size[0]
                else: width = max_line_len
                element.TKStringVar = tk.StringVar()
                default = element.DefaultValue if element.DefaultValue else element.Values[0]
                element.TKStringVar.set(default)
                element.TKOptionMenu = tk.OptionMenu(tk_row_frame, element.TKStringVar ,*element.Values)
                element.TKOptionMenu.config(highlightthickness=0, font=font, width=width )
                element.TKOptionMenu.config(borderwidth=border_depth)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKOptionMenu.configure(background=element.BackgroundColor)
                if element.TextColor != COLOR_SYSTEM_DEFAULT and element.TextColor is not None:
                    element.TKOptionMenu.configure(fg=element.TextColor)
                element.TKOptionMenu.pack(side=tk.LEFT,padx=element.Pad[0], pady=element.Pad[1])
            # -------------------------  LISTBOX element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_LISTBOX:
                max_line_len = max([len(str(l)) for l in element.Values])
                if auto_size_text is False: width=element_size[0]
                else: width = max_line_len
                listbox_frame = tk.Frame(tk_row_frame)
                element.TKStringVar = tk.StringVar()
                element.TKListbox= tk.Listbox(listbox_frame, height=element_size[1], width=width, selectmode=element.SelectMode, font=font)
                for index, item in enumerate(element.Values):
                    element.TKListbox.insert(tk.END, item)
                    if element.DefaultValues is not None and item in element.DefaultValues:
                        element.TKListbox.selection_set(index)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKListbox.configure(background=element.BackgroundColor)
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKListbox.configure(fg=text_color)
                if element.ChangeSubmits:
                    element.TKListbox.bind('<<ListboxSelect>>', element.ListboxSelectHandler)
                vsb = tk.Scrollbar(listbox_frame, orient="vertical", command=element.TKListbox.yview)
                element.TKListbox.configure(yscrollcommand=vsb.set)
                element.TKListbox.pack(side=tk.LEFT)
                vsb.pack(side=tk.LEFT, fill='y')
                listbox_frame.pack(side=tk.LEFT,padx=element.Pad[0], pady=element.Pad[1])
                element.TKListbox.bind('<Return>', element.ReturnKeyHandler)
            # -------------------------  INPUT MULTI LINE element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_MULTILINE:
                default_text = element.DefaultText
                width, height = element_size
                element.TKText = tk.scrolledtext.ScrolledText(tk_row_frame, width=width, height=height, wrap='word', bd=border_depth,font=font)
                element.TKText.insert(1.0, default_text)                    # set the default text
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKText.configure(background=element.BackgroundColor)
                    element.TKText.vbar.config(troughcolor=DEFAULT_SCROLLBAR_COLOR)
                element.TKText.pack(side=tk.LEFT,padx=element.Pad[0], pady=element.Pad[1])
                if element.EnterSubmits:
                    element.TKText.bind('<Return>', element.ReturnKeyHandler)
                if element.Focus is True or (toplevel_form.UseDefaultFocus and not focus_set):
                    focus_set = True
                    element.TKText.focus_set()
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKText.configure(fg=text_color)
            # -------------------------  INPUT CHECKBOX element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_CHECKBOX:
                width = 0 if auto_size_text else element_size[0]
                default_value = element.InitialState
                element.TKIntVar = tk.IntVar()
                element.TKIntVar.set(default_value if default_value is not None else 0)
                element.TKCheckbutton = tk.Checkbutton(tk_row_frame, anchor=tk.NW, text=element.Text, width=width, variable=element.TKIntVar, bd=border_depth, font=font)
                if default_value is None:
                    element.TKCheckbutton.configure(state='disable')
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKCheckbutton.configure(background=element.BackgroundColor)
                    element.TKCheckbutton.configure(selectcolor=element.BackgroundColor)
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKCheckbutton.configure(fg=text_color)
                element.TKCheckbutton.pack(side=tk.LEFT,padx=element.Pad[0], pady=element.Pad[1])
            # -------------------------  PROGRESS BAR element  ------------------------- #
            elif element_type == ELEM_TYPE_PROGRESS_BAR:
                # save this form because it must be 'updated' (refreshed) solely for the purpose of updating bar
                width = element_size[0]
                fnt = tkinter.font.Font()
                char_width = fnt.measure('A')       # single character width
                progress_length = width*char_width
                progress_width = element_size[1]
                direction = element.Orientation
                if element.BarColor != (None, None):    # if element has a bar color, use it
                    bar_color = element.BarColor
                else:
                    bar_color = DEFAULT_PROGRESS_BAR_COLOR
                element.TKProgressBar = TKProgressBar(tk_row_frame, element.MaxValue, progress_length, progress_width, orientation=direction, BarColor=bar_color, border_width=element.BorderWidth, relief=element.Relief, style=element.BarStyle )
                element.TKProgressBar.TKProgressBarForReal.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # -------------------------  INPUT RADIO BUTTON element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_RADIO:
                width = 0 if auto_size_text else element_size[0]
                default_value = element.InitialState
                ID = element.GroupID
                # see if ID has already been placed
                value = EncodeRadioRowCol(row_num, col_num)     # value to set intvar to if this radio is selected
                if ID in toplevel_form.RadioDict:
                    RadVar = toplevel_form.RadioDict[ID]
                else:
                    RadVar = tk.IntVar()
                    toplevel_form.RadioDict[ID] = RadVar
                element.TKIntVar = RadVar                       # store the RadVar in Radio object
                if default_value:                               # if this radio is the one selected, set RadVar to match
                    element.TKIntVar.set(value)
                element.TKRadio = tk.Radiobutton(tk_row_frame, anchor=tk.NW, text=element.Text, width=width,
                                                       variable=element.TKIntVar, value=value, bd=border_depth, font=font)
                if not element.BackgroundColor in (None, COLOR_SYSTEM_DEFAULT):
                    element.TKRadio.configure(background=element.BackgroundColor)
                    element.TKRadio.configure(selectcolor=element.BackgroundColor)
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKRadio.configure(fg=text_color)
                element.TKRadio.pack(side=tk.LEFT, padx=element.Pad[0],pady=element.Pad[1])
                # -------------------------  INPUT SPIN Box element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SPIN:
                width, height = element_size
                width = 0 if auto_size_text else element_size[0]
                element.TKStringVar = tk.StringVar()
                element.TKSpinBox = tk.Spinbox(tk_row_frame, values=element.Values, textvariable=element.TKStringVar, width=width, bd=border_depth)
                element.TKStringVar.set(element.DefaultValue)
                element.TKSpinBox.configure(font=font)  # set wrap to width of widget
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKSpinBox.configure(background=element.BackgroundColor)
                element.TKSpinBox.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    element.TKSpinBox.configure(fg=text_color)
                if element.ChangeSubmits:
                    element.TKSpinBox.bind('<ButtonRelease-1>', element.SpinChangedHandler)
                # -------------------------  OUTPUT element  ------------------------- #
            elif element_type == ELEM_TYPE_OUTPUT:
                width, height = element_size
                element.TKOut = TKOutput(tk_row_frame, width=width, height=height, bd=border_depth, background_color=element.BackgroundColor, text_color=text_color, font=font, pad=element.Pad)
                element.TKOut.pack(side=tk.LEFT)
                # -------------------------  IMAGE Box element  ------------------------- #
            elif element_type == ELEM_TYPE_IMAGE:
                if element.Filename is not None:
                    photo = tk.PhotoImage(file=element.Filename)
                elif element.Data is not None:
                    photo = tk.PhotoImage(data=element.Data)
                else:
                    photo = None
                    print('*ERROR laying out form.... Image Element has no image specified*')

                if photo is not None:
                    if element_size == (None, None) or element_size == None or element_size == toplevel_form.DefaultElementSize:
                        width, height = photo.width(), photo.height()
                    else:
                        width, height = element_size
                    if photo is not None:
                        element.tktext_label = tk.Label(tk_row_frame, image=photo, width=width, height=height, bd=border_depth)
                    else:
                        element.tktext_label = tk.Label(tk_row_frame, width=width, height=height, bd=border_depth)
                    element.tktext_label.image = photo
                    # tktext_label.configure(anchor=tk.NW, image=photo)
                    element.tktext_label.pack(side=tk.LEFT, padx=element.Pad[0],pady=element.Pad[1])
                # -------------------------  Canvas element  ------------------------- #
            elif element_type == ELEM_TYPE_CANVAS:
                width, height = element_size
                if element.TKCanvas is None:
                    element.TKCanvas = tk.Canvas(tk_row_frame, width=width, height=height, bd=border_depth)
                else:
                    element.TKCanvas.master = tk_row_frame
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKCanvas.configure(background=element.BackgroundColor)
                element.TKCanvas.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
            # -------------------------  MENUBAR element  ------------------------- #
            elif element_type == ELEM_TYPE_MENUBAR:
                menu_def = (('File', ('Open', 'Save')),
                            ('Help', 'About...'),)
                            # ('Help',))

                menu_def = element.MenuDefinition

                element.TKMenu = tk.Menu(toplevel_form.TKroot, tearoff=0)    # create the menubar
                menubar = element.TKMenu
                for menu_entry in menu_def:
                    # print(f'Adding a Menubar ENTRY')
                    baritem = tk.Menu(menubar)
                    menubar.add_cascade(label=menu_entry[0], menu=baritem)
                    if len(menu_entry) > 1:
                        AddMenuItem(baritem, menu_entry[1], element)

                toplevel_form.TKroot.configure(menu=element.TKMenu)
            # -------------------------  Frame element  ------------------------- #
            elif element_type == ELEM_TYPE_FRAME:
                width, height = element_size
                if element.TKFrame is None:
                    element.TKFrame = tk.Frame(tk_row_frame, width=width, height=height, bd=border_depth)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    element.TKFrame.configure(background=element.BackgroundColor)
                element.TKFrame.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # -------------------------  SLIDER Box element  ------------------------- #
            elif element_type == ELEM_TYPE_INPUT_SLIDER:
                slider_length = element_size[0] * CharWidthInPixels()
                slider_width = element_size[1]
                element.TKIntVar = tk.IntVar()
                element.TKIntVar.set(element.DefaultValue)
                if element.Orientation[0] == 'v':
                    range_from = element.Range[1]
                    range_to = element.Range[0]
                    slider_length += DEFAULT_MARGINS[1]*(element_size[0]*2)     # add in the padding
                else:
                    range_from = element.Range[0]
                    range_to = element.Range[1]
                if element.ChangeSubmits:
                    tkscale = tk.Scale(tk_row_frame, orient=element.Orientation, variable=element.TKIntVar, from_=range_from, to_=range_to, resolution = element.Resolution, length=slider_length, width=slider_width , bd=element.BorderWidth, relief=element.Relief, font=font, command=element.SliderChangedHandler)
                else:
                    tkscale = tk.Scale(tk_row_frame, orient=element.Orientation, variable=element.TKIntVar, from_=range_from, to_=range_to, resolution = element.Resolution, length=slider_length, width=slider_width , bd=element.BorderWidth, relief=element.Relief, font=font)
                tkscale.config(highlightthickness=0)
                if element.BackgroundColor is not None and element.BackgroundColor != COLOR_SYSTEM_DEFAULT:
                    tkscale.configure(background=element.BackgroundColor)
                    if DEFAULT_SCROLLBAR_COLOR != COLOR_SYSTEM_DEFAULT:
                        tkscale.config(troughcolor=DEFAULT_SCROLLBAR_COLOR)
                if text_color is not None and text_color != COLOR_SYSTEM_DEFAULT:
                    tkscale.configure(fg=text_color)
                tkscale.pack(side=tk.LEFT, padx=element.Pad[0],pady=element.Pad[1])
                element.TKScale = tkscale
        #............................DONE WITH ROW pack the row of widgets ..........................#
        # done with row, pack the row of widgets
        # tk_row_frame.grid(row=row_num+2, sticky=tk.NW, padx=DEFAULT_MARGINS[0])
        tk_row_frame.pack(side=tk.TOP, anchor='sw', padx=DEFAULT_MARGINS[0])

        if form.BackgroundColor is not None and form.BackgroundColor != COLOR_SYSTEM_DEFAULT:
            tk_row_frame.configure(background=form.BackgroundColor)
        if not toplevel_form.IsTabbedForm:
            toplevel_form.TKroot.configure(padx=DEFAULT_MARGINS[0], pady=DEFAULT_MARGINS[1])
        else: toplevel_form.ParentWindow.configure(padx=DEFAULT_MARGINS[0], pady=DEFAULT_MARGINS[1])
    return


def ConvertFlexToTK(MyFlexForm):
    master = MyFlexForm.TKroot
    # only set title on non-tabbed forms
    if not MyFlexForm.IsTabbedForm:
        master.title(MyFlexForm.Title)
    InitializeResults(MyFlexForm)
    try:
        if MyFlexForm.NoTitleBar:
            MyFlexForm.TKroot.wm_overrideredirect(True)
    except:
        pass
    PackFormIntoFrame(MyFlexForm, master, MyFlexForm)
    #....................................... DONE creating and laying out window ..........................#
    if MyFlexForm.IsTabbedForm:
        master = MyFlexForm.ParentWindow
    screen_width = master.winfo_screenwidth()      # get window info to move to middle of screen
    screen_height = master.winfo_screenheight()
    if MyFlexForm.Location != (None, None):
        x,y = MyFlexForm.Location
    elif DEFAULT_WINDOW_LOCATION != (None, None):
        x,y = DEFAULT_WINDOW_LOCATION
    else:
        master.update_idletasks()                   # don't forget to do updates or values are bad
        win_width = master.winfo_width()
        win_height = master.winfo_height()
        x = screen_width/2 -win_width/2
        y = screen_height/2 - win_height/2
        if y+win_height > screen_height:
            y = screen_height-win_height
        if x+win_width > screen_width:
            x = screen_width-win_width

    move_string = '+%i+%i'%(int(x),int(y))
    master.geometry(move_string)
    master.update_idletasks()  # don't forget
    return


# ----====----====----====----====----==== STARTUP TK ====----====----====----====----====----#
def ShowTabbedForm(title, *args, auto_close=False, auto_close_duration=DEFAULT_AUTOCLOSE_TIME, fav_icon=DEFAULT_WINDOW_ICON, no_titlebar=False):
    # takes as input (form, rows, tab name) for each tab
    global _my_windows

    uber = UberForm()
    root = tk.Tk()
    uber.TKroot = root
    if title is not None:
        root.title(title)
    try:
        root.attributes('-alpha', 0)             # hide window while building it. makes for smoother 'paint'
    except:
        pass

    if not len(args):
        print('******************* SHOW TABBED FORMS ERROR .... no arguments')
        return
    if DEFAULT_BACKGROUND_COLOR:
        framestyle = ttk.Style()
        try:
            framestyle.theme_create('framestyle', parent='alt',
                                settings={'TFrame':
                                              {'configure':
                                                   {'background': DEFAULT_BACKGROUND_COLOR,
                                                    }}})
        except: pass
        # ATTENTION: this applies the new style 'combostyle' to all ttk.Combobox
        # framestyle.theme_use('framestyle')
    tab_control = ttk.Notebook(root)

    for num,x in enumerate(args):
        form, rows, tab_name = x
        form.AddRows(rows)

        if DEFAULT_BACKGROUND_COLOR:
            framestyle.theme_use('framestyle')
        tab = ttk.Frame(tab_control)  # Create tab 1
        # s.configure("my.Frame.TFrame", background=DEFAULT_BACKGROUND_COLOR)
        tab_control.add(tab, text=tab_name)  # Add tab 1
        # tab_control.configure(text='new text')
        tab_control.grid(row=0, sticky=tk.W)
        form.TKTabControl = tab_control
        form.TKroot = tab
        form.IsTabbedForm = True
        form.ParentWindow = root
        ConvertFlexToTK(form)
        form.UberParent = uber
        uber.AddForm(form)
        uber.FormReturnValues.append(form.ReturnValues)

    # dangerous??  or clever? use the final form as a callback for autoclose
    id = root.after(auto_close_duration * 1000, form._AutoCloseAlarmCallback) if auto_close else 0
    icon = fav_icon if not _my_windows.user_defined_icon else _my_windows.user_defined_icon
    try: uber.TKroot.iconbitmap(icon)
    except: pass
    try:
        if no_titlebar:
            uber.TKroot.wm_overrideredirect(True)
    except:
        pass

    try:
        root.attributes('-alpha', 255)             # hide window while building it. makes for smoother 'paint'
    except:
        pass
    root.mainloop()

    if id: root.after_cancel(id)
    uber.TKrootDestroyed = True
    return uber.FormReturnValues

# ----====----====----====----====----==== STARTUP TK ====----====----====----====----====----#
def StartupTK(my_flex_form):
    global _my_windows

    ow = _my_windows.NumOpenWindows
    # print('Starting TK open Windows = {}'.format(ow))
    root = tk.Tk() if not ow else tk.Toplevel()
    try:
        root.attributes('-alpha', 0)             # hide window while building it. makes for smoother 'paint'
    except:
        pass
    # root.wm_overrideredirect(True)
    if my_flex_form.BackgroundColor is not None and my_flex_form.BackgroundColor != COLOR_SYSTEM_DEFAULT:
        root.configure(background=my_flex_form.BackgroundColor)
    _my_windows.Increment()

    my_flex_form.TKroot = root
    # Make moveable window
    if (my_flex_form.GrabAnywhere is not False and not (my_flex_form.NonBlocking and my_flex_form.GrabAnywhere is not True)):
        root.bind("<ButtonPress-1>", my_flex_form.StartMove)
        root.bind("<ButtonRelease-1>", my_flex_form.StopMove)
        root.bind("<B1-Motion>", my_flex_form.OnMotion)

    if my_flex_form.KeepOnTop:
        root.wm_attributes("-topmost", 1)

    # root.protocol("WM_DELETE_WINDOW", MyFlexForm.DestroyedCallback())
    # root.bind('<Destroy>', MyFlexForm.DestroyedCallback())
    ConvertFlexToTK(my_flex_form)
    my_flex_form.SetIcon(my_flex_form.WindowIcon)

    try:
        root.attributes('-alpha', 255)             # hide window while building it. makes for smoother 'paint'
    except:
        pass

    if my_flex_form.ReturnKeyboardEvents and not my_flex_form.NonBlocking:
        root.bind("<KeyRelease>", my_flex_form._KeyboardCallback)
        root.bind("<MouseWheel>", my_flex_form._MouseWheelCallback)
    elif my_flex_form.ReturnKeyboardEvents:
        root.bind("<Key>", my_flex_form._KeyboardCallback)
        root.bind("<MouseWheel>", my_flex_form._MouseWheelCallback)

    if my_flex_form.AutoClose:
        duration = DEFAULT_AUTOCLOSE_TIME if my_flex_form.AutoCloseDuration is None else my_flex_form.AutoCloseDuration
        my_flex_form.TKAfterID = root.after(duration * 1000, my_flex_form._AutoCloseAlarmCallback)
    if my_flex_form.NonBlocking:
        my_flex_form.TKroot.protocol("WM_WINDOW_DESTROYED", my_flex_form.OnClosingCallback())
    else:       # it's a blocking form
        # print('..... CALLING MainLoop')
        my_flex_form.TKroot.mainloop()
        # print('..... BACK from MainLoop')
        if not my_flex_form.FormRemainedOpen:
            _my_windows.Decrement()
        if my_flex_form.RootNeedsDestroying:
            my_flex_form.TKroot.destroy()
            my_flex_form.RootNeedsDestroying = False
    return

# ==============================_GetNumLinesNeeded ==#
# Helper function for determining how to wrap text   #
# ===================================================#
def _GetNumLinesNeeded(text, max_line_width):
    if max_line_width == 0:
        return 1
    lines = text.split('\n')
    num_lines = len(lines)                          # number of original lines of text
    max_line_len = max([len(l) for l in lines])     # longest line
    lines_used = []
    for L in lines:
        lines_used.append(len(L)//max_line_width + (len(L) % max_line_width > 0))       # fancy math to round up
    total_lines_needed = sum(lines_used)
    return total_lines_needed

# ==============================  PROGRESS METER ========================================== #

def ConvertArgsToSingleString(*args):
    max_line_total, width_used , total_lines, = 0,0,0
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
def _ProgressMeter(title, max_value, *args, orientation=None, bar_color=(None,None), button_color=None, size=DEFAULT_PROGRESS_BAR_SIZE, scale=(None, None), border_width=None):
    '''
    Create and show a form on tbe caller's behalf.
    :param title:
    :param max_value:
    :param args: ANY number of arguments the caller wants to display
    :param orientation:
    :param bar_color:
    :param size:
    :param scale:
    :param Style:
    :param StyleOffset:
    :return: ProgressBar object that is in the form
    '''
    local_orientation = DEFAULT_METER_ORIENTATION if orientation is None else orientation
    local_border_width = DEFAULT_PROGRESS_BAR_BORDER_WIDTH if border_width is None else border_width
    bar2 = ProgressBar(max_value, orientation=local_orientation, size=size, bar_color=bar_color, scale=scale, border_width=local_border_width, relief=DEFAULT_PROGRESS_BAR_RELIEF)
    form = FlexForm(title, auto_size_text=True)

    # Form using a horizontal bar
    if local_orientation[0].lower() == 'h':
        single_line_message, width, height = ConvertArgsToSingleString(*args)
        bar2.TextToDisplay = single_line_message
        bar2.MaxValue = max_value
        bar2.CurrentValue = 0
        bar_text = Text(single_line_message, size=(width, height + 3), auto_size_text=True)
        form.AddRow(bar_text)
        form.AddRow((bar2))
        form.AddRow((Cancel(button_color=button_color)))
    else:
        single_line_message, width, height = ConvertArgsToSingleString(*args)
        bar2.TextToDisplay = single_line_message
        bar2.MaxValue = max_value
        bar2.CurrentValue = 0
        bar_text = Text(single_line_message, size=(width, height + 3), auto_size_text=True)
        form.AddRow(bar2, bar_text)
        form.AddRow((Cancel(button_color=button_color)))

    form.NonBlocking = True
    form.Show(non_blocking= True)
    return bar2, bar_text

# ============================== ProgressMeterUpdate  =====#
def _ProgressMeterUpdate(bar, value, text_elem, *args):
    '''
    Update the progress meter for a form
    :param form: class ProgressBar
    :param value: int
    :return: True if not cancelled, OK....False if Error
    '''
    global  _my_windows
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
    if bar.ParentForm.RootNeedsDestroying:
        try:
            bar.ParentForm.TKroot.destroy()
            _my_windows.Decrement()
        except: pass
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
            '{} %'.format(100*self.CurrentValue//self.MaxValue),
            '',
            ' {:6.2f} Iterations per Second'.format(self.CurrentValue/total_seconds),
            ' {:6.2f} Seconds per Iteration'.format(total_seconds/(self.CurrentValue if self.CurrentValue else 1)),
            '',
            '{} Elapsed Time'.format(time_delta_short),
            '{} Time Remaining'.format(time_remaining_short),
            '{} Estimated Total Time'.format(total_time_short)]
        return


# ============================== EasyProgressMeter  =====#
def EasyProgressMeter(title, current_value, max_value, *args, orientation=None, bar_color=(None,None), button_color=None, size=DEFAULT_PROGRESS_BAR_SIZE, scale=(None, None), border_width=None):
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
    :param scale:
    :param Style:
    :param StyleOffset:
    :return: False if should stop the meter
    '''
    local_border_width = DEFAULT_PROGRESS_BAR_BORDER_WIDTH if not border_width else border_width
    # STATIC VARIABLE!
    # This is a very clever form of static variable using a function attribute
    # If the variable doesn't yet exist, then it will create it and initialize with the 3rd parameter
    EasyProgressMeter.EasyProgressMeterData = getattr(EasyProgressMeter, 'EasyProgressMeterData', EasyProgressMeterDataClass())
    # if no meter currently running
    if EasyProgressMeter.EasyProgressMeterData.MeterID is None:           # Starting a new meter
        if int(current_value) >= int(max_value):
            return False
        del(EasyProgressMeter.EasyProgressMeterData)
        EasyProgressMeter.EasyProgressMeterData = EasyProgressMeterDataClass(title, 1, int(max_value), datetime.datetime.utcnow(), [])
        EasyProgressMeter.EasyProgressMeterData.ComputeProgressStats()
        message = "\n".join([line for line in EasyProgressMeter.EasyProgressMeterData.StatMessages])
        EasyProgressMeter.EasyProgressMeterData.MeterID, EasyProgressMeter.EasyProgressMeterData.MeterText= _ProgressMeter(title, int(max_value), message, *args, orientation=orientation, bar_color=bar_color, size=size, scale=scale, button_color=button_color, border_width=local_border_width)
        EasyProgressMeter.EasyProgressMeterData.ParentForm = EasyProgressMeter.EasyProgressMeterData.MeterID.ParentForm
        return True
    # if exactly the same values as before, then ignore.
    if EasyProgressMeter.EasyProgressMeterData.MaxValue == max_value and EasyProgressMeter.EasyProgressMeterData.CurrentValue == current_value:
        return True
    if EasyProgressMeter.EasyProgressMeterData.MaxValue != int(max_value):
        EasyProgressMeter.EasyProgressMeterData.MeterID = None
        EasyProgressMeter.EasyProgressMeterData.ParentForm = None
        del(EasyProgressMeter.EasyProgressMeterData)
        EasyProgressMeter.EasyProgressMeterData = EasyProgressMeterDataClass()            # setup a new progress meter
        return True         # HAVE to return TRUE or else the new meter will thing IT is failing when it hasn't
    EasyProgressMeter.EasyProgressMeterData.CurrentValue = int(current_value)
    EasyProgressMeter.EasyProgressMeterData.MaxValue = int(max_value)
    EasyProgressMeter.EasyProgressMeterData.ComputeProgressStats()
    message = ''
    for line in EasyProgressMeter.EasyProgressMeterData.StatMessages:
        message = message + str(line) + '\n'
    message = "\n".join(EasyProgressMeter.EasyProgressMeterData.StatMessages)
    args= args + (message,)
    rc = _ProgressMeterUpdate(EasyProgressMeter.EasyProgressMeterData.MeterID, current_value,
                              EasyProgressMeter.EasyProgressMeterData.MeterText, *args)
    # if counter >= max then the progress meter is all done. Indicate none running
    if current_value >= EasyProgressMeter.EasyProgressMeterData.MaxValue or not rc:
        EasyProgressMeter.EasyProgressMeterData.MeterID = None
        del(EasyProgressMeter.EasyProgressMeterData)
        EasyProgressMeter.EasyProgressMeterData = EasyProgressMeterDataClass()            # setup a new progress meter
        return False     # even though at the end, return True so don't cause error with the app
    return rc           # return whatever the update told us


def EasyProgressMeterCancel(title, *args):
    EasyProgressMeter.EasyProgressMeterData = getattr(EasyProgressMeter, 'EasyProgressMeterData', EasyProgressMeterDataClass())
    if EasyProgressMeter.EasyProgressMeterData.MeterID is not None:
        # tell the normal meter update that we're at max value which will close the meter
        rc = EasyProgressMeter(title, EasyProgressMeter.EasyProgressMeterData.MaxValue, EasyProgressMeter.EasyProgressMeterData.MaxValue, ' *** CANCELLING ***', 'Caller requested a cancel', *args)
        return rc
    return True


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
_easy_print_data = None     # global variable... I'm cheating

class DebugWin():
    def __init__(self, size=(None, None)):
        # Show a form that's a running counter
        win_size = size if size !=(None, None) else DEFAULT_DEBUG_WINDOW_SIZE
        self.form = FlexForm('Debug Window', auto_size_text=True, font=('Courier New', 12))
        self.output_element = Output(size=win_size)
        self.form_rows = [[Text('EasyPrint Output')],
                     [self.output_element],
                     [Quit()]]
        self.form.AddRows(self.form_rows)
        self.form.Show(non_blocking=True)  # Show a ;non-blocking form, returns immediately
        return

    def Print(self, *args, end=None, sep=None):
        sepchar = sep if sep is not None else ' '
        endchar = end if end is not None else '\n'
        print(*args, sep=sepchar, end=endchar)
        # for a in args:
        #     msg = str(a)
        #     print(msg, end="", sep=sepchar)
        #     print(1, 2, 3, sep='-')
        # if end is None:
        #     print("")
        self.form.ReadNonBlocking()

    def Close(self):
        self.form.CloseNonBlockingForm()
        self.form.__del__()

def Print(*args, size=(None,None), end=None, sep=None):
    EasyPrint(*args, size=size, end=end, sep=sep)

def PrintClose():
    EasyPrintClose()

def eprint(*args, size=(None,None), end=None, sep=None):
    EasyPrint(*args, size=size, end=end, sep=sep)

def EasyPrint(*args, size=(None,None), end=None, sep=None):
    global _easy_print_data

    if _easy_print_data  is None:
        _easy_print_data = DebugWin(size=size)
    _easy_print_data.Print(*args, end=end, sep=sep)



def EasyPrintold(*args, size=(None,None), end=None, sep=None):
    if 'easy_print_data' not in EasyPrint.__dict__:     # use a function property to save DebugWin object (static variable)
        EasyPrint.easy_print_data = DebugWin(size=size)
    if EasyPrint.easy_print_data is None:
        EasyPrint.easy_print_data = DebugWin(size=size)
    EasyPrint.easy_print_data.Print(*args, end=end, sep=sep)

def EasyPrintClose():
    if 'easy_print_data' in EasyPrint.__dict__:
        if EasyPrint.easy_print_data is not None:
            EasyPrint.easy_print_data._Close()
        EasyPrint.easy_print_data = None
        # del EasyPrint.easy_print_data

# ========================  Scrolled Text Box   =====#
# ===================================================#
def ScrolledTextBox(*args, button_color=None, yes_no=False, auto_close=False, auto_close_duration=None, size=(None, None)):
    if not args: return
    width, height = size
    width = width if width else MESSAGE_BOX_LINE_WIDTH
    with FlexForm(args[0], auto_size_text=True, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration) as form:
        max_line_total, max_line_width, total_lines, height_computed = 0,0,0,0
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
        pad = max_line_total-15 if max_line_total > 15 else 1
        # show either an OK or Yes/No depending on paramater
        if yes_no:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), Yes(), No())
            button, values = form.Read()
            return button
        else:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), SimpleButton('OK', size=(5, 1), button_color=button_color))
        button, values = form.Read()
        return button


PopupScrolled = ScrolledTextBox

# ---------------------------------------------------------------------- #
#  GetPathBox                                                            #
#   Pre-made dialog that looks like this roughly                         #
#       MESSAGE                                                          #
#        __________________________                                      #
#       |__________________________| (BROWSE)                            #
#       (SUBMIT)  (CANCEL)                                               #
#  RETURNS two values:                                                   #
#    True/False, path                                                    #
#     (True if Submit was pressed, false otherwise)                      #
# ---------------------------------------------------------------------- #
def GetPathBox(title, message, default_path='', button_color=None, size=(None, None)):
    with FlexForm(title, auto_size_text=True, button_color=button_color) as form:
        layout = [[Text(message, auto_size_text=True)],
                  [InputText(default_text=default_path, size=size), FolderBrowse()],
                  [Submit(), Cancel()]]

        (button, input_values) = form.LayoutAndRead(layout)
        if button != 'Submit':
            return False,None
        else:
            path = input_values[0]
            return True, path


def PopupGetFolder(message, default_path='', no_window=False, button_color=None, size=(None, None)):
    if no_window:
        root = tk.Tk()
        try:
            root.attributes('-alpha', 0)  # hide window while building it. makes for smoother 'paint'
        except:
            pass
        folder_name = tk.filedialog.askdirectory()  # show the 'get folder' dialog box
        root.destroy()
        return folder_name

    with FlexForm(title=message, auto_size_text=True, button_color=button_color) as form:
        layout = [[Text(message, auto_size_text=True)],
                  [InputText(default_text=default_path, size=size), FolderBrowse()],
                  [Ok(), Cancel()]]

        (button, input_values) = form.LayoutAndRead(layout)
        if button != 'Ok':
            return None
        else:
            path = input_values[0]
            return path

# ============================== GetFileBox =========#
# Like the Get folder box but for files              #
# ===================================================#
def GetFileBox(title, message, default_path='', file_types=(("ALL Files", "*.*"),), button_color=None, size=(None, None)):
    with FlexForm(title, auto_size_text=True, button_color=button_color) as form:
        layout = [[Text(message, auto_size_text=True)],
                  [InputText(default_text=default_path, size=size), FileBrowse(file_types=file_types)],
                  [Submit(), Cancel()]]

        (button, input_values) = form.LayoutAndRead(layout)
        if button != 'Submit':
            return False,None
        else:
            path = input_values[0]
            return True, path

GetFile = GetFileBox
AskForFile = GetFileBox


def PopupGetFile(message, default_path='',save_as=False, no_window=False,  file_types=(("ALL Files", "*.*"),), button_color=None, size=(None, None)):
    if no_window:
        root = tk.Tk()
        try:
            root.attributes('-alpha', 0)  # hide window while building it. makes for smoother 'paint'
        except:
            pass
        if save_as:
            filename = tk.filedialog.asksaveasfilename(filetypes=file_types)  # show the 'get file' dialog box
        else:
            filename = tk.filedialog.askopenfilename(filetypes=file_types)  # show the 'get file' dialog box
        root.destroy()
        return filename

    if save_as:
        browse_button =  SaveAs(file_types=file_types)
    else:
        browse_button =  FileBrowse(file_types=file_types)

    with FlexForm(title=message, auto_size_text=True, button_color=button_color) as form:
        layout = [[Text(message, auto_size_text=True)],
                  [InputText(default_text=default_path, size=size), browse_button],
                  [Ok(), Cancel()]]

        (button, input_values) = form.LayoutAndRead(layout)
        if button != 'Ok':
            return None
        else:
            path = input_values[0]
            return path


# ============================== GetTextBox =========#
# Get a single line of text                          #
# ===================================================#
def GetTextBox(title, message, default_text='', button_color=None, size=(None, None)):
    with FlexForm(title, auto_size_text=True, button_color=button_color, grab_anywhere=False) as form:
        layout = [[Text(message, auto_size_text=True)],
                  [InputText(default_text=default_text, size=size)],
                  [Submit(), Cancel()]]

        (button, input_values) = form.LayoutAndRead(layout)
        if button != 'Submit':
            return False,None
        else:
            return True, input_values[0]


def PopupGetText(message, default_text='', password_char='', button_color=None, size=(None, None)):
    with FlexForm(title=message, auto_size_text=True, button_color=button_color, grab_anywhere=False) as form:
        layout = [[Text(message, auto_size_text=True)],
                  [InputText(default_text=default_text, size=size, password_char=password_char)],
                  [Ok(), Cancel()]]

        (button, input_values) = form.LayoutAndRead(layout)
        if button != 'Ok':
            return None
        else:
            return input_values[0]


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
def SetOptions(icon=None, button_color=None, element_size=(None,None), button_element_size=(None, None), margins=(None,None),
               element_padding=(None,None),auto_size_text=None, auto_size_buttons=None, font=None, border_width=None,
               slider_border_width=None, slider_relief=None, slider_orientation=None,
               autoclose_time=None, message_box_line_width=None,
               progress_meter_border_depth=None, progress_meter_style=None,
               progress_meter_relief=None, progress_meter_color=None, progress_meter_size=None,
               text_justification=None, background_color=None, element_background_color=None,
               text_element_background_color=None, input_elements_background_color=None, input_text_color=None,
               scrollbar_color=None, text_color=None, element_text_color = None, debug_win_size=(None,None), window_location=(None,None)):

    global DEFAULT_ELEMENT_SIZE
    global DEFAULT_BUTTON_ELEMENT_SIZE
    global DEFAULT_MARGINS                # Margins for each LEFT/RIGHT margin is first term
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

    if element_size != (None,None):
        DEFAULT_ELEMENT_SIZE = element_size

    if button_element_size != (None,None):
        DEFAULT_BUTTON_ELEMENT_SIZE = button_element_size

    if margins != (None,None):
        DEFAULT_MARGINS = margins

    if element_padding != (None,None):
        DEFAULT_ELEMENT_PADDING = element_padding

    if auto_size_text != None:
        DEFAULT_AUTOSIZE_TEXT = auto_size_text

    if auto_size_buttons != None:
        DEFAULT_AUTOSIZE_BUTTONS = auto_size_buttons

    if font !=None:
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

    if window_location != (None,None):
        DEFAULT_WINDOW_LOCATION = window_location

    if debug_win_size != (None,None):
        DEFAULT_DEBUG_WINDOW_SIZE = debug_win_size

    if text_color != None:
        DEFAULT_TEXT_COLOR = text_color

    if scrollbar_color != None:
        DEFAULT_SCROLLBAR_COLOR = scrollbar_color

    if element_text_color != None:
        DEFAULT_ELEMENT_TEXT_COLOR = element_text_color

    if input_text_color is not None:
        DEFAULT_INPUT_TEXT_COLOR = input_text_color
    return True


#################### ChangeLookAndFeel #######################
# Predefined settings that will change the colors and styles #
# of the elements.                                           #
##############################################################
def ChangeLookAndFeel(index):
    # look and feel table
    look_and_feel =  {'SystemDefault': {'BACKGROUND' : COLOR_SYSTEM_DEFAULT, 'TEXT': COLOR_SYSTEM_DEFAULT, 'INPUT': COLOR_SYSTEM_DEFAULT,'TEXT_INPUT' : COLOR_SYSTEM_DEFAULT, 'SCROLL': COLOR_SYSTEM_DEFAULT, 'BUTTON': OFFICIAL_PYSIMPLEGUI_BUTTON_COLOR, 'PROGRESS': COLOR_SYSTEM_DEFAULT, 'BORDER': 1,'SLIDER_DEPTH':1, 'PROGRESS_DEPTH':0},

                      'GreenTan': {'BACKGROUND' : '#9FB8AD', 'TEXT': COLOR_SYSTEM_DEFAULT, 'INPUT':'#F7F3EC','TEXT_INPUT' : 'black','SCROLL': '#F7F3EC', 'BUTTON': ('white', '#475841'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0},

                      'Dark': {'BACKGROUND': 'gray25', 'TEXT': 'white', 'INPUT': 'gray30',
                                   'TEXT_INPUT': 'white', 'SCROLL': 'gray44', 'BUTTON': ('white', '#004F00'),
                                   'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                   'PROGRESS_DEPTH': 0},

                      'Dark2': {'BACKGROUND': 'gray25', 'TEXT': 'white', 'INPUT': 'white',
                               'TEXT_INPUT': 'black', 'SCROLL': 'gray44', 'BUTTON': ('white', '#004F00'),
                               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                               'PROGRESS_DEPTH': 0},

                      'Black': {'BACKGROUND': 'black', 'TEXT': 'white', 'INPUT': 'gray30',
                               'TEXT_INPUT': 'white', 'SCROLL': 'gray44', 'BUTTON': ('black', 'white'),
                               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                               'PROGRESS_DEPTH': 0},

                      'Tan': {'BACKGROUND': '#fdf6e3', 'TEXT': '#268bd1', 'INPUT': '#eee8d5',
                                'TEXT_INPUT': '#6c71c3', 'SCROLL': '#eee8d5', 'BUTTON': ('white', '#063542'),
                                'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                'PROGRESS_DEPTH': 0},

                      'TanBlue': {'BACKGROUND': '#e5dece', 'TEXT': '#063289', 'INPUT': '#f9f8f4',
                              'TEXT_INPUT': '#242834', 'SCROLL': '#eee8d5', 'BUTTON': ('white', '#063289'),
                              'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                              'PROGRESS_DEPTH': 0},

                      'DarkTanBlue': {'BACKGROUND': '#242834', 'TEXT': '#dfe6f8', 'INPUT': '#97755c',
                                  'TEXT_INPUT': 'white', 'SCROLL': '#a9afbb', 'BUTTON': ('white', '#063289'),
                                  'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                  'PROGRESS_DEPTH': 0},

                      'DarkAmber': {'BACKGROUND': '#2c2825', 'TEXT': '#fdcb52', 'INPUT': '#705e52',
                                   'TEXT_INPUT': '#fdcb52', 'SCROLL': '#705e52', 'BUTTON': ('black', '#fdcb52'),
                                   'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                                   'PROGRESS_DEPTH': 0},

                      'DarkBlue': {'BACKGROUND': '#1a2835', 'TEXT': '#d1ecff', 'INPUT': '#335267',
                              'TEXT_INPUT': '#acc2d0', 'SCROLL': '#1b6497', 'BUTTON': ('black', '#fafaf8'),
                              'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                              'PROGRESS_DEPTH': 0},

                      'Reds': {'BACKGROUND': '#280001', 'TEXT': 'white', 'INPUT': '#d8d584',
                               'TEXT_INPUT': 'black', 'SCROLL': '#763e00', 'BUTTON': ('black', '#daad28'),
                               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                               'PROGRESS_DEPTH': 0},

                      'Green': {'BACKGROUND': '#82a459', 'TEXT': 'black', 'INPUT': '#d8d584',
                               'TEXT_INPUT': 'black', 'SCROLL': '#e3ecf3', 'BUTTON': ('white', '#517239'),
                               'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1, 'SLIDER_DEPTH': 0,
                               'PROGRESS_DEPTH': 0},

                      'LightGreen' :{'BACKGROUND' : '#B7CECE', 'TEXT': 'black', 'INPUT':'#FDFFF7','TEXT_INPUT' : 'black', 'SCROLL': '#FDFFF7','BUTTON': ('white', '#658268'), 'PROGRESS':DEFAULT_PROGRESS_BAR_COLOR, 'BORDER':1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0},

                      'BluePurple': {'BACKGROUND' : '#A5CADD', 'TEXT': '#6E266E', 'INPUT':'#E0F5FF','TEXT_INPUT' : 'black', 'SCROLL': '#E0F5FF','BUTTON': ('white', '#303952'),'PROGRESS':DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0},

                      'Purple': {'BACKGROUND': '#B0AAC2', 'TEXT': 'black', 'INPUT': '#F2EFE8','SCROLL': '#F2EFE8','TEXT_INPUT' : 'black',
                                     'BUTTON': ('black', '#C2D4D8'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0},

                      'BlueMono': {'BACKGROUND': '#AAB6D3', 'TEXT': 'black', 'INPUT': '#F1F4FC','SCROLL': '#F1F4FC','TEXT_INPUT' : 'black',
                                     'BUTTON': ('white', '#7186C7'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0},

                      'GreenMono': {'BACKGROUND': '#A8C1B4', 'TEXT': 'black', 'INPUT': '#DDE0DE', 'SCROLL': '#E3E3E3','TEXT_INPUT' : 'black',
                                   'BUTTON': ('white', '#6D9F85'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0},

                      'BrownBlue': {'BACKGROUND': '#64778d', 'TEXT': 'white', 'INPUT': '#f0f3f7', 'SCROLL': '#A6B2BE','TEXT_INPUT' : 'black', 'BUTTON': ('white', '#283b5b'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0},

                      'BrightColors': {'BACKGROUND': '#b4ffb4', 'TEXT': 'black', 'INPUT': '#ffff64','SCROLL': '#ffb482','TEXT_INPUT' : 'black', 'BUTTON': ('black', '#ffa0dc'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0},

                      'NeutralBlue': {'BACKGROUND': '#92aa9d', 'TEXT': 'black', 'INPUT': '#fcfff6',
                                       'SCROLL': '#fcfff6', 'TEXT_INPUT': 'black', 'BUTTON': ('black', '#d0dbbd'),
                                       'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0},

                      'Kayak': {'BACKGROUND': '#a7ad7f', 'TEXT': 'black', 'INPUT': '#e6d3a8',
                                      'SCROLL': '#e6d3a8', 'TEXT_INPUT': 'black', 'BUTTON': ('white', '#5d907d'),
                                      'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0},

                      'SandyBeach': {'BACKGROUND': '#efeccb', 'TEXT': '#012f2f', 'INPUT': '#e6d3a8',
                                'SCROLL': '#e6d3a8', 'TEXT_INPUT': '#012f2f', 'BUTTON': ('white', '#046380'),
                                'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0},

                      'TealMono': {'BACKGROUND': '#a8cfdd', 'TEXT': 'black', 'INPUT': '#dfedf2','SCROLL': '#dfedf2', 'TEXT_INPUT' : 'black', 'BUTTON': ('white', '#183440'), 'PROGRESS': DEFAULT_PROGRESS_BAR_COLOR, 'BORDER': 1,'SLIDER_DEPTH':0, 'PROGRESS_DEPTH':0}
                      }
    try:
        colors = look_and_feel[index]

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
    except:    # most likely an index out of range
        pass




# ============================== sprint ======#
# Is identical to the Scrolled Text Box       #
# Provides a crude 'print' mechanism but in a #
# GUI environment                             #
# ============================================#
sprint=ScrolledTextBox

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
# =====================================   Upper PySimpleGUI ============================================================== #
#   Pre-built dialog boxes for all your needs                                                                        #
# ------------------------------------------------------------------------------------------------------------------ #

# ====================================  MSG BOX =====#
# Display a message wrapping at 60 characters        #
# Exits via an OK button2 press                      #
# Returns nothing                                    #
# ===================================================#
def Popup(*args, button_color=None, button_type=MSG_BOX_OK, auto_close=False, auto_close_duration=None, non_blocking=False, icon=DEFAULT_WINDOW_ICON, line_width=None, font=None, no_titlebar=False, keep_on_top=False):
    '''
    Show message box.  Displays one line per user supplied argument. Takes any Type of variable to display.
    :param args:
    :param button_color:
    :param button_type:
    :param auto_close:
    :param auto_close_duration:
    :param icon:
    :param line_width:
    :param font:
    :return:
    '''
    if not args:
        args_to_print = ['']
    else:
        args_to_print = args
    if line_width != None:
        local_line_width = line_width
    else:
        local_line_width = MESSAGE_BOX_LINE_WIDTH
    title = args_to_print[0] if args_to_print[0] is not None else 'None'
    with FlexForm(title, auto_size_text=True, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, icon=icon, font=font, no_titlebar=no_titlebar, keep_on_top=keep_on_top) as form:
        max_line_total, total_lines = 0,0
        for message in args_to_print:
            # fancy code to check if string and convert if not is not need. Just always convert to string :-)
            # if not isinstance(message, str): message = str(message)
            message = str(message)
            if message.count('\n'):
                message_wrapped = message
            else:
                message_wrapped = textwrap.fill(message, local_line_width)
            message_wrapped_lines = message_wrapped.count('\n')+1
            longest_line_len = max([len(l) for l in message.split('\n')])
            width_used = min(longest_line_len, local_line_width)
            max_line_total = max(max_line_total, width_used)
            # height = _GetNumLinesNeeded(message, width_used)
            height = message_wrapped_lines
            # print('Msgbox width, height', width_used, height)
            form.AddRow(Text(message_wrapped, auto_size_text=True))
            total_lines += height

        pad = max_line_total-15 if max_line_total > 15 else 1
        pad =1
        if non_blocking:
            PopupButton = DummyButton
        else:
            PopupButton = SimpleButton
        # show either an OK or Yes/No depending on paramater
        if button_type is MSG_BOX_YES_NO:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), PopupButton('Yes', button_color=button_color, focus=True, bind_return_key=True), PopupButton('No', button_color=button_color))
        elif button_type is MSG_BOX_CANCELLED:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), PopupButton('Cancelled', button_color=button_color, focus=True, bind_return_key=True))
        elif button_type is MSG_BOX_ERROR:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), PopupButton('ERROR', size=(5, 1), button_color=button_color, focus=True, bind_return_key=True))
        elif button_type is MSG_BOX_OK_CANCEL:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), PopupButton('OK', size=(5, 1), button_color=button_color, focus=True, bind_return_key=True),
                        PopupButton('Cancel', size=(5, 1), button_color=button_color))
        elif button_type is MSG_BOX_NO_BUTTONS:
            pass
        else:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), PopupButton('OK', size=(5, 1), button_color=button_color, focus=True, bind_return_key=True))

        if non_blocking:
            button, values = form.ReadNonBlocking()
        else:
            button, values = form.Show()

    return button



# ==============================  MsgBox============#
# Lazy function. Same as calling Popup with parms   #
# ==================================================#
# MsgBox is the legacy call and show not be used any longer
MsgBox = Popup

# --------------------------- PopupNoButtons ---------------------------
def PopupoNoButtons(*args, button_color=None, auto_close=False, auto_close_duration=None, font=None):
    Popup(*args, button_type=MSG_BOX_NO_BUTTONS, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)
    return


# --------------------------- PopupNonBlocking ---------------------------
def PopupoNonBlocking(*args, button_color=None, auto_close=False, auto_close_duration=None, font=None):
    Popup(*args, non_blocking=True, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)
    return

PopupNoWait = PopupoNonBlocking


# --------------------------- PopupNoFrame ---------------------------
def PopupNoTitlebar(*args, button_color=None, auto_close=False, auto_close_duration=None, font=None):
    Popup(*args, non_blocking=False, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font, no_titlebar=True)
    return

PopupNoFrame = PopupNoTitlebar
PopupNoBorder = PopupNoTitlebar
PopupAnnoying = PopupNoTitlebar


# ==============================  MsgBoxAutoClose====#
# Lazy function. Same as calling MsgBox with parms   #
# ===================================================#
def MsgBoxAutoClose(*args, button_color=None, auto_close=True, auto_close_duration=DEFAULT_AUTOCLOSE_TIME, font=None):
    '''
    Display a standard MsgBox that will automatically close after a specified amount of time
    :param args:
    :param button_color:
    :param auto_close:
    :param auto_close_duration:
    :param font:
    :return:
    '''
    return MsgBox(*args, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)

PopupTimed = MsgBoxAutoClose
PopupAutoClose = MsgBoxAutoClose

# ==============================  MsgBoxError   =====#
# Like MsgBox but presents RED BUTTONS               #
# ===================================================#
def MsgBoxError(*args, button_color=DEFAULT_ERROR_BUTTON_COLOR, auto_close=False, auto_close_duration=None, font=None):
    '''
    Display a MsgBox with a red button
    :param args:
    :param button_color:
    :param auto_close:
    :param auto_close_duration:
    :param font:
    :return:
    '''
    return MsgBox(*args, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)


PopupError = MsgBoxError


# ==============================  MsgBoxCancel  =====#
#                                                    #
# ===================================================#
def MsgBoxCancel(*args, button_color=None, auto_close=False, auto_close_duration=None, font=None):
    '''
    Display a MsgBox with a single "Cancel" button.
    :param args:
    :param button_color:
    :param auto_close:
    :param auto_close_duration:
    :param font:
    :return:
    '''
    return MsgBox(*args, button_type=MSG_BOX_CANCELLED, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)

PopupCancel = MsgBoxCancel


# ==============================  MsgBoxOK      =====#
# Like MsgBox but only 1 button                      #
# ===================================================#
def MsgBoxOK(*args, button_color=None, auto_close=False, auto_close_duration=None, font=None):
    '''
    Display a MsgBox with a single buttoned labelled "OK"
    :param args:
    :param button_color:
    :param auto_close:
    :param auto_close_duration:
    :param font:
    :return:
    '''
    return MsgBox(*args, button_type=MSG_BOX_OK, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)

PopupOk = MsgBoxOK


# ==============================  MsgBoxOKCancel ====#
# Like MsgBox but presents OK and Cancel buttons     #
# ===================================================#
def MsgBoxOKCancel(*args, button_color=None, auto_close=False, auto_close_duration=None, font=None):
    '''
    Display MsgBox with 2 buttons, "OK" and "Cancel"
    :param args:
    :param button_color:
    :param auto_close:
    :param auto_close_duration:
    :param font:
    :return:
    '''
    return MsgBox(*args, button_type=MSG_BOX_OK_CANCEL, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)

PopupOkCancel = MsgBoxOKCancel


# ====================================  YesNoBox=====#
# Like MsgBox but presents Yes and No buttons        #
# Returns True if Yes was pressed else False         #
# ===================================================#
def MsgBoxYesNo(*args, button_color=None, auto_close=False, auto_close_duration=None, font=None):
    '''
    Display MsgBox with 2 buttons, "Yes" and "No"
    :param args:
    :param button_color:
    :param auto_close:
    :param auto_close_duration:
    :param font:
    :return:
    '''
    result = MsgBox(*args, button_type=MSG_BOX_YES_NO, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)
    return result


PopupYesNo = MsgBoxYesNo



def main():
    with FlexForm('Demo form..') as form:
        form_rows = [[Text('You are running the PySimpleGUI.py file itself')],
                     [Text('You should be importing it rather than running it', size=(50,2))],
                     [Text('Here is your sample input form....')],
                     [Text('Source Folder', size=(15, 1), justification='right'), InputText('Source', focus=True),FolderBrowse()],
                     [Text('Destination Folder', size=(15, 1), justification='right'), InputText('Dest'), FolderBrowse()],
                     [Ok(), Cancel()]]

        button, (source, dest) = form.LayoutAndRead(form_rows)


if __name__ == '__main__':
    main()
    exit(69)