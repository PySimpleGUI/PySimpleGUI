#!/usr/bin/env Python3
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
import tkinter.scrolledtext as tkst
import tkinter.font
from random import randint
import datetime
import sys
import textwrap


# ----====----====----==== Constants the use CAN safely change ====----====----====----#
DEFAULT_WINDOW_ICON = ''
DEFAULT_ELEMENT_SIZE = (45,1)           # In CHARACTERS
DEFAULT_MARGINS = (10,5)                # Margins for each LEFT/RIGHT margin is first term
DEFAULT_ELEMENT_PADDING = (5,3)         # Padding between elements (row, col) in pixels
DEFAULT_AUTOSIZE_TEXT = False
DEFAULT_FONT = ("Helvetica", 10)

DEFAULT_BORDER_WIDTH = 6
DEFAULT_AUTOCLOSE_TIME = 3              # time in seconds to show an autoclose form
MAX_SCROLLED_TEXT_BOX_HEIGHT = 50
#################### COLOR STUFF ####################
BLUES = ("#082567","#0A37A3","#00345B")
PURPLES = ("#480656","#4F2398","#380474")
GREENS = ("#01826B","#40A860","#96D2AB", "#00A949","#003532")
YELLOWS = ("#F3FB62", "#F0F595")
TANS = ("#FFF9D5","#F4EFCF","#DDD8BA")
NICE_BUTTON_COLORS = ((GREENS[3], TANS[0]), ('#000000','#FFFFFF'),('#FFFFFF', '#000000'), (YELLOWS[0], PURPLES[1]),
               (YELLOWS[0], GREENS[3]), (YELLOWS[0], BLUES[2]))
# DEFAULT_BUTTON_COLOR = (YELLOWS[0], PURPLES[0])    # (Text, Background) or (Color "on", Color) as a way to remember
# DEFAULT_BUTTON_COLOR = (GREENS[3], TANS[0])    # Foreground, Background (None, None) == System Default
# DEFAULT_BUTTON_COLOR = (YELLOWS[0], GREENS[4])    # Foreground, Background (None, None) == System Default
DEFAULT_BUTTON_COLOR = ('white', 'black')    # Foreground, Background (None, None) == System Default
# DEFAULT_BUTTON_COLOR = (YELLOWS[0], PURPLES[2])    # Foreground, Background (None, None) == System Default
DEFAULT_ERROR_BUTTON_COLOR =("#FFFFFF", "#FF0000")
DEFAULT_CANCEL_BUTTON_COLOR = (GREENS[3], TANS[0])
BarColor=()
# DEFAULT_PROGRESS_BAR_COLOR = (GREENS[2], GREENS[0])     # a nice green progress bar
DEFAULT_PROGRESS_BAR_COLOR = (GREENS[3], GREENS[3])     # a nice green progress bar
# DEFAULT_PROGRESS_BAR_COLOR = (BLUES[1], BLUES[1])     # a nice green progress bar
# DEFAULT_PROGRESS_BAR_COLOR = (BLUES[0], BLUES[0])     # a nice green progress bar
# DEFAULT_PROGRESS_BAR_COLOR = (PURPLES[1],PURPLES[0])    # a nice purple progress bar
DEFAULT_PROGRESS_BAR_SIZE = (30,25)         # Size of Progress Bar (characters for length, pixels for width)
DEFAULT_PROGRESS_BAR_BORDER_WIDTH=8
DEFAULT_PROGRESS_BAR_RELIEF = tk.SUNKEN
DEFAULT_PROGRESS_BAR_STYLE = 'default'
DEFAULT_METER_ORIENTATION = 'Horizontal'
# DEFAULT_METER_ORIENTATION = 'Vertical'
# ----====----====----==== Constants the user should NOT f-with ====----====----====----#
ThisRow = 555666777         # magic number
# Progress Bar Relief Choices
# -relief
RAISED='raised'
SUNKEN='sunken'
FLAT='flat'
RIDGE='ridge'
GROOVE='groove'
SOLID = 'solid'

PROGRESS_BAR_STYLES = ('default','winnative', 'clam', 'alt', 'classic', 'vista', 'xpnative')
# DEFAULT_WINDOW_ICON = ''
MESSAGE_BOX_LINE_WIDTH = 60

# a shameful global variable. This represents the top-level window information. Needed because opening a second window is different than opening the first.
class MyWindows():
    def __init__(self):
        self.NumOpenWindows = 0
        self.user_defined_icon = None

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
BROWSE_FOLDER = 1
BROWSE_FILE = 2
CLOSES_WIN = 5
READ_FORM = 7

# -------------------------  Element types  ------------------------- #
# class ElementType(Enum):
TEXT = 1
INPUT_TEXT = 20
INPUT_COMBO = 21
INPUT_RADIO = 5
INPUT_MULTILINE = 7
INPUT_CHECKBOX = 8
INPUT_SPIN = 9
BUTTON = 3
OUTPUT = 300
PROGRESS_BAR = 200
BLANK = 100

# -------------------------  MsgBox Buttons Types  ------------------------- #
MSG_BOX_YES_NO = 1
MSG_BOX_CANCELLED = 2
MSG_BOX_ERROR = 3
MSG_BOX_OK_CANCEL = 4
MSG_BOX_OK = 0

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
    def __init__(self, type, scale=(None, None), size=(None, None), auto_size_text=None, font=None):
        self.Size = size
        self.Type = type
        self.AutoSizeText = auto_size_text
        self.Scale = scale
        self.Pad = DEFAULT_ELEMENT_PADDING
        self.Font = font

        self.TKStringVar = None
        self.TKIntVar = None
        self.TKText = None
        self.TKEntry = None

        self.ParentForm=None
        self.TextInputDefault = None
        self.Position = (0,0)       # Default position Row 0, Col 0
        return

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
#                           Input Class                                 #
# ---------------------------------------------------------------------- #
class InputText(Element):

    def __init__(self, default_text ='', scale=(None, None), size=(None, None), auto_size_text=None):
        self.DefaultText = default_text
        super().__init__(INPUT_TEXT, scale, size, auto_size_text)
        return

    def ReturnKeyHandler(self, event):
        MyForm = self.ParentForm
        # search through this form and find the first button that will exit the form
        for row in MyForm.Rows:
            for element in row.Elements:
                if element.Type == BUTTON:
                    if element.BType == CLOSES_WIN or element.BType == READ_FORM:
                        element.ButtonCallBack()
                        return
    def __del__(self):
        super().__del__()

# ---------------------------------------------------------------------- #
#                           Combo                                        #
# ---------------------------------------------------------------------- #
class InputCombo(Element):

    def __init__(self, values, scale=(None, None), size=(None, None), auto_size_text=None):
        self.Values = values
        self.TKComboBox = None
        super().__init__(INPUT_COMBO, scale, size, auto_size_text)
        return

    def __del__(self):
        try:
            self.TKComboBox.__del__()
        except:
            pass
        super().__del__()

