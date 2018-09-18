import PySimpleGUI as sg


layout = [
           [sg.Canvas(size=(150, 150), background_color='red', key='canvas')],
           [sg.T('Change circle color to:'), sg.ReadFormButton('Red'), sg.ReadFormButton('Blue')]
           ]

form = sg.FlexForm('Canvas test')
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
