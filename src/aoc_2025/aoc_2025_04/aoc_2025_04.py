# Advent of Code 2025 - Day 04 solution


import numpy as np
import scipy.ndimage as ndimage

def less_than_4_neighbours(x) -> int:
    if x[4] == 0:
        return 0
    else:
        if sum(x)-1 < 4:
            return 1
        else:
            return 0

def solve_part_1(input : str) -> int:
    f = lambda x: 1 if x == '@' else 0
    map = np.array([[f(char) for char in line] for line in input.strip().splitlines()])
    result = ndimage.generic_filter(map, less_than_4_neighbours, size = (3,3), mode = 'constant', cval = 0)
    return np.sum(result)


def solve_part_2(input : str) -> int:
    f = lambda x: 1 if x == '@' else 0
    map = np.array([[f(char) for char in line] for line in input.strip().splitlines()])
    removed = 0
    new_removed = 1

    while new_removed != 0:
        result = ndimage.generic_filter(map, less_than_4_neighbours, size = (3,3), mode = 'constant', cval = 0)

        new_removed = np.sum(result)
        removed += new_removed

        map -= result

    return removed

if __name__ == "__main__":
    pass