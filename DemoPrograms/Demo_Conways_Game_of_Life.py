#!/usr/bin/env python

#  John Conway's "Game of Life" using a GUI.
#  Copyright (C) 2018 PySimpleGUI.org
#  GUI provided by PySimpleGUI.
#  Core game engine provied by Christian Jacobs

#  An implementation of Conway's Game of Life in Python.

#  Copyright (C) 2013 Christian Jacobs.

#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import numpy
import PySimpleGUI as sg

BOX_SIZE = 15

class GameOfLife:

    def __init__(self, N=20, T=200):
        """ Set up Conway's Game of Life. """
        # Here we create two grids to hold the old and new configurations.
        # This assumes an N*N grid of points.
        # Each point is either alive or dead, represented by integer values of 1 and 0, respectively.
        self.N = N
        self.old_grid = numpy.zeros(N * N, dtype='i').reshape(N, N)
        self.new_grid = numpy.zeros(N * N, dtype='i').reshape(N, N)
        self.T = T  # The maximum number of generations

        # Set up a random initial configuration for the grid.
        for i in range(0, self.N):
            for j in range(0, self.N):
                self.old_grid[i][j] = 0
        self.init_graphics()
        self.manual_board_setup()

    def live_neighbours(self, i, j):
        """ Count the number of live neighbours around point (i, j). """
        s = 0  # The total number of live neighbours.
        # Loop over all the neighbours.
        for x in [i - 1, i, i + 1]:
            for y in [j - 1, j, j + 1]:
                if (x == i and y == j):
                    continue  # Skip the current point itself - we only want to count the neighbours!
                if (x != self.N and y != self.N):
                    s += self.old_grid[x][y]
                # The remaining branches handle the case where the neighbour is off the end of the grid.
                # In this case, we loop back round such that the grid becomes a "toroidal array".
                elif (x == self.N and y != self.N):
                    s += self.old_grid[0][y]
                elif (x != self.N and y == self.N):
                    s += self.old_grid[x][0]
                else:
                    s += self.old_grid[0][0]
        return s

    def play(self):
        """ Play Conway's Game of Life. """

        # Write the initial configuration to file.

        self.t = 1  # Current time level
        while self.t <= self.T:  # Evolve!
            # print( "At time level %d" % t)

            # Loop over each cell of the grid and apply Conway's rules.
            for i in range(self.N):
                for j in range(self.N):
                    live = self.live_neighbours(i, j)
                    if (self.old_grid[i][j] == 1 and live < 2):
                        self.new_grid[i][j] = 0  # Dead from starvation.
                    elif (self.old_grid[i][j] == 1 and (live == 2 or live == 3)):
                        self.new_grid[i][j] = 1  # Continue living.
                    elif (self.old_grid[i][j] == 1 and live > 3):
                        self.new_grid[i][j] = 0  # Dead from overcrowding.
                    elif (self.old_grid[i][j] == 0 and live == 3):
                        self.new_grid[i][j] = 1  # Alive from reproduction.

            # Output the new configuration.

            # The new configuration becomes the old configuration for the next generation.
            self.old_grid = self.new_grid.copy()
            self.draw_board()
            # Move on to the next time level
            self.t += 1

    def init_graphics(self):
        self.graph = sg.Graph((600, 600), (0, 0), (450, 450), key='_GRAPH_', change_submits=True, drag_submits=False, background_color='lightblue')
        layout = [
            [sg.Text('Game of Life    ', font='ANY 15'), sg.Text('', key='_OUTPUT_', size=(30,1), font='ANY 15')],
            [self.graph],
            [sg.Button('Go!', key='_DONE_'),
             sg.Text('  Delay (ms)') , sg.Slider([0,400], orientation='h', key='_SLIDER_', size=(15,15)),
             sg.Text('  Num Generations'), sg.Slider([0, 3000],default_value=400, orientation='h',size=(15,15), key='_SLIDER2_')]
        ]

        self.window = sg.Window('Window Title', ).Layout(layout).Finalize()
        event, values = self.window.Read(timeout=0)
        self.delay = values['_SLIDER_']


    def draw_board(self):
        BOX_SIZE = 15
        self.graph.Erase()
        for i in range(self.N):
            for j in range(self.N):
                if self.old_grid[i][j]:
                    self.graph.DrawRectangle((i * BOX_SIZE, j * BOX_SIZE),
                                             (i * BOX_SIZE + BOX_SIZE, j * (BOX_SIZE) + BOX_SIZE),
                                             line_color='black', fill_color='yellow')
        event, values = self.window.Read(timeout=self.delay)
        if event in (None, '_DONE_'):
            exit()
        self.delay = values['_SLIDER_']
        self.T = int(values['_SLIDER2_'])
        self.window.Element('_OUTPUT_').Update('Generation {}'.format(self.t))

    def manual_board_setup(self):
        ids = []
        for i in range(self.N):
            ids.append([])
            for j in range(self.N):
                ids[i].append(0)
        while True:  # Event Loop
            event, values = self.window.Read()
            if event is None or event == '_DONE_':
                break
            mouse = values['_GRAPH_']

            if event == '_GRAPH_':
                if mouse == (None, None):
                    continue
                box_x = mouse[0] // BOX_SIZE
                box_y = mouse[1] // BOX_SIZE
                if self.old_grid[box_x][box_y] == 1:
                    id = ids[box_x][box_y]
                    self.graph.DeleteFigure(id)
                    self.old_grid[box_x][box_y] = 0
                else:
                    id = self.graph.DrawRectangle((box_x * BOX_SIZE, box_y * BOX_SIZE),
                                                  (box_x * BOX_SIZE + BOX_SIZE, box_y * (BOX_SIZE) + BOX_SIZE),
                                                  line_color='black', fill_color='yellow')
                    ids[box_x][box_y] = id
                    self.old_grid[box_x][box_y] = 1
        self.window.Element('_DONE_').Update(text='Exit')

if (__name__ == "__main__"):
    game = GameOfLife(N=35, T=200)
    game.play()
