
# Testing async form, see if can have a slider
# that adjusts the size of text displayed

import PySimpleGUI as sg

form = sg.FlexForm("Font size selector")

fontSize = 12

layout = [
          [sg.Text("Aa", size=(2, 1), font="Helvetica " + str(fontSize), key='text'),
           sg.Spin([sz for sz in range(6, 72)], font=('Helvetica 20'), initial_value=fontSize, change_submits=True,
                   key='spin'), sg.Slider(range=(6,50), orientation='h', size=(10,20), change_submits=True, key='slider')],
          [sg.OK(), sg.Cancel()]
         ]

sz = fontSize
form.Layout(layout)
while True:
    button, values= form.Read()
    if button in (None, 'OK', 'Cancel'):
        break
    sz_spin = int(values['spin'])
    sz_slider = int(values['slider'])
    sz = sz_spin if sz_spin != fontSize else sz_slider
    if sz != fontSize:
        fontSize = sz
        font = "Helvetica " + str(fontSize)
        form.FindElement('text').Update(font=font)
        form.FindElement('slider').Update(sz)
        form.FindElement('spin').Update(sz)

print("Done.")
