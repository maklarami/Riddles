# Tests for Advent of Code 2024 - Day 10
from src.utils.commons import import_input
from src.aoc_2024.aoc_2024_10.aoc_2024_10 import solve_part_1, solve_part_2

YEAR = 2024
DAY = 10

# Placeholder for example input data (must be defined in your actual test runner context)
example= """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""" 


def test_part_1_example():
    # Change 0 to the expected answer
    assert solve_part_1(example) == 36

def test_part_2_example():
    # Change 0 to the expected answer
    assert solve_part_2(example) == 81

def test_part_1_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_1(input)
    print(f"Part 1 result: {result}")
    assert result == 796

def test_part_2_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_2(input)
    print(f"Part 2 result: {result}")
    assert result == 1942

