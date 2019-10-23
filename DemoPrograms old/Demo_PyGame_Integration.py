import pygame
import PySimpleGUI as sg
import os

"""
    Demo of integrating PyGame with PySimpleGUI, the tkinter version
    A similar technique may be possible with WxPython
    Only works on windows from what I've read
"""
# --------------------- PySimpleGUI window layout and creation --------------------
layout = [[sg.T('Test of PySimpleGUI with PyGame')],
          [sg.Graph((500,500), (0,0), (500,500), background_color='lightblue', key='_GRAPH_' )],
          [sg.B('Draw'), sg.Exit()]]

window = sg.Window('PySimpleGUI + PyGame', layout).Finalize()
graph = window.Element('_GRAPH_')

# -------------- Magic code to integrate PyGame with tkinter -------
embed = graph.TKCanvas
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

# ----------------------------- PyGame Code -----------------------------

screen = pygame.display.set_mode((500,500))
screen.fill(pygame.Color(255,255,255))

pygame.display.init()
pygame.display.update()

while True:
    event, values = window.Read(timeout=10)
    if event in (None, 'Exit'):
        break
    elif event == 'Draw':
        pygame.draw.circle(screen, (0, 0, 0), (250, 250), 125)
    pygame.display.update()

window.Close()