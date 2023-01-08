import numpy as np
from collections import deque

"""
Block Types
0: empty
1: start
2: end
3: brick
"""

# For testing purposes
block_map = np.array([[1, 3, 0, 0, 0], [0, 3, 0, 0, 0], [0, 0, 3, 0, 0], [0, 0, 0, 3, 0], [0, 0, 0, 0, 2]])



# Assume sx, sy, ex, ey given (since can be taken from button pressed)
x_start = 0
y_start = 0
x_end = 4
y_end = 4

# Algo start
row = len(block_map)
col = len(block_map[1])

visited = np.full((row, col), False)
#prev_node = [[None]*row for i in range(col)]
x_queue = deque([x_start])
y_queue = deque([y_start])
visited[y_start][x_start] = True

while x_queue:
    # Popping from queue and indicate it has been visited
    x = x_queue.popleft()
    y = y_queue.popleft()

    print(visited)
    print()

    if block_map[y][x] == 2:
        visited[y][x] = True
        print("TA DA!")
        break

    # Exploring neighbour of current coordinate (x, y) by up, right, down, left
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    

    for i in range(len((dx))):

        xx = x + dx[i]
        yy = y + dy[i]


        # Seeing if move is valid
        # Out of bounds
        if xx >= row or yy >= row: 
            # print(f"out of bounds {xx}, {yy}")
            continue
        if xx < 0 or yy < 0: 
            # print(f"out of bounds {xx}, {yy}")
            continue
        # block is visted or a brick
        if visited[yy][xx] == True:
            # print(f"visited {xx}, {yy}")
            continue
        if block_map[yy][xx] == 3:
            # print(f"blocked {xx}, {yy}")
            continue

        # If valid move, add to the queue
        x_queue.append(xx)
        y_queue.append(yy)

        visited[yy][xx] = True
    

        

    
  






