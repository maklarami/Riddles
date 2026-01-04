# Tests for Advent of Code 2025 - Day 04
from src.utils.commons import import_input
from src.aoc_2025.aoc_2025_04.aoc_2025_04 import solve_part_1, solve_part_2

YEAR = 2025
DAY = 4

# Placeholder for example input data (must be defined in your actual test runner context)
example = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

def test_part_1_example():
    assert solve_part_1(example) == 13   # Change 0 to the expected answer

def test_part_2_example():
    assert solve_part_2(example) == 43

def test_part_1_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_1(input)
    print(f"Part 1 result: {result}")
    assert result == 1344

def test_part_2_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_2(input)
    print(f"Part 2 result: {result}")
    assert result == 8112

