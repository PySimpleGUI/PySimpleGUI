import PySimpleGUIWeb as sg

"""
Simple Demo that shows how Elements can effect other elements in the Window
In this case, the slider controls the size of the text font and the value shown in the spinner
Additionally, if the spinner is changed, the text size is changed and so is the slider
In other words, the slider and the spinner are essentially connected together
"""

fontsize = 12       # initial and smallest font size to show

layout = [[sg.Spin([sz for sz in range(6, 172)], size=(6,1), font=('Helvetica 20'), initial_value=fontsize, change_submits=True, key='spin'),
           sg.Slider(range=(6,172), orientation='h', size=(10,20), change_submits=True, key='slider', font=('Helvetica 20')),
           sg.Text("Aa", size=(2, 1), font="Helvetica " + str(fontsize), key='text')],]

window = sg.Window("Font size selector").Layout(layout)

while True:         # the event loop
    event, values= window.Read()
    if event is None or event == 'Quit':
        break
    fontsize = int(values['spin']) if int(values['spin']) != fontsize else int(values['slider'])
    font = "Helvetica " + str(fontsize)
    window.FindElement('text').Update(font=font)
    window.FindElement('slider').Update(fontsize, range=(10,20))
    window.FindElement('spin').Update(fontsize)
window.Close()

print("Done.")
