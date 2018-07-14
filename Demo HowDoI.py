import PySimpleGUI as SG
import subprocess

# CHANGE THIS LINE OF CODE!  Point it to the howdoi.py file that is in the howdoi code you download from github
HOW_DO_I_COMMAND = 'python C:\\Python\\PycharmProjects\\GitHub\\howdoi\\howdoi\\howdoi.py'
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
    form = SG.FlexForm('How Do I ??', AutoSizeText=True, DefaultElementSize=(30, 2), Icon=DEFAULT_ICON)
    form.AddRow(SG.Text('Ask and your answer will appear here....', Size=(40, 1)))
    form.AddRow(SG.Output(Size=(90, 20)))
    form.AddRow(SG.Multiline(Size=(90, 5), EnterSubmits=True),
                SG.ReadFormButton('SEND', ButtonColor=(SG.YELLOWS[0], SG.BLUES[0])),
                SG.SimpleButton('EXIT', ButtonColor=(SG.YELLOWS[0], SG.GREENS[0])))

    # ---===--- Loop taking in user input and using it to query HowDoI web oracle --- #
    while True:
        (button, value) = form.Read()
        if button == 'SEND':
            command = value[0][:-1]
            QueryHowDoI(command)
        else:
            print(button, 'pressed')
            break

    print('Exiting the app now')
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

