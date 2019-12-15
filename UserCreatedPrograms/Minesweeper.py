import PySimpleGUI as sg
import random

'''
Source code of MineSweeper Game
'''

blank = b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAAEnQAABJ0Ad5mH3gAAAA5SURBVEhL7c0xAQAgDMTABynVU7MohAUN6ZJbMmbV6ZsB+xfnGOMY4xjjGOMY4xjjGOMY4xgzNE4euGMCWklhg+IAAAAASUVORK5CYII='
bomb = b'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'
flag = b'iVBORw0KGgoAAAANSUhEUgAAAB4AAAAeCAYAAAA7MK6iAAAE9ElEQVR4nL2WTWxUVRTHf+fe+147pbQKFChUipREKUYEEhAT2SgGNP0IpkkXsDCwIWHVdMWGuDEkRIwJC+OCEQkbiCB2ISQkiiHRlCIsnBqirZCWr1JqKRPBmXn3uJg37bR0qNHqP3nJzP363XPOPedeUVURESUvAbRlTf0zodWGocePrl3ovZeO+0KgAngAFMY7wDMhib9cUVsIZIr+o6pipkBpe7UuIWQuOOu/r51T/jbwprX2hDHmJ2NMyhhzVUQ+rK2tXeacyznnvHPOG2M8EMVQsda+IyKfAXOL1wcQERWKtB8MQOqVpTseRdH+c6mhPg9bmCJjDLlcbgT4CPgauAsEZWVlz2cymc0i0gysBUa89yuAsYKxxa4plgD6+Y6X5yS7b9258OtIZexKLbhRRDSKIr9x40bX3NxMTU0Nt2/f/iOZTAbXr18PrLWoKrH1t733rcCP8XxPCQnAx1tXlm1bvbi/PHQRIpExRo0xGgSBioju2bNH0+m0T6fT2YGBAe3v79f79+/rhg0bIhHJOuciY0wuntcRr21LQSfBW9bU/lBdESpIzsZg55wCOjw8rMlkUltbW3Xnzp26adMmr6r+0KFDCmgYhj6GPmCaGE+rtrb8zt5du+TUouqEgmRtkcXOOd27d6+mUim9ePGinjlzRs+fP68DAwPa0NCggDrn1BgTxd858id7EthMBQ8N5QeEVgYTgQF0fIr3nlwux+HDh+nu7iaRSBAEAXV1dTQ2NmKtpby8nCiKIB9PA3xDPp0mudqVstwZO5AIJsbGJ5nOzk6uXLlCT08Ply5dIp1OM2/ePFpaWjh27Bi7du3iyJEjOOckiiJUdR1P5vuTFhcUWBkod/luEYP3nvnz53Pw4EHOnj1LfX09XV1dnD59mqqqKjo7Ozl+/DgLFixAZMKrItJDnNtPtXjhwnyuOSe3yvJggyree6IoYvv27aRSKXbv3k1vby9jY2OMjo7S3NxMX18fxhhEhCiKBEBVXwc+AR7GcJ3W4saT+Y4glDuBNR7EeFUNgoDR0VGGh4e1o6NDV61axYEDB2hqauLo0aMkk0my2Szt7e1473HOeSASkc1ANUXFo5QEYP9bjfPeeHHhiLVGjTG5IAiyIuLb29u1r69P169fr7ELFdDq6mrdt2+fr6+vz4lIZK3VOKV6gFXxuiVDOw4+0dZmt7206JdEvogUFlFghHyJ1DAM1TmXC8MwS75SKaDGGBWRq8aY95g4zU/P41gGoHXNku+enVOmIL9ZkQ+cc69VVlYuAKorKirWicipwoastRqG4Ygx5gtrbQuTz8/fgo4XkdY1tV+9sHjup0BVqZnW2iZjzC5r7RZg4dTuUtBp87hQRECG1j9X/e21Ow/HltVTfuMGGSYOiQAaRVHXNDDI521UyrinBhv0VjqTWw3I8uXkmLiptOi3jQ0oWBcxEe+SmgHMoMUsmmGRwuU/I2xGcKGIqJhBRWuK22ZL08a4UEQM3CSf/Jw8WfoS/yea1uL3Y5f9mcncVaFs68qVZUy8Qv47cEF3E/fui6KJxKOa2QLOBFZALl8mq8LjyEWLAfb/Hxa3teX7BPndqCwF6G2bPXDJh8B4EVEdEqRuUtssaKY8BpFbQN1sAWcEj+etMojo1Br8r1XS1Zwk5upNYMWkzcyCjKpOG7cT8eNMA/kZ+BJmr4ioqvwF0Vn06LBZVccAAAAASUVORK5CYII='

font        = 'Courier 16 bold'
width       = 25
height      = 14
all         = 80
new_start   = True
size        = (30,30)
# 0: 0, 1: hidden card, 2: bomb card, 3: flag card, 4: shown card
im          = ['', blank, bomb,flag, '']
color       = [('grey', 'grey'), ('black', 'green'),
               ('black', 'green'), ('black', 'green'), ('black', 'grey')]

def binding_all():                  # Bind right button of mouse to cell object

    for x in range(width):
        for y in range(height):
            window[b[x][y].key].bind(
                '<Button-3>', '+RIGHT')

