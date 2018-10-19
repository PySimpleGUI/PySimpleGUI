import PySimpleGUI as sg


class keyboard():
    def __init__(self, font=('Arial', 16)):
        self.font = font
        numberRow = '1234567890'
        topRow = 'QWERTYUIOP'
        midRow = 'ASDFGHJKL'
        bottomRow = 'ZXCVBNM'
        keyboard_layout = [[sg.ReadButton(c, key=c, pad=(0, 0), size=(4, 2), font=self.font) for c in numberRow] + [
            sg.ReadButton('⌫', key='back', pad=(0, 0), size=(4, 2), font=self.font),
            sg.ReadButton('Esc', key='close', pad=(0, 0), size=(4, 2), font=self.font)],
                           [sg.T(' ' * 4)] + [sg.ReadButton(c, key=c, pad=(0, 0), size=(4, 2), font=self.font) for c in
                                              topRow],
                           [sg.T(' ' * 11)] + [sg.ReadButton(c, key=c, pad=(0, 0), size=(4, 2), font=self.font) for c in
                                               midRow],
                           [sg.T(' ' * 18)] + [sg.ReadButton(c, key=c, pad=(0, 0), size=(4, 2), font=self.font) for c in
                                               bottomRow]]

        self.window = sg.Window('keyboard', grab_anywhere=True, keep_on_top=True, no_titlebar=True).Layout(
            keyboard_layout).Finalize()
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
        self.event, _ = self.window.ReadNonBlocking()
        if focus is not None:
            self.focus = focus
        self._keyboardhandler()

    def close(self):
        self.window.CloseNonBlocking()


class GUI():
    def __init__(self):
        layout = [[sg.Text('Enter Text')],
                  [sg.Input(size=(17, 1), key='input1', do_not_clear=True )],
                  [sg.InputText(size=(17, 1), key='input2', do_not_clear=True)],
                  [sg.ReadButton('on-screen keyboard', key='keyboard')],
                  [sg.ReadButton('close', key='close')]]

        self.mainWindow = sg.Window('On-screen test', grab_anywhere=False, no_titlebar=True).Layout(layout)
        self.keyboard = keyboard()
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
            elif event == 'close':
                break
        self.keyboard.close()
        self.mainWindow.CloseNonBlocking()


if __name__ == '__main__':
    app = GUI()
    app.run()
