import PySimpleGUI as gui

layout = [
           [gui.Canvas(size=(100,100), background_color='red', key='canvas')],
           [gui.T('Change circle color to:'), gui.ReadFormButton('Red'), gui.ReadFormButton('Blue')]
           ]

form = gui.FlexForm('Canvas test')
form.Layout(layout)
form.Finalize()

cir = form.FindElement('canvas').TKCanvas.create_oval(50, 50, 100, 100)

while True:
    button, values = form.Read()
    if button is None:
        break
    if button is 'Blue':
        form.FindElement('canvas').TKCanvas.itemconfig(cir, fill = "Blue")
    elif button is 'Red':
        form.FindElement('canvas').TKCanvas.itemconfig(cir, fill = "Red")
