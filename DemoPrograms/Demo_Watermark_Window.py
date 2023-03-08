import PySimpleGUI as sg

"""
    Demo - Watermarking all windows

    Watermarking windows can be done in 4.60.0.160 and greater.  It's a very simple mechanism for now.
    
    The option is normally set in the Global Settings control panel.  However, you can "Force" the watermark
    on all windows by setting the Window paramter watermark=True on any window you create and from then on
    all windows will have the watermark.

    Copyright 2023 PySimpleGUI
"""

"""
M"""""""`YM          
M  mmmm.  M          
M  MMMMM  M .d8888b. 
M  MMMMM  M 88'  `88 
M  MMMMM  M 88.  .88 
M  MMMMM  M `88888P' 
MMMMMMMMMMM          
                     
M""MMM""MMM""M            dP                                                  dP       
M  MMM  MMM  M            88                                                  88       
M  MMP  MMP  M .d8888b. d8888P .d8888b. 88d888b. 88d8b.d8b. .d8888b. 88d888b. 88  .dP  
M  MM'  MM' .M 88'  `88   88   88ooood8 88'  `88 88'`88'`88 88'  `88 88'  `88 88888"   
M  `' . '' .MM 88.  .88   88   88.  ... 88       88  88  88 88.  .88 88       88  `8b. 
M    .d  .dMMM `88888P8   dP   `88888P' dP       dP  dP  dP `88888P8 dP       dP   `YP 
MMMMMMMMMMMMMM
"""

layout = [  [sg.Text('No Watermark')],
            [sg.Button('Exit')]  ]

window = sg.Window('No Watermark', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()


"""
MP""""""`MM                     dP                       
M  mmmmm..M                     88                       
M.      `YM dP    dP .d8888b. d8888P .d8888b. 88d8b.d8b. 
MMMMMMM.  M 88    88 Y8ooooo.   88   88ooood8 88'`88'`88 
M. .MMM'  M 88.  .88       88   88   88.  ... 88  88  88 
Mb.     .dM `8888P88 `88888P'   dP   `88888P' dP  dP  dP 
MMMMMMMMMMM      .88                                     
             d8888P                                      
M""MMM""MMM""M            dP                                                  dP       
M  MMM  MMM  M            88                                                  88       
M  MMP  MMP  M .d8888b. d8888P .d8888b. 88d888b. 88d8b.d8b. .d8888b. 88d888b. 88  .dP  
M  MM'  MM' .M 88'  `88   88   88ooood8 88'  `88 88'`88'`88 88'  `88 88'  `88 88888"   
M  `' . '' .MM 88.  .88   88   88.  ... 88       88  88  88 88.  .88 88       88  `8b. 
M    .d  .dMMM `88888P8   dP   `88888P' dP       dP  dP  dP `88888P8 dP       dP   `YP 
MMMMMMMMMMMMMM
"""

sg.set_options(watermark_text='')       # noramlly not requird unless previously set by user

layout = [  [sg.Text('System Provided Watermark')],
            [sg.Button('Exit')]  ]

window = sg.Window('System Watermark', layout, watermark=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()


"""
M""MMMMM""M                            
M  MMMMM  M                            
M  MMMMM  M .d8888b. .d8888b. 88d888b. 
M  MMMMM  M Y8ooooo. 88ooood8 88'  `88 
M  `MMM'  M       88 88.  ... 88       
Mb       dM `88888P' `88888P' dP       
MMMMMMMMMMM                            
                                       
M""MMM""MMM""M            dP                                                  dP       
M  MMM  MMM  M            88                                                  88       
M  MMP  MMP  M .d8888b. d8888P .d8888b. 88d888b. 88d8b.d8b. .d8888b. 88d888b. 88  .dP  
M  MM'  MM' .M 88'  `88   88   88ooood8 88'  `88 88'`88'`88 88'  `88 88'  `88 88888"   
M  `' . '' .MM 88.  .88   88   88.  ... 88       88  88  88 88.  .88 88       88  `8b. 
M    .d  .dMMM `88888P8   dP   `88888P' dP       dP  dP  dP `88888P8 dP       dP   `YP 
MMMMMMMMMMMMMM
"""

sg.set_options(watermark_text='User Supplied Version 1.0')

layout = [  [sg.Text('User Supplied Watermark')],
            [sg.Button('Exit')]  ]

window = sg.Window('User Supplied Watermark', layout, watermark=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
