import sys
from util import *


def task1(commands):
    depth = 0
    hoz = 0
    for command in commands:
        action, _, amount = command.partition(" ")
        if action == "forward":
            hoz += int(amount)
        elif action == "up":
            depth -= int(amount)
        elif action == "down":
            depth += int(amount)
    return hoz * depth


def task2(commands):
    depth = 0
    hoz = 0
    aim = 0
    for command in commands:
        action, _, amount = command.partition(" ")
        if action == "forward":
            hoz += int(amount)
            depth += aim * int(amount)
        elif action == "up":
            aim -= int(amount)
        elif action == "down":
            aim += int(amount)
    return hoz * depth

def preprocess(stdin):
    return stdin.splitlines()


def run(stdin):
    yield task1(preprocess(stdin))
    yield task2(preprocess(stdin))
    yield from ()


if __name__ == "__main__":
    results = run(sys.stdin.read())
    for result in results:
        print(result)

    run_tests(globals())
