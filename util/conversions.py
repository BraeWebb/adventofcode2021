
def convert_sequence(sequence, type=int):
    result = []
    for item in sequence:
        result.append(type(item))
    return result

def rotate(lines):
    return zip(*lines)
