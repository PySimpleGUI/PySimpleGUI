import PySimpleGUI as gui

canvas = gui.Canvas(size=(100,100), background_color='red')

layout = [
           [canvas],
           [gui.T('Change circle color to:'), gui.ReadFormButton('Red'), gui.ReadFormButton('Blue')]
           ]

form = gui.FlexForm('Canvas test')
form.Layout(layout)
form.ReadNonBlocking()

cir = canvas.TKCanvas.create_oval(50, 50, 100, 100)

while True:
    button, values = form.Read()
    if button is None: break
    if button is 'Blue':
        canvas.TKCanvas.itemconfig(cir, fill = "Blue")
    elif button is 'Red':
        canvas.TKCanvas.itemconfig(cir, fill = "Red")
