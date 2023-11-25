import sys
def path_finder(maze):
    sys.setrecursionlimit(2147483647)
    directions = [ [-1, +0], [+1, +0], [+0, -1], [+0, +1] ]

    maze = maze.split('\n')
    N = len(maze)

    def move(direction, origin):
        return [ x + y for x, y in zip(direction, origin) ] 

    been_positions = []
    didAchieve = False
    def mv( current_pos, goal_position ):
        nonlocal didAchieve

        if current_pos == goal_position:
            didAchieve = True

        been_positions.append(current_pos)

        for direction in directions:
            new_pos = move(direction, current_pos)
            if  new_pos[0] >= 0 and new_pos[0] < N and new_pos[1] >= 0 and new_pos[1] < N:
                if maze[new_pos[1]][new_pos[0]] != 'W' and not new_pos in been_positions and not didAchieve:
                    mv(new_pos, goal_position)

    mv([0, 0], [N-1, N-1])

    return didAchieve 

