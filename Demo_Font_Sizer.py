
# Testing async form, see if can have a spinner
# that adjusts the size of text displayed

import PySimpleGUI as sg

form = sg.FlexForm("Font size selector")

fontSize = 12
sampleText = sg.Text("Aa", size=(2, 1), font="Helvetica " + str(fontSize))
layout = [
          [sampleText, sg.Spin([sz for sz in range(4,72)], font=('Helvetica 20'), initial_value=fontSize, change_submits=True, key='spin')],
          [sg.OK(), sg.Cancel()]
         ]

sz = fontSize
form.Layout(layout)
while True:
    button, values= form.Read()
    if button is None:
        break
    sz = int(values['spin'])
    if sz != fontSize:
        fontSize = sz
        font = "Helvetica " + str(fontSize)
        sampleText.Update(font=font)

print("Done.")
