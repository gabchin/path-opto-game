# Importing neccessary libraries
from collections import deque 

# Algos
def get_prev_node(start, graph):
    # Finding the number of nodes in graph
    n = 7 # FOR NOW JUST HARD CODING

    # Initialization
    prev_node = [None]*n # Initialize list of None to keep track of final prev list
    traversed = set() # Initialize set of traversed to keep track of what node has been traversed
    
    # Adding to start of queue and marking start node as traversed
    queue = deque([start]) # Adding start node to begin queue
    traversed.add(start)

    while(queue):
        current_node = queue.popleft()

        if current_node in graph:
            next_nodes = graph[current_node]
            for next_node in next_nodes:
                if next_node not in traversed:
                    queue.append(next_node)
                    traversed.add(next_node)
                    prev_node[next_node] = current_node

    return prev_node

def reconstruct_path(start, end, prev):
    path = []
    node = end
    
    while node!= None:
        path.append(node)
        node = prev[node]

    path.reverse()

    if path[0]==start:
        return path
    return []


def find_shortest_path(start, end, graph):

    # Generating all previous node to all nodes in graph
    prev = get_prev_node(start, graph)

    # Reconstructing path from start to end node
    return reconstruct_path(start, end, prev)


# Running algo
adjacent_graph = {
    0: [1,2],
    1: [3,4],
    2: [5,6],
    4: [5]
}
s = 4
e = 5

print(find_shortest_path(s, e, adjacent_graph))