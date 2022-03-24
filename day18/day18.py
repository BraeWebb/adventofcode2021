""""(*@ \section{Day 18: Snailfish} @*)"""""

import math
import sys
from util import *

def preprocess(stdin):
    for line in stdin.splitlines():
        yield eval(line) # forgive me

""""(*@ \subsection{Task One} @*)"""""

# def flatten(pairs, indexes):
#     for i, item in enumerate(pairs):
#         if isinstance(item, list):
#             yield from flatten(item, indexes + [i])
#         else:
#             yield item, indexes + [i]

# def explode(pairs):
#     # pairs = flatten(pairs, [])
#     for i, (element, index) in enumerate(pairs):
#         if len(index) >= 5:
#             if i - 1 >= 0:
#                 pairs[i - 1] = (pairs[i - 1][0] + element, pairs[i - 1][1])
#             if i + 2 < len(pairs):
#                 pairs[i + 2] = (pairs[i + 2][0] + pairs[i + 1][0], pairs[i + 2][1])
#             pairs[i] = (0, pairs[i][1][:-1])
#             del pairs[i + 1]
#             # print("after explode:", element, pairs)
#             return

# def split(pairs):
#     for i, (element, index) in enumerate(pairs):
#         if element >= 10:
#             pairs[i] = (element // 2, index + [0])
#             pairs.insert(i + 1, (math.ceil(element / 2), index + [1]))
#             # print("after split:", element, pairs)

# def reduce(pairs):
#     last = None
#     while last != pairs:
#         last = pairs[:]
#         print(reconstruct(last))
#         explode(pairs)
#         split(pairs)
        
#     return pairs
#     last = pairs[:]
#     explode(pairs)
#     split(pairs)
#     if pairs == last:
#         return pairs
#     else:
#         return reduce(pairs)

# def reconstruct(pairs):
#     # return ""
#     result = []
#     for (element, index) in pairs:
#         current = result
#         for i in index:
#             try:
#                 current = current[i]
#             except IndexError:
#                 current.insert(i, [])
#                 current = current[i]

#         current = result
#         for i in index[:-1]:
#             current = current[i]

#         current[index[-1]] = element
#     return result

class Branch:
    def __init__(self, parent: "Branch", left, right) -> None:
        self.parent = parent
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"({self.left}, {self.right})"

def build_tree(snailfish, parent):
    # parent = Branch(None)
    for i, item in enumerate(snailfish):
        if len(item) == 2 and isinstance(item[0], int) and isinstance(item[1], int):
            pair = Branch(parent, item[0], item[1])
            yield pair
        else:
            branch = Branch(parent, None, None)
            children = tuple(build_tree(item, branch))
            branch.left = children[0]
            branch.right = children[1]
            yield branch

def print_tree(root):
    print("[", end="")
    for child in root:
        if isinstance(child, Branch):
            print_tree((child.left, child.right))
        else:
            print(child, end=", ")
    print("]", end="")

def split(pair: Branch):
    if pair.parent is None:
        return
    replace_index = pair.parent.children.index(pair)
    if pair.left >= 10:
        new = Branch(pair.parent, None, None)
        new.left = Branch(new, pair.left // 2, math.ceil(pair.left / 2))
        new.right = pair.right
        pair.parent[replace_index] = new
    elif pair.right >= 10:
        new = Branch(pair.parent, None, None)
        new.left = pair.left
        new.right = Branch(new, pair.right // 2, math.ceil(pair.right / 2))
        pair.parent[replace_index] = new
    
    if isinstance(pair.left, Branch):
        split(pair.left)
    if isinstance(pair.right, Branch):
        split(pair.right)

def task1(lines):
    # sys.setrecursionlimit(100500)

    lines = list(lines)
    snailfish = lines[0]
    for line in lines[1:]:
        snailfish = [snailfish] + [line]
    # for line in lines:
    print(snailfish)

    root = None
    left, right = build_tree(snailfish, root)
    print_tree((left, right))
    split(left)
    split(right)
    print_tree((left, right))

    # line = list(flatten(snailfish, []))
    # print(reconstruct(line))
    # # try:
    # print(reconstruct(reduce(line)))
    # except:
        # print(reconstruct(line))
    # print(line)
    # print(reduce(line))
        # print(list(flatten(line, [])))


""""(*@ \subsection{Task Two} @*)"""""

def task2(target):
    pass


run(globals())
