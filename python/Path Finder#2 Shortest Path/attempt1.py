import sys

def move(origin, direction):
    return (origin[0] + direction[0], origin[1] + direction[1])

class Node:
    directions = [ (1, 0), (0, 1), (-1, 0), (0, -1) ]

    def __init__(self, position: tuple[int, int], parent = None):
        self.position = position
        self.parent = parent

        self.distance2root = 0 if parent is None else parent.distance2root + 1

    # def build_tree(self, maze: list[str], target_position: tuple[int, int], trip_recorder: dict ):
    def build_tree(self, maze: list[str], target_position: tuple[int, int], trip_recorder: list[ list[int|None] ] ):
        if self.position == target_position:
            return

        for direction in Node.directions:
            new_position = move(self.position, direction)

            if (new_position[0] < 0 or new_position[1] < 0 or new_position[0] >= len(maze) or new_position[1] >= len(maze) 
                or maze[new_position[0]][new_position[1]] != '.' ):
                continue

            recorded_distance = trip_recorder[new_position[0]][new_position[1]]
            
            if ( recorded_distance is None or self.distance2root + 1 < recorded_distance):
                child =  Node(position=new_position, parent=self )
                trip_recorder[new_position[0]][new_position[1]] = child.distance2root
                child.build_tree( maze=maze, target_position=target_position, trip_recorder=trip_recorder )



def path_finder(maze):  # sourcery skip: square-identity
    maze = maze.split("\n")
    N = len(maze)

    sys.setrecursionlimit(2147483647)

    reg = [ [ None if None is None else N**2 ] * N for _ in range(N) ]

    target_position = (N-1, N-1)

    root_node = Node( position=(0, 0), parent=None )
    root_node.build_tree(maze=maze, target_position=target_position, trip_recorder=reg)

    minimal = reg[target_position[0]][target_position[1]]

    return minimal if minimal != None else False