# ---------------------------------------------------------------------- #
#                           Radio                                        #
# ---------------------------------------------------------------------- #
class Radio(Element):
    def __init__(self, text, group_id, default=False, scale=(None, None), size=(None, None), auto_size_text=None, font=None):
        self.InitialState = default
        self.Text = text
        self.TKRadio = None
        self.GroupID = group_id
        self.Value = None
        super().__init__(INPUT_RADIO, scale, size, auto_size_text, font)
        return

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
    def __init__(self, text, default=False, scale=(None, None), size=(None, None), auto_size_text=None, font=None):
        self.Text = text
        self.InitialState = default
        self.Value = None
        self.TKCheckbox = None

        super().__init__(INPUT_CHECKBOX, scale, size, auto_size_text, font)
        return

    def __del__(self):
        try:
            self.TKCheckbox.__del__()
        except:
            pass
        super().__del__()

# ---------------------------------------------------------------------- #
#                           Spin                                         #
# ---------------------------------------------------------------------- #

class Spin(Element):
    # Values = None
    # TKSpinBox = None
    def __init__(self, values, initial_value=None, scale=(None, None), size=(None, None), auto_size_text=None, font=None):
        self.Values = values
        self.DefaultValue = initial_value
        self.TKSpinBox = None
        super().__init__(INPUT_SPIN, scale, size, auto_size_text, font=font)
        return

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
    def __init__(self, default_text='', enter_submits = False, scale=(None, None), size=(None, None), auto_size_text=None):
        self.DefaultText = default_text
        self.EnterSubmits = enter_submits
        super().__init__(INPUT_MULTILINE, scale, size, auto_size_text)
        return

    def ReturnKeyHandler(self, event):
        MyForm = self.ParentForm
        # search through this form and find the first button that will exit the form
        for row in MyForm.Rows:
            for element in row.Elements:
                if element.Type == BUTTON:
                    if element.BType == CLOSES_WIN or element.BType == READ_FORM:
                        element.ButtonCallBack()
                        return

    def __del__(self):
        super().__del__()

# ---------------------------------------------------------------------- #
#                                       Text                             #
# ---------------------------------------------------------------------- #
class Text(Element):
    def __init__(self, text, scale=(None, None), size=(None, None), auto_size_text=None, font=None, text_color=None):
        self.DisplayText = text
        self.TextColor = text_color if text_color else 'black'
        # self.Font = Font if Font else DEFAULT_FONT
        # i=1/0
        super().__init__(TEXT, scale, size, auto_size_text, font=font if font else DEFAULT_FONT)
        return

    def Update(self, NewValue):
        self.DisplayText=NewValue
        stringvar = self.TKStringVar
        stringvar.set(NewValue)

    def __del__(self):
        super().__del__()


# ---------------------------------------------------------------------- #
#                       TKProgressBar                                    #
#  Emulate the TK ProgressBar using canvas and rectangles
# ---------------------------------------------------------------------- #

class TKProgressBar():
    def __init__(self, root, max, length=400, width=20, highlightt=0, relief='sunken', border_width=4, orientation='horizontal', BarColor=DEFAULT_PROGRESS_BAR_COLOR):
        self.Length = length
        self.Width = width
        self.Max = max
        self.Orientation = orientation
        self.Count = None
        self.PriorCount = 0
        if orientation[0].lower() == 'h':
            self.TKCanvas = tk.Canvas(root, width=length, height=width, highlightt=highlightt, relief=relief, borderwidth=border_width)
            self.TKRect = self.TKCanvas.create_rectangle(0, 0, -(length * 1.5), width * 1.5, fill=BarColor[0], tags='bar')
            # self.canvas.pack(padx='10')
        else:
            self.TKCanvas = tk.Canvas(root, width=width, height=length, highlightt=highlightt, relief=relief, borderwidth=border_width)
            self.TKRect = self.TKCanvas.create_rectangle(width * 1.5, 2 * length + 40, 0, length * .5, fill=BarColor[0], tags='bar')
            # self.canvas.pack()

    def Update(self, count):
        if count > self.Max: return
        if self.Orientation[0].lower() == 'h':
            try:
                if count != self.PriorCount:
                    delta = count - self.PriorCount
                    self.TKCanvas.move(self.TKRect, delta*(self.Length / self.Max), 0)
                if 0: self.TKCanvas.update()
            except:
                return False            # the window was closed by the user on us
        else:
            try:
                if count != self.PriorCount:
                    delta = count - self.PriorCount
                    self.TKCanvas.move(self.TKRect, 0, delta*(-self.Length / self.Max))
                if 0: self.TKCanvas.update()
            except:
                return False            # the window was closed by the user on us
        self.PriorCount = count
        return True

    def __del__(self):
        try:
            self.TKCanvas.__del__()
            self.TKRect.__del__()
        except:
            pass

# ---------------------------------------------------------------------- #
#                           Output                                       #
#   New Type of Widget that's a Text Widget in disguise                  #
# ---------------------------------------------------------------------- #
class TKOutput(tk.Frame):
    ''' Demonstrate python interpreter output in Tkinter Text widget
type python expression in the entry, hit DoIt and see the results
in the text pane.'''
    # previous_stderr = None
    # previous_stdout = None
    def __init__(self, parent, width, height, bd):
        tk.Frame.__init__(self, parent)
        self.output = tk.Text(parent, width=width, height=height, bd=bd)

        self.vsb = tk.Scrollbar(parent, orient="vertical", command=self.output.yview)
        self.vsb.pack(side="right", fill="y")
        self.output.configure(yscrollcommand=self.vsb.set)
        self.output.pack(side="left", fill="both", expand=True)
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

