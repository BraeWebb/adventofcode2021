""""(*@ \section{Day 16: Packet Decoder} @*)"""""

from functools import reduce

from util import *

HEXS = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

def unhex(hex):
    def convert(hex):
        for char in hex:
            yield HEXS[char]

    return "".join(convert(hex))

def preprocess(stdin):
    first_line = stdin.splitlines()[0]
    return unhex(first_line)

""""(*@ \subsection{Task One} @*)"""""

def read(iterator, amount):
    result = ""
    for _ in range(amount):
        try:
            result += next(iterator)
        except StopIteration:
            raise Exception("Packet finished before being decoded")
    return result

def binary(bits):
    return int(bits, 2)


def decode_value_packet(tokens):
    bits = []
    while True:
        part = read(tokens, 5)
        bits.append(part[1:])

        if part[0] == "0":
            break
    
    return binary("".join(bits))

def decode_fixed_length_subpackets(tokens):
    length = binary(read(tokens, 15))
    subpackets = read(tokens, length)

    while subpackets:
        packet, remaining = decode_packet(subpackets)
        yield packet
        subpackets = "".join(remaining)

def decode_fixed_amount_subpackets(tokens):
    packets = binary(read(tokens, 11))

    for _ in range(packets):
        packet, tokens = decode_packet(tokens)
        yield packet


def decode_packet(line):
    tokens = iter(line)
    version = binary(read(tokens, 3))
    type_id = binary(read(tokens, 3))

    if type_id == 4:
        return (version, type_id, decode_value_packet(tokens)), tokens

    length_type_id = binary(read(tokens, 1))

    if length_type_id == 0:
        return (version, type_id, list(decode_fixed_length_subpackets(tokens))), tokens

    if length_type_id == 1:
        return (version, type_id, list(decode_fixed_amount_subpackets(tokens))), tokens

    return Exception("Unknown packet header")


def versions(packet):
    yield packet[0]

    if isinstance(packet[-1], list):
        for p in packet[-1]:
            yield from versions(p)

def task1(header):
    packets, _ = decode_packet(header)

    return sum(versions(packets))


assert task1(unhex("8A004A801A8002F478")) == 16
assert task1(unhex("620080001611562C8802118E34")) == 12
assert task1(unhex("C0015000016115A2E0802F182340")) == 23
assert task1(unhex("A0016C880162017C3686B18A3D4780")) == 31


""""(*@ \subsection{Task Two} @*)"""""

def perform_operator(type_id, packets):
    if type_id == 0:
        return sum(packets)
    elif type_id == 1:
        return reduce(lambda x, y: x * y, packets, 1)
    elif type_id == 2:
        return min(packets)
    elif type_id == 3:
        return max(packets)
    elif type_id == 4:
        return packets
    elif type_id == 5:
        return 1 if packets[0] > packets[1] else 0
    elif type_id == 6:
        return 1 if packets[0] < packets[1] else 0
    elif type_id == 7:
        return 1 if packets[0] == packets[1] else 0

def fold(packet):
    if isinstance(packet[-1], list):
        return perform_operator(packet[1], [fold(p) for p in packet[-1]])
    else:
        return packet[-1]

def task2(header):
    packets, _ = decode_packet(header)

    return fold(packets)

assert task2(unhex("C200B40A82")) == 3
assert task2(unhex("04005AC33890")) == 54
assert task2(unhex("880086C3E88112")) == 7
assert task2(unhex("CE00C43D881120")) == 9
assert task2(unhex("D8005AC2A8F0")) == 1
assert task2(unhex("F600BC2D8F")) == 0
assert task2(unhex("9C005AC2F8F0")) == 0
assert task2(unhex("9C0141080250320F1802104A08")) == 1

run(globals())
