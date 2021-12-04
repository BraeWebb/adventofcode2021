""""(*@ \section{Day 1: Sonar Sweep} @*)"""""

from util import *

def preprocess(stdin):
    """Convert lines into a list of integers."""
    return convert_sequence(stdin.splitlines(), int)

""""(*@
\subsection{Task One}

Goal: Calculate how many times a successive value in a series of values increments.\\

Approach: Use \texttt{caching\_enumerate} which keep track of the previous value during iteration of a sequence.\,
Then if the current value is great or equal to the last, increments the total seen.
@*)"""""

def task1(lines):
    total = 0
    for last, current in caching_enumerate(lines):
        if last < current:
            total += 1
    return total

""""(*@
\subsection{Task Two} 

Goal: Calculate how many times the sum of a successive overlapping window of three within a sequence increments.\\

Approach: Break the sequence into overlapping windows of size 3 with \texttt{break\_into\_parts}.\,
Then use the same approach as task one but using the sum of the window to detect an increment.
@*)"""""

def task2(lines):
    total = 0
    parts = windows(lines, parts=3)
    for last, current in caching_enumerate(parts):
        if sum(last) < sum(current):
            total += 1
    return total

run(globals())
