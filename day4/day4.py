from collections import defaultdict
import itertools
import sys
from typing import Dict, List, Tuple
from dataclasses import dataclass

from util import *


GRID_SIZE = 5


@dataclass
class Board:
    board_number: int
    rows: List[List[int]]
    marks: Dict[Tuple[int, int], Tuple[int, bool]]

    def iterate(self, f):
        for x in range(GRID_SIZE):
            row = []
            for y in range(GRID_SIZE):
                row.append(f(x, y))
            yield row

    def mark(self, x, y):
        self.marks[(x, y)] = True

    def all_marks(self):
        yield from self.iterate(lambda x, y: self.marks[(x, y)])

    def all_numbers(self):
        yield from self.iterate(lambda x, y: self.rows[x][y])

    def all(self):
        yield from itertools.chain(*self.iterate(lambda x, y: (self.rows[x][y], self.marks[(x, y)])))


@dataclass
class Bingo:
    numbers: List[int]
    boards: List[Board]


def parse_called_numbers(source) -> List[int]:
    sequence = next(source).split(",")
    return convert_sequence(sequence, int)


def parse_board_row(line) -> List[int]:
    return convert_sequence(line.split(), int)


def parse_board(source, board_number) -> Board:
    rows = []

    while True:
        line = next(source, None)
        if line == "": # ignore blank lines
            continue

        rows.append(parse_board_row(line))

        if len(rows) == GRID_SIZE:
            break
        
    return Board(board_number, rows, defaultdict(lambda : False))


def preprocess(stdin):
    lines = iter(stdin.splitlines())
    
    numbers = parse_called_numbers(lines)

    boards = []
    while True:
        boards.append(parse_board(lines, len(boards)))

        blank_line = next(lines, None) # ignores blank
        if blank_line is None:
            break

    return Bingo(numbers, boards)


def is_won(board: Board):
    horizontal = board.all_marks()
    for row in horizontal:
        if all(row):
            return True

    vertical = rotate(board.all_marks())
    for column in vertical:
        if all(column):
            return True

    return False


def tally_points(board: Board):
    count = 0

    parts = board.all()
    for number, marked in parts:
        if not marked:
            count += number

    return count


def mark_number(number, boards: List[Board]):
    for board in boards:
        for x, row in enumerate(board.rows):
            for y, column in enumerate(row):
                if column == number:
                    board.mark(x, y)

        if is_won(board):
            yield board

def task1(bingo: Bingo):
    for number in bingo.numbers:
        winner = next(mark_number(number, bingo.boards), None)
        if winner is not None:
            return tally_points(winner) * number


def task2(bingo: Bingo):
    winners = set()
    wins = []
    for number in bingo.numbers:
        round_winners = list(mark_number(number, bingo.boards))

        for winner in round_winners:
            if winner.board_number not in winners:
                bingo.boards.remove(winner) # stop marking
                wins.append((winner, number))
                winners.add(winner.board_number)
    
    last_board, last_number = wins[-1]
    return tally_points(last_board) * last_number


def run(stdin):
    # yield task1(preprocess(stdin))
    # yield task2(preprocess(stdin))
    yield from ()


if __name__ == "__main__":
    results = run(sys.stdin.read())
    for result in results:
        print(result)

    run_tests(globals())