# Setting for top buttons
def button1(text, key=None, disabled=False, button_color=('white', 'green')):

    return sg.Button(text, pad=(10, 10), font=font, focus=False, key=key,
            disabled=disabled, button_color=button_color)

def button2(x, y):                  # define cell as instance of button and

    b[x][y] = button(x,y)           # bulid Button
    return b[x][y].button

def check_blank(x, y):              # Check if cell near 0-bomb cel

    if b[x][y].num==0: return False
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i==0 and j==0: continue
            if ((0<=x+i<width) and (0<=y+j<height) and
                (b[x+i][y+j].num==0)): return True
    return False

def check_num():                    # check number of bombs, flags and hides

    bomb_count = flag_count = hide_count = 0
    for x in range(width):
        for y in range(height):
            if b[x][y].state == 1:
                hide_count += 1
            elif b[x][y].state == 2:
                bomb_count += 1
            elif b[x][y].state == 3:
                flag_count += 1
    return bomb_count, flag_count, hide_count

# Count number of bombs about cell
def count_bomb(x, y):

    global bomb
    if bomb[x][y]==10: return 10
    count = 0
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i==0 and j==0: continue
            if ((0<=x+i<width) and (0<=y+j<height) and
                (bomb[x+i][y+j]==10)):
                count += 1
    return count

# set position for all boms
def deal():

    global bomb
    bomb_list   = random.sample(range(width*height), all)
    bomb        = [[0 for y in range(height)] for x in range(width)]

    for x in range(width):
        for y in range(height):
            if x*height+y in bomb_list: bomb[x][y]=10

    for x in range(width):
        for y in range(height):
            bomb[x][y] = count_bomb(x, y)

    return

def new_card():                     # refresh all cells to hidden card

    for x in range(width):
        for y in range(height):
            b[x][y].state = 1
            b[x][y].num = bomb[x][y]
            b[x][y].color = color[1]
            b[x][y].update(1)

def show_blank():                   # Show all cell not around by any bomb

    for x in range(width):
        for y in range(height):
            if b[x][y].num == 0:
                b[x][y].update(0)
            elif check_blank(x, y):
                b[x][y].update(4)

# Class for each button object
class button():

    def __init__(self, x, y):

        self.x          = x
        self.y          = y
        self.state      = 1
        self.color      = color[self.state]
        self.disabled   = False
        self.key        = (x,y)             # keys can be ANYTHING, not just strings
        self.num        = bomb[x][y]
        self.button     = sg.Button(' ',
            auto_size_button=False,
            border_width=2,
            button_color=self.color,
            disabled=self.disabled,
            focus=False,
            font=font,
            image_size=size,
            # image_filename=im[self.state],
            image_data=im[self.state],
            key=self.key,
            pad=(1,1))

    def right_click(self):   # Right_click handler

        if self.state == 1:
            self.update(3)
        elif self.state == 3:
            self.update(1)

    def update(self, state):        # update state of cell

        self.state = state
        if state == 0:
            self.disabled = True
            text = ' '
        elif state in [1,2,3]:
            self.disabled = False
            text = ' '
        elif state == 4:
            self.disabled = True
            text = str(self.num)
        self.color = color[self.state]
        window[self.key].Widget['disabledforeground'] = 'white'
        self.button.Update(text=text, disabled=self.disabled,
            # image_filename=im[self.state],
            image_data=im[self.state],
            image_size=size,
            button_color=self.color)

# set theme for window
sg.change_look_and_feel('DarkGreen')

deal()  # Initial position of bombs
b = [[0 for j in range(height)] for i in range(width)]

layout  = [[button1('New Game', key='-New Game-'),  # Layout of window
            button1('Game Over', key='-Game Over-'),
            button1('Target:'+str(all), key='-Target-'),
            button1('Bomb:0', key='-Count-Bomb-'),
            button1('Flag:0', key='-Count-Flag-')]]+[
            [button2(x, y) for x in range(width)] for y in range(height)]

window = sg.Window('MineSweeper', layout=layout, finalize=True) # Create window
binding_all()       # Binding right button event handler of all cells
show_blank()        # Show all cells near no-bomb cell

new_start   = True  # Flag for new game
message     = False # Flag for game over message sent

while True:

    if new_start:   # Actions for new game

        deal()
        new_card()
        show_blank()
        message = False
        new_start = False
        pass

    event, values = window.read()    # read window event

    if event==None or event=='-Game Over-':     # Window close / Game over
        break

    elif event == '-New Game-':                 # New Game, set the flag
        new_start = True

    elif isinstance(event, tuple):              # buttons have tuple for event
        right_click = False
        if isinstance(event[0], tuple):         # if the tuple has a tuple, then it's a right click event
            x,y = event[0]
            right_click = True
        else:
            x, y = event
        if not right_click:
            if b[x][y].state == 1:
                if b[x][y].num == 10:
                    b[x][y].update(2)
                else:
                    b[x][y].update(4)
        else:
            b[x][y].right_click()
    # Update number onf bombs, flags
    bomb_num, flag_num, hide_num = check_num()
    window['-Count-Bomb-'].Update(text='Bomb:'+str(bomb_num))
    window['-Count-Flag-'].Update(text='Flag:'+str(flag_num))

    # Check if game over
    if hide_num==0 and (bomb_num+flag_num==all) and (not message):
        message = True
        sg.popup('Game Over', title='Note')

window.close()
