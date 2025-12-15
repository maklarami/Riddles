# Tests for Advent of Code 2024 - Day 11
from src.utils.commons import import_input
from src.aoc_2024.aoc_2024_11.aoc_2024_11 import solve_part_1, solve_part_2

YEAR = 2024
DAY = 11

# Placeholder for example input data (must be defined in your actual test runner context)
example = "125 17" 

def test_part_1_example():
    blinks = 6
    assert solve_part_1(example, blinks) == 22 

def test_part_1_input():
    input = import_input(year=YEAR, day=DAY)
    blinks = 25
    result = solve_part_1(input, blinks)
    print(f"Part 1 result: {result}")
    assert result == 199986

def test_part_2_example():
    blinks = 6
    assert solve_part_2(example, blinks) == 22

def test_part_2_input():
    input = import_input(year=YEAR, day=DAY)
    blinks = 75
    result = solve_part_2(input, blinks)
    print(f"Part 2 result: {result}")
    assert result == 236804088748754

