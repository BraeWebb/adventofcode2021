from itertools import tee


def break_into_parts(sequence, parts=1):
    iters = tee(sequence, parts)
    for i in range(1, parts):
        for each in iters[i:]:
            next(each, None)
    yield from zip(*iters)
    # for i in range(len(sequence) - parts - 1):
    #     yield tuple(sequence[i + di] for di in range(parts))


def caching_enumerate(sequence):
    last = None
    for item in sequence:
        if last is not None:
            yield last, item

        last = item
