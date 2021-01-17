import PySimpleGUIQt as sg
print(sg)
      

dicta1 = {
    "a": "hellgdfgo world",
    4: 5,
    "qwerty" : "ytjyhrewq"
}
dicta2 = {
    "a": "helldasdo world",
    4: 5,
    "qwerty" : "ytrewq"
}
dicta3 = {
    "a": "hello world",
    4: 5,
    "qwerty" : "ytwqddqwrewq"
}


class ParsingError(object):
    def __init__(self, psg_object, num):
        self.num = num
        self.psg_object = psg_object

    def __str__(self):
        return self.__repr__()
        
    def __repr__(self):
        return f'{self.num} {self.psg_object}' 

    @staticmethod
    def headers():
        return 'num,psg_object'.split(',')
    
      
items = [
    ParsingError(dicta1, 45),
    ParsingError(dicta2, 42),
    ParsingError(dicta3, 12),
]


window = sg.Window('Test', [
    [sg.Listbox(items, key='qwe', enable_events=True)],
    [sg.B('q1'), sg.B('q2'), sg.B('q3')],
],return_keyboard_events=True)

while True:
    event, values = window()
    if event in ('Exit', None): break

    print(event, values)

    if event == 'q1':
        gui = values['qwe'][0]
        print(gui.num)
        print(gui.psg_object[4])

window.close()