class Output(Element):
    def __init__(self, scale=(None, None), size=(None, None)):
        self.TKOut = None
        super().__init__(OUTPUT, scale, size)

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
    def __init__(self, button_type=CLOSES_WIN, target=(None, None), button_text='', file_types=(("ALL Files", "*.*"),), scale=(None, None), size=(None, None), auto_size_text=None, button_color=None, font=None):
        self.BType = button_type
        self.FileTypes = file_types
        self.TKButton = None
        self.Target = target
        self.ButtonText = button_text
        self.ButtonColor = button_color if button_color else DEFAULT_BUTTON_COLOR
        self.UserData = None
        super().__init__(BUTTON, scale, size, auto_size_text, font=font)
        return

    # -------  Button Callback  ------- #
    def ButtonCallBack(self):
        global _my_windows
        # Buttons modify targets or return from the form
        # If modifying target, get the element object at the target and modify its StrVar
        target = self.Target
        if target[0] == ThisRow:
            target = [self.Position[0], target[1]]
            if target[1] < 0:
                target[1] = self.Position[1] + target[1]
        strvar = None
        if target[0] != None:
            if target[0] < 0:
                target = [self.Position[0] + target[0], target[1]]
            target_element = self.ParentForm.GetElementAtLocation(target)
            try:
                strvar = target_element.TKStringVar
            except: pass
        else:
            strvar = None
        filetypes = [] if self.FileTypes is None else self.FileTypes
        if self.BType == BROWSE_FOLDER:
            folder_name = tk.filedialog.askdirectory()  # show the 'get folder' dialog box
            try:
                strvar.set(folder_name)
            except: pass
        elif self.BType == BROWSE_FILE:
            file_name = tk.filedialog.askopenfilename(filetypes=filetypes)  # show the 'get file' dialog box
            strvar.set(file_name)
        elif self.BType == CLOSES_WIN:  # this is a return type button so GET RESULTS and destroy window
            # first, get the results table built
            # modify the Results table in the parent FlexForm object
            r,c = self.Position
            self.ParentForm.Results[r][c] = True        # mark this button's location in results
            # if the form is tabbed, must collect all form's results and destroy all forms
            if self.ParentForm.IsTabbedForm:
                self.ParentForm.UberParent.Close()
            else:
                self.ParentForm.Close()
            self.ParentForm.TKroot.quit()
            if self.ParentForm.NonBlocking:
                self.ParentForm.TKroot.destroy()
                _my_windows.NumOpenWindows -= 1 * (_my_windows.NumOpenWindows != 0)  # decrement if not 0
        elif self.BType == READ_FORM:                   # LEAVE THE WINDOW OPEN!! DO NOT CLOSE
            # first, get the results table built
            # modify the Results table in the parent FlexForm object
            r,c = self.Position
            self.ParentForm.Results[r][c] = True        # mark this button's location in results
            self.ParentForm.TKroot.quit()               # kick the users out of the mainloop
        return

    def ReturnKeyHandler(self, event):
        MyForm = self.ParentForm
        # search through this form and find the first button that will exit the form
        for row in MyForm.Rows:
            for element in row.Elements:
                if element.Type == BUTTON:
                    if element.BType == CLOSES_WIN or element.BType == READ_FORM:
                        element.ButtonCallBack()
                        return

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
    def __init__(self, max_value, orientation=None, target=(None, None), scale=(None, None), size=(None, None), auto_size_text=None, bar_color=(None, None), style=None, broder_width=None, relief=None):
        self.MaxValue = max_value
        self.TKProgressBar = None
        self.Cancelled = False
        self.NotRunning = True
        self.Orientation = orientation if orientation else DEFAULT_METER_ORIENTATION
        self.BarColor = bar_color
        self.BarStyle = style if style else DEFAULT_PROGRESS_BAR_STYLE
        self.Target = target
        self.BorderWidth = broder_width if broder_width else DEFAULT_PROGRESS_BAR_BORDER_WIDTH
        self.Relief = relief if relief else DEFAULT_PROGRESS_BAR_RELIEF
        self.BarExpired = False
        super().__init__(PROGRESS_BAR, scale, size, auto_size_text)
        return

    def UpdateBar(self, current_count):
        if self.ParentForm.TKrootDestroyed:
            return False
        target = self.Target
        if target[0] != None:  # if there's a target, get it and update the strvar
            target_element = self.ParentForm.GetElementAtLocation(target)
            strvar = target_element.TKStringVar
            rc = strvar.set(self.TextToDisplay)
        # update the progress bar counter
        # self.TKProgressBar['value'] = self.CurrentValue

        self.TKProgressBar.Update(current_count)
        try:
            self.ParentForm.TKroot.update()
        except:
            _my_windows.NumOpenWindows -= 1 * (_my_windows.NumOpenWindows != 0)  # decrement if not 0
            return False
        return True

    def __del__(self):
        try:
            self.TKProgressBar.__del__()
        except:
            pass
        super().__del__()

# ------------------------------------------------------------------------- #
#                       Row CLASS                                           #
# ------------------------------------------------------------------------- #
class Row():
    def __init__(self, auto_size_text = None):
        self.AutoSizeText = auto_size_text        # Setting to override the form's policy on autosizing.
        self.Elements = []              # List of Elements in this Rrow
        return

    # ------------------------- AddElement ------------------------- #
    def AddElement(self, element):
        self.Elements.append(element)
        return

    # -------------------------  Print  ------------------------- #
    def __str__(self):
        outstr = ''
        for i, element in enumerate(self.Elements):
            outstr += 'Element #%i = %s'%(i,element)
            # outstr += f'Element #{i} = {element}'
        return outstr

# ------------------------------------------------------------------------- #
#                       FlexForm CLASS                                      #
# ------------------------------------------------------------------------- #
class FlexForm:
    '''
    Display a user defined for and return the filled in data
    '''
    def __init__(self, title, default_element_size=(DEFAULT_ELEMENT_SIZE[0], DEFAULT_ELEMENT_SIZE[1]), auto_size_text=DEFAULT_AUTOSIZE_TEXT, scale=(None, None), size=(None, None), location=(None, None), button_color=None, font=None, progress_bar_color=(None, None), is_tabbed_form=False, border_depth=None, auto_close=False, auto_close_duration=DEFAULT_AUTOCLOSE_TIME, icon=DEFAULT_WINDOW_ICON):
        self.AutoSizeText = auto_size_text
        self.Title = title
        self.Rows = []                     # a list of ELEMENTS for this row
        self.DefaultElementSize = default_element_size
        self.Size = size
        self.Scale = scale
        self.Location = location
        self.ButtonColor = button_color if button_color else DEFAULT_BUTTON_COLOR
        self.IsTabbedForm = is_tabbed_form
        self.ParentWindow = None
        self.Font = font if font else DEFAULT_FONT
        self.RadioDict = {}
        self.BorderDepth = border_depth
        self.WindowIcon = icon if not _my_windows.user_defined_icon else _my_windows.user_defined_icon
        self.AutoClose = auto_close
        self.NonBlocking = False
        self.TKroot = None
        self.TKrootDestroyed = False
        self.TKAfterID = None
        self.ProgressBarColor = progress_bar_color
        self.AutoCloseDuration = auto_close_duration
        self.UberParent = None
        self.RootNeedsDestroying = False
        self.Shown = False
        self.ReturnValues = None

    # ------------------------- Add ONE Row to Form ------------------------- #
    def AddRow(self, *args, auto_size_text=None):
        ''' Parms are a variable number of Elements '''
        NumRows = len(self.Rows)               # number of existing rows is our row number
        CurrentRowNumber = NumRows             # this row's number
        CurrentRow = Row(auto_size_text)                      # start with a blank row and build up
        # -------------------------  Add the elements to a row  ------------------------- #
        for i, element in enumerate(args):                    # Loop through list of elements and add them to the row
            element.Position = (CurrentRowNumber, i)
            CurrentRow.Elements.append(element)
        CurrentRow.AutoSizeText = auto_size_text
        # -------------------------  Append the row to list of Rows  ------------------------- #
        self.Rows.append(CurrentRow)

    # ------------------------- Add Multiple Rows to Form ------------------------- #
    def AddRows(self,rows):
        for row in rows:
            self.AddRow(*row)

    def LayoutAndShow(self,rows):
        self.AddRows(rows)
        self.Show()
        return self.ReturnValues

    # ------------------------- ShowForm   THIS IS IT! ------------------------- #
    def Show(self, non_blocking=False):
        self.Shown = True
        # Compute num rows & num cols (it'll come in handy debugging)
        self.NumRows = len(self.Rows)
        self.NumCols = max(len(row.Elements) for row in self.Rows)
        self.NonBlocking=non_blocking

        # -=-=-=-=-=-=-=-=- RUN the GUI -=-=-=-=-=-=-=-=- ##
        StartupTK(self)
        return self.ReturnValues

    # ------------------------- SetIcon - set the window's fav icon ------------------------- #
    def SetIcon(self, icon):
        self.WindowIcon = icon
        try:
            self.TKroot.iconbitmap(icon)
        except: pass

    def GetElementAtLocation(self, location):
        (row_num,col_num) = location
        row = self.Rows[row_num]
        element = row.Elements[col_num]
        return element

    def GetDefaultElementSize(self):
        return self.DefaultElementSize

    def AutoCloseAlarmCallback(self):
        try:
            if self.UberParent:
                window = self.UberParent
            else:
                window = self
            if window:
                window.Close()
                self.TKroot.quit()
                self.RootNeedsDestroying = True
        except:
            pass

    def Read(self):
        if self.TKrootDestroyed: return None
        if not self.TKrootDestroyed and not self.Shown:
            self.Show()
        elif not self.TKrootDestroyed:
            self.TKroot.mainloop()
            if self.RootNeedsDestroying:
                self.TKroot.destroy()
        return(BuildResults(self))

    def OutputFlush(self, Message=''):
        if self.TKrootDestroyed: return None
        if Message:
            print(Message)
        try:
            self.TKroot.update()
        except:
            self.TKrootDestroyed = True
        return(BuildResults(self))

    def Close(self):
        try:
            self.TKroot.update()
        except: pass
        results = BuildResults(self)
        if self.TKrootDestroyed:
            return results
        self.TKrootDestroyed = True
        self.RootNeedsDestroying = True
        return results

    def OnClosingCallback(self):
        return

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.__del__()
        return self

    def __del__(self):
        for row in self.Rows:
            for element in row.Elements:
                element.__del__()
        try:
            del(self.TKroot)
        except:
            pass

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

    def Close(self):
        self.FormReturnValues = []
        for form in self.FormList:
            form.Close()
            self.FormReturnValues.append(form.ReturnValues)
        if not self.TKrootDestroyed:
            self.TKrootDestroyed = True
            self.TKroot.destroy()

    def __del__(self):
        return

