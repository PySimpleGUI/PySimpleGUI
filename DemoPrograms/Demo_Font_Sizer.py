import PySimpleGUI as sg

# Testing async form, see if can have a slider
# that adjusts the size of text displayed

fontSize = 12
layout = [
    [sg.Spin([sz for sz in range(6, 172)],
             font=('Helvetica 20'),
             initial_value=fontSize,
             change_submits=True, key='spin'),
     sg.Slider(range=(6, 172), orientation='h', size=(10, 20), change_submits=True, key='slider',
               font=('Helvetica 20')),
     sg.Text("Aa", size=(2, 1), font="Helvetica " + str(fontSize), key='text')]
]
sz = fontSize
window = sg.Window("Font size selector", layout, grab_anywhere=False)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    sz_spin = int(values['spin'])
    sz_slider = int(values['slider'])

    sz = sz_spin if sz_spin != fontSize else sz_slider

    if sz != fontSize:
        fontSize = sz
        font = "Helvetica " + str(fontSize)
        window['text'].update(font=font)
        window['slider'].update(sz)
        window['spin'].update(sz)

window.close()
