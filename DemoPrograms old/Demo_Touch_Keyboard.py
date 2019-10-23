import PySimpleGUI as sg
# import PySimpleGUIQt as sg            # 100% portable to Qt by changing to this import


class keyboard():
    def __init__(self, location=(None, None), font=('Arial', 16)):
        self.font = font
        numberRow = '1234567890'
        topRow = 'QWERTYUIOP'
        midRow = 'ASDFGHJKL'
        bottomRow = 'ZXCVBNM'
        keyboard_layout = [[sg.Button(c, key=c, size=(4, 2), font=self.font) for c in numberRow] + [
            sg.Button('⌫', key='back', size=(4, 2), font=self.font),
            sg.Button('Esc', key='close', size=(4, 2), font=self.font)],
                           [sg.T(' ' * 4)] + [sg.Button(c, key=c, size=(4, 2), font=self.font) for c in
                                              topRow] + [sg.Stretch()],
                           [sg.T(' ' * 11)] + [sg.Button(c, key=c, size=(4, 2), font=self.font) for c in
                                               midRow] + [sg.Stretch()],
                           [sg.T(' ' * 18)] + [sg.Button(c, key=c, size=(4, 2), font=self.font) for c in
                                               bottomRow] + [sg.Stretch()]]

        self.window = sg.Window('keyboard',
                                grab_anywhere=True,
                                keep_on_top=True,
                                alpha_channel=0,
                                no_titlebar=True,
                                element_padding=(0,0),
                                location=location
                                ).Layout(keyboard_layout).Finalize()
        self.hide()

    def _keyboardhandler(self):
        if self.event is not None:
            if self.event == 'close':
                self.hide()
            elif len(self.event) == 1:
                self.focus.Update(self.focus.Get() + self.event)
            elif self.event == 'back':
                Text = self.focus.Get()
                if len(Text) > 0:
                    Text = Text[:-1]
                    self.focus.Update(Text)

    def hide(self):
        self.visible = False
        self.window.Disappear()

    def show(self):
        self.visible = True
        self.window.Reappear()

    def togglevis(self):
        if self.visible:
            self.hide()
        else:
            self.show()

    def update(self, focus):
        self.event, _ = self.window.Read(timeout=0)
        if focus is not None:
            self.focus = focus
        self._keyboardhandler()

    def close(self):
        self.window.Close()


class GUI():
    def __init__(self):
        layout = [[sg.Text('Enter Text')],
                  [sg.Input(size=(17, 1), key='input1', do_not_clear=True)],
                  [sg.InputText(size=(17, 1), key='input2', do_not_clear=True)],
                  [sg.Button('on-screen keyboard', key='keyboard')],
                  [sg.Button('close', key='close')]]

        self.mainWindow = sg.Window('On-screen test',
                                    grab_anywhere=True,
                                    no_titlebar=False,
                                    ).Layout(layout).Finalize()
        location = self.mainWindow.CurrentLocation()
        location = location[0]-200, location[1]+200
        self.keyboard = keyboard(location)
        self.focus = None

    def run(self):
        while True:
            cur_focus = self.mainWindow.FindElementWithFocus()
            if cur_focus is not None:
                self.focus = cur_focus
            event, values = self.mainWindow.Read(timeout=200, timeout_key='timeout')
            if self.focus is not None:
                self.keyboard.update(self.focus)
            if event == 'keyboard':
                self.keyboard.togglevis()
            elif event == 'close' or event is None:
                break
        self.keyboard.close()
        self.mainWindow.Close()


if __name__ == '__main__':
    app = GUI()
    app.run()
