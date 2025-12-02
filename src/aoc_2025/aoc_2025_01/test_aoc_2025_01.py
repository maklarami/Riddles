# Tests for Advent of Code 2025 - Day 01
from src.utils.commons import import_input
from src.aoc_2025.aoc_2025_01.aoc_2025_01 import solve_part_1, solve_part_2, solve_part_2_HL, solve_part_2_KM

YEAR = 2025
DAY = 1

# Placeholder for example input data (must be defined in your actual test runner context)
example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""" 

def test_part_1_example():
    # Change 0 to the expected answer
    assert solve_part_1(example) == 3

def test_part_2_example():
    # Change 0 to the expected answer
    assert solve_part_2_KM(example) == 6

def test_part_1_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_1(input)
    print(f"Part 1 result: {result}")
    # Change 0 to the expected answer when ready
    assert result == 1152 

def test_part_2_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_2(input)
    print(f"Part 2 result: {result}")
    # Change 0 to the expected answer when ready
    assert result == 6671

