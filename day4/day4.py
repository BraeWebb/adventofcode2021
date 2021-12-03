import sys
from util import *

from collections import Counter


def preprocess(stdin):
    return convert_sequence(stdin.splitlines())


def run(stdin):
    # yield task1(preprocess(stdin))
    # yield task2(preprocess(stdin))
    yield from ()


if __name__ == "__main__":
    results = run(sys.stdin.read())
    for result in results:
        print(result)

    run_tests(globals())