# ====================================================================== #
# BUTTON Lazy Functions                                                  #
# ====================================================================== #

# -------------------------  INPUT TEXT Element lazy functions  ------------------------- #
def In(default_text ='', scale=(None, None), size=(None, None), auto_size_text=None):
    return InputText(default_text=default_text, scale=scale, size=size, auto_size_text=auto_size_text)

def Input(default_text ='', scale=(None, None), size=(None, None), auto_size_text=None):
    return InputText(default_text=default_text, scale=scale, size=size, auto_size_text=auto_size_text)

# -------------------------  TEXT Element lazy functions  ------------------------- #
def Txt(display_text, scale=(None, None), size=(None, None), auto_size_text=None, font=None, text_color=None):
    return Text(display_text, scale=scale, size=size, auto_size_text=auto_size_text, font=font, text_color=text_color)

def T(display_text, scale=(None, None), size=(None, None), auto_size_text=None, font=None, text_color=None):
    return Text(display_text, scale=scale, size=size, auto_size_text=auto_size_text, font=font, text_color=text_color)

# -------------------------  FOLDER BROWSE Element lazy function  ------------------------- #
def FolderBrowse(target=(ThisRow, -1), button_text='Browse', scale=(None, None), size=(None, None), auto_size_text=None, button_color=None):
    return Button(BROWSE_FOLDER, target=target, button_text=button_text, scale=scale, size=size, auto_size_text=auto_size_text, button_color=button_color)

# -------------------------  FILE BROWSE Element lazy function  ------------------------- #
def FileBrowse(target=(ThisRow, -1), file_types=(("ALL Files", "*.*"),), button_text='Browse', scale=(None, None), size=(None, None), auto_size_text=None, button_color=None):
    return Button(BROWSE_FILE, target, button_text=button_text, file_types=file_types, scale=scale, size=size, auto_size_text=auto_size_text, button_color=button_color)

# -------------------------  SUBMIT BUTTON Element lazy function  ------------------------- #
def Submit(button_text='Submit', scale=(None, None), size=(None, None), auto_size_text=None, button_color=None):
    return Button(CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_text=auto_size_text, button_color=button_color)

# -------------------------  OK BUTTON Element lazy function  ------------------------- #
def OK(button_text='OK', scale=(None, None), size=(None, None), auto_size_text=None, button_color=None):
    return Button(CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_text=auto_size_text, button_color=button_color)

# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Ok(button_text='Ok', scale=(None, None), size=(None, None), auto_size_text=None, button_color=None):
    return Button(CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_text=auto_size_text, button_color=button_color)

# -------------------------  CANCEL BUTTON Element lazy function  ------------------------- #
def Cancel(button_text='Cancel', scale=(None, None), size=(None, None), auto_size_text=None, button_color=None, font=None):
    return Button(CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_text=auto_size_text, button_color=button_color, font=font)

# -------------------------  YES BUTTON Element lazy function  ------------------------- #
def Yes(button_text='Yes', scale=(None, None), size=(None, None), auto_size_text=None, button_color=None):
    return Button(CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_text=auto_size_text, button_color=button_color)

# -------------------------  NO BUTTON Element lazy function  ------------------------- #
def No(button_text='No', scale=(None, None), size=(None, None), auto_size_text=None, button_color=None):
    return Button(CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_text=auto_size_text, button_color=button_color)

# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
# this is the only button that REQUIRES button text field
def SimpleButton(button_text, scale=(None, None), size=(None, None), auto_size_text=None, button_color=None, font=None):
    return Button(CLOSES_WIN, button_text=button_text, scale=scale, size=size, auto_size_text=auto_size_text, button_color=button_color, font=font)

# -------------------------  GENERIC BUTTON Element lazy function  ------------------------- #
# this is the only button that REQUIRES button text field
def ReadFormButton(button_text, scale=(None, None), size=(None, None), auto_size_text=None, button_color=None, Font=None):
    return Button(READ_FORM, button_text=button_text, scale=scale, size=size, auto_size_text=auto_size_text, button_color=button_color, font=Font)

