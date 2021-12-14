""""(*@ \section{Day 14: Extended Polymerization} @*)"""""

from collections import Counter
from util import *


def preprocess(stdin):
    lines = stdin.splitlines()
    template = lines[0]

    pairs = []
    for line in lines[2:]:
        match, _, replace = line.partition(" -> ")
        pairs.append((match, replace))

    return template, dict(pairs)

""""(*@ \subsection{Task One} @*)"""""

def step(polymer, pairs):
    for segment in windows(polymer, parts=2):
        segment = "".join(segment)
        if segment in pairs:
            yield segment[0] + pairs[segment]
        else:
            yield segment[0]
    
    yield polymer[-1]

def task1(lines):
    """A naive solution which constructs the string."""
    template, pairs = lines

    polymer = template
    for _ in range(10):
        polymer = "".join(list(step(polymer, pairs)))
    
    commons = Counter(polymer).most_common()

    return commons[0][1] - commons[-1][1]


""""(*@ \subsection{Task Two} @*)"""""

"""An overly complicated solution which builds a graph and DFS's to count"""

def expand_graph(graph, pairs):
    for key, value in graph.items():
        if value is not None:
            continue

        if key in pairs:
            insert = pairs[key]
            left, right = (key[0] + insert, insert + key[1])
            yield (key, (left, right))

            if left not in graph:
                yield (left, None)
            if right not in graph:
                yield (right, None)


def graph_traverser(counter, max):
    def dfs(graph, node, step):
        if step == max:
            counter[node[0]] += 1
            return

        for neighbour in graph[node]:
            dfs(graph, neighbour, step + 1)

    return dfs


def task2(lines):
    template, pairs = lines

    start_nodes = ["".join(window) for window in windows(template, parts=2)]
    graph = {key: None for key in start_nodes}

    for _ in range(10):
        graph.update(list(expand_graph(graph, pairs)))

    counter = Counter()
    traverser = graph_traverser(counter, 40)

    for node in start_nodes:
        traverser(graph, node, 0, counter)
    
    counter[template[-1]] += 1 # account for the last character

    commons = counter.most_common()

    return commons[0][1] - commons[-1][1]

# less complex solution :(

def task2(lines):
    template, pairs = lines
    
    start_nodes = ["".join(window) for window in windows(template, parts=2)]
    pair_totals = Counter(start_nodes)

    for _ in range(40):
        for key, value in pair_totals.copy().items():
            left, right = key
            replace_with = pairs[key]

            pair_totals[key] -= value
            pair_totals[left + replace_with] += value
            pair_totals[replace_with + right] += value

    counter = Counter()
    for key, value in pair_totals.items():
        counter[key[0]] += value
    
    counter[template[-1]] += 1 # account for the last character

    commons = counter.most_common()

    return commons[0][1] - commons[-1][1]

run(globals())
