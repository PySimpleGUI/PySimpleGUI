import PySimpleGUI as sg
import random
# ------- Sort visualizer. Displays bar chart representing list items -------
BAR_SPACING, BAR_WIDTH, EDGE_OFFSET = 11, 10, 3
DATA_SIZE = GRAPH_SIZE = (700, 500)      # width, height of the graph portion


def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n - x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
                yield arr


def draw_bars(graph, items):
    # type: (sg.Graph, List)->None
    for i, item in enumerate(items):
        graph.draw_rectangle(top_left=(i * BAR_SPACING + EDGE_OFFSET, item),
                             bottom_right=(i * BAR_SPACING + EDGE_OFFSET + BAR_WIDTH, 0),
                             fill_color='#76506d')


def main():
    sg.theme('LightGreen')
    # Make list to sort
    num_bars = DATA_SIZE[0]//(BAR_WIDTH+1)
    list_to_sort = [DATA_SIZE[1]//num_bars*i for i in range(1, num_bars)]
    random.shuffle(list_to_sort)

    # define window layout
    graph = sg.Graph(GRAPH_SIZE, (0, 0), DATA_SIZE)
    layout = [[graph],
              [sg.Text('Speed    Faster'), sg.Slider((0, 20), orientation='h', default_value=10, key='-SPEED-'), sg.Text('Slower')]]

    window = sg.Window('Sort Demonstration', layout, finalize=True)
    # draw the initial window's bars
    draw_bars(graph, list_to_sort)

    sg.popup('Click OK to begin Bubblesort')    # Wait for user to start it up
    bsort = bubble_sort(list_to_sort)           # get an iterator for the sort
    timeout = 10                                  # start with 10ms delays between draws
    while True:                                 # ----- The event loop -----
        event, values = window.read(timeout=timeout)
        if event == sg.WIN_CLOSED:
            break
        try:
            partially_sorted_list = bsort.__next__()
        except:
            sg.popup('Sorting done!')
            break
        graph.erase()
        draw_bars(graph, partially_sorted_list)
        timeout = int(values['-SPEED-'])

    window.close()


main()
