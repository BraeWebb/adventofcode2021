""""(*@ \section{Day 9: Smoke Basin} @*)"""""

from util import *

def preprocess(stdin):
    for line in stdin.splitlines():
        yield convert_sequence(line)

""""(*@ \subsection{Task One} @*)"""""

def return_or_none(lines, x, y):
    """Hack to avoid checking ranges"""
    try:
        return lines[x][y]
    except IndexError:
        return None

def get_surrounding_positions(lines, x, y):
    up = x, y - 1
    down = x, y + 1
    left = x - 1, y
    right = x + 1, y
    
    for x, y in (up, down, left, right):
        if x < 0 or y < 0: # forgot this at first :(
            continue
        if return_or_none(lines, x, y) is not None:
            yield (x, y)

def get_surrounding(lines, x, y):
    for x, y in get_surrounding_positions(lines, x, y):
        yield lines[x][y]

def find_low_points(lines):
    risks = []
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            surroundings = list(get_surrounding(lines, x, y))
            if lines[x][y] < min(surroundings):
                risks.append((x, y))
                
    return risks

def task1(lines):
    lines = list(lines)
    
    total = 0
    for x, y in find_low_points(lines):
        total += lines[x][y] + 1
    return total


""""(*@ \subsection{Task Two} @*)"""""

def search_from(grid, point):
    """Breadth first search of the grid"""
    visited = set((point,))
    queue = [point]

    while queue:
        x, y = queue.pop(0) 

        for neighbour in get_surrounding_positions(grid, x, y):
            if neighbour not in visited:
                visited.add(neighbour)
                
                # stop at hill tops
                if grid[neighbour[0]][neighbour[1]] != 9:
                    queue.append(neighbour)

    return visited


def task2(lines):
    lines = list(lines)
    
    lows = find_low_points(lines)

    basins = []
    for low in lows:
        basin = search_from(lines, low)
        
        # ignore any included hills
        basin = list(filter(lambda point: lines[point[0]][point[1]] != 9, basin))

        basins.append(len(basin))

    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]



run(globals())
