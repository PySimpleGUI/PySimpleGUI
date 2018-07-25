import PySimpleGUI as SG
import subprocess
import howdoi

# Test this command in a dos window if you are having trouble.
HOW_DO_I_COMMAND =  'python -m howdoi.howdoi'

# if you want an icon on your taskbar for this gui, then change this line of code to point to the ICO file
DEFAULT_ICON = 'E:\\TheRealMyDocs\\Icons\\QuestionMark.ico'

def HowDoI():
    '''
    Make and show a window (PySimpleGUI form) that takes user input and sends to the HowDoI web oracle
    Excellent example of 2 GUI concepts
        1. Output Element that will show text in a scrolled window
        2. Non-Window-Closing Buttons - These buttons will cause the form to return with the form's values, but doesn't close the form
    :return: never returns
    '''
    # -------  Make a new FlexForm  ------- #
    SG.SetOptions(border_width=1)
    form = SG.FlexForm('How Do I ??', auto_size_text=True, default_element_size=(30, 2), icon=DEFAULT_ICON)
    form.AddRow(SG.Text('Ask and your answer will appear here....', size=(40, 1)))
    form.AddRow(SG.Output(size=(90, 20)))
    form.AddRow(SG.Multiline(size=(85, 5), enter_submits=True),
                SG.ReadFormButton('SEND', button_color=(SG.YELLOWS[0], SG.BLUES[0])),
                SG.SimpleButton('EXIT', button_color=(SG.YELLOWS[0], SG.GREENS[0])))

    # ---===--- Loop taking in user input and using it to query HowDoI --- #
    while True:
        (button, value) = form.Read()
        if button == 'SEND':
            QueryHowDoI(value[0][:-1])      # send string without carriage return on end
        else:
            break           # exit button clicked

    exit(69)

def QueryHowDoI(Query):
    '''
    Kicks off a subprocess to send the 'Query' to HowDoI
    Prints the result, which in this program will route to a gooeyGUI window
    :param Query: text english question to ask the HowDoI web engine
    :return: nothing
    '''
    howdoi_command = HOW_DO_I_COMMAND
    t = subprocess.Popen(howdoi_command + ' '+ Query, stdout=subprocess.PIPE)
    (output, err) = t.communicate()
    print('You asked: '+ Query)
    print('_______________________________________')
    print(output.decode("utf-8") )
    exit_code = t.wait()

if __name__ == '__main__':
    HowDoI()