#------------------------------------------------------------------------------------------------------#
# -------  FUNCTION InitializeResults.  Sets up form results matrix  ------- #
def InitializeResults(form):
    # initial results for elements are:
    #   TEXT - None
    #   INPUT - Initial value
    #   Button - False
    results = []
    return_vals = []
    for row_num,row in enumerate(form.Rows):
        r = []
        for element in row.Elements:
            if element.Type == TEXT:
                r.append(None)
            elif element.Type == INPUT_TEXT:
                r.append(element.TextInputDefault)
                return_vals.append(None)
            elif element.Type == INPUT_MULTILINE:
                r.append(element.TextInputDefault)
                return_vals.append(None)
            elif element.Type == BUTTON:
                r.append(False)
            elif element.Type == PROGRESS_BAR:
                r.append(None)
            elif element.Type == INPUT_CHECKBOX:
                r.append(element.InitialState)
                return_vals.append(element.InitialState)
            elif element.Type == INPUT_RADIO:
                r.append(element.InitialState)
                return_vals.append(element.InitialState)
            elif element.Type == INPUT_COMBO:
                r.append(element.TextInputDefault)
                return_vals.append(None)
            elif element.Type == INPUT_SPIN:
                r.append(element.TextInputDefault)
                return_vals.append(None)
        results.append(r)
    form.Results=results
    form.ReturnValues = (None, return_vals)
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
def BuildResults(form):
    # Results for elements are:
    #   TEXT - Nothing
    #   INPUT - Read value from TK
    #   Button - Button Text and position as a Tuple

    # Get the initialized results so we don't have to rebuild
    results=form.Results
    button_pressed_text = None
    input_values = []
    for row_num,row in enumerate(form.Rows):
        for col_num, element in enumerate(row.Elements):
            if element.Type == INPUT_TEXT:
                value=element.TKStringVar.get()
                results[row_num][col_num] = value
                input_values.append(value)
            elif element.Type == INPUT_CHECKBOX:
                value=element.TKIntVar.get()
                results[row_num][col_num] = value
                input_values.append(value != 0)
            elif element.Type == INPUT_RADIO:
                RadVar=element.TKIntVar.get()
                this_rowcol = EncodeRadioRowCol(row_num,col_num)
                value = RadVar == this_rowcol
                results[row_num][col_num] = value
                input_values.append(value)
            elif element.Type == BUTTON:
                if results[row_num][col_num] is True:
                    button_pressed_text = element.ButtonText
                    results[row_num][col_num] = False
            elif element.Type == INPUT_COMBO:
                value=element.TKStringVar.get()
                results[row_num][col_num] = value
                input_values.append(value)
            elif element.Type == INPUT_SPIN:
                try:
                    value=element.TKStringVar.get()
                except:
                    value = 0
                results[row_num][col_num] = value
                input_values.append(value)
            elif element.Type == INPUT_MULTILINE:
                try:
                    value=element.TKText.get(1.0, tk.END)
                    element.TKText.delete('1.0', tk.END)
                except:
                    value = None
                results[row_num][col_num] = value
                input_values.append(value)

    return_value = (button_pressed_text,input_values)
    form.ReturnValues = return_value
    form.ResultsBuilt = True
    return return_value


