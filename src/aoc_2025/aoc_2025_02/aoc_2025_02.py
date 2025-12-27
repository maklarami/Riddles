# Advent of Code 2025 - Day 02 solution

import math


def solve_even_range(start, end, length) -> int:
    sum = 0

    start_int = int(start)
    end_int = int(end)

    start_first = start[:length//2]
    start_first_int = int(start_first)
    check = int(start_first + start_first)
    while check <= end_int:
        if start_int <= check:
            sum += check
        start_first_int += 1
        start_first = str(start_first_int)
        check = int(start_first + start_first)

    return sum

def solve_range(start: str, end: str) -> int:
    sum = 0
    num_chars = len(start)

    if num_chars != len(end):
        new_start = "".join(["1"]+["0"]*num_chars)
        sum += solve_range(new_start, end)
        end = "".join(["9"]*num_chars)
    
    if num_chars % 2 == 1:
        return sum
    
    sum += solve_even_range(start, end, num_chars)
    return sum

def solve_range_for_denominator(start: str, end:str, length: int, denom: int) -> set[int]:
    myset = set()

    start_int = int(start)
    end_int = int(end)

    start_first = start[:length//denom]
    start_first_int = int(start_first)
    check = int(start_first * denom)
    while check <= end_int:
        if start_int <= check:
            myset.add(check)
        start_first_int += 1
        start_first = str(start_first_int)
        check = int(start_first * denom)

    return myset

def solve_range_2(start: str, end: str) -> int:
    my_sum = 0
    num_chars = len(start)

    if num_chars != len(end):
        new_start = "".join(["1"]+["0"]*num_chars)
        my_sum += solve_range_2(new_start, end)
        end = "".join(["9"]*num_chars)
    
    denominators = [i for i in range(2, num_chars +1) if num_chars % i == 0]
    numbers = set()
    for i in denominators:
        numbers.update(solve_range_for_denominator(start, end, num_chars, i))
    my_sum += sum(numbers)   
    
    return my_sum

def solve_part_1(input : str) -> int:
    ranges = [part.split("-") for part in input.strip().split(",")]
    sum = 0

    for range in ranges:
        sum += solve_range(range[0], range[1])

    return sum

def solve_part_2(input : str) -> int:
    ranges = [part.split("-") for part in input.strip().split(",")]
    sum = 0

    for range in ranges:
        sum += solve_range_2(range[0], range[1])

    return sum

if __name__ == "__main__":
    print(solve_part_1("9959142-10053234"))
