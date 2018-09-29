#!/usr/bin/env python
import sys
if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg
# GUI for switching an LED on and off to GPIO14

# GPIO and time library:
import RPi.GPIO as GPIO
import time

# determine that GPIO numbers are used:
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

def SwitchLED():
    varLEDStatus = GPIO.input(14)
    varLedStatus = 0
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
           [sg.T('', size=(14, 1), key='output')],
           [sg.ReadButton('Switch LED')],
           [sg.ReadButton('Flash LED')],
           [sg.Exit()]]

window = sg.Window('Raspberry Pi GUI', grab_anywhere=False).Layout(layout)

while True:
    button, values = window.Read()
    if button is None:
        break

    if button is 'Switch LED':
        window.FindElement('output').Update(SwitchLED())
    elif button is 'Flash LED':
        window.FindElement('output').Update('LED is Flashing')
        window.ReadNonBlocking()
        FlashLED()
        window.FindElement('output').Update('')

sg.Popup('Done... exiting')
