""""(*@ \section{Day 17: Trick Shot} @*)"""""

from util import *

def preprocess(stdin):
    line = stdin.splitlines()[0]
    line = line.strip("target area: ")
    x, _, y = line.partition(", ")
    x1, _, x2 = x.strip("x=").partition("..")
    y1, _, y2 = y.strip("y=").partition("..")

    return (int(x1), int(x2)), (int(y1), int(y2))

""""(*@ \subsection{Task One} @*)"""""

def lower_target(target):
    return min(target[1])

def task1(target):
    minimum = lower_target(target)
    return minimum * (minimum + 1) // 2


""""(*@ \subsection{Task Two} @*)"""""

def is_in_target(position, target):
    if position[0] < target[0][0] or position[0] > target[0][1]:
        return False
    if position[1] < target[1][0] or position[1] > target[1][1]:
        return False
    return True

def step(position, acceleration, target):
    minimum = lower_target(target)
    x, y = position
    dx, dy = acceleration
    while y >= minimum:
        x += dx
        y += dy
        if dx != 0:
            dx = dx - 1 if dx > 0 else dx + 1
        dy -= 1

        if is_in_target((x, y), target):
            return True

    return False

def hitting_angles(target):
    (x1, x2), (y1, y2) = target
    for dx in range(0, max(x2, 0) + 1):
        for dy in range(y1, abs(y2) * 2 + 1):
            enters = step((0, 0), (dx, dy), target)
            if enters:
                yield dx, dy

def task2(target):
    count = 0
    for _ in hitting_angles(target):
        count += 1
    return count


run(globals())