# ------------------------------------------------------------------------------------------------------------------ #
# =====================================   TK CODE STARTS HERE ====================================================== #
# ------------------------------------------------------------------------------------------------------------------ #
def ConvertFlexToTK(MyFlexForm):
    master = MyFlexForm.TKroot
    # only set title on non-tabbed forms
    if not MyFlexForm.IsTabbedForm:
        master.title(MyFlexForm.Title)
    font = MyFlexForm.Font
    InitializeResults(MyFlexForm)
    border_depth = MyFlexForm.BorderDepth if MyFlexForm.BorderDepth is not None else DEFAULT_BORDER_WIDTH
    # --------------------------------------------------------------------------- #
    # ****************  Use FlexForm to build the tkinter window ********** ----- #
    # Building is done row by row.                                                #
    # --------------------------------------------------------------------------- #
    focus_set = False
    ######################### LOOP THROUGH ROWS #########################
    # *********** -------  Loop through ROWS  ------- ***********#
    for row_num, flex_row in enumerate(MyFlexForm.Rows):
        ######################### LOOP THROUGH ELEMENTS ON ROW #########################
        # *********** -------  Loop through ELEMENTS  ------- ***********#
        # *********** Make TK Row                             ***********#
        tk_row_frame = tk.Frame(master)
        for col_num, element in enumerate(flex_row.Elements):
            element.ParentForm = MyFlexForm  # save the button's parent form object
            if MyFlexForm.Font and (element.Font == DEFAULT_FONT or not element.Font):
                font = MyFlexForm.Font
            elif element.Font is not None:
                font = element.Font
            # -------  Determine Auto-Size setting on a cascading basis ------- #
            if element.AutoSizeText is not None:            # if element overide
                auto_size_text = element.AutoSizeText
            elif flex_row.AutoSizeText is not None:         # if Row override
                auto_size_text = flex_row.AutoSizeText
            elif MyFlexForm.AutoSizeText is not None:       # if form override
                auto_size_text = MyFlexForm.AutoSizeText
            else:
                auto_size_text = DEFAULT_AUTOSIZE_TEXT
            # Determine Element size
            element_size = element.Size
            if (element_size == (None, None)):      # user did not specify a size
                element_size = MyFlexForm.DefaultElementSize
            else: auto_size_text = False                # if user has specified a size then it shouldn't autosize
            # Apply scaling... Element scaling is higher priority than form level
            if element.Scale != (None, None):
                element_size = (int(element_size[0] * element.Scale[0]), int(element_size[1] * element.Scale[1]))
            elif MyFlexForm.Scale != (None, None):
                element_size = (int(element_size[0] * MyFlexForm.Scale[0]), int(element_size[1] * MyFlexForm.Scale[1]))
            # -------------------------  TEXT element  ------------------------- #
            element_type = element.Type
            if element_type == TEXT:
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
                tktext_label = tk.Label(tk_row_frame,anchor=tk.NW, textvariable=stringvar, width=width, height=height, justify=tk.LEFT, bd=border_depth, fg=element.TextColor)
                # tktext_label = tk.Label(tk_row_frame,anchor=tk.NW, text=display_text, width=width, height=height, justify=tk.LEFT, bd=border_depth)
                # Set wrap-length for text (in PIXELS) == PAIN IN THE ASS
                wraplen = tktext_label.winfo_reqwidth()  # width of widget in Pixels
                tktext_label.configure(anchor=tk.NW, font=font, wraplen=wraplen*2 )  # set wrap to width of widget
                tktext_label.pack(side=tk.LEFT)
            # -------------------------  BUTTON element  ------------------------- #
            elif element_type == BUTTON:
                element.Location = (row_num, col_num)
                btext = element.ButtonText
                btype = element.BType
                if auto_size_text is False: width=element_size[0]
                else: width = 0
                height=element_size[1]
                lines = btext.split('\n')
                max_line_len = max([len(l) for l in lines])
                num_lines = len(lines)
                if element.ButtonColor != (None, None)and element.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = element.ButtonColor
                elif MyFlexForm.ButtonColor != (None, None) and MyFlexForm.ButtonColor != DEFAULT_BUTTON_COLOR:
                    bc = MyFlexForm.ButtonColor
                else:
                    bc = DEFAULT_BUTTON_COLOR
                if bc == 'Random' or bc == 'random':
                    bc = GetRandomColorPair()
                tkbutton = tk.Button(tk_row_frame, text=btext, width=width, height=height,command=element.ButtonCallBack, justify=tk.LEFT, foreground=bc[0], background=bc[1], bd=border_depth)
                element.TKButton = tkbutton          # not used yet but save the TK button in case
                wraplen = tkbutton.winfo_reqwidth()  # width of widget in Pixels
                tkbutton.configure(wraplength=wraplen, font=font)  # set wrap to width of widget
                tkbutton.pack(side=tk.LEFT,  padx=element.Pad[0], pady=element.Pad[1])
                if not focus_set and btype == CLOSES_WIN:
                    focus_set = True
                    element.TKButton.bind('<Return>', element.ReturnKeyHandler)
                    element.TKButton.focus_set()
                    MyFlexForm.TKroot.focus_force()
            # -------------------------  INPUT (Single Line) element  ------------------------- #
            elif element_type == INPUT_TEXT:
                default_text = element.DefaultText
                element.TKStringVar = tk.StringVar()
                element.TKStringVar.set(default_text)
                element.TKEntry = tk.Entry(tk_row_frame, width=element_size[0], textvariable=element.TKStringVar, bd=border_depth, font=font)
                element.TKEntry.bind('<Return>', element.ReturnKeyHandler)
                element.TKEntry.pack(side=tk.LEFT,padx=element.Pad[0], pady=element.Pad[1])
                if not focus_set:
                    focus_set = True
                    element.TKEntry.focus_set()
            # -------------------------  COMBO BOX (Drop Down) element  ------------------------- #
            elif element_type == INPUT_COMBO:
                max_line_len = max([len(str(l)) for l in element.Values])
                if auto_size_text is False: width=element_size[0]
                else: width = max_line_len
                element.TKStringVar = tk.StringVar()
                element.TKCombo = ttk.Combobox(tk_row_frame, width=width, textvariable=element.TKStringVar,font=font )
                element.TKCombo['values'] = element.Values
                element.TKCombo.pack(side=tk.LEFT,padx=element.Pad[0], pady=element.Pad[1])
                element.TKCombo.current(0)
            # -------------------------  INPUT MULTI LINE element  ------------------------- #
            elif element_type == INPUT_MULTILINE:
                default_text = element.DefaultText
                width, height = element_size
                element.TKText = tk.scrolledtext.ScrolledText(tk_row_frame, width=width, height=height, wrap='word', bd=border_depth,font=font)
                element.TKText.insert(1.0, default_text)                    # set the default text
                element.TKText.pack(side=tk.LEFT,padx=element.Pad[0], pady=element.Pad[1])
                if element.EnterSubmits:
                    element.TKText.bind('<Return>', element.ReturnKeyHandler)
                if not focus_set:
                    focus_set = True
                    element.TKText.focus_set()
            # -------------------------  INPUT CHECKBOX element  ------------------------- #
            elif element_type == INPUT_CHECKBOX:
                width = 0 if auto_size_text else element_size[0]
                default_value = element.InitialState
                element.TKIntVar = tk.IntVar()
                element.TKIntVar.set(default_value)
                element.TKCheckbutton = tk.Checkbutton(tk_row_frame, anchor=tk.NW, text=element.Text, width=width, variable=element.TKIntVar, bd=border_depth, font=font)
                element.TKCheckbutton.pack(side=tk.LEFT,padx=element.Pad[0], pady=element.Pad[1])
            # -------------------------  PROGRESS BAR element  ------------------------- #
            elif element_type == PROGRESS_BAR:
                # save this form because it must be 'updated' (refreshed) solely for the purpose of updating bar
                width = element_size[0]
                fnt = tkinter.font.Font()
                char_width = fnt.measure('A')       # single character width
                progress_length = width*char_width
                progress_width = element_size[1]
                direction = element.Orientation
                if element.BarColor == 'Random' or element.BarColor == 'random':
                    bar_color = GetRandomColorPair()
                elif element.BarColor != (None, None):    # if element has a bar color, use it
                    bar_color = element.BarColor
                else:
                    bar_color = DEFAULT_PROGRESS_BAR_COLOR
                element.TKProgressBar = TKProgressBar(tk_row_frame, element.MaxValue, progress_length, progress_width, orientation=direction, BarColor=bar_color, border_width=element.BorderWidth, relief=element.Relief)
                s = ttk.Style()
                element.TKProgressBar.TKCanvas.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # -------------------------  INPUT RADIO BUTTON element  ------------------------- #
            elif element_type == INPUT_RADIO:
                width = 0 if auto_size_text else element_size[0]
                default_value = element.InitialState
                ID = element.GroupID
                # see if ID has already been placed
                value = EncodeRadioRowCol(row_num, col_num)     # value to set intvar to if this radio is selected
                if ID in MyFlexForm.RadioDict:
                    RadVar = MyFlexForm.RadioDict[ID]
                else:
                    RadVar = tk.IntVar()
                    MyFlexForm.RadioDict[ID] = RadVar
                element.TKIntVar = RadVar                       # store the RadVar in Radio object
                if default_value:                               # if this radio is the one selected, set RadVar to match
                    element.TKIntVar.set(value)
                element.TKRadio = tk.Radiobutton(tk_row_frame, anchor=tk.NW, text=element.Text, width=width,
                                                       variable=element.TKIntVar, value=value, bd=border_depth, font=font)
                element.TKRadio.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # -------------------------  INPUT SPIN Box element  ------------------------- #
            elif element_type == INPUT_SPIN:
                width, height = element_size
                width = 0 if auto_size_text else element_size[0]
                element.TKStringVar = tk.StringVar()
                element.TKSpinBox = tk.Spinbox(tk_row_frame, values=element.Values, textvariable=element.TKStringVar, width=width, bd=border_depth)
                element.TKStringVar.set(element.DefaultValue)
                element.TKSpinBox.configure(font=font)  # set wrap to width of widget
                element.TKSpinBox.pack(side=tk.LEFT, padx=element.Pad[0], pady=element.Pad[1])
                # -------------------------  OUTPUT element  ------------------------- #
            elif element_type == OUTPUT:
                width, height = element_size
                element.TKOut = TKOutput(tk_row_frame, width=width, height=height, bd=border_depth)
        #............................DONE WITH ROW pack the row of widgets ..........................#
        # done with row, pack the row of widgets
        tk_row_frame.grid(row=row_num+2, sticky=tk.W, padx=DEFAULT_MARGINS[0])
        if not MyFlexForm.IsTabbedForm:
            MyFlexForm.TKroot.configure(padx=DEFAULT_MARGINS[0], pady=DEFAULT_MARGINS[1])
        else: MyFlexForm.ParentWindow.configure(padx=DEFAULT_MARGINS[0], pady=DEFAULT_MARGINS[1])
    #....................................... DONE creating and laying out window ..........................#
    if MyFlexForm.IsTabbedForm:
        master = MyFlexForm.ParentWindow
    screen_width = master.winfo_screenwidth()               # get window info to move to middle of screen
    screen_height = master.winfo_screenheight()
    if MyFlexForm.Location != (None, None):
        loc = MyFlexForm.Location
        x,y = MyFlexForm.Location
    else:
        master.update_idletasks()  # don't forget
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
def ShowTabbedForm(title, *args, auto_close=False, auto_close_duration=DEFAULT_AUTOCLOSE_TIME, fav_icon=DEFAULT_WINDOW_ICON):
    global _my_windows

    uber = UberForm()
    root = tk.Tk()
    uber.TKroot = root
    if title is not None:
        root.title(title)
    if not len(args):
        ('******************* SHOW TABBED FORMS ERROR .... no arguments')
        return
    tab_control = ttk.Notebook(root)
    for num,x in enumerate(args):
        form, rows, tab_name = x
        form.AddRows(rows)
        tab = ttk.Frame(tab_control)  # Create tab 1
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
    id = root.after(auto_close_duration * 1000, form.AutoCloseAlarmCallback) if auto_close else 0
    icon = fav_icon if not _my_windows.user_defined_icon else _my_windows.user_defined_icon
    try: uber.TKroot.iconbitmap(icon)
    except: pass

    root.mainloop()

    if id: root.after_cancel(id)
    uber.TKrootDestroyed = True
    return uber.FormReturnValues

