import time
from random import randint
import random
import string
import PySimpleGUI as SG

# A simple blocking form.   Your best starter-form
def SourceDestFolders():
    with SG.FlexForm('Demo Source / Destination Folders', auto_size_text=True) as form:
        form_rows = [[SG.Text('Enter the Source and Destination folders')],
                     [SG.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), SG.InputText('Source')],
                     [SG.Text('Destination Folder', size=(15, 1), auto_size_text=False, justification='right'), SG.InputText('Dest'), SG.FolderBrowse()],
                     [SG.Submit(), SG.Cancel()]]

        button, (source, dest) = form.LayoutAndRead(form_rows)
    if button == 'Submit':
        SG.MsgBox('Submitted', 'The user entered source:', source, 'Destination folder:', dest, 'Using button', button)
    else:
        SG.MsgBoxError('Cancelled', 'User Cancelled')

# YOUR BEST STARTING POINT
# This is a form showing you all of the basic Elements (widgets)
# Some have a few of the optional parameters set, but there are more to choose from
# You want to use the context manager because it will free up resources when you are finished
# Use this especially if you are runningm multi-threaded
# Where you free up resources is really important to tkinter
def Everything():
    with SG.FlexForm('Everything bagel', auto_size_text=True, default_element_size=(40, 1)) as form:
        layout = [
            [SG.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
            [SG.Text('Here is some text.... and a place to enter text')],
            [SG.InputText()],
            [SG.Checkbox('My first checkbox!'), SG.Checkbox('My second checkbox!', default=True)],
            [SG.Radio('My first Radio!     ', "RADIO1", default=True), SG.Radio('My second Radio!', "RADIO1")],
            [SG.Multiline(default_text='This is the default Text shoulsd you decide not to type anything',
                          scale=(2, 10))],
            [SG.InputCombo(['Combobox 1', 'Combobox 2'], size=(20, 3)),
             SG.Slider(range=(1, 100), orientation='h', size=(35, 20), default_value=85)],
            [SG.Listbox(values=['Listbox 1', 'Listbox 2', 'Listbox 3'], size=(30, 6)),
             SG.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=25),
             SG.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=75),
             SG.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=10)],
            [SG.Text('_' * 100, size=(70, 1))],
            [SG.Text('Choose Source and Destination Folders', size=(35, 1))],
            [SG.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), SG.InputText('Source'), SG.FolderBrowse()],
            [SG.Text('Destination Folder', size=(15, 1), auto_size_text=False, justification='right'), SG.InputText('Dest'),
             SG.FolderBrowse()],
            [SG.Submit(), SG.Cancel(), SG.SimpleButton('Customized', button_color=('white', 'green'))]
             ]

        button, values = form.LayoutAndRead(layout)

    SG.MsgBox('Title', 'Typical message box', 'The results of the form are a lot of data!  Get ready... ', 'The button clicked was "{}"'.format(button), 'The values are', values)

# Should you decide not to use a context manager, then try this form as your starting point
# Be aware that tkinter, which this is based on, is picky about who frees up resources, especially if
# you are running multithreaded
def Everything_NoContextManager():
    form = SG.FlexForm('Everything bagel', auto_size_text=True, default_element_size=(40, 1))
    layout = [[SG.Text('All graphic widgets in one form!', size=(30, 1), font=("Helvetica", 25), text_color='blue')],
              [SG.Text('Here is some text.... and a place to enter text')],
              [SG.InputText()],
              [SG.Checkbox('My first checkbox!'), SG.Checkbox('My second checkbox!', default=True)],
              [SG.Radio('My first Radio!     ', "RADIO1", default=True), SG.Radio('My second Radio!', "RADIO1")],
              [SG.Multiline(default_text='This is the default Text shoulsd you decide not to type anything', scale=(2, 10))],
              [SG.InputCombo(['Combobox 1', 'Combobox 2'], size=(20, 3)), SG.Slider(range=(1,100), orientation='h', size=(35,20), default_value=85)],
              [SG.Listbox(values=['Listbox 1','Listbox 2', 'Listbox 3'], size=(30,6)),
               SG.Slider(range=(1,100), orientation='v', size=(10, 20), default_value=25),
               SG.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=75),
               SG.Slider(range=(1, 100), orientation='v', size=(10, 20), default_value=10)],
              [SG.Text('_' * 100, size=(70, 1))],
              [SG.Text('Choose Source and Destination Folders', size=(35, 1), text_color='red')],
              [SG.Text('Source Folder', size=(15, 1), auto_size_text=False, justification='right'), SG.InputText('Source'), SG.FolderBrowse()],
              [SG.Text('Destination Folder', size=(15, 1), auto_size_text=False,  justification='right'), SG.InputText('Dest'), SG.FolderBrowse()],
              [SG.Submit(), SG.Cancel(), SG.SimpleButton('Customized', button_color=('white', 'green'))]]

    button, values = form.LayoutAndRead(layout)
    del(form)

    SG.MsgBox('Title', 'Typical message box', 'Here are the restults!  There is one entry per input field ', 'The button clicked was "{}"'.format(button), 'The values are', values)

