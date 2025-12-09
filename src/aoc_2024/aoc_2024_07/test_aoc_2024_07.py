# Tests for Advent of Code 2024 - Day 07
from src.utils.commons import import_input
from src.aoc_2024.aoc_2024_07.aoc_2024_07 import solve_part_1, solve_part_2

YEAR = 2024
DAY = 7

# Placeholder for example input data (must be defined in your actual test runner context)
example = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

def test_part_1_example():
    # Change 0 to the expected answer
    assert solve_part_1(example) == 3749

def test_part_2_example():
    # Change 0 to the expected answer
    assert solve_part_2(example) == 11387

def test_part_1_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_1(input)
    print(f"Part 1 result: {result}")
    assert result == 28730327770375

def test_part_2_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_2(input)
    print(f"Part 2 result: {result}")
    # Change 0 to the expected answer when ready
    assert result == 424977609625985

