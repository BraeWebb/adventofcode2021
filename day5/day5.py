""""(*@ \section{Day 5: Hydrothermal Venture} @*)"""""
from collections import defaultdict

from util import *


def preprocess(stdin):
    """Pipes recorded in the form 0,9 -> 5,9"""
    for line in stdin.splitlines():
        start, _, end = line.partition(" -> ")
        sx, _, sy = start.partition(",")
        ex, _, ey = end.partition(",")
        yield (int(sx), int(sy)), (int(ex), int(ey))


""""(*@ \subsection{Task One} @*)"""""

def filter_straight(line):
    """Only straight lines pipes"""
    ((sx, sy), (ex, ey)) = line
    return sx == ex or sy == ey

def sign_of(number):
    return 1 if number > 0 else -1

def build_grid(lines):
    grid = defaultdict(int)
    for ((sx, sy), (ex, ey)) in lines:
        # distance to walk on the board
        count = max(abs(ex - sx), abs(ey - sy))

        dx = sign_of(ex - sx)
        dy = sign_of(ey - sy)

        for _ in range(count + 1):
            grid[(sx, sy)] += 1

            if sx + dx != ex + dx:
                sx += dx
            if sy + dy != ey + dy:
                sy += dy
    
    return dict(grid)


def tally_overlaps(grid):
    """Count cells with pipes > 2"""
    total = 0
    for _, pipes in grid.items():
        if pipes >= 2:
            total += 1
    return total

def task1(lines):
    lines = list(filter(filter_straight, lines))
    grid = build_grid(lines)
    return tally_overlaps(grid)


""""(*@ \subsection{Task Two} @*)"""""

def task2(lines):
    grid = build_grid(lines)
    return tally_overlaps(grid)

run(globals())
