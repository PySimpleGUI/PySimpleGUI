import PySimpleGUI as rg

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

layout = [[rg.T('Raspberry Pi LEDs')],
           [rg.T('', size=(14, 1), key='output')],
           [rg.ReadFormButton('Switch LED')],
           [rg.ReadFormButton('Flash LED')],
           [rg.Exit()]
          ]

form = rg.FlexForm('Raspberry Pi GUI', grab_anywhere=False)
form.Layout(layout)

while True:
    button, values = form.Read()
    if button is None:
        break

    if button is 'Switch LED':
        form.FindElement('output').Update(SwitchLED())
    elif button is 'Flash LED':
        form.FindElement('output').Update('LED is Flashing')
        form.ReadNonBlocking()
        FlashLED()
        form.FindElement('output').Update('')

rg.Popup('Done... exiting')
