""""(*@ \section{Day 10: Syntax Scoring} @*)"""""

from util import *

def preprocess(stdin):
    return stdin.splitlines()

""""(*@ \subsection{Task One} @*)"""""

MATCHING = {
    "[": "]",
    "{": "}",
    "(": ")",
    "<": ">",
}

SYNTAX_POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

OPENING = MATCHING.keys()
CLOSING = SYNTAX_POINTS.keys()

def parse_line(line):
    """
    Parse a line.
    Returns the remaining characters to be closed and the error char or None if incomplete.
    """
    stack = []
    for char in line:
        # add opening to stack
        if char in OPENING:
            stack.append(char)
        
        # remove opening from stack
        elif char in CLOSING:
            last = stack.pop() # matching open
            expected = MATCHING.get(last, None)
            if expected != char: # mismatched closing
                return stack, char

    return stack, None


def task1(lines):
    points = 0
    for line in lines:
        error_char = parse_line(line)[1] # mismatched char or None
        if error_char is not None:
            points += SYNTAX_POINTS[error_char]
    return points


""""(*@ \subsection{Task Two} @*)"""""

COMPLETION_POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

def complete(stack):
    """Finish a line."""
    for opening in stack:
        yield MATCHING[opening]

def task2(lines):
    lines = map(parse_line, lines)
    lines = filter(lambda line: line[1] is None, lines) # filter mismatches
    
    line_scores = []
    for line in lines:
        to_complete = reversed(list(complete(line[0])))

        points = 0
        for char in to_complete:
            points *= 5
            points += COMPLETION_POINTS[char]
        
        line_scores.append(points)
    
    line_scores.sort()
    return line_scores[len(line_scores)//2]


run(globals())
