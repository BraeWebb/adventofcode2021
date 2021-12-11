""""(*@ \section{Day 11: Dumbo Octopus} @*)"""""

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
    positions = [(dx, dy) 
                    for dx in range(x-1, x+2) 
                    for dy in range(y-1, y+2) 
                    if (dx,dy) != (x,y)]
    
    for x, y in positions:
        if x < 0 or y < 0:
            continue
        if return_or_none(lines, x, y) is not None:
            yield (x, y)

def flash(octopuses, flashes, position):
    x, y = position

    # can only flash once
    if (x,y) in flashes:
        return

    energy = octopuses[x][y]
    if energy > 9:
        flashes.add((x, y))

        for (dx, dy) in get_surrounding_positions(octopuses, x, y):
            octopuses[dx][dy] += 1
            flash(octopuses, flashes, (dx, dy))

def step(octopuses):
    flashes = set()
    # increment first
    for x, row in enumerate(octopuses):
        for y, _ in enumerate(row):
            octopuses[x][y] += 1

    # flash after
    for x, row in enumerate(octopuses):
        for y, _ in enumerate(row):
            flash(octopuses, flashes, (x, y))

    # zero out last
    for x, y in flashes:
        octopuses[x][y] = 0

    return flashes


def task1(lines):
    lines = list(lines)

    total = 0
    for _ in range(100):
        total += len(step(lines))

    return total


""""(*@ \subsection{Task Two} @*)"""""

def task2(lines):
    lines = list(lines)
    size = len(lines) * len(lines[0])

    i = 1
    while True:
        if len(step(lines)) == size:
            return i
        
        i += 1


run(globals())
