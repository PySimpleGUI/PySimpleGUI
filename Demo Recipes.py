import PySimpleGUI as g

def SourceDestFolders():
    with g.FlexForm('Demo Source / Destination Folders', AutoSizeText=True) as form:
        form_rows = [[g.Text('Enter the Source and Destination folders')],
                     [g.Text('Choose Source and Destination Folders')],
                     [g.Text('Source Folder', Size=(15, 1), AutoSizeText=False), g.InputText('Source'),
                      g.FolderBrowse()],
                     [g.Text('Destination Folder', Size=(15, 1), AutoSizeText=False), g.InputText('Dest'),
                      g.FolderBrowse()],
                     [g.Submit(), g.Cancel()]]

        (button, (source, dest)) = form.LayoutAndShow(form_rows)
    if button == 'Submit':
        # do something useful with the inputs
        g.MsgBox('Submitted', 'The user entered source folder', source, 'And destination folder', dest)
    else:
        g.MsgBoxError('Cancelled', 'User Cancelled')

def Everything():
    with g.FlexForm('Everything bagel', AutoSizeText=True, DefaultElementSize=(40,1)) as form:
        layout = [[g.Text('All graphic widgets in one form!', Size=(30,1), Font=("Helvetica", 25))],
              [g.Text('Here is some text.... and a place to enter text')],
              [g.InputText()],
              [g.Checkbox('My first checkbox!'), g.Checkbox('My second checkbox!', Default=True)],
              [g.Radio('My first Radio!', "RADIO1", Default=True), g.Radio('My second Radio!', "RADIO1")],
              [g.Multiline(DefaultText='This is the DEFAULT Text should you decide not to type anything', Scale=(2, 10))],
              [g.InputCombo(['choice 1', 'choice 2'], Size=(20, 3))],
              [g.Text('_' * 100, Size=(90, 1))],
              [g.Text('Choose Source and Destination Folders', Size=(35,1))],
              [g.Text('Source Folder', Size=(15, 1), AutoSizeText=False), g.InputText('Source'), g.FolderBrowse()],
              [g.Text('Destination Folder', Size=(15, 1), AutoSizeText=False), g.InputText('Dest'), g.FolderBrowse()],
              [g.SimpleButton('Your very own button')],
              [g.Submit(), g.Cancel()]]

        (button, (values)) = form.LayoutAndShow(layout)

    g.MsgBox('Title', 'Typical message box', 'The results of the form are a lot of data!  Get ready... ', 'The button clicked was "{}"'.format(button), 'The values are', values)

# example of an Asynchronous form
def ChatBot():
    with g.FlexForm('Chat Window', AutoSizeText=True, DefaultElementSize=(30, 2)) as form:
        form.AddRow(g.Text('This is where standard out is being routed', Size=[40,1]))
        form.AddRow(g.Output(Size=(80, 20)))
        form.AddRow(g.Multiline(Size=(70, 5), EnterSubmits=True), g.ReadFormButton('SEND', ButtonColor=(g.YELLOWS[0], g.BLUES[0])), g.SimpleButton('EXIT', ButtonColor=(g.YELLOWS[0], g.GREENS[0])))

        # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
        while True:
            (button, value) = form.Read()
            if button == 'SEND':
                print(value)
            else:
                print('Exiting the form now')
                break
    print('Exiting the chatbot....')

def main():
    SourceDestFolders()
    Everything()
    ChatBot()

if __name__ == '__main__':
    main()
