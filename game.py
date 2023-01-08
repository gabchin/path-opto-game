# Importing libraries 
import tkinter as tk
import numpy as np
from collections import deque

# BFS searching algo
def bfs_shortest_path(x_start, y_start):
    # Defining row for setting grid boundary
    row = len(block_map)
    col = len(block_map[1])

    # Defining matrix for tracking explored node and parent node
    explored = np.full((row, col), False)
    parent = np.full((row, col), None)

    # Defining queues for x and y to keep track of nodes that
    # need to be explored
    x_queue = deque([x_start])
    y_queue = deque([y_start])
    explored[y_start][x_start] = True
    
    # Looping over if there is a node in the queues (meaning there are explored but unexplored node)
    while x_queue:
        # Popping from queue to get node that needs to be explored
        x = x_queue.popleft()
        y = y_queue.popleft()

        # Break when end point is found
        if block_map[y][x] == 2:
            break
        
        explore_neighbour(x, y, block_map, explored, row, col, x_queue, y_queue)
    
    return explored


def explore_neighbour(x, y, map, explored, row, col,  x_queue, y_queue):
    # Exploring neighbour of current coordinate (x, y) by up, right, down, left
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(len((dx))):
        xx = x + dx[i]
        yy = y + dy[i]

        # Seeing if move is valid
        if xx >= row or yy >= col: # Out of bounds condition.
            continue
        if xx < 0 or yy < 0: # Out of bounds condition.
            continue
        if explored[yy][xx] == True: # block is visted.
            continue
        if map[yy][xx] == 3: # Block is a brick.
            continue

        # If valid move, add to the queue for visiting.
        x_queue.append(xx)
        y_queue.append(yy)

        # Mark valid coordiate as explored.
        explored[yy][xx] = True


# Initializing window
root = tk.Tk()
# root.resizable(height=False, width=False)
root.title('Maze Path Finder')

# Initializing play area
play_area = tk.Frame(root, width=800, height=500, bg="white")
play_area.grid(row=0, column=0, padx=10, pady=10)

# Intialize array for tracking
block_map = np.zeros((10,10)) 

# Invisible 1x1 pixel to make button square
btn_img = tk.PhotoImage("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII=")

# 
x_start = -1
y_start = -1

# Defining block class for configuring 
class Block:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.value = None # value be start, stop, block or none
        self.button = tk.Button(play_area, image = btn_img, text='', bg='white', width = 50, height=50, command=self.change_block)
        self.button.grid(row=x, column=y)
    
    def reset(self):
        self.button.configure(text='', bg='white')
        self.value = None

    def change_block(self):
        self.button.configure(bg=func_colors[var.get()])
        block_map[self.x][self.y] = var.get()
        if var.get() == 1:
            global x_start 
            x_start = self.x
            global y_start 
            y_start = self.y


# Generating a grid in the play area
for x in range(10):
    for y in range(10):
        Block(x, y)


# Initializing selection area
selection_area = tk.Frame(root)
selection_area.grid(row=0, column=1, padx=10, pady=10)

var = tk.IntVar()

# Dictionary to create multiple buttons
func_values = {
    "reset" : 0,
    "start": 1,
    "stop" : 2,
    "brick" : 3
}

func_colors = {
    0: 'white',
    1: "red",
    2: "green",
    3: 'black'
}

def change_block_func():
    selection = "Block function: " + str(var.get())

for (text, value) in func_values.items():
    tk.Radiobutton(selection_area, text=text, variable=var, value=value, command=change_block_func).pack()

def find_path():
    final = bfs_shortest_path(x_start, y_start)
    print(final)

run_btn = tk.Button(selection_area, text="RUN b0ss!", command=find_path)
run_btn.pack()





root.mainloop()