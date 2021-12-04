from .iterations import *
from .conversions import *
from .test import *


def main(state):
    preprocess = state.get("preprocess", lambda x: x)
    task1 = state.get("task1", lambda x: None)
    task2 = state.get("task2", lambda x: None)

    stdin = sys.stdin.read()
    
    yield task1(preprocess(stdin))
    yield task2(preprocess(stdin))
    yield from ()


def run(state):
    name = state.get("__name__")

    if name == "__main__":
        for result in main(state):
            print(result)

        run_tests(state)

    

__all__ = [
    "windows",
    "caching_enumerate",
    "convert_sequence",
    "rotate",
    "run_tests",
    "run",
]