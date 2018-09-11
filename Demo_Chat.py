import PySimpleGUI as sg

'''
A chat window.  Add call to your send-routine, print the response and you're done
'''

# -------  Make a new FlexForm  ------- #
sg.ChangeLookAndFeel('GreenTan')            # give our form a spiffy set of colors

form = sg.FlexForm('Chat window', default_element_size=(30, 2), font=('Helvetica',' 13'), default_button_element_size=(8,2))

layout =  [
            [sg.Text('Your output will go here', size=(40, 1))],
            [sg.Output(size=(127, 30), font=('Helvetica 10'))],
            [sg.Multiline(size=(85, 5), enter_submits=True, key='query'),
            sg.ReadFormButton('SEND', button_color=(sg.YELLOWS[0], sg.BLUES[0]), bind_return_key=True),
            sg.SimpleButton('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]
          ]
form.Layout(layout)

# ---===--- Loop taking in user input and using it  --- #
while True:
    (button, value) = form.Read()
    if button is 'SEND':
        query = value['query'].rstrip()
        # EXECUTE YOUR COMMAND HERE
        print('The command you entered was {}'.format(query))
    elif button is None or button is 'EXIT':            # quit if exit button or X
        break
exit(69)

