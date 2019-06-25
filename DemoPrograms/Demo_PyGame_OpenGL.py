import os
import PySimpleGUI as sg
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *


"""
    Demo of integrating PyGame/OpenGL with PySimpleGUI, the tkinter version
    A similar technique may be possible with WxPython
    To make it work on Windows, set SDL_VIDEODRIVER like
    specified in http://www.pygame.org/docs/ref/display.html, pygame.display.init() section.
"""

vertices= (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

# --------------------- PySimpleGUI window layout and creation --------------------
layout = [[sg.T('Test of PySimpleGUI with PyGame')],
          [sg.Graph((500,500), (0,0), (500,500), background_color='lightblue', key='_GRAPH_' )],
          [sg.Exit()]]

window = sg.Window('PySimpleGUI + PyGame + OpenGL', layout).Finalize()
graph = window.Element('_GRAPH_')

# -------------- Magic code to integrate OpenGL with tkinter -------
embed = graph.TKCanvas
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'x11' # change this to 'windib' to make it work on Windows

# ----------------------------- PyGame/OpenGL Code -----------------------------
display = (500, 500)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
pygame.display.init()
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0,0.0, -5)

while True:
    event, values = window.Read(timeout=10)
    if event in (None, 'Exit'):
        break
    glRotatef(1, 3, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube()
    pygame.display.flip()

window.Close()
