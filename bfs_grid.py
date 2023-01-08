import numpy as np
from collections import deque

# For testing purposes
block_map = np.array([[1, 3, 0, 0, 0], 
                      [0, 0, 0, 0, 0], 
                      [0, 0, 3, 0, 0], 
                      [0, 0, 0, 3, 0], 
                      [0, 0, 0, 0, 2]])

# Assume sx, sy, ex, ey given (since can be taken from button pressed)
x_start = 0
y_start = 0

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