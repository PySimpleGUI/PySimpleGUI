import PySimpleGUIWeb as sg

"""
Simple Demo that shows how Elements can effect other elements in the Window
In this case, the slider controls the size of the text font and the value shown in the spinner
Additionally, if the spinner is changed, the text size is changed and so is the slider
In other words, the slider and the spinner are essentially connected together
"""

fontsize = 12       # initial and smallest font size to show

layout = [
        [sg.Spin([sz for sz in range(6, 172)], size=(6, 1),
            font=('Helvetica 20'), initial_value=fontsize,
            change_submits=True, key='spin'),
           sg.Slider(range=(6, 172), orientation='h', size=(10, 20),
                     change_submits=True, key='slider', font=('Helvetica 20')),
           sg.Text("Aa", size=(2, 1), font="Helvetica " + str(fontsize), key='text')]
    ]

window = sg.Window("Font size selector", layout)

while True:         # the event loop
    event, values = window.read()
    if event is None or event == 'Quit':
        break
    
    if int(values['spin']) != fontsize:
        fontsize = int(values['spin'])
    else:
        fontsize = int(values['slider'])
    
    window['text'].update(font="Helvetica " + str(fontsize))
    window['slider'].update(fontsize, range=(10, 20))
    window['spin'].update(fontsize)
window.close()

print("Done.")
