# Tests for Advent of Code 2024 - Day 06
from src.utils.commons import import_input
from src.aoc_2024.aoc_2024_06.aoc_2024_06 import solve_part_1, solve_part_2

YEAR = 2024
DAY = 6

# Placeholder for example input data (must be defined in your actual test runner context)
example = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""" 

def test_part_1_example():
    # Change 0 to the expected answer
    assert solve_part_1(example) == 41

def test_part_2_example():
    # Change 0 to the expected answer
    assert solve_part_2(example) == 6

def test_part_1_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_1(input)
    print(f"Part 1 result: {result}")
    # Change 0 to the expected answer when ready
    assert result == 4647

def test_part_2_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_2(input)
    print(f"Part 2 result: {result}")
    assert result == 1723

