""""(*@ \section{Day 15: Chiton} @*)"""""

from queue import PriorityQueue

from util import *

def preprocess(stdin):
    for line in stdin.splitlines():
        yield convert_sequence(line)

""""(*@ \subsection{Task One} @*)"""""

def return_or_none(lines, x, y):
    """Hack to avoid checking ranges"""
    try:
        return lines[x][y]
    except IndexError:
        return None

def get_surrounding_positions(lines, x, y):
    up = x, y - 1
    down = x, y + 1
    left = x - 1, y
    right = x + 1, y
    
    for x, y in (up, down, left, right):
        if x < 0 or y < 0:
            continue
        if return_or_none(lines, x, y) is not None:
            yield (x, y)


# my dijkstra is pretty rusty but seems to do the trick
def dijkstra(graph, start=(0, 0)):
    risks = {(x, y):float('inf') for x, row in enumerate(graph) for y, _ in enumerate(row)}
    risks[start] = 0

    queue = PriorityQueue()
    queue.put((0, start))

    visited = set()

    parents = {}

    while not queue.empty():
        (_, node) = queue.get()
        visited.add(node)
        x, y = node

        for dx, dy in get_surrounding_positions(graph, x, y):
            if (dx, dy) in visited:
                continue

            risk = graph[dx][dy]
            old_total_risk = risks[(dx, dy)] # old risk to get to this node
            new_total_risk = risks[node] + risk # new risk to get there through this node

            if new_total_risk < old_total_risk:
                queue.put((new_total_risk, (dx, dy)))

                # better to go through this node to get to dx dy
                risks[(dx, dy)] = new_total_risk
                parents[(dx, dy)] = (x, y)

    return risks, parents


def task1(lines):
    cave = list(lines)
    risks, _ = dijkstra(cave)

    destination = (len(cave) - 1, len(cave[0]) - 1)
    return risks[destination]


""""(*@ \subsection{Task Two} @*)"""""

def wrap(number, k=10):
    # mod doesn't work for wrap to one, assume only increments by one
    return 1 if number >= k else number

def extend_map(graph, magnitude):
    width = len(graph)

    # expand across
    for x in range(magnitude - 1):
        for row_index, row in enumerate(graph):
            # chop row on segment to copy
            row = row[x*width:(x+1)*width]
            graph[row_index] += [wrap(val + 1) for val in row]

    # expand down
    for x in range(magnitude - 1):
        for row_index, row in enumerate(graph[x*width:(x+1)*width]):
            graph.append([wrap(val + 1) for val in row])

    return graph

def task2(lines):
    cave = extend_map(list(lines), 5)
    risks, _ = dijkstra(cave)

    destination = (len(cave) - 1, len(cave[0]) - 1)
    return risks[destination]

run(globals())
