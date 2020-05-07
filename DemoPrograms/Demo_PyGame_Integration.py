import pygame
import PySimpleGUI as sg
import os

"""
    Demo of integrating PyGame with PySimpleGUI, the tkinter version
    A similar technique may be possible with WxPython
    To make it work on Linux, set SDL_VIDEODRIVER like
    specified in http://www.pygame.org/docs/ref/display.html, in the
    pygame.display.init() section.
"""
# --------------------- PySimpleGUI window layout and creation --------------------
layout = [[sg.Text('Test of PySimpleGUI with PyGame')],
          [sg.Graph((500, 500), (0, 0), (500, 500),
                    background_color='lightblue', key='-GRAPH-')],
          [sg.Button('Draw'), sg.Exit()]]

window = sg.Window('PySimpleGUI + PyGame', layout, finalize=True)
graph = window['-GRAPH-']

# -------------- Magic code to integrate PyGame with tkinter -------
embed = graph.TKCanvas
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
# change this to 'x11' to make it work on Linux
os.environ['SDL_VIDEODRIVER'] = 'windib'

# ----------------------------- PyGame Code -----------------------------

screen = pygame.display.set_mode((500, 500))
screen.fill(pygame.Color(255, 255, 255))

pygame.display.init()
pygame.display.update()

while True:
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Draw':
        pygame.draw.circle(screen, (0, 0, 0), (250, 250), 125)
    pygame.display.update()

window.close()
