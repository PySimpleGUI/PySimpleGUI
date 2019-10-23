#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
# GUI for switching an LED on and off to GPIO14

# GPIO and time library:
import time

if sys.platform == 'win32':
    from random import randint

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

layout = [[sg.T('Raspberry Pi LEDs')],
           [sg.T('', size=(20, 1), key='output')],
           [sg.Button('Switch LED')],
           [sg.Button('Flash LED')],
           [sg.Exit()]]

window = sg.Window('Raspberry Pi GUI', layout, grab_anywhere=False)

while True:
    event, values = window.Read()
    if event in (None, 'Exit'):
        break

    if event == 'Switch LED':
        window.FindElement('output').Update(SwitchLED())
    elif event == 'Flash LED':
        window.FindElement('output').Update('LED is Flashing')
        window.Refresh()
        FlashLED()
        window.FindElement('output').Update('')

window.Close()
sg.Popup('Done... exiting')
