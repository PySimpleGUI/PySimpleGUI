import PySimpleGUI as g

def SourceDestFolders():
    with g.FlexForm('Demo Source / Destination Folders', auto_size_text=True) as form:
        form_rows = [[g.Text('Enter the Source and Destination folders')],
                     [g.Text('Choose Source and Destination Folders')],
                     [g.Text('Source Folder', size=(15, 1), auto_size_text=False), g.InputText('Source'),
                      g.FolderBrowse()],
                     [g.Text('Destination Folder', size=(15, 1), auto_size_text=False), g.InputText('Dest'),
                      g.FolderBrowse()],
                     [g.Submit(), g.Cancel()]]

        (button, (source, dest)) = form.LayoutAndShow(form_rows)
    if button == 'Submit':
        # do something useful with the inputs
        g.MsgBox('Submitted', 'The user entered source folder', source, 'And destination folder', dest)
    else:
        g.MsgBoxError('Cancelled', 'User Cancelled')

def Everything():
    with g.FlexForm('Everything bagel', auto_size_text=True, default_element_size=(40,1)) as form:
        layout = [[g.Text('All graphic widgets in one form!', size=(30,1), font=("Helvetica", 25), text_color='blue')],
              [g.Text('Here is some text.... and a place to enter text')],
              [g.InputText()],
              [g.Checkbox('My first checkbox!'), g.Checkbox('My second checkbox!', default=True)],
              [g.Radio('My first Radio!', "RADIO1", default=True), g.Radio('My second Radio!', "RADIO1")],
              [g.Multiline(default_text='This is the default Text should you decide not to type anything', scale=(2,10))],
              [g.InputCombo(['choice 1', 'choice 2'], size=(20,3))],
              [g.Text('_' * 100, size=(70,1))],
              [g.Text('Choose Source and Destination Folders', size=(35,1))],
              [g.Text('Source Folder', size=(15,1), auto_size_text=False), g.InputText('Source'), g.FolderBrowse()],
              [g.Text('Destination Folder', size=(15,1), auto_size_text=False), g.InputText('Dest'), g.FolderBrowse()],
              [g.SimpleButton('Your very own button', button_color=('white', 'green'))],
              [g.Submit(), g.Cancel()]]

        (button, (values)) = form.LayoutAndShow(layout)

    g.MsgBox('Title', 'Typical message box', 'The results of the form are a lot of data!  Get ready... ', 'The button clicked was "{}"'.format(button), 'The values are', values, auto_close=True)

# example of an Asynchronous form
def ChatBot():
    with g.FlexForm('Chat Window', auto_size_text=True, default_element_size=(30, 2)) as form:
        form.AddRow(g.Text('This is where standard out is being routed', size=[40,1]))
        form.AddRow(g.Output(size=(80, 20)))
        form.AddRow(g.Multiline(size=(70, 5), enter_submits=True), g.ReadFormButton('SEND', button_color=(g.YELLOWS[0], g.BLUES[0])), g.SimpleButton('EXIT', button_color=(g.YELLOWS[0], g.GREENS[0])))

        # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
        while True:
            (button, value) = form.Read()
            if button == 'SEND':
                print(value, end="")
            else:
                break

def main():
    SourceDestFolders()
    Everything()
    ChatBot()

if __name__ == '__main__':
    main()
