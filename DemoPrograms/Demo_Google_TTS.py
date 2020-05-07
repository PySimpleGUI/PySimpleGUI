#!/usr/bin/env python
import PySimpleGUI as sg
from gtts import gTTS
from pygame import mixer
import time
import os

'''
    Simple demonstration of using Google Text to Speech
    Get a multi-line string
    Convert to speech
    Play back the speech
    
    Note that there are 2 temp files created. The program tries to delete them but will fail on one of them
'''

layout = [[sg.Text('What would you like me to say?')],
          [sg.MLine(size=(60,10), enter_submits=True)],
          [sg.Button('Speak', bind_return_key=True), sg.Exit()]]

window = sg.Window('Google Text to Speech', layout)

i = 0
mixer.init()
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # Get the text and convert to mp3 file
    tts = gTTS(text=values[0], lang='en',slow=False)
    tts.save('speech{}.mp3'.format(i%2))
    # playback the speech
    mixer.music.load('speech{}.mp3'.format(i%2))
    mixer.music.play()
    # wait for playback to end
    while mixer.music.get_busy():
        time.sleep(.1)
    mixer.stop()
    i += 1

window.close()

# try to remove the temp files. You'll likely be left with 1 to clean up
try:
    os.remove('speech0.mp3')
except:
    pass
try:
    os.remove('speech1.mp3')
except:
    pass