# ----====----====----====----====----==== STARTUP TK ====----====----====----====----====----#
def StartupTK(my_flex_form):
    global _my_windows

    ow = _my_windows.NumOpenWindows
    root = tk.Tk() if not ow else tk.Toplevel()
    _my_windows.NumOpenWindows += 1

    my_flex_form.TKroot = root
    # root.protocol("WM_DELETE_WINDOW", MyFlexForm.DestroyedCallback())
    # root.bind('<Destroy>', MyFlexForm.DestroyedCallback())
    ConvertFlexToTK(my_flex_form)
    my_flex_form.SetIcon(my_flex_form.WindowIcon)

    if my_flex_form.AutoClose:
        duration = DEFAULT_AUTOCLOSE_TIME if my_flex_form.AutoCloseDuration is None else my_flex_form.AutoCloseDuration
        my_flex_form.TKAfterID = root.after(duration * 1000, my_flex_form.AutoCloseAlarmCallback)
    if my_flex_form.NonBlocking:
        my_flex_form.TKroot.protocol("WM_WINDOW_DESTROYED", my_flex_form.OnClosingCallback())
        pass
    else:       # it's a blocking form
        my_flex_form.TKroot.mainloop()
        _my_windows.NumOpenWindows -= 1 * (_my_windows.NumOpenWindows != 0)       # decrement if not 0
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

# ------------------------------------------------------------------------------------------------------------------ #
# =====================================   Upper PySimpleGUI ============================================================== #
#   Pre-built dialog boxes for all your needs                                                                        #
# ------------------------------------------------------------------------------------------------------------------ #

# ====================================  MSG BOX =====#
# Display a message wrapping at 60 characters        #
# Exits via an OK button2 press                      #
# Returns nothing                                    #
# ===================================================#
def MsgBox(*args, button_color=None, button_type=MSG_BOX_OK, auto_close=False, auto_close_duration=None, icon=DEFAULT_WINDOW_ICON, line_width=MESSAGE_BOX_LINE_WIDTH, font=None):
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
    with FlexForm(args_to_print[0], auto_size_text=True, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, icon=icon, font=font) as form:
        max_line_total, total_lines = 0,0
        for message in args_to_print:
            # fancy code to check if string and convert if not is not need. Just always convert to string :-)
            # if not isinstance(message, str): message = str(message)
            message = str(message)
            if message.count('\n'):
                message_wrapped = message
            else:
                message_wrapped = textwrap.fill(message, line_width)
            message_wrapped_lines = message_wrapped.count('\n')+1
            longest_line_len = max([len(l) for l in message.split('\n')])
            width_used = min(longest_line_len, line_width)
            max_line_total = max(max_line_total, width_used)
            # height = _GetNumLinesNeeded(message, width_used)
            height = message_wrapped_lines
            form.AddRow(Text(message_wrapped, auto_size_text=True))
            total_lines += height

        pad = max_line_total-15 if max_line_total > 15 else 1
        pad =1
        # show either an OK or Yes/No depending on paramater
        if button_type is MSG_BOX_YES_NO:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), Yes(button_color=button_color), No(
                button_color=button_color))
            (button_text, values) = form.Show()
            return button_text == 'Yes'
        elif button_type is MSG_BOX_CANCELLED:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), SimpleButton('Cancelled', button_color=button_color))
        elif button_type is MSG_BOX_ERROR:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), SimpleButton('ERROR', size=(5, 1), button_color=button_color))
        elif button_type is MSG_BOX_OK_CANCEL:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), SimpleButton('OK', size=(5, 1), button_color=button_color),
                        SimpleButton('Cancel', size=(5, 1), button_color=button_color))
        else:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), SimpleButton('OK', size=(5, 1), button_color=button_color))

        button, values = form.Show()
    return button

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
    MsgBox(*args, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)
    return


# ==============================  MsgBoxError   =====#
# Like MsgBox but presents RED BUTTONS               #
# ===================================================#
def MsgBoxError(*args, button_color=DEFAULT_ERROR_BUTTON_COLOR, auto_close=False, auto_close_duration=None, Font=None):
    '''
    Display a MsgBox with a red button
    :param args:
    :param button_color:
    :param auto_close:
    :param auto_close_duration:
    :param Font:
    :return:
    '''
    MsgBox(*args, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=Font)
    return

# ==============================  MsgBoxCancel  =====#
#                                                    #
# ===================================================#
def MsgBoxCancel(*args, button_color=DEFAULT_CANCEL_BUTTON_COLOR, auto_close=False, auto_close_duration=None, font=None):
    '''
    Display a MsgBox with a single "Cancel" button.
    :param args:
    :param button_color:
    :param auto_close:
    :param auto_close_duration:
    :param font:
    :return:
    '''
    MsgBox(*args, button_type=MSG_BOX_CANCELLED, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)
    return

# ==============================  MsgBoxOK      =====#
# Like MsgBox but only 1 button                      #
# ===================================================#
def MsgBoxOK(*args, button_color=('white', 'black'), auto_close=False, auto_close_duration=None, font=None):
    '''
    Display a MsgBox with a single buttoned labelled "OK"
    :param args:
    :param button_color:
    :param auto_close:
    :param auto_close_duration:
    :param font:
    :return:
    '''
    MsgBox(*args, button_type=MSG_BOX_OK, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)
    return

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
    result = MsgBox(*args, button_type=MSG_BOX_OK_CANCEL, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration, font=font)
    return result

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
        width_used = min(longest_line_len, MESSAGE_BOX_LINE_WIDTH)
        max_line_total = max(max_line_total, width_used)
        lines_needed = _GetNumLinesNeeded(message, width_used)
        total_lines += lines_needed
        single_line_message += message + '\n'
    return single_line_message, width_used, total_lines


