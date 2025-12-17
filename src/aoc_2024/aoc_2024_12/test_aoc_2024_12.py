# Tests for Advent of Code 2024 - Day 12
from src.utils.commons import import_input
from src.aoc_2024.aoc_2024_12.aoc_2024_12 import solve_part_1, solve_part_2

YEAR = 2024
DAY = 12

# Placeholder for example input data (must be defined in your actual test runner context)
example = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""

def test_part_1_example():
    assert solve_part_1(example) == 1930

def test_part_2_example():
    assert solve_part_2(example) == 1206

def test_part_1_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_1(input)
    print(f"Part 1 result: {result}")
    assert result == 1546338

def test_part_2_input():
    input = import_input(year=YEAR, day=DAY)

    result = solve_part_2(input)
    print(f"Part 2 result: {result}")
    assert result == 978590

