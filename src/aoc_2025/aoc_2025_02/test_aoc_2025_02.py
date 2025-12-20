# Tests for Advent of Code 2025 - Day 02
from src.utils.commons import import_input
from src.aoc_2025.aoc_2025_02.aoc_2025_02 import solve_part_1, solve_part_2

YEAR = 2025
DAY = 2

# Placeholder for example input data (must be defined in your actual test runner context)
example = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124""" 

def test_part_1_example():
    assert solve_part_1(example) == 1227775554   # Change 0 to the expected answer

def test_part_2_example():
    assert solve_part_2(example) == 0   # Change 0 to the expected answer

def test_part_1_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_1(input)
    print(f"Part 1 result: {result}")
    assert result == 18893502033                # Change 0 to the expected answer when ready

def test_part_2_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_2(input)
    print(f"Part 2 result: {result}")
    assert result == 0                  # Change 0 to the expected answer when ready

