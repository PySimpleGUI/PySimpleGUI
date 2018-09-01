
# Testing async form, see if can have a slider
# that adjusts the size of text displayed

import PySimpleGUI as sg

form = sg.FlexForm("Font size selector")

fontSize = 12
sampleText = sg.Text("Aa", size=(2, 1), font="Helvetica " + str(fontSize))
slider = sg.Slider(range=(6,50), orientation='h', size=(10,20), change_submits=True, key='slider')
spin = sg.Spin([sz for sz in range(4,72)], font=('Helvetica 20'), initial_value=fontSize, change_submits=True, key='spin')
layout = [
          [sampleText, spin, slider],
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
        print(sampleText.Font, sampleText.Size)
        fontSize = sz
        font = "Helvetica " + str(fontSize)
        sampleText.Update(font=font)
        slider.Update(sz)
        spin.Update(sz)

print("Done.")