# ============================== ProgressMeter  =====#
# ===================================================#
def ProgressMeter(title, max_value, *args, Orientation=None, bar_color=DEFAULT_PROGRESS_BAR_COLOR, button_color=None, size=DEFAULT_PROGRESS_BAR_SIZE, scale=(None, None), border_width=DEFAULT_PROGRESS_BAR_BORDER_WIDTH):
    '''
    Create and show a form on tbe caller's behalf.
    :param title:
    :param max_value:
    :param args: ANY number of arguments the caller wants to display
    :param Orientation:
    :param bar_color:
    :param size:
    :param scale:
    :param Style:
    :param StyleOffset:
    :return: ProgressBar object that is in the form
    '''
    orientation = DEFAULT_METER_ORIENTATION if Orientation is None else Orientation
    target = (0,0) if orientation[0].lower() == 'h' else (0,1)
    bar2 = ProgressBar(max_value, orientation=orientation, size=size, bar_color=bar_color, scale=scale, target=target, broder_width=border_width)
    form = FlexForm(title, auto_size_text=True)

    # Form using a horizontal bar
    if orientation[0].lower() == 'h':
        single_line_message, width, height = ConvertArgsToSingleString(*args)
        bar2.TextToDisplay = single_line_message
        bar2.MaxValue = max_value
        bar2.CurrentValue = 0
        form.AddRow(Text(single_line_message, size=(width + 20, height + 3), auto_size_text=True))
        form.AddRow((bar2))
        form.AddRow((Cancel(button_color=button_color)))
    else:
        single_line_message, width, height = ConvertArgsToSingleString(*args)
        bar2.TextToDisplay = single_line_message
        bar2.MaxValue = max_value
        bar2.CurrentValue = 0
        form.AddRow(bar2, Text(single_line_message, size=(width + 20, height + 3), auto_size_text=True))
        form.AddRow((Cancel(button_color=button_color)))

    form.NonBlocking = True
    form.Show(non_blocking= True)
    return bar2

# ============================== ProgressMeterUpdate  =====#
def ProgressMeterUpdate(bar, value, *args):
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


    bar.TextToDisplay = message
    bar.CurrentValue = value
    rc = bar.UpdateBar(value)
    if value >= bar.MaxValue or not rc:
        bar.BarExpired = True
        bar.ParentForm.Close()
    if bar.ParentForm.RootNeedsDestroying:
        try:
            bar.ParentForm.TKroot.destroy()
            _my_windows.NumOpenWindows -= 1 * (_my_windows.NumOpenWindows != 0)  # decrement if not 0
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
def EasyProgressMeter(title, current_value, max_value, *args, orientation=None, bar_color=DEFAULT_PROGRESS_BAR_COLOR, button_color=None, size=DEFAULT_PROGRESS_BAR_SIZE, scale=(None, None), border_width=DEFAULT_PROGRESS_BAR_BORDER_WIDTH):
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
        EasyProgressMeter.EasyProgressMeterData.MeterID = ProgressMeter(title, int(max_value), message, *args, Orientation=orientation, bar_color=bar_color, size=size, scale=scale, button_color=button_color, border_width=border_width)
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
    rc = ProgressMeterUpdate(EasyProgressMeter.EasyProgressMeterData.MeterID, current_value, *args, message)
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


def GetRandomColor():
    nums = randint(0,255), randint(0,255), randint(0,255)
    color_code ='#' + ''.join('{:02X}'.format(a) for a in nums)
    return color_code


def GetRandomColorPair():
    fg = GetRandomColor()
    bg = GetComplimentaryHex(fg)
    color_code = (fg, bg)
    return color_code

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
    # return the result
    return comp_color

# ========================  Scrolled Text Box   =====#
# ===================================================#
def ScrolledTextBox(*args, button_color=None, yes_no=False, auto_close=False, auto_close_duration=None, height=None):
    if not args: return
    with FlexForm(args[0], auto_size_text=True, button_color=button_color, auto_close=auto_close, auto_close_duration=auto_close_duration) as form:
        max_line_total, max_line_width, total_lines, height_computed = 0,0,0,0
        complete_output = ''
        for message in args:
            # fancy code to check if string and convert if not is not need. Just always convert to string :-)
            # if not isinstance(message, str): message = str(message)
            message = str(message)
            longest_line_len = max([len(l) for l in message.split('\n')])
            width_used = min(longest_line_len, MESSAGE_BOX_LINE_WIDTH)
            max_line_total = max(max_line_total, width_used)
            max_line_width = MESSAGE_BOX_LINE_WIDTH
            lines_needed = _GetNumLinesNeeded(message, width_used)
            height_computed += lines_needed
            complete_output += message + '\n'
            total_lines += lines_needed
        height_computed = MAX_SCROLLED_TEXT_BOX_HEIGHT if height_computed > MAX_SCROLLED_TEXT_BOX_HEIGHT else height_computed
        if height:
            height_computed = height
        form.AddRow(Multiline(complete_output, size=(max_line_width, height_computed)), auto_size_text=True)
        pad = max_line_total-15 if max_line_total > 15 else 1
        # show either an OK or Yes/No depending on paramater
        if yes_no:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), Yes(), No())
            (button_text, values) = form.Show()
            return button_text == 'Yes'
        else:
            form.AddRow(Text('', size=(pad, 1), auto_size_text=False), SimpleButton('OK', size=(5, 1), button_color=button_color))
        form.Show()


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

        (button, input_values) = form.LayoutAndShow(layout)
        if button != 'Submit':
            return False,None
        else:
            path = input_values[0]
            return True, path

# ============================== GetFileBox =========#
# Like the Get folder box but for files              #
# ===================================================#
def GetFileBox(title, message, default_path='', file_types=(("ALL Files", "*.*"),), button_color=None, size=(None, None)):
    with FlexForm(title, auto_size_text=True, button_color=button_color) as form:
        layout = [[Text(message, auto_size_text=True)],
                  [InputText(default_text=default_path, size=size), FileBrowse(file_types=file_types)],
                  [Submit(), Cancel()]]

        (button, input_values) = form.LayoutAndShow(layout)
        if button != 'Submit':
            return False,None
        else:
            path = input_values[0]
            return True, path


# ============================== GetTextBox =========#
# Get a single line of text                          #
# ===================================================#
def GetTextBox(title, message, Default='', button_color=None, size=(None, None)):
    with FlexForm(title, auto_size_text=True, button_color=button_color) as form:
        layout = [[Text(message, auto_size_text=True)],
                  [InputText(default_text=Default, size=size)],
                  [Submit(), Cancel()]]

        (button, input_values) = form.LayoutAndShow(layout)
        if button != 'Submit':
            return False,None
        else:
            return True, input_values[0]


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


# ============================== SetButtonColor =====#
# Sets the defaul button color                       #
# ===================================================#
def SetButtonColor(foreground, background):
    global DEFAULT_BUTTON_COLOR

    DEFAULT_BUTTON_COLOR = (foreground, background)


# ============================== sprint ======#
# Is identical to the Scrolled Text Box       #
# Provides a crude 'print' mechanism but in a #
# GUI environment                             #
# ============================================#
sprint=ScrolledTextBox
