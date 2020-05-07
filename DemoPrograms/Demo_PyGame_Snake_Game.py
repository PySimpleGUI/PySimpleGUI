import pygame
import PySimpleGUI as sg
import os

"""
    Demo - Simple Snake Game using PyGame and PySimpleGUI
    This demo may not be fully functional in terms of getting the coordinate
    systems right or other problems due to a lack of understanding of PyGame
    The purpose of the demo is to show one way of adding a PyGame window into your PySimpleGUI window
    Note, you must click on the game area in order for PyGame to get keyboard strokes, etc.
    Tried using set_focus to switch to the PyGame canvas but still needed to click on game area
"""

# --- Globals ---
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the width and height of each snake segment
segment_width = 15
segment_height = 15
# Margin between each segment
segment_margin = 3

# Set initial speed
x_change = segment_width + segment_margin
y_change = 0


class Segment(pygame.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function

    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([segment_width, segment_height])
        self.image.fill(WHITE)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# --------------------------- GUI Setup & Create Window -------------------------------


layout = [[sg.Text('Snake Game - PySimpleGUI + PyGame')],
          [sg.Graph((800, 600), (0, 0), (800, 600),
                    background_color='lightblue', key='-GRAPH-')],
          [sg.Exit()]]

window = sg.Window('Snake Game using PySimpleGUI and PyGame',
                   layout, finalize=True)

# ------------------------ Do the magic that integrates PyGame and Graph Element ------------------
graph = window['-GRAPH-']           # type: sg.Graph
embed = graph.TKCanvas
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

# ----------------------------- PyGame Code -----------------------------
# Call this function so the Pygame library can initialize itself
# pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill(pygame.Color(255, 255, 255))

pygame.display.init()
pygame.display.update()

# Set the title of the window
pygame.display.set_caption('Snake Example')

allspriteslist = pygame.sprite.Group()

# Create an initial snake
snake_segments = []
for i in range(15):
    x = 250 - (segment_width + segment_margin) * i
    y = 30
    segment = Segment(x, y)
    snake_segments.append(segment)
    allspriteslist.add(segment)

clock = pygame.time.Clock()

while True:
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = (segment_width + segment_margin) * -1
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = (segment_width + segment_margin)
                y_change = 0
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = (segment_height + segment_margin) * -1
            if event.key == pygame.K_DOWN:
                x_change = 0
                y_change = (segment_height + segment_margin)

    # Get rid of last segment of the snake
    # .pop() command removes last item in list
    old_segment = snake_segments.pop()
    allspriteslist.remove(old_segment)

    # Figure out where new segment will be
    x = snake_segments[0].rect.x + x_change
    y = snake_segments[0].rect.y + y_change
    segment = Segment(x, y)

    # Insert new segment into the list
    snake_segments.insert(0, segment)
    allspriteslist.add(segment)

    # -- Draw everything
    # Clear screen
    screen.fill(BLACK)

    allspriteslist.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(5)

window.close()
