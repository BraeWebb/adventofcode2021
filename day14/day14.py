""""(*@ \section{Day 13: Transparent Origami} @*)"""""

from util import *

def read_positions(lines):
    for line in lines:
        if line == "":
            break
        yield tuple(convert_sequence(line.split(",")))

def read_folds(lines):
    for fold in lines:
        direction, _, crease = fold.strip("fold along ").partition("=")
        yield direction, int(crease)

def preprocess(stdin):
    lines = iter(stdin.splitlines())
    
    return list(read_positions(lines)), list(read_folds(lines))

""""(*@ \subsection{Task One} @*)"""""

def copy_up(grid, row_no):
    for x, y in grid:
        if y > row_no:
            yield x, row_no - (y - row_no)
        else:
            yield (x, y)

def copy_left(grid, col_no):
    for x, y in grid:
        if x > col_no:
            yield col_no - (x - col_no), y
        else:
            yield (x, y)

def grid_string(grid, size):
    result = ""
    for x in range(size[1]):
        for y in range(size[0]):
            result += "█" if (y, x) in grid else " "
        result += "\n"
    return result


def simulate(dots, folds):
    x, y = max(dot[0] for dot in dots) + 1, max(dot[1] for dot in dots) + 1

    for direction, crease in folds:
        if direction == "x":
            dots = set(copy_left(dots, crease))
            x -= x - crease
        if direction == "y":
            dots = set(copy_up(dots, crease))
            y -= y - crease

    return dots, (x, y)

def task1(lines):
    points, folds = lines
    dots = set(points)
    dots, _ = simulate(dots, folds[:1])

    return len(dots)


""""(*@ \subsection{Task Two} @*)"""""

def task2(lines):
    points, folds = lines
    dots = set(points)
    dots, size = simulate(dots, folds)

    return grid_string(dots, size)

run(globals())