def ProgressMeter():
    for i in range(1,10000):
        if not SG.EasyProgressMeter('My Meter', i+1, 10000): break
        # SG.Print(i)

# Blocking form that doesn't close
def ChatBot():
    with SG.FlexForm('Chat Window', auto_size_text=True, default_element_size=(30, 2)) as form:
        layout = [[(SG.Text('This is where standard out is being routed', size=[40, 1]))],
                    [SG.Output(size=(80, 20))],
                    [SG.Multiline(size=(70, 5), enter_submits=True), SG.ReadFormButton('SEND', button_color=(SG.YELLOWS[0], SG.BLUES[0])), SG.SimpleButton('EXIT', button_color=(SG.YELLOWS[0], SG.GREENS[0]))]]
        # notice this is NOT the usual LayoutAndRead call because you don't yet want to read the form
        # if you call LayoutAndRead from here, then you will miss the first button click
        form.Layout(layout)
        # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
        while True:
            button, value = form.Read()
            if button == 'SEND':
                print(value)
            else:
                break

# Shows a form that's a running counter
# this is the basic design pattern if you can keep your reading of the
# form within the 'with' block.  If your read occurs far away in your code from the form creation
# then you will want to use the NonBlockingPeriodicUpdateForm example
def NonBlockingPeriodicUpdateForm_ContextManager():
    with SG.FlexForm('Running Timer', auto_size_text=True) as form:
        text_element = SG.Text('',size=(10,2), font=('Helvetica', 20), text_color='red', justification='center')
        layout = [[SG.Text('Non blocking GUI with updates', justification='center')],
                     [text_element],
                     [SG.T(' '*15), SG.Quit()]]
        form.LayoutAndRead(layout, non_blocking=True)

        for i in range(1,500):
            text_element.Update('{:02d}:{:02d}.{:02d}'.format(*divmod(int(i/100), 60), i%100))
            button, values = form.ReadNonBlocking()
            if values is None or button == 'Quit':      # if user closed the window using X
                break
            time.sleep(.01)
        else:
            # if the loop finished then need to close the form for the user
            form.CloseNonBlockingForm()

# Use this context-manager-free version if your read of the form occurs far away in your code
# from the form creation (call to LayoutAndRead)
def NonBlockingPeriodicUpdateForm():
    # Show a form that's a running counter
    form = SG.FlexForm('Running Timer', auto_size_text=True)
    text_element = SG.Text('',size=(10,2), font=('Helvetica', 20), justification='center')
    form_rows = [[SG.Text('Non blocking GUI with updates')],
                 [text_element],
                 [SG.T(' ' * 15), SG.Quit()]]
    form.LayoutAndRead(form_rows, non_blocking=True)

    for i in range(1,50000):
        text_element.Update(f'{(i//100)//60:02d}:{(i//100)%60:02d}.{i%100:02d}')
        button, values = form.ReadNonBlocking()
        if values is None or button == 'Quit':      # if user closed the window using X or clicked Quit button
            break
        time.sleep(.01)
    else:
        # if the loop finished then need to close the form for the user
        form.CloseNonBlockingForm()
    del(form)

def DebugTest():
    # SG.Print('How about we print a bunch of random numbers?', , size=(90,40))
    for i in range (1,300):
        SG.Print(i, randint(1, 1000), end='', sep='-')


def main():
    # SG.SetOptions(border_width=1, font=("Helvetica", 10), button_color=('white', SG.BLUES[0]), slider_border_width=1)
    Everything_NoContextManager()
    Everything()
    NonBlockingPeriodicUpdateForm_ContextManager()
    NonBlockingPeriodicUpdateForm()
    ChatBot()
    Everything()
    ProgressMeter()
    SourceDestFolders()
    ChatBot()
    DebugTest()
    SG.MsgBox('Done with all recipes')

if __name__ == '__main__':
    main()
    exit(69)
