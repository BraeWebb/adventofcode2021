""""(*@ \section{Day 6: Lanternfish} @*)"""""

from util import *


def preprocess(stdin):
    return convert_sequence(stdin.splitlines()[0].split(","))


""""(*@ \subsection{Task One} @*)"""""

def generate(fishes):
    """Yield the next generation of fishes from the current."""
    for fish in fishes:
        if fish == 0:
            yield 6
            yield 8
        else:
            yield fish - 1



def task1(lines):
    """Naive simulation"""
    state = lines
    
    for _ in range(80):
        state = list(generate(state))
    
    return len(state)


""""(*@ \subsection{Task Two} @*)"""""

def task2(lines):
    """
    Smarter bucket based simulating.
    Tallying fish in buckets of respawn time.
    """
    buckets = [0] * 9
    for fish in lines:
        buckets[fish] += 1

    for _ in range(256):
        reproducing = buckets.pop(0)
        buckets.append(reproducing) # spawn kids
        buckets[6] += reproducing # reset itself to 6 away from reproduction

    return sum(buckets)

run(globals())
