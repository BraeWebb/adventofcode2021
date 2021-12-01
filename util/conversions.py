
def convert_sequence(sequence, type=int):
    for item in sequence:
        yield type(item)
