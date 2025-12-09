# Tests for Advent of Code 2024 - Day 08
from src.utils.commons import import_input
from src.aoc_2024.aoc_2024_08.aoc_2024_08 import solve_part_1, solve_part_2

YEAR = 2024
DAY = 8

# Placeholder for example input data (must be defined in your actual test runner context)
example = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def test_part_1_example():
    # Change 0 to the expected answer
    assert solve_part_1(example) == 14

def test_part_2_example():
    # Change 0 to the expected answer
    assert solve_part_2(example) == 0

def test_part_1_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_1(input)
    print(f"Part 1 result: {result}")
    assert result == 301

def test_part_2_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_2(input)
    print(f"Part 2 result: {result}")
    # Change 0 to the expected answer when ready
    assert result == 0

