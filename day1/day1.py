import sys
from util import *


def task1(lines):
    total = 0
    for last, current in caching_enumerate(lines):
        if current >= last:
            total += 1
    return total


def task2(lines):
    total = 0
    parts = break_into_parts(lines, parts=3)
    for last, current in caching_enumerate(parts):
        if sum(current) > sum(last):
            total += 1
    return total


def preprocess(stdin):
    return convert_sequence(stdin.splitlines())


def run(stdin):
    yield task1(preprocess(stdin))
    yield task2(preprocess(stdin))


if __name__ == "__main__":
    results = run(sys.stdin.read())
    for result in results:
        print(result)

    run_tests(globals())
