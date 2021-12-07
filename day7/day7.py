""""(*@ \section{Day 7: The Treachery of Whales} @*)"""""

from util import *


def preprocess(stdin):
    return convert_sequence(stdin.splitlines()[0].split(","))


""""(*@ \subsection{Task One} @*)"""""


def calculate_fuel(lines, line):
    total = 0
    for crab in lines:
        total += abs(line - crab)
    return total

def find_best(lines, measure):
    fuels = []
    for i in range(max(lines)):
        fuels.append(measure(lines, i))
    return min(fuels)

def task1(lines):
    return find_best(lines, calculate_fuel)


""""(*@ \subsection{Task Two} @*)"""""

def calculate_dynamic_fuel(lines, line):
    total = 0
    for crab in lines:
        total += sum(range(abs(line - crab) + 1)) # this is a bit slow
    return total

def task2(lines):
    return find_best(lines, calculate_dynamic_fuel)


run(globals())
