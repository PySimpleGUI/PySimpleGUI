import PySimpleGUI as g

# GUI for switching an LED on and off to GPIO14

# GPIO and time library:
import RPi.GPIO as GPIO
import time

# determine that GPIO numbers are used:
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

def SwitchLED():
    varLEDStatus = GPIO.input(14)

    if varLEDStatus == 0:
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

results_elem = g.T('', size=(30,1))

layout = [[g.T('Raspberry Pi LEDs')],
           [results_elem],
           [g.ReadFormButton('Switch LED')],
           [g.ReadFormButton('Flash LED')],
           [g.ReadFormButton('Show slider value')],
           [g.Slider(range=(0, 100), default_value=0, orientation='h', size=(40,20), key='slider')],
           [g.Exit()]
          ]

form = g.FlexForm('Raspberry Pi GUI')
form.Layout(layout)

while True:
    button, values = form.Read()
    if button is None:
        break
    if button is 'Switch LED':
        results_elem.Update(SwitchLED())
    elif button is 'Flash LED':
        results_elem.Update('LED is Flashing')
        form.ReadNonBlocking()
        FlashLED()
        results_elem.Update('')
    elif button is 'Show slider value':
        results_elem.Update('Slider = %s'%values['slider'])

g.MsgBox('Done... exiting')
