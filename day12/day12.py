""""(*@ \section{Day 12: Passage Pathing} @*)"""""

from typing import List
from util import *


def preprocess(stdin):
    for line in stdin.splitlines():
        yield line.split("-")

""""(*@ \subsection{Task One} @*)"""""

class Graph:
    def __init__(self, stopping_condition) -> None:
        self._lines = []
        self._stopping_condition = stopping_condition

    def add_line(self, start, end):
        self._lines.append((start, end))
        self._lines.append((end, start))

    def get_nexts(self, from_) -> List[str]:
        for start, end in self._lines:
            if from_ == start:
                yield end

    def find_paths_from(self, start, path, seen):
        for next in self.get_nexts(start):
            # path finished, yield it
            if next == "end":
                yield path + ("end",)

            # task specific rules for stopping
            if self._stopping_condition(seen, next):
                continue
            
            # update seen dictionary to add one to the next
            now_seen = dict(seen, **{next: seen.get(next, 0) + 1})

            # find all paths to 'end' from here
            next_path = path + (next,)
            yield from self.find_paths_from(next, next_path, now_seen)

    def find_all_paths(self):
        path_generator = self.find_paths_from(
            "start",
            ("start",),
            {"start": 1}
        )

        return set(path for path in path_generator)


def visit_small_once(seen, next):
    if next in ("start", "end"):
        return True
    
    return next.islower() and next in seen

def task1(lines):
    graph = Graph(visit_small_once)
    for line in lines:
        graph.add_line(*line)

    return len(graph.find_all_paths())


""""(*@ \subsection{Task Two} @*)"""""

def visit_small_twice(seen, next):
    if next in ("start", "end"):
        return True
    
    if next.islower() and next in seen:
        for cave, visited in seen.items():
            if cave.islower() and visited > 1:
                return True
    
    return False

def task2(lines):
    graph = Graph(visit_small_twice)
    for line in lines:
        graph.add_line(*line)

    return len(graph.find_all_paths())


run(globals())
