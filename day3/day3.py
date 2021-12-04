""""(*@ \section{Day 3: Binary Diagnostic} @*)"""""

from collections import Counter

from util import *

def preprocess(stdin):
    return stdin.splitlines()

""""(*@ \subsection{Task One} @*)"""""

def max_bit(bit_array, tie_value=1):
    rates = Counter(bit_array)

    # break a tie
    if rates["0"] == rates["1"]:
        return tie_value
    
    return rates.most_common(1)[0][0]


def gamma_rate(lines):
    columns = rotate(lines)

    for column in columns:
        yield max_bit(column)


def byte_array_to_int(byte_array):
    return int("".join(byte_array), 2)


def flip_bits(byte, bit_width):
    return ~byte & ((2 ** bit_width) - 1)


def task1(lines):
    gamma = byte_array_to_int(gamma_rate(lines))

    bit_width = len(bin(gamma)) - 2
    epsilon = flip_bits(gamma, bit_width)

    return gamma * epsilon


""""(*@ \subsection{Task Two} @*)"""""

def oxygen_filter(bits, row):
    most = max_bit(bits, tie_value="1")
    return bits[row] == most

def co2_filter(bits, row):
    most = max_bit(bits, tie_value="1")
    return bits[row] != most


def filter_rows(lines, filter_func):
    remaining = lines[:]

    for column in range(len(lines[0])):
        bits = []
        for line in remaining:
            bits.append(line[column])
        
        for i, line in enumerate(remaining[:]):
            if not filter_func(bits, i):
                remaining.remove(line)

        if len(remaining) == 1:
            return remaining[0]

def task2(lines):
    oxygen_rating = filter_rows(lines, oxygen_filter)
    co2_rating = filter_rows(lines, co2_filter)

    return int(oxygen_rating, 2) * int(co2_rating, 2)

run(globals())
