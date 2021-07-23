import time
import PySimpleGUI as sg

"""
    Demo Long Operations
    
    How to make calls to your functions that take a very long time to complete.
    
    One of the classic GUI problems is when a function takes a long time to complete.
    Normally these functions cause a GUI to appear to the operating system to have
    hung and you'll see a message asking if you want to kill your program.
    
    PySimpleGUI has a Window method - perform_long_operation that can help in these situations
    NOTE - because this method uses threads, it's important you do not make any PySimpleGUI calls
    from your long function.  Also, some things simply cannot be safely run as a thread.  Just understand
    that this function perform_long_operation utilizes threads.
    
    window.perform_long_operation takes 2 parameters:
        * A lambda expression that represents your function call
        * A key that is returned when you function completes
        
    When you function completes, you will receive an event when calling window.read() that
    matches the key provided.

    Copyright 2021 PySimpleGUI
"""


'''
M""MMMMM""M                            
M  MMMMM  M                            
M  MMMMM  M .d8888b. .d8888b. 88d888b. 
M  MMMMM  M Y8ooooo. 88ooood8 88'  `88 
M  `MMM'  M       88 88.  ... 88       
Mb       dM `88888P' `88888P' dP       
MMMMMMMMMMM                            
                                       
MM""""""""`M                            
MM  mmmmmmmM                            
M'      MMMM dP    dP 88d888b. .d8888b. 
MM  MMMMMMMM 88    88 88'  `88 88'  `"" 
MM  MMMMMMMM 88.  .88 88    88 88.  ... 
MM  MMMMMMMM `88888P' dP    dP `88888P' 
MMMMMMMMMMMM
'''


def my_long_func(count, a=1, b=2):
    """
    This is your function that takes a long time
    :param count:
    :param a:
    :param b:
    :return:
    """
    for i in range(count):
        print(i, a, b)
        time.sleep(.5)
    return 'DONE!'


'''
                    oo          
                                
88d8b.d8b. .d8888b. dP 88d888b. 
88'`88'`88 88'  `88 88 88'  `88 
88  88  88 88.  .88 88 88    88 
dP  dP  dP `88888P8 dP dP    dP 
                                
                                
oo                dP oo                              dP                        dP dP 
                  88                                 88                        88 88 
dP 88d888b. .d888b88 dP 88d888b. .d8888b. .d8888b. d8888P    .d8888b. .d8888b. 88 88 
88 88'  `88 88'  `88 88 88'  `88 88ooood8 88'  `""   88      88'  `"" 88'  `88 88 88 
88 88    88 88.  .88 88 88       88.  ... 88.  ...   88      88.  ... 88.  .88 88 88 
dP dP    dP `88888P8 dP dP       `88888P' `88888P'   dP      `88888P' `88888P8 dP dP
'''

# This is your new code that uses a thread to perform the long operation

def main():
    layout = [  [sg.Text('Indirect Call Version')],
                [sg.Text('How many times to run the loop?'), sg.Input(s=(4,1), key='-IN-')],
                [sg.Text(s=(30,1), k='-STATUS-')],
                [sg.Button('Go', bind_return_key=True), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Go':
            window['-STATUS-'].update('Calling your function...')
            if values['-IN-'].isnumeric():

                # This is where the magic happens.  Add your function call as a lambda
                window.perform_long_operation(lambda :
                                              my_long_func(int(values['-IN-']), a=10),
                                              '-END KEY-')
            else:
                window['-STATUS-'].update('Try again... how about an int?')
        elif event == '-END KEY-':
            return_value = values[event]
            window['-STATUS-'].update(f'Completed. Returned: {return_value}')
    window.close()


'''
                    oo          
                                
88d8b.d8b. .d8888b. dP 88d888b. 
88'`88'`88 88'  `88 88 88'  `88 
88  88  88 88.  .88 88 88    88 
dP  dP  dP `88888P8 dP dP    dP 
                                
                                
      dP oo                              dP                        dP dP 
      88                                 88                        88 88 
.d888b88 dP 88d888b. .d8888b. .d8888b. d8888P    .d8888b. .d8888b. 88 88 
88'  `88 88 88'  `88 88ooood8 88'  `""   88      88'  `"" 88'  `88 88 88 
88.  .88 88 88       88.  ... 88.  ...   88      88.  ... 88.  .88 88 88 
`88888P8 dP dP       `88888P' `88888P'   dP      `88888P' `88888P8 dP dP
'''

# This is your original code... it's all going great.... until the call takes too long
def old_main():
    layout = [  [sg.Text('Direct Call Version')],
                [sg.Text('How many times to run the loop?'), sg.Input(s=(4,1), key='-IN-')],
                [sg.Text(s=(30,1), k='-STATUS-')],
                [sg.Button('Go', bind_return_key=True), sg.Button('Exit')]  ]

    window = sg.Window('Window Title', layout)

    while True:             # Event Loop
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Go':
            if values['-IN-'].isnumeric():
                window['-STATUS-'].update('Calling your function...')
                window.refresh()        # needed to make the message show up immediately20

                return_value = my_long_func(int(values['-IN-']), a=10)

                window['-STATUS-'].update(f'Completed. Returned: {return_value}')
            else:
                window['-STATUS-'].update('Try again... how about an int?')

    window.close()




if __name__ == '__main__':
    # old_main()
    main()
