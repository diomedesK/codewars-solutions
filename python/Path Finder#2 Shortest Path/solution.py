from queue import Queue

'''
BREADTH FIRST ALGORITHM 
Althought for tree traversal, it can be used to find the shortest 
path in scenarios where no weight is attributed to the edges)

1. Add root node to the queue, and mark it as visited(already explored).
2. Loop on the queue as long as it's not empty.
   1. Get and remove the node at the top of the queue(current).
   2. For every non-visited child of the current node, do the following: 
       1. Mark it as visited.
       2. Check if it's the goal node, If so, then return it.
       3. Otherwise, push it to the queue.
3. If queue is empty, then goal node was not found!
'''

def shortest_path(maze: list, target_position: tuple[int, int] ):
    VISITED, WALL, FREE = 'V', 'W', '.'
    queue = Queue()
    table = [list(m) for m in maze]
    traceback = { (0, 0): None }

    queue.put( (0, 0) )
    table[0][0] = VISITED

    hasFound = False


    while not queue.qsize() == 0 and not hasFound:
        position = queue.get()
        x, y = position

        new_positions = [ (x + 1, y), (x - 1, y), (x, y + 1), (x, y -1 )]
        for new_position in new_positions:
            nX, nY = new_position

            if nX < 0 or nY < 0 or nX >= len(maze) or nY >= len(maze) or table[nY][nX] in [WALL, VISITED]:
                continue

            queue.put(new_position)
            traceback[nX, nY] = position
            table[nY][nX] = VISITED

            if new_position == target_position:
                hasFound = True
                break

    if not hasFound:
        return False

    node = target_position
    path = []
    while node != (0, 0):
        node = traceback[node] #pyright: ignore
        path.append(node)

    return len(path)


def path_finder(maze):
    m = maze.split("\n")
    return shortest_path(m, ( len(m) - 1, ) * 2 )
