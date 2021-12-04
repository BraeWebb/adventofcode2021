""""(*@ \section{Day 2: Dive!} @*)"""""

from util import *

def preprocess(stdin):
    """
    Each line consists of a space seperates action string and number.
    e.g. forward 10
    """
    for line in stdin.splitlines():
        action, _, amount = line.partition(" ")
        yield action, int(amount)

""""(*@ \subsection{Task One} 

Goal: Process actions by the rules. Rules:
\begin{description}
    \item[forward] increase horizontal by amount.
    \item[up] decrease depth by amount.
    \item[down] increase depth by amount.
\end{description}

Approach: The most reasonable way seems to be iterating commands and acting on a `switch' statement.
@*)"""""

def task1(commands):
    depth = 0
    horizontal = 0
    for action, amount in commands:
        if action == "forward":
            horizontal += amount
        elif action == "up":
            depth -= amount
        elif action == "down":
            depth += amount
    return horizontal * depth

""""(*@ \subsection{Task Two}

Goal: As with the last task but with different rules. Rules:
\begin{description}
    \item[forward] increase horizontal by amount and increase depth by aim times amount.
    \item[up] decrease aim by amount.
    \item[down] increase aim by amount.
\end{description}
@*)"""""

def task2(commands):
    depth = 0
    horizontal = 0
    aim = 0
    for action, amount in commands:
        if action == "forward":
            horizontal += amount
            depth += aim * amount
        elif action == "up":
            aim -= amount
        elif action == "down":
            aim += amount
    return horizontal * depth

run(globals())
