#!/usr/bin/env python
import sys
import PySimpleGUI as sg
import time

"""
    Copyright 2023 PySimpleSoft, Inc. and/or its licensors. All rights reserved.

    Redistribution, modification, or any other use of PySimpleGUI or any portion thereof is subject to the terms of the PySimpleGUI License Agreement available at https://eula.pysimplegui.com.

    You may not redistribute, modify or otherwise use PySimpleGUI or its contents except pursuant to the PySimpleGUI License Agreement.
"""

# App for Raspberry Pi.

if sys.platform == 'win32':

    class GPIO():
        LOW = 0
        HIGH = 1
        BCM = OUT = 0
        current_value = 0

        @classmethod
        def setmode(self, mode):
            return

        @classmethod
        def setup(self, arg1, arg2):
            return

        @classmethod
        def output(self, port, value):
            self.current_value = value

        @classmethod
        def input(self, port):
            return self.current_value
else:
    import RPi.GPIO as GPIO

# determine that GPIO numbers are used:
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)


def SwitchLED():
    varLedStatus = GPIO.input(14)
    if varLedStatus == 0:
        GPIO.output(14, GPIO.HIGH)
        return "LED is switched ON"
    else:
        GPIO.output(14, GPIO.LOW)
        return "LED is switched OFF"


def FlashLED():
    for i in range(5):
        GPIO.output(14, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(14, GPIO.LOW)
        time.sleep(0.5)


layout = [[sg.Text('Raspberry Pi LEDs')],
          [sg.Text('', size=(20, 1), key='output')],
          [sg.Button('Switch LED')],
          [sg.Button('Flash LED')],
          [sg.Exit()]]

window = sg.Window('Raspberry Pi GUI', layout, grab_anywhere=False)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    if event == 'Switch LED':
        window['output'].update(SwitchLED())
    elif event == 'Flash LED':
        window['output'].update('LED is Flashing')
        window.refresh()
        FlashLED()
        window['output'].update('')

window.close()
