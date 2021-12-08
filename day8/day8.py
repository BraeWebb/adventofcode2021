""""(*@ \section{Day 8: Seven Segment Search} @*)"""""

from util import *

def preprocess(stdin):
    for line in stdin.splitlines():
        input, output = line.split(" | ")
        yield (input.split(" "), output.split(" "))

""""(*@ \subsection{Task One} @*)"""""

def has_unique_length(segment):
    """1, 4, 7, 8"""
    size = len(segment)
    return size in (2, 4, 3, 7)

def task1(lines):
    total = 0
    for _, output_values in lines:
        for segment in output_values:
            if has_unique_length(segment):
                total += 1
    return total


""""(*@ \subsection{Task Two} @*)"""""

from constraint import *

SEGMENTS = {
    0: set("abcefg"),
    1: set("cf"),
    2: set("acdeg"),
    3: set("acdfg"),
    4: set("bcdf"),
    5: set("abdfg"),
    6: set("abdefg"),
    7: set("acf"),
    8: set("abcdefg"),
    9: set("abcdfg")
}

def convert(solution, segment):
    """Uncross wires in a segment for a solution"""
    return set(solution[char] for char in segment)

def get_digit(on):
    """Digit corresponding to a set of on signals"""
    for digit, signal in SEGMENTS.items():
        if on == signal:
            return digit

def constraint_rule(segment):
    """Constraint rules for known segment lengths"""
    size = len(segment)
    if size == 2:
        return lambda *args: set(args) == SEGMENTS[1]
    if size == 4:
        return lambda *args: set(args) == SEGMENTS[4]
    if size == 3:
        return lambda *args: set(args) == SEGMENTS[7]
    if size == 7:
        return lambda *args: set(args) == SEGMENTS[8]


def validate_solution(segments, solution):
    """Ensure all segments for a solution have a digit"""
    for segment in segments:
        on = convert(solution, segment)
        digit = get_digit(on)

        if digit is None:
            return False

    return True

def find_solution(solutions, line):
    for solution in solutions:
        if validate_solution(line[0], solution):
            return solution

def solve_line(line):
    variables = list("abcdefg")

    problem = Problem()
    problem.addVariables(variables, variables)

    for segment in line[0]:
        contraint = constraint_rule(segment)
        if contraint is not None:
            problem.addConstraint(contraint, variables=list(segment))
    
    solutions = problem.getSolutions()
    solution = find_solution(solutions, line)

    number = ""
    for segment in line[1]:
        on = convert(solution, segment)
        digit = get_digit(on)
        number += str(digit)

    return int(number)
    
def task2(lines):
    results = []
    for line in lines:
        results.append(solve_line(line))

    return sum(results)

run(globals())
